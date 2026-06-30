#!/bin/bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
for track in $(find "$ROOT/tracks" -mindepth 2 -maxdepth 2 -type d -name 'slb-*' | sort); do
  echo "==> Pushing $track"
  (cd "$track" && instruqt track push)
done
echo "Done."
