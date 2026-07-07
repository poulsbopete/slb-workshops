#!/bin/bash
# Seed SLB workshop sample data — logs, APM transactions, metrics, OTLP traces, Kibana assets.
set -euo pipefail

SLB_SEED_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

: "${ES_URL:?ES_URL required}"
# API key preferred; bootstrap always sets ES_PASSWORD as fallback for Kibana APIs
if [ -z "${ES_API_KEY:-}" ] && [ -z "${ELASTIC_API_KEY:-}" ] && [ -z "${ES_PASSWORD:-}" ]; then
  echo "ERROR: ES_API_KEY or ES_PASSWORD required" >&2
  exit 1
fi

export ES_API_KEY="${ES_API_KEY:-${ELASTIC_API_KEY:-}}"
export ELASTIC_API_KEY="${ELASTIC_API_KEY:-$ES_API_KEY}"
export ES_USERNAME="${ES_USERNAME:-admin}"
export ES_PASSWORD="${ES_PASSWORD:-}"
export KIBANA_URL="${KIBANA_URL:-${ES_KIBANA_URL:-}}"
export WORKSHOP_OTLP_ENDPOINT="${WORKSHOP_OTLP_ENDPOINT:-${WORKSHOP_OTLP_BASE:-}}"

echo "=== SLB Workshop seed script ==="
echo "ES_URL=$ES_URL"
[ -n "${WORKSHOP_OTLP_ENDPOINT:-}" ] && echo "OTLP=$WORKSHOP_OTLP_ENDPOINT"

# OTLP is optional; skip slow pip installs during bootstrap (bulk APM docs cover labs).
export SLB_SKIP_OTLP_PIP=1

exec python3 "${SLB_SEED_DIR}/seed_workshop_data.py"
