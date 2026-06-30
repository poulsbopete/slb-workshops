#!/bin/bash
# Standard track-level setup wrapper — copies shared bootstrap inline for Instruqt.
# Instruqt runs this from track_scripts/; we invoke the base script if repo is cloned,
# otherwise fall back to embedded minimal bootstrap (same as base script).

set -euo pipefail

if [ -f /opt/slb-workshops/shared/scripts/setup-es3-api-base.sh ]; then
  exec bash /opt/slb-workshops/shared/scripts/setup-es3-api-base.sh
fi

# Fallback: download base script from GitHub (track may run before repo clone)
curl -fsSL "${SLB_WORKSHOPS_RAW_URL:-https://raw.githubusercontent.com/poulsbopete/slb-workshops/main}/shared/scripts/setup-es3-api-base.sh" \
  -o /tmp/setup-es3-api-base.sh
chmod +x /tmp/setup-es3-api-base.sh
exec bash /tmp/setup-es3-api-base.sh
