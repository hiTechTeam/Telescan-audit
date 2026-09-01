#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import sys
from pathlib import Path


PACKAGE_ROOT = Path(__file__).resolve().parent.parent
EXCLUDED_NAMES = {"PACKAGE_HASHES.sha256"}
EXCLUDED_PARTS = {"__pycache__", ".DS_Store"}


def included_files() -> list[Path]:
    return sorted(
        path
        for path in PACKAGE_ROOT.rglob("*")
        if path.is_file()
        and path.name not in EXCLUDED_NAMES
        and not EXCLUDED_PARTS.intersection(path.parts)
    )


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    for path in included_files():
        relative = path.relative_to(PACKAGE_ROOT)
        print(f"{sha256(path)}  {relative.as_posix()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

