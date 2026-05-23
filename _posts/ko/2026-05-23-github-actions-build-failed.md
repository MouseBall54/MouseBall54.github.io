---
typora-root-url: ../
layout: single
title: >
  GitHub Actions build failed 해결 방법
seo_title: >
  GitHub Actions build failed 해결 방법
date: 2026-05-23T19:00:00+09:00
last_modified_at: 2026-05-23T23:59:59+09:00
lang: ko
translation_id: github-actions-build-failed
header:
   teaser: /images/2026-05-23-github-actions-build-failed/github-actions-build-failed-hero.png
   overlay_image: /images/2026-05-23-github-actions-build-failed/github-actions-build-failed-hero.png
   overlay_filter: 0.5
   image_description: >
     GitHub Actions build failed 해결 방법 주제를 한눈에 설명하는 시각 자료입니다.
excerpt: >
  GitHub Actions build failed 오류를 실패한 step log, workflow YAML, dependency install command, runner version, secret, branch trigger 기준으로 해결하는 방법입니다.
seo_description: >
  GitHub Actions build failed 오류를 실패한 step log, workflow YAML, dependency install command, runner version, secret, branch trigger 기준으로 해결하는 방법입니다.
categories:
  - ko_Troubleshooting
tags:
  - GitHubActions
  - CI
  - GitHub
  - Build
---

## 문제 상황

Pull request 또는 push 후 GitHub Actions check가 실패할 수 있습니다.

![GitHub Actions build failed 해결 방법 설명 이미지](/images/2026-05-23-github-actions-build-failed/github-actions-build-failed-hero.png)

```text
build failed
Process completed with exit code 1
```

또는 workflow 자체가 유효하지 않다는 메시지가 나올 수 있습니다.

```text
The workflow is not valid
```

해결 방법은 실패 위치에 따라 달라집니다.
무작정 YAML부터 고치지 말고, 실패한 workflow run을 열어 failed job과 failed step을 먼저 확인해야 합니다.

## 원인

GitHub Actions build는 보통 다음 이유로 실패합니다.

- Workflow file의 YAML이 잘못되었거나 위치가 틀렸습니다.
- Workflow trigger가 branch 또는 event와 맞지 않습니다.
- Build step 전에 dependency install이 되지 않았습니다.
- CI runner의 Node, Python, Java, Ruby version이 local과 다릅니다.
- Secret 또는 environment variable이 없습니다.
- Test, lint, typecheck, build command가 실제로 실패했습니다.
- Cache가 오래된 dependency를 복원했습니다.
- Deploy step에 필요한 permission이 없습니다.

GitHub workflow file은 `.github/workflows` 아래에 있어야 하며 `.yml` 또는 `.yaml` 확장자를 사용해야 합니다.
파일 자체가 invalid라면 YAML을 고칠 때까지 새 commit마다 실패한 workflow run이 생길 수 있습니다.

## 빠른 진단

실패한 run을 엽니다.

1. GitHub repository로 이동합니다.
2. **Actions** tab을 엽니다.
3. 실패한 workflow를 선택합니다.
4. 실패한 run을 엽니다.
5. Failed job을 클릭합니다.
6. Failed step을 펼쳐 첫 번째 실제 error를 읽습니다.

GitHub CLI를 사용한다면 최근 run을 확인할 수 있습니다.

```bash
gh run list
gh run view --log
```

Log에서 아래 단어를 검색합니다.

```text
Error:
failed
exit code
not found
permission
```

중요한 error는 보통 `Process completed with exit code 1`보다 위에 있습니다.

## 단계별 해결 방법

### 1. Invalid Workflow YAML 수정하기

Workflow file은 아래 위치에 있어야 합니다.

```text
.github/workflows/ci.yml
```

기본 예시:

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Show working directory
        run: pwd
```

다음을 확인합니다.

- tab 대신 space를 사용했는지
- indentation이 맞는지
- colon이 빠지지 않았는지
- 중복 key가 없는지
- 파일이 `.github/workflows` 밖에 저장되지 않았는지
- expression syntax가 올바른지

YAML 오류는 package나 test 오류보다 먼저 해결해야 합니다.

### 2. Trigger 확인하기

Workflow가 예상대로 실행되지 않는다면 `on` 설정을 확인합니다.

아래 설정은 `main` branch push에서만 실행됩니다.

```yaml
on:
  push:
    branches: [main]
```

Feature branch에서 테스트한다면 `pull_request`를 추가하거나 branch 조건을 넓힙니다.

```yaml
on:
  push:
  pull_request:
```

`paths` 또는 `paths-ignore`가 있으면 해당 path 밖의 변경에서는 workflow가 skip될 수 있습니다.

### 3. Runtime Version 맞추기

CI runner의 version이 local과 달라 build가 실패하는 경우가 많습니다.

Node 예시:

```yaml
- uses: actions/setup-node@v4
  with:
    node-version: 20
    cache: npm

