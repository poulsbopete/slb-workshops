---
slug: arch-01-lab
id: x9ovfzhtar6n
type: challenge
title: Arch 01 — Architecture & Migration Strategy
teaser: Target-state ingestion design and coexistence planning during migration.
notes:
- type: text
  contents: "## While you wait…\n\n<iframe src=\"https://poulsbopete.github.io/slb-workshops/docs/slides/arch-01/\"\
    \n  width=\"100%\" height=\"1400\" frameborder=\"0\"\n  style=\"border-radius:8px;display:block;width:100%;min-height:900px\"\
    >\n</iframe>\n\n*Provisioning your Elastic **Observability Serverless** lab for\
    \ **Arch 01** (usually 2–3 minutes).*"
- type: text
  contents: '## Session topics

    - Target-state ingestion design

    - Coexistence planning during migration (Grafana + Elastic side by side)

    - Multi-team deployment and access patterns

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
> **Serverless lab:** use the **Elastic Serverless** tab only. Every step is copy/paste in Kibana — no terminal or shell required.

# Architecture & Migration Strategy

## Part 1 — Current state inventory

1. **Stack Management → Index Management** — list data streams and retention.
2. **Fleet** (if visible) — note agent vs OTel collection patterns.

## Part 2 — Target-state sketch

Document coexistence plan:

| Phase | Grafana | Elastic |
|-------|---------|---------|
| Now | Primary | Pilot |
| Migration | Side-by-side | Growing |
| Target | Retained? | Primary |

## Part 3 — Multi-team access

Review **Stack Management → Roles** — note space and index privileges patterns.

Click **Check**.
