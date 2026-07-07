#!/usr/bin/env python3
"""Generate consolidated Instruqt tracks (8 series tracks, multiple challenges each)."""

from __future__ import annotations

import sys
import textwrap
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))
CATALOG = ROOT / "catalog" / "workshops.yaml"
SECTIONS = ROOT / "catalog" / "sections.yaml"
TRACKS_DIR = ROOT / "tracks"

KIBANA_TAB = """\
- title: Elastic Serverless
  type: service
  hostname: es3-api
  path: /app/home
  port: 8080
  custom_request_headers:
  - key: Content-Security-Policy
    value: 'script-src ''self'' https://kibana.estccdn.com; worker-src blob: ''self'';
      style-src ''unsafe-inline'' ''self'' https://kibana.estccdn.com'
  custom_response_headers:
  - key: Content-Security-Policy
    value: 'script-src ''self'' https://kibana.estccdn.com; worker-src blob: ''self'';
      style-src ''unsafe-inline'' ''self'' https://kibana.estccdn.com'"""

SETUP_TRACK = """\
#!/bin/bash
set -euo pipefail
# Provision Observability Serverless + Kibana proxy (:8080)
if [ -f /opt/slb-workshops/shared/scripts/setup-es3-api-base.sh ]; then
  exec bash /opt/slb-workshops/shared/scripts/setup-es3-api-base.sh
fi
curl -fsSL "https://raw.githubusercontent.com/poulsbopete/slb-workshops/main/shared/scripts/setup-es3-api-base.sh" \\
  -o /tmp/setup-es3-api-base.sh
chmod +x /tmp/setup-es3-api-base.sh
exec bash /tmp/setup-es3-api-base.sh
"""

CLEANUP_TRACK = """\
#!/bin/bash
set -euo pipefail
if [ -f /opt/slb-workshops/shared/scripts/cleanup-es3-api-base.sh ]; then
  exec bash /opt/slb-workshops/shared/scripts/cleanup-es3-api-base.sh
fi
curl -fsSL "https://raw.githubusercontent.com/poulsbopete/slb-workshops/main/shared/scripts/cleanup-es3-api-base.sh" \\
  -o /tmp/cleanup-es3-api-base.sh
chmod +x /tmp/cleanup-es3-api-base.sh
exec bash /tmp/cleanup-es3-api-base.sh
"""

CHECK_CHALLENGE = """\
#!/bin/bash
set -euo pipefail
source /root/.bashrc 2>/dev/null || true
if [ -z "${KIBANA_URL:-}" ] && [ -z "${ES_URL:-}" ]; then
  echo "CHECK FAIL — environment not bootstrapped; wait or run solve-es3-api"
  exit 1
fi
if [ -n "${ES_URL:-}" ] && [ -n "${ES_API_KEY:-}" ]; then
  _count=$(curl -s -H "Authorization: ApiKey ${ES_API_KEY}" \\
    "${ES_URL%/}/logs-*/_count" | jq -r '.count // 0' 2>/dev/null || echo 0)
  if [ "${_count:-0}" -gt 0 ] 2>/dev/null; then
    echo "CHECK PASS — Elastic Serverless ready with ${_count} log documents"
    exit 0
  fi
  echo "CHECK WARN — project ready but sample logs not indexed yet; refresh in a minute"
  exit 0
fi
echo "CHECK PASS — Elastic Serverless environment is ready"
exit 0
"""

SOLVE_CHALLENGE = """\
#!/bin/bash
set -euo pipefail
echo "Environment is provisioned by track setup. Refresh the Elastic Serverless tab."
exit 0
"""

CHALLENGE_SETUP = """\
#!/bin/bash
exit 0
"""

from labs_serverless import LABS
from site_config import slide_deck_url


BASE_TAGS = [
    "slb",
    "slb-workshops",
    "elastic",
    "serverless",
    "observability",
    "co.elastic.workshops",
]

IFRAME_HEIGHT = 1400


def iframe_note(workshop: dict) -> str:
    wid = workshop["id"]
    code = workshop["code"]
    url = slide_deck_url(wid)
    return (
        "    ## While you wait…\n\n"
        f'    <iframe src="{url}"\n'
        f'      width="100%" height="{IFRAME_HEIGHT}" frameborder="0"\n'
        '      style="border-radius:8px;display:block;width:100%;min-height:900px">\n'
        "    </iframe>\n\n"
        f"    *Provisioning your **Observability Serverless** lab for **{code}** "
        "(usually 2–3 minutes). Same Kibana workflows apply on **ECH** and **self-managed**.*"
    )


def assignment_md(workshop: dict) -> str:
    wid = workshop["id"]
    body = LABS.get(wid, f"\n# {workshop['title']}\n\nLab content TBD.\n")
    topic_lines = chr(10).join("    - " + t for t in workshop.get("topics", []))
    front = f"""---
slug: {wid}-lab
type: challenge
title: "{workshop['code']} — {workshop['title']}"
teaser: "{workshop['description'].strip().replace(chr(10), ' ')[:200]}"
notes:
- type: text
  contents: |-
{iframe_note(workshop)}
- type: text
  contents: |
    ## Session topics
{topic_lines}
tabs:
{KIBANA_TAB}
timelimit: 0
---

{body.strip()}
"""
    return front


