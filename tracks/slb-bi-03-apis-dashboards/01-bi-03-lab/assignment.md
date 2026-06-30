---
slug: bi-03-lab
type: challenge
title: "BI 03 — APIs, Integrations & Dashboard Building"
teaser: "Elasticsearch API basics and building dashboards for operational reporting."
notes:
- type: text
  contents: |
    ## Provisioning your lab…

    Creating an Elastic **Observability Serverless** project for **BI 03**.
    This usually takes 2–3 minutes.

    **Live session topics:**
    - API calls and pulling data into external tools
    - Building dashboards for operational and business review
    - Data schema considerations
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
- title: Terminal
  type: terminal
  hostname: es3-api
timelimit: 0
---

# APIs, Integrations & Dashboard Building

## Part 1 — Search API (Terminal)

```bash
source ~/.bashrc
curl -s -H "Authorization: ApiKey $ES_API_KEY" \
  -H "Content-Type: application/json" \
  "$ES_URL/logs-*/_search" \
  -d '{"size":3,"sort":[{"@timestamp":"desc"}]}' | jq '.hits.hits[]._source | keys'
```

## Part 2 — Dashboard for business review

1. Create a dashboard with at least two Lens panels.
2. Add a markdown panel with session context / KPI definitions.

## Part 3 — Schema considerations

Note field types in **Stack Management → Data views** — keyword vs text vs date.

Click **Check**.
