#!/usr/bin/env python3
"""Embed GitHub Pages slide iframes into Instruqt assignment.md notes."""

from __future__ import annotations

import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "catalog" / "workshops.yaml"
TRACKS = ROOT / "tracks"
PAGES_BASE = "https://poulsbopete.github.io/slb-workshops"


def slug_to_workshop() -> dict[str, dict]:
    with CATALOG.open() as f:
        data = yaml.safe_load(f)
    return {
        ws["instruqt_track"]: ws
        for ws in data["workshops"]
        if ws.get("instruqt_track")
    }


def iframe_note(workshop: dict) -> str:
    wid = workshop["id"]
    code = workshop["code"]
    url = f"{PAGES_BASE}/slides/{wid}/"
    return (
        f"## While you wait…\n\n"
        f"<iframe src=\"{url}\"\n"
        f"  width=\"100%\" height=\"800\" frameborder=\"0\"\n"
        f"  style=\"border-radius:8px;display:block\">\n"
        f"</iframe>\n\n"
        f"*Provisioning your Elastic **Observability Serverless** lab for **{code}** "
        f"(usually 2–3 minutes).*"
    )


def patch_assignment(path: Path, workshop: dict) -> bool:
    text = path.read_text()
    parts = text.split("---", 2)
    if len(parts) < 3:
        return False

    front = yaml.safe_load(parts[1])
    if not isinstance(front, dict):
        return False

    slide_contents = iframe_note(workshop)
    notes = front.get("notes") or []

    # Replace or prepend slide iframe note
    if notes and "iframe src=" in str(notes[0].get("contents", "")):
        notes[0]["contents"] = slide_contents
    else:
        notes.insert(0, {"type": "text", "contents": slide_contents})

    # Keep second note as provisioning topics if missing
    has_topics = any("Live session topics" in str(n.get("contents", "")) for n in notes[1:])
    if not has_topics and workshop.get("topics"):
        topic_lines = "\n".join(f"- {t}" for t in workshop["topics"])
        notes.append(
            {
                "type": "text",
                "contents": (
                    f"## Session topics\n\n{topic_lines}"
                ),
            }
        )

    front["notes"] = notes

    # Rebuild file — preserve body after second ---
    body = parts[2]
    dumped = yaml.dump(front, default_flow_style=False, sort_keys=False, allow_unicode=True)
    new_text = f"---\n{dumped}---{body}"
    if new_text == text:
        return False
    path.write_text(new_text)
    return True


def find_assignments() -> list[tuple[Path, str]]:
    out: list[tuple[Path, str]] = []
    for track_yml in TRACKS.rglob("track.yml"):
        slug = track_yml.parent.name
        if not slug.startswith("slb-"):
            continue
        for assignment in track_yml.parent.glob("*/assignment.md"):
            out.append((assignment, slug))
    return out


def main() -> None:
    mapping = slug_to_workshop()
    for path, slug in find_assignments():
        ws = mapping.get(slug)
        if not ws:
            print(f"  ? skip {path.relative_to(ROOT)} (no catalog entry)")
            continue
        if patch_assignment(path, ws):
            print(f"  ✓ embedded slides in {path.relative_to(ROOT)}")
        else:
            print(f"  · unchanged {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
