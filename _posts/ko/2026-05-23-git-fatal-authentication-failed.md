---
typora-root-url: ../
layout: single
title: >
  Git fatal: Authentication failed 오류 해결 방법
seo_title: >
  Git fatal Authentication failed 해결
date: 2026-05-23T23:59:56+09:00
last_modified_at: 2026-05-23T23:59:59+09:00
lang: ko
translation_id: git-fatal-authentication-failed
header:
   teaser: /images/2026-05-23-git-fatal-authentication-failed/git-authentication-failed-hero.png
   overlay_image: /images/2026-05-23-git-fatal-authentication-failed/git-authentication-failed-hero.png
   overlay_filter: 0.35
   image_description: >
     Git fatal: Authentication failed 오류 해결 방법 주제를 한눈에 설명하는 시각 자료입니다.
excerpt: >
  Git fatal: Authentication failed 오류를 remote URL, HTTPS token, SSH key, credential cache, repository 권한 순서로 점검해 해결합니다.
seo_description: >
  Git fatal: Authentication failed 오류를 remote URL, HTTPS token, SSH key, credential cache, repository 권한 순서로 점검해 해결합니다.
categories:
  - ko_Troubleshooting
tags:
  - Git
  - GitHub
  - Authentication
  - SSH
  - Windows
---

## 핵심 요약

`fatal: Authentication failed`는 Git이 remote server에는 도달했지만 credential이 거부되었다는 뜻입니다.
HTTPS remote를 쓴다면 계정 password를 넣는 방식이 아닙니다.
Git Credential Manager, personal access token, 또는 SSH key를 사용해야 합니다.

![Git 인증 실패 흐름과 token 인증 성공 경로를 보여주는 이미지](/images/2026-05-23-git-fatal-authentication-failed/git-authentication-failed-hero.png)

이미지는 자주 보이는 실패 흐름을 보여줍니다.
Git은 remote repository를 찾았지만 credential gate에서 막힙니다.
해결 순서는 remote URL 확인, 오래된 credential 제거, 다시 인증, `git fetch`로 검증입니다.

## 흔한 증상

아래 메시지를 볼 수 있습니다.

```text
fatal: Authentication failed for 'https://github.com/OWNER/REPO.git/'
remote: Invalid username or password.
remote: Support for password authentication was removed.
```

보통 다음 명령에서 발생합니다.

```bash
git clone https://github.com/OWNER/REPO.git
git fetch
git pull
git push
```

중요한 단서는 remote URL 자체는 접근된다는 점입니다.
DNS 문제, proxy 문제, repository 없음 문제와는 다릅니다.

## 1. Remote URL 확인

먼저 Git이 어떤 remote를 사용 중인지 확인합니다.

```bash
git remote -v
```

HTTPS라면 보통 아래처럼 보입니다.

```text
origin  https://github.com/OWNER/REPO.git (fetch)
origin  https://github.com/OWNER/REPO.git (push)
```

owner나 repository 이름이 틀리면 수정합니다.

```bash
git remote set-url origin https://github.com/OWNER/REPO.git
```

SSH를 쓰려면 다음처럼 바꿉니다.

```bash
git remote set-url origin git@github.com:OWNER/REPO.git
```

실제로 접근 권한이 있는 repository를 가리키는지 먼저 확인해야 합니다.

## 2. HTTPS에서 계정 Password를 쓰지 않는다

대부분의 최신 Git hosting service는 HTTPS Git 작업에서 계정 password 인증을 받지 않습니다.
token 기반 인증이나 credential manager flow를 사용해야 합니다.

GitHub 기준으로 실전 선택지는 다음과 같습니다.

- Git Credential Manager로 로그인
- 필요한 repository 권한이 있는 personal access token 사용
- SSH로 전환하고 SSH key 사용

personal access token은 password처럼 다뤄야 합니다.
코드, config file, screenshot, 공유되는 shell history에 남기면 안 됩니다.

## 3. 오래된 Credential 제거

올바른 token을 만들었는데도 같은 오류가 계속 날 수 있습니다.
컴퓨터가 예전 password를 계속 보내고 있기 때문입니다.

Windows에서는:

1. **Credential Manager**를 엽니다.
2. **Windows Credentials**로 이동합니다.
3. Git host 관련 오래된 항목을 삭제합니다.
4. `git fetch`를 다시 실행하고 새 credential flow로 로그인합니다.

macOS Keychain에서는:

1. **Keychain Access**를 엽니다.
2. Git host를 검색합니다.
3. 오래된 internet password 항목을 삭제합니다.
4. Git 명령을 다시 실행합니다.

Git Credential Manager를 쓴다면 host에서 로그아웃할 수도 있습니다.

