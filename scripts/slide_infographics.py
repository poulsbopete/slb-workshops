"""Why-you-need-it infographic slides for SLB workshop decks."""

from __future__ import annotations

import html
from typing import TypedDict


class Feature(TypedDict):
    id: str
    title: str
    icon: str
    tagline: str
    without: str
    with_feature: str
    benefits: list[str]
    flow: list[str]


FEATURES: dict[str, Feature] = {
    "observability-serverless": {
        "id": "observability-serverless",
        "title": "Observability Serverless",
        "icon": "☁",
        "tagline": "Full observability without operating a cluster",
        "without": "You patch nodes, tune ILM, scale shards, and babysit upgrades — SRE time goes to the platform, not the product.",
        "with_feature": "Elastic runs ingestion, storage, scaling, and upgrades. Your team focuses on telemetry quality, alerts, and incident response.",
        "benefits": [
            "No Fleet agents, data tiers, or ILM policies to maintain",
            "Same Kibana UX — logs, metrics, traces, SLOs in one project",
            "Faster time-to-value for SLB teams migrating off Grafana-only stacks",
        ],
        "flow": ["OTel collectors", "Managed project", "Kibana ops"],
    },
    "elastic-streams": {
        "id": "elastic-streams",
        "title": "Elastic Streams",
        "icon": "⎇",
        "tagline": "Managed routing and processing for telemetry",
        "without": "Custom ingest pipelines, index templates, and rollover policies per team — fragile, hard to govern, and different on every cluster.",
        "with_feature": "Streams define how logs, metrics, and traces are routed, processed, and retained — natively on Serverless, with a single UI.",
        "benefits": [
            "Replace DIY pipeline + ILM work with declarative stream rules",
            "Consistent ownership and naming across SLB domains",
            "Easier troubleshooting when ingest volume or schema changes",
        ],
        "flow": ["Ingest", "Streams", "Search & alerts"],
    },
    "managed-otel": {
        "id": "managed-otel",
        "title": "Managed OTel ingestion",
        "icon": "📡",
        "tagline": "Send OTLP once — Elastic handles the rest",
        "without": "Multiple exporters, bespoke endpoints, and glue code to normalize Prometheus, Loki, and Jaeger into one query model.",
        "with_feature": "Point OpenTelemetry collectors at managed OTLP endpoints — unified logs, metrics, and traces in Observability Serverless.",
        "benefits": [
            "One semantic model (OTel) across services and hosts",
            "Side-by-side migration: Grafana today, Elastic Streams tomorrow",
            "Less custom integration code to maintain",
        ],
        "flow": ["OTel SDK", "Managed OTLP", "Unified store"],
    },
    "esql": {
        "id": "esql",
        "title": "ES|QL",
        "icon": "⌘",
        "tagline": "One query language for logs, metrics, and traces",
        "without": "Different syntax per signal — PromQL for metrics, LogQL for logs, trace UI only — context switching slows incidents.",
        "with_feature": "ES|QL pipes data through filters, stats, and joins across observability datasets in Logs Explorer and Dev Tools.",
        "benefits": [
            "Faster investigations with reusable query patterns",
            "Works the same on Serverless — no cluster URLs to manage",
            "AI Assistant can draft and explain ES|QL for your team",
        ],
        "flow": ["FROM logs-*", "STATS / WHERE", "Answer"],
    },
    "unified-observability": {
        "id": "unified-observability",
        "title": "Unified Observability",
        "icon": "◎",
        "tagline": "Logs, metrics, and traces in one place",
        "without": "Three tabs, three tools, manual correlation — \"which deploy caused this spike?\" takes too long.",
        "with_feature": "APM, Logs Explorer, and Metrics views link the same service context — pivot from error log to trace to CPU in clicks.",
        "benefits": [
            "Shorter MTTR when signals share service.name and trace.id",
            "Deploy validation: check all three pillars after a release",
            "One Observability overview for leadership and SRE review",
        ],
        "flow": ["Logs", "Metrics", "Traces"],
    },
    "ai-assistant": {
        "id": "ai-assistant",
        "title": "AI Assistant",
        "icon": "✦",
        "tagline": "Natural language over your live telemetry",
        "without": "Every investigator rebuilds the same ES|QL, scrolls dashboards, and writes runbook prose from scratch.",
        "with_feature": "Ask questions in plain language — get ES|QL, summaries, and correlated logs/traces grounded in your project data.",
        "benefits": [
            "Onboard new engineers without memorizing query syntax",
            "Explain spikes and error patterns during live incidents",
            "Draft queries you can save, share, and reuse",
        ],
        "flow": ["Question", "AI Assistant", "Evidence"],
    },
    "agent-builder": {
        "id": "agent-builder",
        "title": "Agent Builder",
        "icon": "🤖",
        "tagline": "Repeatable AI workflows with guardrails",
        "without": "Ad-hoc ChatGPT sessions with no access to SLB data, no audit trail, and inconsistent answers per engineer.",
        "with_feature": "Build agents that use observability context, tools, and retrieval — tuned prompts your team can trust and share.",
        "benefits": [
            "Standardize \"investigate service X\" and \"summarize deploy\" playbooks",
            "Connect tools (ES|QL, alerts, docs) instead of copy-paste context",
            "Govern who can publish agents — architecture-friendly AI ops",
        ],
        "flow": ["Agent", "Tools + data", "Action"],
    },
    "workflows": {
        "id": "workflows",
        "title": "Workflows",
        "icon": "⚡",
        "tagline": "Automate alert response safely",
        "without": "Manual Slack pings, ticket copy-paste, and runbook hunts — alerts fire but nothing moves until a human acts.",
        "with_feature": "Workflows chain connectors (Slack, PagerDuty, webhooks) with approval steps when alerts or SLOs breach.",
        "benefits": [
            "Notify the right channel with context automatically",
            "Add human-in-the-loop before remediation scripts run",
            "Reduce toil without bypassing change control",
        ],
        "flow": ["Alert", "Workflow", "Notify / act"],
    },
    "slos": {
        "id": "slos",
        "title": "SLOs",
        "icon": "◉",
        "tagline": "User-facing reliability, not just green dashboards",
        "without": "CPU graphs look fine while customers see errors — no shared error budget or burn-rate language with product teams.",
        "with_feature": "SLOs define availability/latency targets from real traces and metrics, with burn alerts before users flood support.",
        "benefits": [
            "Align SRE and product on measurable reliability",
            "Prioritize fixes when error budget is draining",
            "Works natively in Observability Serverless — no custom PromQL recording rules",
        ],
        "flow": ["SLI signal", "SLO target", "Burn alert"],
    },
    "alerts": {
        "id": "alerts",
        "title": "Observability Alerts",
        "icon": "🔔",
        "tagline": "Signal without the noise",
        "without": "Alert storms, duplicate pages, and rules that never get tuned — on-call learns to ignore the channel.",
        "with_feature": "Threshold, anomaly, and SLO-based rules with grouping, suppression, and AI-assisted triage in one alerts UI.",
        "benefits": [
            "Tune rules to SLB services instead of one-size-fits-all thresholds",
            "Deduplicate and acknowledge with context for handoffs",
            "Feed Workflows for automated first response",
        ],
        "flow": ["Rule", "Alert", "Triage"],
    },
    "dashboards-lens": {
        "id": "dashboards-lens",
        "title": "Dashboards & Lens",
        "icon": "▦",
        "tagline": "Grafana-style views, Elastic-native drilldowns",
        "without": "Static panels that break when fields change — no path from chart to raw events without switching tools.",
        "with_feature": "Lens builds visualizations drag-and-drop; dashboards link to Discover, APM, and ES|QL for drilldown.",
        "benefits": [
            "Familiar panel workflow for Grafana users",
            "Share operational and business review boards in one project",
            "Markdown KPI panels for runbook links and escalation info",
        ],
        "flow": ["Lens panel", "Dashboard", "Drilldown"],
    },
    "discover": {
        "id": "discover",
        "title": "Discover",
        "icon": "🔍",
        "tagline": "Explore raw telemetry before you visualize",
        "without": "Jump straight to dashboards and miss the field that explains the outage.",
        "with_feature": "Discover filters, sorts, and column-picks any index pattern — the fastest way to learn your schema.",
        "benefits": [
            "Entry point for BI and dev users new to Elastic",
            "Validate data quality before building Lens charts",
            "Export and save views for repeat investigations",
        ],
        "flow": ["Filter", "Columns", "Insight"],
    },
    "anomalies-ml": {
        "id": "anomalies-ml",
        "title": "Anomaly detection",
        "icon": "📈",
        "tagline": "Catch unknown-unknowns in telemetry",
        "without": "Static thresholds miss slow leaks and seasonal shifts — you only notice when customers complain.",
        "with_feature": "ML jobs and log anomalies learn normal behavior and flag deviations across metrics and log rates.",
        "benefits": [
            "Complement fixed thresholds for dynamic workloads",
            "Pair with AI Assistant to explain what changed",
            "Use when you do not yet know the right alert threshold",
        ],
        "flow": ["Baseline", "Anomaly", "Investigate"],
    },
    "rag-mcp": {
        "id": "rag-mcp",
        "title": "RAG & MCP",
        "icon": "🔗",
        "tagline": "Agents grounded in SLB knowledge and live data",
        "without": "LLMs hallucinate runbooks; engineers paste Confluence into chat every incident.",
        "with_feature": "Retrieval-augmented generation pulls from Elasticsearch indices; MCP exposes ES|QL, streams, and alerts as agent tools.",
        "benefits": [
            "Answers cite your docs and telemetry, not the open internet",
            "Standard tool interface for custom SLB integrations",
            "Build \"what changed?\" agents without bespoke glue code",
        ],
        "flow": ["Question", "Retrieve", "Tool call"],
    },
    "hybrid-search": {
        "id": "hybrid-search",
        "title": "Hybrid search",
        "icon": "⊕",
        "tagline": "Keyword precision plus semantic recall",
        "without": "Exact-match search misses reworded errors; vector-only search misses ticket IDs and hostnames.",
        "with_feature": "Combine BM25 keyword scoring with semantic similarity — find \"connection reset\" and paraphrased variants together.",
        "benefits": [
            "Better log and runbook search during incidents",
            "Tune relevance for SLB-specific vocabulary",
            "AI Assistant can leverage hybrid retrieval patterns",
        ],
        "flow": ["Keyword", "+ semantic", "Ranked hits"],
    },
    "api-keys-governance": {
        "id": "api-keys-governance",
        "title": "API keys & access",
        "icon": "🔐",
        "tagline": "Secure multi-team automation on Serverless",
        "without": "Shared credentials, over-privileged scripts, and no clear ownership per integration.",
        "with_feature": "Project-scoped API keys and role patterns replace cluster superuser — each team gets least privilege.",
        "benefits": [
            "Automate dashboards and CI checks without shared passwords",
            "Audit who can query vs who can configure Streams",
            "Architect-friendly boundary between teams on one project",
        ],
        "flow": ["Team", "API key", "Scoped access"],
    },
    "support": {
        "id": "support",
        "title": "Elastic support & enablement",
        "icon": "🛟",
        "tagline": "Faster answers when production is on the line",
        "without": "Vague tickets, missing project context, and unclear escalation — cases bounce and MTTR grows.",
        "with_feature": "Know your Elastic team, ticket template, and escalation path before day-two incidents hit Serverless.",
        "benefits": [
            "Include project type, time range, and ES|QL tried in every case",
            "Use this workshop program for role-based depth (SRE, Dev, BI, AIOps)",
            "Escalate with reproduction steps — not screenshots alone",
        ],
        "flow": ["Symptom", "Ticket", "Resolution"],
    },
}

