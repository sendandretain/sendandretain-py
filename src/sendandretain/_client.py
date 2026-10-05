"""`SendAndRetain` and `AsyncSendAndRetain` — the clients most code should use."""

from __future__ import annotations

from typing import Any

import httpx

from ._resources import AsyncResources, Resources
from ._runtime import (
    DEFAULT_MAX_RETRIES,
    DEFAULT_TIMEOUT_SECONDS,
    AsyncRetryTransport,
    RetryTransport,
    resolve_api_key,
    resolve_base_url,
)
from ._version import __version__
from ._webhooks import verify_webhook
from .client import AuthenticatedClient

__all__ = ["AsyncSendAndRetain", "SendAndRetain"]


def _raw_client(key: str, base_url: str, timeout: float, transport: Any) -> AuthenticatedClient:
    return AuthenticatedClient(
        base_url=base_url,
        token=key,
        prefix="Bearer",
        timeout=httpx.Timeout(timeout),
        httpx_args={"transport": transport},
    )


class SendAndRetain(Resources):
    """The Send & Retain client.

    >>> from sendandretain import SendAndRetain
    >>> client = SendAndRetain()  # reads SENDANDRETAIN_API_KEY  # doctest: +SKIP
    >>> email = client.emails.send(to="jane@acme.com", template="welcome")  # doctest: +SKIP
    >>> email.id  # doctest: +SKIP

    Methods return the parsed model and raise a `SendAndRetainError` subclass on
    any failure. Requests that fail with 408/429/5xx or a network error are
    retried with backoff; every POST carries an `Idempotency-Key` (yours, or a
    generated one) so a retry can never do the work twice.
    """

    def __init__(
        self,
        api_key: str | None = None,
        *,
        base_url: str | None = None,
        timeout: float = DEFAULT_TIMEOUT_SECONDS,
        max_retries: int = DEFAULT_MAX_RETRIES,
        transport: httpx.BaseTransport | None = None,
    ) -> None:
        key = resolve_api_key(api_key)
        retry = RetryTransport(key, __version__, max_retries=max_retries, transport=transport)
        #: The generated client, for `sendandretain.api.*` functions directly.
        self.raw = _raw_client(key, resolve_base_url(base_url), timeout, retry)
        super().__init__(self.raw)

    @staticmethod
    def verify_webhook(payload: str | bytes, headers: Any, secret: str) -> dict[str, Any]:
        """Verify a webhook delivery and return the event. See `sendandretain.verify_webhook`."""
        return verify_webhook(payload, headers, secret)

    def close(self) -> None:
        self.raw.get_httpx_client().close()

    def __enter__(self) -> SendAndRetain:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()


class AsyncSendAndRetain(AsyncResources):
    """The asyncio twin of `SendAndRetain`: same resources, every method awaitable.

    >>> async with AsyncSendAndRetain() as client:  # doctest: +SKIP
    ...     email = await client.emails.send(to="jane@acme.com", template="welcome")
    """

    def __init__(
        self,
        api_key: str | None = None,
        *,
        base_url: str | None = None,
        timeout: float = DEFAULT_TIMEOUT_SECONDS,
        max_retries: int = DEFAULT_MAX_RETRIES,
        transport: httpx.AsyncBaseTransport | None = None,
    ) -> None:
        key = resolve_api_key(api_key)
        retry = AsyncRetryTransport(key, __version__, max_retries=max_retries, transport=transport)
        self.raw = _raw_client(key, resolve_base_url(base_url), timeout, retry)
        super().__init__(self.raw)

    @staticmethod
    def verify_webhook(payload: str | bytes, headers: Any, secret: str) -> dict[str, Any]:
        """Verify a webhook delivery and return the event. Synchronous — it does no I/O."""
        return verify_webhook(payload, headers, secret)

    async def close(self) -> None:
        await self.raw.get_async_httpx_client().aclose()

    async def __aenter__(self) -> AsyncSendAndRetain:
        return self

    async def __aexit__(self, *_: object) -> None:
        await self.close()
