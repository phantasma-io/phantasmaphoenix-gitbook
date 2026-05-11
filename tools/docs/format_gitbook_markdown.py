#!/usr/bin/env python3
"""Conservative formatter for this GitBook Markdown tree."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path
from typing import List


EXCLUDED_DIRS = {".git", "node_modules", "_book"}


def iter_markdown_files(root: Path) -> List[Path]:
    try:
        result = subprocess.run(
            [
                "git",
                "ls-files",
                "--cached",
                "--others",
                "--exclude-standard",
                "--",
                "*.md",
            ],
            cwd=str(root),
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError):
        result = None

    if result is not None:
        return sorted((root / line).resolve() for line in result.stdout.splitlines() if line)

    files: List[Path] = []
    for path in root.rglob("*.md"):
        parts = path.relative_to(root).parts
        if any(part in EXCLUDED_DIRS or part.startswith(".") for part in parts):
            continue
        if path.is_file():
            files.append(path)
    return sorted(files)


def normalize_markdown(raw: bytes) -> bytes:
    text = raw.decode("utf-8")
    if text.startswith("\ufeff"):
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
        description="Normalize GitBook Markdown files without reflowing text."
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
                "Run `just formatter`.",
                file=sys.stderr,
            )
            return 1
        print(f"Formatted {len(changed)} Markdown file(s).")
    else:
        print("No Markdown files needed formatting.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
