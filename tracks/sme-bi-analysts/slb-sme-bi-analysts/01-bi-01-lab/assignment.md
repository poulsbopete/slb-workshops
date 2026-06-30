---
slug: bi-01-lab
id: fluwvyl3dhcv
type: challenge
title: BI 01 — Dashboard & Data Exploration Basics
teaser: Kibana Discover, Lens visualizations, and dashboards for BI users.
notes:
- type: text
  contents: "## While you wait…\n\n<iframe src=\"https://poulsbopete.github.io/slb-workshops/slides/bi-01/\"\
    \n  width=\"100%\" height=\"1400\" frameborder=\"0\"\n  style=\"border-radius:8px;display:block;width:100%;min-height:900px\"\
    >\n</iframe>\n\n*Provisioning your **Observability Serverless** lab for **BI 01**\
    \ (usually 2–3 minutes). Same Kibana workflows apply on **ECH** and **self-managed**.*"
- type: text
  contents: '## Session topics

    - Navigating Discover, Lens, and dashboards

    - Filtering, slicing, and exporting

    - Entry-level friendly — no prior Elastic experience required

    '
tabs:
- id: bmrjyhl5y0ty
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

# Dashboard & Data Exploration Basics

## Part 1 — Discover

1. **Analytics → Discover** — select observability data.
2. Time picker: **Last 24 hours** — add columns and sort.

## Part 2 — Lens

1. **Visualize → Lens** — bar chart of events over time.
2. Save to a new dashboard.

## Part 3 — ES|QL peek

In **Logs → Explorer**:

```esql
FROM logs-* | STATS count = COUNT(*) BY service.name | SORT count DESC | LIMIT 10
```

Click **Check**.
