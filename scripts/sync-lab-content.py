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

from site_config import kibana_tab_dict, slide_deck_url, slides_tab_yaml, waiting_room_note

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


def update_waiting_room_note(front: dict, workshop_id: str) -> bool:
    expected = waiting_room_note(workshop_id)
    notes = front.get("notes") or []
    contents = str(notes[0].get("contents", "")) if notes else ""
    needs_update = (
        len(notes) != 1
        or "## Session topics" in contents
        or "iframe src=" in contents
        or "Provisioning your" in contents
        or notes[0].get("contents") != expected
    )
    if not needs_update:
        return False
    front["notes"] = [{"type": "text", "contents": expected}]
    return True


def ensure_slides_tab(front: dict, workshop_id: str) -> bool:
    tabs = front.get("tabs") or []
    expected_url = slide_deck_url(workshop_id)
    slides_tabs = [t for t in tabs if t.get("type") == "website"]
    kibana_tabs = [t for t in tabs if t.get("type") == "service" and t.get("hostname") == "es3-api"]
    other_tabs = [
        t
        for t in tabs
        if t not in slides_tabs and t not in kibana_tabs
    ]

    slides = slides_tab_yaml(workshop_id)
    if slides_tabs and slides_tabs[0].get("url") == expected_url and slides_tabs[0].get("title") == "Session slides":
        new_slides = slides_tabs[0]
        changed = False
    else:
        new_slides = slides
        changed = True

    if not kibana_tabs:
        kibana_tabs = [kibana_tab_dict()]
        changed = True
    else:
        # Preserve Instruqt tab id and headers from existing kibana tab
        merged = kibana_tab_dict()
        merged.update({k: v for k, v in kibana_tabs[0].items() if k in ("id",)})
        kibana_tabs = [merged]

    new_tabs = [new_slides, kibana_tabs[0], *other_tabs]
    if new_tabs != tabs:
        front["tabs"] = new_tabs
        return True
    return changed


def dedupe_notes(front: dict) -> bool:
    notes = front.get("notes") or []
    if len(notes) <= 1:
        return False
    front["notes"] = [notes[0]]
    return True


def format_waiting_notes_yaml(workshop_id: str) -> str:
    note = waiting_room_note(workshop_id)
    indented = "\n".join(f"    {line}" for line in note.splitlines())
    return f"notes:\n- type: text\n  contents: |-\n{indented}\n"


def format_tabs_yaml(front: dict, workshop_id: str) -> str:
    ensure_slides_tab(front, workshop_id)
    lines = ["tabs:"]
    for tab in front.get("tabs") or []:
        dumped = yaml.dump(
            [tab], default_flow_style=False, sort_keys=False, allow_unicode=True
        ).rstrip()
        lines.extend(f"  {line}" for line in dumped.splitlines())
    return "\n".join(lines) + "\n"


def yaml_dump_front(front: dict, workshop_id: str) -> str:
    """Dump front matter with waiting-room text and website slides tab."""
    copy = dict(front)
    copy.pop("notes", None)
    copy.pop("tabs", None)
    ensure_slides_tab(front, workshop_id)
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
    parts.append(format_waiting_notes_yaml(workshop_id))
    parts.append(format_tabs_yaml(front, workshop_id))
    tail_keys = ["difficulty", "timelimit", "enhanced_loading"]
    tail: dict = {}
    for key in tail_keys:
        if key in copy:
            tail[key] = copy.pop(key)
    if tail:
        parts.append(
            yaml.dump(tail, default_flow_style=False, sort_keys=False, allow_unicode=True)
        )
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
    needs_layout_refresh = (
        "iframe src=" in front_matter
        or "type: website" not in front_matter
        or "Session slides" not in front_matter
        or "## Session topics" in front_matter
        or "Provisioning your" in front_matter
        or notes_after_tabs
    )
    if needs_layout_refresh:
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
    if update_waiting_room_note(front, workshop_id):
        changed = True
    if ensure_slides_tab(front, workshop_id):
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
