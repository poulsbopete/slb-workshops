---
slug: dev-03-lab
id: nc21uboysr3h
type: challenge
title: Dev 03 — Deployment Validation & Incident Workflows
teaser: Elastic-native workflows for validating service health and correlating telemetry.
notes:
- type: text
  contents: |-
    ## While you wait…

    <iframe src="https://poulsbopete.github.io/slb-workshops/slides/dev-03/"
      width="100%" height="800" frameborder="0"
      style="border-radius:8px;display:block">
    </iframe>

    *Provisioning your Elastic **Observability Serverless** lab for **Dev 03** (usually 2–3 minutes).*
tabs:
- id: dk3ybid9w7rd
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

# Deployment Validation & Incident Workflows

## Part 1 — Service health after deploy

1. **Observability → APM → Services** — pick a service (or use sample data).
2. Compare error rate and latency for **last 15 minutes** vs **previous day**.

## Part 2 — Correlate logs, metrics, traces

1. From a service view, pivot to **Logs** and **Metrics** for the same time range.
2. Use **Unified view** or split tabs to correlate signals.

## Part 3 — Saved views

1. Save an ES|QL query as a **saved search** (**Save** in the ES|QL editor).
2. Pin a dashboard panel for post-deploy validation.

## Part 4 — Runbook in Kibana

1. Open your dashboard (or create one) and add a **Markdown** panel.
2. Paste a short post-deploy checklist, for example:

```
Post-deploy check (ES|QL):
FROM logs-* | WHERE service.environment == "production" | LIMIT 20
```

Click **Check**.
