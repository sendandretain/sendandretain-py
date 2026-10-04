from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.import_suppressions_body import ImportSuppressionsBody
from ...models.import_suppressions_response_200 import ImportSuppressionsResponse200
from ...types import Response


def _get_kwargs(
    *,
    body: ImportSuppressionsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/suppressions/import",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | ImportSuppressionsResponse200 | None:
    if response.status_code == 200:
        response_200 = ImportSuppressionsResponse200.from_dict(response.json())

        return response_200

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
) -> Response[Error | ImportSuppressionsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ImportSuppressionsBody,
) -> Response[Error | ImportSuppressionsResponse200]:
    """Bulk import suppressions

     Carry existing unsubscribes over BEFORE your first send, so people who already opted out never hear
    from you again. Only `manual` and `unsubscribe` are importable — bounces and complaints are facts
    the provider reports through webhooks, and asserting them by hand would corrupt the severity ladder.

    Args:
        body (ImportSuppressionsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ImportSuppressionsResponse200]
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
    client: AuthenticatedClient | Client,
    body: ImportSuppressionsBody,
) -> Error | ImportSuppressionsResponse200 | None:
    """Bulk import suppressions

     Carry existing unsubscribes over BEFORE your first send, so people who already opted out never hear
    from you again. Only `manual` and `unsubscribe` are importable — bounces and complaints are facts
    the provider reports through webhooks, and asserting them by hand would corrupt the severity ladder.

    Args:
        body (ImportSuppressionsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ImportSuppressionsResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ImportSuppressionsBody,
) -> Response[Error | ImportSuppressionsResponse200]:
    """Bulk import suppressions

     Carry existing unsubscribes over BEFORE your first send, so people who already opted out never hear
    from you again. Only `manual` and `unsubscribe` are importable — bounces and complaints are facts
    the provider reports through webhooks, and asserting them by hand would corrupt the severity ladder.

    Args:
        body (ImportSuppressionsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ImportSuppressionsResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ImportSuppressionsBody,
) -> Error | ImportSuppressionsResponse200 | None:
    """Bulk import suppressions

     Carry existing unsubscribes over BEFORE your first send, so people who already opted out never hear
    from you again. Only `manual` and `unsubscribe` are importable — bounces and complaints are facts
    the provider reports through webhooks, and asserting them by hand would corrupt the severity ladder.

    Args:
        body (ImportSuppressionsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ImportSuppressionsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
