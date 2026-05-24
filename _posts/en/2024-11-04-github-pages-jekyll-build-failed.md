---
typora-root-url: ../
layout: single
title: >
  Fix GitHub Pages Jekyll Build Failed
seo_title: >
  Fix GitHub Pages Jekyll Build Failed
date: 2024-11-04T07:44:00+09:00
last_modified_at: 2026-05-23T23:59:59+09:00
lang: en
translation_id: github-pages-jekyll-build-failed
header:
   teaser: /images/2026-05-23-github-pages-jekyll-build-failed/github-pages-jekyll-build-failed-hero.png
   overlay_image: /images/2026-05-23-github-pages-jekyll-build-failed/github-pages-jekyll-build-failed-hero.png
   overlay_filter: 0.5
   image_description: >
     Visual guide explaining Fix GitHub Pages Jekyll Build Failed.
excerpt: >
  Fix GitHub Pages Jekyll build failed errors by checking Pages workflow logs, _config.yml YAML, front matter dates, includes, plugins, Sass, and local Jekyll builds.
seo_description: >
  Fix GitHub Pages Jekyll build failed errors by checking Pages workflow logs, _config.yml YAML, front matter dates, includes, plugins, Sass, and local Jekyll builds.
categories:
  - en_Troubleshooting
tags:
  - GitHubPages
  - Jekyll
  - GitHub
  - Build
---

## Problem

GitHub Pages fails to publish a Jekyll site:

![Fix GitHub Pages Jekyll Build Failed explanatory image](/images/2026-05-23-github-pages-jekyll-build-failed/github-pages-jekyll-build-failed-hero.png)

```text
Pages build and deployment failed
```

or:

```text
Error: Process completed with exit code 1
```

The message may mention `_config.yml`, front matter, Sass, an include file, a plugin, or a post date.
The fastest fix is to read the Pages workflow log and reproduce the Jekyll build locally.

## Cause

Common causes include:

- `_config.yml` has invalid YAML.
- A post filename or front matter date is invalid.
- A file uses invalid UTF-8 encoding.
- A Liquid tag is not closed.
- An include references a missing file in `_includes`.
- Sass or SCSS syntax is invalid.
- The site uses a plugin that GitHub Pages does not support in that build mode.
- The configured publishing source is wrong.
- The local Ruby/Bundler environment differs from GitHub Pages.

GitHub recommends GitHub Actions for deploying and automating Pages sites.
That also means the build log is usually available in the repository's Actions tab.

## Quick Diagnosis

Open the failed Pages build:

1. Go to the repository on GitHub.
2. Open the **Actions** tab.
3. Open the failed **Pages build and deployment** run.
4. Open the failed job.
5. Expand the failed step.
6. Read the first file path and line number mentioned in the log.

Then run a local build:

```bash
bundle install
bundle exec jekyll build --trace
```

If you do not use Bundler yet, install it and keep a `Gemfile`.
Bundler makes the Ruby gem set more predictable and reduces environment-related Jekyll errors.

## Step-by-Step Fix

### 1. Fix _config.yml YAML Errors

If the log mentions `_config.yml`, check YAML syntax first.

Common mistakes:

```yaml
title: My site: notes
```

Use quotes when a value contains a colon:

```yaml
title: "My site: notes"
```

Also check:

- spaces instead of tabs
- a space after each `:`
- valid UTF-8 text
- correct indentation
- block scalars for long text

Example:

```yaml
description: >
  A short description that can span multiple lines
  without breaking YAML parsing.
```

### 2. Fix Post Dates and Front Matter

Jekyll posts must use valid dates in filenames:

```text
_posts/en/2026-05-23-example-post.md
```

The front matter date should also be valid:

```yaml
date: 2026-05-23T20:00:00+09:00
```

Check for:

- impossible dates such as `2026-02-31`
- malformed time zone offsets
- missing opening or closing `---`
- tabs in front matter
- unquoted special characters in titles

If a title contains quotes, a block scalar is safer:

