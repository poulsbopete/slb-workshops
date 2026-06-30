#!/usr/bin/env python3
"""Apply section tags and metadata to existing track.yml files (preserves id/checksum)."""

from __future__ import annotations

import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "catalog" / "workshops.yaml"
SECTIONS = ROOT / "catalog" / "sections.yaml"
TRACKS_DIR = ROOT / "tracks"

BASE_TAGS = [
    "slb",
    "slb-workshops",
    "elastic",
    "serverless",
    "observability",
    "co.elastic.workshops",
]

# Legacy/noisy tags to strip when syncing
STRIP_TAGS = {
    "sme-track--aiops-&-alerting",
    "sme-track--developers",
    "sme-track--sre-&-infra-ops",
    "sme-track--bi-&-data-analysts",
    "all",
    "aiops",
    "developers",
    "sre",
    "bi",
    "foundations",
    "shared-foundations",
}


def slug_to_section() -> dict[str, str]:
    with SECTIONS.open() as f:
        data = yaml.safe_load(f)
    mapping: dict[str, str] = {}
    for section in data["sections"]:
        for slug in section["tracks"]:
            mapping[slug] = section["tag"]
    return mapping


def workshop_by_slug() -> dict[str, dict]:
    with CATALOG.open() as f:
        data = yaml.safe_load(f)
    return {
        ws["instruqt_track"]: ws
        for ws in data["workshops"]
        if ws.get("instruqt_track")
    }


def parse_track_yml(text: str) -> tuple[dict, str]:
    """Return parsed dict and trailing content after tags block if any."""
    return yaml.safe_load(text), text


def update_tags(existing: list[str], section_tag: str) -> list[str]:
    tags = [
        t
        for t in existing
        if not t.startswith("slb-section-") and not t.startswith("slb-series-")
    ]
    tags = [t for t in tags if t not in STRIP_TAGS]
    # slb + slb-workshops first, then section, then base, then any extras (e.g. database-monitoring)
    combined = ["slb", "slb-workshops", section_tag]
    for t in BASE_TAGS + tags:
        if t not in combined:
            combined.append(t)
    return combined


def patch_track(path: Path, section_tag: str, workshop: dict | None) -> bool:
    text = path.read_text()
    data = yaml.safe_load(text)
    if not isinstance(data, dict):
        return False

    changed = False
    new_tags = update_tags(data.get("tags") or [], section_tag)
    if new_tags != (data.get("tags") or []):
        data["tags"] = new_tags
        changed = True

    if workshop:
        code = workshop["code"]
        title = workshop["title"]
        expected_title = f"SLB {code} — {title}"
        if data.get("title") != expected_title:
            data["title"] = expected_title
            changed = True

    if not changed:
        return False

    # Preserve key order-ish: dump and keep checksum/id
    out = yaml.dump(data, default_flow_style=False, sort_keys=False, allow_unicode=True)
    path.write_text(out)
    return True


def find_track_dirs() -> list[Path]:
    dirs: list[Path] = []
    for p in TRACKS_DIR.rglob("track.yml"):
        if p.parent.name.startswith("slb-"):
            dirs.append(p.parent)
    return sorted(set(dirs))


def main() -> None:
    slug_sections = slug_to_section()
    workshops = workshop_by_slug()

    for track_dir in find_track_dirs():
        slug = track_dir.name
        section_tag = slug_sections.get(slug)
        if not section_tag:
            print(f"  ? skip {slug} (no section)")
            continue
        track_yml = track_dir / "track.yml"
        if patch_track(track_yml, section_tag, workshops.get(slug)):
            print(f"  ✓ patched {track_dir.relative_to(ROOT)}")
        else:
            print(f"  · unchanged {track_dir.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
