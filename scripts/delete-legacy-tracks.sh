#!/bin/bash
# Delete per-session Instruqt tracks superseded by 8 consolidated series tracks.
set -euo pipefail

LEGACY=(
  slb-f-01-support-best-practices
  slb-f-02-intro-to-elastic
  slb-f-03-elastic-day-to-day
  slb-f-04-looking-forward
  slb-dev-01-ui-dashboards
  slb-dev-02-esql-essentials
  slb-dev-03-deployment-validation
  slb-sre-01-platform-ops
  slb-sre-02-ilm-data-tier
  slb-sre-03-ingestion-architecture
  slb-sre-04-production-readiness
  slb-arch-01-architecture-migration
  slb-arch-02-lifecycle-governance
  slb-bi-01-dashboard-basics
  slb-bi-02-esql-analysts
  slb-bi-03-apis-dashboards
  slb-aiops-01-alert-fatigue
  slb-aiops-02-ai-investigation
  slb-aiops-03-workflows-remediation
  slb-oneoff-ai-ml-overview
  slb-oneoff-rag-mcp
  slb-oneoff-hybrid-search
  slb-all-teams-platform-review
)

for slug in "${LEGACY[@]}"; do
  echo "==> Deleting $slug"
  instruqt track delete "$slug" 2>&1 || echo "    (not found — skipped)"
done

echo "Done."
