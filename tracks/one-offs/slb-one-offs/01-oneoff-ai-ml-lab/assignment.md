---
slug: oneoff-ai-ml-lab
id: y47gpnfmoqry
type: challenge
title: One-off — AI/ML Overview
teaser: One-off demo session — Elastic AI/ML capabilities across observability use
  cases.
notes:
- type: text
  contents: "## While you wait…\n\n<iframe src=\"https://poulsbopete.github.io/slb-workshops/docs/slides/oneoff-ai-ml/\"\
    \n  width=\"100%\" height=\"1400\" frameborder=\"0\"\n  style=\"border-radius:8px;display:block;width:100%;min-height:900px\"\
    >\n</iframe>\n\n*Provisioning your Elastic **Observability Serverless** lab for\
    \ **One-off** (usually 2–3 minutes).*"
- type: text
  contents: '## Session topics

    - Overview of Elastic AI/ML capabilities for observability

    - Anomaly detection and log pattern analysis

    - AI Assistant for Observability

    '
tabs:
- id: 4nbmvhjpwo3w
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

# AI/ML Overview — Hands-on Lab

## Part 1 — AI Assistant

1. Open **AI Assistant** from Observability.
2. Ask: "Summarize error patterns in the last hour."

## Part 2 — ML features

1. **Machine Learning → Anomaly Detection** — browse job templates.
2. **Logs → Log patterns** (if available) — review pattern grouping.

## Part 3 — Use cases for SLB

Discuss with facilitator: anomaly detection vs AI Assistant vs alerting — when to use each.

Click **Check**.
