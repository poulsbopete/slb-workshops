---
slug: cross-team-lab
id: voem0yxaqp7l
type: challenge
title: Cross-team — Cross-team Platform Review
teaser: Cross-team session reviewing adoption progress and next steps.
notes:
- type: text
  contents: |-
    <iframe src="https://slb-workshops.vercel.app/slides/cross-team/"
      width="100%" height="1400" frameborder="0"
      style="border-radius:8px;display:block;width:100%;min-height:900px">
    </iframe>
tabs:
- id: ahuakfmqw6b5
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

# Cross-team Platform Review

## Part 1 — Adoption snapshot

1. **Observability → Overview** — active signals across logs, metrics, traces.
2. **Streams** — how many routes are in production use?
3. **Agents** — any team agents deployed?

## Part 2 — Maturity checklist

| Capability | Team using it? |
|------------|----------------|
| ES|QL daily | |
| Streams | |
| SLOs | |
| AI Assistant | |
| Workflows | |

## Part 3 — Next steps

List one action item per persona track before the next live session.

Click **Check**.
