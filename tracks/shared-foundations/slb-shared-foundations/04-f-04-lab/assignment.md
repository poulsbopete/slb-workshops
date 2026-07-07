---
slug: f-04-lab
id: by3sx37gxyko
type: challenge
title: F-04 — Looking Forward with Elastic
teaser: First look at Elastic 9.x and what it means for SLB SRE.
notes:
- type: text
  contents: "## While you wait…\n\n<iframe src=\"https://slb-workshops.vercel.app/slides/f-04/\"\
    \n  width=\"100%\" height=\"1400\" frameborder=\"0\"\n  style=\"border-radius:8px;display:block;width:100%;min-height:900px\"\
    >\n</iframe>\n\n*Provisioning your **Observability Serverless** lab for **F-04**\
    \ (usually 2–3 minutes). Same Kibana workflows apply on **ECH** and **self-managed**.*"
- type: text
  contents: '## Session topics

    - What''s new in Elastic 9.x

    - What to expect during the migration

    - Key features relevant to SLB SRE

    - Roadmap highlights

    '
tabs:
- id: choly6ztcbdi
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

# Looking Forward with Elastic

## Part 1 — What's new

1. From Kibana Home, open **What's new** / release highlights.
2. Note cross-deployment features: **Streams**, **Agent Builder**, **Workflows**, enhanced **AI Assistant**.

## Part 2 — Hands-on preview

1. **Observability → Streams** — managed ingestion routing.
2. **Agents** — open **Agent Builder** (or AI Assistant) and ask: *What observability data do I have?*

## Part 3 — SLB roadmap

With facilitator, identify one capability to pilot on your target deployment (Streams, SLOs, AI investigation, or Workflows).

Click **Check**.
