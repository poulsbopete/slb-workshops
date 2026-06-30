---
slug: sre-03-lab
id: nexmo5rmxpmw
type: challenge
title: SRE 03 — Ingestion Architecture & Troubleshooting
teaser: Elastic Agent vs OTel tradeoffs, Prometheus ingestion, and failure store handling.
notes:
- type: text
  contents: |-
    ## While you wait…

    <iframe src="https://poulsbopete.github.io/slb-workshops/slides/sre-03/"
      width="100%" height="800" frameborder="0"
      style="border-radius:8px;display:block">
    </iframe>

    *Provisioning your Elastic **Observability Serverless** lab for **SRE 03** (usually 2–3 minutes).*
tabs:
- id: 7qsvzoxxwzgp
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
