# AdSense Rollout Checklist

Use this checklist before turning on ads for production posts.

## Current Implementation

- Global config: `_config.yml`
- Script include: `_includes/head/custom.html`
- Article ad controller: `_includes/ad-content.html`
- Ad unit markup: `_includes/ad-inarticle.html`
- Post layout hook: `_layouts/single.html`
- Styles: `_sass/minimal-mistakes/_page.scss`

Auto ads are enabled with the publisher code that is currently available:

```yaml
adsense:
  enabled: true
  client: "ca-pub-2983974324971673"
  auto_ads: true
  in_article_slot:
  post_bottom_slot:
  min_words_for_ads: 700
```

With this configuration, the AdSense script loads for Auto ads.
Manual in-article and post-bottom units are wired into every post layout, but those manual units render only after both slot IDs are set.

Automatic post eligibility:

- The page must be a Jekyll post with `page.id`.
- The page must not set `ads: false`.
- The body must meet `adsense.min_words_for_ads`.
- The first in-article unit is inserted after the first `h2`.
- The bottom unit is inserted after the post content.

## Manual Slot Activation Steps

1. Create a responsive in-article ad unit in AdSense.
2. Put the slot ID in `adsense.in_article_slot`.
3. Create a second responsive display or in-article unit for post bottom placement.
4. Put the slot ID in `adsense.post_bottom_slot`.
5. Keep `adsense.enabled: true`.
6. Set `adsense.auto_ads: false` only if you want manual units to be the only ad path.
7. Run `npm run validate:content-plan`.
8. Confirm the validator does not report empty manual slot errors.
9. Run `bundle exec jekyll build --trace` when Ruby/Bundler is available and the long build is acceptable.
10. Inspect at least five representative posts on desktop and mobile.

Expected Auto ads validator warning while manual slots are empty:

```text
WARN AdSense Auto ads are enabled; manual post ad slots remain inactive until slot IDs are configured
```

This warning is acceptable before manual AdSense slots are created.
After manual slot activation, the warning should disappear.

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

Auto ads are currently enabled with the provided publisher code because manual slot IDs are not available yet.
Keep density conservative until manual page review is complete.

Recommended first Auto ads test:

- Auto ads: on
- In-page formats: low density
- Anchor ads: off until mobile reading is reviewed
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
