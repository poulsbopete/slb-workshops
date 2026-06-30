---
slug: bi-02-lab
id: nnet8vyzftqd
type: challenge
title: BI 02 — ES|QL for Analysts
teaser: ES|QL query patterns, aggregations, and time-series analysis for analysts.
notes:
- type: text
  contents: |-
    ## While you wait…

    <iframe src="https://poulsbopete.github.io/slb-workshops/slides/bi-02/"
      width="100%" height="800" frameborder="0"
      style="border-radius:8px;display:block">
    </iframe>

    *Provisioning your Elastic **Observability Serverless** lab for **BI 02** (usually 2–3 minutes).*
tabs:
- id: rx4kavtmizgc
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
difficulty: ""
timelimit: 0
enhanced_loading: null
---

> **Serverless lab:** use the **Elastic Serverless** tab only. Every step is copy/paste in Kibana — no terminal or shell required.

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
