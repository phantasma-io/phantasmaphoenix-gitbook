set shell := ["bash", "-eu", "-o", "pipefail", "-c"]

default:
    @just --list

formatter *args:
    python3 tools/docs/format_gitbook_markdown.py {{args}}

format *args:
    python3 tools/docs/format_gitbook_markdown.py {{args}}

alias f := format

build:
    git diff --check
    git diff --cached --check
    python3 tools/docs/check_gitbook_docs.py

check: build
