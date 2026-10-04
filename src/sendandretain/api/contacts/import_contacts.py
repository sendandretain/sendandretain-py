from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.import_contacts_body import ImportContactsBody
from ...models.import_contacts_response_200 import ImportContactsResponse200
from ...types import Response


def _get_kwargs(
    *,
    body: ImportContactsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/contacts/import",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | ImportContactsResponse200 | None:
    if response.status_code == 200:
        response_200 = ImportContactsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | ImportContactsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ImportContactsBody,
) -> Response[Error | ImportContactsResponse200]:
    """Bulk import contacts

     Upserts up to 1000 contacts per call. **Partial success is the contract**: every entry is attempted,
    and the response reports how many failed rather than rolling the batch back over one bad address.
    Importing does NOT enroll anyone in anything — automations trigger on events, so a bulk import is
    silent.

    Args:
        body (ImportContactsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ImportContactsResponse200]
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
    body: ImportContactsBody,
) -> Error | ImportContactsResponse200 | None:
    """Bulk import contacts

     Upserts up to 1000 contacts per call. **Partial success is the contract**: every entry is attempted,
    and the response reports how many failed rather than rolling the batch back over one bad address.
    Importing does NOT enroll anyone in anything — automations trigger on events, so a bulk import is
    silent.

    Args:
        body (ImportContactsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ImportContactsResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ImportContactsBody,
) -> Response[Error | ImportContactsResponse200]:
    """Bulk import contacts

     Upserts up to 1000 contacts per call. **Partial success is the contract**: every entry is attempted,
    and the response reports how many failed rather than rolling the batch back over one bad address.
    Importing does NOT enroll anyone in anything — automations trigger on events, so a bulk import is
    silent.

    Args:
        body (ImportContactsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ImportContactsResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ImportContactsBody,
) -> Error | ImportContactsResponse200 | None:
    """Bulk import contacts

     Upserts up to 1000 contacts per call. **Partial success is the contract**: every entry is attempted,
    and the response reports how many failed rather than rolling the batch back over one bad address.
    Importing does NOT enroll anyone in anything — automations trigger on events, so a bulk import is
    silent.

    Args:
        body (ImportContactsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ImportContactsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
