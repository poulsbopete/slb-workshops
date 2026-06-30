---
slug: oneoff-rag-mcp-lab
type: challenge
title: One-off — RAG & MCP
teaser: Hands-on overview of RAG patterns and MCP tooling with Elasticsearch.
notes:
- type: text
  contents: "## While you wait…\n\n<iframe src=\"https://poulsbopete.github.io/slb-workshops/slides/oneoff-rag-mcp/\"\
    \n  width=\"100%\" height=\"800\" frameborder=\"0\"\n  style=\"border-radius:8px;display:block\"\
    >\n</iframe>\n\n*Provisioning your Elastic **Observability Serverless** lab for\
    \ **One-off** (usually 2–3 minutes).*"
- type: text
  contents: '## Session topics

    - Retrieval-augmented generation with Elasticsearch

    - Model Context Protocol (MCP) integrations

    - Building agent workflows on Elastic data

    '
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
timelimit: 0
---

> **Serverless lab:** use the **Elastic Serverless** tab only. Every step is copy/paste in Kibana — no terminal or shell required.

# RAG & MCP — Hands-on Lab

## Part 1 — Semantic search basics

1. Open **Search → Playground** or **Elasticsearch → Search** (if available).
2. Run a natural-language query against sample documents.

## Part 2 — RAG pattern

1. Note how retrieved documents ground the model response.
2. In **Dev Tools**, inspect an index with dense_vector or semantic fields (if present).

## Part 3 — MCP integration

Discuss with facilitator: how MCP tools could expose Elasticsearch indices to agent workflows.

Click **Check**.