```yaml
title: >
  How to Fix "Build failed" in Jekyll
```

### 3. Fix Missing Includes

If the log says a file does not exist in the includes directory, search for the include:

{% raw %}
```bash
rg "{% include" .
```
{% endraw %}

Example problem:

{% raw %}
```liquid
{% include ad-banner.html %}
```
{% endraw %}

Jekyll expects:

```text
_includes/ad-banner.html
```

Fix the filename, move the file into `_includes`, or remove the include if it is no longer used.

### 4. Fix Liquid Tag Errors

Liquid errors often mention tags not being closed or terminated.

Wrong:

{% raw %}
```liquid
{% if page.title %}
  {{ page.title }
{% endif %}
```
{% endraw %}

Right:

{% raw %}
```liquid
{% if page.title %}
  {{ page.title }}
{% endif %}
```
{% endraw %}

Check custom layouts and includes first because one broken layout can break many pages.

### 5. Fix Sass or SCSS Errors

If the log points to `.scss` or `.sass`, open the exact file and line.

Common mistakes:

- missing semicolon
- missing closing brace
- invalid variable name
- importing a file that does not exist

After fixing, run:

```bash
bundle exec jekyll build --trace
```

### 6. Check Plugins and GitHub Pages Mode

Some Jekyll plugins work locally but not in a restricted GitHub Pages build.

If you need custom plugins, use a GitHub Actions workflow that builds the site and deploys the generated output.
If you publish directly from a branch with the default Pages build, keep plugins compatible with GitHub Pages.

Check `Gemfile` and `_config.yml` together:

```yaml
plugins:
  - jekyll-feed
  - jekyll-sitemap
```

Remove plugins you do not use.

### 7. Confirm the Publishing Source

If the log says the `docs` folder is missing, check Pages settings:

```text
Settings > Pages > Build and deployment
```

Confirm whether the site publishes from:

- a branch root
- a `/docs` folder
- a custom GitHub Actions workflow

If you selected `/docs`, the `docs` folder must exist at the repository root on the selected branch.

## How to Verify

Run locally:

```bash
bundle exec jekyll build --trace
```

Then push and check GitHub:

```bash
git add .
git commit -m "Fix GitHub Pages build"
git push
```

The fix is complete when:

- local Jekyll build succeeds
- the Pages workflow succeeds
- the site URL updates after deployment
- the changed page renders without broken assets or missing includes

GitHub Pages publishing may take several minutes after a successful build.

## Common Mistakes

- Looking only at the final `exit code 1` line.
- Editing a post while the failure is actually in a shared layout.
- Forgetting the closing `---` in front matter.
- Using unsupported plugins in the default Pages build.
- Selecting `/docs` as the source after deleting or moving the `docs` folder.
- Assuming a local build is valid without using `bundle exec`.
- Ignoring case-sensitive file paths that fail on Linux runners.

## Official References

- [About Jekyll build errors for GitHub Pages sites](https://docs.github.com/articles/generic-jekyll-build-failures)
- [Troubleshooting Jekyll build errors for GitHub Pages sites](https://docs.github.com/articles/page-build-failed-markdown-errors)
- [Creating a GitHub Pages site with Jekyll](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/creating-a-github-pages-site-with-jekyll)

## Related Posts

- [How to Fix GitHub Actions Build Failed](/en_troubleshooting/github-actions-build-failed/)
- [How to Fix fatal: not a git repository Error](/en_troubleshooting/git-fatal-not-a-git-repository/)
- [How to Use Gitignore Correctly](/en_troubleshooting/git-using-gitignore/)

## FAQ

### When should I use this guide?

Use it when you can reproduce the error and need a practical order for checking commands, versions, paths, permissions, and logs.

### What should beginners verify first?

Start with the exact error message, the command you ran, the operating system, and the tool version. These details usually narrow the cause faster than changing many settings at once.

### Which keywords should I search next?

Search for "Fix GitHub Pages Jekyll Build Failed" together with the exact error text, version, operating system, and tool name used in your environment.
