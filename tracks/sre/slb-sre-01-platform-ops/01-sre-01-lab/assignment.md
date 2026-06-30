---
slug: sre-01-lab
id: 3x5l70vojsvq
type: challenge
title: SRE 01 — Platform Operations Fundamentals
teaser: Core building blocks — data streams, indices, tiers, templates, and pipelines.
notes:
- type: text
  contents: |
    ## Provisioning your lab…

    Creating an Elastic **Observability Serverless** project for **SRE 01**.
    This usually takes 2–3 minutes.

    **Live session topics:**
    - Data streams, indices, tiers, templates, pipelines
    - Elastic Agent default integrations vs OTel-native receiver patterns
    - Fleet-managed vs standalone deployment models
tabs:
- id: t4ybuasacvzc
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
- id: cjqegfv5mazw
  title: Terminal
  type: terminal
  hostname: es3-api
difficulty: ""
timelimit: 0
enhanced_loading: null
---

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

## Part 4 — Terminal inspection

```bash
source ~/.bashrc
curl -s -H "Authorization: ApiKey $ES_API_KEY" \
  "$ES_URL/_data_stream" | jq '.data_streams[].name' | head -10
```

Click **Check**.
