from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.set_ab_test_body import SetAbTestBody
from ...models.set_ab_test_response_200 import SetAbTestResponse200
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: SetAbTestBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/automations/{id}/ab-test".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | SetAbTestResponse200 | None:
    if response.status_code == 200:
        response_200 = SetAbTestResponse200.from_dict(response.json())

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

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | SetAbTestResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SetAbTestBody,
) -> Response[Error | SetAbTestResponse200]:
    """Set up an A/B split

     Splits a send step across weighted template VERSIONS. Assignment is deterministic per contact-run,
    so a contact always sees the same arm. Pass `variants: null` to clear the split.

    Args:
        id (str):
        body (SetAbTestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SetAbTestResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SetAbTestBody,
) -> Error | SetAbTestResponse200 | None:
    """Set up an A/B split

     Splits a send step across weighted template VERSIONS. Assignment is deterministic per contact-run,
    so a contact always sees the same arm. Pass `variants: null` to clear the split.

    Args:
        id (str):
        body (SetAbTestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SetAbTestResponse200
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SetAbTestBody,
) -> Response[Error | SetAbTestResponse200]:
    """Set up an A/B split

     Splits a send step across weighted template VERSIONS. Assignment is deterministic per contact-run,
    so a contact always sees the same arm. Pass `variants: null` to clear the split.

    Args:
        id (str):
        body (SetAbTestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SetAbTestResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SetAbTestBody,
) -> Error | SetAbTestResponse200 | None:
    """Set up an A/B split

     Splits a send step across weighted template VERSIONS. Assignment is deterministic per contact-run,
    so a contact always sees the same arm. Pass `variants: null` to clear the split.

    Args:
        id (str):
        body (SetAbTestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SetAbTestResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
