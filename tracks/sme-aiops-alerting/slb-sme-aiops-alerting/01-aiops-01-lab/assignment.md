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
    
    Open the **Session slides** tab for today's deck while your Observability Serverless project provisions (~2–3 minutes).
    
    When provisioning finishes, switch to **Elastic Serverless** for the hands-on lab.
tabs:
  - title: Session slides
    type: website
    url: https://slb-workshops.vercel.app/slides/aiops-01/
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
    id: gdxdjt59pvyr
difficulty: ''
timelimit: 0
enhanced_loading: null
---
> **Lab environment:** Use the **Elastic Serverless** tab only. Hands-on steps run on **Observability Serverless** with **pre-loaded SLB sample data** (logs, metrics, traces, alert rules, and an SLO). The **same observability capabilities** apply on **ECH** and **self-managed**; Serverless mainly saves platform management. Steps are copy/paste in Kibana — no terminal required.

# Alert Fatigue & Noise Reduction

## Part 1 — Review rules

1. **Alerts → Rules** — sort by recent activity.
2. Identify noisy rules.

## Part 2 — Tune a rule

Adjust threshold, window, or grouping. Enable deduplication / suppression if available.

## Part 3 — Triage

1. **Alerts** — acknowledge and annotate an alert.
2. Use **AI Assistant**: *Why might this alert be firing repeatedly?*

Click **Check**.
