---
slug: sre-01-lab
id: kkjhd17klluc
type: challenge
title: SRE 01 — Platform Operations Fundamentals
teaser: Core Serverless building blocks — managed ingestion, Streams, ES|QL, and observability
  signals.
notes:
- type: text
  contents: |-
    ## While you wait…

    <iframe src="https://poulsbopete.github.io/slb-workshops/slides/sre-01/"
      width="100%" height="1400" frameborder="0"
      style="border-radius:8px;display:block;width:100%;min-height:900px">
    </iframe>

    *Provisioning your Elastic **Observability Serverless** lab for **SRE 01** (usually 2–3 minutes).*
- type: text
  contents: |
    ## Session topics

    - Managed OTel ingestion and Elastic Streams
    - Streams routing vs self-managed pipelines
    - Serverless operations model (no Fleet / ILM)
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
> **Elastic Observability Serverless** — use the **Elastic Serverless** tab only. These labs focus on **managed Serverless** capabilities (no ILM, Fleet, or self-managed tiers). Steps are copy/paste in Kibana — no terminal required.

# Serverless Platform Operations

## Part 1 — Managed ingestion model

1. **Observability → Add data** (or **Integrations**) — review **OpenTelemetry** and managed OTLP endpoints.
2. Note: no Fleet agents or node roles to manage on Serverless.

## Part 2 — Streams foundation

1. **Observability → Streams** — browse stream definitions and routing.
2. Discuss with facilitator: how Streams replace manual pipeline + index template work on self-managed clusters.

## Part 3 — Confirm telemetry (ES|QL)

In **Logs → Explorer** (ES|QL):

```esql
FROM logs-* | STATS streams = COUNT(*) BY data_stream.dataset | SORT streams DESC | LIMIT 10
```

## Part 4 — Dev Tools (optional)

**Management → Dev Tools**:

```
GET _data_stream/logs-*
```

Review names — retention is **project-managed**, not ILM.

Click **Check**.
