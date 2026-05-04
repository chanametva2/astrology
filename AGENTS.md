# Agent Notes

## Project Shape
- Jekyll site using `jekyll-theme-chirpy ~> 7.5`; no `package.json` at root.
- `_config.yml` is the main config; `baseurl: "/astrology"` — all internal links must include this prefix.
- `timezone: Asia/Bangkok`, `theme_mode: dark`, `lang: en`.
- Content entrypoints: `_posts/` (posts, `permalink: /posts/:title/`) and `_tabs/` (About, Archives, Categories, Tags).
- Wiki entrypoint: `_wiki/` is the persistent knowledge layer, rendered as the `wiki` collection under `/wiki/`.
- Theme layouts/assets come from the Chirpy gem; only starter override files live in this repo.
- `_drafts/` may exist for unpublished posts; posts there have `comments: false` by default.

## Wiki Maintenance Rules
- Treat raw sources as immutable. Do not modify `_posts/`, `_drafts/`, imported files, or other source material unless explicitly asked.
- Treat `_wiki/` as the maintained, compounding markdown knowledge layer.
- Keep blog posts and wiki pages separate: posts are chronological writing; wiki pages are durable topic, entity, and concept summaries.
- Prefer updating existing wiki pages over creating duplicates. Create a new page only when a durable concept lacks a suitable page.
- Every wiki page must use `layout: wiki` and include front matter keys: `title`, `summary`, `tags`, `sources`, and `related`.
- Keep wiki writing concise and encyclopedic. Avoid chat-style narration, speculative claims, and unnecessary duplication from source posts.
- Keep wiki pages interlinked. Add related links between affected pages and use links that respect `baseurl: "/astrology"` when writing explicit HTML or absolute URLs.
- Update `_wiki/index.md` and append `_wiki/log.md` on every wiki ingest, update, or lint pass.
- Preserve Jekyll compatibility: valid YAML front matter, collection-safe filenames, and stable permalinks under `/wiki/`.

## Wiki Ingest Workflow
- Read the source without editing it.
- Identify durable concepts, entities, and topics.
- Create or update wiki pages for those concepts.
- Add source references in wiki front matter.
- Add related links between affected wiki pages.
- Update `_wiki/index.md` with one-line summaries.
- Append a dated entry to `_wiki/log.md` describing the ingest or update.

## Wiki Lint Workflow
- Find duplicate or overlapping wiki pages.
- Find orphan pages with no inbound or related links.
- Find stale claims or contradictions against cited sources.
- Find concepts mentioned repeatedly but lacking dedicated pages.
- Suggest the smallest concrete fixes, then update `_wiki/index.md` and `_wiki/log.md` if changes are made.

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
