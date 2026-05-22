---
typora-root-url: ../
layout: single
title: >
  GitHub Pages Jekyll build failed 해결 방법
seo_title: >
  GitHub Pages Jekyll build failed 해결 방법
date: 2026-05-23T20:00:00+09:00
lang: ko
translation_id: github-pages-jekyll-build-failed
header:
   teaser: /images/header_images/overlay_image_git.png
   overlay_image: /images/header_images/overlay_image_git.png
   overlay_filter: 0.5
excerpt: >
  GitHub Pages Jekyll build failed 오류를 Pages workflow log, _config.yml YAML, front matter date, include, plugin, Sass, local Jekyll build 기준으로 해결하는 방법입니다.
seo_description: >
  GitHub Pages Jekyll build failed 오류를 Pages workflow log, _config.yml YAML, front matter date, include, plugin, Sass, local Jekyll build 기준으로 해결하는 방법입니다.
categories:
  - ko_Troubleshooting
tags:
  - GitHubPages
  - Jekyll
  - GitHub
  - Build
---

## 문제 상황

GitHub Pages가 Jekyll site를 publish하지 못하고 실패할 수 있습니다.

```text
Pages build and deployment failed
```

또는 아래처럼 표시될 수 있습니다.

```text
Error: Process completed with exit code 1
```

메시지에는 `_config.yml`, front matter, Sass, include file, plugin, post date 등이 함께 나올 수 있습니다.
가장 빠른 해결은 Pages workflow log를 읽고 같은 Jekyll build를 local에서 재현하는 것입니다.

## 원인

흔한 원인은 다음과 같습니다.

- `_config.yml`의 YAML 문법이 잘못되었습니다.
- Post filename 또는 front matter date가 유효하지 않습니다.
- 파일 encoding이 UTF-8이 아닙니다.
- Liquid tag가 닫히지 않았습니다.
- Include가 `_includes`에 없는 파일을 참조합니다.
- Sass 또는 SCSS 문법이 잘못되었습니다.
- 현재 build mode에서 지원되지 않는 plugin을 사용합니다.
- Publishing source 설정이 잘못되었습니다.
- Local Ruby/Bundler 환경과 GitHub Pages 환경이 다릅니다.

GitHub는 Pages site 배포와 자동화에 GitHub Actions 사용을 권장합니다.
따라서 build log는 보통 repository의 Actions tab에서 확인할 수 있습니다.

## 빠른 진단

실패한 Pages build를 엽니다.

1. GitHub repository로 이동합니다.
2. **Actions** tab을 엽니다.
3. 실패한 **Pages build and deployment** run을 엽니다.
4. Failed job을 엽니다.
5. Failed step을 펼칩니다.
6. Log에 처음 나온 file path와 line number를 확인합니다.

그다음 local build를 실행합니다.

```bash
bundle install
bundle exec jekyll build --trace
```

아직 Bundler를 사용하지 않는다면 Bundler와 `Gemfile`을 쓰는 것이 좋습니다.
Bundler는 Ruby gem dependency를 고정해 환경 차이로 생기는 Jekyll 오류를 줄입니다.

## 단계별 해결 방법

### 1. _config.yml YAML 오류 수정하기

Log에 `_config.yml`이 나오면 YAML 문법부터 확인합니다.

흔한 문제:

```yaml
title: My site: notes
```

값에 colon이 들어가면 quote를 사용합니다.

```yaml
title: "My site: notes"
```

다음도 확인합니다.

- tab 대신 space를 사용했는지
- 각 `:` 뒤에 space가 있는지
- UTF-8 text인지
- indentation이 맞는지
- 긴 text에 block scalar를 사용했는지

예시:

```yaml
description: >
  A short description that can span multiple lines
  without breaking YAML parsing.
```

### 2. Post Date와 Front Matter 수정하기

Jekyll post filename은 유효한 date를 사용해야 합니다.

```text
_posts/ko/2026-05-23-example-post.md
```

Front matter date도 유효해야 합니다.

```yaml
date: 2026-05-23T20:00:00+09:00
```

다음을 확인합니다.

- `2026-02-31` 같은 존재하지 않는 날짜
- 잘못된 time zone offset
- 열거나 닫는 `---` 누락
- front matter 안의 tab
- title 안의 quote 또는 colon 처리

Title에 quote가 있으면 block scalar가 안전합니다.

```yaml
title: >
  How to Fix "Build failed" in Jekyll
```

