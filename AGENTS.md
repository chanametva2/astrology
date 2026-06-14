# Agent Notes

## Project Shape
- Jekyll site using `jekyll-theme-chirpy ~> 7.5`; no `package.json` at root.
- `_config.yml`: `baseurl: "/astrology"` — all internal links must include this prefix; `timezone: Asia/Bangkok`; `theme_mode: dark`; `lang: en`.
- GitHub Pages via GitHub Actions (`url: "https://chanametva2.github.io"`).
- CI: Ruby 3.4 on ubuntu-latest; `actions/checkout@v6` with `fetch-depth: 0` (needed by `_plugins/posts-lastmod-hook.rb`). Deploys on pushes to `main`/`master`, ignores `.gitignore`, `README.md`, `LICENSE` changes.
- CI runs `htmlproofer` (no-external) as a test step after build.
- Devcontainer available (`.devcontainer/devcontainer.json`) for containerized dev.
- `Gemfile.lock` is **gitignored** — CI resolves deps fresh each build via `bundler-cache: true`.
- `.bundle/config` sets `BUNDLE_WITHOUT: "test"` — html-proofer not installed locally by default.

## Structure
- `_posts/`: 87 blog posts (Thai language), `permalink: /posts/:title/`. Each post has `order:` field numbered chronologically (1–87). Categories: `[Astrology]`.
- `_wiki/`: persistent knowledge collection (23 pages, **Thai language**), rendered under `/wiki/`. Layout `wiki`, front matter keys: `title`, `summary`, `tags`, `sources`, `related`.
- `_tabs/`: static pages (About, Archives, Categories, Tags) plus a `wiki.md` tab pointing at `/wiki/`.
- `_layouts/`: overrides for `home.html` (shows `order` in post list), `post.html` (shows `order` in post title), and `wiki.html` — all copied from Chirpy gem and modified.
- `_data/`: `contact.yml`, `share.yml` — Chirpy config.
- `.gitignore` also excludes `_sass/vendors`, `assets/js/dist`, `node_modules` — Chirpy build artifacts.

## Wiki Maintenance
- Treat `_posts/` as immutable source material; `_wiki/` is the curated knowledge layer.
- Prefer updating existing wiki pages over creating duplicates. New page only when a durable concept lacks one.
- Interlink related wiki pages; update `_wiki/index.md` and append `_wiki/log.md` on every ingest/update/lint.
- Keep concise and encyclopedic; avoid chat-style narration.

## Commands
| Command | Purpose |
|---|---|
| `bundle install` | Install deps (skips `html-proofer` due to `.bundle/config`) |
| `bundle exec jekyll build` | Fast verify |
| `bundle exec jekyll serve` | Dev server with live reload |
| `bash tools/run.sh` | Dev server wrapper (`-p` production, `-H` host) |
| `bash tools/test.sh` | Full production build + htmlproofer (needs `bundle install --with test` first) |
| `JEKYLL_ENV=production bundle exec jekyll build` | Production build (used by CI and `test.sh`) |

## Post Creation Conventions
- Title in front matter; categories `[Astrology]`; tags in English.
- `image.path: /assets/img/posts/<slug>/summary-infographic.jpg` (or `.svg`).
- Source PNG in `temp/` → convert with `magick <src>.png -quality 82 <dst>.jpg`
- Internal links use `baseurl: "/astrology"` prefix.
- Dates use `Asia/Bangkok` timezone; avoid future dates unless intentional.

## Gotchas
- `_plugins/posts-lastmod-hook.rb` derives `last_modified_at` from Git log — metadata unstable before first commit of a post.
- `.gitmodules` declares `assets/lib` as Chirpy submodule but it's **commented out** in CI; may be empty locally.
- `temp/` is gitignored — source materials live there but are not committed.
- Changes only to `.gitignore`, `README.md`, or `LICENSE` are ignored by deploy workflow.
- `opencode.json` exists but is minimal (schema reference only).

## Formatting
- `.editorconfig`: 2-space indent, LF endings, final newline.
- Markdown (`.md`) exempt from `trim_trailing_whitespace` — preserve trailing spaces.
- Shell scripts: LF endings enforced by `.gitattributes`.
