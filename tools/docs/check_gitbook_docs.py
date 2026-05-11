#!/usr/bin/env python3
"""Validate local GitBook Markdown structure without external dependencies."""

from __future__ import annotations

import argparse
import html
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional, Tuple
from urllib.parse import unquote


EXCLUDED_DIRS = {".git", "node_modules", "_book"}
SUMMARY_FILES = ("SUMMARY.md", "SUMMARY-HIDDEN.md")

MARKDOWN_LINK_RE = re.compile(r"!?\[[^\]\n]*\]\(([^)\n]+)\)")
REFERENCE_LINK_RE = re.compile(r"^\s*\[[^\]\n]+\]:\s*(\S+)", re.MULTILINE)
CONTENT_REF_RE = re.compile(r'{%\s*content-ref\s+url=["\']([^"\']+)["\']\s*%}')
HTML_SRC_RE = re.compile(r"<(?:img|source)\b[^>]*\bsrc=[\"']([^\"']+)[\"']", re.I)
COVER_RE = re.compile(r"^cover:\s*(.+?)\s*$", re.MULTILINE)

EXTERNAL_PREFIXES = (
    "http://",
    "https://",
    "mailto:",
    "tel:",
    "ftp://",
    "data:",
    "javascript:",
)

KNOWN_STALE_PATTERNS = (
    (
        re.compile(r"\bPhantasmaRPC\.send_transaction\b"),
        "Python docs should use send_raw_transaction(...) or send_carbon_transaction(...).",
    ),
)


@dataclass(frozen=True)
class Issue:
    path: Path
    line: int
    message: str


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


