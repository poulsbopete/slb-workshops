"""Public URL for slide decks (GitHub Pages, Vercel, or custom domain)."""

from __future__ import annotations

import os

# Override at build/deploy time: SLIDES_BASE_URL=https://your-domain.com
DEFAULT_SLIDES_BASE = "https://slb-workshops.vercel.app"


def slides_base() -> str:
    return os.environ.get("SLIDES_BASE_URL", DEFAULT_SLIDES_BASE).rstrip("/")


def slide_deck_url(workshop_id: str) -> str:
    return f"{slides_base()}/slides/{workshop_id}/"


IFRAME_HEIGHT = 1400


def iframe_note(workshop_id: str, *, height: int = IFRAME_HEIGHT) -> str:
    """Instruqt waiting-room note: slide deck iframe (no session topic bullets)."""
    url = slide_deck_url(workshop_id)
    return (
        "## While you wait…\n\n"
        '<div style="width:100%;max-width:100%;margin:0;padding:0;">\n'
        f'<iframe src="{url}" width="100%" height="{height}" frameborder="0" '
        f'style="display:block;width:100%;min-width:100%;height:{height}px;'
        f'border:0;border-radius:8px"></iframe>\n'
        "</div>"
    )
