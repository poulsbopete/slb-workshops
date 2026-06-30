"""Public URL for slide decks (GitHub Pages, Vercel, or custom domain)."""

from __future__ import annotations

import os

# Override at build/deploy time: SLIDES_BASE_URL=https://your-domain.com
DEFAULT_SLIDES_BASE = "https://slb-workshops.vercel.app"


def slides_base() -> str:
    return os.environ.get("SLIDES_BASE_URL", DEFAULT_SLIDES_BASE).rstrip("/")


def slide_deck_url(workshop_id: str) -> str:
    return f"{slides_base()}/slides/{workshop_id}/"
