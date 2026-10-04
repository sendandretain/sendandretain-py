#!/usr/bin/env python3
"""Fail if the committed client no longer matches the committed spec.

Regenerates into a throwaway directory and compares byte-for-byte against the
generated paths in `src/sendandretain`. Any difference means someone edited generated
code by hand, or changed `openapi.json` without regenerating -- both of which
quietly break the promise that the generated tree IS the contract.

Run it locally with `python scripts/verify_schema_sync.py`; CI runs it on every
push. Fix a failure with `python scripts/generate.py`.
"""

from __future__ import annotations

import filecmp
import pathlib
import sys
import tempfile

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from generate import GENERATED_PATHS, PACKAGE, REPO, generate_into  # noqa: E402, I001

IGNORED_DIRS = {"__pycache__", ".ruff_cache", ".mypy_cache"}


def generated_files(root: pathlib.Path) -> set[pathlib.Path]:
    """Every generator-owned source file under `root`.

    Interpreter and tool artefacts are skipped: they are gitignored and appear
    only once the tree has been imported, so counting them would make the check
    fail purely because the tests happened to run first.
    """
    found: set[pathlib.Path] = set()
    for name in GENERATED_PATHS:
        path = root / name
        if path.is_file():
            found.add(pathlib.Path(name))
        elif path.is_dir():
            found.update(
                child.relative_to(root)
                for child in path.rglob("*")
                if child.is_file() and not IGNORED_DIRS & set(child.relative_to(root).parts) and child.suffix != ".pyc"
            )
    return found


def main() -> int:
    if not PACKAGE.exists():
        print(f"FAIL {PACKAGE.relative_to(REPO)} does not exist. Run: python scripts/generate.py")
        return 1

    with tempfile.TemporaryDirectory(dir=REPO, prefix=".verify-") as tmp:
        fresh = pathlib.Path(tmp) / "client"
        generate_into(fresh)

        committed = generated_files(PACKAGE)
        regenerated = generated_files(fresh)

        missing = sorted(regenerated - committed)
        stale = sorted(committed - regenerated)
        changed = sorted(
            path for path in committed & regenerated if not filecmp.cmp(PACKAGE / path, fresh / path, shallow=False)
        )

    if not (missing or stale or changed):
        print(f"OK generated client is in sync with openapi.json ({len(committed)} files)")
        return 0

    print("FAIL generated client has drifted from openapi.json\n")
    for label, paths in (
        ("missing (regenerate adds)", missing),
        ("stale (regenerate removes)", stale),
        ("changed", changed),
    ):
        if paths:
            print(f"  {label}: {len(paths)}")
            for path in paths[:20]:
                print(f"    {path}")
            if len(paths) > 20:
                print(f"    ... and {len(paths) - 20} more")
    print("\nFix with: python scripts/generate.py")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
