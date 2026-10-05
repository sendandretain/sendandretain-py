# sendandretain

The official Python SDK for the [Send & Retain](https://sendandretain.com) email API — send email,
sync contacts, emit events that drive automations, and verify webhooks. Sync and asyncio.

```bash
pip install sendandretain    # or: uv add sendandretain
```

Python 3.11 or newer.

## Quickstart

```python
from sendandretain import SendAndRetain

client = SendAndRetain()  # reads SENDANDRETAIN_API_KEY

email = client.emails.send(
    to="jane@acme.com",
    template="welcome",
    props={"firstName": "Jane"},
)
print(email.id)  # queued — delivery is reported by webhook
```

A send is accepted with `202` and delivered in the background. Follow it with
`client.emails.get(email.id)` or, better, a [webhook](#webhooks).

## Authentication

Mint a key in the dashboard. Every Send & Retain API key starts with `aem_`
and is sent as `Authorization: Bearer aem_…`.

```python
client = SendAndRetain("aem_...")  # or set SENDANDRETAIN_API_KEY and pass nothing
```

### Scopes and the send grant

Authorization has two independent axes.

The **scope** is ranked — a key satisfies any requirement at or below its own
tier:

| Scope | What it can do |
| --- | --- |
| `read` | See messages, contacts, templates and metrics. Never changes anything, and cannot send. |
| `write` | Everything `read` does, plus managing contacts, templates, automations, segments and suppressions. |
| `admin` | Everything `write` does, plus domains, senders and workspace settings. |

The **send grant** is a separate boolean, not a rung. Delivering mail to a real
inbox — `send_email`, `send_email_batch`, `reschedule_email` and
`send_template_test` — needs `write` **and** the grant; a key can hold `admin`
and still be refused there. The dashboard mints that combination as
**Send + manage**; **Manage only** is the same rung with the grant withheld.

A key that falls short gets `403`, and the body says which axis refused it:
`required_scope` / `key_scope` for the tier, or `required_grant` when the tier
was enough but the key lacks the grant — not a generic denial.

## Errors

Methods return the parsed model and raise on any failure. Every exception is a
`SendAndRetainError` carrying `code`, `status`, `request_id` and the full error `body`:

```python
from sendandretain import NotFoundError, QuotaExceededError, SendAndRetainError

try:
    client.templates.get("welcome")
except NotFoundError:
    ...
except QuotaExceededError:  # 429 daily_cap / monthly_cap — a quota, not a throttle
    ...
except SendAndRetainError as e:
    print(e.code, e.request_id)  # quote request_id to support
```

| Exception | When |
| --- | --- |
| `InvalidRequestError` | 400 / 422 — fix the request; nothing changed |
| `AuthenticationError` | 401 — missing, invalid or revoked key |
| `PermissionDeniedError` | 403 — see `e.body["required_scope"]` / `["required_grant"]` |
| `NotFoundError` | 404 |
| `ConflictError` | 409 — an idempotency conflict, or the resource's state forbids it |
| `RateLimitError` | 429 `rate_limited`, after the SDK's retries |
| `QuotaExceededError` | 429 `daily_cap` / `monthly_cap` — never retried |
| `APIError` | anything else, 5xx included |
| `APIConnectionError` | no response arrived |

## Idempotency

Pass `idempotency_key` on any create to make it safe to retry:

```python
client.emails.send(to="jane@acme.com", template="welcome", idempotency_key="welcome/user_42")
```

The same key and body replays the first result instead of sending again; a different body with the
same key raises `ConflictError`. Keys live 24 hours. When you pass none, the SDK generates one per
call, so its own retries can never send twice.

## Retries and timeouts

`408`, `429` and `5xx` responses, and requests that get no response, are retried twice with
exponential backoff and jitter, honouring `Retry-After` — but only when safe: reads, updates,
deletes, and creates carrying an idempotency key (all of them, by default). A sending quota is
never retried.

```python
client = SendAndRetain(max_retries=4, timeout=10.0)
```

## Pagination

Lists return a page — `.data`, `.has_more`, `.next_cursor`. `iterate` walks every page:

```python
for email in client.emails.iterate(status="bounced"):
    print(email.to)

page = client.contacts.list(limit=100)
if page.has_more:
    page = client.contacts.list(limit=100, cursor=page.next_cursor)
```

Under a resource: `client.contacts.iterate_events(contact_id)`,
`client.automations.iterate_runs(automation_id)`, `client.webhooks.deliveries.iterate(endpoint_id)`.

## Async

`AsyncSendAndRetain` has the same resources, every method awaitable:

```python
from sendandretain import AsyncSendAndRetain

async with AsyncSendAndRetain() as client:
    email = await client.emails.send(to="jane@acme.com", template="welcome")
    async for contact in client.contacts.iterate():
        ...
```

## Webhooks

Subscribe an endpoint and store the secret it returns — it is shown once:

```python
endpoint = client.webhooks.create(
    url="https://acme.com/webhooks/sendandretain",
    event_types=["email.delivered", "email.bounced", "email.complained"],
)
```

Verify every delivery against the **raw** body, then act on `event["type"]`:

```python
from sendandretain import WebhookVerificationError, verify_webhook

# Flask: request.get_data() · FastAPI: await request.body() · Django: request.body
try:
    event = verify_webhook(raw_body, request.headers, secret=os.environ["SENDANDRETAIN_WEBHOOK_SECRET"])
except WebhookVerificationError:
    return "", 400

if event["type"] == "email.bounced":
    ...
```

Deliveries are [Standard Webhooks](https://www.standardwebhooks.com), at-least-once and unordered:
dedupe on `event["id"]`, order on `event["occurred_at"]`. Verification is standard library only.

## Resources

| Resource | Methods |
| --- | --- |
| `emails` | `send`, `get`, `list`, `iterate`, `reschedule`, `cancel`, `batch.send` |
| `contacts` | `upsert`, `get`, `list`, `iterate`, `delete`, `import_`, `events`, `iterate_events` |
| `events` | `emit` |
| `suppressions` | `list`, `iterate`, `add`, `remove`, `import_` |
| `templates` | `create`, `list`, `get`, `update`, `update_meta`, `archive`, `list_versions`, `publish`, `unpublish`, `render`, `test`, `add_translation` |
| `automations` | `create`, `list`, `get`, `update`, `archive`, `set_status`, `duplicate`, `backfill`, `preflight`, `runs`, `iterate_runs`, `metrics`, `set_ab_test`, `promote_ab_winner`, `steps.{add,update,remove,move,sync_props}` |
| `segments` | `create`, `list`, `update`, `delete`, `refresh_count` |
| `domains` | `create`, `list`, `verify`, `delete` |
| `senders` | `create`, `list`, `update`, `delete` |
| `webhooks` | `create`, `list`, `get`, `update`, `delete`, `rotate_secret`, `test`, `deliveries.list`, `deliveries.iterate`, `deliveries.replay` |
| `metrics` | `get`, `trends`, `queue_health` |
| `settings` | `get`, `update`, `get_brand`, `update_brand` |
| `setup` | `onboarding`, `connection`, `register_provider_webhook` |

Every API operation has a method; a test fails if one is missing. Body fields are keyword arguments
with their wire names, except `from`, which is `from_`.

## How it is organised

| Path | What it is |
| --- | --- |
| `SendAndRetain`, `AsyncSendAndRetain` | `_client.py`, hand-written. Key, base URL, transport. |
| resource methods | `_resources.py`, **generated** from `openapi.json` by `scripts/generate_facade.py`. |
| `sendandretain.api.*`, `sendandretain.models` | **Generated** by openapi-python-client `0.29.0`: one module per operation, attrs models. Use them directly for anything the facade does not shape your way; `client.raw` is the `AuthenticatedClient` they take. |
| `_runtime.py` | The transport — retries, idempotency, User-Agent. Synced from the Send & Retain source tree. |
| `_exceptions.py`, `_webhooks.py`, `_base.py` | Hand-written. |
| `openapi.json` | The vendored spec everything is generated from. |

`sendandretain.Client` — the 0.1 factory returning the generated `AuthenticatedClient` — still works.

## Regenerating

The generated tree and the facade are committed. Regenerate both after changing `openapi.json`:

```bash
uv run python scripts/generate.py
```

And check both are in sync — this is what CI runs:

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