def workshops_by_id(catalog: dict) -> dict[str, dict]:
    return {ws["id"]: ws for ws in catalog["workshops"]}


def load_sections() -> list[dict]:
    with SECTIONS.open() as f:
        return yaml.safe_load(f)["sections"]


def section_tag(section_id: str) -> str:
    for section in load_sections():
        if section["id"] == section_id:
            return section["tag"]
    return f"slb-series-{section_id}"


def tags_for(section_id: str) -> list[str]:
    return ["slb", "slb-workshops", section_tag(section_id)] + [
        t for t in BASE_TAGS if t not in {"slb", "slb-workshops"}
    ]


def track_yml(section: dict, workshops: list[dict]) -> str:
    name = section["name"]
    session_lines = chr(10).join(
        f"  - **{ws['code']}** — {ws['title']}" for ws in workshops
    )
    lab_word = "labs" if len(workshops) != 1 else "lab"
    return f"""slug: {section['track']}
title: "SLB — {name}"
teaser: |
  Consolidated Instruqt track for the SLB × Elastic **{name}** series.
  Complete the labs in order, or jump to the session matching your live workshop.
description: |-
  **SLB — {name}**

  This track contains **{len(workshops)}** hands-on {lab_word} — one per live session in the series.
  Each lab runs on **Elastic Observability Serverless** for hands-on practice — the **same Kibana workflows** apply on **ECH** and **self-managed** deployments.

  **What you learn:** ES|QL, Streams, AI Assistant, Agent Builder, Workflows, SLOs, and unified Observability. **What Serverless skips:** day-to-day cluster, ILM, and Fleet operations.

  ## Sessions in this track
{session_lines}

  Register for live sessions: [events.elastic.co/slbworkshops](https://events.elastic.co/slbworkshops)
icon: https://cdn.instruqt.com/assets/templates/kubernetes.png
tags:
{chr(10).join('  - ' + t for t in tags_for(section['id']))}
owner: elastic
developers:
- peter.simkins@elastic.co
idle_timeout: 3600
timelimit: 10800
lab_config:
  sidebar_enabled: true
  feedback_recap_enabled: true
  feedback_tab_enabled: false
  loadingMessages: true
  theme:
    name: modern-dark
  default_layout: AssignmentRight
  default_layout_sidebar_size: 35
  override_challenge_layout: false
"""


def write_challenge(challenge_dir: Path, workshop: dict) -> None:
    challenge_dir.mkdir(parents=True, exist_ok=True)
    for name, content in [
        (challenge_dir / "assignment.md", assignment_md(workshop)),
        (challenge_dir / "setup-es3-api", CHALLENGE_SETUP),
        (challenge_dir / "check-es3-api", CHECK_CHALLENGE),
        (challenge_dir / "solve-es3-api", SOLVE_CHALLENGE),
    ]:
        name.write_text(content)
        if name.name != "assignment.md":
            name.chmod(0o755)


def write_consolidated_track(section: dict, workshops: list[dict]) -> None:
    section_id = section["id"]
    track_slug = section["track"]
    track_dir = TRACKS_DIR / section_id / track_slug
    track_yml_path = track_dir / "track.yml"

    if track_yml_path.exists():
        existing = yaml.safe_load(track_yml_path.read_text())
        if isinstance(existing, dict) and existing.get("id"):
            print(f"  · skip {track_slug} (preserves Instruqt id)")
            return

    scripts_dir = track_dir / "track_scripts"
    scripts_dir.mkdir(parents=True, exist_ok=True)

    track_yml_path.write_text(track_yml(section, workshops))
    (track_dir / "config.yml").write_text((ROOT / "shared" / "config.yml").read_text())
    (scripts_dir / "setup-es3-api").write_text(SETUP_TRACK)
    (scripts_dir / "cleanup-es3-api").write_text(CLEANUP_TRACK)
    (scripts_dir / "setup-es3-api").chmod(0o755)
    (scripts_dir / "cleanup-es3-api").chmod(0o755)

    for index, workshop in enumerate(workshops, start=1):
        challenge_dir = track_dir / f"{index:02d}-{workshop['id']}-lab"
        write_challenge(challenge_dir, workshop)

    print(f"  ✓ tracks/{section_id}/{track_slug} ({len(workshops)} labs)")


def main() -> None:
    with CATALOG.open() as f:
        catalog = yaml.safe_load(f)
    by_id = workshops_by_id(catalog)

    for section in load_sections():
        workshops = [by_id[wid] for wid in section["workshop_ids"]]
        missing = [wid for wid in section["workshop_ids"] if wid not in by_id]
        if missing:
            print(f"  ? skip {section['track']} (missing workshops: {missing})")
            continue
        write_consolidated_track(section, workshops)

    print(f"\nGenerated consolidated tracks in {TRACKS_DIR}")


if __name__ == "__main__":
    main()
