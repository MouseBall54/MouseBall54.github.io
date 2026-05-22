# Troubleshooting Post Production Template

Use this template for every new paired Korean and English troubleshooting post.

## Pair Metadata

- Topic:
- Primary keyword:
- Secondary keywords:
- Category cluster:
- Korean file:
- English file:
- Translation ID:
- Header image:
- Related posts to link:
- Verification command tested:
- Notes from actual reproduction:

## Korean Front Matter

```yaml
---
typora-root-url: ../
layout: single
title: >
  한국어 제목
seo_title: >
  한국어 SEO 제목
date: 2026-05-23T09:00:00+09:00
lang: ko
translation_id: topic-slug
header:
  teaser: /images/header_images/overlay_image_python.png
  overlay_image: /images/header_images/overlay_image_python.png
  overlay_filter: 0.5
excerpt: >
  문제와 해결책을 120-160자 안팎으로 설명합니다.
seo_description: >
  문제와 해결책을 120-160자 안팎으로 설명합니다.
categories:
  - ko_Troubleshooting
tags:
  - Python
  - pip
  - Windows
---
```

## English Front Matter

```yaml
---
typora-root-url: ../
layout: single
title: >
  How to Fix ...
seo_title: >
  How to Fix ...
date: 2026-05-23T09:00:00+09:00
lang: en
translation_id: topic-slug
header:
  teaser: /images/header_images/overlay_image_python.png
  overlay_image: /images/header_images/overlay_image_python.png
  overlay_filter: 0.5
excerpt: >
  Explain the problem and the fix in about 120-160 characters.
seo_description: >
  Explain the problem and the fix in about 120-160 characters.
categories:
  - en_Troubleshooting
tags:
  - Python
  - pip
  - Windows
---
```

## Article Outline

````markdown
## Problem

State the exact error message and when it appears.

## Cause

Explain the likely cause. Keep this section concrete: version, path, dependency, permission, network, or config.

## Quick Fix

Start with the safest fix.

```bash
# command here
```

## Step-by-Step Fix

### 1. Check the Current State

```bash
# diagnostic command
```

### 2. Apply the Fix

```bash
# fix command
```

### 3. Verify the Result

```bash
# verification command
```

## Common Mistakes

- Mistake 1
- Mistake 2
- Mistake 3

## Related Posts

- [Related post title](/category/post-slug/)
- [Related post title](/category/post-slug/)
````

## Quality Checklist

- [ ] Korean and English posts exist.
- [ ] Both posts have the same `translation_id`.
- [ ] Front matter starts and ends with `---`.
- [ ] `date`, `lang`, `categories`, `tags`, `excerpt`, and `seo_description` are set.
- [ ] Title contains the primary keyword or exact error text.
- [ ] The first paragraph states the problem without filler.
- [ ] Commands are copyable and separated by OS when needed.
- [ ] The fix is verified with a command or observable result.
- [ ] Related posts include 2-4 internal links.
- [ ] Images have meaningful alt text if images are used.
- [ ] Build is checked with `bundle exec jekyll build --trace` when Bundler is available.

## Ad Placement Notes

- Manual in-article ads are controlled by `_includes/ad-content.html`.
- Ads render only when `site.adsense.enabled` is true and slot IDs exist in `_config.yml`.
- Set `ads: false` in front matter for short posts, legal pages, search pages, or pages where ads would interrupt the task.
- Do not place ads near download links, navigation links, or code copy buttons.
