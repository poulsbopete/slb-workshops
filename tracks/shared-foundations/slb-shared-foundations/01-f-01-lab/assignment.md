---
slug: f-01-lab
id: 1v9xivra74li
type: challenge
title: F-01 — Your Elastic Team, Support & Best Practices
teaser: Start here. This session introduces your Elastic team, shows you how to get
  the fastest and most effective support responses, and sets you up to have the best
  possible experience with Elastic.
notes:
- type: text
  contents: "## While you wait…\n\n<iframe src=\"https://poulsbopete.github.io/slb-workshops/slides/f-01/\"\
    \n  width=\"100%\" height=\"1400\" frameborder=\"0\"\n  style=\"border-radius:8px;display:block;width:100%;min-height:900px\"\
    >\n</iframe>\n\n*Provisioning your **Observability Serverless** lab for **F-01**\
    \ (usually 2–3 minutes). Same Kibana workflows apply on **ECH** and **self-managed**.*"
- type: text
  contents: '## Session topics

    - Meet your Elastic team — who does what and when to reach out

    - How to open an effective support ticket and what to expect

    - Escalation paths — when and how to escalate a case

    - Best practices for faster responses

    - Introduction to the enablement program

    '
tabs:
- id: ymzcz4ahn8fi
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
> **Lab environment:** Use the **Elastic Serverless** tab only. Hands-on steps run on **Observability Serverless** for a zero-ops learning experience. The **same observability capabilities** — ES|QL, Streams, AI Assistant, Agent Builder, Workflows, SLOs — apply on **ECH** and **self-managed**; Serverless mainly saves platform management (cluster sizing, ILM, Fleet, upgrades). Steps are copy/paste in Kibana — no terminal required.

# Your Elastic Team, Support & Best Practices

## Part 1 — Your lab project

1. Open the **Elastic Serverless** tab (Kibana Home).
2. Note the project type: **Observability Serverless** — our hands-on environment; the same Kibana apps apply on **ECH** and **self-managed**.
3. Click **Help** (?) — bookmark **Documentation** and support paths.

## Part 2 — Support readiness

Draft a support ticket template (works for any deployment):

| Field | Your answer |
|-------|-------------|
| Deployment | Serverless / ECH / self-managed |
| Project or cluster ID | |
| Symptom | |
| Time range | |
| ES|QL or query tried | |

## Part 3 — Enablement program

With your facilitator, pick the SME track that matches your role.

Click **Check**.
