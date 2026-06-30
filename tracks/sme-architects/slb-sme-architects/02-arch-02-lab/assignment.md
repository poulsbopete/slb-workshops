---
slug: arch-02-lab
id: xmiktsb1pr6x
type: challenge
title: Arch 02 — Governance, Streams & Standards
teaser: Governance for Serverless — Streams standards, schema conventions, and AI
  agent policies.
notes:
- type: text
  contents: |-
    ## While you wait…

    <iframe src="https://poulsbopete.github.io/slb-workshops/slides/arch-02/"
      width="100%" height="1400" frameborder="0"
      style="border-radius:8px;display:block;width:100%;min-height:900px">
    </iframe>

    *Provisioning your Elastic **Observability Serverless** lab for **Arch 02** (usually 2–3 minutes).*
- type: text
  contents: |
    ## Session topics

    - Streams naming and ownership standards
    - Managed retention on Serverless vs self-managed ILM
    - ECS vs OTel semantic conventions
    - Agent Builder and AI governance
tabs:
- id: z2y9yjgurhfy
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

# Governance & Standards on Serverless

> No ILM policies on Serverless — focus on **Streams**, **schema**, and **access** standards.

## Part 1 — Streams naming & ownership

1. **Observability → Streams** — document naming conventions for SLB teams.
2. Define owners per stream / dataset.

## Part 2 — ECS vs OTel semantics

Compare field naming for one log type:

| ECS field | OTel equivalent |
|-----------|-----------------|
| `service.name` | `service.name` |
| `host.name` | `host.name` |
| `log.level` | `severity_text` |

Pick one convention for SLB and stick to it in OTel resource attributes.

## Part 3 — Agent Builder governance

1. Open **Agents** — review who can create agents and connect tools.
2. Draft a policy: when to use **AI Assistant** vs automated **Workflows**.

Click **Check**.
