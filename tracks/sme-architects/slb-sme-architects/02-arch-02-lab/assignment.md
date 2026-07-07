---
slug: arch-02-lab
id: xmiktsb1pr6x
type: challenge
title: Arch 02 — Governance, Streams & Standards
teaser: Governance — Streams standards, schema conventions, and AI agent policies
  across deployments.
notes:
- type: text
  contents: |-
    ## While you wait…
    
    Open the **Session slides** tab for today's deck while your Observability Serverless project provisions (~2–3 minutes).
    
    When provisioning finishes, switch to **Elastic Serverless** for the hands-on lab.
tabs:
  - title: Session slides
    type: website
    url: https://slb-workshops.vercel.app/slides/arch-02/
  - title: Elastic Serverless
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
    id: z2y9yjgurhfy
difficulty: ''
timelimit: 0
enhanced_loading: null
---
> **Lab environment:** Use the **Elastic Serverless** tab only. Hands-on steps run on **Observability Serverless** with **pre-loaded SLB sample data** (logs, metrics, traces, alert rules, and an SLO). The **same observability capabilities** apply on **ECH** and **self-managed**; Serverless mainly saves platform management. Steps are copy/paste in Kibana — no terminal required.

# Governance, Streams & Standards

> **Retention:** This lab uses project-managed retention. On **ECH/on-prem**, pair **Streams** standards with your **ILM** policies — routing and lifecycle are separate concerns.

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
2. Draft a policy: when to use **AI Assistant** vs automated **Workflows** (same rules on any deployment).

Click **Check**.
