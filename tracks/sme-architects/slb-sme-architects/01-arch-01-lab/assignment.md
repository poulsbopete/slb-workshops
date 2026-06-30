---
slug: arch-01-lab
id: x9ovfzhtar6n
type: challenge
title: Arch 01 — Architecture & Migration Strategy
teaser: Target-state ingestion design and coexistence planning during migration.
notes:
- type: text
  contents: |-
    ## While you wait…

    <iframe src="https://poulsbopete.github.io/slb-workshops/slides/arch-01/"
      width="100%" height="1400" frameborder="0"
      style="border-radius:8px;display:block;width:100%;min-height:900px">
    </iframe>

    *Provisioning your Elastic **Observability Serverless** lab for **Arch 01** (usually 2–3 minutes).*
- type: text
  contents: |
    ## Session topics

    - Streams and OTel target-state on Serverless
    - Coexistence planning during migration (Grafana + Elastic side by side)
    - Multi-team project access and API keys
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
difficulty: ""
timelimit: 0
enhanced_loading: null
---
> **Elastic Observability Serverless** — use the **Elastic Serverless** tab only. These labs focus on **managed Serverless** capabilities (no ILM, Fleet, or self-managed tiers). Steps are copy/paste in Kibana — no terminal required.

# Serverless Architecture & Migration

## Part 1 — Target state

1. **Observability → Add data** — map OTel collectors → **managed OTLP** (no self-managed Elasticsearch cluster).
2. **Streams** — sketch routing for logs / metrics / traces by team or domain.

## Part 2 — Coexistence plan

| Phase | Grafana / Prometheus | Elastic Serverless |
|-------|---------------------|-------------------|
| Now | Primary | Pilot project |
| Migration | Side-by-side | Streams + ES|QL |
| Target | Optional retained | Primary observability |

## Part 3 — Access & API keys

1. **Stack Management → API keys** — note patterns for automation and multi-team access.
2. Discuss project-level boundaries vs self-managed cluster RBAC.

Click **Check**.