- run: npm ci
- run: npm run build
```

Python 예시:

```yaml
- uses: actions/setup-python@v5
  with:
    python-version: "3.12"

- run: python -m pip install -r requirements.txt
- run: pytest
```

`.nvmrc`, `.python-version`, `package.json`, `pyproject.toml`, project 문서에 적힌 version과 맞추는 것이 좋습니다.

### 4. 올바른 Install Command 사용하기

CI에서는 lockfile을 기준으로 설치하는 명령을 사용합니다.

npm project:

```yaml
- run: npm ci
- run: npm test
- run: npm run build
```

pnpm project:

```yaml
- uses: pnpm/action-setup@v4
- run: pnpm install --frozen-lockfile
- run: pnpm build
```

Bundler project:

```yaml
- run: bundle install
- run: bundle exec jekyll build --trace
```

Log에 `command not found`가 보이면 해당 tool을 설치하거나 setup action을 먼저 실행해야 합니다.

### 5. Secret과 Permission 확인하기

Log에 authentication, token, permission 관련 메시지가 있다면 repository secret과 workflow permission을 확인합니다.

흔한 증상:

```text
Context access might be invalid: SECRET_NAME
Resource not accessible by integration
Permission denied
```

Secret은 아래 위치에서 확인합니다.

```text
Settings > Secrets and variables > Actions
```

Push, deploy, package publish를 하는 workflow라면 permission도 확인합니다.

```yaml
permissions:
  contents: read
  pages: write
  id-token: write
```

Job에 필요한 권한만 부여하세요.

### 6. 실패한 Command를 Local에서 재현하기

Failed step에 나온 명령을 local에서 그대로 실행합니다.

```bash
npm ci
npm run build
```

또는:

```bash
bundle install
bundle exec jekyll build --trace
```

Local에서도 실패하면 project code나 dependency 문제입니다.
GitHub Actions에서만 실패하면 version, environment variable, file path, OS 차이를 비교해야 합니다.

### 7. Cache는 근거가 있을 때만 정리하기

Cache 문제가 생길 수는 있지만 첫 번째 가정으로 삼지는 마세요.

Lockfile 변경 후에도 dependency 오류가 반복된다면 cache를 잠시 끄거나 cache key를 바꿔 확인합니다.
CI를 통과시키기 위해 lockfile을 삭제하는 것은 좋지 않습니다.
Lockfile은 재현 가능한 build의 일부입니다.

## 해결 확인 방법

Workflow 또는 project file을 수정한 뒤 push합니다.

```bash
git add .
git commit -m "Fix CI build"
git push
```

그다음 확인합니다.

- 예상 branch 또는 pull request에서 workflow가 실행됩니다.
- 이전에 실패했던 step이 통과합니다.
- Test와 build가 모두 통과합니다.
- Deploy step에 필요한 permission이 있습니다.

다음 step에서 다시 실패한다면 같은 방식으로 그 step의 log를 읽고 별도 오류로 처리합니다.

## 흔한 실수

- `exit code 1`만 보고 그 위의 실제 error를 놓칩니다.
- 다른 workflow file을 수정합니다.
- Project가 `npm ci`를 기대하는데 CI에서 `npm install`을 사용합니다.
- Command 실행 전에 runtime setup을 하지 않습니다.
- Local secret은 있지만 GitHub Actions secret은 없는 상태를 놓칩니다.
- 필요한 permission을 고치지 않고 broad permission부터 부여합니다.
- Dependency conflict를 피하려고 lockfile을 삭제합니다.

## 공식 문서

- [Using workflow run logs](https://docs.github.com/en/actions/how-tos/monitor-workflows/use-workflow-run-logs)
- [Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax)

## 관련 글

- [Git failed to push some refs 오류 해결 방법](/ko_Troubleshooting/git-failed-to-push-some-refs/)
- [Git merge conflict 해결 방법](/ko_Troubleshooting/git-resolving-merge-conflicts/)
- [Git fatal: could not read Username 오류 해결 방법](/ko_Troubleshooting/git-fatal-could-not-read-username/)

## 자주 묻는 질문

### 이 글은 언제 먼저 적용하면 좋나요?

오류 메시지, 실행한 명령, 사용 중인 OS와 버전을 먼저 기록한 뒤 이 글의 원인별 순서대로 확인하는 것이 좋습니다.

### 초보자가 가장 먼저 확인할 부분은 무엇인가요?

처음에는 환경 변수, 설치 경로, 권한, 캐시처럼 재현 가능성이 높은 항목부터 확인하세요. 그다음 로그와 설정 파일을 비교하면 원인을 좁히기 쉽습니다.

### 더 찾아볼 때 어떤 키워드를 쓰면 좋나요?

추가 검색할 때는 "GitHub Actions build failed 해결 방법" 같은 핵심 문구와 error message, version, Windows, GitHub Pages, Jekyll 같은 실제 환경 키워드를 붙이면 더 정확한 결과를 얻기 쉽습니다.
