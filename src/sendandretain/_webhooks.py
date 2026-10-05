"""Standard Webhooks verification, standard library only.

Every delivery carries `webhook-id`, `webhook-timestamp` and `webhook-signature`.
The signature is `v1,<base64 HMAC-SHA256>` of `{id}.{timestamp}.{raw body}`, keyed
with the base64 part of the endpoint's `whsec_` secret; during a secret rotation
the header carries two, space-separated, and either may match.
"""

from __future__ import annotations

import base64
import hashlib
import hmac
import json
import time
from collections.abc import Mapping
from typing import Any

from ._exceptions import WebhookVerificationError

__all__ = ["TOLERANCE_SECONDS", "verify_webhook"]

#: Reject a timestamp further than this from now — replay protection.
TOLERANCE_SECONDS = 5 * 60

_SECRET_PREFIX = "whsec_"


def _fail(message: str) -> WebhookVerificationError:
    return WebhookVerificationError(message, code="invalid_signature")


def verify_webhook(
    payload: str | bytes,
    headers: Mapping[str, str],
    secret: str,
    *,
    tolerance: int = TOLERANCE_SECONDS,
    now: float | None = None,
) -> dict[str, Any]:
    """Verify a delivery and return the parsed event (`event["type"]`, `event["data"]`).

    Pass the RAW body — `await request.body()`, `request.get_data()` — never a
    re-serialised dict: one changed byte fails the signature.

    Raises:
        WebhookVerificationError: missing headers, a bad signature, or a stale timestamp.
    """
    lower = {k.lower(): v for k, v in headers.items()}
    msg_id = lower.get("webhook-id")
    timestamp = lower.get("webhook-timestamp")
    signatures = lower.get("webhook-signature")
    if not msg_id or not timestamp or not signatures:
        raise _fail("Missing webhook-id, webhook-timestamp or webhook-signature header.")

    try:
        sent = int(timestamp)
    except ValueError as exc:
        raise _fail("webhook-timestamp is not a number.") from exc
    if abs((now if now is not None else time.time()) - sent) > tolerance:
        raise _fail("webhook-timestamp is outside the tolerance window.")

    key = secret.removeprefix(_SECRET_PREFIX)
    try:
        key_bytes = base64.b64decode(key) if secret.startswith(_SECRET_PREFIX) else secret.encode()
    except ValueError as exc:
        raise _fail("The secret is not valid base64 after whsec_.") from exc

    body = payload if isinstance(payload, bytes) else payload.encode()
    signed = f"{msg_id}.{timestamp}.".encode() + body
    expected = base64.b64encode(hmac.new(key_bytes, signed, hashlib.sha256).digest()).decode()

    for candidate in signatures.split(" "):
        version, _, value = candidate.partition(",")
        if version == "v1" and hmac.compare_digest(value, expected):
            event: dict[str, Any] = json.loads(body)
            return event
    raise _fail("No signature matched.")
