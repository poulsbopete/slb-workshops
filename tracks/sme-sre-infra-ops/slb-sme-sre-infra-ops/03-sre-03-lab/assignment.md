---
slug: sre-03-lab
id: de3rkl9k77xe
type: challenge
title: SRE 03 — Ingestion Architecture & Troubleshooting
teaser: Ingestion troubleshooting with Streams, ES|QL, and AI Assistant — lab on Serverless,
  patterns apply everywhere.
notes:
- type: text
  contents: |-
    ## While you wait…
    
    Open the **Session slides** tab for today's deck while your Observability Serverless project provisions (~2–3 minutes).
    
    When provisioning finishes, switch to **Elastic Serverless** for the hands-on lab.
tabs:
  - title: Session slides
    type: website
    url: https://slb-workshops.vercel.app/slides/sre-03/
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
    id: jru4krdqiog7
difficulty: ''
timelimit: 0
enhanced_loading: null
---
> **Lab environment:** Use the **Elastic Serverless** tab only. Hands-on steps run on **Observability Serverless** with **pre-loaded SLB sample data** (logs, metrics, traces, alert rules, and an SLO). The **same observability capabilities** apply on **ECH** and **self-managed**; Serverless mainly saves platform management. Steps are copy/paste in Kibana — no terminal required.

# Ingestion Architecture & Troubleshooting

## Part 1 — OTel → Elastic OTLP

1. **Observability → Add data → OpenTelemetry** — review the OTLP endpoint pattern.
2. Compare with your current Grafana/Prometheus export path (facilitator-led) — same OTel path works on ECH and on-prem.

## Part 2 — Diagnose gaps in ES|QL

```esql
FROM logs-* | STATS count = COUNT(*) BY bucket = BUCKET(@timestamp, 5 minutes) | SORT bucket DESC
```

Look for missing buckets = possible ingest gaps.

## Part 3 — Streams health

1. **Observability → Streams** — check stream status indicators.
2. **Observability → Logs → Anomalies** (if enabled) — review unusual patterns.

## Part 4 — Error logs

```esql
FROM logs-* | WHERE message LIKE "*error*" OR log.level == "error" | LIMIT 20
```

Click **Check**.
