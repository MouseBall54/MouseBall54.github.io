# Repository Guidelines

This guide is the single operating reference for coding agents and contributors working on MouseBall54's Toolbox. It follows the direction of the Karpathy-inspired agent rules from `multica-ai/andrej-karpathy-skills`: think before editing, prefer simple changes, touch only what the task requires, and verify the result.

## Agent Operating Principles

### Think Before Editing

Do not guess silently. State assumptions when a request is ambiguous, and ask only when the answer cannot be found from the repository. If a simpler path exists, use it and explain the tradeoff briefly.

### Simplicity First

This is a Jekyll content site, not an application framework. Avoid new abstractions, generators, or workflows unless they clearly reduce repeated work. Prefer small Markdown, YAML, Liquid, or Sass edits over broad rewrites.

### Surgical Changes

Every changed line should connect to the task. Do not reformat unrelated posts, theme files, or generated assets. If you find unrelated dead Minimal Mistakes leftovers, either leave a note or remove them only when the task explicitly includes cleanup.

### Goal-Driven Verification

For non-trivial work, define success before editing. Examples:

- Content change: both Korean and English posts exist, front matter is valid, images render.
- Layout change: the affected page renders locally and does not break categories, tags, or search.
- Cleanup: removed files are not referenced by `_config.yml`, workflows, navigation, or build commands.

## Project Direction

- The site is a GitHub Pages blog for developer troubleshooting content and web tool introductions.
- Easy Labeling is the representative tool. Related posts should focus on features, usage, and practical labeling workflows.
- Early traffic content is centered on Python, JavaScript, Java, and Git troubleshooting.
- The initial 120 troubleshooting topics across Python, JavaScript, Java, and Git are complete. New topics should continue the same paired-language and verification standards.

## Project Structure

- `_config.yml`: global Jekyll settings, defaults, plugins, comments, analytics, search.
- `_posts/ko` and `_posts/en`: paired Korean and English posts.
- `_pages`: static pages such as categories, tags, and Easy Labeling introduction.
- `_data/navigation.yml`: top navigation and category sidebar.
- `_layouts`, `_includes`, `_sass`: checked-in Minimal Mistakes theme templates and customizations.
- `assets` and `images`: CSS/JS entrypoints, profile assets, header images, post screenshots.

## Development Commands

- `bundle install`: install Ruby/Jekyll dependencies.
- `bundle exec jekyll serve`: run the site locally.
- `bundle exec jekyll build --trace`: validate the production build.
- `python update_posts.py`: add missing `lang` and `translation_id` fields to paired posts.
- `rake js`: rebuild `assets/js/main.min.js` after JavaScript source edits.

## Content Rules

Create posts in Korean and English together. Current paths are:

- `_posts/ko/YYYY-MM-DD-topic-slug.md`
- `_posts/en/YYYY-MM-DD-topic-slug.md`

Use the same date and matching `translation_id` values for paired posts. Troubleshooting posts should include `title`, `date`, `header`, `excerpt`, `lang`, `translation_id`, `categories`, and English tags. Use 3-5 tags, all in English.

Write in short, clear sentences, but make the explanation detailed enough to be useful. Keep Korean prose natural and keep programming error names, API names, commands, library names, and terms such as `ModuleNotFoundError`, `Promise`, and `git rebase` in English when clearer. Avoid AI-translation tone, inflated marketing copy, and empty conclusions.

When practical, record brief work history in the relevant post or PR description. Do not depend on a separate project log file.

## Front Matter Standards

Troubleshooting posts normally use this structure:

```yaml
title: >
  How to Fix "Permission denied (publickey)" Error with Git on Windows
date: 2025-07-22T22:00:00+09:00
header:
  teaser: /images/header_images/overlay_image_git.png
  overlay_image: /images/header_images/overlay_image_git.png
  overlay_filter: 0.5
excerpt: >
  Fix Git's "Permission denied (publickey)" error on Windows.
lang: en
translation_id: git-permission-denied-publickey
categories:
  - en_Troubleshooting
tags:
  - Git
  - SSH
  - Windows
```

Use YAML block scalars such as `>` or `|` when titles or excerpts contain quotes. Current troubleshooting header images are:

- Python: `/images/header_images/overlay_image_python.png`
- Java: `/images/header_images/overlay_image_java.png`
- JavaScript: `/images/header_images/overlay_image_js.png`
- Git: `/images/header_images/overlay_image_git.png`

Current content categories are:

- `ko_Troubleshooting`
- `en_Troubleshooting`
- `ko_easy_labeling`
- `en_easy_labeling`

## Article Structure

Troubleshooting posts usually follow this flow:

1. Problem summary
2. Cause
3. Quick fix
4. Example code or commands
5. How to verify
6. Related mistakes or prevention tips

Easy Labeling posts usually follow this flow:

1. What work the tool reduces
2. Main features
3. Usage steps
4. Real screens or examples
5. Related links

## Images and Links

- Store post images under `images/<post-slug>/` when practical.
- Always use meaningful alt text.
- Use `https://mouseball54.github.io/easy_labeling/` for the Easy Labeling launch link.
- Check internal links against the deployed URL shape so category, tag, and tool links do not break.

## Style

Follow `.editorconfig`: two-space indentation, LF line endings, UTF-8, and no trailing whitespace except where Markdown needs it. Match existing Liquid, YAML, and Sass style. Do not edit minified JavaScript directly unless the source is unavailable.

## Verification

Before publishing or finishing non-trivial content work, check:

- `bundle exec jekyll build --trace` succeeds.
- Korean and English posts have matching `translation_id` values.
- The affected category pages include the new posts.
- Image paths and links are valid.
- The writing uses the intended short, clear style.

## Pull Requests and Commits

Use scoped commits. Existing history uses `(Add)`, `(Fix)`, `(Mod)`, and `docs:`; prefer clear messages such as:

`docs: Git 트러블슈팅 포스트 추가`

For post work, write commit messages in Korean when practical. If a commit message file is useful, use `git commit -F <file>`.

PRs should include a summary, affected pages or posts, verification command output, and screenshots for visual changes. New content must update both language versions.
