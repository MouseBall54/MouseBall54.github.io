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

- Ubuntu setup when Ruby is missing: `sudo apt-get update && sudo apt-get install -y ruby-full build-essential zlib1g-dev libssl-dev libyaml-dev libffi-dev`.
- `gem install bundler`: install Bundler if `bundle -v` is not available.
- `bundle install`: install Ruby/Jekyll dependencies from `Gemfile`.
- `bundle exec jekyll serve`: run the site locally at `http://127.0.0.1:4000`.
- `bundle exec jekyll build --trace`: validate the production build.
- `python update_posts.py`: add missing `lang` and `translation_id` fields to paired posts.
- `rake js`: rebuild `assets/js/main.min.js` after JavaScript source edits.
- `npm run validate:content-plan`: validate paired posts, category hubs, internal links, images, and AdSense wiring.

## Minimal Mistakes Usage

This repository vendors Minimal Mistakes layouts, includes, Sass, and assets instead of using a remote theme. Keep custom site logic in the smallest possible include or layout override.

- Global custom head code belongs in `_includes/head/custom.html`; Minimal Mistakes includes it at the end of `<head>`.
- Main and sidebar navigation belongs in `_data/navigation.yml`.
- Category and tag archive settings live in `_config.yml`.
- Do not enable `jekyll-archives` unless the project intentionally moves away from the manual bilingual category hubs.
- Keep `url: "https://mouseball54.github.io"` and empty `baseurl` for the user GitHub Pages site.

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
- `ko_AI_Trends`
- `en_AI_Trends`
- `ko_Global_Affairs`
- `en_Global_Affairs`
- `ko_Climate_Energy`
- `en_Climate_Energy`
- `ko_Consumer_Rights`
- `en_Consumer_Rights`
- `ko_Digital_Security`
- `en_Digital_Security`
- `ko_Personal_Finance`
- `en_Personal_Finance`
- `ko_Health_Literacy`
- `en_Health_Literacy`
- `ko_Study`
- `en_Study`
- `ko_Economy`
- `en_Economy`

Each post should have exactly one language-prefixed category. Category hub pages must exist at `_pages/category-<category>.md` with a lowercase permalink such as `/en_troubleshooting/`, `sidebar.nav: "sidebar-category"`, useful intro copy, and at least three starting links when enough posts exist.

AI Trends posts should use official or institution-grade sources such as OpenAI documentation, NIST AI RMF, OWASP LLM guidance, OECD AI Principles, EU AI Act resources, and Stanford HAI AI Index. Treat them as educational workflow and governance guides, not model hype or vendor promotion. Focus on verification, evals, tool boundaries, data handling, security, cost control, and human review.

Study posts should be evidence-informed educational guides, not generic motivation or unsupported study hacks. Prefer sources such as IES What Works Clearinghouse, Education Endowment Foundation, CDC or NIH sleep guidance, Purdue OWL, Cornell Learning Strategies Center, Harvard academic resources, and official programming documentation. Focus on observable routines: retrieval prompts, spaced review, mistake logs, feedback loops, sleep and focus boundaries, and measurable weekly output.

Global Affairs posts should use official sources where possible, include a source notes section, and translate international events into practical Korea-facing channels such as exports, import prices, energy security, financial conditions, household costs, and security policy.

Climate & Energy posts should use official or institution-grade sources such as IEA, IPCC, WMO, UNEP, UNFCCC, World Bank, OECD, EIA, KEA, KESIS, KMA, and Korean climate or energy ministries. Treat them as educational briefings, not investment advice or technology promotion. Separate targets, policy tools, costs, grid constraints, supply chains, adaptation risk, and Korea-facing channels such as electricity bills, industrial competitiveness, exports, ports, and household costs.

Consumer Rights posts should be educational only and must not present legal advice. Prefer official sources such as FTC, CFPB, FCC, DOT, CPSC, FDA, NHTSA, econsumer.gov, Korea Consumer Agency, and Korea Fair Trade Commission. Focus on evidence, dates, contract wording, refund or repair requests, complaint escalation, and clear distinction between seller, platform, payment provider, carrier, and regulator.

Digital Security posts should prioritize official guidance from sources such as CISA, NIST, FTC, KISA, and privacy reporting agencies. Write them as practical safety routines, not fear-based product recommendations. Include source notes, recovery steps, and clear warnings that fast reporting reduces damage.

Personal Finance posts should be educational only and must not present individualized investment, tax, lending, or legal advice. Prefer official sources such as CFPB, SEC Investor.gov, FINRA, IRS, FTC, FSS, and KINFA. Include source notes, assumptions to verify, and a reminder to check local tax and financial rules.

Economy posts should be educational only and must not present individualized investment, tax, lending, legal, or personal financial advice. Prefer official or institution-grade sources such as IMF, World Bank, OECD, Federal Reserve, BEA, BLS, FRED, Bank of Korea, KOSIS, CFPB, SEC, and FDIC. Connect macro signals to household-facing channels such as prices, wages, interest payments, exchange rates, savings, debt service, imports, exports, and Korea-facing cost pressure.

Health Literacy posts should be educational only and must not present diagnosis, treatment, dosage, or personalized medical advice. Prefer official sources such as CDC, WHO, FDA, NIH MedlinePlus, NIMH, and ODPHP. Include source notes, safety red flags, and clear guidance to contact emergency services or qualified medical professionals for severe, sudden, or safety-critical symptoms.

## AdSense

AdSense is configured through `_config.yml`:

- `adsense.enabled`: turns AdSense markup on or off.
- `adsense.client`: must stay in `ca-pub-...` format.
- `adsense.auto_ads`: when true, the AdSense loader in `_includes/head/custom.html` allows Google Auto ads to place ads after the site is approved and Auto ads are enabled in AdSense.
- `adsense.amp_auto_ads`: when true, AMP Auto ads markup is available only on pages or layouts that explicitly set `amp: true`.
- `adsense.in_article_slot` and `adsense.post_bottom_slot`: optional manual ad unit slot IDs. Leave empty until real slot IDs are created in AdSense.
- `adsense.min_words_for_ads`: minimum post word count for manual in-article units.

The root `ads.txt` publisher ID must match `_config.yml` without the `ca-` prefix. Do not paste duplicate AdSense loader scripts into layouts or posts; keep the single non-AMP loader in `_includes/head/custom.html`. AMP pages should use the guarded `amp-auto-ads` include so AMP-only tags do not leak into normal HTML pages.

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
