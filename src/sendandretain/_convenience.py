"""The hand-written convenience layer over the generated client.

Deliberately thin, and one of only two hand-written modules in the package.
Everything beside it under `sendandretain/` is generated from `openapi.json` and is the
contract; this module exists only so callers need not remember the base URL,
spell `AuthenticatedClient`, or wire up the `Bearer` prefix by hand.

Kept out of `__init__.py` so that regeneration, which rewrites `client.py`,
`api/`, `models/`, `types.py` and `errors.py` wholesale, can never clobber it.
"""

from __future__ import annotations

import os

import httpx

from .client import AuthenticatedClient

__all__ = ["API_KEY_ENV_VAR", "API_KEY_PREFIX", "DEFAULT_BASE_URL", "Client"]

DEFAULT_BASE_URL = "https://sendandretain.com"
"""Production base URL for the Send & Retain API."""

API_KEY_PREFIX = "aem_"
"""Every Send & Retain API key starts with this. The server rejects anything else
before it touches the database, so checking it here turns a 401 into a
`ValueError` that names the actual problem."""

API_KEY_ENV_VAR = "SENDANDRETAIN_API_KEY"
"""Consulted when `api_key` is not passed explicitly."""


def Client(  # noqa: N802 - a factory that reads as a constructor at the call site
    api_key: str | None = None,
    *,
    base_url: str = DEFAULT_BASE_URL,
    timeout: httpx.Timeout | float | None = None,
    raise_on_unexpected_status: bool = False,
    **kwargs: object,
) -> AuthenticatedClient:
    """Build an authenticated client for the Send & Retain API.

    Args:
        api_key: A `aem_…` key. Falls back to `$SENDANDRETAIN_API_KEY`.
        base_url: Override only to target a non-production deployment.
        timeout: Passed through to httpx. Seconds, or an `httpx.Timeout`.
        raise_on_unexpected_status: Raise `errors.UnexpectedStatus` on a status
            the spec does not document, instead of returning `None`.
        **kwargs: Forwarded to the generated `AuthenticatedClient` — `headers`,
            `cookies`, `verify_ssl`, `follow_redirects`, `httpx_args`.

    Returns:
        An `AuthenticatedClient` accepted by every function in
        `sendandretain.api.*` as the `client=` argument.

    Raises:
        ValueError: No key was supplied, or it does not look like a Send & Retain key.
    """
    key = api_key if api_key is not None else os.environ.get(API_KEY_ENV_VAR)
    if not key:
        raise ValueError(f"No API key. Pass Client(api_key=...) or set ${API_KEY_ENV_VAR}.")
    if not key.startswith(API_KEY_PREFIX):
        raise ValueError(f"Send & Retain API keys start with {API_KEY_PREFIX!r}; got {key[:8]!r}…")

    if isinstance(timeout, (int, float)):
        timeout = httpx.Timeout(timeout)

    return AuthenticatedClient(
        base_url=base_url,
        token=key,
        prefix="Bearer",
        timeout=timeout,
        raise_on_unexpected_status=raise_on_unexpected_status,
        **kwargs,  # type: ignore[arg-type]
    )
