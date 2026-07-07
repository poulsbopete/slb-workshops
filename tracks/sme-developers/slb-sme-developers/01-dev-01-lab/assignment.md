---
slug: dev-01-lab
id: 1qfx5l5ueej6
type: challenge
title: Dev 01 — Elastic UI & Dashboard Workflows
teaser: Fast track to Kibana — Discover, dashboards, filters, and drilldowns with
  direct comparisons to Grafana workflows.
notes:
- type: text
  contents: |-
    ## While you wait…
    
    Open the **Session slides** tab for today's deck while your Observability Serverless project provisions (~2–3 minutes).
    
    When provisioning finishes, switch to **Elastic Serverless** for the hands-on lab.
tabs:
  - title: Session slides
    type: website
    url: https://slb-workshops.vercel.app/slides/dev-01/
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
    id: qxzu1et4tfko
difficulty: ''
timelimit: 0
enhanced_loading: null
---
> **Lab environment:** Use the **Elastic Serverless** tab only. Hands-on steps run on **Observability Serverless** with **pre-loaded SLB sample data** (logs, metrics, traces, alert rules, and an SLO). The **same observability capabilities** apply on **ECH** and **self-managed**; Serverless mainly saves platform management. Steps are copy/paste in Kibana — no terminal required.

# Elastic UI & Dashboard Workflows

## Part 1 — Discover & Explorer

1. **Analytics → Discover** or **Logs → Explorer** — explore available data.
2. Add a filter on `service.name` or `log.level`.
3. Save the search for reuse.

## Part 2 — Lens dashboards

1. **Analytics → Dashboards → Create dashboard**.
2. Add a **Lens** time series — event volume over time.
3. Add a **Drilldown** to open filtered logs on click.

## Part 3 — AI shortcut

Open **AI Assistant** and ask: *Show me error logs in the last hour by service.*

Click **Check**.
