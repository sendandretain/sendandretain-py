"""Normalise an OpenAPI document so openapi-python-client can model every union.

openapi-python-client cannot generate a model for an *anonymous* ``object`` or
``array`` member of an ``anyOf``/``oneOf``: union members have to be scalars or
``$ref``s to named schemas. When it meets one it emits
``Invalid property in union <name>`` and drops the whole endpoint.

This pass is a pure refactor of the document, not a change to the contract: each
inline union member is lifted into ``components/schemas`` under a deterministic
name and replaced by a ``$ref`` to it. A ``$ref`` to an identical subschema
validates identically, so the wire contract is untouched.

Deterministic in both name and order, so regenerating from the same input always
produces the same output -- that is what makes the drift check meaningful.
"""

from __future__ import annotations

import re
from typing import Any

UNION_KEYS = ("anyOf", "oneOf")


def _camel(text: str) -> str:
    parts = re.split(r"[^0-9a-zA-Z]+", text)
    return "".join(p[:1].upper() + p[1:] for p in parts if p)


def _needs_hoist(member: Any) -> bool:
    """True for a union member that openapi-python-client cannot name itself."""
    if not isinstance(member, dict) or "$ref" in member:
        return False
    if member.get("type") in ("object", "array"):
        return True
    # An untyped member that still carries object/array structure.
    return any(k in member for k in ("properties", "items", "additionalProperties"))


def _widen_untyped_array(node: dict[str, Any]) -> bool:
    """Drop a ``type`` list whose ``array`` branch carries no ``items``.

    OpenAPI 3.1 allows ``{"type": ["array", "object", "null"]}`` to mean "any
    JSON". openapi-python-client expands that into a union and then cannot model
    the ``array`` branch, because an array with no ``items`` has no element type
    -- so it discards the entire response.

    Dropping ``type`` leaves an unconstrained schema, which is the spelling the
    generator understands for the same intent, and which it renders as ``Any``.
    Applied ONLY when ``array`` appears without ``items``; every other multi-type
    schema (``["object", "null"]`` and friends) generates fine and is left alone.
    """
    kind = node.get("type")
    if not isinstance(kind, list) or "array" not in kind or "items" in node:
        return False
    del node["type"]
    return True


def normalize(document: dict[str, Any]) -> tuple[dict[str, Any], int, int]:
    """Return ``(document, hoisted, widened)``. The input is mutated in place."""
    schemas = document.setdefault("components", {}).setdefault("schemas", {})
    used: set[str] = set(schemas)
    hoisted = 0
    widened = 0

    def unique(base: str) -> str:
        name = base or "Inline"
        if name not in used:
            used.add(name)
            return name
        n = 2
        while f"{name}{n}" in used:
            n += 1
        used.add(f"{name}{n}")
        return f"{name}{n}"

    def visit(node: Any, hint: str) -> None:
        nonlocal hoisted, widened
        if isinstance(node, list):
            for index, item in enumerate(node):
                visit(item, f"{hint}{index}")
            return
        if not isinstance(node, dict):
            return

        if _widen_untyped_array(node):
            widened += 1

        for key in UNION_KEYS:
            members = node.get(key)
            if not isinstance(members, list):
                continue
            for index, member in enumerate(members):
                if not _needs_hoist(member):
                    # Not hoistable itself (a bare `anyOf` wrapper, say), but it
                    # can still nest a union that is -- descend into it, because
                    # the generic walk below deliberately skips union keys.
                    visit(member, f"{hint}Variant{index}")
                    continue
                name = unique(f"{_camel(hint)}Variant{index}")
                schemas[name] = member
                members[index] = {"$ref": f"#/components/schemas/{name}"}
                hoisted += 1
                # Recurse into the member under its new name so nested unions
                # inside it are hoisted too.
                visit(member, name)

        for key, value in list(node.items()):
            if key in UNION_KEYS:
                continue
            next_hint = hint if key in ("properties", "items", "schema") else f"{hint}{_camel(key)}"
            visit(value, next_hint)

    # Named schemas first, each hinted with its own name so a hoisted member is
    # called e.g. `CreateAutomationSchema1Variant0` rather than inheriting a
    # path-shaped prefix. Iterate a snapshot: `visit` grows `schemas` as it goes
    # and recurses into whatever it adds.
    for name in list(schemas):
        visit(schemas[name], _camel(name))

    for path, item in (document.get("paths") or {}).items():
        visit(item, _camel(path.replace("/api/v1", "").replace("{", "").replace("}", "")))

    if "webhooks" in document:
        visit(document["webhooks"], "Webhook")

    return document, hoisted, widened


if __name__ == "__main__":
    import json
    import sys

    src = sys.argv[1]
    with open(src) as fh:
        doc = json.load(fh)
    doc, hoisted, widened = normalize(doc)
    sys.stderr.write(f"hoisted {hoisted} inline union member(s); widened {widened} untyped array union(s)\n")
    json.dump(doc, sys.stdout, indent=2)
