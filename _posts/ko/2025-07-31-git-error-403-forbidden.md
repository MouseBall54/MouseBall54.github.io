---
typora-root-url: ../
layout: single
title: "Git \"The requested URL returned error: 403\" 오류 해결 방법"

lang: ko
translation_id: git-error-403-forbidden
excerpt: "자격 증명을 업데이트하거나, 개인용 액세스 토큰(PAT)을 사용하거나, 더 안전한 액세스를 위해 SSH 인증으로 전환하여 Git 403 Forbidden 오류를 해결하세요."
header:
   teaser: /images/header_images/overlay_image_git.png
   overlay_image: /images/header_images/overlay_image_git.png
   overlay_filter: 0.5
categories:
  - ko_Troubleshooting
tags:
  - Git
  - Authentication
  - 403 Forbidden
  - HTTPS
  - SSH
---

## 서론

`fatal: unable to access '...': The requested URL returned error: 403`은 Git에서 인증 또는 권한 문제를 나타내는 일반적인 오류다. "403 Forbidden" 상태 코드는 서버가 요청을 이해했지만 승인을 거부하고 있음을 의미한다. 본질적으로, 사용자는 권한이 없는 작업(`push`, `pull`, `clone` 등)을 시도하고 있는 것이다. 이 가이드에서는 이 오류의 주요 원인과 해결 방법을 다룬다.

## 원인 1: 부정확하거나 오래된 자격 증명

403 오류의 가장 흔한 원인은 Git이 사용 중인 자격 증명(사용자 이름 및 비밀번호)이 부정확하거나, 만료되었거나, 해지된 경우다. 특히 GitHub, GitLab, Bitbucket과 같은 많은 Git 호스팅 제공업체들이 더 안전한 방법을 위해 비밀번호 기반 인증을 중단하면서 이 문제가 더 흔해졌다.

### 해결책: 개인용 액세스 토큰(PAT) 사용

계정 비밀번호 대신 개인용 액세스 토큰(PAT)을 사용해야 한다. PAT는 HTTPS를 통해 Git에 인증할 때 비밀번호 대신 사용할 수 있는 무작위로 생성된 문자열이다. Git 제공업체의 설정에서 PAT를 생성하고 특정 권한(스코프)을 부여할 수 있다.

**PAT 사용 단계:**
1.  **PAT 생성**:
    -   **GitHub**: `Settings` > `Developer settings` > `Personal access tokens` > `Generate new token`으로 이동한다.
    -   **GitLab**: `User Settings` > `Access Tokens`로 이동한다.
    -   **Bitbucket**: `Personal settings` > `App passwords`로 이동한다.
    토큰에 필요한 스코프(예: 전체 저장소 액세스를 위한 `repo`)를 부여해야 한다. 토큰을 즉시 복사하라—다시는 볼 수 없다.
2.  **자격 증명 업데이트**: Git이 비밀번호를 묻는 메시지를 표시하면, 비밀번호 대신 PAT를 붙여넣는다.
    ```bash
    git pull
    Username for 'https://github.com': your-username
    Password for 'https://your-username@github.com': [여기에 토큰을 붙여넣으세요]
    ```
3.  **자격 증명 도우미 업데이트 (선택 사항)**: 운영 체제가 이전 비밀번호를 캐시했을 수 있다. 시스템의 자격 증명 관리자에서 업데이트해야 할 수 있다.
    -   **Windows**: 제어판의 `자격 증명 관리자`로 이동하여 Git 제공업체 항목(예: `git:https://github.com`)을 찾는다. 편집하여 이전 비밀번호를 PAT로 교체한다.
    -   **macOS**: `키체인 접근`을 열고 Git 제공업체를 검색하여 비밀번호를 업데이트한다.
    -   **Linux**: `libsecret`이나 `gnome-keyring`과 같은 자격 증명 도우미를 구성해야 할 수 있다.

## 원인 2: 불충분한 저장소 권한

인증은 올바르게 되었지만, 사용 중인 계정이 접근하려는 저장소에 필요한 권한이 없는 경우다.

-   읽기 전용 접근 권한만 있는 저장소에 푸시하려고 할 수 있다.
-   저장소가 비공개이며 접근 권한을 부여받지 못했을 수 있다.
-   조직에 속해 있는 경우, 관리자에 의해 접근이 제한되었을 수 있다.

### 해결책: 권한 확인

-   **역할 확인**: GitHub, GitLab 또는 Bitbucket의 저장소 페이지에서 자신의 접근 수준(예: Read, Write, Maintain, Admin)을 확인한다.
-   **소유자에게 연락**: 접근 권한이 있어야 한다고 생각되면, 저장소 소유자나 조직 관리자에게 연락하여 올바른 권한을 부여해달라고 요청한다.

## 원인 3: 잘못된 인증 방법 사용 (HTTPS vs. SSH)

때때로 저장소가 SSH 연결을 선호하거나 허용하도록 구성될 수 있다. HTTPS URL을 사용하려고 하면 접근이 거부될 수 있다.

### 해결책: SSH로 전환

Git 인증에 SSH를 사용하는 것은 HTTPS보다 종종 더 안전하고 편리하다. 사용자 이름과 비밀번호/토큰 대신 키 쌍을 사용하여 인증한다.

**SSH로 전환하는 단계:**
1.  **기존 SSH 키 확인**:
    ```bash
    ls -al ~/.ssh
    ```
    `id_rsa.pub` 또는 `id_ed25519.pub`라는 이름의 파일을 찾는다.
2.  **새 SSH 키 생성** (없는 경우):
    ```bash
    ssh-keygen -t ed25519 -C "your_email@example.com"
    ```
    안내에 따라 키를 저장한다.
3.  **Git 제공업체에 SSH 키 추가**:
    -   공개 키 파일(`id_ed25519.pub`)의 내용을 복사한다.
        ```bash
        cat ~/.ssh/id_ed25519.pub
        ```
    -   Git 제공업체의 사용자 프로필에 있는 SSH 키 설정으로 이동하여 키를 붙여넣는다.
4.  **저장소의 원격 URL 업데이트**: 원격 URL을 HTTPS에서 SSH 형식으로 변경한다.
    ```bash
    # 현재 원격 URL 보기
    git remote -v
    # https://github.com/user/repo.git 와 같이 보일 것이다

    # URL 업데이트
    git remote set-url origin git@github.com:user/repo.git
    ```
    이제 `push` 또는 `pull`을 할 때 Git은 인증을 위해 SSH 키를 사용하게 되며, 403 오류가 해결될 것이다.

자격 증명, 권한 및 인증 방법을 확인함으로써 Git 403 Forbidden 오류를 효과적으로 해결하고 수정할 수 있다.
