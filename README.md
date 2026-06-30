# SLB × Elastic Workshop Program — Instruqt Labs

Hands-on Instruqt tracks for the **SLB SRE × Elastic** enablement program. **One Instruqt track per workshop session**, organized by section.

| Resource | Link |
|----------|------|
| Live registration | [events.elastic.co/slbworkshops](https://events.elastic.co/slbworkshops) |
| Instruqt | [play.instruqt.com/manage/elastic/tracks](https://play.instruqt.com/manage/elastic/tracks) |
| Source repo | [github.com/poulsbopete/slb-workshops](https://github.com/poulsbopete/slb-workshops) |

Filter tracks in Instruqt by tag **`slb-workshops`** or **`slb`** (all program tracks), or by section e.g. **`slb-section-aiops`**.

## Sections

| Section | Tag | Tracks |
|---------|-----|--------|
| **All SLB tracks** | `slb-workshops`, `slb` | every track below |
| **Foundations** | `slb-section-foundations` | F-02, F-03 |
| **Developers** | `slb-section-developers` | Dev 01–03 |
| **SRE & Infra Ops** | `slb-section-sre` | SRE 01–04 |
| **BI & Analysts** | `slb-section-bi` | BI 01–03 |
| **AIOps & Alerting** | `slb-section-aiops` | AIOps 01–02 |
| **Reference** | `slb-section-reference` | DB monitoring lab |

Full mapping: [`catalog/sections.yaml`](catalog/sections.yaml) · Session metadata: [`catalog/workshops.yaml`](catalog/workshops.yaml)

### Example track slugs

```
tracks/aiops/slb-aiops-01-alert-fatigue/
tracks/developers/slb-dev-02-esql-essentials/
tracks/sre/slb-sre-01-platform-ops/
```

Titles follow **`SLB {Section} {NN} — {Topic}`** (e.g. *SLB AIOps 01 — Alert Fatigue & Noise Reduction*).

## Repository layout

```
catalog/
  workshops.yaml              # Session schedule (source of truth)
  sections.yaml               # Section → track slug mapping
tracks/
  foundations/ slb-f-02-…
  developers/  slb-dev-01-…
  sre/         slb-sre-01-…
  bi/          slb-bi-01-…
  aiops/       slb-aiops-01-…
  reference/   slb-workshops   # OTel DB monitoring reference only
shared/                       # Serverless bootstrap scripts
scripts/
  generate-tracks.py            # Scaffold new section tracks
  sync-section-tags.py          # Patch section tags on track.yml
```

## Workflow

```bash
make list                  # tracks grouped by section
make list-sections         # section tags and collection names
make push-section SECTION=aiops   # push one section only
make publish               # git push + push all Instruqt tracks
```

Each track provisions a fresh **Elastic Observability Serverless** project per participant via `elastic/es3-api-v2`.

## Instruqt collections

Create one collection per section in the Instruqt UI (names in `catalog/sections.yaml`):

- **SLB — Foundations**
- **SLB — Developer Track**
- **SLB — SRE Track**
- **SLB — BI & Analyst Track**
- **SLB — AIOps Track**

Add the matching `slb-*` tracks to each collection and share invite links with workshop attendees.

## License

Internal Elastic / SLB enablement content. Contact peter.simkins@elastic.co.
