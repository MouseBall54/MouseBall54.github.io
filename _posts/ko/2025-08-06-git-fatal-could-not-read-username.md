---
typora-root-url: ../
layout: single
title: >
   Git 오류 해결: "fatal: could not read Username for 'https://...': terminal prompts disabled"

lang: ko
translation_id: git-fatal-could-not-read-username
header:
   teaser: /images/header_images/overlay_image_git.png
   overlay_image: /images/header_images/overlay_image_git.png
   overlay_filter: 0.5
excerpt: >
    자격 증명 헬퍼를 사용하거나 SSH 인증으로 전환하여 Git 오류 "fatal: could not read Username for 'https://...': terminal prompts disabled"를 해결하는 방법을 알아보세요.
categories:
  - ko_Troubleshooting
tags:
  - Git
  - Authentication
  - HTTPS
  - SSH
  - Credentials
---

## 오류 이해하기

`fatal: could not read Username for 'https://...': terminal prompts disabled` 오류 메시지는 Git이 HTTPS를 통해 원격 저장소와 인증해야 하지만 사용자 이름과 암호를 묻는 메시지를 표시할 수 없는 환경에서 실행될 때 발생합니다.

이는 자동화된 스크립트, CI/CD 파이프라인 또는 상호 작용을 위한 적절한 터미널이 없는 GUI 기반 Git 클라이언트를 사용할 때 자주 발생합니다.

## 문제 상황

명령줄 인터페이스가 없는 스크립트나 도구에서 `git pull` 또는 `git push` 명령을 실행하려고 합니다. 자격 증명을 묻는 대신 명령이 "terminal prompts disabled" 오류와 함께 실패합니다.

## 해결 방법 1: 자격 증명 헬퍼 사용하기

Git 자격 증명 헬퍼는 자격 증명을 저장해 주는 프로그램이므로 Git이 매번 묻지 않아도 됩니다. 이는 일상적인 개발에서 이 문제를 해결하는 가장 일반적이고 안전한 방법입니다.

### 자격 증명 헬퍼 구성 방법

대부분의 운영 체제에는 기본 제공 자격 증명 헬퍼가 있습니다.

-   **Windows:** Git for Windows에는 "Git Credential Manager"가 포함되어 있습니다. 기본적으로 활성화되어 있어야 합니다. 그렇지 않은 경우 다음과 같이 구성할 수 있습니다.
    ```bash
    git config --global credential.helper manager
    ```

-   **macOS:** `osxkeychain` 헬퍼를 사용하여 macOS 키체인에 자격 증명을 안전하게 저장할 수 있습니다.
    ```bash
    git config --global credential.helper osxkeychain
    ```

-   **Linux:** `cache` 헬퍼를 사용하여 자격 증명을 메모리에 잠시 저장하거나 `store`를 사용하여 일반 텍스트 파일에 저장할 수 있습니다(덜 안전함).
    ```bash
    # 1시간(3600초) 동안 캐시
    git config --global credential.helper 'cache --timeout=3600'
    ```

헬퍼를 구성한 후 다음에 인증이 필요한 Git 명령을 실행하면 마지막으로 한 번 사용자 이름과 암호를 묻는 메시지가 표시됩니다. 그러면 헬퍼가 나중에 사용할 수 있도록 저장합니다.

## 해결 방법 2: SSH 인증으로 전환하기

HTTPS 대신 SSH 프로토콜을 인증에 사용할 수 있습니다. SSH는 사용자 이름과 암호 대신 키 쌍(컴퓨터의 개인 키와 Git 서버의 공개 키)을 사용합니다.

### SSH로 전환하는 단계

1.  **SSH 키 생성:** 없는 경우 새 SSH 키를 만듭니다.
    ```bash
    ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
    ```

2.  **Git 호스트에 SSH 키 추가:** 공개 키(일반적으로 `~/.ssh/id_rsa.pub`에 있음)를 복사하여 GitHub, GitLab, Bitbucket 또는 Git 서버의 계정 설정에 추가합니다.

3.  **원격 URL 변경:** 저장소의 원격 URL을 HTTPS에서 SSH 형식으로 업데이트합니다.
    -   HTTPS URL: `https://github.com/user/repo.git`
    -   SSH URL: `git@github.com:user/repo.git`

    다음 명령으로 URL을 변경할 수 있습니다.
    ```bash
    git remote set-url origin git@github.com:user/repo.git
    ```

이제 Git은 인증에 SSH 키를 사용하므로 암호 프롬프트가 필요하지 않습니다.

## 해결 방법 3: URL에 자격 증명 포함하기 (권장하지 않음)

원격 URL에 사용자 이름과 개인용 액세스 토큰(PAT)을 직접 포함할 수 있습니다. **이 방법은 안전하지 않습니다.** 자격 증명이 Git 구성에 일반 텍스트로 저장되기 때문입니다.

```bash
git remote set-url origin https://<your_username>:<your_pat>@github.com/user/repo.git
```

이 방법은 최후의 수단으로만 사용하고 구성 파일에 대한 액세스를 제어할 수 있는 환경에서만 사용하세요.

## 결론

"terminal prompts disabled" 오류는 Git이 자격 증명을 요청할 수 없을 때 발생하는 일반적인 문제입니다. 가장 좋은 해결책은 자격 증명 헬퍼를 구성하거나 SSH 인증으로 전환하는 것입니다. 두 방법 모두 원격 저장소와 상호 작용할 때마다 암호를 수동으로 입력하는 것보다 더 안전하고 편리합니다.
