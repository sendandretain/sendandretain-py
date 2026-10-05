"""Send & Retain — Python SDK.

    >>> from sendandretain import SendAndRetain
    >>> client = SendAndRetain()  # reads SENDANDRETAIN_API_KEY  # doctest: +SKIP
    >>> email = client.emails.send(to="jane@acme.com", template="welcome")  # doctest: +SKIP

Three layers, top to bottom:

- `SendAndRetain` / `AsyncSendAndRetain` — one method per operation, typed
  keyword arguments, typed exceptions. Generated from `openapi.json` by
  `scripts/generate_facade.py` into `_resources.py`.
- `sendandretain.api` / `sendandretain.models` — the full generated client, for
  anything the facade does not shape the way you need.
- `_runtime.py` — the transport (retries, idempotency, User-Agent), synced from
  the Send & Retain source tree.
"""

from __future__ import annotations

from . import api, errors, models, types
from ._client import AsyncSendAndRetain, SendAndRetain
from ._convenience import API_KEY_ENV_VAR, API_KEY_PREFIX, DEFAULT_BASE_URL, Client
from ._exceptions import (
    APIConnectionError,
    APIError,
    AuthenticationError,
    ConflictError,
    InvalidRequestError,
    NotFoundError,
    PermissionDeniedError,
    QuotaExceededError,
    RateLimitError,
    SendAndRetainError,
    WebhookVerificationError,
)
from ._version import __version__
from ._webhooks import verify_webhook
from .client import AuthenticatedClient
from .client import Client as RawClient

__all__ = [
    "API_KEY_ENV_VAR",
    "API_KEY_PREFIX",
    "DEFAULT_BASE_URL",
    "APIConnectionError",
    "APIError",
    "AsyncSendAndRetain",
    "AuthenticatedClient",
    "AuthenticationError",
    "Client",
    "ConflictError",
    "InvalidRequestError",
    "NotFoundError",
    "PermissionDeniedError",
    "QuotaExceededError",
    "RateLimitError",
    "RawClient",
    "SendAndRetain",
    "SendAndRetainError",
    "WebhookVerificationError",
    "__version__",
    "api",
    "errors",
    "models",
    "types",
    "verify_webhook",
]
