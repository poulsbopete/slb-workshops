#!/usr/bin/env python3
"""Generate Instruqt track scaffolds from catalog/workshops.yaml."""

from __future__ import annotations

import textwrap
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
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
      style-src ''unsafe-inline'' ''self'' https://kibana.estccdn.com'
- title: Terminal
  type: terminal
  hostname: es3-api"""

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
if [ -n "${KIBANA_URL:-}" ] || [ -n "${ES_URL:-}" ]; then
  echo "CHECK PASS — Elastic Serverless environment is ready"
  exit 0
fi
echo "CHECK FAIL — environment not bootstrapped; wait or run solve-es3-api"
exit 1
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

# Lab instructions keyed by workshop id
LABS: dict[str, str] = {
    "f-02": """
# Intro to Elastic — Hands-on Lab

Welcome to your personal **Elastic Observability Serverless** project. This lab
supports the **F-02 — Intro to Elastic** live session.

## Part 1 — Platform tour

1. Open the **Elastic Serverless** tab (Kibana Home).
2. Navigate **Observability → Overview**. Note the unified view of logs, metrics, and traces.
3. Open **Stack Management → Index Management**. Observe data streams created by the platform.
4. Open **Stack Management → Data tiers**. Review hot / warm / cold / frozen / delete concepts
   from the session.

## Part 2 — Persona lenses

Pick the lens closest to your role:

| Persona | Start here |
|---------|------------|
| Developer | **Observability → APM → Services** |
| SRE / Infra | **Observability → Hosts** and **Fleet** |
| Analyst | **Analytics → Discover** |
| Architect | **Stack Management → Index Lifecycle Policies** |

## Part 3 — SLB context

Discuss with your facilitator: which of these building blocks map to your current
Grafana / Prometheus / OTel workflows today?

When finished, click **Check**.
""",
    "f-03": """
# Elastic Day to Day — Hands-on Lab

## Part 1 — Discover and ES|QL

1. Go to **Analytics → Discover** (or **Observability → Logs → Explorer**).
2. Open the ES|QL editor and run:

```esql
FROM logs-* | LIMIT 10
```

3. Add a filter on `@timestamp` for the last 15 minutes.

## Part 2 — Grafana → Elastic translation

| Grafana concept | Elastic equivalent |
|-----------------|-------------------|
| Explore | Discover / Logs Explorer |
| Dashboard panel | Lens visualization |
| Prometheus query | ES|QL or PromQL in Metrics |
| Alert rule | **Observability → Alerts** |

## Part 3 — Ingestion fundamentals

1. Open **Integrations** and browse an OTel or Elastic Agent integration.
2. Note the data stream naming pattern (`logs-*`, `metrics-*`, `traces-*`).

## Part 4 — API peek (Terminal tab)

```bash
source ~/.bashrc
curl -s -H "Authorization: ApiKey $ES_API_KEY" \\
  "$ES_URL/_cat/indices?v" | head -20
```

Click **Check** when complete.
""",
    "dev-01": """
# Elastic UI & Dashboard Workflows

**Audience:** Developers coming from Grafana.

## Part 1 — Discover

1. **Analytics → Discover** — select a logs data stream.
2. Add a KQL filter (e.g. `service.name : *`).
3. Save the search.

## Part 2 — Dashboards

1. **Analytics → Dashboards → Create dashboard**.
2. Add a **Lens** visualization — time series of log volume by service.
3. Add a **Drilldown** from the chart to Discover (filter on clicked series).

## Part 3 — Grafana translation exercise

| Your Grafana habit | Do this in Kibana |
|--------------------|-------------------|
| Dashboard variables | **Controls** on dashboard |
| Panel links | **Drilldowns** |
| Explore from panel | **Open in Discover** |

Customize one panel title and layout. Click **Check**.
""",
    "dev-02": """
# ES|QL Essentials for Troubleshooting

## Part 1 — Syntax basics

In **Discover** or **Logs → Explorer**, run these queries:

```esql
FROM logs-* | WHERE @timestamp > NOW() - 1 hour | LIMIT 20
```

```esql
FROM logs-* | STATS count = COUNT(*) BY service.name | SORT count DESC | LIMIT 10
```