### 3. Missing Include 수정하기

Log에 include file이 없다고 나오면 include 사용 지점을 검색합니다.

```bash
rg "{% include" .
```

문제 예시:

```liquid
{% include ad-banner.html %}
```

Jekyll은 아래 파일을 기대합니다.

```text
_includes/ad-banner.html
```

Filename을 고치거나, 파일을 `_includes`로 옮기거나, 더 이상 쓰지 않는 include라면 제거합니다.

### 4. Liquid Tag 오류 수정하기

Liquid 오류는 tag가 닫히지 않았거나 output tag가 끝나지 않았을 때 자주 발생합니다.

잘못된 예:

```liquid
{% if page.title %}
  {{ page.title }
{% endif %}
```

올바른 예:

```liquid
{% if page.title %}
  {{ page.title }}
{% endif %}
```

Layout이나 include 하나가 깨지면 여러 page가 함께 실패할 수 있으므로 공통 파일부터 확인합니다.

### 5. Sass 또는 SCSS 오류 수정하기

Log가 `.scss` 또는 `.sass` 파일을 가리키면 해당 file과 line을 엽니다.

흔한 문제는 다음과 같습니다.

- semicolon 누락
- closing brace 누락
- 잘못된 variable name
- 존재하지 않는 file import

수정 후 다시 실행합니다.

```bash
bundle exec jekyll build --trace
```

### 6. Plugin과 GitHub Pages Mode 확인하기

일부 Jekyll plugin은 local에서는 동작하지만 제한된 GitHub Pages build에서는 동작하지 않을 수 있습니다.

Custom plugin이 필요하다면 GitHub Actions workflow로 site를 build하고 generated output을 deploy하는 방식을 사용합니다.
Branch에서 바로 publish하는 default Pages build라면 GitHub Pages와 호환되는 plugin만 유지해야 합니다.

`Gemfile`과 `_config.yml`을 함께 확인합니다.

```yaml
plugins:
  - jekyll-feed
  - jekyll-sitemap
```

사용하지 않는 plugin은 제거합니다.

### 7. Publishing Source 확인하기

Log에 `docs` folder가 없다고 나오면 Pages 설정을 확인합니다.

```text
Settings > Pages > Build and deployment
```

Site가 어디서 publish되는지 확인합니다.

- branch root
- `/docs` folder
- custom GitHub Actions workflow

`/docs`를 선택했다면 선택한 branch의 repository root에 `docs` folder가 실제로 있어야 합니다.

## 해결 확인 방법

Local에서 build합니다.

```bash
bundle exec jekyll build --trace
```

그다음 push하고 GitHub에서 확인합니다.

```bash
git add .
git commit -m "Fix GitHub Pages build"
git push
```

해결 기준은 다음과 같습니다.

- Local Jekyll build가 성공합니다.
- Pages workflow가 성공합니다.
- Deploy 후 site URL이 갱신됩니다.
- 변경한 page가 깨진 asset이나 missing include 없이 렌더링됩니다.

GitHub Pages는 build 성공 후 반영까지 몇 분 걸릴 수 있습니다.

## 흔한 실수

- 마지막 `exit code 1` 줄만 봅니다.
- 실제로는 shared layout 문제인데 post만 수정합니다.
- Front matter의 닫는 `---`를 빠뜨립니다.
- Default Pages build에서 지원되지 않는 plugin을 사용합니다.
- `/docs` source를 선택한 뒤 `docs` folder를 삭제하거나 이동합니다.
- `bundle exec` 없이 local build 결과를 믿습니다.
- Linux runner에서 실패하는 대소문자 file path 차이를 놓칩니다.

## 공식 문서

- [About Jekyll build errors for GitHub Pages sites](https://docs.github.com/articles/generic-jekyll-build-failures)
- [Troubleshooting Jekyll build errors for GitHub Pages sites](https://docs.github.com/articles/page-build-failed-markdown-errors)
- [Creating a GitHub Pages site with Jekyll](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/creating-a-github-pages-site-with-jekyll)

## 관련 글

- [GitHub Actions build failed 해결 방법](/ko_Troubleshooting/github-actions-build-failed/)
- [Git fatal: not a git repository 오류 해결 방법](/ko_Troubleshooting/git-fatal-not-a-git-repository/)
- [Gitignore 사용법과 흔한 실수](/ko_Troubleshooting/git-using-gitignore/)
