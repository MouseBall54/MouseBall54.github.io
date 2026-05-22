# Contributing

This repository powers MouseBall54's Toolbox, a Jekyll blog for developer troubleshooting guides and Easy Labeling documentation.

Read `AGENTS.md` before making changes. Keep edits small, project-specific, and verified.

## Content Changes

- Add Korean and English posts together.
- Use matching dates, slugs, and `translation_id` values.
- Put Korean posts in `_posts/ko` and English posts in `_posts/en`.
- Keep tags in English.
- Store post images under `images/<post-slug>/` when practical.

## Site Changes

- Keep Minimal Mistakes customizations scoped to `_layouts`, `_includes`, `_sass`, `assets`, and `_data`.
- Do not edit generated output in `_site`.
- Do not commit `node_modules`, `.jekyll-cache`, `vendor/bundle`, or other local build artifacts.

## Pull Requests

Before opening a pull request:

1. Run `bundle exec jekyll build --trace`.
2. Check affected pages locally with `bundle exec jekyll serve`.
3. Follow the content rules in `AGENTS.md`.
4. Include screenshots for layout or visual changes.
