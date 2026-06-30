---
slug: sre-04-lab
id: whmifgelxfmb
type: challenge
title: SRE 04 — Production Readiness Workshop
teaser: Validation checklists, runbook documentation, and ingestion health checks.
notes:
- type: text
  contents: "## While you wait…\n\n<iframe src=\"https://poulsbopete.github.io/slb-workshops/slides/sre-04/\"\
    \n  width=\"100%\" height=\"800\" frameborder=\"0\"\n  style=\"border-radius:8px;display:block\"\
    >\n</iframe>\n\n*Provisioning your Elastic **Observability Serverless** lab for\
    \ **SRE 04** (usually 2–3 minutes).*"
- type: text
  contents: '## Provisioning your lab…


    Creating an Elastic **Observability Serverless** project for **SRE 04**.

    This usually takes 2–3 minutes.


    **Live session topics:**

    - Validation checklists and runbook documentation

    - Ingestion health checks

    - Building confidence operating Elastic in production

    '
tabs:
- id: tzs36ugxw8ak
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
- id: meoh8e6xvdod
  title: Terminal
  type: terminal
  hostname: es3-api
difficulty: ''
timelimit: 0
enhanced_loading: null
---

# Production Readiness Workshop

## Part 1 — Validation checklist

Work through this checklist in Kibana:

- [ ] Data streams receiving data (Index Management)
- [ ] ILM policies attached
- [ ] Fleet agents healthy (if applicable)
- [ ] Critical alert rules enabled
- [ ] Dashboards loading for SLO review

## Part 2 — Ingestion health

1. **Observability → Logs → Anomalies** (if enabled).
2. **Fleet → Agent details** — last check-in times.

## Part 3 — Runbook draft

In the Terminal tab, create a runbook outline:

```bash
cat > /root/production-readiness-notes.md <<'EOF'
# SLB Elastic Production Readiness
## Ingestion health checks
## Escalation contacts
## Rollback criteria
EOF
cat /root/production-readiness-notes.md
```

Click **Check**.
