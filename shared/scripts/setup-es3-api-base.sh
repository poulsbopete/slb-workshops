#!/bin/bash
# Shared SLB workshop bootstrap — provisions Elastic Observability Serverless
# and proxies Kibana on :8080. Workshop-specific seeding runs in challenge setup.
#
# Usage (from track track_scripts/setup-es3-api):
#   export WORKSHOP_SEED_SCRIPT=/opt/slb-workshops/shared/seeds/sample-otel.sh  # optional
#   bash /opt/slb-workshops/shared/scripts/setup-es3-api-base.sh

set -euxo pipefail

PME_CLOUD_INSTRUQT_API_KEY="${ESS_CLOUD_API_KEY:-}"
if [ -z "${PME_CLOUD_INSTRUQT_API_KEY:-}" ]; then
  PME_CLOUD_INSTRUQT_API_KEY="$(agent variable get ESS_CLOUD_API_KEY 2>/dev/null || echo "")"
fi
if [ -z "${PME_CLOUD_INSTRUQT_API_KEY:-}" ]; then
  echo "ERROR: Cloud API key not set. Configure Instruqt secret ESS_CLOUD_API_KEY." >&2
  exit 1
fi
export PME_CLOUD_INSTRUQT_API_KEY

echo "=== SLB Workshop — Serverless bootstrap ==="

if [[ "${PME_CLOUD_INSTRUQT_API_KEY}" == '$'* ]] || [[ "${#PME_CLOUD_INSTRUQT_API_KEY}" -lt 20 ]]; then
  PME_CLOUD_INSTRUQT_API_KEY="${ESS_CLOUD_API_KEY}"
fi

_auth_check=$(curl -s -o /dev/null -w "%{http_code}" \
  -H "Authorization: ApiKey ${PME_CLOUD_INSTRUQT_API_KEY}" \
  "https://api.elastic-cloud.com/api/v1/serverless/projects/observability?page_size=1")
if [ "$_auth_check" = "401" ] || [ "$_auth_check" = "403" ]; then
  echo "ERROR: ESS_CLOUD_API_KEY invalid (HTTP ${_auth_check})." >&2
  exit 1
fi

_n=0
until [ -f /opt/instruqt/bootstrap/host-bootstrap-completed ]; do
  sleep 1; _n=$((_n + 1))
  [ "$_n" -ge 600 ] && { echo "ERROR: host-bootstrap timeout" >&2; exit 1; }
done

PRODUCT_TIER="${PRODUCT_TIER:-complete}"
python3 bin/es3-api.py \
  --operation create \
  --project-type "${PROJECT_TYPE:-observability}" \
  --product-tier "$PRODUCT_TIER" \
  --regions "${REGIONS:-aws-us-east-1}" \
  --project-name "${INSTRUQT_TRACK_SLUG:-slb-workshop}-$INSTRUQT_PARTICIPANT_ID-$(date '+%s')" \
  --api-key "${PME_CLOUD_INSTRUQT_API_KEY}" \
  --wait-for-ready

timeout=120; counter=0
while [ $counter -lt $timeout ]; do
  [ -f /tmp/project_results.json ] && break
  sleep 1; counter=$((counter + 1))
done
[ -f /tmp/project_results.json ] || { echo "ERROR: /tmp/project_results.json not found" >&2; exit 1; }

REG="${REGIONS:-aws-us-east-1}"
KIBANA_URL="$(jq -r --arg r "$REG" '.[$r].endpoints.kibana' /tmp/project_results.json)"
ES_URL="$(jq -r --arg r "$REG" '.[$r].endpoints.elasticsearch' /tmp/project_results.json)"
ELASTICSEARCH_PASSWORD="$(jq -r --arg r "$REG" '.[$r].credentials.password' /tmp/project_results.json)"
export KIBANA_URL ES_URL ELASTICSEARCH_PASSWORD

agent variable set ES_KIBANA_URL "$KIBANA_URL"
agent variable set ES_URL "$ES_URL"
agent variable set ES_USERNAME "$(jq -r --arg r "$REG" '.[$r].credentials.username' /tmp/project_results.json)"
agent variable set ES_PASSWORD "$ELASTICSEARCH_PASSWORD"
agent variable set ES_DEPLOYMENT_ID "$(jq -r --arg r "$REG" '.[$r].id' /tmp/project_results.json)"

WORKSHOP_ES_API_KEY=""
output="$(curl -X POST -s -u "admin:${ELASTICSEARCH_PASSWORD}" \
  -w "\n%{http_code}" "$ES_URL/_security/api_key" \
  -H 'Content-Type: application/json' \
  -d '{"name":"slb-workshop"}' || true)"
