#!/bin/bash
# Shared cleanup — delete the provisioned Serverless project.
set -euo pipefail

echo "=== SLB Workshop — cleanup ==="

PME_CLOUD_INSTRUQT_API_KEY="${ESS_CLOUD_API_KEY:-${PME_CLOUD_INSTRUQT_API_KEY:-}}"

if [ -f /tmp/project_results.json ] && [ -n "${PME_CLOUD_INSTRUQT_API_KEY:-}" ]; then
  REG="${REGIONS:-aws-us-east-1}"
  PROJECT_ID="$(jq -r --arg r "$REG" '.[$r].id // empty' /tmp/project_results.json)"
  if [ -n "$PROJECT_ID" ] && [ "$PROJECT_ID" != "null" ]; then
    echo "Deleting Serverless project ${PROJECT_ID}..."
    python3 bin/es3-api.py \
      --operation delete \
      --project-id "$PROJECT_ID" \
      --api-key "${PME_CLOUD_INSTRUQT_API_KEY}" || echo "WARN: project delete failed"
  fi
fi

echo "Cleanup complete."
