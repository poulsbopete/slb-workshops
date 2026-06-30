# SLB × Elastic Workshop Program — Instruqt Labs

Hands-on Instruqt tracks for the **SLB SRE × Elastic** enablement program. **One Instruqt track per workshop session**, organized by **series category**.

| Resource | Link |
|----------|------|
| Live registration | [events.elastic.co/slbworkshops](https://events.elastic.co/slbworkshops) |
| Instruqt | [play.instruqt.com/manage/elastic/tracks](https://play.instruqt.com/manage/elastic/tracks) |
| Source repo | [github.com/poulsbopete/slb-workshops](https://github.com/poulsbopete/slb-workshops) |
| Slide decks (GitHub Pages) | [poulsbopete.github.io/slb-workshops](https://poulsbopete.github.io/slb-workshops) |

Filter tracks in Instruqt by tag **`slb-workshops`** or **`slb`** (all program tracks), or by series e.g. **`slb-series-shared-foundations`**.

## Series categories

| Series | Tag | Sessions |
|--------|-----|----------|
| **All SLB tracks** | `slb-workshops`, `slb` | every track below |
| **Shared Foundations** | `slb-series-shared-foundations` | F-01–F-04 |
| **SME Track: Developers** | `slb-series-sme-developers` | Dev 01–03 |
| **SME Track: SRE & Infra Ops** | `slb-series-sme-sre` | SRE 01–04 |
| **SME Track: Architects** | `slb-series-sme-architects` | Arch 01–02 |
| **SME Track: BI & Data Analysts** | `slb-series-sme-bi` | BI 01–03 |
| **SME Track: AIOps & Alerting** | `slb-series-sme-aiops` | AIOps 01–03 |
| **One-off: AI/ML Overview** | `slb-series-oneoff-ai-ml` | AI/ML Overview |
| **One-off: RAG & MCP** | `slb-series-oneoff-rag-mcp` | RAG & MCP |
| **One-off: Hybrid Search** | `slb-series-oneoff-hybrid-search` | Hybrid Search |
| **SME Track: All Teams** | `slb-series-sme-all-teams` | Cross-team review |
| **Reference** | `slb-series-reference` | DB monitoring lab |

Full mapping: [`catalog/sections.yaml`](catalog/sections.yaml) · [`catalog/series.yaml`](catalog/series.yaml) · Session metadata: [`catalog/workshops.yaml`](catalog/workshops.yaml)

### Example track paths

```
tracks/shared-foundations/slb-f-02-intro-to-elastic/
tracks/sme-developers/slb-dev-02-esql-essentials/
tracks/sme-aiops-alerting/slb-aiops-01-alert-fatigue/
tracks/oneoff-rag-mcp/slb-oneoff-rag-mcp/
```

Titles follow **`SLB {Code} — {Topic}`** (e.g. *SLB AIOps 01 — Alert Fatigue & Noise Reduction*).

## Repository layout

```
catalog/
  workshops.yaml              # Session schedule (source of truth)
  sections.yaml               # Series → track slug mapping
  series.yaml                 # Canonical series definitions
tracks/
  shared-foundations/         # F-01–F-04
  sme-developers/             # Dev 01–03
  sme-sre-infra-ops/          # SRE 01–04
  sme-architects/             # Arch 01–02
  sme-bi-analysts/            # BI 01–03
  sme-aiops-alerting/         # AIOps 01–03
  oneoff-ai-ml/               # AI/ML Overview
  oneoff-rag-mcp/             # RAG & MCP
  oneoff-hybrid-search/       # Hybrid Search
  sme-all-teams/              # Cross-team review
  reference/                  # slb-workshops (OTel DB monitoring)
shared/                       # Serverless bootstrap scripts
scripts/
  generate-tracks.py          # Scaffold new series tracks
  sync-section-tags.py        # Patch series tags on track.yml
```

## GitHub Pages slides

Slide decks live in [`docs/slides/`](docs/slides/) (Reveal.js) and embed in Instruqt while labs provision.

**One-time setup:** Repo → **Settings → Pages** → Source: **Deploy from a branch** → `main` → `/docs`  
(or enable **GitHub Actions** as source to use `.github/workflows/pages.yml`).

| URL | Content |
|-----|---------|
| [poulsbopete.github.io/slb-workshops](https://poulsbopete.github.io/slb-workshops) | Slide index |
| `.../slides/f-02/` | F-02 deck (example) |
| `.../slides/aiops-01/` | AIOps 01 deck |

Regenerate after catalog changes:

```bash
make slides-all    # rebuild decks + update Instruqt iframes
make publish
```

## Workflow

```bash
make list                  # tracks grouped by series
make list-sections         # series tags and collection names
make slides-all            # regenerate GitHub Pages decks + embed in Instruqt
make push-section SECTION=sme-aiops-alerting   # push one series only
make publish               # git push + push all Instruqt tracks
```

Each track provisions a fresh **Elastic Observability Serverless** project per participant via `elastic/es3-api-v2`. Labs are **Kibana-only** — copy/paste in the UI (ES|QL, Dev Tools, Lens). The Terminal tab is omitted from session tracks; the reference DB monitoring track keeps it for optional advanced steps.

## Instruqt collections

Create one collection per series in the Instruqt UI (names in `catalog/sections.yaml`):

- **SLB — Shared Foundations**
- **SLB — SME Track: Developers**
- **SLB — SME Track: SRE & Infra Ops**
- **SLB — SME Track: Architects**
- **SLB — SME Track: BI & Data Analysts**
- **SLB — SME Track: AIOps & Alerting**
- **SLB — One-off: AI/ML Overview**
- **SLB — One-off: RAG & MCP**
- **SLB — One-off: Hybrid Search**
- **SLB — SME Track: All Teams**

Add the matching `slb-*` tracks to each collection and share invite links with workshop attendees.

## License

Internal Elastic / SLB enablement content. Contact peter.simkins@elastic.co.
