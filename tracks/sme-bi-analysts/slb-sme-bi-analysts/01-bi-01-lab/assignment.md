---
slug: bi-01-lab
type: challenge
title: BI 01 — Dashboard & Data Exploration Basics
teaser: Kibana Discover, Lens visualizations, and dashboards for BI users.
notes:
- type: text
  contents: "## While you wait…\n\n<iframe src=\"https://poulsbopete.github.io/slb-workshops/slides/bi-01/\"\
    \n  width=\"100%\" height=\"800\" frameborder=\"0\"\n  style=\"border-radius:8px;display:block\"\
    >\n</iframe>\n\n*Provisioning your Elastic **Observability Serverless** lab for\
    \ **BI 01** (usually 2–3 minutes).*"
- type: text
  contents: '## Session topics

    - Navigating Discover, Lens, and dashboards

    - Filtering, slicing, and exporting

    - Entry-level friendly — no prior Elastic experience required

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

# Dashboard & Data Exploration Basics

**No prior Elastic experience required.**

## Part 1 — Discover

1. **Analytics → Discover**.
2. Select any available data view.
3. Use the time picker — **Last 24 hours**.
4. Add a field column and sort.

## Part 2 — Lens

1. **Visualize Library → Create visualization → Lens**.
2. Build a bar chart — count of events over time.
3. Save to a new dashboard.

## Part 3 — Export

1. From Discover, export a CSV sample (Share → CSV Reports if available,
   or copy table data).

Click **Check**.
