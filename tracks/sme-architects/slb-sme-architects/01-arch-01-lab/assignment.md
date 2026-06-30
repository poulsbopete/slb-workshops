---
slug: arch-01-lab
id: x9ovfzhtar6n
type: challenge
title: Arch 01 — Architecture & Migration Strategy
teaser: Target-state ingestion design and coexistence planning during migration.
notes:
- type: text
  contents: "## While you wait…\n\n<iframe src=\"https://slb-workshops.vercel.app/slides/arch-01/\"\
    \n  width=\"100%\" height=\"1400\" frameborder=\"0\"\n  style=\"border-radius:8px;display:block;width:100%;min-height:900px\"\
    >\n</iframe>\n\n*Provisioning your **Observability Serverless** lab for **Arch\
    \ 01** (usually 2–3 minutes). Same Kibana workflows apply on **ECH** and **self-managed**.*"
- type: text
  contents: '## Session topics


    - Streams and OTel target-state (Serverless, ECH, or on-prem)

    - Coexistence planning during migration (Grafana + Elastic side by side)

    - Multi-team project access and API keys

    '
tabs:
- id: 9vejoukhuxkm
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

# Architecture & Migration Strategy

## Part 1 — Target state

1. **Observability → Add data** — map OTel collectors → **Elastic OTLP** (Serverless, ECH, or self-managed endpoint).
2. **Streams** — sketch routing for logs / metrics / traces by team or domain.

## Part 2 — Coexistence plan

| Phase | Grafana / Prometheus | Elastic (your deployment) |
|-------|---------------------|---------------------------|
| Now | Primary | Pilot (Serverless, ECH, or on-prem) |
| Migration | Side-by-side | Streams + ES|QL |
| Target | Optional retained | Primary observability |

## Part 3 — Access & API keys

1. **Stack Management → API keys** — note patterns for automation and multi-team access.
2. Discuss boundaries: project keys (Serverless) vs deployment keys (ECH) vs cluster RBAC (self-managed).

Click **Check**.
