---
slug: program-overview
type: challenge
title: SLB Workshop Program Overview
teaser: Orientation to the SLB × Elastic enablement series and linked hands-on labs.
notes:
- type: text
  contents: |
    ## Welcome

    Provisioning your Elastic **Observability Serverless** environment.
    While you wait, review the workshop schedule below.
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

# SLB × Elastic Workshop Program

**Registration:** [events.elastic.co/slbworkshops](https://events.elastic.co/slbworkshops)

## Hands-on tracks (Instruqt)

| Code | Lab track slug |
|------|----------------|
| F-02 | `slb-f-02-intro-to-elastic` |
| F-03 | `slb-f-03-elastic-day-to-day` |
| Dev 01 | `slb-dev-01-ui-dashboards` |
| Dev 02 | `slb-dev-02-esql-essentials` |
| Dev 03 | `slb-dev-03-deployment-validation` |
| SRE 01 | `slb-sre-01-platform-ops` |
| SRE 02 | `slb-sre-02-ilm-data-tier` |
| SRE 03 | `slb-sre-03-ingestion-architecture` |
| SRE 04 | `slb-sre-04-production-readiness` |
| BI 01 | `slb-bi-01-dashboard-basics` |
| BI 02 | `slb-bi-02-esql-analysts` |
| BI 03 | `slb-bi-03-apis-dashboards` |
| AIOps 01 | `slb-aiops-01-alert-fatigue` |
| AIOps 02 | `slb-aiops-02-ai-investigation` |

Ask your facilitator for invite links to session-specific tracks.

## Next challenge

Continue to **Database Monitoring Lab** for the full OTel reference environment
(six database engines, dashboards, and alerting).

Click **Check** when you have reviewed the schedule.
