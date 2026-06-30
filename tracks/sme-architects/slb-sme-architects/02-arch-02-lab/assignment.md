---
slug: arch-02-lab
id: xmiktsb1pr6x
type: challenge
title: Arch 02 — Lifecycle, Governance & Standards
teaser: ILM and retention strategy, Fleet tradeoffs, and ECS vs OTel conventions.
notes:
- type: text
  contents: "## While you wait…\n\n<iframe src=\"https://poulsbopete.github.io/slb-workshops/slides/arch-02/\"\
    \n  width=\"100%\" height=\"1400\" frameborder=\"0\"\n  style=\"border-radius:8px;display:block;width:100%;min-height:900px\"\
    >\n</iframe>\n\n*Provisioning your Elastic **Observability Serverless** lab for\
    \ **Arch 02** (usually 2–3 minutes).*"
- type: text
  contents: '## Session topics

    - ILM/retention strategy and long-term platform design

    - Fleet-managed vs standalone tradeoffs

    - ECS vs OTel semantic conventions

    - Ownership boundaries and reusable standards across teams

    '
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
difficulty: ''
timelimit: 0
enhanced_loading: null
---
> **Serverless lab:** use the **Elastic Serverless** tab only. Every step is copy/paste in Kibana — no terminal or shell required.

# Lifecycle, Governance & Standards

## Part 1 — ILM policies

1. **Stack Management → Index Lifecycle Policies**.
2. Review hot/warm/cold/frozen phases for a sample policy.

## Part 2 — Standards

Compare **ECS** vs **OTel semantic conventions** for one log type.

## Part 3 — Ownership

Draft reusable standards: naming, retention, and who owns each data stream tier.

Click **Check**.
