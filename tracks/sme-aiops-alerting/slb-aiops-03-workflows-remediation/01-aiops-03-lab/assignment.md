---
slug: aiops-03-lab
id: 67n5mh5xpcni
type: challenge
title: AIOps 03 — Workflows & Automated Remediation
teaser: Build and test automated remediation workflows triggered from observability
  alerts.
notes:
- type: text
  contents: |-
    ## While you wait…

    <iframe src="https://poulsbopete.github.io/slb-workshops/slides/aiops-03/"
      width="100%" height="800" frameborder="0"
      style="border-radius:8px;display:block">
    </iframe>

    *Provisioning your Elastic **Observability Serverless** lab for **AIOps 03** (usually 2–3 minutes).*
- type: text
  contents: |
    ## Session topics
    - Elastic Workflows for alert-driven automation
    - Connector patterns — Slack, PagerDuty, webhooks
    - Safe remediation guardrails and approval steps
tabs:
- id: omxsz5hkwtxv
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

> **Serverless lab:** use the **Elastic Serverless** tab only. Every step is copy/paste in Kibana — no terminal or shell required.

# Workflows & Automated Remediation

## Part 1 — Explore Workflows

1. Open **Management → Workflows** (or **Stack Management → Connectors and Actions**).
2. Review available workflow templates and connectors.

## Part 2 — Alert-driven automation

1. **Observability → Alerts → Rules** — open a rule.
2. Note **Actions** / **Connectors** that could trigger a workflow.

## Part 3 — Design a safe remediation

Document a workflow with:

| Step | Guardrail |
|------|-----------|
| Trigger | Alert threshold |
| Action | Notify / runbook link |
| Approval | Human in the loop |

Click **Check**.
