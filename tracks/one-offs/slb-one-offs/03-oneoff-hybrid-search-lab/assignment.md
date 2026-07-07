---
slug: oneoff-hybrid-search-lab
id: bcyjnx13eyo2
type: challenge
title: One-off — Hybrid Search
teaser: Explore hybrid search — BM25 plus vector similarity — in Elasticsearch.
notes:
- type: text
  contents: "## While you wait\u2026\n\n<iframe src=\"https://slb-workshops.vercel.app/slides/oneoff-hybrid-search/\"\n  width=\"100%\" height=\"1400\" frameborder=\"0\"\n  style=\"border-radius:8px;display:block;width:100%;min-height:900px\">\n</iframe>\n\n*Provisioning your **Observability Serverless** lab for **One-off** (usually 2\u20133 minutes). Same Kibana workflows apply on **ECH** and **self-managed**.*"
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
    id: mp56y2peydbu
difficulty: ''
timelimit: 0
enhanced_loading: null
---
> **Lab environment:** Use the **Elastic Serverless** tab only. Hands-on steps run on **Observability Serverless** with **pre-loaded SLB sample data** (logs, metrics, traces, alert rules, and an SLO). The **same observability capabilities** apply on **ECH** and **self-managed**; Serverless mainly saves platform management. Steps are copy/paste in Kibana — no terminal required.

# Hybrid Search for Observability

## Part 1 — Keyword search (Dev Tools)

```
GET logs-*/_search
{
  "query": { "match": { "message": "timeout connection refused" } },
  "size": 5
}
```

## Part 2 — ES|QL + AI

1. Run an ES|QL query for errors in **Logs → Explorer**.
2. Ask **AI Assistant**: *Find logs semantically similar to this error pattern.*

## Part 3 — When to use hybrid search

List one scenario where semantic + keyword beats either alone (e.g. varied error messages for the same root cause).

Click **Check**.
