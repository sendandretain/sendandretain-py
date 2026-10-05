#!/usr/bin/env python3
"""Generate `src/sendandretain/_resources.py` — the resource facade — from `openapi.json`.

The generated client under `sendandretain.api` is complete and typed, but every
call reads `send_email.sync(client=..., body=SendEmailBody.from_dict({...}))`.
The facade turns that into `client.emails.send(to=..., template=...)`: one method
per operation, keyword arguments typed from the request schema, the parsed model
returned, and a typed exception raised on any error.

It is generated rather than hand-written for the same reason the client is: 80
operations in a sync and an async flavour is 160 methods, and a hand-kept copy
drifts the first time the spec gains a field. `FACADE` below is the only
hand-maintained part — the method name each operation gets, mirroring the Node
SDK — and `tests/test_facade.py` fails when an operation has no entry.

    uv run python scripts/generate_facade.py           # write
    uv run python scripts/generate_facade.py --check   # exit 1 if stale
"""

from __future__ import annotations

import json
import keyword
import pathlib
import re
import sys
from typing import Any

REPO = pathlib.Path(__file__).resolve().parent.parent
SPEC = REPO / "openapi.json"
PACKAGE = REPO / "src" / "sendandretain"
OUT = PACKAGE / "_resources.py"

# operationId -> "resource.method". Nested resources use dots: "emails.batch.send".
FACADE: dict[str, str] = {
    "sendEmail": "emails.send",
    "listEmails": "emails.list",
    "sendEmailBatch": "emails.batch.send",
    "getMessage": "emails.get",
    "rescheduleEmail": "emails.reschedule",
    "cancelEmail": "emails.cancel",
    "upsertContact": "contacts.upsert",
    "listContacts": "contacts.list",
    "getContact": "contacts.get",
    "deleteContact": "contacts.delete",
    "importContacts": "contacts.import_",
    "listContactEvents": "contacts.events",
    "emitEvent": "events.emit",
    "listSuppressions": "suppressions.list",
    "addSuppression": "suppressions.add",
    "removeSuppression": "suppressions.remove",
    "importSuppressions": "suppressions.import_",
    "createTemplate": "templates.create",
    "listTemplates": "templates.list",
    "getTemplate": "templates.get",
    "updateTemplate": "templates.update",
    "archiveTemplate": "templates.archive",
    "updateTemplateMeta": "templates.update_meta",
    "listTemplateVersions": "templates.list_versions",
    "publishTemplateVersion": "templates.publish",
    "unpublishTemplate": "templates.unpublish",
    "renderTemplate": "templates.render",
    "sendTemplateTest": "templates.test",
    "addTemplateTranslation": "templates.add_translation",
    "createAutomation": "automations.create",
    "listAutomations": "automations.list",
    "getAutomation": "automations.get",
    "updateAutomation": "automations.update",
    "archiveAutomation": "automations.archive",
    "setAutomationStatus": "automations.set_status",
    "duplicateAutomation": "automations.duplicate",
    "backfillMissedEnrollments": "automations.backfill",
    "preflightAutomation": "automations.preflight",
    "listAutomationRuns": "automations.runs",
    "getAutomationMetrics": "automations.metrics",
    "setAbTest": "automations.set_ab_test",
    "promoteAbWinner": "automations.promote_ab_winner",
    "addAutomationSteps": "automations.steps.add",
    "updateAutomationStep": "automations.steps.update",
    "removeAutomationStep": "automations.steps.remove",
    "moveAutomationStep": "automations.steps.move",
    "syncAutomationStepProps": "automations.steps.sync_props",
    "createSegment": "segments.create",
    "listSegments": "segments.list",
    "updateSegment": "segments.update",
    "deleteSegment": "segments.delete",
    "refreshSegmentCount": "segments.refresh_count",
    "createDomain": "domains.create",
    "listDomains": "domains.list",
    "verifyDomain": "domains.verify",
    "deleteDomain": "domains.delete",
    "createSender": "senders.create",
    "listSenders": "senders.list",
    "updateSender": "senders.update",
    "deleteSender": "senders.delete",
    "createWebhookEndpoint": "webhooks.create",
    "listWebhookEndpoints": "webhooks.list",
    "getWebhookEndpoint": "webhooks.get",
    "updateWebhookEndpoint": "webhooks.update",
    "deleteWebhookEndpoint": "webhooks.delete",
    "rotateWebhookSecret": "webhooks.rotate_secret",
    "testWebhookEndpoint": "webhooks.test",
    "listWebhookDeliveries": "webhooks.deliveries.list",
    "replayWebhookDelivery": "webhooks.deliveries.replay",
    "getMetrics": "metrics.get",
    "getMetricsTrends": "metrics.trends",
    "getQueueHealth": "metrics.queue_health",
    "getProjectSettings": "settings.get",
    "updateProjectSettings": "settings.update",
    "getBrand": "settings.get_brand",
    "updateBrand": "settings.update_brand",
    "getOnboardingSteps": "setup.onboarding",
    "getConnectionStatus": "setup.connection",
    "registerProviderWebhook": "setup.register_provider_webhook",
    "registerWebhooks": "setup.register_webhooks",
}