```bash
git credential-manager github logout
```

그 다음 다시 시도합니다.

```bash
git fetch origin
```

## 4. Push 전에 Fetch로 검증

먼저 `git fetch`로 확인합니다.
remote를 변경하지 않으므로 `git push`보다 안전한 테스트입니다.

```bash
git fetch origin
```

fetch가 성공하면 현재 branch를 확인합니다.

```bash
git branch --show-current
git status
```

그 다음 올바른 branch일 때만 push합니다.

```bash
git push origin HEAD
```

fetch는 되는데 push가 실패하면 login 자체는 된 것입니다.
이 경우 repository write permission, organization SSO, branch protection, token scope를 확인해야 합니다.

## 5. 2FA와 SSO 확인

회사나 조직 repository는 SSO 또는 two-factor authentication 정책을 사용할 수 있습니다.
token이 있어도 해당 organization에 authorize되지 않으면 실패할 수 있습니다.

확인할 항목은 다음과 같습니다.

- 내 account가 repository 접근 권한을 가지고 있는가?
- token에 필요한 repository permission이 있는가?
- organization이 SSO authorization을 요구하는가?
- protected branch에 push하려는 것은 아닌가?

Authentication과 authorization은 다릅니다.
Authentication은 내가 누구인지 증명합니다.
Authorization은 내가 무엇을 할 수 있는지 결정합니다.

## 6. SSH로 전환하기

SSH는 key 설정이 끝나면 HTTPS credential prompt를 줄일 수 있습니다.

기본 흐름은 다음과 같습니다.

```bash
ssh-keygen -t ed25519 -C "your-email@example.com"
ssh -T git@github.com
git remote set-url origin git@github.com:OWNER/REPO.git
git fetch origin
```

`ssh -T`가 실패한다면 SSH 설정부터 고쳐야 합니다.
remote URL만 바꿔도 key가 등록되어 있지 않으면 해결되지 않습니다.

## 흔한 실수

첫 번째 실수는 GitHub website password를 Git에 붙여 넣는 것입니다.
HTTPS Git 작업에서는 올바른 방식이 아닙니다.

두 번째 실수는 token을 만들고도 오래된 password를 credential store에 남겨 두는 것입니다.
Git은 삭제하기 전까지 stale credential을 계속 보낼 수 있습니다.

세 번째 실수는 remote URL이 잘못된 것입니다.
private fork나 organization repository를 잘못 가리키면 인증 또는 권한 문제가 납니다.

네 번째 실수는 `git fetch` 확인 없이 바로 `git push`로 테스트하는 것입니다.
fetch는 되는데 push만 실패하면 login 문제가 아니라 write permission이나 branch policy일 수 있습니다.

## 함께 보면 좋은 글

- [Git Permission denied publickey 오류 해결 방법](/ko_Troubleshooting/git-permission-denied-publickey/)
- [Git fatal: could not read Username 오류 해결 방법](/ko_Troubleshooting/git-fatal-could-not-read-username/)
- [GitHub: Managing personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)
- [GitHub: Caching credentials in Git](https://docs.github.com/en/get-started/git-basics/caching-your-github-credentials-in-git)

## 최종 체크리스트

```text
[ ] `git remote -v`가 올바른 repository를 가리킨다.
[ ] HTTPS Git에 account password를 쓰지 않는다.
[ ] credential store에서 오래된 credential을 삭제했다.
[ ] `git fetch origin`이 성공한다.
[ ] token 또는 account에 repository 접근 권한이 있다.
[ ] organization SSO나 branch protection이 막고 있지 않다.
```

올바른 account로 fetch가 성공하면, 남은 문제는 대개 permission 또는 branch policy입니다.
이 둘을 분리해서 보면 해결 속도가 훨씬 빨라집니다.

## 자주 묻는 질문

### 이 글은 언제 먼저 적용하면 좋나요?

오류 메시지, 실행한 명령, 사용 중인 OS와 버전을 먼저 기록한 뒤 이 글의 원인별 순서대로 확인하는 것이 좋습니다.

### 초보자가 가장 먼저 확인할 부분은 무엇인가요?

처음에는 환경 변수, 설치 경로, 권한, 캐시처럼 재현 가능성이 높은 항목부터 확인하세요. 그다음 로그와 설정 파일을 비교하면 원인을 좁히기 쉽습니다.

### 더 찾아볼 때 어떤 키워드를 쓰면 좋나요?

추가 검색할 때는 "Git fatal: Authentication failed 오류 해결 방법" 같은 핵심 문구와 error message, version, Windows, GitHub Pages, Jekyll 같은 실제 환경 키워드를 붙이면 더 정확한 결과를 얻기 쉽습니다.
