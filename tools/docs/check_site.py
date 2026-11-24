#!/usr/bin/env python3
"""Checks the site that Hugo built into public/.

It fails when a page of content/ was not built, when a link or a source inside the site points
to a file that does not exist, to an anchor that the page does not have or to a Markdown file,
or when the text of a page still holds a GitBook tag or a Hugo shortcode that was not rendered.

Usage: python3 tools/docs/check_site.py [--root <repository>]
Exit 0: no problem. Exit 1: one line per problem.
"""

from __future__ import annotations

import argparse
import posixpath
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

SITE_URL = "https://docs.phantasma.info/"
LEFTOVERS = ("{%", "{{<", "{{%")


class Page(HTMLParser):
    """Collects the ids, the links and the visible text of one HTML file."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: set[str] = set()
        self.links: list[str] = []
        self.text: list[str] = []
        self._skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self._skip += 1
        for name, value in attrs:
            if name in ("id", "name") and value:
                self.ids.add(value)
            if name in ("href", "src") and value:
                self.links.append(value)

    def handle_endtag(self, tag):
        if tag in ("script", "style") and self._skip:
            self._skip -= 1

    def handle_data(self, data):
        if not self._skip:
            self.text.append(data)


def expected_output(page: Path, content: Path) -> str:
    """Returns the path under public/ that Hugo writes for a content file."""
    rel = page.relative_to(content).as_posix().lower()
    folder, name = posixpath.split(rel)
    if name in ("_index.md", "index.md"):
        return posixpath.join(folder, "index.html")
    return posixpath.join(folder, name[: -len(".md")], "index.html")


def target_file(public: Path, url_path: str) -> Path:
    path = public / url_path.lstrip("/")
    if url_path.endswith("/") or path.is_dir():
        path = path / "index.html"
    return path


def main() -> int:
    parser = argparse.ArgumentParser(description="Check the built site in public/.")
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="repository root")
    args = parser.parse_args()
    root = args.root.resolve()
    public = root / "public"
    content = root / "content"
    problems: list[str] = []

    if not public.is_dir():
        print("public/ does not exist; build the site first", file=sys.stderr)
        return 1

    for page in sorted(content.rglob("*.md")):
        output = expected_output(page, content)
        if not (public / output).is_file():
            problems.append(f"{page.relative_to(root)}: not built (expected public/{output})")

    parsed: dict[Path, Page] = {}

    def parse(path: Path) -> Page:
        if path not in parsed:
            page = Page()
            page.feed(path.read_text(encoding="utf-8"))
            parsed[path] = page
        return parsed[path]

    html_files = sorted(public.rglob("*.html"))
    for path in html_files:
        page = parse(path)
        rel = path.relative_to(public).as_posix()
        text = "".join(page.text)
        for marker in LEFTOVERS:
            if marker in text:
                problems.append(f"public/{rel}: the text holds {marker!r}")
        base = "/" + posixpath.dirname(rel) + "/" if posixpath.dirname(rel) else "/"
        for link in page.links:
            if link.startswith(SITE_URL):
                link = "/" + link[len(SITE_URL):]
            parts = urlsplit(link)
            if parts.scheme or link.startswith("//") or not (parts.path or parts.fragment):
                continue
            url_path = unquote(parts.path) if parts.path else "/" + rel
            if url_path.endswith(".md"):
                # Hugo writes a Markdown copy next to each page, so such a link would point to a
                # file that exists. A link to a page that Hugo could not resolve looks like this.
                problems.append(f"public/{rel}: {link}: link to a Markdown file, not to a page")
                continue
            if not url_path.startswith("/"):
                url_path = posixpath.normpath(posixpath.join(base, url_path)) + ("/" if url_path.endswith("/") else "")
            target = path if not parts.path else target_file(public, url_path)
            if not target.is_file():
                problems.append(f"public/{rel}: {link}: no such file")
                continue
            if parts.fragment and target.suffix == ".html" and unquote(parts.fragment) not in parse(target).ids:
                problems.append(f"public/{rel}: {link}: no such anchor")

    for problem in problems:
        print(problem, file=sys.stderr)
    if problems:
        print(f"{len(problems)} problem(s) in the built site.", file=sys.stderr)
        return 1
    print(f"Site check passed: {len(html_files)} HTML files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