# Deprecated query params are not offered on the facade; the raw client still has them.
SKIP_QUERY = {"before"}

HEADER = '''# Generated by scripts/generate_facade.py from openapi.json — do not edit.
"""The resource facade: one method per API operation. See `_base.py` for the plumbing."""

from __future__ import annotations

import builtins
from collections.abc import AsyncIterator, Iterator
from typing import Any

from . import models
from ._base import AsyncResource, Resource
'''


def snake(name: str) -> str:
    return re.sub(r"(?<!^)(?=[A-Z])", "_", name).replace("-", "_").lower()


def pyname(name: str) -> str:
    n = snake(name) if not name.islower() else name.replace("-", "_")
    return f"{n}_" if keyword.iskeyword(n) or n in {"self", "body", "options"} else n


def py_type(schema: dict[str, Any]) -> str:
    t = schema.get("type")
    if isinstance(t, list):
        types = [x for x in t if x != "null"]
        base = py_type({**schema, "type": types[0]}) if len(types) == 1 else "Any"
        return f"{base} | None" if "null" in t and base != "Any" else base
    return {
        "string": "str",
        "integer": "int",
        "number": "float",
        "boolean": "bool",
        "array": "builtins.list[Any]",  # a resource method named `list` shadows the builtin
        "object": "dict[str, Any]",
    }.get(t or "", "Any")


def resolve(spec: dict[str, Any], node: dict[str, Any]) -> dict[str, Any]:
    while "$ref" in node:
        parts = node["$ref"].removeprefix("#/").split("/")
        cur: Any = spec
        for p in parts:
            cur = cur[p]
        node = cur
    return node


def return_type(module_path: pathlib.Path) -> str:
    """`Error | X | None` from the generated `sync()` -> `models.X`."""
    src = module_path.read_text()
    m = re.search(r"^def sync\(.*?\)\s*->\s*(.+?):\n", src, re.S | re.M)
    if not m:
        return "Any"
    parts = [p.strip() for p in m.group(1).split("|")]
    keep = [p for p in parts if p not in ("Error", "None", "Any")]
    if len(keep) != 1 or not re.fullmatch(r"\w+", keep[0]):
        return "Any"
    return f"models.{keep[0]}"


def item_type(model: str) -> str:
    """The element type of a list response's `data` field."""
    if not model.startswith("models."):
        return "Any"
    cls = model.removeprefix("models.")
    path = PACKAGE / "models" / f"{snake(cls)}.py"
    if not path.exists():
        return "Any"
    m = re.search(r"^\s+data: list\[(\w+)\]", path.read_text(), re.M)
    return f"models.{m.group(1)}" if m else "Any"


def collect(spec: dict[str, Any]) -> list[dict[str, Any]]:
    ops = []
    for methods in spec["paths"].values():
        shared = [resolve(spec, p) for p in methods.get("parameters", [])]
        for method, op in methods.items():
            if method == "parameters":
                continue
            params = shared + [resolve(spec, p) for p in op.get("parameters", [])]
            body = None
            if "requestBody" in op:
                body = resolve(spec, op["requestBody"]["content"]["application/json"]["schema"])
            tag = op["tags"][0].lower()
            module = snake(op["operationId"])
            ops.append(
                {
                    "id": op["operationId"],
                    "summary": op.get("summary", ""),
                    "deprecated": op.get("deprecated", False),
                    "tag": tag,
                    "module": module,
                    "path_params": [p for p in params if p["in"] == "path"],
                    "query": [p for p in params if p["in"] == "query" and p["name"] not in SKIP_QUERY],
                    "idempotent": any(p["in"] == "header" and p["name"] == "Idempotency-Key" for p in params),
                    "body": body,
                    "returns": return_type(PACKAGE / "api" / tag / f"{module}.py"),
                }
            )
    return ops


