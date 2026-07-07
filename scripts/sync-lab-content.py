#!/usr/bin/env python3
"""Sync lab markdown bodies from generate-tracks LABS dict; remove Terminal tabs."""

from __future__ import annotations

import importlib.util
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))
TRACKS = ROOT / "tracks"
CATALOG = ROOT / "catalog" / "workshops.yaml"

from site_config import iframe_note

LAB_INTRO = """> **Lab environment:** Use the **Elastic Serverless** tab only. Hands-on steps run on **Observability Serverless** with **pre-loaded SLB sample data** (logs, metrics, traces, alert rules, and an SLO). The **same observability capabilities** apply on **ECH** and **self-managed**; Serverless mainly saves platform management. Steps are copy/paste in Kibana — no terminal required.

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


def strip_session_topic_notes(front: dict) -> bool:
    notes = front.get("notes") or []
    filtered = [
        n
        for n in notes
        if "## Session topics" not in str(n.get("contents", ""))
        and "Live session topics" not in str(n.get("contents", ""))
    ]
    if len(filtered) == len(notes):
        return False
    front["notes"] = filtered
    return True


def update_iframe_note(front: dict, workshop_id: str) -> bool:
    expected = iframe_note(workshop_id)
    notes = front.get("notes") or []
    contents = str(notes[0].get("contents", "")) if notes else ""
    needs_update = (
        len(notes) != 1
        or "## Session topics" in contents
        or "## While you wait" in contents
        or "Provisioning your" in contents
        or contents.startswith('"')
        or notes[0].get("contents") != expected
    )
    if not needs_update:
        return False
    front["notes"] = [{"type": "text", "contents": expected}]
    return True


def dedupe_notes(front: dict) -> bool:
    notes = front.get("notes") or []
    if len(notes) <= 1:
        return False
    first_has_iframe = "iframe src=" in str(notes[0].get("contents", ""))
    if not first_has_iframe:
        return False
    front["notes"] = [notes[0]]
    return True


def format_iframe_notes_yaml(workshop_id: str) -> str:
    iframe = iframe_note(workshop_id)
    indented = "\n".join(f"    {line}" for line in iframe.splitlines())
    return f"notes:\n- type: text\n  contents: |-\n{indented}\n"


def yaml_dump_front(front: dict, workshop_id: str) -> str:
    """Dump front matter with notes (iframe only) before tabs."""
    copy = dict(front)
    copy.pop("notes", None)
    head_keys = ["slug", "id", "type", "title", "teaser"]
    parts: list[str] = []
    for key in head_keys:
        if key in copy:
            parts.append(
                yaml.dump(
                    {key: copy.pop(key)},
                    default_flow_style=False,
                    sort_keys=False,
                    allow_unicode=True,
                )
            )
    parts.append(format_iframe_notes_yaml(workshop_id))
    if copy:
        parts.append(
            yaml.dump(copy, default_flow_style=False, sort_keys=False, allow_unicode=True)
        )
    return "".join(parts).rstrip()


def workshops_by_id() -> dict[str, dict]:
    with CATALOG.open() as f:
        data = yaml.safe_load(f)
    return {ws["id"]: ws for ws in data["workshops"]}


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

    front_matter = text.split("---", 2)[1]
    notes_after_tabs = "tabs:" in front_matter and front_matter.find("notes:") > front_matter.find("tabs:")
    if "contents: |-" not in front_matter or notes_after_tabs:
        update_iframe_note(front, workshop_id)
        changed = True

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
    if strip_session_topic_notes(front):
        changed = True
    if dedupe_notes(front):
        changed = True
    if update_iframe_note(front, workshop_id):
        changed = True

    if not changed:
        return False

    dumped = yaml_dump_front(front, workshop_id)
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
