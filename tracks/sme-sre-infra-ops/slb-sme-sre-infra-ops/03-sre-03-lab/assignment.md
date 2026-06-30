---
slug: sre-03-lab
type: challenge
title: SRE 03 — Ingestion Architecture & Troubleshooting
teaser: Elastic Agent vs OTel tradeoffs, Prometheus ingestion, and failure store handling.
notes:
- type: text
  contents: "## While you wait…\n\n<iframe src=\"https://poulsbopete.github.io/slb-workshops/slides/sre-03/\"\
    \n  width=\"100%\" height=\"800\" frameborder=\"0\"\n  style=\"border-radius:8px;display:block\"\
    >\n</iframe>\n\n*Provisioning your Elastic **Observability Serverless** lab for\
    \ **SRE 03** (usually 2–3 minutes).*"
- type: text
  contents: '## Session topics

    - Elastic Agent integrations vs OTel-native collection tradeoffs

    - Prometheus scrape and remote_write ingestion patterns

    - Failure store and ingest error handling

    - Diagnosing dashboard instability when switching Prometheus environments

    '
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
timelimit: 0
---
> **Serverless lab:** use the **Elastic Serverless** tab only. Every step is copy/paste in Kibana — no terminal or shell required.

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