## Part 2 — Logs / metrics / traces

```esql
FROM metrics-* | STATS avg(cpu) = AVG(system.cpu.total.pct) BY host.name | LIMIT 10
```

```esql
FROM traces-* | LIMIT 10
```

## Part 3 — Incident workflow

Simulate an investigation:

1. Find the noisiest `service.name` in the last hour.
2. Filter logs for ERROR level for that service.
3. Save the query for daily use.

Click **Check** when done.
""",
    "dev-03": """
# Deployment Validation & Incident Workflows

## Part 1 — Service health after deploy

1. **Observability → APM → Services** — pick a service (or use sample data).
2. Compare error rate and latency for **last 15 minutes** vs **previous day**.

## Part 2 — Correlate logs, metrics, traces

1. From a service view, pivot to **Logs** and **Metrics** for the same time range.
2. Use **Unified view** or split tabs to correlate signals.

## Part 3 — Saved views

1. Save an ES|QL query as a **saved search**.
2. Pin a dashboard panel for post-deploy validation.

## Part 4 — Runbook snippet (Terminal)

Document your validation query in a note:

```bash
source ~/.bashrc
echo "Post-deploy check: FROM logs-* | WHERE service.environment == 'production' ..."
```

Click **Check**.
""",
    "sre-01": """
# Platform Operations Fundamentals

## Part 1 — Data streams and templates

1. **Stack Management → Index Management** — filter **Data streams**.
2. Inspect naming: `logs-*`, `metrics-*`, `traces-*`.
3. **Index Management → Index Templates** — review composable templates.

## Part 2 — Ingest pipelines

1. **Stack Management → Ingest Pipelines** — open a default pipeline.
2. Note processors (date, set, rename).

## Part 3 — Fleet vs standalone

1. **Fleet → Agents** — review Fleet-managed model.
2. Compare with **Integrations → OTel** standalone collector docs.

## Part 4 — Terminal inspection

```bash
source ~/.bashrc
curl -s -H "Authorization: ApiKey $ES_API_KEY" \\
  "$ES_URL/_data_stream" | jq '.data_streams[].name' | head -10
```

Click **Check**.
""",
    "sre-02": """
# ILM & Data Tier Deep Dive

## Part 1 — ILM policies

1. **Stack Management → Index Lifecycle Policies**.
2. Review phases: **hot → warm → cold → frozen → delete**.
3. Note rollover conditions on the hot phase.

## Part 2 — Tier allocation

1. Open a policy and inspect **allocate** and **migrate** actions.
2. Discuss SLB retention targets with your facilitator.

## Part 3 — Common misconfigurations

Checklist to review:

- Rollover max_size vs ingest rate
- Warm phase shrink/replica settings
- Frozen searchable snapshot prerequisites

## Part 4 — API

```bash
source ~/.bashrc
curl -s -H "Authorization: ApiKey $ES_API_KEY" \\
  "$ES_URL/_ilm/policy" | jq 'keys'
```

Click **Check**.
""",
    "sre-03": """
# Ingestion Architecture & Troubleshooting

## Part 1 — Integration comparison

1. **Integrations** — compare **Elastic Agent** vs **OpenTelemetry** integrations.
2. Note data stream outputs for each.

## Part 2 — Prometheus patterns

1. Search integrations for **Prometheus**.
2. Review **remote_write** vs **receiver scrape** options.

## Part 3 — Failure store

1. **Stack Management → Index Management** — look for failure store indices.
2. **Ingest Pipelines** — review on_failure handlers.

## Part 4 — Troubleshooting commands

```bash
source ~/.bashrc
curl -s -H "Authorization: ApiKey $ES_API_KEY" \\
  "$ES_URL/_cat/indices?v&health=red"
```

Click **Check**.
""",
    "sre-04": """
# Production Readiness Workshop

## Part 1 — Validation checklist

Work through this checklist in Kibana:

- [ ] Data streams receiving data (Index Management)
- [ ] ILM policies attached
- [ ] Fleet agents healthy (if applicable)
- [ ] Critical alert rules enabled
- [ ] Dashboards loading for SLO review

## Part 2 — Ingestion health

