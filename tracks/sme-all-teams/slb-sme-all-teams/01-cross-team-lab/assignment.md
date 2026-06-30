---
slug: cross-team-lab
id: voem0yxaqp7l
type: challenge
title: Cross-team — Cross-team Platform Review
teaser: Cross-team session reviewing adoption progress and next steps.
notes:
- type: text
  contents: |-
    ## While you wait…

    <iframe src="https://poulsbopete.github.io/slb-workshops/docs/slides/cross-team/"
      width="100%" height="1400" frameborder="0"
      style="border-radius:8px;display:block;width:100%;min-height:900px">
    </iframe>

    *Provisioning your Elastic **Observability Serverless** lab for **Cross-team** (usually 2–3 minutes).*
- type: text
  contents: |
    ## Session topics
    - Elastic adoption progress across all teams
    - Open Q&A and live troubleshooting
    - Next steps and program evolution
tabs:
- id: ahuakfmqw6b5
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
> **Serverless lab:** use the **Elastic Serverless** tab only. Every step is copy/paste in Kibana — no terminal or shell required.

# Cross-team Platform Review

## Part 1 — Adoption snapshot

1. **Observability → Overview** — note active data sources.
2. **Analytics → Dashboards** — browse shared dashboards.

## Part 2 — Open Q&A prep

List three questions for the live session (ingestion, alerts, ES|QL, migration).

## Part 3 — Next steps

Identify one action item for your team before the next SME session.

Click **Check**.
