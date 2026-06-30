# SLB × Elastic Workshop Program — Instruqt Labs

Hands-on Instruqt tracks for the **SLB SRE × Elastic** enablement program. **Eight consolidated tracks** — one per series — each containing multiple lab challenges (one per live session).

| Resource | Link |
|----------|------|
| Live registration | [events.elastic.co/slbworkshops](https://events.elastic.co/slbworkshops) |
| Instruqt | [play.instruqt.com/manage/elastic/tracks](https://play.instruqt.com/manage/elastic/tracks) |
| Source repo | [github.com/poulsbopete/slb-workshops](https://github.com/poulsbopete/slb-workshops) |
| Slide decks (GitHub Pages) | [poulsbopete.github.io/slb-workshops](https://poulsbopete.github.io/slb-workshops) |

Filter tracks in Instruqt by tag **`slb-workshops`** or **`slb`** (all program tracks), or by series e.g. **`slb-series-shared-foundations`**.

## Eight consolidated tracks

| Track slug | Series | Labs (sub-tracks) |
|------------|--------|-------------------|
| `slb-shared-foundations` | Shared Foundations | F-01, F-02, F-03, F-04 |
| `slb-sme-developers` | SME Track: Developers | Dev 01–03 |
| `slb-sme-sre-infra-ops` | SME Track: SRE & Infra Ops | SRE 01–04 |
| `slb-sme-architects` | SME Track: Architects | Arch 01–02 |
| `slb-sme-bi-analysts` | SME Track: BI & Data Analysts | BI 01–03 |
| `slb-sme-aiops-alerting` | SME Track: AIOps & Alerting | AIOps 01–03 |
| `slb-one-offs` | One-off Sessions | AI/ML, RAG & MCP, Hybrid Search |
| `slb-sme-all-teams` | SME Track: All Teams | Cross-team review |

Each track uses a **single Serverless environment** for the whole series. Learners advance through numbered challenges (e.g. `01-f-01-lab` → `04-f-04-lab`) or jump to the lab matching their live session.

Full mapping: [`catalog/sections.yaml`](catalog/sections.yaml) · Session metadata: [`catalog/workshops.yaml`](catalog/workshops.yaml)

### Example layout

```
tracks/shared-foundations/slb-shared-foundations/
  track.yml
  01-f-01-lab/assignment.md
  02-f-02-lab/assignment.md
  03-f-03-lab/assignment.md
  04-f-04-lab/assignment.md
```

## Repository layout

```
catalog/
  workshops.yaml              # Session schedule (source of truth)
  sections.yaml               # 8 tracks → workshop_ids
  series.yaml                 # Canonical series definitions
tracks/
  shared-foundations/slb-shared-foundations/
  sme-developers/slb-sme-developers/
  sme-sre-infra-ops/slb-sme-sre-infra-ops/
  sme-architects/slb-sme-architects/
  sme-bi-analysts/slb-sme-bi-analysts/
  sme-aiops-alerting/slb-sme-aiops-alerting/
  one-offs/slb-one-offs/
  sme-all-teams/slb-sme-all-teams/
shared/                       # Serverless bootstrap scripts
scripts/
  generate-tracks.py          # Scaffold consolidated tracks + challenges
  sync-section-tags.py        # Patch series tags on track.yml
  delete-legacy-tracks.sh     # Remove old per-session Instruqt tracks
```

## GitHub Pages slides

Slide decks live in [`docs/`](docs/) (Reveal.js) and embed in each challenge while labs provision.

**Pages setup:** Repo → **Settings → Pages** → Source: **GitHub Actions** (recommended), or deploy from branch `main` folder **`/docs`**.

| URL | Content |
|-----|---------|
| [poulsbopete.github.io/slb-workshops](https://poulsbopete.github.io/slb-workshops) | Slide index |
| `.../slides/f-02/` | F-02 deck (example) |

```bash
make slides-all    # rebuild decks + update Instruqt iframes
make publish       # git push + push all 8 Instruqt tracks
```

## Workflow

```bash
make list                  # 8 tracks and their challenge folders
make list-sections         # series tags and collection names
make generate              # rebuild track scaffolds from catalog
make sync-labs             # sync lab bodies from LABS dict
make push-section SECTION=sme-developers
make publish
```

Each track provisions **Elastic Observability Serverless** via `elastic/es3-api-v2`. Labs are **Kibana-only** — ES|QL, Dev Tools, Lens; no Terminal tab.

## Instruqt collections

Create one collection per series (names in `catalog/sections.yaml`) and add the matching consolidated track:

- **SLB — Shared Foundations** → `slb-shared-foundations`
- **SLB — SME Track: Developers** → `slb-sme-developers`
- *(etc.)*

## License

Internal Elastic / SLB enablement content. Contact peter.simkins@elastic.co.
