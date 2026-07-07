#!/usr/bin/env python3
"""Sync check-es3-api scripts from generate-tracks template."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRACKS = ROOT / "tracks"
SCRIPTS = ROOT / "scripts"


def load_check_script() -> str:
    spec = importlib.util.spec_from_file_location(
        "generate_tracks", SCRIPTS / "generate-tracks.py"
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.CHECK_CHALLENGE


def main() -> None:
    content = load_check_script()
    updated = 0
    for path in sorted(TRACKS.rglob("check-es3-api")):
        if path.read_text() != content:
            path.write_text(content)
            path.chmod(0o755)
            updated += 1
            print(f"  ✓ {path.relative_to(ROOT)}")
    if not updated:
        print("  · all check-es3-api scripts up to date")


if __name__ == "__main__":
    main()
