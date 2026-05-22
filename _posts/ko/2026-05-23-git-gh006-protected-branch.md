---
typora-root-url: ../
layout: single
title: >
  GH006 Protected Branch Hook Declined 오류 해결 방법
seo_title: >
  GH006 Protected Branch Hook Declined 해결
date: 2026-05-23T23:59:59+09:00
last_modified_at: 2026-05-23T23:59:59+09:00
lang: ko
translation_id: git-gh006-protected-branch
header:
   teaser: /images/2026-05-23-git-gh006-protected-branch/git-gh006-protected-branch-hero.png
   overlay_image: /images/2026-05-23-git-gh006-protected-branch/git-gh006-protected-branch-hero.png
   overlay_filter: 0.35
excerpt: >
  GitHub GH006 protected branch hook declined 오류를 feature branch, pull request, required checks, review approval, branch protection rule 순서로 해결합니다.
seo_description: >
  GitHub GH006 protected branch hook declined 오류를 feature branch, pull request, required checks, review approval, branch protection rule 순서로 해결합니다.
categories:
  - ko_Troubleshooting
tags:
  - Git
  - GitHub
  - BranchProtection
  - PullRequest
  - CI
---

## 핵심 요약

`GH006: Protected branch update failed`는 GitHub가 protected branch로의 push를 거부했다는 뜻입니다.
보통 해결책은 강제로 push하는 것이 아닙니다.
새 branch를 만들고, pull request를 열고, required checks와 review 조건을 통과한 뒤 허용된 방식으로 merge해야 합니다.

![직접 push는 막히고 pull request check 경로는 통과하는 protected branch gate 이미지](/images/2026-05-23-git-gh006-protected-branch/git-gh006-protected-branch-hero.png)

이미지는 핵심 구조를 보여줍니다.
직접 push는 protected branch gate에서 막힙니다.
pull request 경로는 check, review, policy gate를 거쳐 통과할 수 있습니다.

## 대표 오류 메시지

아래와 비슷한 메시지가 나올 수 있습니다.

```text
remote: error: GH006: Protected branch update failed for refs/heads/main.
remote: error: Required status check "build" is expected.
remote: error: At least 1 approving review is required.
```

세부 메시지는 branch rule에 따라 다릅니다.
required checks, required reviews, force push 금지, signed commits, direct push 제한 때문에 막힐 수 있습니다.

## 1. 어떤 Branch가 Protected인지 확인

현재 branch와 remote를 확인합니다.

```bash
git branch --show-current
git status
git remote -v
```

push 대상도 확인합니다.

```bash
git push origin HEAD
```

`HEAD`가 `main`, `master`, `production` 같은 protected branch라면 거부되는 것이 정상일 수 있습니다.
protected branch는 직접 update를 막기 위해 존재합니다.

## 2. Feature Branch로 Push

새 branch를 만들고 push합니다.

```bash
git switch -c fix/my-change
git push -u origin fix/my-change
```

그 다음 `fix/my-change`에서 protected branch로 pull request를 엽니다.
이 경로에서 GitHub가 check를 실행하고 review를 받을 수 있습니다.

이미 branch가 있다면:

```bash
git switch fix/my-change
git push
```

repository rule이 명시적으로 허용하고 영향 범위를 이해한 경우가 아니라면 protected branch에 `--force`를 사용하지 마세요.

## 3. Required Checks 확인

branch protection은 CI status check를 요구하는 경우가 많습니다.
pull request를 열고 GitHub Actions 또는 다른 CI가 실행 중인지 확인합니다.

check가 멈춰 있다면 다음을 봅니다.

- workflow가 target branch에 존재하는가?
- path filter 때문에 workflow가 skip되었는가?
- workflow가 사용하는 secret이나 permission이 맞는가?
- 실패 원인을 고친 뒤 job을 다시 실행했는가?

check가 실패했다면 feature branch에서 build를 고치고 다시 push합니다.
protected branch는 check가 통과하기 전까지 update하면 안 됩니다.

## 4. Required Review Approval 받기

일부 protected branch는 하나 이상의 approving review를 요구합니다.
이 경우 pull request에 충분한 approval이 있어야 merge할 수 있습니다.

