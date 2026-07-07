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
    
    <div style="width:100%;max-width:100%;margin:0;padding:0;">
    <iframe src="https://slb-workshops.vercel.app/slides/aiops-03/" width="100%" height="1400" frameborder="0" style="display:block;width:100%;min-width:100%;height:1400px;border:0;border-radius:8px"></iframe>
    </div>
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
difficulty: ''
timelimit: 0
enhanced_loading: null
---
> **Lab environment:** Use the **Elastic Serverless** tab only. Hands-on steps run on **Observability Serverless** with **pre-loaded SLB sample data** (logs, metrics, traces, alert rules, and an SLO). The **same observability capabilities** apply on **ECH** and **self-managed**; Serverless mainly saves platform management. Steps are copy/paste in Kibana — no terminal required.

# Workflows & Automated Remediation

## Part 1 — Workflows

1. **Management → Workflows** — browse templates.
2. Review connectors (Slack, email, webhook).

## Part 2 — Alert-driven automation

1. **Alerts → Rules** — open a rule's **Actions**.
2. Map which workflow could run on trigger.

## Part 3 — Safe automation design

| Step | Guardrail |
|------|-----------|
| Trigger | Alert threshold + SLO breach |
| Action | Notify + runbook link |
| Approval | Human in the loop before remediation |

Click **Check**.
