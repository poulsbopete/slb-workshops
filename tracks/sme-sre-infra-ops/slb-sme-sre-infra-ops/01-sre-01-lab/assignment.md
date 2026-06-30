---
slug: sre-01-lab
id: kkjhd17klluc
type: challenge
title: SRE 01 — Platform Operations Fundamentals
teaser: Core observability building blocks — labs use Serverless; skills transfer
  to ECH and on-prem.
notes:
- type: text
  contents: |-
    ## While you wait…

    <iframe src="https://slb-workshops.vercel.app/slides/sre-01/"
      width="100%" height="1400" frameborder="0"
      style="border-radius:8px;display:block;width:100%;min-height:900px">
    </iframe>

    *Provisioning your **Observability Serverless** lab for **SRE 01** (usually 2–3 minutes). Same Kibana workflows apply on **ECH** and **self-managed**.*
- type: text
  contents: |
    ## Session topics

    - OTel ingestion and Elastic Streams
    - Streams routing vs traditional ingest pipelines
    - Deployment models — Serverless vs ECH vs self-managed (what you manage)
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
> **Lab environment:** Use the **Elastic Serverless** tab only. Hands-on steps run on **Observability Serverless** for a zero-ops learning experience. The **same observability capabilities** — ES|QL, Streams, AI Assistant, Agent Builder, Workflows, SLOs — apply on **ECH** and **self-managed**; Serverless mainly saves platform management (cluster sizing, ILM, Fleet, upgrades). Steps are copy/paste in Kibana — no terminal required.

# Platform Operations Fundamentals

## Part 1 — OTel ingestion (all deployments)

1. **Observability → Add data** (or **Integrations**) — review **OpenTelemetry** and OTLP endpoints.
2. In this **Serverless lab**, Fleet agents and node roles are not in scope — on **ECH/on-prem** your team operates that layer.

## Part 2 — Streams foundation

1. **Observability → Streams** — browse stream definitions and routing.
2. Discuss with facilitator: Streams simplify routing vs manual ingest pipelines; on self-managed/ECH you may pair Streams with ILM for retention.

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

Review data stream names — retention is **project-managed here**; on ECH/on-prem you configure **ILM** instead.

Click **Check**.
