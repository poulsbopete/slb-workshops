---
slug: sre-02-lab
id: jwqhu4mnysqr
type: challenge
title: SRE 02 — Elastic Streams & Data Routing
teaser: Elastic Streams deep dive — routing and processing; retention differs by deployment,
  capabilities do not.
notes:
- type: text
  contents: "## While you wait…\n\n<iframe src=\"https://poulsbopete.github.io/slb-workshops/slides/sre-02/\"\
    \n  width=\"100%\" height=\"1400\" frameborder=\"0\"\n  style=\"border-radius:8px;display:block;width:100%;min-height:900px\"\
    >\n</iframe>\n\n*Provisioning your **Observability Serverless** lab for **SRE\
    \ 02** (usually 2–3 minutes). Same Kibana workflows apply on **ECH** and **self-managed**.*"
- type: text
  contents: '## Session topics


    - Elastic Streams — routing and processing

    - Retention on Serverless vs ILM on ECH/on-prem

    - Troubleshooting stream health with ES|QL and AI Assistant

    '
tabs:
- id: aui2vrhafknu
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
> **Lab environment:** Use the **Elastic Serverless** tab only. Hands-on steps run on **Observability Serverless** for a zero-ops learning experience. The **same observability capabilities** — ES|QL, Streams, AI Assistant, Agent Builder, Workflows, SLOs — apply on **ECH** and **self-managed**; Serverless mainly saves platform management (cluster sizing, ILM, Fleet, upgrades). Steps are copy/paste in Kibana — no terminal required.

# Elastic Streams & Data Routing

> **In this lab:** Retention is project-managed (no ILM UI). On **ECH/self-managed** you use **ILM** for lifecycle — **Streams** routing and processing work the same either way.

## Part 1 — Streams tour

1. **Observability → Streams** — open the Streams management view.
2. Review how logs, metrics, and traces flow through streams.
3. Note any **processing** or **routing** rules visible in the UI.

## Part 2 — Query stream-backed data

In **Logs → Explorer** (ES|QL):

```esql
FROM logs-* | STATS volume = COUNT(*) BY bucket = BUCKET(@timestamp, 1 hour) | SORT bucket DESC | LIMIT 24
```

Identify peak ingest windows — capacity is auto-scaled in Serverless; on ECH/on-prem you plan shard and tier capacity.

## Part 3 — Retention & governance

1. **Stack Management → Project settings** (or **Management** overview) — note how retention is set in this lab.
2. With facilitator, compare **what you control** across deployment models:

| You control (all deployments) | Ops burden differs by deployment |
|-------------------------------|----------------------------------|
| OTel schema & labels | Serverless: Elastic manages scaling & base retention |
| Streams routing rules | ECH: hosted cluster + ILM policies |
| Alerts & SLOs | Self-managed: you run Fleet, nodes, ILM, upgrades |

## Part 4 — Troubleshooting routing

1. In **Streams**, check for failed or lagging streams (if indicators are shown).
2. Use **AI Assistant**: *Are any streams dropping data in the last hour?*

Click **Check**.
