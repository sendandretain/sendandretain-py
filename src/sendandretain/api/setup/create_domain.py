from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_domain_body import CreateDomainBody
from ...models.create_domain_response_201 import CreateDomainResponse201
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CreateDomainBody,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/domains",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateDomainResponse201 | Error | None:
    if response.status_code == 201:
        response_201 = CreateDomainResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 409:
        response_409 = Error.from_dict(response.json())

        return response_409

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateDomainResponse201 | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateDomainBody,
    idempotency_key: str | Unset = UNSET,
) -> Response[CreateDomainResponse201 | Error]:
    """Add a sending domain

     Registers the domain with the project's provider and returns the DNS records to publish, plus a
    recommended DMARC record (`dmarc.recommended_record`) — Gmail/Yahoo bulk-sender rules require DMARC
    on the From domain, but the provider does not, so it's advisory. A human still has to add them at
    the DNS host; then call the verify endpoint. Sends from an unverified domain are refused. Requires
    an `admin`-scope key.

    Args:
        idempotency_key (str | Unset):
        body (CreateDomainBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateDomainResponse201 | Error]
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
    client: AuthenticatedClient,
    body: CreateDomainBody,
    idempotency_key: str | Unset = UNSET,
) -> CreateDomainResponse201 | Error | None:
    """Add a sending domain

     Registers the domain with the project's provider and returns the DNS records to publish, plus a
    recommended DMARC record (`dmarc.recommended_record`) — Gmail/Yahoo bulk-sender rules require DMARC
    on the From domain, but the provider does not, so it's advisory. A human still has to add them at
    the DNS host; then call the verify endpoint. Sends from an unverified domain are refused. Requires
    an `admin`-scope key.

    Args:
        idempotency_key (str | Unset):
        body (CreateDomainBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateDomainResponse201 | Error
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateDomainBody,
    idempotency_key: str | Unset = UNSET,
) -> Response[CreateDomainResponse201 | Error]:
    """Add a sending domain

     Registers the domain with the project's provider and returns the DNS records to publish, plus a
    recommended DMARC record (`dmarc.recommended_record`) — Gmail/Yahoo bulk-sender rules require DMARC
    on the From domain, but the provider does not, so it's advisory. A human still has to add them at
    the DNS host; then call the verify endpoint. Sends from an unverified domain are refused. Requires
    an `admin`-scope key.

    Args:
        idempotency_key (str | Unset):
        body (CreateDomainBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateDomainResponse201 | Error]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateDomainBody,
    idempotency_key: str | Unset = UNSET,
) -> CreateDomainResponse201 | Error | None:
    """Add a sending domain

     Registers the domain with the project's provider and returns the DNS records to publish, plus a
    recommended DMARC record (`dmarc.recommended_record`) — Gmail/Yahoo bulk-sender rules require DMARC
    on the From domain, but the provider does not, so it's advisory. A human still has to add them at
    the DNS host; then call the verify endpoint. Sends from an unverified domain are refused. Requires
    an `admin`-scope key.

    Args:
        idempotency_key (str | Unset):
        body (CreateDomainBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateDomainResponse201 | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
