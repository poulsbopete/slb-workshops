---
slug: aiops-01-lab
id: 8ldo2is78uqr
type: challenge
title: AIOps 01 — Alert Fatigue & Noise Reduction
teaser: Reduce alert volume through rule tuning, deduplication, and suppression.
notes:
- type: text
  contents: |-
    ## While you wait…

    <iframe src="https://slb-workshops.vercel.app/slides/aiops-01/"
      width="100%" height="1400" frameborder="0"
      style="border-radius:8px;display:block;width:100%;min-height:900px">
    </iframe>

    *Provisioning your **Observability Serverless** lab for **AIOps 01** (usually 2–3 minutes). Same Kibana workflows apply on **ECH** and **self-managed**.*
- type: text
  contents: |
    ## Session topics
    - Understanding why alert fatigue happens in Elastic
    - Rule tuning — thresholds and conditions
    - Alert deduplication, suppression, and exceptions
    - Day-to-day alert triage and diagnosis workflows
tabs:
- id: gdxdjt59pvyr
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
> **Lab environment:** Use the **Elastic Serverless** tab only. Hands-on steps run on **Observability Serverless** for a zero-ops learning experience. The **same observability capabilities** — ES|QL, Streams, AI Assistant, Agent Builder, Workflows, SLOs — apply on **ECH** and **self-managed**; Serverless mainly saves platform management (cluster sizing, ILM, Fleet, upgrades). Steps are copy/paste in Kibana — no terminal required.

# Alert Fatigue & Noise Reduction

## Part 1 — Review rules

1. **Observability → Alerts → Rules** — sort by recent activity.
2. Identify noisy rules.

## Part 2 — Tune a rule

Adjust threshold, window, or grouping. Enable deduplication / suppression if available.

## Part 3 — Triage

1. **Observability → Alerts** — acknowledge and annotate an alert.
2. Use **AI Assistant**: *Why might this alert be firing repeatedly?*

Click **Check**.
