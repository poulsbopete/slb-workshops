---
slug: oneoff-rag-mcp-lab
id: wysvvc0d0tk5
type: challenge
title: One-off — RAG & MCP
teaser: Hands-on overview of RAG patterns and MCP tooling with Elasticsearch.
notes:
- type: text
  contents: |-
    ## While you wait…
    
    Open the **Session slides** tab for today's deck while your Observability Serverless project provisions (~2–3 minutes).
    
    When provisioning finishes, switch to **Elastic Serverless** for the hands-on lab.
tabs:
  - title: Session slides
    type: website
    url: https://slb-workshops.vercel.app/slides/oneoff-rag-mcp/
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
    id: m5a3xelh56rn
difficulty: ''
timelimit: 0
enhanced_loading: null
---
> **Lab environment:** Use the **Elastic Serverless** tab only. Hands-on steps run on **Observability Serverless** with **pre-loaded SLB sample data** (logs, metrics, traces, alert rules, and an SLO). The **same observability capabilities** apply on **ECH** and **self-managed**; Serverless mainly saves platform management. Steps are copy/paste in Kibana — no terminal required.

# RAG, Agents & MCP

## Part 1 — Agent Builder + retrieval

1. **Agents → Agent Builder** — open an agent with knowledge retrieval.
2. Ask a question grounded in your observability documentation or runbooks.

## Part 2 — MCP concept

With facilitator, discuss how **Model Context Protocol (MCP)** tools could expose:

- ES|QL query results
- Stream metadata
- Alert history

## Part 3 — Practical pattern

Document one SLB use case: *Agent answers "what changed?" using logs + traces via MCP tools.*

Click **Check**.
