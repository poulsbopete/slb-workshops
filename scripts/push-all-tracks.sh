#!/bin/bash
# Push all SLB workshop tracks to Instruqt (elastic team).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
for track in "$ROOT"/tracks/slb-*; do
  [ -d "$track" ] || continue
  slug="$(basename "$track")"
  echo "==> Pushing $slug"
  (cd "$track" && instruqt track push)
done
echo "Done."
