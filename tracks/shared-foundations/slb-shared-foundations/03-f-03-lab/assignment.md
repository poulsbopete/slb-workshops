---
slug: f-03-lab
id: wedpg7tppltb
type: challenge
title: F-03 — Elastic Day to Day
teaser: Practical examples of data ingestion, querying with ES|QL, and using Kibana
  dashboards — with a focus on what Grafana users need to know.
notes:
- type: text
  contents: "## While you wait…\n\n<iframe src=\"https://slb-workshops.vercel.app/slides/f-03/\"\
    \n  width=\"100%\" height=\"1400\" frameborder=\"0\"\n  style=\"border-radius:8px;display:block;width:100%;min-height:900px\"\
    >\n</iframe>\n\n*Provisioning your **Observability Serverless** lab for **F-03**\
    \ (usually 2–3 minutes). Same Kibana workflows apply on **ECH** and **self-managed**.*"
- type: text
  contents: '## Session topics


    - ES|QL and Streams in daily workflows

    - Where dashboards and AI Assistant fit

    - OTel ingestion patterns (lab runs on Serverless)

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
> **Lab environment:** Use the **Elastic Serverless** tab only. Hands-on steps run on **Observability Serverless** with **pre-loaded SLB sample data** (logs, metrics, traces, alert rules, and an SLO). The **same observability capabilities** apply on **ECH** and **self-managed**; Serverless mainly saves platform management. Steps are copy/paste in Kibana — no terminal required.

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
