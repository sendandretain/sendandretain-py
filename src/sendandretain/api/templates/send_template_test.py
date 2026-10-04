from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.send_template_test_body import SendTemplateTestBody
from ...models.send_template_test_response_201 import SendTemplateTestResponse201
from ...types import Response


def _get_kwargs(
    slug: str,
    *,
    body: SendTemplateTestBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/templates/{slug}/test".format(
            slug=quote(str(slug), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | SendTemplateTestResponse201 | None:
    if response.status_code == 201:
        response_201 = SendTemplateTestResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | SendTemplateTestResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    slug: str,
    *,
    client: AuthenticatedClient | Client,
    body: SendTemplateTestBody,
) -> Response[Error | SendTemplateTestResponse201]:
    """Send a test email

     Sends a `[TEST]`-prefixed copy to one inbox. Works on an unpublished draft — that's the point, you
    test before you publish. Test sends deliberately skip idempotency, suppression and the daily cap,
    but every attempt is still logged.

    Args:
        slug (str):
        body (SendTemplateTestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SendTemplateTestResponse201]
    """

    kwargs = _get_kwargs(
        slug=slug,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    slug: str,
    *,
    client: AuthenticatedClient | Client,
    body: SendTemplateTestBody,
) -> Error | SendTemplateTestResponse201 | None:
    """Send a test email

     Sends a `[TEST]`-prefixed copy to one inbox. Works on an unpublished draft — that's the point, you
    test before you publish. Test sends deliberately skip idempotency, suppression and the daily cap,
    but every attempt is still logged.

    Args:
        slug (str):
        body (SendTemplateTestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SendTemplateTestResponse201
    """

    return sync_detailed(
        slug=slug,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    slug: str,
    *,
    client: AuthenticatedClient | Client,
    body: SendTemplateTestBody,
) -> Response[Error | SendTemplateTestResponse201]:
    """Send a test email

     Sends a `[TEST]`-prefixed copy to one inbox. Works on an unpublished draft — that's the point, you
    test before you publish. Test sends deliberately skip idempotency, suppression and the daily cap,
    but every attempt is still logged.

    Args:
        slug (str):
        body (SendTemplateTestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SendTemplateTestResponse201]
    """

    kwargs = _get_kwargs(
        slug=slug,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    slug: str,
    *,
    client: AuthenticatedClient | Client,
    body: SendTemplateTestBody,
) -> Error | SendTemplateTestResponse201 | None:
    """Send a test email

     Sends a `[TEST]`-prefixed copy to one inbox. Works on an unpublished draft — that's the point, you
    test before you publish. Test sends deliberately skip idempotency, suppression and the daily cap,
    but every attempt is still logged.

    Args:
        slug (str):
        body (SendTemplateTestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SendTemplateTestResponse201
    """

    return (
        await asyncio_detailed(
            slug=slug,
            client=client,
            body=body,
        )
    ).parsed
