#!/usr/bin/env python3
"""Apply series tags and metadata to consolidated track.yml files."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SECTIONS = ROOT / "catalog" / "sections.yaml"
CATALOG = ROOT / "catalog" / "workshops.yaml"
TRACKS_DIR = ROOT / "tracks"

BASE_TAGS = [
    "slb",
    "slb-workshops",
    "elastic",
    "serverless",
    "observability",
    "co.elastic.workshops",
]

STRIP_TAGS = {
    "sme-track--aiops-&-alerting",
    "sme-track--developers",
    "sme-track--sre-&-infra-ops",
    "sme-track--bi-&-data-analysts",
    "foundations",
    "shared-foundations",
}


def load_sections() -> list[dict]:
    with SECTIONS.open() as f:
        return yaml.safe_load(f)["sections"]


def update_tags(existing: list[str], section_tag: str) -> list[str]:
    tags = [
        t
        for t in existing
        if not t.startswith("slb-section-") and not t.startswith("slb-series-")
    ]
    tags = [t for t in tags if t not in STRIP_TAGS]
    combined = ["slb", "slb-workshops", section_tag]
    for t in BASE_TAGS + tags:
        if t not in combined:
            combined.append(t)
    return combined


def load_generate_tracks():
    spec = importlib.util.spec_from_file_location(
        "generate_tracks", ROOT / "scripts" / "generate-tracks.py"
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def workshops_for_section(section: dict) -> list[dict]:
    with CATALOG.open() as f:
        by_id = {ws["id"]: ws for ws in yaml.safe_load(f)["workshops"]}
    return [by_id[wid] for wid in section["workshop_ids"]]


def patch_track(path: Path, section: dict, gen) -> bool:
    text = path.read_text()
    data = yaml.safe_load(text)
    if not isinstance(data, dict):
        return False

    changed = False
    section_tag = section["tag"]
    new_tags = update_tags(data.get("tags") or [], section_tag)
    if new_tags != (data.get("tags") or []):
        data["tags"] = new_tags
        changed = True

    expected_title = f"SLB — {section['name']}"
    if data.get("title") != expected_title:
        data["title"] = expected_title
        changed = True

    workshops = workshops_for_section(section)
    fresh = yaml.safe_load(gen.track_yml(section, workshops))
    for key in ("teaser", "description"):
        if data.get(key) != fresh.get(key):
            data[key] = fresh[key]
            changed = True

    if not changed:
        return False

    out = yaml.dump(data, default_flow_style=False, sort_keys=False, allow_unicode=True)
    path.write_text(out)
    return True


def main() -> None:
    gen = load_generate_tracks()
    for section in load_sections():
        track_dir = TRACKS_DIR / section["id"] / section["track"]
        track_yml = track_dir / "track.yml"
        if not track_yml.exists():
            print(f"  ? missing {track_yml.relative_to(ROOT)}")
            continue
        if patch_track(track_yml, section, gen):
            print(f"  ✓ patched {track_dir.relative_to(ROOT)}")
        else:
            print(f"  · unchanged {track_dir.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
