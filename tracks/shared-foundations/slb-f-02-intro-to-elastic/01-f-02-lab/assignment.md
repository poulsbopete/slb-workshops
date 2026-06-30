---
slug: f-02-lab
id: 7axlyx5pq96w
type: challenge
title: F-02 — Intro to Elastic
teaser: Overview of the Elastic platform and how it fits into SLB SRE's observability
  journey — ingestion, storage, query, and visualization.
notes:
- type: text
  contents: |-
    ## While you wait…

    <iframe src="https://poulsbopete.github.io/slb-workshops/slides/f-02/"
      width="100%" height="800" frameborder="0"
      style="border-radius:8px;display:block">
    </iframe>

    *Provisioning your Elastic **Observability Serverless** lab for **F-02** (usually 2–3 minutes).*
tabs:
- id: uk37unyh1jev
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

# Intro to Elastic — Hands-on Lab

Welcome to your personal **Elastic Observability Serverless** project. This lab
supports the **F-02 — Intro to Elastic** live session.

## Part 1 — Platform tour

1. Open the **Elastic Serverless** tab (Kibana Home).
2. Navigate **Observability → Overview**. Note the unified view of logs, metrics, and traces.
3. Open **Stack Management → Index Management**. Observe data streams created by the platform.
4. Open **Stack Management → Data tiers**. Review hot / warm / cold / frozen / delete concepts
   from the session.

## Part 2 — Persona lenses

Pick the lens closest to your role:

| Persona | Start here |
|---------|------------|
| Developer | **Observability → APM → Services** |
| SRE / Infra | **Observability → Hosts** and **Fleet** |
| Analyst | **Analytics → Discover** |
| Architect | **Stack Management → Index Lifecycle Policies** |

## Part 3 — SLB context

Discuss with your facilitator: which of these building blocks map to your current
Grafana / Prometheus / OTel workflows today?

When finished, click **Check**.
