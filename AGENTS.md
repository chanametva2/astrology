# Agent Notes

## Project Shape
- This is a Jekyll site using the `jekyll-theme-chirpy` gem, not a Node app; there is no `package.json` at the repo root.
- Main site configuration is `_config.yml`; the site timezone is `Asia/Bangkok`.
- Content entrypoints are `_posts/` for posts and `_tabs/` for pages such as About, Archives, Categories, and Tags.
- Theme layouts/assets mostly come from the Chirpy gem; only starter override files live in this repo.

## Setup And Commands
- Install Ruby gems with `bundle install`; on this machine `.bundle/config` excludes the `test` group, so `html-proofer` may be absent locally.
- Fast local verification: `bundle exec jekyll build`.
- Local dev server: `bundle exec jekyll serve` or `bash tools/run.sh` in a Unix-like shell/devcontainer.
- Production-style local test, when `html-proofer` is installed: `bash tools/test.sh`.
- CI builds with Ruby 3.4 and runs `bundle exec jekyll b -d "_site${{ steps.pages.outputs.base_path }}"` followed by `bundle exec htmlproofer _site --disable-external ...`.
- GitHub Pages must be configured with `Build and deployment` source set to `GitHub Actions`; otherwise `actions/configure-pages` fails before the Jekyll build starts.

## Repo-Specific Gotchas
- `Gemfile.lock`, `.bundle/`, `_site/`, `.jekyll-cache/`, and `.jekyll-metadata` are ignored; do not treat generated build output or local Bundler config as source changes.
- `.gitmodules` declares `assets/lib` as a Chirpy static-assets submodule, but this checkout may have it empty unless submodules are initialized.
- `_plugins/posts-lastmod-hook.rb` derives `last_modified_at` for posts from Git history, so post metadata can differ before and after commit history exists.
- GitHub Pages deploys only on pushes to `main` or `master`; changes only to `.gitignore`, `README.md`, or `LICENSE` are ignored by the deploy workflow.

## Formatting
- Follow `.editorconfig`: 2-space indentation, LF endings, final newline; Markdown keeps trailing whitespace.
- Shell scripts must keep LF endings per `.gitattributes`.