http_code="$(echo "$output" | tail -n1)"
response_body="$(echo "$output" | sed '$d')"
if [ "$http_code" = "200" ]; then
  ELASTICSEARCH_API_KEY="$(echo "$response_body" | jq -r '.encoded // empty')"
  if [ -n "$ELASTICSEARCH_API_KEY" ]; then
    agent variable set ES_API_KEY "$ELASTICSEARCH_API_KEY"
    agent variable set ELASTIC_API_KEY "$ELASTICSEARCH_API_KEY"
    WORKSHOP_ES_API_KEY="$ELASTICSEARCH_API_KEY"
  fi
fi

BASE64="$(echo -n "admin:${ELASTICSEARCH_PASSWORD}" | base64 -w0 2>/dev/null || echo -n "admin:${ELASTICSEARCH_PASSWORD}" | base64)"
KIBANA_URL_WITHOUT_PROTOCOL="$(echo "$KIBANA_URL" | sed -e 's#http[s]\?://##g')"

cat > /etc/nginx/conf.d/default.conf <<NGX
server {
  listen 8080 default_server;
  server_name kibana;
  location /nginx_status { stub_status on; allow 127.0.0.1; deny all; }
  location / {
    proxy_set_header Host ${KIBANA_URL_WITHOUT_PROTOCOL};
    proxy_pass ${KIBANA_URL};
    proxy_next_upstream error timeout invalid_header http_500 http_502 http_503 http_504;
    proxy_set_header Connection "keep-alive";
    proxy_hide_header Content-Security-Policy;
    proxy_hide_header X-Frame-Options;
    proxy_hide_header X-Content-Type-Options;
    proxy_hide_header Strict-Transport-Security;
    proxy_set_header X-Scheme \$scheme;
    proxy_set_header X-Forwarded-Proto https;
    proxy_set_header X-Forwarded-Host \$host;
    proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
    proxy_set_header X-Real-IP \$remote_addr;
    proxy_set_header Authorization "Basic ${BASE64}";
    proxy_set_header Accept-Encoding "gzip, deflate, br";
    proxy_redirect off;
    proxy_http_version 1.1;
    client_max_body_size 20M;
    proxy_read_timeout 600;
    proxy_buffering off;
  }
}
NGX

systemctl restart nginx; sleep 2
systemctl is-active --quiet nginx || { echo "ERROR: nginx failed"; exit 1; }

# Clone workshop repo for shared scripts (best-effort)
SLB_REPO_URL="${SLB_WORKSHOPS_GIT_URL:-https://github.com/poulsbopete/slb-workshops.git}"
SLB_REPO_RAW="${SLB_WORKSHOPS_RAW_URL:-https://raw.githubusercontent.com/poulsbopete/slb-workshops/main}"
SLB_REPO_DIR=/opt/slb-workshops
if [ ! -d "$SLB_REPO_DIR/.git" ]; then
  export DEBIAN_FRONTEND=noninteractive
  apt-get update -y
  apt-get install -y --no-install-recommends git jq curl ca-certificates python3-pip
  git clone --depth 1 "$SLB_REPO_URL" "$SLB_REPO_DIR" 2>/dev/null || true
else
  git -C "$SLB_REPO_DIR" pull --ff-only 2>/dev/null || true
fi

ensure_workshop_seed_scripts() {
  local seed_dir="${SLB_REPO_DIR}/shared/seeds"
  mkdir -p "$seed_dir"
  if [ ! -f "${seed_dir}/seed-workshop-data.sh" ] || [ ! -f "${seed_dir}/seed_workshop_data.py" ]; then
    echo "Fetching workshop seed scripts from ${SLB_REPO_RAW}…"
    curl -fsSL "${SLB_REPO_RAW}/shared/seeds/seed-workshop-data.sh" -o "${seed_dir}/seed-workshop-data.sh"
    curl -fsSL "${SLB_REPO_RAW}/shared/seeds/seed_workshop_data.py" -o "${seed_dir}/seed_workshop_data.py"
    curl -fsSL "${SLB_REPO_RAW}/shared/seeds/requirements-seed.txt" -o "${seed_dir}/requirements-seed.txt" 2>/dev/null || true
  fi
  chmod +x "${seed_dir}/seed-workshop-data.sh"
}

ensure_workshop_seed_scripts

# OTLP endpoint for optional seed scripts
MOTLP_FROM_API=""
for _key in motlp otlp otel; do
  _val="$(jq -r --arg r "$REG" --arg k "$_key" '.[$r].endpoints[$k] // empty' /tmp/project_results.json)"
  [ -n "$_val" ] && [ "$_val" != "null" ] && { MOTLP_FROM_API="$_val"; break; }
done
DERIVED_OTLP=""
if [[ -n "${ES_URL:-}" ]] && [[ "$ES_URL" == *".es."* ]]; then
  DERIVED_OTLP="${ES_URL%/}"; DERIVED_OTLP="${DERIVED_OTLP//.es./.ingest.}"
fi
WORKSHOP_OTLP_BASE="${MOTLP_FROM_API:-$DERIVED_OTLP}"
[ -n "$WORKSHOP_OTLP_BASE" ] && agent variable set ES_OTLP_ENDPOINT "$WORKSHOP_OTLP_BASE" || true

