---
slug: sre-03-lab
id: nexmo5rmxpmw
type: challenge
title: SRE 03 — Ingestion Architecture & Troubleshooting
teaser: Elastic Agent vs OTel tradeoffs, Prometheus ingestion, and failure store handling.
notes:
- type: text
  contents: |
    ## Provisioning your lab…

    Creating an Elastic **Observability Serverless** project for **SRE 03**.
    This usually takes 2–3 minutes.

    **Live session topics:**
    - Elastic Agent integrations vs OTel-native collection tradeoffs
    - Prometheus scrape and remote_write ingestion patterns
    - Failure store and ingest error handling
    - Diagnosing dashboard instability when switching Prometheus environments
tabs:
- id: 7qsvzoxxwzgp
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
- id: kqktiaul9kwh
  title: Terminal
  type: terminal
  hostname: es3-api
difficulty: ""
timelimit: 0
enhanced_loading: null
---

# Ingestion Architecture & Troubleshooting

## Part 1 — Integration comparison

1. **Integrations** — compare **Elastic Agent** vs **OpenTelemetry** integrations.
2. Note data stream outputs for each.

## Part 2 — Prometheus patterns

1. Search integrations for **Prometheus**.
2. Review **remote_write** vs **receiver scrape** options.

## Part 3 — Failure store

1. **Stack Management → Index Management** — look for failure store indices.
2. **Ingest Pipelines** — review on_failure handlers.

## Part 4 — Troubleshooting commands

```bash
source ~/.bashrc
curl -s -H "Authorization: ApiKey $ES_API_KEY" \
  "$ES_URL/_cat/indices?v&health=red"
```

Click **Check**.