def line_for_offset(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def strip_code_fences(text: str) -> str:
    output: List[str] = []
    fence_marker: Optional[str] = None

    for line in text.splitlines(keepends=True):
        stripped = line.lstrip()
        marker = None
        if stripped.startswith("```"):
            marker = "```"
        elif stripped.startswith("~~~"):
            marker = "~~~"

        if marker is not None:
            fence_marker = None if fence_marker == marker else marker
            output.append("\n")
            continue

        output.append("\n" if fence_marker else line)

    return "".join(output)


def extract_destination(raw: str) -> str:
    value = html.unescape(raw.strip())
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        value = value[1:-1]
    if value.startswith("<") and ">" in value:
        value = value[1 : value.index(">")]
    else:
        value = value.split()[0] if value.split() else ""
    return unquote(value)


def is_external_or_anchor(target: str) -> bool:
    lowered = target.lower()
    return (
        target == ""
        or target.startswith("#")
        or lowered.startswith(EXTERNAL_PREFIXES)
    )


def resolve_local_target(root: Path, source: Path, raw_target: str) -> Optional[Path]:
    target = extract_destination(raw_target)
    if is_external_or_anchor(target):
        return None

    target = target.split("#", 1)[0].split("?", 1)[0]
    if target == "":
        return None

    if target.startswith("/"):
        resolved = root / target.lstrip("/")
    else:
        resolved = source.parent / target

    return resolved.resolve(strict=False)


def target_exists(path: Path) -> bool:
    if path.exists():
        return True
    if path.is_dir() and (path / "README.md").exists():
        return True
    return False


def check_markdown_bytes(root: Path, path: Path, raw: bytes) -> List[Issue]:
    rel = path.relative_to(root)
    issues: List[Issue] = []

    if raw.startswith(b"\xef\xbb\xbf"):
        issues.append(Issue(rel, 1, "file starts with a UTF-8 BOM"))
    if b"\r" in raw:
        issues.append(Issue(rel, 1, "file contains CRLF or CR line endings"))
    if raw and not raw.endswith(b"\n"):
        issues.append(Issue(rel, raw.count(b"\n") + 1, "file is missing final newline"))

    for number, line in enumerate(raw.splitlines(), start=1):
        if line.endswith((b" ", b"\t")):
            issues.append(Issue(rel, number, "line has trailing whitespace"))

    return issues


def check_front_matter(root: Path, path: Path, text: str) -> List[Issue]:
    rel = path.relative_to(root)
    if not text.startswith("---\n"):
        return []

    for number, line in enumerate(text.splitlines()[1:], start=2):
        if line == "---":
            return []
    return [Issue(rel, 1, "front matter starts with --- but has no closing ---")]


def check_code_fences(root: Path, path: Path, text: str) -> List[Issue]:
    rel = path.relative_to(root)
    issues: List[Issue] = []
    fence_marker: Optional[str] = None
    fence_line = 0

    for number, line in enumerate(text.splitlines(), start=1):
        stripped = line.lstrip()
        marker = None
        if stripped.startswith("```"):
            marker = "```"
        elif stripped.startswith("~~~"):
            marker = "~~~"

        if marker is None:
            continue
        if fence_marker is None:
            fence_marker = marker
            fence_line = number
        elif fence_marker == marker:
            fence_marker = None
            fence_line = 0

    if fence_marker is not None:
        issues.append(Issue(rel, fence_line, f"unclosed {fence_marker} code fence"))
    return issues


def check_links(root: Path, path: Path, text: str) -> List[Issue]:
    rel = path.relative_to(root)
    issues: List[Issue] = []
    searchable = strip_code_fences(text)

    matches: List[Tuple[int, str, str]] = []
    for regex, kind in (
        (MARKDOWN_LINK_RE, "Markdown link"),
        (REFERENCE_LINK_RE, "reference link"),
        (CONTENT_REF_RE, "content-ref"),
        (HTML_SRC_RE, "HTML src"),
        (COVER_RE, "cover"),
    ):
        for match in regex.finditer(searchable):
            matches.append((match.start(1), match.group(1), kind))

    for offset, raw_target, kind in matches:
        target = extract_destination(raw_target)
        resolved = resolve_local_target(root, path, raw_target)
        if resolved is None:
            continue

        try:
            resolved.relative_to(root)
        except ValueError:
            issues.append(
                Issue(
                    rel,
                    line_for_offset(text, offset),
                    f"{kind} points outside the repository: {target}",
                )
            )
            continue

        if not target_exists(resolved):
            issues.append(
                Issue(
                    rel,
                    line_for_offset(text, offset),
                    f"{kind} target does not exist: {target}",
                )
            )

    return issues


def check_content_ref_blocks(root: Path, path: Path, text: str) -> List[Issue]:
    rel = path.relative_to(root)
    issues: List[Issue] = []
    open_line: Optional[int] = None

    for number, line in enumerate(text.splitlines(), start=1):
        if "{% content-ref" in line:
            if open_line is not None:
                issues.append(Issue(rel, number, "nested content-ref block"))
            open_line = number
        elif "{% endcontent-ref %}" in line:
            if open_line is None:
                issues.append(Issue(rel, number, "endcontent-ref without content-ref"))
            open_line = None

    if open_line is not None:
        issues.append(Issue(rel, open_line, "content-ref block has no endcontent-ref"))

    return issues


def check_summary(root: Path, path: Path, text: str) -> List[Issue]:
    rel = path.relative_to(root)
    issues: List[Issue] = []

    for number, line in enumerate(text.splitlines(), start=1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith(" "):
            leading = len(line) - len(line.lstrip(" "))
            if leading % 2 != 0:
                issues.append(Issue(rel, number, "SUMMARY indentation must use two spaces"))
        if "\t" in line[: len(line) - len(line.lstrip())]:
            issues.append(Issue(rel, number, "SUMMARY indentation must not use tabs"))

    return issues


def check_known_stale_patterns(root: Path, path: Path, text: str) -> List[Issue]:
    rel = path.relative_to(root)
    issues: List[Issue] = []
    searchable = strip_code_fences(text)

    for regex, message in KNOWN_STALE_PATTERNS:
        for match in regex.finditer(searchable):
            issues.append(Issue(rel, line_for_offset(text, match.start()), message))

    if rel.as_posix().startswith("developers/sdks/python/"):
        for match in re.finditer(r"\b(?:CarbonReader|BinaryReader)\.remaining\(\)", searchable):
            issues.append(
                Issue(
                    rel,
                    line_for_offset(text, match.start()),
                    "Python reader remaining APIs are properties, not methods.",
                )
            )

    return issues


def check_file(root: Path, path: Path) -> List[Issue]:
    issues: List[Issue] = []
    raw = path.read_bytes()
    issues.extend(check_markdown_bytes(root, path, raw))

    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        rel = path.relative_to(root)
        return issues + [Issue(rel, 1, f"invalid UTF-8: {exc}")]

    issues.extend(check_front_matter(root, path, text))
    issues.extend(check_code_fences(root, path, text))
    issues.extend(check_links(root, path, text))
    issues.extend(check_content_ref_blocks(root, path, text))
    issues.extend(check_known_stale_patterns(root, path, text))

    if path.name in SUMMARY_FILES:
        issues.extend(check_summary(root, path, text))

    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate GitBook Markdown files.")
    parser.add_argument(
        "--root",
        type=Path,
        default=Path.cwd(),
        help="repository root, defaults to the current directory",
    )
    args = parser.parse_args()

    root = args.root.resolve()
    issues: List[Issue] = []

    for path in iter_markdown_files(root):
        issues.extend(check_file(root, path))

    for summary in SUMMARY_FILES:
        if not (root / summary).exists():
            issues.append(Issue(Path(summary), 1, "summary file is missing"))

    if issues:
        for issue in issues:
            print(f"{issue.path}:{issue.line}: {issue.message}", file=sys.stderr)
        print(f"{len(issues)} GitBook validation issue(s) found.", file=sys.stderr)
        return 1

    print("GitBook docs validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
