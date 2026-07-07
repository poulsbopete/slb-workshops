---
slug: dev-03-lab
id: 25qyawoy0ntl
type: challenge
title: Dev 03 — Deployment Validation & Incident Workflows
teaser: Elastic-native workflows for validating service health and correlating telemetry.
notes:
- type: text
  contents: |-
    ## While you wait…
    
    Open the **Session slides** tab for today's deck while your Observability Serverless project provisions (~2–3 minutes).
    
    When provisioning finishes, switch to **Elastic Serverless** for the hands-on lab.
tabs:
  - title: Session slides
    type: website
    url: https://slb-workshops.vercel.app/slides/dev-03/
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
    id: 16kzhiujlkdd
difficulty: ''
timelimit: 0
enhanced_loading: null
---
> **Lab environment:** Use the **Elastic Serverless** tab only. Hands-on steps run on **Observability Serverless** with **pre-loaded SLB sample data** (logs, metrics, traces, alert rules, and an SLO). The **same observability capabilities** apply on **ECH** and **self-managed**; Serverless mainly saves platform management. Steps are copy/paste in Kibana — no terminal required.

# Deployment Validation & Incident Workflows

## Part 1 — APM service health

1. **Observability → APM → Services** — select a service.
2. Compare error rate and latency: **last 15 minutes** vs **previous day**.

## Part 2 — Correlate signals

1. From the service, open **Logs** and **Metrics** for the same time range.
2. Use **Unified view** where available.

## Part 3 — Saved validation kit

1. Save your ES|QL query in Logs Explorer (**Save**).
2. Add a **Markdown** panel on a dashboard with a post-deploy checklist.

## Part 4 — Agent Builder (optional)

In **Agents**, create or run a simple agent prompt: *Summarize deploy health for my top 3 services.*

Click **Check**.