1. **Observability → Logs → Anomalies** (if enabled).
2. **Fleet → Agent details** — last check-in times.

## Part 3 — Runbook draft

In the Terminal tab, create a runbook outline:

```bash
cat > /root/production-readiness-notes.md <<'EOF'
# SLB Elastic Production Readiness
## Ingestion health checks
## Escalation contacts
## Rollback criteria
EOF
cat /root/production-readiness-notes.md
```

Click **Check**.
""",
    "bi-01": """
# Dashboard & Data Exploration Basics

**No prior Elastic experience required.**

## Part 1 — Discover

1. **Analytics → Discover**.
2. Select any available data view.
3. Use the time picker — **Last 24 hours**.
4. Add a field column and sort.

## Part 2 — Lens

1. **Visualize Library → Create visualization → Lens**.
2. Build a bar chart — count of events over time.
3. Save to a new dashboard.

## Part 3 — Export

1. From Discover, export a CSV sample (Share → CSV Reports if available,
   or copy table data).

Click **Check**.
""",
    "bi-02": """
# ES|QL for Analysts

## Part 1 — Aggregations

```esql
FROM logs-* | STATS events = COUNT(*) BY service.name | SORT events DESC | LIMIT 10
```

## Part 2 — Time-based analysis

```esql
FROM logs-* | STATS count = COUNT(*) BY bucket = BUCKET(@timestamp, 1 hour) | SORT bucket
```

## Part 3 — Cost / utilization correlation

Discuss with facilitator how to join observability metrics with cost data
(lookup join or separate index). Try:

```esql
FROM metrics-* | STATS avg_cpu = AVG(system.cpu.total.pct) BY host.name | LIMIT 10
```

Click **Check**.
""",
    "bi-03": """
# APIs, Integrations & Dashboard Building

## Part 1 — Search API (Terminal)

```bash
source ~/.bashrc
curl -s -H "Authorization: ApiKey $ES_API_KEY" \\
  -H "Content-Type: application/json" \\
  "$ES_URL/logs-*/_search" \\
  -d '{"size":3,"sort":[{"@timestamp":"desc"}]}' | jq '.hits.hits[]._source | keys'
```

## Part 2 — Dashboard for business review

1. Create a dashboard with at least two Lens panels.
2. Add a markdown panel with session context / KPI definitions.

## Part 3 — Schema considerations

Note field types in **Stack Management → Data views** — keyword vs text vs date.

Click **Check**.
""",
    "aiops-01": """
# Alert Fatigue & Noise Reduction

## Part 1 — Review existing rules

1. **Observability → Alerts → Rules**.
2. Sort by **active alerts** or **recent executions**.

## Part 2 — Tune a rule

1. Open a threshold rule — adjust window, threshold, or grouping.
2. Enable **deduplication** or **suppress duplicates** where available.

## Part 3 — Triage workflow

1. **Observability → Alerts** — practice acknowledging and adding notes.
2. Create a **maintenance window** (if applicable).

## Part 4 — Goal

Document one rule change that would reduce noise for SLB's alert volume.

Click **Check**.
""",
    "aiops-02": """
# AI-Assisted Investigation & Automated Response

## Part 1 — AI Assistant

1. Open **AI Assistant** from Observability (Observability AI Assistant).
2. Ask: "What services had the highest error rate in the last hour?"

## Part 2 — Correlation

1. From an alert, open **Investigate in APM / Logs**.
2. Correlate logs, metrics, and traces for one incident.

## Part 3 — Workflows (if enabled)

1. **Management → Workflows** — review available workflow templates.
2. Discuss automated remediation patterns with facilitator.

