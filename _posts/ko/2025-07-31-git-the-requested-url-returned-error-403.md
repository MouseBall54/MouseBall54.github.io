---
typora-root-url: ../
layout: single
title: "Git 오류 해결: The requested URL returned error: 403"

lang: ko
translation_id: git-the-requested-url-returned-error-403
excerpt: "Git의 '403 Forbidden' 오류를 자격 증명 업데이트, 개인용 액세스 토큰(PAT) 사용, 또는 저장소 권한 확인을 통해 해결하세요. 이 흔한 인증 문제를 해결하는 단계를 배웁니다."
header:
   teaser: /images/header_images/overlay_image_git.png
   overlay_image: /images/header_images/overlay_image_git.png
   overlay_filter: 0.5
categories:
  - ko_Troubleshooting
tags:
  - Git
  - Authentication
  - Error 403
  - Troubleshooting
---

## "The requested URL returned error: 403" 오류란?

원격 저장소에서 `git push`, `git pull`, 또는 `git clone`을 시도할 때 `fatal: The requested URL returned error: 403`이라는 오류 메시지가 나타날 수 있다. 이는 "Forbidden(금지됨)"을 의미하는 HTTP 상태 코드다. Git의 맥락에서는 제공한 자격 증명으로는 저장소에 접근할 권한이 없다는 것을 나타낸다.

이것은 순전히 인증 또는 권한 부여 문제다. 로컬 저장소의 코드나 히스토리와는 관련이 없다.

## 주요 원인과 해결 방법

403 오류의 가장 흔한 원인과 해결 방법을 알아보자.

### 1. 부정확하거나 만료된 자격 증명

저장된 Git 자격 증명(사용자 이름과 비밀번호)이 올바르지 않거나 만료되었을 수 있다. 특히 최근에 GitHub, GitLab, Bitbucket과 같은 Git 호스팅 서비스에서 비밀번호를 변경한 경우 흔히 발생한다.

#### 해결 방법: 자격 증명 업데이트

가장 쉬운 해결책은 저장된 자격 증명을 업데이트하는 것이다. 대부분의 최신 Git 클라이언트는 이 정보를 저장하기 위해 자격 증명 관리자를 사용한다.

**Windows:**

1.  제어판에서 **자격 증명 관리자**를 연다.
2.  **Windows 자격 증명** 탭으로 이동한다.
3.  Git 호스팅 서비스에 대한 항목(예: `git:https://github.com`)을 찾는다.
4.  **편집**을 클릭하여 비밀번호를 업데이트하거나 **제거**를 클릭하여 항목을 삭제한다. 제거하면 다음에 연결할 때 Git이 사용자 이름과 비밀번호를 다시 요청할 것이다.

**macOS:**

1.  **키체인 접근** 응용 프로그램을 연다.
2.  Git 호스팅 서비스(예: "github.com")를 검색한다.
3.  "internet password" 항목을 찾아 업데이트하거나 삭제한다. 다음 시도 시 Git이 자격 증명을 요청할 것이다.

**Linux:**

자격 증명 도우미가 설정된 경우, Git이 이전 자격 증명을 잊도록 강제할 수 있다. 정확한 명령어는 설정에 따라 다르지만, 도우미를 재설정하거나 저장된 자격 증명 파일(예: `~/.git-credentials`)을 수동으로 편집하여 지울 수 있다.

더 간단한 접근 방식은 원격 URL에 사용자 이름을 포함하여 비밀번호 입력을 강제하는 것이다.

```bash
git remote set-url origin https://<YOUR_USERNAME>@github.com/<USERNAME>/<REPO>.git
```

다음에 푸시나 풀을 할 때 Git이 비밀번호를 물어볼 것이다.

### 2. 비밀번호 대신 개인용 액세스 토큰(PAT) 미사용

GitHub를 포함한 대부분의 주요 Git 제공업체는 더 이상 HTTPS를 통한 Git 작업에 비밀번호 인증을 허용하지 않는다. 대신 **개인용 액세스 토큰(PAT)**을 사용해야 한다.

#### 해결 방법: PAT 생성 및 사용

1.  **PAT 생성:**
    *   **GitHub:** **Settings > Developer settings > Personal access tokens > Tokens (classic)**로 이동하여 **Generate new token**을 클릭한다. 설명적인 이름을 지정하고 필요한 범위(예: 전체 저장소 접근을 위한 `repo`)를 선택한다.
    *   **GitLab:** **Preferences > Access Tokens**로 이동한다.
    *   **Bitbucket:** **Personal settings > App passwords**로 이동한다.

2.  **PAT 복사:** 토큰을 즉시 안전한 곳에 저장한다. 다시는 볼 수 없다.

3.  **PAT 사용:** Git이 비밀번호를 요청하면 대신 PAT를 입력한다.

자격 증명이 캐시된 경우, 이전 섹션의 단계에 따라 먼저 지운다. 그런 다음, 다음에 Git 작업을 수행할 때 사용자 이름과 비밀번호로 PAT를 사용한다.

### 3. 불충분한 저장소 권한

403 오류는 계정이 시도하려는 작업을 수행할 권한이 없다는 것을 의미할 수도 있다. 예를 들어, 읽기 전용 접근 권한만 있는 저장소에 푸시하려고 할 수 있다.

#### 해결 방법: 권한 확인

*   **협력자 접근:** 저장소 소유자에게 올바른 권한(예: 변경 사항을 푸시하기 위한 "Write" 또는 "Maintain" 접근)으로 협력자로 추가되었는지 확인한다.
*   **조직/팀 접근:** 저장소가 조직에 속한 경우, 적절한 접근 수준을 가진 팀의 구성원인지 확인한다.
*   **포크 및 풀 리퀘스트:** 쓰기 접근 권한이 없는 경우, 표준 워크플로는 저장소를 포크하고, 변경 사항을 자신의 포크에 푸시한 다음, 원래 저장소로 풀 리퀘스트를 여는 것이다.

### 4. 단일 로그인(SSO) 문제

조직이 Git 제공업체와 단일 로그인(SSO)을 사용하는 경우, SSO로 보호되는 저장소와 함께 사용하기 위해 PAT를 승인해야 할 수 있다.

#### 해결 방법: SSO에 대한 PAT 승인

GitHub에서 PAT를 생성할 때, 조직의 리소스와 함께 사용하기 위해 **"Configure SSO"** 또는 **"Authorize"** 토큰 옵션이 표시된다. 이 단계를 반드시 완료해야 한다. 기존 PAT가 있는 경우, 토큰 설정 페이지에서 SSO에 대해 활성화해야 할 수 있다.

## 결론

Git의 `403 Forbidden` 오류는 거의 항상 인증 또는 권한과 관련이 있다. 자격 증명을 체계적으로 확인하고, 개인용 액세스 토큰으로 전환하며, 저장소 접근 권한을 확인함으로써 이 오류를 신속하게 해결할 수 있다. 확실하지 않을 때는 이전 자격 증명을 지우고 새로운 PAT로 다시 시도하는 것부터 시작하는 것이 좋다.
