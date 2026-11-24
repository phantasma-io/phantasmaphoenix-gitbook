#!/usr/bin/env python3
"""Validates the Markdown pages under content/ without external dependencies."""

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


MARKDOWN_LINK_RE = re.compile(r"!?\[[^\]\n]*\]\(([^)\n]+)\)")
REFERENCE_LINK_RE = re.compile(r"^\s*\[[^\]\n]+\]:\s*(\S+)", re.MULTILINE)
HTML_SRC_RE = re.compile(r"<(?:img|source)\b[^>]*\bsrc=[\"']([^\"']+)[\"']", re.I)
GITBOOK_TAG_RE = re.compile(r"\{%")

EXTERNAL_PREFIXES = (
    "http://",
    "https://",
    "mailto:",
    "tel:",
    "ftp://",
    "data:",
    "javascript:",
)

KNOWN_STALE_PATTERNS: tuple[tuple[re.Pattern[str], str], ...] = ()

# Public pages document the product, not how the docs are produced. Internal
# provenance/generation notes (commit hashes, "source baseline" framing) read as
# maintainer metadata and go stale immediately, so they are publication blockers.
META_PROSE_PATTERNS = (
    (
        re.compile(r"(?i)\bsource baseline\b"),
        "Public docs must not reference an internal source baseline.",
    ),
    (
        re.compile(r"(?i)\bsource commit\b"),
        "Public docs must not cite an internal source commit.",
    ),
)


@dataclass(frozen=True)
class Issue:
    path: Path
    line: int
    message: str


def iter_markdown_files(root: Path) -> List[Path]:
    """Returns the pages under content/ and the README of the repository."""
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


def line_for_offset(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


CODE_SPAN_RE = re.compile(r"(`+)(.+?)\1")


def strip_code_fences(text: str) -> str:
    """Returns the text with code blocks emptied and code spans blanked. Each line keeps its
    place, so a line number taken from the result is the line number in the file."""
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

        if fence_marker:
            output.append("\n")
        else:
            output.append(CODE_SPAN_RE.sub(lambda m: " " * len(m.group(0)), line))

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
    return target == "" or target.startswith("#") or lowered.startswith(EXTERNAL_PREFIXES)


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
    """A page needs front matter with a title, because the site shows it as the page heading."""
    rel = path.relative_to(root)
    if rel.parts[0] != "content":
        return []
    if not text.startswith("---\n"):
        return [Issue(rel, 1, "page has no front matter")]
    end = text.find("\n---\n", 4)
    if end < 0:
        return [Issue(rel, 1, "front matter starts with --- but has no closing ---")]
    if not re.search(r"^title:\s*\S", text[4:end], re.MULTILINE):
        return [Issue(rel, 1, "front matter has no title")]
    return []


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


def check_link_target(root: Path, path: Path, target: str) -> Optional[str]:
    """Returns why a local link target is wrong, or None."""
    target = target.split("#", 1)[0].split("?", 1)[0]
    if target == "/":
        return None
    if target.startswith("/"):
        static = root / "static" / target.lstrip("/")
        return None if static.is_file() else f"no file static{target}"
    resolved = (path.parent / target).resolve(strict=False)
    try:
        resolved.relative_to(root / "content")
    except ValueError:
        if not resolved.is_file():
            return f"points outside content/: {target}"
        return None
    if not target.endswith(".md"):
        return f"link to a page by its .md file, not by a folder or a site path: {target}"
    if not resolved.is_file():
        return f"target does not exist: {target}"
    return None


def check_links(root: Path, path: Path, text: str) -> List[Issue]:
    rel = path.relative_to(root)
    issues: List[Issue] = []
    searchable = strip_code_fences(text)

    matches: List[Tuple[int, str, str]] = []
    for regex, kind in (
        (MARKDOWN_LINK_RE, "Markdown link"),
        (REFERENCE_LINK_RE, "reference link"),
        (HTML_SRC_RE, "HTML src"),
    ):
        for match in regex.finditer(searchable):
            matches.append((match.start(1), match.group(1), kind))

    for offset, raw_target, kind in matches:
        target = extract_destination(raw_target)
        if is_external_or_anchor(target):
            continue
        problem = check_link_target(root, path, target)
        if problem:
            issues.append(Issue(rel, line_for_offset(searchable,offset), f"{kind}: {problem}"))

    return issues


def check_gitbook_tags(root: Path, path: Path, text: str) -> List[Issue]:
    rel = path.relative_to(root)
    searchable = strip_code_fences(text)
    return [
        Issue(rel, line_for_offset(searchable,match.start()), "GitBook tag; use Markdown or a GitHub alert")
        for match in GITBOOK_TAG_RE.finditer(searchable)
    ]


def check_known_stale_patterns(root: Path, path: Path, text: str) -> List[Issue]:
    rel = path.relative_to(root)
    issues: List[Issue] = []
    searchable = strip_code_fences(text)

    for regex, message in KNOWN_STALE_PATTERNS:
        for match in regex.finditer(searchable):
            issues.append(Issue(rel, line_for_offset(searchable,match.start()), message))

    if rel.as_posix().startswith("content/developers/sdks/python/"):
        for match in re.finditer(r"\b(?:CarbonReader|BinaryReader)\.remaining\(\)", searchable):
            issues.append(
                Issue(
                    rel,
                    line_for_offset(searchable,match.start()),
                    "Python reader remaining APIs are properties, not methods.",
                )
            )

    return issues


def check_meta_prose(root: Path, path: Path, text: str) -> List[Issue]:
    rel = path.relative_to(root)
    issues: List[Issue] = []
    searchable = strip_code_fences(text)

    for regex, message in META_PROSE_PATTERNS:
        for match in regex.finditer(searchable):
            issues.append(Issue(rel, line_for_offset(searchable,match.start()), message))

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
    issues.extend(check_gitbook_tags(root, path, text))
    issues.extend(check_known_stale_patterns(root, path, text))
    issues.extend(check_meta_prose(root, path, text))
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the Markdown pages of the site.")
    parser.add_argument(
        "--root",
        type=Path,
        default=Path.cwd(),
        help="repository root, defaults to the current directory",
    )
    args = parser.parse_args()

    root = args.root.resolve()
    issues: List[Issue] = []
    files = iter_markdown_files(root)

    for path in files:
        issues.extend(check_file(root, path))

    if issues:
        for issue in issues:
            print(f"{issue.path}:{issue.line}: {issue.message}", file=sys.stderr)
        print(f"{len(issues)} docs validation issue(s) found.", file=sys.stderr)
        return 1

    print(f"Docs validation passed: {len(files)} Markdown files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
