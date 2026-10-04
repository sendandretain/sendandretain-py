from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.verify_domain_response_200 import VerifyDomainResponse200
from ...types import Response


def _get_kwargs(
    domain: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/domains/{domain}/verify".format(
            domain=quote(str(domain), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | VerifyDomainResponse200 | None:
    if response.status_code == 200:
        response_200 = VerifyDomainResponse200.from_dict(response.json())

        return response_200

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
) -> Response[Error | VerifyDomainResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    domain: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | VerifyDomainResponse200]:
    """Verify a domain

     Asks the provider to re-check DNS. Poll after publishing the records — `verified: false` just means
    DNS hasn't propagated yet, which is normal for the first several minutes. Also re-checks DMARC and
    returns the advisory `dmarc` block; DMARC never blocks verification.

    Args:
        domain (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | VerifyDomainResponse200]
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
    client: AuthenticatedClient | Client,
) -> Error | VerifyDomainResponse200 | None:
    """Verify a domain

     Asks the provider to re-check DNS. Poll after publishing the records — `verified: false` just means
    DNS hasn't propagated yet, which is normal for the first several minutes. Also re-checks DMARC and
    returns the advisory `dmarc` block; DMARC never blocks verification.

    Args:
        domain (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | VerifyDomainResponse200
    """

    return sync_detailed(
        domain=domain,
        client=client,
    ).parsed


async def asyncio_detailed(
    domain: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | VerifyDomainResponse200]:
    """Verify a domain

     Asks the provider to re-check DNS. Poll after publishing the records — `verified: false` just means
    DNS hasn't propagated yet, which is normal for the first several minutes. Also re-checks DMARC and
    returns the advisory `dmarc` block; DMARC never blocks verification.

    Args:
        domain (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | VerifyDomainResponse200]
    """

    kwargs = _get_kwargs(
        domain=domain,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    domain: str,
    *,
    client: AuthenticatedClient | Client,
) -> Error | VerifyDomainResponse200 | None:
    """Verify a domain

     Asks the provider to re-check DNS. Poll after publishing the records — `verified: false` just means
    DNS hasn't propagated yet, which is normal for the first several minutes. Also re-checks DMARC and
    returns the advisory `dmarc` block; DMARC never blocks verification.

    Args:
        domain (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | VerifyDomainResponse200
    """

    return (
        await asyncio_detailed(
            domain=domain,
            client=client,
        )
    ).parsed
