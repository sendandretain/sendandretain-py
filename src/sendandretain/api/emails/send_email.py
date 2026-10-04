from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.send_email_body import SendEmailBody
from ...models.send_result import SendResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: SendEmailBody,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/emails",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | SendResult | None:
    if response.status_code == 200:
        response_200 = SendResult.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = SendResult.from_dict(response.json())

        return response_202

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = Error.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())

        return response_429

    if response.status_code == 502:
        response_502 = Error.from_dict(response.json())

        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | SendResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SendEmailBody,
    idempotency_key: str | Unset = UNSET,
) -> Response[Error | SendResult]:
    """Send an email

     Queues a send to one recipient from a published template. Returns `202` with a message id once the
    send is durably recorded — never waiting on the provider, so this is safe to call from inside your
    own user-facing request. Address verification, rendering and provider dispatch happen in the
    background, exactly as they do behind SendGrid's `202 Accepted` and Resend's immediate id.

    Problems with the REQUEST still come back right away as a 4xx: an unknown or unpublished template,
    no verified sender, a suppressed or undeliverable recipient, a paused project, a cap. What moves is
    the delivery itself.

    Follow a message with `GET /api/v1/emails/{id}`, or subscribe to your provider's webhooks. Pass an
    `Idempotency-Key` header to make retries safe.

    Requires a `write`-scope key.

    Args:
        idempotency_key (str | Unset):
        body (SendEmailBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SendResult]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: SendEmailBody,
    idempotency_key: str | Unset = UNSET,
) -> Error | SendResult | None:
    """Send an email

     Queues a send to one recipient from a published template. Returns `202` with a message id once the
    send is durably recorded — never waiting on the provider, so this is safe to call from inside your
    own user-facing request. Address verification, rendering and provider dispatch happen in the
    background, exactly as they do behind SendGrid's `202 Accepted` and Resend's immediate id.

    Problems with the REQUEST still come back right away as a 4xx: an unknown or unpublished template,
    no verified sender, a suppressed or undeliverable recipient, a paused project, a cap. What moves is
    the delivery itself.

    Follow a message with `GET /api/v1/emails/{id}`, or subscribe to your provider's webhooks. Pass an
    `Idempotency-Key` header to make retries safe.

    Requires a `write`-scope key.

    Args:
        idempotency_key (str | Unset):
        body (SendEmailBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SendResult
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SendEmailBody,
    idempotency_key: str | Unset = UNSET,
) -> Response[Error | SendResult]:
    """Send an email

     Queues a send to one recipient from a published template. Returns `202` with a message id once the
    send is durably recorded — never waiting on the provider, so this is safe to call from inside your
    own user-facing request. Address verification, rendering and provider dispatch happen in the
    background, exactly as they do behind SendGrid's `202 Accepted` and Resend's immediate id.

    Problems with the REQUEST still come back right away as a 4xx: an unknown or unpublished template,
    no verified sender, a suppressed or undeliverable recipient, a paused project, a cap. What moves is
    the delivery itself.

    Follow a message with `GET /api/v1/emails/{id}`, or subscribe to your provider's webhooks. Pass an
    `Idempotency-Key` header to make retries safe.

    Requires a `write`-scope key.

    Args:
        idempotency_key (str | Unset):
        body (SendEmailBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SendResult]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SendEmailBody,
    idempotency_key: str | Unset = UNSET,
) -> Error | SendResult | None:
    """Send an email

     Queues a send to one recipient from a published template. Returns `202` with a message id once the
    send is durably recorded — never waiting on the provider, so this is safe to call from inside your
    own user-facing request. Address verification, rendering and provider dispatch happen in the
    background, exactly as they do behind SendGrid's `202 Accepted` and Resend's immediate id.

    Problems with the REQUEST still come back right away as a 4xx: an unknown or unpublished template,
    no verified sender, a suppressed or undeliverable recipient, a paused project, a cap. What moves is
    the delivery itself.

    Follow a message with `GET /api/v1/emails/{id}`, or subscribe to your provider's webhooks. Pass an
    `Idempotency-Key` header to make retries safe.

    Requires a `write`-scope key.

    Args:
        idempotency_key (str | Unset):
        body (SendEmailBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SendResult
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
