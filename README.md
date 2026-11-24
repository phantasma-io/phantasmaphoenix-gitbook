# Phantasma Phoenix documentation

The source of https://docs.phantasma.info. The site is built with [Hugo](https://gohugo.io) and the
[Hextra](https://github.com/imfing/hextra) theme.

## Writing pages

- Pages live in `content/`. A folder with an `_index.md` is a section in the sidebar. The
  `weight` in the front matter of a page sets its place among its neighbours.
- Every page has a `title` in its front matter. The site shows it as the page heading, so the page
  starts with its first paragraph, not with a `#` heading. `linkTitle` sets a shorter name for the
  sidebar.
- A note is a GitHub alert: `> [!NOTE]`, `> [!TIP]`, `> [!IMPORTANT]`, `> [!WARNING]` or
  `> [!CAUTION]`.
- A link to another page is the relative path of its `.md` file, for example
  `[Fees](../economy/fees.md)` or `[SDKs](sdks/_index.md)`.
- Images live in `static/images/` and are linked as `/images/<name>`.

## Building

- `just check` checks the pages.
- `just build` checks the pages, builds the site into `public/` with Hugo v0.166.0 in a
  container, and checks every page and link of the result.
- `just serve` shows a preview at http://localhost:1313.

The theme in `themes/hextra/` is Hextra v0.13.0 (commit `adf732f8`), unchanged: its `assets`,
`data`, `i18n`, `layouts` and `static` folders, `hugo.toml`, `theme.toml` and `LICENSE`.
`layouts/_partials/` replaces two of its partials: the sidebar, which is drawn six levels deep
instead of four, and the icons. The search library FlexSearch v0.8.143 is the file
`assets/js/flexsearch/flexsearch.bundle.min.js`, so the build needs no network.
