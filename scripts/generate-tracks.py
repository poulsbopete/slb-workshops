#!/usr/bin/env python3
"""Generate consolidated Instruqt tracks (8 series tracks, multiple challenges each)."""

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
    "f-01": """
# Your Elastic Team, Support & Best Practices

## Part 1 — Navigate Kibana help resources

1. Open **Elastic Serverless** (Kibana Home).
2. Click **Help** (?) — note **Documentation**, **Support**, and **Give feedback**.
3. Open **Stack Management → Stack Monitoring** (if visible) — observe health signals.

## Part 2 — Support readiness checklist

In a Markdown panel or your notes, draft a support ticket template:

| Field | Your answer |
|-------|-------------|
| Environment | Serverless Observability |
| Symptom | |
| Time range | |
| Steps tried | |

## Part 3 — Enablement program

Discuss with facilitator: which SME track matches your role?

Click **Check**.
""",
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
    "f-04": """
# Looking Forward with Elastic — Hands-on Lab

## Part 1 — What's new in 9.x

1. Open **Elastic Serverless** → **What's new** (release highlights).
2. Browse **Stack Management → Upgrade Assistant** or release notes links.

## Part 2 — Migration preview

1. **Observability → Overview** — note unified navigation changes.
2. **Stack Management → Index Management** — review data stream defaults.

## Part 3 — SLB roadmap discussion

With facilitator, identify one Elastic 9.x feature relevant to your team's migration.

Click **Check**.
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

## Part 4 — See your indices (Dev Tools)

1. Open **Management → Dev Tools** (search “Dev Tools” in the Kibana header).
2. Paste into the console and click the **play** button:

```
GET _cat/indices?v
```

3. Scan the table for `logs-*`, `metrics-*`, and `traces-*` data streams.

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

Open **Discover** or **Observability → Logs → Explorer**, switch to **ES|QL**, and paste each query below (one at a time):

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

1. Save an ES|QL query as a **saved search** (**Save** in the ES|QL editor).
2. Pin a dashboard panel for post-deploy validation.

## Part 4 — Runbook in Kibana

1. Open your dashboard (or create one) and add a **Markdown** panel.
2. Paste a short post-deploy checklist, for example:

```
Post-deploy check (ES|QL):
FROM logs-* | WHERE service.environment == "production" | LIMIT 20
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

## Part 4 — Confirm data streams (Dev Tools)

You already browsed **Index Management** in Part 1. Optionally paste in **Management → Dev Tools**:

```
GET _data_stream
```

Review the `data_streams` names in the JSON response.

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

## Part 4 — Policy names (Dev Tools)

After reviewing policies in the UI, paste in **Management → Dev Tools**:

```
GET _ilm/policy
```

Note the policy names in the response (keys of the JSON object).

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

## Part 4 — Index health

1. **Stack Management → Index Management** — check for **red** or **yellow** health badges.
2. Optional — **Management → Dev Tools**, paste:

```
GET _cat/indices?v&health=red
```

An empty response means no red indices (good).

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

1. **Analytics → Dashboards** — open or create a dashboard.
2. Add a **Markdown** panel with your production readiness outline, for example:

```
# SLB Elastic Production Readiness
- Ingestion health checks
- Escalation contacts
- Rollback criteria
```

3. Save the dashboard.

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

In **Discover** or **Logs → Explorer** (ES|QL mode), paste:

```esql
FROM logs-* | STATS events = COUNT(*) BY service.name | SORT events DESC | LIMIT 10
```

## Part 2 — Time-based analysis

Paste in the same ES|QL editor:

```esql
FROM logs-* | STATS count = COUNT(*) BY bucket = BUCKET(@timestamp, 1 hour) | SORT bucket
```

## Part 3 — Cost / utilization correlation

Discuss with facilitator how to join observability metrics with cost data
(lookup join or separate index). Paste:

```esql
FROM metrics-* | STATS avg_cpu = AVG(system.cpu.total.pct) BY host.name | LIMIT 10
```

Click **Check**.
""",
    "bi-03": """
# APIs, Integrations & Dashboard Building

## Part 1 — Search API (Dev Tools)

1. Open **Management → Dev Tools**.
2. Paste and click **Run**:

```
GET logs-*/_search
{
  "size": 3,
  "sort": [{ "@timestamp": "desc" }]
}
```

3. In the response, expand a hit and note field names under `_source`.

**Tip:** The same data appears in **Discover** — Dev Tools shows the raw API shape analysts integrate against.

## Part 2 — Dashboard for business review

1. **Analytics → Dashboards → Create dashboard**.
2. Add at least two **Lens** panels.
3. Add a **Markdown** panel with session context / KPI definitions.

## Part 3 — Schema considerations

1. **Stack Management → Data views** — open a data view.
2. Note field types: **keyword** vs **text** vs **date**.

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
    "aiops-03": """
