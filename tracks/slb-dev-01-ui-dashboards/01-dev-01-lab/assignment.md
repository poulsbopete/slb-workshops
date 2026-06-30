---
slug: dev-01-lab
id: ukvg5wt2qp5g
type: challenge
title: Dev 01 — Elastic UI & Dashboard Workflows
teaser: Fast track to Kibana — Discover, dashboards, filters, and drilldowns with
  direct comparisons to Grafana workflows.
notes:
- type: text
  contents: |
    ## Provisioning your lab…

    Creating an Elastic **Observability Serverless** project for **Dev 01**.
    This usually takes 2–3 minutes.

    **Live session topics:**
    - Navigating Discover, filtering, drilldowns
    - Grafana-to-Elastic translation for dashboard users
    - Dashboard navigation and customization
tabs:
- id: dvt78huvv8ng
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
- id: 0henpfrjwxl3
  title: Terminal
  type: terminal
  hostname: es3-api
difficulty: ""
timelimit: 0
enhanced_loading: null
---

# Elastic UI & Dashboard Workflows

**Audience:** Developers coming from Grafana.

## Part 1 — Discover

1. **Analytics → Discover** — select a logs data stream.
2. Add a KQL filter (e.g. `service.name : *`).
3. Save the search.

## Part 2 — Dashboards

1. **Analytics → Dashboards → Create dashboard**.
2. Add a **Lens** visualization — time series of log volume by service.
3. Add a **Drilldown** from the chart to Discover (filter on clicked series).

## Part 3 — Grafana translation exercise

| Your Grafana habit | Do this in Kibana |
|--------------------|-------------------|
| Dashboard variables | **Controls** on dashboard |
| Panel links | **Drilldowns** |
| Explore from panel | **Open in Discover** |

Customize one panel title and layout. Click **Check**.
