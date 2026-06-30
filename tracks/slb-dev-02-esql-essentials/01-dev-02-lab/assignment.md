---
slug: dev-02-lab
id: ap6loltg3ylx
type: challenge
title: Dev 02 — ES|QL Essentials for Troubleshooting
teaser: Core ES|QL syntax, common patterns, and queries across logs, metrics, and
  traces.
notes:
- type: text
  contents: |
    ## Provisioning your lab…

    Creating an Elastic **Observability Serverless** project for **Dev 02**.
    This usually takes 2–3 minutes.

    **Live session topics:**
    - Core ES|QL syntax and common patterns
    - Logs/metrics/traces query patterns
    - Incident investigation workflows
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
- id: oqayvaidbcg0
  title: Terminal
  type: terminal
  hostname: es3-api
difficulty: ""
timelimit: 0
enhanced_loading: null
---

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
