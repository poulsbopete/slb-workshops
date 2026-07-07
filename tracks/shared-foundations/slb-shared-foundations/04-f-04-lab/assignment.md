---
slug: f-04-lab
id: by3sx37gxyko
type: challenge
title: F-04 — Looking Forward with Elastic
teaser: First look at Elastic 9.x and what it means for SLB SRE.
notes:
- type: text
  contents: |-
    ## While you wait…
    
    Open the **Session slides** tab for today's deck while your Observability Serverless project provisions (~2–3 minutes).
    
    When provisioning finishes, switch to **Elastic Serverless** for the hands-on lab.
tabs:
  - title: Session slides
    type: website
    url: https://slb-workshops.vercel.app/slides/f-04/
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
    id: choly6ztcbdi
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
