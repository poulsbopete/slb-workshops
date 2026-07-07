#!/usr/bin/env python3
"""Sync lab markdown bodies from generate-tracks LABS dict; remove Terminal tabs."""

from __future__ import annotations

import importlib.util
import json
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

from site_config import iframe_note, iframe_note_yaml, slide_deck_url

LAB_INTRO = """> **Lab environment:** Use the **Elastic Serverless** tab only. Hands-on steps run on **Observability Serverless** with **pre-loaded SLB sample data** (logs, metrics, traces, alert rules, and an SLO). The **same observability capabilities** apply on **ECH** and **self-managed**; Serverless mainly saves platform management. Steps are copy/paste in Kibana — no terminal required.

"""

KEEP_TERMINAL_SLUGS: set[str] = set()

KIBANA_TAB_TEMPLATE = {
    "title": "Elastic Serverless",
    "type": "service",
    "hostname": "es3-api",
    "path": "/app/home",
    "port": 8080,
    "custom_request_headers": [
        {
            "key": "Content-Security-Policy",
            "value": (
                "script-src 'self' https://kibana.estccdn.com; worker-src blob: 'self'; "
                "style-src 'unsafe-inline' 'self' https://kibana.estccdn.com"
            ),
        }
    ],
    "custom_response_headers": [
        {
            "key": "Content-Security-Policy",
            "value": (
                "script-src 'self' https://kibana.estccdn.com; worker-src blob: 'self'; "
                "style-src 'unsafe-inline' 'self' https://kibana.estccdn.com"
            ),
        }
    ],
}


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
        and "Session slides" not in str(n.get("contents", ""))
    ]
    if len(filtered) == len(notes):
        return False
    front["notes"] = filtered
    return True


def ensure_kibana_tab_only(front: dict) -> bool:
    tabs = front.get("tabs") or []
    kibana = [t for t in tabs if t.get("type") == "service" and t.get("hostname") == "es3-api"]
    if not kibana:
        kibana = [dict(KIBANA_TAB_TEMPLATE)]
        changed = True
    else:
        merged = dict(KIBANA_TAB_TEMPLATE)
        if kibana[0].get("id"):
            merged["id"] = kibana[0]["id"]
        kibana = [merged]
        changed = tabs != kibana
    if tabs != kibana:
        front["tabs"] = kibana
        return True
    return changed


def update_iframe_note(front: dict, workshop_id: str, code: str) -> bool:
    expected = iframe_note(workshop_id, code)
    notes = front.get("notes") or []
    if len(notes) == 1 and notes[0].get("contents") == expected:
        return False
    front["notes"] = [{"type": "text", "contents": expected}]
    return True


def yaml_dump_front(front: dict, workshop_id: str, code: str) -> str:
    copy = dict(front)
    copy.pop("notes", None)
    ensure_kibana_tab_only(front)
    copy.pop("tabs", None)
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
    parts.append(iframe_note_yaml(workshop_id, code))
    tabs_yaml = yaml.dump(
        front.get("tabs") or [],
        default_flow_style=False,
        sort_keys=False,
        allow_unicode=True,
    ).rstrip()
    parts.append("tabs:\n" + "\n".join(f"  {line}" for line in tabs_yaml.splitlines()) + "\n")
    tail_keys = ["difficulty", "timelimit", "enhanced_loading"]
    tail = {k: copy.pop(k) for k in tail_keys if k in copy}
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
    code = workshop["code"]
    expected_url = slide_deck_url(workshop_id)

    if workshop_id in labs:
        new_body = LAB_INTRO + labs[workshop_id].strip() + "\n"
        if new_body != old_body:
            changed = True

    expected_title = f"{code} — {workshop['title']}"
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
    if ensure_kibana_tab_only(front):
        changed = True
    if update_iframe_note(front, workshop_id, code):
        changed = True

    # Force refresh if website tab or missing iframe URL in notes
    front_matter = text.split("---", 2)[1]
    if "type: website" in front_matter or expected_url not in front_matter:
        update_iframe_note(front, workshop_id, code)
        ensure_kibana_tab_only(front)
        changed = True

    if not changed:
        return False

    dumped = yaml_dump_front(front, workshop_id, code)
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
