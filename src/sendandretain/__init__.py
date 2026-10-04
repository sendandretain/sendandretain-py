"""Send & Retain — Python SDK.

Send transactional and lifecycle email, sync contacts, and emit events that drive automations.

The typed surface under `sendandretain.api` and `sendandretain.models` is generated from the
published OpenAPI document and is the contract. `Client` is a small hand-written
wrapper that supplies the base URL and bearer prefix; see `sendandretain._convenience`.

    >>> from sendandretain import Client
    >>> from sendandretain.api.campaigns import list_campaigns  # doctest: +SKIP
    >>> client = Client(api_key="...")  # doctest: +SKIP
"""

from __future__ import annotations

from . import api, errors, models, types
from ._convenience import API_KEY_ENV_VAR, API_KEY_PREFIX, DEFAULT_BASE_URL, Client
from .client import AuthenticatedClient
from .client import Client as RawClient

__all__ = [
    "API_KEY_ENV_VAR",
    "API_KEY_PREFIX",
    "DEFAULT_BASE_URL",
    "AuthenticatedClient",
    "Client",
    "RawClient",
    "api",
    "errors",
    "models",
    "types",
]

__version__ = "0.1.0"
