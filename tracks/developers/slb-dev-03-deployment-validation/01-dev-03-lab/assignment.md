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
- type: text
  contents: |
    ## Provisioning your lab…

    Creating an Elastic **Observability Serverless** project for **Dev 03**.
    This usually takes 2–3 minutes.

    **Live session topics:**
    - Service health checks after deployments
    - Correlating telemetry sources (logs, metrics, traces)
    - Saved queries and views for daily use
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
- id: jez8jaapq957
  title: Terminal
  type: terminal
  hostname: es3-api
difficulty: ""
timelimit: 0
enhanced_loading: null
---

# Deployment Validation & Incident Workflows

## Part 1 — Service health after deploy

1. **Observability → APM → Services** — pick a service (or use sample data).
2. Compare error rate and latency for **last 15 minutes** vs **previous day**.

## Part 2 — Correlate logs, metrics, traces

1. From a service view, pivot to **Logs** and **Metrics** for the same time range.
2. Use **Unified view** or split tabs to correlate signals.

## Part 3 — Saved views

1. Save an ES|QL query as a **saved search**.
2. Pin a dashboard panel for post-deploy validation.

## Part 4 — Runbook snippet (Terminal)

Document your validation query in a note:

```bash
source ~/.bashrc
echo "Post-deploy check: FROM logs-* | WHERE service.environment == 'production' ..."
```

Click **Check**.