# Features to show per workshop (order = slide order)
WORKSHOP_FEATURES: dict[str, list[str]] = {
    "f-01": ["support", "observability-serverless"],
    "f-02": [
        "observability-serverless",
        "elastic-streams",
        "esql",
        "unified-observability",
        "ai-assistant",
        "agent-builder",
    ],
    "f-03": ["esql", "elastic-streams", "managed-otel", "dashboards-lens", "ai-assistant"],
    "f-04": ["observability-serverless", "agent-builder", "workflows", "elastic-streams"],
    "dev-01": ["discover", "dashboards-lens", "unified-observability"],
    "dev-02": ["esql", "unified-observability", "ai-assistant"],
    "dev-03": ["unified-observability", "esql", "slos", "alerts"],
    "sre-01": ["observability-serverless", "managed-otel", "elastic-streams", "esql"],
    "sre-02": ["elastic-streams", "esql", "ai-assistant"],
    "sre-03": ["managed-otel", "elastic-streams", "esql", "ai-assistant"],
    "sre-04": ["slos", "alerts", "workflows", "elastic-streams", "ai-assistant"],
    "arch-01": ["observability-serverless", "managed-otel", "elastic-streams", "api-keys-governance"],
    "arch-02": ["elastic-streams", "api-keys-governance", "agent-builder"],
    "bi-01": ["discover", "dashboards-lens", "esql"],
    "bi-02": ["esql", "ai-assistant", "unified-observability"],
    "bi-03": ["dashboards-lens", "api-keys-governance", "esql"],
    "aiops-01": ["alerts", "slos", "ai-assistant"],
    "aiops-02": ["ai-assistant", "agent-builder", "unified-observability", "workflows"],
    "aiops-03": ["workflows", "alerts", "slos"],
    "oneoff-ai-ml": ["ai-assistant", "agent-builder", "anomalies-ml"],
    "oneoff-rag-mcp": ["rag-mcp", "agent-builder", "esql"],
    "oneoff-hybrid-search": ["hybrid-search", "esql", "ai-assistant"],
    "cross-team": [
        "observability-serverless",
        "elastic-streams",
        "esql",
        "slos",
        "ai-assistant",
        "workflows",
    ],
}


