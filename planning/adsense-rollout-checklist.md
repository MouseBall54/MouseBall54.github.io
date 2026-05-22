# AdSense Rollout Checklist

Use this checklist before turning on ads for production posts.

## Current Implementation

- Global config: `_config.yml`
- Script include: `_includes/head/custom.html`
- Article ad controller: `_includes/ad-content.html`
- Ad unit markup: `_includes/ad-inarticle.html`
- Post layout hook: `_layouts/single.html`
- Styles: `_sass/minimal-mistakes/_page.scss`

Ads are disabled by default:

```yaml
adsense:
  enabled: false
  client: "ca-pub-2983974324971673"
  auto_ads: false
  in_article_slot:
  post_bottom_slot:
  min_words_for_ads: 700
```

With this default configuration, ad markup is wired into every post layout but no live ad is rendered yet.
Ads start rendering only after `enabled: true` and both manual slot IDs are set.

Automatic post eligibility:

- The page must be a Jekyll post with `page.id`.
- The page must not set `ads: false`.
- The body must meet `adsense.min_words_for_ads`.
- The first in-article unit is inserted after the first `h2`.
- The bottom unit is inserted after the post content.

## Activation Steps

1. Create a responsive in-article ad unit in AdSense.
2. Put the slot ID in `adsense.in_article_slot`.
3. Create a second responsive display or in-article unit for post bottom placement.
4. Put the slot ID in `adsense.post_bottom_slot`.
5. Keep `adsense.auto_ads: false` for the first rollout unless testing Auto ads intentionally.
6. Set `adsense.enabled: true`.
7. Run `npm run validate:content-plan`.
8. Confirm the validator does not report empty ad slot errors.
9. Run `bundle exec jekyll build --trace` when Ruby/Bundler is available.
10. Inspect at least five representative posts on desktop and mobile.

Expected inactive-mode validator warning:

```text
WARN AdSense is disabled or slot IDs are empty; ads will not render on posts until enabled and slots are configured
```

This warning is acceptable before AdSense slots are created.
After activation, the warning should disappear.

## Page-Level Controls

Use this front matter to suppress ads on a specific page or post:

```yaml
ads: false
```

Use `ads: false` for:

- Very short posts
- Search pages
- Category and tag pages
- Legal or policy pages
- Pages where an ad would appear near a download link, navigation link, or code-copy control

## Manual QA

Check each item before enabling ads broadly:

- [ ] No ad appears before the reader reaches the actual content.
- [ ] The first ad appears only after the first `h2`.
- [ ] Ads do not appear on archive, category, tag, or search pages.
- [ ] Ads are visually labeled as `Advertisements`.
- [ ] Ads do not look like navigation, download buttons, or related-post links.
- [ ] Mobile layout does not shift heavily when the ad loads.
- [ ] Code blocks and copy buttons remain usable.
- [ ] Comments and related posts remain visible and not crowded.

## Auto Ads Policy

Start with manual ads. Test Auto ads only after manual placements are stable.

Recommended first Auto ads test:

- Auto ads: on
- In-page formats: low density
- Anchor ads: mobile only after manual review
- Vignette ads: off at first
- Side rail ads: desktop only, if it does not cover reading

Stop or reduce Auto ads if:

- Mobile reading becomes cluttered
- Anchor ads cover content
- Pages feel slower or jumpy
- Search Console engagement drops after rollout
- AdSense reports invalid traffic warnings

## Measurement

Review after 7, 14, and 30 days:

- Page RPM by category
- Impression RPM
- Ad viewability
- GA4 engaged sessions
- Search Console clicks and average position
- Top pages with revenue but poor engagement

Change only one ad variable at a time, then wait at least seven days before judging the result.
