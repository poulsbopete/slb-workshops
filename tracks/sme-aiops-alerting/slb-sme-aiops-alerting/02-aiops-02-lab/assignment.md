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

    <iframe src="https://poulsbopete.github.io/slb-workshops/slides/aiops-02/"
      width="100%" height="1400" frameborder="0"
      style="border-radius:8px;display:block;width:100%;min-height:900px">
    </iframe>

    *Provisioning your Elastic **Observability Serverless** lab for **AIOps 02** (usually 2–3 minutes).*
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
> **Elastic Observability Serverless** — use the **Elastic Serverless** tab only. These labs focus on **managed Serverless** capabilities (no ILM, Fleet, or self-managed tiers). Steps are copy/paste in Kibana — no terminal required.

# AI-Assisted Investigation (Serverless)

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