자주 보이는 review blocker:

- 아직 approval이 없음
- requested changes가 해결되지 않음
- 새 commit 때문에 approval이 dismiss됨
- code owner review가 필요함
- author가 자신의 pull request를 approve할 수 없음

pull request의 review 영역을 확인합니다.
code owner가 필요하다면 표시된 owner에게 review를 요청합니다.

## 5. Admin과 Bypass Rule 확인

repository admin도 branch protection을 우회할 수 없도록 설정될 수 있습니다.
조직 ruleset이 여러 repository에 적용될 수도 있습니다.

repository 소유자이고 정책을 바꾸려면 아래 항목을 확인합니다.

- Required pull request reviews
- Required status checks
- Require branches to be up to date
- Restrict who can push
- Require signed commits
- Allow force pushes
- Allow deletions

팀 프로세스 자체를 바꿔야 할 때만 rule을 수정하세요.
실패한 check를 피하려고 protection을 약화시키면 안 됩니다.

## 6. 지금 Protected Branch를 고쳐야 한다면

가장 위험이 낮은 경로를 사용합니다.

```bash
git switch -c hotfix/short-description
git push -u origin hotfix/short-description
```

pull request를 열고 required checks를 실행합니다.
필요한 review를 받고 repository가 허용하는 merge button으로 merge합니다.

production 장애처럼 emergency bypass가 필요한 상황이라면 조직의 문서화된 절차를 따릅니다.
우회한 이유도 기록해야 합니다.

## 흔한 실수

첫 번째 실수는 GH006을 authentication 문제로 보는 것입니다.
로그인은 맞을 수 있습니다.
GitHub가 branch rule 때문에 update를 거부하는 것입니다.

두 번째 실수는 `git push --force`를 시도하는 것입니다.
protected branch는 보통 이를 거부하고, 허용되어도 shared history를 바꿀 수 있습니다.

세 번째 실수는 로컬에서 test를 통과했다고 바로 직접 push하는 것입니다.
required checks는 GitHub 또는 설정된 CI provider에서 통과해야 합니다.

네 번째 실수는 실패 원인을 고치지 않고 branch protection rule을 바꾸는 것입니다.
protection rule은 main branch를 안정적으로 유지하기 위해 존재합니다.

## 함께 보면 좋은 글

- [Git fatal Authentication failed 오류 해결](/ko_Troubleshooting/git-fatal-authentication-failed/)
- [GitHub Actions Build Failed 해결](/ko_Troubleshooting/github-actions-build-failed/)
- [GitHub: About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)
- [GitHub: Managing a branch protection rule](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule)

## 최종 체크리스트

```text
[ ] protected branch에 직접 push하지 않는다.
[ ] 작업이 feature 또는 hotfix branch에 있다.
[ ] pull request base branch가 올바르다.
[ ] required CI checks가 통과했다.
[ ] required review 또는 code owner approval이 완료되었다.
[ ] branch protection rule을 불필요하게 약화시키지 않았다.
```

GH006은 대개 Git 문법 오류가 아니라 프로세스 오류입니다.
pull request 경로를 사용하고 GitHub가 알려주는 branch rule 조건을 충족하면 됩니다.

## 자주 묻는 질문

### 이 글은 언제 먼저 적용하면 좋나요?

오류 메시지, 실행한 명령, 사용 중인 OS와 버전을 먼저 기록한 뒤 이 글의 원인별 순서대로 확인하는 것이 좋습니다.

### 초보자가 가장 먼저 확인할 부분은 무엇인가요?

처음에는 환경 변수, 설치 경로, 권한, 캐시처럼 재현 가능성이 높은 항목부터 확인하세요. 그다음 로그와 설정 파일을 비교하면 원인을 좁히기 쉽습니다.

### 더 찾아볼 때 어떤 키워드를 쓰면 좋나요?

추가 검색할 때는 "GH006 Protected Branch Hook Declined 오류 해결 방법" 같은 핵심 문구와 error message, version, Windows, GitHub Pages, Jekyll 같은 실제 환경 키워드를 붙이면 더 정확한 결과를 얻기 쉽습니다.
