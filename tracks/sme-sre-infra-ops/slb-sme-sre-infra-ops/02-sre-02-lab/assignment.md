---
slug: sre-02-lab
id: jwqhu4mnysqr
type: challenge
title: SRE 02 — Elastic Streams & Data Routing
teaser: Elastic Streams on Serverless — routing and processing without ILM or data
  tiers.
notes:
- type: text
  contents: "## While you wait…\n\n<iframe src=\"https://poulsbopete.github.io/slb-workshops/slides/sre-02/\"\
    \n  width=\"100%\" height=\"1400\" frameborder=\"0\"\n  style=\"border-radius:8px;display:block;width:100%;min-height:900px\"\
    >\n</iframe>\n\n*Provisioning your Elastic **Observability Serverless** lab for\
    \ **SRE 02** (usually 2–3 minutes).*"
- type: text
  contents: '## Session topics


    - Elastic Streams on Observability Serverless

    - Routing, processing, and managed retention

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
> **Elastic Observability Serverless** — use the **Elastic Serverless** tab only. These labs focus on **managed Serverless** capabilities (no ILM, Fleet, or self-managed tiers). Steps are copy/paste in Kibana — no terminal required.

# Elastic Streams on Serverless

> **Serverless note:** ILM and data tiers are not applicable — routing, processing, and retention are managed via **Streams** and project settings.

## Part 1 — Streams tour

1. **Observability → Streams** — open the Streams management view.
2. Review how logs, metrics, and traces flow through managed streams.
3. Note any **processing** or **routing** rules visible in the UI.

## Part 2 — Query stream-backed data

In **Logs → Explorer** (ES|QL):

```esql
FROM logs-* | STATS volume = COUNT(*) BY bucket = BUCKET(@timestamp, 1 hour) | SORT bucket DESC | LIMIT 24
```

Identify peak ingest windows to discuss capacity (managed by Elastic).

## Part 3 — Retention & governance (Serverless)

1. **Stack Management → Project settings** (or **Management** overview) — note retention is managed for Serverless.
2. With facilitator, document **what you control** vs **what Elastic manages**:

| You control | Elastic manages |
|-------------|-----------------|
| OTel schema & labels | Scaling & storage tiers |
| Streams routing rules | Platform upgrades |
| Alerts & SLOs | Base retention policy |

## Part 4 — Troubleshooting routing

1. In **Streams**, check for failed or lagging streams (if indicators are shown).
2. Use **AI Assistant**: *Are any streams dropping data in the last hour?*

Click **Check**.
