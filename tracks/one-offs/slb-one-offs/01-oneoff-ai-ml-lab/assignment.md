---
slug: oneoff-ai-ml-lab
id: y47gpnfmoqry
type: challenge
title: One-off — AI/ML Overview
teaser: One-off demo session — Elastic AI/ML capabilities across observability use
  cases.
notes:
- type: text
  contents: |-
    ## While you wait…

    <iframe src="https://slb-workshops.vercel.app/slides/oneoff-ai-ml/"
      width="100%" height="1400" frameborder="0"
      style="border-radius:8px;display:block;width:100%;min-height:900px">
    </iframe>

    *Provisioning your **Observability Serverless** lab for **One-off** (usually 2–3 minutes). Same Kibana workflows apply on **ECH** and **self-managed**.*
- type: text
  contents: |
    ## Session topics
    - Overview of Elastic AI/ML capabilities for observability
    - Anomaly detection and log pattern analysis
    - AI Assistant for Observability
tabs:
- id: 4nbmvhjpwo3w
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
> **Lab environment:** Use the **Elastic Serverless** tab only. Hands-on steps run on **Observability Serverless** with **pre-loaded SLB sample data** (logs, metrics, traces, and alert rules). The **same observability capabilities** apply on **ECH** and **self-managed**; Serverless mainly saves platform management. Steps are copy/paste in Kibana — no terminal required.

# AI/ML on Observability

## Part 1 — AI Assistant deep dive

Ask three questions in **AI Assistant**:

1. *Summarize error patterns in the last hour.*
2. *Which services have latency anomalies?*
3. *Draft an ES|QL query for OOM errors.*

## Part 2 — Agent Builder

1. **Agents → Agent Builder** — create or explore an agent.
2. Attach observability tools / context (as shown by facilitator).

## Part 3 — Anomalies

1. **Observability → Logs → Anomalies** or **Machine Learning** (if available).
2. Compare ML anomalies vs AI Assistant investigation — when to use each.

Click **Check**.
