"""Plumbing shared by every generated resource method in `_resources.py`.

A facade method hands its operation's generated module and plain Python values
to `_call`; this turns the body into the generated model, invokes the module's
`sync_detailed` / `asyncio_detailed`, and returns the parsed success model or
raises a typed `SendAndRetainError`. The per-operation knowledge — which
arguments are path, query or body — lives in the generated method signatures.
"""

from __future__ import annotations

import inspect
import json
import types
import typing
from functools import cache
from typing import Any

import httpx

from ._exceptions import APIConnectionError, error_for

__all__ = ["AsyncResource", "Resource", "invoke", "ainvoke"]


@cache
def _body_model(module: types.ModuleType) -> Any:
    """The attrs model the module's `body` parameter takes, or None."""
    param = inspect.signature(module.sync_detailed).parameters.get("body")
    if param is None:
        return None
    hint = typing.get_type_hints(module.sync_detailed).get("body", param.annotation)
    for candidate in (hint, *typing.get_args(hint)):
        if hasattr(candidate, "from_dict"):
            return candidate
    return None


def _kwargs(module: types.ModuleType, body: dict[str, Any] | None, params: dict[str, Any]) -> dict[str, Any]:
    kwargs = {k: v for k, v in params.items() if v is not None}
    if body is not None:
        model = _body_model(module)
        compact = {k: v for k, v in body.items() if v is not None}
        kwargs["body"] = model.from_dict(compact) if model is not None else compact
    return kwargs


def _result(response: Any) -> Any:
    status = int(response.status_code)
    if 200 <= status < 300:
        if response.parsed is not None:
            return response.parsed
        try:
            return json.loads(response.content) if response.content else None
        except ValueError:
            return None
    try:
        payload = json.loads(response.content) if response.content else None
    except ValueError:
        payload = None
    raise error_for(status, payload, response.headers.get("X-Request-Id"))


def invoke(raw: Any, module: types.ModuleType, body: dict[str, Any] | None, params: dict[str, Any]) -> Any:
    try:
        response = module.sync_detailed(client=raw, **_kwargs(module, body, params))
    except httpx.TransportError as exc:
        raise APIConnectionError(str(exc) or type(exc).__name__, code="network_error") from exc
    return _result(response)


async def ainvoke(raw: Any, module: types.ModuleType, body: dict[str, Any] | None, params: dict[str, Any]) -> Any:
    try:
        response = await module.asyncio_detailed(client=raw, **_kwargs(module, body, params))
    except httpx.TransportError as exc:
        raise APIConnectionError(str(exc) or type(exc).__name__, code="network_error") from exc
    return _result(response)


class Resource:
    def __init__(self, client: Any) -> None:
        self._raw = client

    def _call(self, module: types.ModuleType, *, body: dict[str, Any] | None = None, **params: Any) -> Any:
        return invoke(self._raw, module, body, params)


class AsyncResource:
    def __init__(self, client: Any) -> None:
        self._raw = client

    async def _call(self, module: types.ModuleType, *, body: dict[str, Any] | None = None, **params: Any) -> Any:
        return await ainvoke(self._raw, module, body, params)
