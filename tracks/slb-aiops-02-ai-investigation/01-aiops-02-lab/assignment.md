---
slug: aiops-02-lab
id: lensuyy3ex7v
type: challenge
title: AIOps 02 — AI-Assisted Investigation & Automated Response
teaser: AI-assisted investigation and automated remediation workflows.
notes:
- type: text
  contents: |
    ## Provisioning your lab…

    Creating an Elastic **Observability Serverless** project for **AIOps 02**.
    This usually takes 2–3 minutes.

    **Live session topics:**
    - Intelligent alert investigation with AI Assistant for Observability
    - Root cause analysis — correlating logs, metrics, traces
    - Log pattern analysis and anomaly detection
    - Automated remediation workflows with Elastic Workflows
tabs:
- id: hnyw92buxccz
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
- id: yj7xkz1ssshz
  title: Terminal
  type: terminal
  hostname: es3-api
difficulty: ""
timelimit: 0
enhanced_loading: null
---

# AI-Assisted Investigation & Automated Response

## Part 1 — AI Assistant

1. Open **AI Assistant** from Observability (Observability AI Assistant).
2. Ask: "What services had the highest error rate in the last hour?"

## Part 2 — Correlation

1. From an alert, open **Investigate in APM / Logs**.
2. Correlate logs, metrics, and traces for one incident.

## Part 3 — Workflows (if enabled)

1. **Management → Workflows** — review available workflow templates.
2. Discuss automated remediation patterns with facilitator.

Click **Check**.
