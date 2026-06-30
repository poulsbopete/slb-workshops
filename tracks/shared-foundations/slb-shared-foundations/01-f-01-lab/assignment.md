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
    >\n</iframe>\n\n*Provisioning your Elastic **Observability Serverless** lab for\
    \ **F-01** (usually 2–3 minutes).*"
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
> **Elastic Observability Serverless** — use the **Elastic Serverless** tab only. These labs focus on **managed Serverless** capabilities (no ILM, Fleet, or self-managed tiers). Steps are copy/paste in Kibana — no terminal required.

# Your Elastic Team, Support & Best Practices (Serverless)

## Part 1 — Your Serverless project

1. Open the **Elastic Serverless** tab (Kibana Home).
2. Note the project type: **Observability Serverless** — fully managed, no cluster to operate.
3. Click **Help** (?) — bookmark **Documentation** and support paths for Serverless.

## Part 2 — Support readiness

Draft a support ticket template for Serverless:

| Field | Your answer |
|-------|-------------|
| Project type | Observability Serverless |
| Region / project ID | (from project settings if visible) |
| Symptom | |
| Time range | |
| ES|QL or query tried | |

## Part 3 — Enablement program

With your facilitator, pick the SME track that matches your role.

Click **Check**.
