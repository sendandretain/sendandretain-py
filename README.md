# sendandretain

Python SDK for the [Send & Retain](https://sendandretain.com) API.

Send transactional and lifecycle email, sync contacts, and emit events that drive automations.

The typed surface is **generated** from the same OpenAPI document the API is
served from, with [openapi-python-client](https://github.com/openapi-generators/openapi-python-client)
`0.29.0`. The generated tree is committed and CI fails if it drifts from the
spec, so what you install always matches what the API actually serves.

## Install

```bash
pip install sendandretain
```

Or with [uv](https://docs.astral.sh/uv/):

```bash
uv add sendandretain
```

Requires Python 3.11 or newer.

## Authentication

Mint a key in the dashboard. Every Send & Retain API key starts with `aem_`
and is sent as `Authorization: Bearer aem_…`.

```python
from sendandretain import Client

client = Client(api_key="aem_...")
```

`Client()` reads `$SENDANDRETAIN_API_KEY` when `api_key` is omitted:

```bash
export SENDANDRETAIN_API_KEY=aem_...
```

```python
client = Client()  # picks the key up from the environment
```

### Scopes

Scopes are **ranked, not orthogonal** — a key satisfies any requirement at or
below its own tier:

| Scope | What it can do |
| --- | --- |
| `read` | See messages, contacts, templates and metrics. Never changes anything. |
| `write` | Everything `read` does, plus **sending email** and managing contacts, templates, automations and segments. |
| `admin` | Everything `write` does, plus domains, senders and workspace settings. |

**Sending requires `write`.** A `read` key cannot deliver mail.

A key that lacks the required scope gets `403` with a body naming both the
scope required and the scope the key holds — not a generic denial.

## Quickstart

```python
from sendandretain import Client
from sendandretain.api.emails import send_email
from sendandretain.models import SendEmailBody, SendEmailBodyProps

client = Client(api_key="aem_...")

# One recipient per send, rendered from a published template — there are no
# bulk campaigns on this endpoint.
result = send_email.sync(
    client=client,
    body=SendEmailBody(
        to="person@example.com",
        template="welcome",
        props=SendEmailBodyProps.from_dict({"first_name": "Ada"}),
    ),
)
print(result)  # SendResult(id="msg_...", status=SendResultStatus.QUEUED)
```

### Async

Every operation ships in four flavours: `sync`, `sync_detailed`, `asyncio` and
`asyncio_detailed`. The `_detailed` pair returns the full `Response` with status
code and headers; the plain pair returns just the parsed body.

```python
import asyncio

from sendandretain import Client
from sendandretain.api.contacts import list_contacts


async def main() -> None:
    client = Client(api_key="aem_...")
    contacts = await list_contacts.asyncio(client=client, limit=50)
    print(contacts)


asyncio.run(main())
```

## How it is organised

| Path | What it is |
| --- | --- |
| `sendandretain.Client` | Hand-written (`_convenience.py`). Sets the base URL and `Bearer` prefix, validates the key prefix, reads the env var. |
| `sendandretain.api.*` | Generated. One module per operation, grouped by tag. |
| `sendandretain.models` | Generated. Request and response models as attrs classes. |
| `sendandretain.client` | Generated. `AuthenticatedClient` / `Client`, re-exported as `AuthenticatedClient` / `RawClient`. |
| `sendandretain.errors` | Generated. `UnexpectedStatus`, raised when `raise_on_unexpected_status=True`. |
| `openapi.json` | The vendored spec the client is generated from. |

Only `__init__.py`, `_convenience.py` and `py.typed` are hand-written;
everything else in the package is regenerated wholesale and must not be edited
by hand — `verify_schema_sync.py` is what catches it if it is.

`Client()` returns the generated `AuthenticatedClient`, so anything the
generated code accepts, it accepts. Pass `raise_on_unexpected_status=True` to
turn an undocumented status into an exception rather than `None`:

```python
client = Client(api_key="aem_...", raise_on_unexpected_status=True, timeout=30.0)
```

## Regenerating

The generated tree is committed. Regenerate after changing `openapi.json`:

```bash
uv run python scripts/generate.py
```

And check it is in sync — this is what CI runs:

```bash
uv run python scripts/verify_schema_sync.py
```

`scripts/normalize_spec.py` runs first and rewrites two constructs the generator
cannot model, without changing the contract: anonymous `object`/`array` members
of an `anyOf`/`oneOf` are lifted into named schemas and replaced with a `$ref`,
and a `type` list whose `array` branch carries no `items` is widened to an
unconstrained schema. Both are deterministic, which is what makes the drift
check meaningful.

## Development

```bash
uv sync
uv run ruff check .
uv run ruff format --check .
uv run mypy
uv run python scripts/verify_schema_sync.py
uv run pytest
```

## License

MIT — see [LICENSE](./LICENSE).
