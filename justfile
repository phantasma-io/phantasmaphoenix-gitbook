set shell := ["bash", "-eu", "-o", "pipefail", "-c"]

# Hugo, pinned by version and digest.
hugo_image := "ghcr.io/gohugoio/hugo:v0.166.0@sha256:9f3cccb54b48e83a5468cd44f0372b10834b6d8418ef692d9821bb1314761829"

# Hugo runs in a throwaway container as the current user. The entry script of the image is
# skipped, because it runs npm when it finds a package.json. label=disable lets the container
# read the repository on hosts with SELinux. The image sets HUGO_CACHEDIR=/cache, which only the
# image's own user can write, so the cache goes to /tmp for every user.
hugo := "docker run --rm --security-opt label=disable --user \"$(id -u):$(id -g)\" -e HOME=/tmp -e HUGO_CACHEDIR=/tmp/hugo-cache -v \"" + justfile_directory() + ":/project\" -w /project --entrypoint hugo"

default:
    @just --list

formatter *args:
    python3 tools/docs/format_markdown.py {{args}}

format *args:
    python3 tools/docs/format_markdown.py {{args}}

alias f := format

# Checks the Markdown pages.
check:
    git diff --check
    git diff --cached --check
    python3 tools/docs/check_docs.py

# Checks the pages, builds the site into public/ and checks every page and link of it.
build: check
    {{hugo}} {{hugo_image}} --cleanDestinationDir --minify
    python3 tools/docs/check_site.py

# Serves a preview with live reload at http://localhost:1313.
serve:
    {{hugo}} -it -p 127.0.0.1:1313:1313 {{hugo_image}} server --bind 0.0.0.0
