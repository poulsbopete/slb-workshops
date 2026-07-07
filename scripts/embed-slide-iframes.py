#!/usr/bin/env python3
"""Sync Session slides website tabs into Instruqt assignment.md files."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main() -> None:
    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "sync-lab-content.py")],
        check=True,
    )


if __name__ == "__main__":
    main()
