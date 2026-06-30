#!/usr/bin/env python3
"""Generate GitHub Pages slide decks from catalog/workshops.yaml."""

from __future__ import annotations

import html
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from slide_infographics import infographic_slides
CATALOG = ROOT / "catalog" / "workshops.yaml"
DOCS = ROOT / "docs"
SLIDES = DOCS / "slides"
from site_config import slide_deck_url, slides_base


def section_slides(workshop: dict) -> list[tuple[str, str]]:
    """Return list of (heading, markdown-ish body) for reveal sections."""
    slides: list[tuple[str, str]] = []
    code = workshop["code"]
    title = workshop["title"]
    series = workshop.get("series", "")
    presenter = workshop.get("presenter", "TBD")
    date = workshop.get("date") or "TBD"
    desc = workshop.get("description", "").strip()

    slides.append(
        (
            f"{code} — {title}",
            f"<p class=\"series\">{html.escape(series)}</p>"
            f"<p><strong>Presenter:</strong> {html.escape(presenter)}</p>"
            f"<p><strong>Date:</strong> {html.escape(str(date))}</p>"
            f"<p class=\"muted\">SLB × Elastic Workshop Program</p>",
        )
    )

    if desc:
        slides.append(("Overview", f"<p>{html.escape(desc)}</p>"))

    slides.append(
        (
            "Where this applies",
            "<p>These labs run on <strong>Observability Serverless</strong> — a fully managed "
            "project so you can practice without cluster operations.</p>"
            "<p>The <strong>same capabilities</strong> you explore here — "
            "<strong>ES|QL, Streams, AI Assistant, Agent Builder, Workflows, and SLOs</strong> — "
            "are available on <strong>Elastic Cloud Hosted (ECH)</strong> and "
            "<strong>self-managed</strong> deployments.</p>"
            "<p><strong>Serverless</strong> mainly saves operational toil (sizing, ILM, Fleet, upgrades). "
            "Your observability skills transfer directly.</p>",
        )
    )

    topics = workshop.get("topics") or []
    if topics:
        items = "".join(f"<li>{html.escape(t)}</li>" for t in topics)
        slides.append(("Session topics", f"<ul>{items}</ul>"))

    wid = workshop["id"]
    for heading, body in infographic_slides(wid):
        slides.append((heading, body))

    fmt = workshop.get("format", "")
    track = workshop.get("instruqt_track")
    if track:
        slides.append(
            (
                "Hands-on lab",
                "<p>Your lab uses <strong>Elastic Observability Serverless</strong> "
                "for a zero-ops learning environment.</p>"
                "<p>The steps and features are the same on <strong>ECH</strong> and "
                "<strong>on-prem</strong> — follow the assignment panel when Kibana opens.</p>"
                f"<p class=\"mono\">Instruqt track: {html.escape(track)}</p>",
            )
        )
    elif fmt == "webinar":
        slides.append(
            (
                "Live session",
                "<p>This session is presentation-focused — no Instruqt lab required.</p>"
                "<p>Register at "
                '<a href="https://events.elastic.co/slbworkshops" target="_blank" rel="noopener">'
                "events.elastic.co/slbworkshops</a></p>",
            )
        )

    slides.append(
        (
            "Resources",
            "<ul>"
            "<li>Registration: events.elastic.co/slbworkshops</li>"
            "<li>Repo: github.com/poulsbopete/slb-workshops</li>"
            "<li>Use ← → arrow keys to navigate slides</li>"
            "</ul>",
        )
    )
    return slides


def render_deck(workshop: dict) -> str:
    wid = workshop["id"]
    sections = section_slides(workshop)
    section_html = []
    for heading, body in sections:
        ig_class = ' class="ig-slide"' if heading.startswith("Why ") else ""
        section_html.append(
            f"<section{ig_class}><h2>{html.escape(heading)}</h2>{body}</section>"
        )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>{html.escape(workshop['code'])} — {html.escape(workshop['title'])} | SLB Workshops</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/reveal.css"/>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/theme/black.css"/>
  <link rel="stylesheet" href="../../assets/slb-theme.css"/>
</head>
<body>
  <div class="reveal">
    <div class="slides">
      {''.join(section_html)}
    </div>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/reveal.js"></script>
  <script>
    Reveal.initialize({{
      hash: true,
      slideNumber: true,
      width: 960,
      height: 700,
      margin: 0.08,
      transition: 'slide'
    }});
  </script>
</body>
</html>
"""


def render_index(workshops: list[dict]) -> str:
    by_series: dict[str, list[dict]] = {}
    for ws in workshops:
        by_series.setdefault(ws.get("series", "Other"), []).append(ws)

    sections_html = []
    for series in sorted(by_series.keys()):
        items = []
        for ws in sorted(by_series[series], key=lambda w: w.get("code", "")):
            wid = ws["id"]
            items.append(
                f'<li><a href="slides/{wid}/">{html.escape(ws["code"])} — '
                f'{html.escape(ws["title"])}</a></li>'
            )
        sections_html.append(
            f"<section><h2>{html.escape(series)}</h2><ul>{''.join(items)}</ul></section>"
        )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>SLB × Elastic Workshop Slides</title>
  <link rel="stylesheet" href="assets/slb-theme.css"/>
</head>
<body class="hub">
  <header>
    <h1>SLB × Elastic Workshop Slides</h1>
    <p>GitHub Pages decks embedded in Instruqt labs while environments provision.</p>
    <p><a href="https://events.elastic.co/slbworkshops">Register for live sessions →</a></p>
  </header>
  <main>
    {''.join(sections_html)}
  </main>
</body>
</html>
"""


def main() -> None:
    with CATALOG.open() as f:
        catalog = yaml.safe_load(f)
    workshops = catalog["workshops"]

    SLIDES.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(exist_ok=True)

    for ws in workshops:
        out_dir = SLIDES / ws["id"]
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "index.html").write_text(render_deck(ws))
        print(f"  ✓ docs/slides/{ws['id']}/index.html")

    (DOCS / "index.html").write_text(render_index(workshops))
    print(f"  ✓ docs/index.html")
    print(f"\nSlides base URL: {slides_base()}/slides/<workshop-id>/")

if __name__ == "__main__":
    main()
