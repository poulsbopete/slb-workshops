---
slug: aiops-01-lab
type: challenge
title: "AIOps 01 — Alert Fatigue & Noise Reduction"
teaser: "Reduce alert volume through rule tuning, deduplication, and suppression."
notes:
- type: text
  contents: |
    ## Provisioning your lab…

    Creating an Elastic **Observability Serverless** project for **AIOps 01**.
    This usually takes 2–3 minutes.

    **Live session topics:**
    - Understanding why alert fatigue happens in Elastic
    - Rule tuning — thresholds and conditions
    - Alert deduplication, suppression, and exceptions
    - Day-to-day alert triage and diagnosis workflows
tabs:
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
- title: Terminal
  type: terminal
  hostname: es3-api
timelimit: 0
---

# Alert Fatigue & Noise Reduction

## Part 1 — Review existing rules

1. **Observability → Alerts → Rules**.
2. Sort by **active alerts** or **recent executions**.

## Part 2 — Tune a rule

1. Open a threshold rule — adjust window, threshold, or grouping.
2. Enable **deduplication** or **suppress duplicates** where available.

## Part 3 — Triage workflow

1. **Observability → Alerts** — practice acknowledging and adding notes.
2. Create a **maintenance window** (if applicable).

## Part 4 — Goal

Document one rule change that would reduce noise for SLB's alert volume.

Click **Check**.
