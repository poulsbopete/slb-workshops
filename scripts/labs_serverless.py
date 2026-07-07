"""Lab bodies for SLB workshops — labs run on Observability Serverless; skills apply on ECH and on-prem."""

LABS: dict[str, str] = {
    "f-01": """
# Your Elastic Team, Support & Best Practices

## Part 1 — Your lab project

1. Open the **Elastic Serverless** tab (Kibana Home).
2. Note the project type: **Observability Serverless** — our hands-on environment; the same Kibana apps apply on **ECH** and **self-managed**.
3. Click **Help** (?) — bookmark **Documentation** and support paths.

## Part 2 — Support readiness

Draft a support ticket template (works for any deployment):

| Field | Your answer |
|-------|-------------|
| Deployment | Serverless / ECH / self-managed |
| Project or cluster ID | |
| Symptom | |
| Time range | |
| ES|QL or query tried | |

## Part 3 — Enablement program

With your facilitator, pick the SME track that matches your role.

Click **Check**.
""",
    "f-02": """
# Intro to Elastic Observability

## Part 1 — Platform tour

1. **Observability → Overview** — unified logs, metrics, traces, and SLOs.
2. **Observability → Streams** — routing and processing for telemetry (same concept on ECH and on-prem).
3. **Agents** (sidebar) — explore **Agent Builder** and **AI Assistant**.

## Part 2 — Persona lenses

| Persona | Start here |
|---------|------------|
| Developer | **Observability → APM → Services** |
| SRE / Infra | **Streams** and **Alerts** |
| Analyst | **Analytics → Discover** or **Logs → Explorer** |
| Architect | **Stack Management → API keys** and access patterns |

## Part 3 — Deployment models (same value, different ops)

| | Serverless (this lab) | ECH | Self-managed |
|--|----------------------|-----|--------------|
| You focus on | Telemetry, alerts, SLOs | Same + cluster policy | Same + full stack ops |
| Elastic manages | Scaling, upgrades, ILM/Fleet | Hosted infrastructure | Software only |

Discuss with facilitator: which model fits each SLB use case.

Click **Check**.
""",
    "f-03": """
# Elastic Day to Day

## Part 1 — ES|QL in Logs Explorer

1. **Observability → Logs → Explorer** — switch to **ES|QL**.
2. Paste and run:

```esql
FROM logs-* | WHERE @timestamp > NOW() - 1 hour | LIMIT 20
```

3. Add a breakdown:

```esql
FROM logs-* | STATS count = COUNT(*) BY service.name | SORT count DESC | LIMIT 10
```

## Part 2 — Grafana → Elastic translation

| Grafana habit | Elastic Observability |
|---------------|----------------------|
| Explore | Logs Explorer / Discover |
| Panel | Lens on Dashboards |
| PromQL | ES|QL or **Metrics** explorer |
| Alert | **Alerts → Rules** |

## Part 3 — Streams quick look

1. Open **Observability → Streams**.
2. Browse how telemetry is organized — on ECH/on-prem you may also tune ILM; Streams handle routing in all deployments.

Click **Check**.
""",
    "f-04": """
# Looking Forward with Elastic

## Part 1 — What's new

1. From Kibana Home, open **What's new** / release highlights.
2. Note cross-deployment features: **Streams**, **Agent Builder**, **Workflows**, enhanced **AI Assistant**.

## Part 2 — Hands-on preview

1. **Observability → Streams** — managed ingestion routing.
2. **Agents** — open **Agent Builder** (or AI Assistant) and ask: *What observability data do I have?*

## Part 3 — SLB roadmap

With facilitator, identify one capability to pilot on your target deployment (Streams, SLOs, AI investigation, or Workflows).

Click **Check**.
""",
    "dev-01": """
# Elastic UI & Dashboard Workflows

## Part 1 — Discover & Explorer

1. **Analytics → Discover** or **Logs → Explorer** — explore available data.
2. Add a filter on `service.name` or `log.level`.
3. Save the search for reuse.

## Part 2 — Lens dashboards

1. **Analytics → Dashboards → Create dashboard**.
2. Add a **Lens** time series — event volume over time.
3. Add a **Drilldown** to open filtered logs on click.

## Part 3 — AI shortcut

Open **AI Assistant** and ask: *Show me error logs in the last hour by service.*

Click **Check**.
""",
    "dev-02": """
# ES|QL Essentials for Troubleshooting

## Part 1 — Syntax (Logs Explorer → ES|QL)

```esql
FROM logs-* | WHERE @timestamp > NOW() - 1 hour | LIMIT 20
```

```esql
FROM logs-* | STATS errors = COUNT(*) BY service.name | SORT errors DESC | LIMIT 10
```

## Part 2 — Metrics & traces

```esql
FROM metrics-* | STATS avg_cpu = AVG(system.cpu.total.pct) BY host.name | LIMIT 10
```

```esql
FROM traces-* | WHERE @timestamp > NOW() - 30 minutes | LIMIT 10
```

## Part 3 — Incident workflow

1. Find the noisiest service in the last hour.
2. Filter ERROR logs for that service.
3. Ask **AI Assistant**: *What changed for this service recently?*

Click **Check**.
""",
    "dev-03": """
# Deployment Validation & Incident Workflows

## Part 1 — APM service health

1. **Observability → APM → Services** — select a service.
2. Compare error rate and latency: **last 15 minutes** vs **previous day**.

## Part 2 — Correlate signals

1. From the service, open **Logs** and **Metrics** for the same time range.
2. Use **Unified view** where available.

## Part 3 — Saved validation kit

1. Save your ES|QL query in Logs Explorer (**Save**).
2. Add a **Markdown** panel on a dashboard with a post-deploy checklist.

## Part 4 — Agent Builder (optional)

In **Agents**, create or run a simple agent prompt: *Summarize deploy health for my top 3 services.*

Click **Check**.
""",
    "sre-01": """
# Platform Operations Fundamentals

## Part 1 — OTel ingestion (all deployments)

1. **Observability → Add data** (or **Integrations**) — review **OpenTelemetry** and OTLP endpoints.
2. In this **Serverless lab**, Fleet agents and node roles are not in scope — on **ECH/on-prem** your team operates that layer.

## Part 2 — Streams foundation

1. **Observability → Streams** — browse stream definitions and routing.
2. Discuss with facilitator: Streams simplify routing vs manual ingest pipelines; on self-managed/ECH you may pair Streams with ILM for retention.

## Part 3 — Confirm telemetry (ES|QL)

In **Logs → Explorer** (ES|QL):

```esql
FROM logs-* | STATS streams = COUNT(*) BY data_stream.dataset | SORT streams DESC | LIMIT 10
```

## Part 4 — Dev Tools (optional)

**Management → Dev Tools**:

```
GET _data_stream/logs-*
```

Review data stream names — retention is **project-managed here**; on ECH/on-prem you configure **ILM** instead.

Click **Check**.
""",
    "sre-02": """
# Elastic Streams & Data Routing

> **In this lab:** Retention is project-managed (no ILM UI). On **ECH/self-managed** you use **ILM** for lifecycle — **Streams** routing and processing work the same either way.

## Part 1 — Streams tour

1. **Observability → Streams** — open the Streams management view.
2. Review how logs, metrics, and traces flow through streams.
3. Note any **processing** or **routing** rules visible in the UI.

## Part 2 — Query stream-backed data

In **Logs → Explorer** (ES|QL):

```esql
FROM logs-* | STATS volume = COUNT(*) BY bucket = BUCKET(@timestamp, 1 hour) | SORT bucket DESC | LIMIT 24
```

Identify peak ingest windows — capacity is auto-scaled in Serverless; on ECH/on-prem you plan shard and tier capacity.

## Part 3 — Retention & governance

1. **Stack Management → Project settings** (or **Management** overview) — note how retention is set in this lab.
2. With facilitator, compare **what you control** across deployment models:

| You control (all deployments) | Ops burden differs by deployment |
|-------------------------------|----------------------------------|
| OTel schema & labels | Serverless: Elastic manages scaling & base retention |
| Streams routing rules | ECH: hosted cluster + ILM policies |
| Alerts & SLOs | Self-managed: you run Fleet, nodes, ILM, upgrades |

## Part 4 — Troubleshooting routing

1. In **Streams**, check for failed or lagging streams (if indicators are shown).
2. Use **AI Assistant**: *Are any streams dropping data in the last hour?*

Click **Check**.
""",
    "sre-03": """
# Ingestion Architecture & Troubleshooting

## Part 1 — OTel → Elastic OTLP

1. **Observability → Add data → OpenTelemetry** — review the OTLP endpoint pattern.
2. Compare with your current Grafana/Prometheus export path (facilitator-led) — same OTel path works on ECH and on-prem.

## Part 2 — Diagnose gaps in ES|QL

```esql
FROM logs-* | STATS count = COUNT(*) BY bucket = BUCKET(@timestamp, 5 minutes) | SORT bucket DESC
```

Look for missing buckets = possible ingest gaps.

## Part 3 — Streams health

1. **Observability → Streams** — check stream status indicators.
2. **Observability → Logs → Anomalies** (if enabled) — review unusual patterns.

## Part 4 — Error logs

```esql
FROM logs-* | WHERE message LIKE "*error*" OR log.level == "error" | LIMIT 20
```

Click **Check**.
""",
    "sre-04": """
# Production Readiness Workshop

## Part 1 — Readiness checklist (any deployment)

- [ ] OTel data flowing (Logs / Metrics / Traces explorers)
- [ ] **Streams** configured for key telemetry types
- [ ] Critical **alert rules** enabled
- [ ] **SLOs** defined for top services
- [ ] Dashboards for daily review
- [ ] **AI Assistant** / runbooks documented
- [ ] (ECH/on-prem) ILM / Fleet / capacity reviewed

## Part 2 — SLOs & alerts

1. **Observability → SLOs** — browse or create an SLO for a key service.
2. **Alerts → Rules** — confirm rules are not flapping.

## Part 3 — Workflows preview

1. **Management → Workflows** — review templates for alert notification.
2. Add a **Markdown** dashboard panel with escalation contacts.

Click **Check**.
""",
    "arch-01": """
# Architecture & Migration Strategy

## Part 1 — Target state

1. **Observability → Add data** — map OTel collectors → **Elastic OTLP** (Serverless, ECH, or self-managed endpoint).
2. **Streams** — sketch routing for logs / metrics / traces by team or domain.

## Part 2 — Coexistence plan

| Phase | Grafana / Prometheus | Elastic (your deployment) |
|-------|---------------------|---------------------------|
| Now | Primary | Pilot (Serverless, ECH, or on-prem) |
| Migration | Side-by-side | Streams + ES|QL |
| Target | Optional retained | Primary observability |

## Part 3 — Access & API keys

1. **Stack Management → API keys** — note patterns for automation and multi-team access.
2. Discuss boundaries: project keys (Serverless) vs deployment keys (ECH) vs cluster RBAC (self-managed).

Click **Check**.
""",
    "arch-02": """
# Governance, Streams & Standards

> **Retention:** This lab uses project-managed retention. On **ECH/on-prem**, pair **Streams** standards with your **ILM** policies — routing and lifecycle are separate concerns.

## Part 1 — Streams naming & ownership

1. **Observability → Streams** — document naming conventions for SLB teams.
2. Define owners per stream / dataset.

## Part 2 — ECS vs OTel semantics

Compare field naming for one log type:

| ECS field | OTel equivalent |
|-----------|-----------------|
| `service.name` | `service.name` |
| `host.name` | `host.name` |
| `log.level` | `severity_text` |

Pick one convention for SLB and stick to it in OTel resource attributes.

## Part 3 — Agent Builder governance

1. Open **Agents** — review who can create agents and connect tools.
2. Draft a policy: when to use **AI Assistant** vs automated **Workflows** (same rules on any deployment).

Click **Check**.
""",
    "bi-01": """
# Dashboard & Data Exploration Basics

## Part 1 — Discover

1. **Analytics → Discover** — select observability data.
2. Time picker: **Last 24 hours** — add columns and sort.

## Part 2 — Lens

1. **Visualize → Lens** — bar chart of events over time.
2. Save to a new dashboard.

## Part 3 — ES|QL peek

In **Logs → Explorer**:

```esql
FROM logs-* | STATS count = COUNT(*) BY service.name | SORT count DESC | LIMIT 10
```

Click **Check**.
""",
    "bi-02": """
# ES|QL for Analysts

## Part 1 — Aggregations

```esql
FROM logs-* | STATS events = COUNT(*) BY service.name | SORT events DESC | LIMIT 10
```

## Part 2 — Time series

```esql
FROM logs-* | STATS count = COUNT(*) BY bucket = BUCKET(@timestamp, 1 hour) | SORT bucket
```

## Part 3 — Metrics correlation

```esql
FROM metrics-* | STATS avg_cpu = AVG(system.cpu.total.pct) BY host.name | LIMIT 10
```

Ask **AI Assistant** to explain a spike in plain language.

Click **Check**.
""",
    "bi-03": """
# APIs, Integrations & Dashboard Building

## Part 1 — Search API (Dev Tools)

```
GET logs-*/_search
{
  "size": 3,
  "sort": [{ "@timestamp": "desc" }]
}
```

## Part 2 — Business dashboard

1. **Analytics → Dashboards → Create dashboard**.
2. Add two **Lens** panels + one **Markdown** KPI panel.

## Part 3 — Field types

1. **Stack Management → Data views** — inspect keyword vs text vs date fields.
2. Same Search and ES|QL APIs on Serverless, ECH, and self-managed — only the endpoint and auth model differ.

Click **Check**.
""",
    "aiops-01": """
# Alert Fatigue & Noise Reduction

## Part 1 — Review rules

1. **Alerts → Rules** — sort by recent activity.
2. Identify noisy rules.

## Part 2 — Tune a rule

Adjust threshold, window, or grouping. Enable deduplication / suppression if available.

## Part 3 — Triage

1. **Alerts** — acknowledge and annotate an alert.
2. Use **AI Assistant**: *Why might this alert be firing repeatedly?*

Click **Check**.
""",
    "aiops-02": """
# AI-Assisted Investigation & Automated Response

## Part 1 — AI Assistant

1. Open **AI Assistant** from Observability.
2. Ask: *What services had the highest error rate in the last hour?*
3. Follow up: *Show correlated logs and traces.*

## Part 2 — Agent Builder

1. Open **Agents** in the sidebar.
2. Explore prebuilt agents or create a simple investigation agent.
3. Connect it to observability context (facilitator demo).

## Part 3 — From alert to root cause

1. Open an active alert → **Investigate in APM / Logs**.
2. Correlate logs, metrics, and traces for one incident.

Click **Check**.
""",
    "aiops-03": """
# Workflows & Automated Remediation

## Part 1 — Workflows

1. **Management → Workflows** — browse templates.
2. Review connectors (Slack, email, webhook).

## Part 2 — Alert-driven automation

1. **Alerts → Rules** — open a rule's **Actions**.
2. Map which workflow could run on trigger.

## Part 3 — Safe automation design

| Step | Guardrail |
|------|-----------|
| Trigger | Alert threshold + SLO breach |
| Action | Notify + runbook link |
| Approval | Human in the loop before remediation |

Click **Check**.
""",
    "oneoff-ai-ml": """
# AI/ML on Observability

## Part 1 — AI Assistant deep dive

Ask three questions in **AI Assistant**:

1. *Summarize error patterns in the last hour.*
2. *Which services have latency anomalies?*
3. *Draft an ES|QL query for OOM errors.*

## Part 2 — Agent Builder

1. **Agents → Agent Builder** — create or explore an agent.
2. Attach observability tools / context (as shown by facilitator).

## Part 3 — Anomalies

1. **Observability → Logs → Anomalies** or **Machine Learning** (if available).
2. Compare ML anomalies vs AI Assistant investigation — when to use each.

Click **Check**.
""",
    "oneoff-rag-mcp": """
# RAG, Agents & MCP

## Part 1 — Agent Builder + retrieval

1. **Agents → Agent Builder** — open an agent with knowledge retrieval.
2. Ask a question grounded in your observability documentation or runbooks.

## Part 2 — MCP concept

With facilitator, discuss how **Model Context Protocol (MCP)** tools could expose:

- ES|QL query results
- Stream metadata
- Alert history

## Part 3 — Practical pattern

Document one SLB use case: *Agent answers "what changed?" using logs + traces via MCP tools.*

Click **Check**.
""",
    "oneoff-hybrid-search": """
# Hybrid Search for Observability

## Part 1 — Keyword search (Dev Tools)

```
GET logs-*/_search
{
  "query": { "match": { "message": "timeout connection refused" } },
  "size": 5
}
```

## Part 2 — ES|QL + AI

1. Run an ES|QL query for errors in **Logs → Explorer**.
2. Ask **AI Assistant**: *Find logs semantically similar to this error pattern.*

## Part 3 — When to use hybrid search

List one scenario where semantic + keyword beats either alone (e.g. varied error messages for the same root cause).

Click **Check**.
""",
    "cross-team": """
# Cross-team Platform Review

## Part 1 — Adoption snapshot

1. **Observability → Overview** — active signals across logs, metrics, traces.
2. **Streams** — how many routes are in production use?
3. **Agents** — any team agents deployed?

## Part 2 — Maturity checklist

| Capability | Team using it? |
|------------|----------------|
| ES|QL daily | |
| Streams | |
| SLOs | |
| AI Assistant | |
| Workflows | |

## Part 3 — Next steps

List one action item per persona track before the next live session.

Click **Check**.
""",
}
