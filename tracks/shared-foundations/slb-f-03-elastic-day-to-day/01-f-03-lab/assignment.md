---
slug: f-03-lab
id: cq2uqdjy6zvy
type: challenge
title: F-03 — Elastic Day to Day
teaser: Practical examples of data ingestion, querying with ES|QL, and using Kibana
  dashboards — with a focus on what Grafana users need to know.
notes:
- type: text
  contents: "## While you wait…\n\n<iframe src=\"https://poulsbopete.github.io/slb-workshops/slides/f-03/\"\
    \n  width=\"100%\" height=\"800\" frameborder=\"0\"\n  style=\"border-radius:8px;display:block\"\
    >\n</iframe>\n\n*Provisioning your Elastic **Observability Serverless** lab for\
    \ **F-03** (usually 2–3 minutes).*"
tabs:
- id: otnmdwf9b6d0
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

> **Serverless lab:** use the **Elastic Serverless** tab only. Every step is copy/paste in Kibana — no terminal or shell required.

# Elastic Day to Day — Hands-on Lab

## Part 1 — Discover and ES|QL

1. Go to **Analytics → Discover** (or **Observability → Logs → Explorer**).
2. Open the ES|QL editor and run:

```esql
FROM logs-* | LIMIT 10
```

3. Add a filter on `@timestamp` for the last 15 minutes.

## Part 2 — Grafana → Elastic translation

| Grafana concept | Elastic equivalent |
|-----------------|-------------------|
| Explore | Discover / Logs Explorer |
| Dashboard panel | Lens visualization |
| Prometheus query | ES|QL or PromQL in Metrics |
| Alert rule | **Observability → Alerts** |

## Part 3 — Ingestion fundamentals

1. Open **Integrations** and browse an OTel or Elastic Agent integration.
2. Note the data stream naming pattern (`logs-*`, `metrics-*`, `traces-*`).

## Part 4 — See your indices (Dev Tools)

1. Open **Management → Dev Tools** (search “Dev Tools” in the Kibana header).
2. Paste into the console and click the **play** button:

```
GET _cat/indices?v
```

3. Scan the table for `logs-*`, `metrics-*`, and `traces-*` data streams.

Click **Check** when complete.
