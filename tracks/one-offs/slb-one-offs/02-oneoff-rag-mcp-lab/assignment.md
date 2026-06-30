---
slug: oneoff-rag-mcp-lab
id: wysvvc0d0tk5
type: challenge
title: One-off — RAG & MCP
teaser: Hands-on overview of RAG patterns and MCP tooling with Elasticsearch.
notes:
- type: text
  contents: "## While you wait…\n\n<iframe src=\"https://poulsbopete.github.io/slb-workshops/slides/oneoff-rag-mcp/\"\
    \n  width=\"100%\" height=\"1400\" frameborder=\"0\"\n  style=\"border-radius:8px;display:block;width:100%;min-height:900px\"\
    >\n</iframe>\n\n*Provisioning your **Observability Serverless** lab for **One-off**\
    \ (usually 2–3 minutes). Same Kibana workflows apply on **ECH** and **self-managed**.*"
- type: text
  contents: '## Session topics

    - Retrieval-augmented generation with Elasticsearch

    - Model Context Protocol (MCP) integrations

    - Building agent workflows on Elastic data

    '
tabs:
- id: m5a3xelh56rn
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
