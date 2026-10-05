"""Typed exceptions. Every API error raised by the facade is a `SendAndRetainError`."""

from __future__ import annotations

from typing import Any

__all__ = [
    "APIConnectionError",
    "APIError",
    "AuthenticationError",
    "ConflictError",
    "InvalidRequestError",
    "NotFoundError",
    "PermissionDeniedError",
    "QuotaExceededError",
    "RateLimitError",
    "SendAndRetainError",
    "WebhookVerificationError",
]


class SendAndRetainError(Exception):
    """Base class. Branch on `code`; quote `request_id` to support."""

    def __init__(
        self,
        message: str,
        *,
        code: str,
        status: int | None = None,
        request_id: str | None = None,
        body: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(message)
        self.message = message
        self.code = code
        self.status = status
        self.request_id = request_id
        #: The full `error` object, including fields like `required_scope`.
        self.body = body or {}

    def __str__(self) -> str:
        ref = f" (request_id {self.request_id})" if self.request_id else ""
        return f"{self.code}: {self.message}{ref}"


class APIError(SendAndRetainError):
    """Any error response not covered by a more specific class — 5xx included."""


class InvalidRequestError(APIError):
    """400 / 422: the request itself is wrong. Nothing changed; fix and resend."""


class AuthenticationError(APIError):
    """401: missing, invalid, revoked or expired key."""


class PermissionDeniedError(APIError):
    """403: the key is valid but lacks the scope or the send grant. See `body["required_scope"]`."""


class NotFoundError(APIError):
    """404: no such resource in this project."""


class ConflictError(APIError):
    """409: an idempotency conflict, or the resource's state forbids the action."""


class RateLimitError(APIError):
    """429 `rate_limited`, after the SDK's own retries were exhausted."""


class QuotaExceededError(APIError):
    """429 `daily_cap` / `monthly_cap`: a sending quota, not a throttle. Never retried."""


class APIConnectionError(SendAndRetainError):
    """No response arrived: DNS, TLS, a reset connection, or a timeout."""


class WebhookVerificationError(SendAndRetainError):
    """A webhook's signature or timestamp did not verify. Answer 400 and do nothing else."""


def error_for(status: int, payload: Any, request_id: str | None) -> APIError:
    envelope = payload.get("error") if isinstance(payload, dict) else None
    envelope = envelope if isinstance(envelope, dict) else {}
    code = str(envelope.get("code") or f"http_{status}")
    message = str(envelope.get("message") or f"HTTP {status}")
    rid = envelope.get("request_id") or request_id
    cls: type[APIError]
    if code in ("daily_cap", "monthly_cap"):
        cls = QuotaExceededError
    elif status in (400, 422):
        cls = InvalidRequestError
    else:
        cls = {
            401: AuthenticationError,
            403: PermissionDeniedError,
            404: NotFoundError,
            409: ConflictError,
            429: RateLimitError,
        }.get(status, APIError)
    return cls(message, code=code, status=status, request_id=rid, body=envelope)
