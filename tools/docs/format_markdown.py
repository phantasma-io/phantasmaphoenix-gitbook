#!/usr/bin/env python3
"""Conservative formatter for the Markdown pages under content/ and the README."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path
from typing import List


def iter_markdown_files(root: Path) -> List[Path]:
    """Returns the pages under content/ and the README. The theme's own .md templates are left alone."""
    result = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "--", "content", "README.md"],
        cwd=str(root),
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    return sorted(
        (root / line).resolve()
        for line in result.stdout.splitlines()
        if line.endswith(".md") and (root / line).is_file()
    )


def normalize_markdown(raw: bytes) -> bytes:
    text = raw.decode("utf-8")
    if text.startswith("﻿"):
        text = text[1:]

    text = text.replace("\r\n", "\n").replace("\r", "\n")
    if text == "":
        return b""

    lines = text.split("\n")
    lines = [line.rstrip(" \t") for line in lines]
    while lines and lines[-1] == "":
        lines.pop()

    return ("\n".join(lines) + "\n").encode("utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Normalize the Markdown pages without reflowing text."
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="report files that need formatting without modifying them",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path.cwd(),
        help="repository root, defaults to the current directory",
    )
    args = parser.parse_args()

    root = args.root.resolve()
    changed: List[Path] = []

    for path in iter_markdown_files(root):
        try:
            raw = path.read_bytes()
            formatted = normalize_markdown(raw)
        except UnicodeDecodeError as exc:
            print(f"{path.relative_to(root)}: invalid UTF-8: {exc}", file=sys.stderr)
            return 1

        if formatted != raw:
            changed.append(path)
            if not args.check:
                path.write_bytes(formatted)

    if changed:
        for path in changed:
            print(path.relative_to(root))
        if args.check:
            print(
                f"{len(changed)} Markdown file(s) need formatting. "
                "Run `just format`.",
                file=sys.stderr,
            )
            return 1
        print(f"Formatted {len(changed)} Markdown file(s).")
    else:
        print("No Markdown files needed formatting.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
