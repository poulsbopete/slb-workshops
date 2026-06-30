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
    """Patch standard lab assignments via YAML (safe for simple front matter)."""
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
    new_text = f"---\n{dumped}---{body}"
    if new_text == text:
        return False
    path.write_text(new_text)
    return True


def patch_db_monitoring(path: Path, workshop: dict) -> bool:
    """Regex patch for complex assignment with many notes (avoid full YAML rewrite)."""
    text = path.read_text()
    url = f"{PAGES_BASE}/slides/{workshop['id']}/"
    new_iframe = (
        f'contents: "## While you wait…\\n\\n<iframe src=\\"{url}\\"\\n'
        f'  width=\\"100%\\" height=\\"800\\" frameborder=\\"0\\"\\n'
        f'  style=\\"border-radius:8px;display:block\\">\\n</iframe>\\n\\n'
        f'*Your Elastic environment and database telemetry are generating in the background.*\\n"'
    )
    new_text, n = re.subn(
        r'contents: "## While you wait…[^"]*"',
        new_iframe,
        text,
        count=1,
    )
    if n and new_text != text:
        path.write_text(new_text)
        return True
    return False


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
        if slug == "slb-workshops":
            ok = patch_db_monitoring(path, ws)
        else:
            ok = patch_simple_assignment(path, ws)
        if ok:
            print(f"  ✓ embedded slides in {path.relative_to(ROOT)}")
        else:
            print(f"  · unchanged {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
