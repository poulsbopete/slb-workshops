---
slug: aiops-03-lab
id: cfg7ndjopyei
type: challenge
title: AIOps 03 — Workflows & Automated Remediation
teaser: Build and test automated remediation workflows triggered from observability
  alerts.
notes:
- type: text
  contents: |-
    ## While you wait…

    <iframe src="https://slb-workshops.vercel.app/slides/aiops-03/"
      width="100%" height="1400" frameborder="0"
      style="border-radius:8px;display:block;width:100%;min-height:900px">
    </iframe>

    *Provisioning your **Observability Serverless** lab for **AIOps 03** (usually 2–3 minutes). Same Kibana workflows apply on **ECH** and **self-managed**.*
- type: text
  contents: |
    ## Session topics
    - Elastic Workflows for alert-driven automation
    - Connector patterns — Slack, PagerDuty, webhooks
    - Safe remediation guardrails and approval steps
tabs:
- id: ca8xascmzi6n
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
> **Lab environment:** Use the **Elastic Serverless** tab only. Hands-on steps run on **Observability Serverless** for a zero-ops learning experience. The **same observability capabilities** — ES|QL, Streams, AI Assistant, Agent Builder, Workflows, SLOs — apply on **ECH** and **self-managed**; Serverless mainly saves platform management (cluster sizing, ILM, Fleet, upgrades). Steps are copy/paste in Kibana — no terminal required.

# Workflows & Automated Remediation

## Part 1 — Workflows

1. **Management → Workflows** — browse templates.
2. Review connectors (Slack, email, webhook).

## Part 2 — Alert-driven automation

1. **Observability → Alerts → Rules** — open a rule's **Actions**.
2. Map which workflow could run on trigger.

## Part 3 — Safe automation design

| Step | Guardrail |
|------|-----------|
| Trigger | Alert threshold + SLO breach |
| Action | Notify + runbook link |
| Approval | Human in the loop before remediation |

Click **Check**.
