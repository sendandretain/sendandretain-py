from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_domain_response_200 import DeleteDomainResponse200
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    domain: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v1/domains/{domain}".format(
            domain=quote(str(domain), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DeleteDomainResponse200 | Error | None:
    if response.status_code == 200:
        response_200 = DeleteDomainResponse200.from_dict(response.json())

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

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DeleteDomainResponse200 | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    domain: str,
    *,
    client: AuthenticatedClient,
) -> Response[DeleteDomainResponse200 | Error]:
    """Delete a domain

     Removes the sending domain from this project — its sender identities go with it — and from the
    provider account, unless another project still uses the provider domain (then it's left in place and
    `warning` says so). Refused while the project's default sender is on this domain and other senders
    exist elsewhere. Templates and automations sending from the domain will fail until it's re-added and
    verified. Requires an `admin`-scope key.

    Args:
        domain (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteDomainResponse200 | Error]
    """

    kwargs = _get_kwargs(
        domain=domain,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    domain: str,
    *,
    client: AuthenticatedClient,
) -> DeleteDomainResponse200 | Error | None:
    """Delete a domain

     Removes the sending domain from this project — its sender identities go with it — and from the
    provider account, unless another project still uses the provider domain (then it's left in place and
    `warning` says so). Refused while the project's default sender is on this domain and other senders
    exist elsewhere. Templates and automations sending from the domain will fail until it's re-added and
    verified. Requires an `admin`-scope key.

    Args:
        domain (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteDomainResponse200 | Error
    """

    return sync_detailed(
        domain=domain,
        client=client,
    ).parsed


async def asyncio_detailed(
    domain: str,
    *,
    client: AuthenticatedClient,
) -> Response[DeleteDomainResponse200 | Error]:
    """Delete a domain

     Removes the sending domain from this project — its sender identities go with it — and from the
    provider account, unless another project still uses the provider domain (then it's left in place and
    `warning` says so). Refused while the project's default sender is on this domain and other senders
    exist elsewhere. Templates and automations sending from the domain will fail until it's re-added and
    verified. Requires an `admin`-scope key.

    Args:
        domain (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteDomainResponse200 | Error]
    """

    kwargs = _get_kwargs(
        domain=domain,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    domain: str,
    *,
    client: AuthenticatedClient,
) -> DeleteDomainResponse200 | Error | None:
    """Delete a domain

     Removes the sending domain from this project — its sender identities go with it — and from the
    provider account, unless another project still uses the provider domain (then it's left in place and
    `warning` says so). Refused while the project's default sender is on this domain and other senders
    exist elsewhere. Templates and automations sending from the domain will fail until it's re-added and
    verified. Requires an `admin`-scope key.

    Args:
        domain (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteDomainResponse200 | Error
    """

    return (
        await asyncio_detailed(
            domain=domain,
            client=client,
        )
    ).parsed
