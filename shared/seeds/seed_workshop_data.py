#!/usr/bin/env python3
"""Seed SLB workshop sample observability data into Elastic Serverless."""

from __future__ import annotations

import json
import os
import random
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone

SERVICES = [
    ("checkout-api", 0.22, "payment"),
    ("billing-service", 0.08, "billing"),
    ("inventory-worker", 0.05, "inventory"),
    ("auth-gateway", 0.12, "auth"),
    ("seismic-ingest", 0.15, "ingest"),
]

HOSTS = [
    "slb-host-ams-01",
    "slb-host-ams-02",
    "slb-host-hou-01",
    "slb-host-hou-02",
]

ERROR_MESSAGES = [
    "Connection timeout to upstream payment provider",
    "HTTP 503 from dependency billing-service",
    "OOM killed container (exit 137)",
    "Database connection pool exhausted",
    "TLS handshake failed with auth-gateway",
    "Rate limit exceeded for API key",
    "Invalid JWT signature on request",
    "Kafka consumer lag exceeded threshold",
]

INFO_MESSAGES = [
    "Request completed successfully",
    "Health check passed",
    "Cache warmed for region us-east",
    "Batch job finished",
    "User session established",
]


def env(name: str, default: str = "") -> str:
    return os.environ.get(name, default).strip()


def auth_header() -> str:
    api_key = env("ES_API_KEY") or env("ELASTIC_API_KEY")
    if api_key:
        return f"ApiKey {api_key}"
    user = env("ES_USERNAME", "admin")
    password = env("ES_PASSWORD")
    if password:
        import base64

        token = base64.b64encode(f"{user}:{password}".encode()).decode()
        return f"Basic {token}"
    raise RuntimeError("No ES_API_KEY or ES_PASSWORD available for seeding")


