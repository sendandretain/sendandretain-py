from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.emit_event_body import EmitEventBody
from ...models.emit_event_response_202 import EmitEventResponse202
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    *,
    body: EmitEventBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/events",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EmitEventResponse202 | Error | None:
    if response.status_code == 202:
        response_202 = EmitEventResponse202.from_dict(response.json())

        return response_202

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[EmitEventResponse202 | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: EmitEventBody,
) -> Response[EmitEventResponse202 | Error]:
    """Emit a contact event

     Records an event for a contact (creating the contact if you pass an unknown email). Provide `email`
    or `external_id`.

    Accepted and queued: you get `202` with an id the moment the event is durably stored, and the
    contact upsert plus automation enrollment run in the background. This endpoint is designed to be
    called from inside your own user-facing request, so it never makes you wait on that work — the same
    reason `202 Accepted` is the only answer SendGrid's send endpoint gives.

    To see what an event actually did — which automations enrolled and why the others declined — read
    the contact's timeline with `GET /api/v1/contacts/{id}/events`; each event carries its recorded
    outcome.

    Args:
        body (EmitEventBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EmitEventResponse202 | Error]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: EmitEventBody,
) -> EmitEventResponse202 | Error | None:
    """Emit a contact event

     Records an event for a contact (creating the contact if you pass an unknown email). Provide `email`
    or `external_id`.

    Accepted and queued: you get `202` with an id the moment the event is durably stored, and the
    contact upsert plus automation enrollment run in the background. This endpoint is designed to be
    called from inside your own user-facing request, so it never makes you wait on that work — the same
    reason `202 Accepted` is the only answer SendGrid's send endpoint gives.

    To see what an event actually did — which automations enrolled and why the others declined — read
    the contact's timeline with `GET /api/v1/contacts/{id}/events`; each event carries its recorded
    outcome.

    Args:
        body (EmitEventBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EmitEventResponse202 | Error
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: EmitEventBody,
) -> Response[EmitEventResponse202 | Error]:
    """Emit a contact event

     Records an event for a contact (creating the contact if you pass an unknown email). Provide `email`
    or `external_id`.

    Accepted and queued: you get `202` with an id the moment the event is durably stored, and the
    contact upsert plus automation enrollment run in the background. This endpoint is designed to be
    called from inside your own user-facing request, so it never makes you wait on that work — the same
    reason `202 Accepted` is the only answer SendGrid's send endpoint gives.

    To see what an event actually did — which automations enrolled and why the others declined — read
    the contact's timeline with `GET /api/v1/contacts/{id}/events`; each event carries its recorded
    outcome.

    Args:
        body (EmitEventBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EmitEventResponse202 | Error]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: EmitEventBody,
) -> EmitEventResponse202 | Error | None:
    """Emit a contact event

     Records an event for a contact (creating the contact if you pass an unknown email). Provide `email`
    or `external_id`.

    Accepted and queued: you get `202` with an id the moment the event is durably stored, and the
    contact upsert plus automation enrollment run in the background. This endpoint is designed to be
    called from inside your own user-facing request, so it never makes you wait on that work — the same
    reason `202 Accepted` is the only answer SendGrid's send endpoint gives.

    To see what an event actually did — which automations enrolled and why the others declined — read
    the contact's timeline with `GET /api/v1/contacts/{id}/events`; each event carries its recorded
    outcome.

    Args:
        body (EmitEventBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EmitEventResponse202 | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
