# Agent Notes

## Project Shape
- Jekyll site using `jekyll-theme-chirpy ~> 7.5`; no `package.json` at root.
- `_config.yml`: `baseurl: "/astrology"` — all internal links must include this prefix; `timezone: Asia/Bangkok`; `theme_mode: dark`.
- GitHub Pages via GitHub Actions (`url: "https://chanametva2.github.io"`).
- CI: Ruby 3.4 on ubuntu-latest; `actions/checkout@v6` with `fetch-depth: 0` (needed by `posts-lastmod-hook.rb`). Deploys on pushes to `main`/`master`, ignores `.gitignore`, `README.md`, `LICENSE` changes.
- `Gemfile.lock`, `.bundle/`, `_site/`, `.jekyll-cache/`, `temp/` are gitignored.
- `.bundle/config` sets `BUNDLE_WITHOUT: "test"` — html-proofer not installed locally by default.
- Devcontainer available (`.devcontainer/devcontainer.json`) for containerized dev.

## Structure
- `_posts/`: blog posts (77 total), `permalink: /posts/:title/`. Each post has `order:` field numbered chronologically (1–77).
- `_wiki/`: persistent knowledge collection (22 pages, **Thai language**), rendered under `/wiki/`. Layout `wiki`, front matter keys: `title`, `summary`, `tags`, `sources`, `related`.
- `_tabs/`: static pages (About, Archives, Categories, Tags).
- `_layouts/`: overrides for `home.html` (shows `order` in post list) and `post.html` (shows `order` in post title) — copied from Chirpy gem and modified.
- `_data/`: `contact.yml`, `share.yml` — Chirpy config.

## Wiki Maintenance
- Treat `_posts/` as immutable source material; `_wiki/` is the curated knowledge layer.
- Prefer updating existing wiki pages over creating duplicates. New page only when a durable concept lacks one.
- Interlink related wiki pages; update `_wiki/index.md` and append `_wiki/log.md` on every ingest/update/lint.
- Keep concise and encyclopedic; avoid chat-style narration.

## Commands
| Command | Purpose |
|---|---|
| `bundle install` | Install deps (`.bundle/config` sets `BUNDLE_WITHOUT: "test"`, skips `html-proofer` locally) |
| `bundle exec jekyll build` | Fast verify |
| `bundle exec jekyll serve` | Dev server |
| `bash tools/run.sh` | Dev server wrapper (`-p` production, `-H` host) |
| `bash tools/test.sh` | Full test (needs `bundle install --with test` first) |

## Post Creation Conventions
- Title in front matter; categories `[Astrology]`; tags in English.
- `image.path: /assets/img/posts/<slug>/summary-infographic.jpg`
- Source PNG in `temp/` → convert with `magick <src>.png -quality 82 <dst>.jpg`
- Internal links use `baseurl: "/astrology"` prefix.
- Dates use `Asia/Bangkok` timezone; avoid future dates unless intentional.

## Gotchas
- `_plugins/posts-lastmod-hook.rb` derives `last_modified_at` from Git log — metadata unstable before first commit of a post.
- `.gitmodules` declares `assets/lib` as Chirpy submodule but it's **commented out** in CI; may be empty locally.
- `temp/` is gitignored — source materials live there but are not committed.
- Changes only to `.gitignore`, `README.md`, or `LICENSE` are ignored by deploy workflow.

## Formatting
- `.editorconfig`: 2-space indent, LF endings, final newline.
- Markdown (`.md`) exempt from `trim_trailing_whitespace` — preserve trailing spaces.
- Shell scripts: LF endings enforced by `.gitattributes`.
