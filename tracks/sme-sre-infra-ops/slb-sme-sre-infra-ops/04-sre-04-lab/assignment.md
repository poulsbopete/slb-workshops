---
slug: sre-04-lab
id: qclvb0rzrc9w
type: challenge
title: SRE 04 — Production Readiness Workshop
teaser: Production readiness for Elastic Observability — SLOs, alerts, Streams, and
  AI ops on any deployment.
notes:
- type: text
  contents: |-
    <iframe src="https://slb-workshops.vercel.app/slides/sre-04/"
      width="100%" height="1400" frameborder="0"
      style="border-radius:8px;display:block;width:100%;min-height:900px">
    </iframe>
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
difficulty: ''
timelimit: 0
enhanced_loading: null
---
> **Lab environment:** Use the **Elastic Serverless** tab only. Hands-on steps run on **Observability Serverless** with **pre-loaded SLB sample data** (logs, metrics, traces, alert rules, and an SLO). The **same observability capabilities** apply on **ECH** and **self-managed**; Serverless mainly saves platform management. Steps are copy/paste in Kibana — no terminal required.

# Production Readiness Workshop

## Part 1 — Readiness checklist (any deployment)

- [ ] OTel data flowing (Logs / Metrics / Traces explorers)
- [ ] **Streams** configured for key telemetry types
- [ ] Critical **alert rules** enabled
- [ ] **SLOs** defined for top services
- [ ] Dashboards for daily review
- [ ] **AI Assistant** / runbooks documented
- [ ] (ECH/on-prem) ILM / Fleet / capacity reviewed

## Part 2 — SLOs & alerts

1. **Observability → SLOs** — browse or create an SLO for a key service.
2. **Alerts → Rules** — confirm rules are not flapping.

## Part 3 — Workflows preview

1. **Management → Workflows** — review templates for alert notification.
2. Add a **Markdown** dashboard panel with escalation contacts.

Click **Check**.
