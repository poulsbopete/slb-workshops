# SLB × Elastic Workshop Program — Instruqt Labs

Hands-on Instruqt tracks for the **SLB SRE × Elastic** enablement program (June 2026 draft).

| Resource | Link |
|----------|------|
| Live registration | [events.elastic.co/slbworkshops](https://events.elastic.co/slbworkshops) |
| Instruqt (elastic team) | [play.instruqt.com/manage/elastic/tracks](https://play.instruqt.com/manage/elastic/tracks) |
| Source repo | [github.com/poulsbopete/slb-workshops](https://github.com/poulsbopete/slb-workshops) |

## Overview

This repository contains **Infrastructure-as-Code** definitions for SLB workshop labs. Each hands-on session gets its own Instruqt track that provisions a fresh **Elastic Observability Serverless** project per participant — always on the latest Elastic stack, with no shared cluster maintenance.

**Phase 1 — Foundation** (July 2026) and **Phase 2 — SME tracks** (August–November 2026) are catalogued in [`catalog/workshops.yaml`](catalog/workshops.yaml), sourced from the workshop planning spreadsheet.

### Workshop formats

| Format | Description | Instruqt track |
|--------|-------------|----------------|
| `webinar` | Live Zoom presentation only | — |
| `hybrid` | Live session + optional self-paced lab | ✓ |
| `hands-on` | Live session with guided lab | ✓ |

## Track index

### Phase 1 — Shared Foundations

| Code | Workshop | Track slug | Live date |
|------|----------|------------|-----------|
| F-01 | Your Elastic Team, Support & Best Practices | — (webinar) | Jul 15, 2026 |
| F-02 | Intro to Elastic | [`slb-f-02-intro-to-elastic`](tracks/slb-f-02-intro-to-elastic) | Jul 22, 2026 |
| F-03 | Elastic Day to Day | [`slb-f-03-elastic-day-to-day`](tracks/slb-f-03-elastic-day-to-day) | Jul 29, 2026 |
| F-04 | Looking Forward with Elastic | — (webinar) | Aug 5, 2026 |

### Phase 2 — SME Tracks

| Code | Workshop | Track slug | Audience |
|------|----------|------------|----------|
| Dev 01 | Elastic UI & Dashboard Workflows | [`slb-dev-01-ui-dashboards`](tracks/slb-dev-01-ui-dashboards) | Developers |
| Dev 02 | ES|QL Essentials for Troubleshooting | [`slb-dev-02-esql-essentials`](tracks/slb-dev-02-esql-essentials) | Developers |
| Dev 03 | Deployment Validation & Incident Workflows | [`slb-dev-03-deployment-validation`](tracks/slb-dev-03-deployment-validation) | Developers |
| SRE 01 | Platform Operations Fundamentals | [`slb-sre-01-platform-ops`](tracks/slb-sre-01-platform-ops) | SRE & Infra Ops |
| SRE 02 | ILM & Data Tier Deep Dive | [`slb-sre-02-ilm-data-tier`](tracks/slb-sre-02-ilm-data-tier) | SRE & Infra Ops |
| SRE 03 | Ingestion Architecture & Troubleshooting | [`slb-sre-03-ingestion-architecture`](tracks/slb-sre-03-ingestion-architecture) | SRE & Infra Ops |
| SRE 04 | Production Readiness Workshop | [`slb-sre-04-production-readiness`](tracks/slb-sre-04-production-readiness) | SRE & Infra Ops |
| Arch 01–02 | Architecture & Governance | — (webinar) | Architects |
| BI 01 | Dashboard & Data Exploration Basics | [`slb-bi-01-dashboard-basics`](tracks/slb-bi-01-dashboard-basics) | BI / Analysts |
| BI 02 | ES\|QL for Analysts | [`slb-bi-02-esql-analysts`](tracks/slb-bi-02-esql-analysts) | BI / Analysts |
| BI 03 | APIs, Integrations & Dashboard Building | [`slb-bi-03-apis-dashboards`](tracks/slb-bi-03-apis-dashboards) | BI / Analysts |
| AIOps 01 | Alert Fatigue & Noise Reduction | [`slb-aiops-01-alert-fatigue`](tracks/slb-aiops-01-alert-fatigue) | SRE / Developers |
| AIOps 02 | AI-Assisted Investigation & Automated Response | [`slb-aiops-02-ai-investigation`](tracks/slb-aiops-02-ai-investigation) | SRE / Developers |

### Reference

| Track | Description |
|-------|-------------|
| [`slb-workshops`](tracks/slb-workshops) | Full OTel database monitoring POC (6 engines, dashboards, alerts) |

## Repository layout

```
catalog/workshops.yaml          # Workshop metadata (source of truth)
shared/
  config.yml                    # Shared es3-api sandbox definition
  scripts/                      # Serverless bootstrap + cleanup
tracks/
  slb-f-02-intro-to-elastic/    # One directory per Instruqt track
    track.yml
    config.yml
    01-<id>-lab/
      assignment.md             # Lab instructions (YAML front matter + markdown)
      check-es3-api
    track_scripts/
      setup-es3-api             # Provisions Serverless + Kibana proxy
      cleanup-es3-api
scripts/
  generate-tracks.py            # Regenerate scaffolds from catalog
```

## Prerequisites

- [Instruqt CLI](https://docs.instruqt.com/instruqt-cli/installation) installed and authenticated
- Access to the **elastic** team on Instruqt
- Instruqt secret **`ESS_CLOUD_API_KEY`** configured on each track (Elastic Cloud Serverless API key)

## Workflow

### Pull an existing track from Instruqt

```bash
cd tracks/slb-f-02-intro-to-elastic
instruqt track pull
```

### Push local changes to Instruqt

```bash
cd tracks/slb-dev-02-esql-essentials
instruqt track push
```

Or push all tracks:

```bash
make push-all
```

### Regenerate scaffolds after editing the catalog

```bash
python3 scripts/generate-tracks.py
```

> **Note:** Regeneration overwrites generated files. Tracks with custom `id` fields (already pushed to Instruqt) should be re-pulled after regeneration to preserve IDs, or excluded from the generator.

## Architecture

Each track uses the **`elastic/es3-api-v2`** VM image to:

1. Create a dedicated **Observability Serverless** project via Elastic Cloud API
2. Proxy Kibana on port **8080** (Instruqt service tab)
3. Expose credentials in the **Terminal** tab (`source ~/.bashrc`)
4. Delete the project on track cleanup

This pattern keeps labs current with Elastic 9.x Serverless without maintaining long-lived clusters.

## Creating an Instruqt collection

For the full program, create a collection in the Instruqt UI (**elastic** team) named **SLB Workshops** and add all `slb-*` tracks. Share collection invite links alongside the [Splash registration page](https://events.elastic.co/slbworkshops).

## Contributing

1. Edit workshop metadata in `catalog/workshops.yaml`
2. Customize lab content in `tracks/<slug>/01-*/assignment.md`
3. Add workshop-specific seed scripts under `shared/seeds/` if needed
4. Push to GitHub and Instruqt

## License

Internal Elastic / SLB enablement content. Contact peter.simkins@elastic.co.