Click **Check**.
""",
}


def slug_section_map() -> dict[str, str]:
    with SECTIONS.open() as f:
        data = yaml.safe_load(f)
    out: dict[str, str] = {}
    for section in data["sections"]:
        sid = section["id"]
        for slug in section["tracks"]:
            out[slug] = sid
    return out


def section_tag(section_id: str) -> str:
    with SECTIONS.open() as f:
        data = yaml.safe_load(f)
    for section in data["sections"]:
        if section["id"] == section_id:
            return section["tag"]
    return f"slb-section-{section_id}"


def tags_for(workshop: dict, section_id: str) -> list[str]:
    return ["slb", "slb-workshops", section_tag(section_id)] + [
        t for t in BASE_TAGS if t not in {"slb", "slb-workshops"}
    ]

BASE_TAGS = [
    "slb",
    "slb-workshops",
    "elastic",
    "serverless",
    "observability",
    "co.elastic.workshops",
]


def assignment_md(workshop: dict) -> str:
    wid = workshop["id"]
    body = LABS.get(wid, f"\n# {workshop['title']}\n\nLab content TBD.\n")
    topics_md = "\n".join(f"- {t}" for t in workshop.get("topics", []))
    front = f"""---
slug: {wid}-lab
type: challenge
title: "{workshop['code']} — {workshop['title']}"
teaser: "{workshop['description'].strip().replace(chr(10), ' ')[:200]}"
notes:
- type: text
  contents: |
    ## Provisioning your lab…

    Creating an Elastic **Observability Serverless** project for **{workshop['code']}**.
    This usually takes 2–3 minutes.

    **Live session topics:**
{chr(10).join('    - ' + t for t in workshop.get('topics', []))}
tabs:
{KIBANA_TAB}
timelimit: 0
---

{body.strip()}
"""
    return front


def track_yml(workshop: dict, slug: str, section_id: str) -> str:
    desc = workshop["description"].strip()
    with SECTIONS.open() as f:
        sections = {s["id"]: s["name"] for s in yaml.safe_load(f)["sections"]}
    section_name = sections.get(section_id, section_id)
    return f"""slug: {slug}
title: "SLB {workshop['code']} — {workshop['title']}"
teaser: |
  {desc}
description: |-
  **{workshop['code']} — {workshop['title']}**

  {desc}

  **Section:** {section_name}
  **Series:** {workshop['series']}
  **Audience:** {workshop['audience']}
  **Presenter:** {workshop['presenter']}
  **Live date:** {workshop.get('date') or 'TBD'}

  ## Session topics
{chr(10).join('  - ' + t for t in workshop.get('topics', []))}
icon: https://cdn.instruqt.com/assets/templates/kubernetes.png
tags:
{chr(10).join('  - ' + t for t in tags_for(workshop, section_id))}
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


def write_track(workshop: dict, slug: str, section_id: str) -> None:
    track_dir = TRACKS_DIR / section_id / slug
    challenge_dir = track_dir / f"01-{workshop['id']}-lab"
    scripts_dir = track_dir / "track_scripts"

    for d in (challenge_dir, scripts_dir):
        d.mkdir(parents=True, exist_ok=True)

    (track_dir / "track.yml").write_text(track_yml(workshop, slug, section_id))
    (track_dir / "config.yml").write_text((ROOT / "shared" / "config.yml").read_text())

    for name, content in [
        (scripts_dir / "setup-es3-api", SETUP_TRACK),
        (scripts_dir / "cleanup-es3-api", CLEANUP_TRACK),
        (challenge_dir / "assignment.md", assignment_md(workshop)),
        (challenge_dir / "setup-es3-api", CHALLENGE_SETUP),
        (challenge_dir / "check-es3-api", CHECK_CHALLENGE),
        (challenge_dir / "solve-es3-api", SOLVE_CHALLENGE),
    ]:
        name.write_text(content)
        if name.name != "assignment.md":
            name.chmod(0o755)

    print(f"  ✓ tracks/{section_id}/{slug}")


def main() -> None:
    with CATALOG.open() as f:
        catalog = yaml.safe_load(f)

    sections = slug_section_map()

    for ws in catalog["workshops"]:
        if ws.get("skip_generate"):
            print(f"  ⊘ skip {ws.get('instruqt_track')} (skip_generate)")
            continue
        slug = ws.get("instruqt_track")
        if not slug:
            continue
        section_id = sections.get(slug)
        if not section_id:
            print(f"  ? skip {slug} (not in catalog/sections.yaml)")
            continue
        write_track(ws, slug, section_id)

    print(f"\nGenerated tracks in {TRACKS_DIR}")


if __name__ == "__main__":
    main()
