#!/usr/bin/env python3
"""Sync lab markdown bodies from generate-tracks LABS dict; remove Terminal tabs."""

from __future__ import annotations

import importlib.util
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
TRACKS = ROOT / "tracks"
CATALOG = ROOT / "catalog" / "workshops.yaml"

LAB_INTRO = """> **Serverless lab:** use the **Elastic Serverless** tab only. Every step is copy/paste in Kibana — no terminal or shell required.

"""

KEEP_TERMINAL_SLUGS = {"slb-workshops"}


def load_labs() -> dict[str, str]:
    spec = importlib.util.spec_from_file_location(
        "generate_tracks", ROOT / "scripts" / "generate-tracks.py"
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.LABS


def slug_to_workshop_id() -> dict[str, str]:
    with CATALOG.open() as f:
        data = yaml.safe_load(f)
    return {
        ws["instruqt_track"]: ws["id"]
        for ws in data["workshops"]
        if ws.get("instruqt_track")
    }


def split_assignment(text: str) -> tuple[dict, str] | None:
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        return None
    front = yaml.safe_load(m.group(1))
    body = text[m.end() :]
    if not isinstance(front, dict):
        return None
    return front, body


def strip_terminal_tab(front: dict, slug: str) -> bool:
    if slug in KEEP_TERMINAL_SLUGS:
        return False
    tabs = front.get("tabs") or []
    new_tabs = [
        t for t in tabs if t.get("type") != "terminal" and t.get("title") != "Terminal"
    ]
    if len(new_tabs) == len(tabs):
        return False
    front["tabs"] = new_tabs
    return True


def dedupe_notes(front: dict) -> bool:
    notes = front.get("notes") or []
    if not notes:
        return False
    kept = [notes[0]]
    first_has_iframe = "iframe src=" in str(notes[0].get("contents", ""))
    has_topics = False
    for n in notes[1:]:
        c = str(n.get("contents", ""))
        if first_has_iframe and "Provisioning your lab" in c:
            continue
        if "Live session topics" in c or "## Session topics" in c:
            if not has_topics:
                kept.append(n)
                has_topics = True
            continue
        kept.append(n)
    if len(kept) == len(notes):
        return False
    front["notes"] = kept
    return True


def patch_assignment(path: Path, workshop_id: str, slug: str, labs: dict[str, str]) -> bool:
    text = path.read_text()
    split = split_assignment(text)
    if not split:
        return False
    front, old_body = split
    changed = False
    new_body = old_body

    if workshop_id in labs and slug not in KEEP_TERMINAL_SLUGS:
        new_body = LAB_INTRO + labs[workshop_id].strip() + "\n"
        if new_body != old_body:
            changed = True

    if strip_terminal_tab(front, slug):
        changed = True
    if dedupe_notes(front):
        changed = True

    if not changed:
        return False

    dumped = yaml.dump(front, default_flow_style=False, sort_keys=False, allow_unicode=True)
    path.write_text(f"---\n{dumped}---\n{new_body}")
    return True


def main() -> None:
    labs = load_labs()
    mapping = slug_to_workshop_id()
    for track_yml in sorted(TRACKS.rglob("track.yml")):
        slug = track_yml.parent.name
        wid = mapping.get(slug)
        if not wid:
            continue
        for assignment in track_yml.parent.glob("*/assignment.md"):
            if patch_assignment(assignment, wid, slug, labs):
                print(f"  ✓ {assignment.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
