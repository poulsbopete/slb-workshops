---
slug: sre-02-lab
id: j4ayxfexqrrc
type: challenge
title: SRE 02 — ILM & Data Tier Deep Dive
teaser: ILM policy design, data tier allocation, and common misconfigurations.
notes:
- type: text
  contents: |-
    ## While you wait…

    <iframe src="https://poulsbopete.github.io/slb-workshops/slides/sre-02/"
      width="100%" height="800" frameborder="0"
      style="border-radius:8px;display:block">
    </iframe>

    *Provisioning your Elastic **Observability Serverless** lab for **SRE 02** (usually 2–3 minutes).*
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
difficulty: ""
timelimit: 0
enhanced_loading: null
---
> **Serverless lab:** use the **Elastic Serverless** tab only. Every step is copy/paste in Kibana — no terminal or shell required.

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

## Part 4 — Policy names (Dev Tools)

After reviewing policies in the UI, paste in **Management → Dev Tools**:

```
GET _ilm/policy
```

Note the policy names in the response (keys of the JSON object).

Click **Check**.
