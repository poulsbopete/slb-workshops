---
slug: f-02-lab
id: i1ldxnpkdu75
type: challenge
title: F-02 — Intro to Elastic
teaser: Platform overview — labs use Serverless; the same observability capabilities
  apply on ECH and self-managed deployments.
notes:
- type: text
  contents: "## While you wait…\n\n<iframe src=\"https://slb-workshops.vercel.app/slides/f-02/\"\
    \n  width=\"100%\" height=\"1400\" frameborder=\"0\"\n  style=\"border-radius:8px;display:block;width:100%;min-height:900px\"\
    >\n</iframe>\n\n*Provisioning your **Observability Serverless** lab for **F-02**\
    \ (usually 2–3 minutes). Same Kibana workflows apply on **ECH** and **self-managed**.*"
- type: text
  contents: '## Session topics


    - Elastic Observability — Serverless, ECH, and self-managed (same Kibana value)

    - Streams, ES|QL, and unified Observability

    - SLB SRE''s journey with Elastic — current state

    - AI Assistant and Agent Builder introduction

    '
tabs:
- id: psprkcbh11mx
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
> **Lab environment:** Use the **Elastic Serverless** tab only. Hands-on steps run on **Observability Serverless** for a zero-ops learning experience. The **same observability capabilities** — ES|QL, Streams, AI Assistant, Agent Builder, Workflows, SLOs — apply on **ECH** and **self-managed**; Serverless mainly saves platform management (cluster sizing, ILM, Fleet, upgrades). Steps are copy/paste in Kibana — no terminal required.

# Intro to Elastic Observability

## Part 1 — Platform tour

1. **Observability → Overview** — unified logs, metrics, traces, and SLOs.
2. **Observability → Streams** — routing and processing for telemetry (same concept on ECH and on-prem).
3. **Agents** (sidebar) — explore **Agent Builder** and **AI Assistant**.

## Part 2 — Persona lenses

| Persona | Start here |
|---------|------------|
| Developer | **Observability → APM → Services** |
| SRE / Infra | **Streams** and **Observability → Alerts** |
| Analyst | **Analytics → Discover** or **Logs → Explorer** |
| Architect | **Stack Management → API keys** and access patterns |

## Part 3 — Deployment models (same value, different ops)

| | Serverless (this lab) | ECH | Self-managed |
|--|----------------------|-----|--------------|
| You focus on | Telemetry, alerts, SLOs | Same + cluster policy | Same + full stack ops |
| Elastic manages | Scaling, upgrades, ILM/Fleet | Hosted infrastructure | Software only |

Discuss with facilitator: which model fits each SLB use case.

Click **Check**.
