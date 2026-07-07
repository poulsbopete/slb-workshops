---
slug: dev-02-lab
id: isacwit1rsev
type: challenge
title: Dev 02 — ES|QL Essentials for Troubleshooting
teaser: Core ES|QL syntax, common patterns, and queries across logs, metrics, and
  traces.
notes:
- type: text
  contents: "## While you wait…\n\n<iframe src=\"https://slb-workshops.vercel.app/slides/dev-02/\"\
    \n  width=\"100%\" height=\"1400\" frameborder=\"0\"\n  style=\"border-radius:8px;display:block;width:100%;min-height:900px\"\
    >\n</iframe>\n\n*Provisioning your **Observability Serverless** lab for **Dev\
    \ 02** (usually 2–3 minutes). Same Kibana workflows apply on **ECH** and **self-managed**.*"
- type: text
  contents: '## Session topics

    - Core ES|QL syntax and common patterns

    - Logs/metrics/traces query patterns

    - Incident investigation workflows

    '
tabs:
- id: p4ses0nqfjda
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
