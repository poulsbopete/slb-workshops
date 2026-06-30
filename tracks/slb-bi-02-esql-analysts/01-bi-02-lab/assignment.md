---
slug: bi-02-lab
type: challenge
title: "BI 02 — ES|QL for Analysts"
teaser: "ES|QL query patterns, aggregations, and time-series analysis for analysts."
notes:
- type: text
  contents: |
    ## Provisioning your lab…

    Creating an Elastic **Observability Serverless** project for **BI 02**.
    This usually takes 2–3 minutes.

    **Live session topics:**
    - Simple query patterns and aggregations
    - Time-based analysis
    - Correlating observability data with cost and utilization context
tabs:
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
  hostname: es3-api
timelimit: 0
---

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
