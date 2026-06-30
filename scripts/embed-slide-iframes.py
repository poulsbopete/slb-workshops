#!/usr/bin/env python3
"""Embed GitHub Pages slide iframes into Instruqt assignment.md notes."""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

CATALOG = ROOT / "catalog" / "workshops.yaml"
TRACKS = ROOT / "tracks"
from site_config import slide_deck_url

IFRAME_HEIGHT = 1400


def workshops_by_id() -> dict[str, dict]:
    with CATALOG.open() as f:
        data = yaml.safe_load(f)
    return {ws["id"]: ws for ws in data["workshops"]}


def workshop_id_from_path(path: Path) -> str | None:
    m = re.match(r"^\d+-(.+)-lab$", path.parent.name)
    return m.group(1) if m else None


def iframe_note(workshop: dict) -> str:
    wid = workshop["id"]
    code = workshop["code"]
    url = slide_deck_url(wid)
    return (
        f"## While you wait…\n\n"
        f"<iframe src=\"{url}\"\n"
        f"  width=\"100%\" height=\"{IFRAME_HEIGHT}\" frameborder=\"0\"\n"
        f"  style=\"border-radius:8px;display:block;width:100%;min-height:900px\">\n"
        f"</iframe>\n\n"
        f"*Provisioning your **Observability Serverless** lab for **{code}** "
        f"(usually 2–3 minutes). Same Kibana workflows apply on **ECH** and **self-managed**.*"
    )


def split_front_matter(text: str) -> tuple[str, dict, str] | None:
    if not text.startswith("---"):
        return None
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        return None
    front_raw = match.group(1)
    body = text[match.end() :]
    front = yaml.safe_load(front_raw)
    if not isinstance(front, dict):
        return None
    return front_raw, front, body


def patch_simple_assignment(path: Path, workshop: dict) -> bool:
    text = path.read_text()
    split = split_front_matter(text)
    if not split:
        return False
    _, front, body = split

    slide_contents = iframe_note(workshop)
    notes = front.get("notes") or []
    if notes and "iframe src=" in str(notes[0].get("contents", "")):
        notes[0]["contents"] = slide_contents
    else:
        notes.insert(0, {"type": "text", "contents": slide_contents})

    front["notes"] = notes
    dumped = yaml.dump(front, default_flow_style=False, sort_keys=False, allow_unicode=True)
    new_text = f"---\n{dumped.rstrip()}\n---\n{body.lstrip()}"
    if new_text == text:
        return False
    path.write_text(new_text)
    return True


def find_assignments() -> list[tuple[Path, str]]:
    out: list[tuple[Path, str]] = []
    for track_yml in TRACKS.rglob("track.yml"):
        for assignment in sorted(track_yml.parent.glob("*-lab/assignment.md")):
            wid = workshop_id_from_path(assignment)
            if wid:
                out.append((assignment, wid))
    return out


def main() -> None:
    by_id = workshops_by_id()
    for path, wid in find_assignments():
        ws = by_id.get(wid)
        if not ws:
            print(f"  ? skip {path.relative_to(ROOT)} (no catalog entry for {wid})")
            continue
        if patch_simple_assignment(path, ws):
            print(f"  ✓ embedded slides in {path.relative_to(ROOT)}")
        else:
            print(f"  · unchanged {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
