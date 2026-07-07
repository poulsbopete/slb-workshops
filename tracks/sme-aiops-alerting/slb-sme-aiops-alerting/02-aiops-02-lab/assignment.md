---
slug: aiops-02-lab
id: pcdlxe6qc1yd
type: challenge
title: AIOps 02 — AI-Assisted Investigation & Automated Response
teaser: AI-assisted investigation and automated remediation workflows.
notes:
- type: text
  contents: |-
    ## While you wait…

    <iframe src="https://slb-workshops.vercel.app/slides/aiops-02/"
      width="100%" height="1400" frameborder="0"
      style="border-radius:8px;display:block;width:100%;min-height:900px">
    </iframe>

    *Provisioning your **Observability Serverless** lab for **AIOps 02** (usually 2–3 minutes). Same Kibana workflows apply on **ECH** and **self-managed**.*
- type: text
  contents: |
    ## Session topics
    - Intelligent alert investigation with AI Assistant for Observability
    - Root cause analysis — correlating logs, metrics, traces
    - Log pattern analysis and anomaly detection
    - Automated remediation workflows with Elastic Workflows
tabs:
- id: jut8ttqqn8c4
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

# AI-Assisted Investigation & Automated Response

## Part 1 — AI Assistant

1. Open **AI Assistant** from Observability.
2. Ask: *What services had the highest error rate in the last hour?*
3. Follow up: *Show correlated logs and traces.*

## Part 2 — Agent Builder

1. Open **Agents** in the sidebar.
2. Explore prebuilt agents or create a simple investigation agent.
3. Connect it to observability context (facilitator demo).

## Part 3 — From alert to root cause

1. Open an active alert → **Investigate in APM / Logs**.
2. Correlate logs, metrics, and traces for one incident.

Click **Check**.
