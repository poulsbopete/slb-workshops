#!/bin/bash
# Seed SLB workshop sample data — logs, APM transactions, metrics, OTLP traces, Kibana assets.
set -euo pipefail

SLB_SEED_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

: "${ES_URL:?ES_URL required}"
: "${ES_API_KEY:?ES_API_KEY required}"

export ES_API_KEY="${ES_API_KEY:-${ELASTIC_API_KEY:-}}"
export ELASTIC_API_KEY="${ELASTIC_API_KEY:-$ES_API_KEY}"
export ES_USERNAME="${ES_USERNAME:-admin}"
export ES_PASSWORD="${ES_PASSWORD:-}"
export KIBANA_URL="${KIBANA_URL:-${ES_KIBANA_URL:-}}"
export WORKSHOP_OTLP_ENDPOINT="${WORKSHOP_OTLP_ENDPOINT:-${WORKSHOP_OTLP_BASE:-}}"

echo "=== SLB Workshop seed script ==="
echo "ES_URL=$ES_URL"
[ -n "${WORKSHOP_OTLP_ENDPOINT:-}" ] && echo "OTLP=$WORKSHOP_OTLP_ENDPOINT"

# Python deps for OTLP export (best-effort)
if ! python3 -c "import opentelemetry.sdk" 2>/dev/null; then
  echo "Installing OTLP seed dependencies…"
  python3 -m pip install -q -r "${SLB_SEED_DIR}/requirements-seed.txt" 2>/dev/null \
    || pip3 install -q -r "${SLB_SEED_DIR}/requirements-seed.txt" 2>/dev/null \
    || apt-get install -y -qq python3-pip && pip3 install -q -r "${SLB_SEED_DIR}/requirements-seed.txt"
fi

exec python3 "${SLB_SEED_DIR}/seed_workshop_data.py"
