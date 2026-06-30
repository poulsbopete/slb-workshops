---
slug: bi-03-lab
id: reccecsquqaj
type: challenge
title: BI 03 — APIs, Integrations & Dashboard Building
teaser: Elasticsearch API basics and building dashboards for operational reporting.
notes:
- type: text
  contents: "## While you wait…\n\n<iframe src=\"https://poulsbopete.github.io/slb-workshops/slides/bi-03/\"\
    \n  width=\"100%\" height=\"800\" frameborder=\"0\"\n  style=\"border-radius:8px;display:block\"\
    >\n</iframe>\n\n*Provisioning your Elastic **Observability Serverless** lab for\
    \ **BI 03** (usually 2–3 minutes).*"
- type: text
  contents: '## Provisioning your lab…


    Creating an Elastic **Observability Serverless** project for **BI 03**.

    This usually takes 2–3 minutes.


    **Live session topics:**

    - API calls and pulling data into external tools

    - Building dashboards for operational and business review

    - Data schema considerations

    '
tabs:
- id: ivrpulj1xtrh
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
- id: xvewxworusva
  title: Terminal
  type: terminal
  hostname: es3-api
difficulty: ''
timelimit: 0
enhanced_loading: null
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
