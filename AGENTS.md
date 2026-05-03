# Agent Notes

## Project Shape
- Jekyll site using `jekyll-theme-chirpy ~> 7.5`; no `package.json` at root.
- `_config.yml` is the main config; `baseurl: "/astrology"` — all internal links must include this prefix.
- `timezone: Asia/Bangkok`, `theme_mode: dark`, `lang: en`.
- Content entrypoints: `_posts/` (posts, `permalink: /posts/:title/`) and `_tabs/` (About, Archives, Categories, Tags).
- Theme layouts/assets come from the Chirpy gem; only starter override files live in this repo.
- `_drafts/` may exist for unpublished posts; posts there have `comments: false` by default.

## Setup And Commands
- `bundle install` — `.bundle/config` sets `BUNDLE_WITHOUT: "test"`, so `html-proofer` is skipped locally.
- Fast verify: `bundle exec jekyll build`.
- Dev server: `bundle exec jekyll serve` or `bash tools/run.sh` (supports `-p` for production, `-H` for host).
- Full local test: `bash tools/test.sh` (requires `html-proofer`; run `bundle install --with test` first if missing).
- CI: Ruby 3.4 on ubuntu-latest; `checkout` uses `fetch-depth: 0` (needed by `posts-lastmod-hook.rb`).
- GitHub Pages source must be set to `GitHub Actions`; deploys only on pushes to `main`/`master`.

## Repo-Specific Gotchas
- `_plugins/posts-lastmod-hook.rb` derives `last_modified_at` from Git history; metadata differs before/after commits exist.
- `.gitmodules` declares `assets/lib` as a Chirpy static-assets submodule, but it is **commented out** in CI and may be empty locally.
- `Gemfile.lock`, `.bundle/`, `_site/`, `.jekyll-cache/`, and `.jekyll-metadata` are gitignored; do not treat generated output as source.
- Changes only to `.gitignore`, `README.md`, or `LICENSE` are ignored by the deploy workflow.

## Formatting
- `.editorconfig`: 2-space indent, LF endings, final newline.
- Markdown (`.md`) is **exempt** from `trim_trailing_whitespace` — preserve existing trailing spaces.
- Shell scripts: LF endings enforced by `.gitattributes`.