def method_source(op: dict[str, Any], name: str, is_async: bool) -> list[str]:
    args: list[str] = ["self"]
    for p in op["path_params"]:
        args.append(f"{pyname(p['name'])}: str")
    kw: list[str] = []
    body_lines: list[str] = []
    body = op["body"]
    if body is not None:
        required = set(body.get("required", []))
        props = body.get("properties", {})
        for prop in sorted(props, key=lambda n: n not in required):
            arg = pyname(prop) if not prop.isidentifier() or keyword.iskeyword(prop) else prop
            hint = py_type(props[prop])
            kw.append(f"{arg}: {hint}" if prop in required else f"{arg}: {hint} | None = None")
            body_lines.append(f'"{prop}": {arg}')
    for q in op["query"]:
        hint = py_type(q.get("schema", {}))
        kw.append(f"{pyname(q['name'])}: {hint} | None = None")
    if op["idempotent"]:
        kw.append("idempotency_key: str | None = None")
    sig = ", ".join(args + (["*", *kw] if kw else []))
    ret = op["returns"]
    call = [f"{op['module']}"]
    for p in op["path_params"]:
        call.append(f"{pyname(p['name'])}={pyname(p['name'])}")
    for q in op["query"]:
        call.append(f"{pyname(q['name'])}={pyname(q['name'])}")
    if body is not None:
        call.append("body={" + ", ".join(body_lines) + "}")
    if op["idempotent"]:
        call.append("idempotency_key=idempotency_key")
    d = "async def" if is_async else "def"
    aw = "await " if is_async else ""
    doc = op["summary"] + (" (deprecated)" if op["deprecated"] else "")
    lines = [
        f"    {d} {name}({sig}) -> {ret}:",
        f'        """{doc}."""',
        f"        return {aw}self._call({', '.join(call)})  # type: ignore[no-any-return]",
    ]
    is_cursor_list = any(q["name"] == "cursor" for q in op["query"])
    if is_cursor_list:
        it_name = "iterate" if name == "list" else f"iterate_{name}"
        it_args = ["self"] + [f"{pyname(p['name'])}: str" for p in op["path_params"]]
        it_kw = [k for k in kw if not k.startswith("cursor:")]
        it_sig = ", ".join(it_args + (["*", *it_kw] if it_kw else []))
        fwd = [pyname(p["name"]) for p in op["path_params"]]
        fwd_kw = [f"{pyname(q['name'])}={pyname(q['name'])}" for q in op["query"] if q["name"] != "cursor"]
        item = item_type(ret)
        call_page = f"self.{name}({', '.join([*fwd, *fwd_kw, 'cursor=cursor'])})"
        if is_async:
            lines += [
                "",
                f"    async def {it_name}({it_sig}) -> AsyncIterator[{item}]:",
                '        """Every row of every page, following `next_cursor`."""',
                "        cursor: str | None = None",
                "        while True:",
                f"            page = await {call_page}",
                "            for row in page.data:",
                "                yield row",
                "            cursor = page.next_cursor if isinstance(page.next_cursor, str) else None",
                "            if not page.has_more or not cursor:",
                "                return",
            ]
        else:
            lines += [
                "",
                f"    def {it_name}({it_sig}) -> Iterator[{item}]:",
                '        """Every row of every page, following `next_cursor`."""',
                "        cursor: str | None = None",
                "        while True:",
                f"            page = {call_page}",
                "            yield from page.data",
                "            cursor = page.next_cursor if isinstance(page.next_cursor, str) else None",
                "            if not page.has_more or not cursor:",
                "                return",
            ]
    return lines


def class_name(resource: str, is_async: bool) -> str:
    base = "".join(part.title().replace("_", "") for part in resource.split("."))
    return f"{'Async' if is_async else ''}{base}Resource"


def render(spec: dict[str, Any]) -> str:
    ops = collect(spec)
    missing = [op["id"] for op in ops if op["id"] not in FACADE]
    if missing:
        sys.exit(f"No facade name for: {', '.join(missing)}. Add them to FACADE.")

    by_resource: dict[str, list[tuple[str, dict[str, Any]]]] = {}
    for op in ops:
        resource, _, method = FACADE[op["id"]].rpartition(".")
        by_resource.setdefault(resource, []).append((method, op))
    # Parents of nested resources must exist even with no methods of their own.
    for resource in list(by_resource):
        parts = resource.split(".")
        for i in range(1, len(parts)):
            by_resource.setdefault(".".join(parts[:i]), [])

    imports = sorted({(op["tag"], op["module"]) for op in ops})
    out = [HEADER]
    for tag, module in imports:
        out.append(f"from .api.{tag} import {module}")
    out.append("")

    for is_async in (False, True):
        for resource in sorted(by_resource, key=lambda r: -r.count(".")):
            base = "AsyncResource" if is_async else "Resource"
            out += ["", f"class {class_name(resource, is_async)}({base}):"]
            children = sorted(r for r in by_resource if r.rpartition(".")[0] == resource and r != resource)
            body: list[str] = []
            if children:
                body.append("    def __init__(self, client: Any) -> None:")
                body.append("        super().__init__(client)")
                for child in children:
                    attr = child.rpartition(".")[2]
                    body.append(f"        self.{attr} = {class_name(child, is_async)}(client)")
            for method, op in sorted(by_resource[resource], key=lambda x: x[0]):
                if body:
                    body.append("")
                body += method_source(op, method, is_async)
            out += body or ["    pass"]
            out.append("")

    top = sorted(r for r in by_resource if "." not in r)
    for is_async in (False, True):
        name = "AsyncResources" if is_async else "Resources"
        out += ["", f"class {name}:", '    """Every top-level resource, attached to a client."""', ""]
        out.append("    def __init__(self, client: Any) -> None:")
        for r in top:
            out.append(f"        self.{r} = {class_name(r, is_async)}(client)")
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def main() -> None:
    spec = json.loads(SPEC.read_text())
    source = render(spec)
    if "--check" in sys.argv:
        if not OUT.exists() or OUT.read_text() != source:
            sys.exit("_resources.py is stale. Run: uv run python scripts/generate_facade.py")
        print("OK facade is in sync with openapi.json")
        return
    OUT.write_text(source)
    print(f"wrote {OUT.relative_to(REPO)} ({len(spec['paths'])} paths)")


if __name__ == "__main__":
    main()
