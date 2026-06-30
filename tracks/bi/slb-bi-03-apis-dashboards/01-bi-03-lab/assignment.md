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
difficulty: ''
timelimit: 0
enhanced_loading: null
---
> **Serverless lab:** use the **Elastic Serverless** tab only. Every step is copy/paste in Kibana — no terminal or shell required.

# APIs, Integrations & Dashboard Building

## Part 1 — Search API (Dev Tools)

1. Open **Management → Dev Tools**.
2. Paste and click **Run**:

```
GET logs-*/_search
{
  "size": 3,
  "sort": [{ "@timestamp": "desc" }]
}
```

3. In the response, expand a hit and note field names under `_source`.

**Tip:** The same data appears in **Discover** — Dev Tools shows the raw API shape analysts integrate against.

## Part 2 — Dashboard for business review

1. **Analytics → Dashboards → Create dashboard**.
2. Add at least two **Lens** panels.
3. Add a **Markdown** panel with session context / KPI definitions.

## Part 3 — Schema considerations

1. **Stack Management → Data views** — open a data view.
2. Note field types: **keyword** vs **text** vs **date**.

Click **Check**.