# Workflows & Automated Remediation

## Part 1 — Explore Workflows

1. Open **Management → Workflows** (or **Stack Management → Connectors and Actions**).
2. Review available workflow templates and connectors.

## Part 2 — Alert-driven automation

1. **Observability → Alerts → Rules** — open a rule.
2. Note **Actions** / **Connectors** that could trigger a workflow.

## Part 3 — Design a safe remediation

Document a workflow with:

| Step | Guardrail |
|------|-----------|
| Trigger | Alert threshold |
| Action | Notify / runbook link |
| Approval | Human in the loop |

Click **Check**.
""",
    "oneoff-ai-ml": """
# AI/ML Overview — Hands-on Lab

## Part 1 — AI Assistant

1. Open **AI Assistant** from Observability.
2. Ask: "Summarize error patterns in the last hour."

## Part 2 — ML features

1. **Machine Learning → Anomaly Detection** — browse job templates.
2. **Logs → Log patterns** (if available) — review pattern grouping.

## Part 3 — Use cases for SLB

Discuss with facilitator: anomaly detection vs AI Assistant vs alerting — when to use each.

Click **Check**.
""",
    "oneoff-rag-mcp": """
# RAG & MCP — Hands-on Lab

## Part 1 — Semantic search basics

1. Open **Search → Playground** or **Elasticsearch → Search** (if available).
2. Run a natural-language query against sample documents.

## Part 2 — RAG pattern

1. Note how retrieved documents ground the model response.
2. In **Dev Tools**, inspect an index with dense_vector or semantic fields (if present).

## Part 3 — MCP integration

Discuss with facilitator: how MCP tools could expose Elasticsearch indices to agent workflows.

Click **Check**.
""",
    "oneoff-hybrid-search": """
# Hybrid Search — Hands-on Lab

## Part 1 — Lexical search

1. **Dev Tools** — run a BM25 search:

```
GET logs-*/_search
{
  "query": { "match": { "message": "error timeout" } },
  "size": 5
}
```

## Part 2 — Hybrid relevance

1. Discuss combining keyword + vector scores (RRF / hybrid query).
2. Review Elastic docs on hybrid search in your facilitator's walkthrough.

## Part 3 — Observability use case

Identify one log search scenario where hybrid search beats keyword-only.

Click **Check**.
""",
    "arch-01": """
# Architecture & Migration Strategy

## Part 1 — Current state inventory

1. **Stack Management → Index Management** — list data streams and retention.
2. **Fleet** (if visible) — note agent vs OTel collection patterns.

## Part 2 — Target-state sketch

Document coexistence plan:

| Phase | Grafana | Elastic |
|-------|---------|---------|
| Now | Primary | Pilot |
| Migration | Side-by-side | Growing |
| Target | Retained? | Primary |

## Part 3 — Multi-team access

Review **Stack Management → Roles** — note space and index privileges patterns.

Click **Check**.
""",
    "arch-02": """
# Lifecycle, Governance & Standards

## Part 1 — ILM policies

1. **Stack Management → Index Lifecycle Policies**.
2. Review hot/warm/cold/frozen phases for a sample policy.

## Part 2 — Standards

Compare **ECS** vs **OTel semantic conventions** for one log type.

## Part 3 — Ownership

Draft reusable standards: naming, retention, and who owns each data stream tier.

Click **Check**.
""",
    "cross-team": """
# Cross-team Platform Review

## Part 1 — Adoption snapshot

1. **Observability → Overview** — note active data sources.
2. **Analytics → Dashboards** — browse shared dashboards.

## Part 2 — Open Q&A prep

List three questions for the live session (ingestion, alerts, ES|QL, migration).

## Part 3 — Next steps

Identify one action item for your team before the next SME session.

Click **Check**.
""",
}


BASE_TAGS = [
    "slb",
    "slb-workshops",
    "elastic",
    "serverless",
    "observability",
    "co.elastic.workshops",
]

PAGES_BASE = "https://poulsbopete.github.io/slb-workshops"
IFRAME_HEIGHT = 1400


def iframe_note(workshop: dict) -> str:
    wid = workshop["id"]
    code = workshop["code"]
    url = f"{PAGES_BASE}/slides/{wid}/"
    return (
        "    ## While you wait…\n\n"
        f'    <iframe src="{url}"\n'
        f'      width="100%" height="{IFRAME_HEIGHT}" frameborder="0"\n'
        '      style="border-radius:8px;display:block;width:100%;min-height:900px">\n'
        "    </iframe>\n\n"
        f"    *Provisioning your Elastic **Observability Serverless** lab for **{code}** "
        "(usually 2–3 minutes).*"
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
  Each lab provisions a personal **Elastic Observability Serverless** project.

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