# Export credentials for seed script (before .bashrc)
export ES_API_KEY="${WORKSHOP_ES_API_KEY:-}"
export ELASTIC_API_KEY="${WORKSHOP_ES_API_KEY:-}"
export ES_USERNAME="admin"
export ES_PASSWORD="${ELASTICSEARCH_PASSWORD}"
export WORKSHOP_OTLP_ENDPOINT="${WORKSHOP_OTLP_BASE:-}"

# Brief pause so Serverless ingest accepts writes before seeding
echo "Waiting for Elasticsearch to accept API requests…"
_es_ready=0
for _i in $(seq 1 36); do
  if [ -n "${ES_API_KEY:-}" ]; then
    _code=$(curl -s -o /dev/null -w "%{http_code}" \
      -H "Authorization: ApiKey ${ES_API_KEY}" \
      "${ES_URL%/}/_security/_authenticate" 2>/dev/null || echo 000)
  else
    _code=$(curl -s -o /dev/null -w "%{http_code}" \
      -u "admin:${ES_PASSWORD}" \
      "${ES_URL%/}/" 2>/dev/null || echo 000)
  fi
  if [ "$_code" = "200" ]; then
    _es_ready=1
    echo "  ✓ Elasticsearch API ready (HTTP ${_code})"
    break
  fi
  [ $((_i % 6)) -eq 1 ] && echo "  … waiting for ES API (${_i}/36, HTTP ${_code})"
  sleep 5
done
[ "$_es_ready" -eq 1 ] || echo "WARN: ES API probe timed out — seed will retry internally" >&2

DEFAULT_SEED="${SLB_REPO_DIR}/shared/seeds/seed-workshop-data.sh"
if [ -f "$DEFAULT_SEED" ]; then
  chmod +x "$DEFAULT_SEED"
  echo "Running default workshop seed: $DEFAULT_SEED"
  _seed_ok=0
  for _attempt in 1 3; do
    if bash "$DEFAULT_SEED"; then
      _seed_ok=1
      break
    fi
    echo "WARN: seed attempt ${_attempt} failed — retrying in 15s…" >&2
    sleep 15
  done
  if [ "$_seed_ok" -ne 1 ]; then
    echo "ERROR: workshop seed failed after retries — labs will have empty data" >&2
    exit 1
  fi
  _log_count=0
  if [ -n "${ES_API_KEY:-}" ]; then
    _log_count=$(curl -s -H "Authorization: ApiKey ${ES_API_KEY}" \
      "${ES_URL%/}/logs-*/_count" | jq -r '.count // 0' 2>/dev/null || echo 0)
  elif [ -n "${ES_PASSWORD:-}" ]; then
    _log_count=$(curl -s -u "admin:${ES_PASSWORD}" \
      "${ES_URL%/}/logs-*/_count" | jq -r '.count // 0' 2>/dev/null || echo 0)
  fi
  if [ "${_log_count:-0}" -lt 100 ] 2>/dev/null; then
    echo "ERROR: bootstrap verification failed — only ${_log_count:-0} log documents indexed" >&2
    exit 1
  fi
  echo "✓ Workshop data verified: ${_log_count} log documents"
elif [ -n "${WORKSHOP_SEED_SCRIPT:-}" ] && [ -f "$WORKSHOP_SEED_SCRIPT" ]; then
  echo "Running workshop seed: $WORKSHOP_SEED_SCRIPT"
  bash "$WORKSHOP_SEED_SCRIPT" || { echo "ERROR: custom seed script failed" >&2; exit 1; }
else
  echo "ERROR: workshop seed script missing at $DEFAULT_SEED" >&2
  exit 1
fi

{
  echo ""
  echo "# === SLB Workshop ==="
  printf 'export KIBANA_URL=%q\n' "$KIBANA_URL"
  printf 'export ES_URL=%q\n' "$ES_URL"
  printf 'export ES_USERNAME=%q\n' "admin"
  printf 'export ES_PASSWORD=%q\n' "$ELASTICSEARCH_PASSWORD"
  [ -n "$WORKSHOP_ES_API_KEY" ] && printf 'export ES_API_KEY=%q\n' "$WORKSHOP_ES_API_KEY"
  [ -n "$WORKSHOP_ES_API_KEY" ] && printf 'export ELASTIC_API_KEY=%q\n' "$WORKSHOP_ES_API_KEY"
  [ -n "$WORKSHOP_OTLP_BASE" ] && printf 'export WORKSHOP_OTLP_ENDPOINT=%q\n' "$WORKSHOP_OTLP_BASE"
  [ -n "${WORKSHOP_ES_API_KEY:-}" ] && printf 'export WORKSHOP_OTLP_AUTH_HEADER=%q\n' "ApiKey ${WORKSHOP_ES_API_KEY}"
} >> /root/.bashrc

echo "=== SLB Workshop bootstrap complete ==="
