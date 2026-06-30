---
slug: sre-04-lab
id: qclvb0rzrc9w
type: challenge
title: SRE 04 — Production Readiness Workshop
teaser: Production readiness for Elastic Observability Serverless — SLOs, alerts,
  Streams, and AI ops.
notes:
- type: text
  contents: |-
    ## While you wait…

    <iframe src="https://poulsbopete.github.io/slb-workshops/slides/sre-04/"
      width="100%" height="1400" frameborder="0"
      style="border-radius:8px;display:block;width:100%;min-height:900px">
    </iframe>

    *Provisioning your Elastic **Observability Serverless** lab for **SRE 04** (usually 2–3 minutes).*
- type: text
  contents: |
    ## Session topics

    - SLOs, alerts, and Streams readiness on Serverless
    - AI Assistant and Workflows in production runbooks
    - Serverless validation checklist (no ILM/Fleet)
tabs:
- id: lqsvkreyeozl
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

# Production Readiness on Serverless

## Part 1 — Serverless readiness checklist

- [ ] OTel data flowing (Logs / Metrics / Traces explorers)
- [ ] **Streams** configured for key telemetry types
- [ ] Critical **alert rules** enabled
- [ ] **SLOs** defined for top services
- [ ] Dashboards for daily review
- [ ] **AI Assistant** / runbooks documented

## Part 2 — SLOs & alerts

1. **Observability → SLOs** — browse or create an SLO for a key service.
2. **Observability → Alerts → Rules** — confirm rules are not flapping.

## Part 3 — Workflows preview

1. **Management → Workflows** — review templates for alert notification.
2. Add a **Markdown** dashboard panel with escalation contacts.

Click **Check**.
