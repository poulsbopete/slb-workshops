---
slug: dev-02-lab
id: ap6loltg3ylx
type: challenge
title: Dev 02 — ES|QL Essentials for Troubleshooting
teaser: Core ES|QL syntax, common patterns, and queries across logs, metrics, and
  traces.
notes:
- type: text
  contents: |-
    ## While you wait…

    <iframe src="https://poulsbopete.github.io/slb-workshops/slides/dev-02/"
      width="100%" height="800" frameborder="0"
      style="border-radius:8px;display:block">
    </iframe>

    *Provisioning your Elastic **Observability Serverless** lab for **Dev 02** (usually 2–3 minutes).*
tabs:
- id: jzljtmzm5amx
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
