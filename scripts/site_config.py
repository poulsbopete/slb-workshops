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


def waiting_room_note(workshop_id: str) -> str:
    """Short provisioning note — slides live in the Session slides tab (full-width)."""
    return (
        "## While you wait…\n\n"
        "Open the **Session slides** tab for today's deck while your "
        "Observability Serverless project provisions (~2–3 minutes).\n\n"
        "When provisioning finishes, switch to **Elastic Serverless** for the hands-on lab."
    )


def slides_tab_yaml(workshop_id: str) -> dict:
    return {
        "title": "Session slides",
        "type": "website",
        "url": slide_deck_url(workshop_id),
    }


def kibana_tab_dict() -> dict:
    return {
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


# Back-compat alias used by older scripts during transition
def iframe_note(workshop_id: str, *, height: int = IFRAME_HEIGHT) -> str:
    return waiting_room_note(workshop_id)
