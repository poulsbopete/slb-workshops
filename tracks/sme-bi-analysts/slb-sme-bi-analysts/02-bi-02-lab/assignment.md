---
slug: bi-02-lab
id: kuxqfixtmstj
type: challenge
title: BI 02 — ES|QL for Analysts
teaser: ES|QL query patterns, aggregations, and time-series analysis for analysts.
notes:
- type: text
  contents: |-
    ## While you wait…
    
    Open the **Session slides** tab for today's deck while your Observability Serverless project provisions (~2–3 minutes).
    
    When provisioning finishes, switch to **Elastic Serverless** for the hands-on lab.
tabs:
  - title: Session slides
    type: website
    url: https://slb-workshops.vercel.app/slides/bi-02/
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
    id: cie5ndzcqs93
difficulty: ''
timelimit: 0
enhanced_loading: null
---
> **Lab environment:** Use the **Elastic Serverless** tab only. Hands-on steps run on **Observability Serverless** with **pre-loaded SLB sample data** (logs, metrics, traces, alert rules, and an SLO). The **same observability capabilities** apply on **ECH** and **self-managed**; Serverless mainly saves platform management. Steps are copy/paste in Kibana — no terminal required.

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
