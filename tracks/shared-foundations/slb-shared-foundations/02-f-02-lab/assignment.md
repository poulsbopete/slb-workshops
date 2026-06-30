---
slug: f-02-lab
id: i1ldxnpkdu75
type: challenge
title: F-02 — Intro to Elastic
teaser: Overview of the Elastic platform and how it fits into SLB SRE's observability
  journey — ingestion, storage, query, and visualization.
notes:
- type: text
  contents: "## While you wait…\n\n<iframe src=\"https://poulsbopete.github.io/slb-workshops/slides/f-02/\"\
    \n  width=\"100%\" height=\"1400\" frameborder=\"0\"\n  style=\"border-radius:8px;display:block;width:100%;min-height:900px\"\
    >\n</iframe>\n\n*Provisioning your Elastic **Observability Serverless** lab for\
    \ **F-02** (usually 2–3 minutes).*"
- type: text
  contents: '## Session topics


    - Elastic Observability Serverless overview

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
> **Elastic Observability Serverless** — use the **Elastic Serverless** tab only. These labs focus on **managed Serverless** capabilities (no ILM, Fleet, or self-managed tiers). Steps are copy/paste in Kibana — no terminal required.

# Intro to Elastic Serverless

## Part 1 — Platform tour

1. **Observability → Overview** — unified logs, metrics, traces, and SLOs.
2. **Observability → Streams** — managed routing and processing for telemetry (Serverless-native).
3. **Agents** (sidebar) — explore **Agent Builder** and AI capabilities available in your project.

## Part 2 — Persona lenses (Serverless)

| Persona | Start here |
|---------|------------|
| Developer | **Observability → APM → Services** |
| SRE / Infra | **Streams** and **Observability → Alerts** |
| Analyst | **Analytics → Discover** or **Logs → Explorer** |
| Architect | **Stack Management → API keys** and project access patterns |

## Part 3 — What Serverless manages for you

Discuss with facilitator: ingestion endpoints, scaling, and retention are managed — your focus is **telemetry quality, ES|QL, Streams, and AI-assisted ops**.

Click **Check**.