def request(
    method: str,
    url: str,
    body: bytes | None = None,
    headers: dict[str, str] | None = None,
    timeout: int = 120,
) -> tuple[int, str]:
    hdrs = {"Authorization": auth_header()}
    if headers:
        hdrs.update(headers)
    req = urllib.request.Request(url, data=body, headers=hdrs, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as exc:
        return exc.code, exc.read().decode("utf-8", errors="replace")


def wait_for_es(es_url: str, attempts: int = 40) -> None:
    for i in range(attempts):
        code, _ = request("GET", f"{es_url.rstrip('/')}/_cluster/health")
        if code == 200:
            print("  ✓ Elasticsearch ready")
            return
        time.sleep(3)
        if i % 5 == 0:
            print(f"  … waiting for Elasticsearch ({i + 1}/{attempts})")
    raise RuntimeError("Elasticsearch not ready for seeding")


def bulk_ndjson(es_url: str, lines: list[str], label: str) -> int:
    if not lines:
        return 0
    payload = "\n".join(lines) + "\n"
    code, body = request(
        "POST",
        f"{es_url.rstrip('/')}/_bulk",
        body=payload.encode("utf-8"),
        headers={"Content-Type": "application/x-ndjson"},
    )
    if code not in (200, 201):
        raise RuntimeError(f"Bulk {label} failed HTTP {code}: {body[:500]}")
    result = json.loads(body)
    if result.get("errors"):
        first = next(
            (item for item in result.get("items", []) if "error" in str(item)),
            None,
        )
        raise RuntimeError(f"Bulk {label} had errors: {first}")
    count = len(lines) // 2
    print(f"  ✓ Indexed {count} {label} documents")
    return count


def ensure_data_streams(es_url: str) -> None:
    streams = [
        "logs-slb.workshop-default",
        "metrics-system.cpu-default",
        "traces-apm-default",
    ]
    for stream in streams:
        code, body = request("PUT", f"{es_url.rstrip('/')}/_data_stream/{stream}")
        if code in (200, 201):
            print(f"  ✓ Data stream {stream}")
        else:
            print(f"  · Data stream {stream} HTTP {code} (may auto-create on bulk)")


def seed_logs(es_url: str, hours: int = 6) -> int:
    now = datetime.now(timezone.utc)
    lines: list[str] = []
    random.seed(42)
    for minute in range(hours * 60):
        ts = now - timedelta(minutes=minute)
        ts_str = ts.strftime("%Y-%m-%dT%H:%M:%S.000Z")
        volume = 4 + (minute % 7)
        for _ in range(volume):
            service, err_rate, domain = random.choice(SERVICES)
            host = random.choice(HOSTS)
            is_error = random.random() < err_rate
            doc = {
                "@timestamp": ts_str,
                "message": random.choice(ERROR_MESSAGES if is_error else INFO_MESSAGES),
                "log": {"level": "error" if is_error else "info"},
                "service": {
                    "name": service,
                    "environment": "production",
                    "version": "2.4.1",
                },
                "host": {"name": host},
                "labels": {"workshop": "slb", "domain": domain},
                "data_stream": {
                    "type": "logs",
                    "dataset": "slb.workshop",
                    "namespace": "default",
                },
            }
            if is_error:
                doc["error"] = {"type": "ServiceException"}
            lines.append(json.dumps({"create": {"_index": "logs-slb.workshop-default"}}))
            lines.append(json.dumps(doc))
        if len(lines) >= 2000:
            bulk_ndjson(es_url, lines, "log batch")
            lines = []
    if lines:
        bulk_ndjson(es_url, lines, "log batch")
    return hours * 60 * 5


def seed_apm_transactions(es_url: str, hours: int = 3) -> int:
    """Classic APM transaction docs so AI Assistant / APM views have error rates."""
    now = datetime.now(timezone.utc)
    lines: list[str] = []
    random.seed(99)
    for minute in range(hours * 60):
        ts = (now - timedelta(minutes=minute)).strftime("%Y-%m-%dT%H:%M:%S.000Z")
        for service, err_rate, _ in SERVICES:
            for _ in range(3 + int(err_rate * 10)):
                failed = random.random() < err_rate
                duration_us = random.randint(80_000, 2_500_000)
                doc = {
                    "@timestamp": ts,
                    "processor": {"event": "transaction", "name": "transaction"},
                    "service": {
                        "name": service,
                        "environment": "production",
                        "language": {"name": "java"},
                    },
                    "host": {"name": random.choice(HOSTS)},
                    "transaction": {
                        "id": f"{service}-{minute}-{random.randint(1000, 9999)}",
                        "type": "request",
                        "duration": {"us": duration_us},
                        "result": "failure" if failed else "success",
                        "sampled": True,
                    },
                    "event": {"outcome": "failure" if failed else "success"},
                    "data_stream": {
                        "type": "traces",
                        "dataset": "apm",
                        "namespace": "default",
                    },
                }
                lines.append(
                    json.dumps({"create": {"_index": "traces-apm-default"}})
                )
                lines.append(json.dumps(doc))
        if len(lines) >= 2000:
            bulk_ndjson(es_url, lines, "APM transaction batch")
            lines = []
    if lines:
        bulk_ndjson(es_url, lines, "APM transaction batch")
    return hours * 60 * len(SERVICES) * 5


def seed_metrics(es_url: str, hours: int = 3) -> int:
    now = datetime.now(timezone.utc)
    lines: list[str] = []
    random.seed(7)
    for minute in range(hours * 60):
        ts = (now - timedelta(minutes=minute)).strftime("%Y-%m-%dT%H:%M:%S.000Z")
        for host in HOSTS:
            cpu = round(random.uniform(0.15, 0.92), 3)
            doc = {
                "@timestamp": ts,
                "metricset": {"name": "cpu"},
                "host": {"name": host},
                "system": {"cpu": {"total": {"pct": cpu}}},
                "data_stream": {
                    "type": "metrics",
                    "dataset": "system.cpu",
                    "namespace": "default",
                },
            }
            lines.append(
                json.dumps({"create": {"_index": "metrics-system.cpu-default"}})
            )
            lines.append(json.dumps(doc))
        if len(lines) >= 2000:
            bulk_ndjson(es_url, lines, "metric batch")
            lines = []
    if lines:
        bulk_ndjson(es_url, lines, "metric batch")
    return hours * 60 * len(HOSTS)


def seed_otlp(otlp_base: str) -> None:
    if not otlp_base:
        print("  · OTLP endpoint not set — skipping OTLP spans")
        return
    try:
        from opentelemetry import trace
        from opentelemetry.exporter.otlp.proto.http.trace_exporter import (
            OTLPSpanExporter,
        )
        from opentelemetry.sdk.resources import Resource
        from opentelemetry.sdk.trace import TracerProvider
        from opentelemetry.sdk.trace.export import BatchSpanProcessor
        from opentelemetry.trace import Status, StatusCode
    except ImportError as exc:
        print(f"  · OTLP packages missing ({exc}) — APM bulk docs still seeded")
        return

    auth = auth_header()
    exporter = OTLPSpanExporter(
        endpoint=f"{otlp_base.rstrip('/')}/v1/traces",
        headers={"Authorization": auth},
    )
    for service, err_rate, _ in SERVICES:
        resource = Resource.create(
            {
                "service.name": service,
                "service.version": "2.4.1",
                "deployment.environment": "production",
                "data_stream.dataset": "slb.workshop",
                "data_stream.namespace": "default",
            }
        )
        provider = TracerProvider(resource=resource)
        provider.add_span_processor(BatchSpanProcessor(exporter))
        trace.set_tracer_provider(provider)
        tracer = trace.get_tracer("slb-workshop-seed")
        for i in range(30):
            failed = i % max(1, int(1 / max(err_rate, 0.05))) == 0
            with tracer.start_as_current_span(
                "process_request",
                attributes={"http.route": "/api/v1/process"},
            ) as span:
                if failed:
                    span.set_status(Status(StatusCode.ERROR, "timeout"))
        provider.shutdown()
    print("  ✓ Exported OTLP traces for all services")


def kibana_request(path: str, payload: dict | None = None) -> tuple[int, str]:
    kibana = env("KIBANA_URL")
    if not kibana:
        return 0, "KIBANA_URL not set"
    body = None if payload is None else json.dumps(payload).encode("utf-8")
    headers = {"kbn-xsrf": "slb-workshop", "Content-Type": "application/json"}
    return request(
        "POST" if payload else "GET",
        f"{kibana.rstrip('/')}{path}",
        body=body,
        headers=headers,
    )


def seed_kibana_assets() -> None:
    kibana = env("KIBANA_URL")
    if not kibana:
        print("  · KIBANA_URL not set — skipping Kibana assets")
        return

    # Data view for workshop logs
    dv_payload = {
        "data_view": {
            "title": "logs-slb.workshop-default,logs-*",
            "name": "SLB Workshop Logs",
            "timeFieldName": "@timestamp",
        }
    }
    code, body = kibana_request("/api/data_views/data_view", dv_payload)
    if code in (200, 201):
        print("  ✓ Created SLB Workshop Logs data view")
    else:
        print(f"  · Data view create HTTP {code} (may already exist)")

    # Alert rule: checkout-api errors (for AIOps labs)
    rule = {
        "name": "SLB Workshop — checkout-api errors",
        "tags": ["slb", "workshop"],
        "rule_type_id": ".es-query",
        "consumer": "alerts",
        "schedule": {"interval": "5m"},
        "actions": [],
        "params": {
            "size": 100,
            "timeWindowSize": 30,
            "timeWindowUnit": "m",
            "threshold": [1],
            "thresholdComparator": ">",
            "searchType": "esqlQuery",
            "esqlQuery": (
                "FROM logs-* | WHERE service.name == \"checkout-api\" "
                "AND log.level == \"error\" | STATS error_count = COUNT(*)"
            ),
            "timeField": "@timestamp",
        },
    }
    code, body = kibana_request("/api/alerting/rule", rule)
    if code in (200, 201):
        print("  ✓ Created sample alert rule (checkout-api errors)")
    else:
        print(f"  · Alert rule HTTP {code}: {body[:300]}")

    # SLO-style rule for billing-service latency context
    slo_rule = {
        "name": "SLB Workshop — billing-service error budget",
        "tags": ["slb", "workshop", "slo"],
        "rule_type_id": ".es-query",
        "consumer": "alerts",
        "schedule": {"interval": "10m"},
        "actions": [],
        "params": {
            "size": 100,
            "timeWindowSize": 1,
            "timeWindowUnit": "h",
            "threshold": [5],
            "thresholdComparator": ">",
            "searchType": "esqlQuery",
            "esqlQuery": (
                "FROM logs-* | WHERE service.name == \"billing-service\" "
                "AND log.level == \"error\" | STATS errors = COUNT(*)"
            ),
            "timeField": "@timestamp",
        },
    }
    code, _ = kibana_request("/api/alerting/rule", slo_rule)
    if code in (200, 201):
        print("  ✓ Created sample alert rule (billing-service errors)")


def verify(es_url: str) -> None:
    for pattern in ("logs-*", "traces-*", "metrics-*"):
        code, body = request("GET", f"{es_url.rstrip('/')}/{pattern}/_count")
        if code == 200:
            count = json.loads(body).get("count", 0)
            print(f"  ✓ {pattern}: {count} documents")
        else:
            print(f"  · {pattern}: count unavailable (HTTP {code})")


def main() -> int:
    es_url = env("ES_URL")
    if not es_url:
        print("ERROR: ES_URL not set", file=sys.stderr)
        return 1

    print("=== SLB Workshop — seeding sample observability data ===")
    wait_for_es(es_url)
    ensure_data_streams(es_url)
    seed_logs(es_url)
    seed_apm_transactions(es_url)
    seed_metrics(es_url)
    otlp = env("WORKSHOP_OTLP_ENDPOINT") or env("WORKSHOP_OTLP_BASE")
    seed_otlp(otlp)
    time.sleep(3)
    seed_kibana_assets()
    time.sleep(2)
    print("=== Verification ===")
    verify(es_url)
    print("=== SLB Workshop seed complete ===")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
