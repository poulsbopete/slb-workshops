---
slug: f-04-lab
id: by3sx37gxyko
type: challenge
title: F-04 — Looking Forward with Elastic
teaser: First look at Elastic 9.x and what it means for SLB SRE.
notes:
- type: text
  contents: "## While you wait…\n\n<iframe src=\"https://poulsbopete.github.io/slb-workshops/slides/f-04/\"\
    \n  width=\"100%\" height=\"1400\" frameborder=\"0\"\n  style=\"border-radius:8px;display:block;width:100%;min-height:900px\"\
    >\n</iframe>\n\n*Provisioning your Elastic **Observability Serverless** lab for\
    \ **F-04** (usually 2–3 minutes).*"
- type: text
  contents: '## Session topics

    - What''s new in Elastic 9.x

    - What to expect during the migration

    - Key features relevant to SLB SRE

    - Roadmap highlights

    '
tabs:
- id: choly6ztcbdi
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

# Looking Forward — Serverless & AI

## Part 1 — What's new

1. From Kibana Home, open **What's new** / release highlights.
2. Note Serverless-first features: **Streams**, **Agent Builder**, **Workflows**, enhanced **AI Assistant**.

## Part 2 — Hands-on preview

1. **Observability → Streams** — future of managed ingestion routing.
2. **Agents** — open **Agent Builder** (or AI Assistant) and ask: *What observability data do I have?*

## Part 3 — SLB roadmap

With facilitator, identify one Serverless capability to pilot (Streams, SLOs, AI investigation, or Workflows).

Click **Check**.
