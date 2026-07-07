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
    
    <div style="width:100%;max-width:100%;margin:0;padding:0;">
    <iframe src="https://slb-workshops.vercel.app/slides/bi-03/" width="100%" height="1400" frameborder="0" style="display:block;width:100%;min-width:100%;height:1400px;border:0;border-radius:8px"></iframe>
    </div>
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
difficulty: ''
timelimit: 0
enhanced_loading: null
---
> **Lab environment:** Use the **Elastic Serverless** tab only. Hands-on steps run on **Observability Serverless** with **pre-loaded SLB sample data** (logs, metrics, traces, alert rules, and an SLO). The **same observability capabilities** apply on **ECH** and **self-managed**; Serverless mainly saves platform management. Steps are copy/paste in Kibana — no terminal required.

# APIs, Integrations & Dashboard Building

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
2. Same Search and ES|QL APIs on Serverless, ECH, and self-managed — only the endpoint and auth model differ.

Click **Check**.
