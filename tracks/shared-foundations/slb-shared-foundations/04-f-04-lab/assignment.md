---
slug: f-04-lab
id: by3sx37gxyko
type: challenge
title: F-04 — Looking Forward with Elastic
teaser: First look at Elastic 9.x and what it means for SLB SRE.
notes:
- type: text
  contents: |-
    ## While you wait…

    <iframe src="https://poulsbopete.github.io/slb-workshops/docs/slides/f-04/"
      width="100%" height="1400" frameborder="0"
      style="border-radius:8px;display:block;width:100%;min-height:900px">
    </iframe>

    *Provisioning your Elastic **Observability Serverless** lab for **F-04** (usually 2–3 minutes).*
- type: text
  contents: |
    ## Session topics
    - What's new in Elastic 9.x
    - What to expect during the migration
    - Key features relevant to SLB SRE
    - Roadmap highlights
tabs:
- id: choly6ztcbdi
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

# Looking Forward with Elastic — Hands-on Lab

## Part 1 — What's new in 9.x

1. Open **Elastic Serverless** → **What's new** (release highlights).
2. Browse **Stack Management → Upgrade Assistant** or release notes links.

## Part 2 — Migration preview

1. **Observability → Overview** — note unified navigation changes.
2. **Stack Management → Index Management** — review data stream defaults.

## Part 3 — SLB roadmap discussion

With facilitator, identify one Elastic 9.x feature relevant to your team's migration.

Click **Check**.
