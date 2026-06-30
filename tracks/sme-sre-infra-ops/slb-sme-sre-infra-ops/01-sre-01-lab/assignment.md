---
slug: sre-01-lab
id: kkjhd17klluc
type: challenge
title: SRE 01 — Platform Operations Fundamentals
teaser: Core building blocks — data streams, indices, tiers, templates, and pipelines.
notes:
- type: text
  contents: |-
    ## While you wait…

    <iframe src="https://poulsbopete.github.io/slb-workshops/docs/slides/sre-01/"
      width="100%" height="1400" frameborder="0"
      style="border-radius:8px;display:block;width:100%;min-height:900px">
    </iframe>

    *Provisioning your Elastic **Observability Serverless** lab for **SRE 01** (usually 2–3 minutes).*
- type: text
  contents: |
    ## Session topics
    - Data streams, indices, tiers, templates, pipelines
    - Elastic Agent default integrations vs OTel-native receiver patterns
    - Fleet-managed vs standalone deployment models
tabs:
- id: hcdahyovlngd
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

# Platform Operations Fundamentals

## Part 1 — Data streams and templates

1. **Stack Management → Index Management** — filter **Data streams**.
2. Inspect naming: `logs-*`, `metrics-*`, `traces-*`.
3. **Index Management → Index Templates** — review composable templates.

## Part 2 — Ingest pipelines

1. **Stack Management → Ingest Pipelines** — open a default pipeline.
2. Note processors (date, set, rename).

## Part 3 — Fleet vs standalone

1. **Fleet → Agents** — review Fleet-managed model.
2. Compare with **Integrations → OTel** standalone collector docs.

## Part 4 — Confirm data streams (Dev Tools)

You already browsed **Index Management** in Part 1. Optionally paste in **Management → Dev Tools**:

```
GET _data_stream
```

Review the `data_streams` names in the JSON response.

Click **Check**.
