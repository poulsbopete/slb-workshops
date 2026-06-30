---
slug: oneoff-hybrid-search-lab
id: bcyjnx13eyo2
type: challenge
title: One-off — Hybrid Search
teaser: Explore hybrid search — BM25 plus vector similarity — in Elasticsearch.
notes:
- type: text
  contents: |-
    ## While you wait…

    <iframe src="https://poulsbopete.github.io/slb-workshops/docs/slides/oneoff-hybrid-search/"
      width="100%" height="1400" frameborder="0"
      style="border-radius:8px;display:block;width:100%;min-height:900px">
    </iframe>

    *Provisioning your Elastic **Observability Serverless** lab for **One-off** (usually 2–3 minutes).*
- type: text
  contents: |
    ## Session topics
    - Combining lexical and semantic search
    - Hybrid search in Elasticsearch
    - Relevance tuning for observability and log search
tabs:
- id: mp56y2peydbu
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

# Hybrid Search — Hands-on Lab

## Part 1 — Lexical search

1. **Dev Tools** — run a BM25 search:

```
GET logs-*/_search
{
  "query": { "match": { "message": "error timeout" } },
  "size": 5
}
```

## Part 2 — Hybrid relevance

1. Discuss combining keyword + vector scores (RRF / hybrid query).
2. Review Elastic docs on hybrid search in your facilitator's walkthrough.

## Part 3 — Observability use case

Identify one log search scenario where hybrid search beats keyword-only.

Click **Check**.
