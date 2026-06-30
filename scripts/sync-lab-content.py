#!/usr/bin/env python3
"""Sync lab markdown bodies from generate-tracks LABS dict; remove Terminal tabs."""

from __future__ import annotations

import importlib.util
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
TRACKS = ROOT / "tracks"
CATALOG = ROOT / "catalog" / "workshops.yaml"

LAB_INTRO = """> **Elastic Observability Serverless** — use the **Elastic Serverless** tab only. These labs focus on **managed Serverless** capabilities (no ILM, Fleet, or self-managed tiers). Steps are copy/paste in Kibana — no terminal required.

"""

KEEP_TERMINAL_SLUGS: set[str] = set()


def load_labs() -> dict[str, str]:
    spec = importlib.util.spec_from_file_location(
        "generate_tracks", ROOT / "scripts" / "generate-tracks.py"
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.LABS


def workshop_id_from_path(path: Path) -> str | None:
    m = re.match(r"^\d+-(.+)-lab$", path.parent.name)
    return m.group(1) if m else None


def split_assignment(text: str) -> tuple[dict, str] | None:
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        return None
    front = yaml.safe_load(m.group(1))
    body = text[m.end() :]
    if not isinstance(front, dict):
        return None
    return front, body


def strip_terminal_tab(front: dict) -> bool:
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


def workshops_by_id() -> dict[str, dict]:
    with CATALOG.open() as f:
        data = yaml.safe_load(f)
    return {ws["id"]: ws for ws in data["workshops"]}


def session_topics_note(workshop: dict) -> str:
    lines = ["## Session topics", ""]
    for topic in workshop.get("topics", []):
        lines.append(f"- {topic}")
    lines.append("")
    return "\n".join(lines)


def topics_from_note(contents: str) -> list[str]:
    topics: list[str] = []
    for line in contents.splitlines():
        line = line.strip()
        if line.startswith("- "):
            topics.append(line[2:].strip())
    return topics


def update_session_topics(front: dict, workshop: dict) -> bool:
    expected_topics = list(workshop.get("topics", []))
    expected = session_topics_note(workshop)
    notes = front.get("notes") or []
    for i, note in enumerate(notes):
        contents = str(note.get("contents", ""))
        if "## Session topics" in contents or "Live session topics" in contents:
            if topics_from_note(contents) == expected_topics:
                return False
            notes[i]["contents"] = expected
            front["notes"] = notes
            return True
    notes.append({"type": "text", "contents": expected})
    front["notes"] = notes
    return True


def patch_assignment(
    path: Path, workshop_id: str, workshop: dict, labs: dict[str, str]
) -> bool:
    text = path.read_text()
    split = split_assignment(text)
    if not split:
        return False
    front, old_body = split
    changed = False
    new_body = old_body

    if workshop_id in labs:
        new_body = LAB_INTRO + labs[workshop_id].strip() + "\n"
        if new_body != old_body:
            changed = True

    expected_title = f"{workshop['code']} — {workshop['title']}"
    if front.get("title") != expected_title:
        front["title"] = expected_title
        changed = True
    teaser = workshop.get("description", "").strip().replace("\n", " ")[:200]
    if front.get("teaser") != teaser:
        front["teaser"] = teaser
        changed = True

    if strip_terminal_tab(front):
        changed = True
    if dedupe_notes(front):
        changed = True
    if update_session_topics(front, workshop):
        changed = True

    if not changed:
        return False

    dumped = yaml.dump(front, default_flow_style=False, sort_keys=False, allow_unicode=True)
    path.write_text(f"---\n{dumped.rstrip()}\n---\n{new_body.lstrip()}")
    return True


def main() -> None:
    labs = load_labs()
    by_id = workshops_by_id()
    for track_yml in sorted(TRACKS.rglob("track.yml")):
        for assignment in sorted(track_yml.parent.glob("*-lab/assignment.md")):
            wid = workshop_id_from_path(assignment)
            if not wid or wid not in by_id:
                continue
            if patch_assignment(assignment, wid, by_id[wid], labs):
                print(f"  ✓ {assignment.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
