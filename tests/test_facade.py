"""The resource facade, the transport under it, and webhook verification.

All against `respx`, so nothing touches the network.
"""

from __future__ import annotations

import base64
import hashlib
import hmac
import json
import pathlib
import tomllib
from typing import Any

import httpx
import pytest
import respx

import sendandretain
from sendandretain import (
    AsyncSendAndRetain,
    NotFoundError,
    PermissionDeniedError,
    QuotaExceededError,
    SendAndRetain,
    WebhookVerificationError,
    verify_webhook,
)

KEY = "aem_test_key"
BASE = "https://sendandretain.com"
REPO = pathlib.Path(__file__).resolve().parent.parent


def client(**kwargs: Any) -> SendAndRetain:
    return SendAndRetain(KEY, **kwargs)


# ── construction ────────────────────────────────────────────────────────────


def test_reads_the_key_from_the_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("SENDANDRETAIN_API_KEY", KEY)
    assert SendAndRetain().raw.token == KEY


def test_refuses_a_missing_or_foreign_key(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("SENDANDRETAIN_API_KEY", raising=False)
    with pytest.raises(ValueError, match="SENDANDRETAIN_API_KEY"):
        SendAndRetain()
    with pytest.raises(ValueError, match="aem_"):
        SendAndRetain("sk_live_wrong")


def test_version_matches_pyproject() -> None:
    pyproject = tomllib.loads((REPO / "pyproject.toml").read_text())
    assert sendandretain.__version__ == pyproject["project"]["version"]


# ── requests ────────────────────────────────────────────────────────────────


@respx.mock
def test_send_builds_the_request_and_returns_the_model() -> None:
    route = respx.post(f"{BASE}/api/v1/emails").mock(
        return_value=httpx.Response(202, json={"id": "msg_1", "status": "queued"})
    )
    email = client().emails.send(
        to="jane@acme.com", template="welcome", props={"firstName": "Jane"}, from_="Acme <hi@acme.com>"
    )
    assert email.id == "msg_1"

    request = route.calls.last.request
    assert request.headers["authorization"] == f"Bearer {KEY}"
    assert request.headers["user-agent"] == f"sendandretain-python:{sendandretain.__version__}"
    body = json.loads(request.content)
    # `from_` is the Python spelling; the wire name is `from`. Unset fields are omitted.
    assert body == {
        "to": "jane@acme.com",
        "template": "welcome",
        "props": {"firstName": "Jane"},
        "from": "Acme <hi@acme.com>",
    }


@respx.mock
def test_idempotency_key_is_the_callers_or_generated_for_every_post() -> None:
    route = respx.post(f"{BASE}/api/v1/emails").mock(
        return_value=httpx.Response(202, json={"id": "msg_1", "status": "queued"})
    )
    c = client()
    c.emails.send(to="a@x.com", template="t", idempotency_key="welcome/42")
    c.emails.send(to="a@x.com", template="t")
    assert route.calls[0].request.headers["idempotency-key"] == "welcome/42"
    assert len(route.calls[1].request.headers["idempotency-key"]) == 36


@respx.mock
def test_path_and_query_parameters() -> None:
    respx.get(f"{BASE}/api/v1/webhooks/whe_1/deliveries").mock(
        return_value=httpx.Response(200, json={"object": "list", "data": [], "has_more": False, "next_cursor": None})
    )
    page = client().webhooks.deliveries.list("whe_1", status="failed", limit=10)
    assert page.has_more is False
    url = respx.calls.last.request.url
    assert url.params["status"] == "failed" and url.params["limit"] == "10"


# ── errors ──────────────────────────────────────────────────────────────────


@respx.mock
def test_a_404_raises_not_found_with_the_request_id() -> None:
    respx.get(f"{BASE}/api/v1/templates/nope").mock(
        return_value=httpx.Response(
            404, json={"error": {"code": "not_found", "message": 'No template "nope".', "request_id": "req_9"}}
        )
    )
    with pytest.raises(NotFoundError) as caught:
        client().templates.get("nope")
    assert caught.value.code == "not_found"
    assert caught.value.status == 404
    assert caught.value.request_id == "req_9"


@respx.mock
def test_a_403_keeps_the_scope_detail() -> None:
    respx.get(f"{BASE}/api/v1/settings").mock(
        return_value=httpx.Response(
            403,
            json={"error": {"code": "forbidden", "message": "Needs admin.", "required_scope": "admin"}},
            headers={"X-Request-Id": "req_h"},
        )
    )
    with pytest.raises(PermissionDeniedError) as caught:
        client().settings.get()
    assert caught.value.body["required_scope"] == "admin"
    assert caught.value.request_id == "req_h"


# ── retries ─────────────────────────────────────────────────────────────────


@respx.mock
def test_retries_a_503_with_the_same_idempotency_key() -> None:
    route = respx.post(f"{BASE}/api/v1/emails").mock(
        side_effect=[
            httpx.Response(503, json={"error": {"code": "internal", "message": "x"}}, headers={"Retry-After": "0"}),
            httpx.Response(202, json={"id": "msg_1", "status": "queued"}),
        ]
    )
    assert client().emails.send(to="a@x.com", template="t").id == "msg_1"
    first, second = (call.request.headers["idempotency-key"] for call in route.calls)
    assert first == second


@respx.mock
def test_never_retries_a_sending_quota() -> None:
    route = respx.post(f"{BASE}/api/v1/emails").mock(
        return_value=httpx.Response(
            429, json={"error": {"code": "daily_cap", "message": "cap"}}, headers={"Retry-After": "0"}
        )
    )
    with pytest.raises(QuotaExceededError):
        client().emails.send(to="a@x.com", template="t")
    assert route.call_count == 1


@respx.mock
def test_gives_up_after_max_retries() -> None:
    route = respx.get(f"{BASE}/api/v1/settings").mock(
        return_value=httpx.Response(
            500, json={"error": {"code": "internal", "message": "x"}}, headers={"Retry-After": "0"}
        )
    )
    with pytest.raises(sendandretain.APIError):
        client(max_retries=3).settings.get()
    assert route.call_count == 4


# ── pagination ──────────────────────────────────────────────────────────────


def message(id_: str) -> dict[str, Any]:
    return {"id": id_, "to": "a@x.com", "status": "delivered", "created_at": "2026-10-05T10:00:00Z"}


@respx.mock
def test_iterate_follows_next_cursor() -> None:
    route = respx.get(f"{BASE}/api/v1/emails").mock(
        side_effect=[
            httpx.Response(
                200,
                json={"object": "list", "data": [message("a"), message("b")], "has_more": True, "next_cursor": "c1"},
            ),
            httpx.Response(
                200, json={"object": "list", "data": [message("c")], "has_more": False, "next_cursor": None}
            ),
        ]
    )
    ids = [email.id for email in client().emails.iterate(status="delivered")]
    assert ids == ["a", "b", "c"]
    assert route.calls[1].request.url.params["cursor"] == "c1"
    assert route.calls[1].request.url.params["status"] == "delivered"


# ── async ───────────────────────────────────────────────────────────────────


@respx.mock
async def test_async_client_has_the_same_surface() -> None:
    respx.post(f"{BASE}/api/v1/emails").mock(return_value=httpx.Response(202, json={"id": "msg_1", "status": "queued"}))
    async with AsyncSendAndRetain(KEY) as c:
        email = await c.emails.send(to="a@x.com", template="t")
    assert email.id == "msg_1"


@respx.mock
async def test_async_iterate() -> None:
    respx.get(f"{BASE}/api/v1/contacts").mock(
        return_value=httpx.Response(
            200,
            json={
                "object": "list",
                "data": [{"id": "ct_1", "email": "a@x.com"}],
                "has_more": False,
                "next_cursor": None,
            },
        )
    )
    async with AsyncSendAndRetain(KEY) as c:
        rows = [row async for row in c.contacts.iterate()]
    assert len(rows) == 1


# ── webhooks ────────────────────────────────────────────────────────────────

SECRET = "whsec_" + base64.b64encode(b"a-32-byte-secret-for-the-tests!!").decode()
EVENT = {"id": "del_1", "type": "email.bounced", "version": "1", "data": {"message": None, "detail": {}}}


def signed(body: bytes, ts: int = 1_760_000_000, msg_id: str = "del_1") -> dict[str, str]:
    key = base64.b64decode(SECRET.removeprefix("whsec_"))
    sig = base64.b64encode(hmac.new(key, f"{msg_id}.{ts}.".encode() + body, hashlib.sha256).digest()).decode()
    return {"Webhook-Id": msg_id, "Webhook-Timestamp": str(ts), "Webhook-Signature": f"v1,{sig}"}


def test_verifies_a_genuine_delivery() -> None:
    body = json.dumps(EVENT).encode()
    event = verify_webhook(body, signed(body), SECRET, now=1_760_000_010)
    assert event["type"] == "email.bounced"
    assert SendAndRetain.verify_webhook is not None


def test_accepts_either_signature_during_a_rotation() -> None:
    body = json.dumps(EVENT).encode()
    headers = signed(body)
    headers["Webhook-Signature"] = "v1,bm90LXRoaXMtb25l " + headers["Webhook-Signature"]
    assert verify_webhook(body.decode(), headers, SECRET, now=1_760_000_000)["id"] == "del_1"


def test_rejects_a_tampered_body_or_a_stale_timestamp() -> None:
    body = json.dumps(EVENT).encode()
    with pytest.raises(WebhookVerificationError):
        verify_webhook(body.replace(b"bounced", b"opened"), signed(body), SECRET, now=1_760_000_000)
    with pytest.raises(WebhookVerificationError):
        verify_webhook(body, signed(body), SECRET, now=1_760_000_000 + 3600)


def test_interoperates_with_the_reference_signer() -> None:
    """Our verifier accepts what the server's signer (Standard Webhooks) produces."""
    standardwebhooks = pytest.importorskip("standardwebhooks")
    body = json.dumps(EVENT)
    from datetime import UTC, datetime

    ts = datetime.fromtimestamp(1_760_000_000, tz=UTC)
    sig = standardwebhooks.Webhook(SECRET).sign("del_1", ts, body)
    headers = {"webhook-id": "del_1", "webhook-timestamp": "1760000000", "webhook-signature": sig}
    assert verify_webhook(body, headers, SECRET, now=1_760_000_000)["type"] == "email.bounced"


# ── coverage ────────────────────────────────────────────────────────────────


def test_every_operation_has_a_facade_method() -> None:
    import importlib.util
    import sys

    spec_path = REPO / "scripts" / "generate_facade.py"
    loader = importlib.util.spec_from_file_location("generate_facade", spec_path)
    assert loader and loader.loader
    module = importlib.util.module_from_spec(loader)
    sys.modules["generate_facade"] = module
    loader.loader.exec_module(module)

    spec = json.loads((REPO / "openapi.json").read_text())
    op_ids = {op["operationId"] for methods in spec["paths"].values() for k, op in methods.items() if k != "parameters"}
    assert op_ids == set(module.FACADE)

    c = client()
    for target in module.FACADE.values():
        obj: Any = c
        for part in target.split("."):
            obj = getattr(obj, part)
        assert callable(obj), target
