---
slug: sre-02-lab
id: j4ayxfexqrrc
type: challenge
title: SRE 02 — ILM & Data Tier Deep Dive
teaser: ILM policy design, data tier allocation, and common misconfigurations.
notes:
- type: text
  contents: |
    ## Provisioning your lab…

    Creating an Elastic **Observability Serverless** project for **SRE 02**.
    This usually takes 2–3 minutes.

    **Live session topics:**
    - ILM policy design and data tier allocation
    - ILM phase transitions and tier allocation behavior
    - Node roles and common misconfigurations
tabs:
- id: mdakwvjarazc
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
- id: rmbjgbbaojz6
  title: Terminal
  type: terminal
  hostname: es3-api
difficulty: ""
timelimit: 0
enhanced_loading: null
---

# ILM & Data Tier Deep Dive

## Part 1 — ILM policies

1. **Stack Management → Index Lifecycle Policies**.
2. Review phases: **hot → warm → cold → frozen → delete**.
3. Note rollover conditions on the hot phase.

## Part 2 — Tier allocation

1. Open a policy and inspect **allocate** and **migrate** actions.
2. Discuss SLB retention targets with your facilitator.

## Part 3 — Common misconfigurations

Checklist to review:

- Rollover max_size vs ingest rate
- Warm phase shrink/replica settings
- Frozen searchable snapshot prerequisites

## Part 4 — API

```bash
source ~/.bashrc
curl -s -H "Authorization: ApiKey $ES_API_KEY" \
  "$ES_URL/_ilm/policy" | jq 'keys'
```

Click **Check**.