def _esc(text: str) -> str:
    return html.escape(text)


def render_flow(steps: list[str]) -> str:
    parts: list[str] = ['<div class="ig-flow">']
    for i, step in enumerate(steps):
        cls = "ig-step ig-highlight" if i == 1 and len(steps) == 3 else "ig-step"
        parts.append(f'<div class="{cls}">{_esc(step)}</div>')
        if i < len(steps) - 1:
            parts.append('<div class="ig-connector" aria-hidden="true"></div>')
    parts.append("</div>")
    return "".join(parts)


def render_feature_infographic(feature: Feature) -> str:
    benefits = "".join(f"<li>{_esc(b)}</li>" for b in feature["benefits"])
    return (
        f'<div class="infographic">'
        f'<div class="ig-header">'
        f'<span class="ig-icon" aria-hidden="true">{_esc(feature["icon"])}</span>'
        f'<p class="ig-tagline">{_esc(feature["tagline"])}</p>'
        f"</div>"
        f'<div class="ig-compare">'
        f'<div class="ig-card ig-problem">'
        f"<h3>Without it</h3><p>{_esc(feature['without'])}</p>"
        f"</div>"
        f'<div class="ig-card ig-solution">'
        f"<h3>With {_esc(feature['title'])}</h3>"
        f"<p>{_esc(feature['with_feature'])}</p>"
        f"</div>"
        f"</div>"
        f'<ul class="ig-benefits">{benefits}</ul>'
        f"{render_flow(feature['flow'])}"
        f"</div>"
    )


def render_features_overview(feature_ids: list[str]) -> str:
    cards: list[str] = ['<div class="ig-overview">']
    for fid in feature_ids:
        feat = FEATURES[fid]
        cards.append(
            f'<div class="ig-mini-card">'
            f'<span class="ig-mini-icon">{_esc(feat["icon"])}</span>'
            f'<strong>{_esc(feat["title"])}</strong>'
            f'<span>{_esc(feat["tagline"])}</span>'
            f"</div>"
        )
    cards.append("</div>")
    cards.append('<p class="ig-hint muted">Use → to see <strong>why</strong> each feature matters for SLB.</p>')
    return "".join(cards)


def infographic_slides(workshop_id: str) -> list[tuple[str, str]]:
    """Return (heading, html_body) slides for a workshop."""
    feature_ids = WORKSHOP_FEATURES.get(workshop_id, [])
    if not feature_ids:
        return []

    slides: list[tuple[str, str]] = [
        ("Why these features?", render_features_overview(feature_ids)),
    ]
    for fid in feature_ids:
        feat = FEATURES[fid]
        slides.append((f"Why {feat['title']}?", render_feature_infographic(feat)))
    return slides
