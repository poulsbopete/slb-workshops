---
slug: f-03-lab
id: wedpg7tppltb
type: challenge
title: F-03 — Elastic Day to Day
teaser: Practical examples of data ingestion, querying with ES|QL, and using Kibana
  dashboards — with a focus on what Grafana users need to know.
notes:
- type: text
  contents: "## While you wait…\n\n<iframe src=\"https://poulsbopete.github.io/slb-workshops/slides/f-03/\"\
    \n  width=\"100%\" height=\"1400\" frameborder=\"0\"\n  style=\"border-radius:8px;display:block;width:100%;min-height:900px\"\
    >\n</iframe>\n\n*Provisioning your Elastic **Observability Serverless** lab for\
    \ **F-03** (usually 2–3 minutes).*"
- type: text
  contents: '## Session topics


    - ES|QL and Streams in daily workflows

    - Where dashboards and AI Assistant fit

    - Managed OTel ingestion on Serverless

    - Grafana → Elastic mental model translation

    '
tabs:
- id: 9mthilxhx6kw
  title: Elastic Serverless
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
difficulty: ''
timelimit: 0
enhanced_loading: null
---
> **Elastic Observability Serverless** — use the **Elastic Serverless** tab only. These labs focus on **managed Serverless** capabilities (no ILM, Fleet, or self-managed tiers). Steps are copy/paste in Kibana — no terminal required.

# Elastic Day to Day on Serverless

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

## Part 2 — Grafana → Serverless translation

| Grafana habit | Elastic Serverless |
|---------------|-------------------|
| Explore | Logs Explorer / Discover |
| Panel | Lens on Dashboards |
| PromQL | ES|QL or **Metrics** explorer |
| Alert | **Observability → Alerts → Rules** |

## Part 3 — Streams quick look

1. Open **Observability → Streams**.
2. Browse how telemetry is organized — note stream names and routing (no manual index templates required).

Click **Check**.
