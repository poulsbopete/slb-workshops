---
slug: f-03-lab
id: cq2uqdjy6zvy
type: challenge
title: F-03 — Elastic Day to Day
teaser: Practical examples of data ingestion, querying with ES|QL, and using Kibana
  dashboards — with a focus on what Grafana users need to know.
notes:
- type: text
  contents: |-
    ## While you wait…

    <iframe src="https://poulsbopete.github.io/slb-workshops/slides/f-03/"
      width="100%" height="800" frameborder="0"
      style="border-radius:8px;display:block">
    </iframe>

    *Provisioning your Elastic **Observability Serverless** lab for **F-03** (usually 2–3 minutes).*
- type: text
  contents: |
    ## Provisioning your lab…

    Creating an Elastic **Observability Serverless** project for **F-03**.
    This usually takes 2–3 minutes.

    **Live session topics:**
    - Data lifecycle in practice
    - Where ES|QL, dashboards and APIs fit into daily workflows
    - Ingestion fundamentals
    - Grafana → Elastic mental model translation
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
- id: 35pdiyavuwyw
  title: Terminal
  type: terminal
  hostname: es3-api
difficulty: ""
timelimit: 0
enhanced_loading: null
---

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

## Part 4 — API peek (Terminal tab)

```bash
source ~/.bashrc
curl -s -H "Authorization: ApiKey $ES_API_KEY" \
  "$ES_URL/_cat/indices?v" | head -20
```

Click **Check** when complete.
