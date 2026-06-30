---
slug: bi-03-lab
id: 2g0vd58tvxxc
type: challenge
title: BI 03 — APIs, Integrations & Dashboard Building
teaser: Elasticsearch API basics and building dashboards for operational reporting.
notes:
- type: text
  contents: |-
    ## While you wait…

    <iframe src="https://poulsbopete.github.io/slb-workshops/slides/bi-03/"
      width="100%" height="1400" frameborder="0"
      style="border-radius:8px;display:block;width:100%;min-height:900px">
    </iframe>

    *Provisioning your Elastic **Observability Serverless** lab for **BI 03** (usually 2–3 minutes).*
- type: text
  contents: |
    ## Session topics
    - API calls and pulling data into external tools
    - Building dashboards for operational and business review
    - Data schema considerations
tabs:
- id: bitfssmxbnj7
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

# APIs & Dashboards on Serverless

## Part 1 — Search API (Dev Tools)

```
GET logs-*/_search
{
  "size": 3,
  "sort": [{ "@timestamp": "desc" }]
}
```

## Part 2 — Business dashboard

1. **Analytics → Dashboards → Create dashboard**.
2. Add two **Lens** panels + one **Markdown** KPI panel.

## Part 3 — Field types

1. **Stack Management → Data views** — inspect keyword vs text vs date fields.
2. Note Serverless uses the same query APIs — no cluster URL management.

Click **Check**.
