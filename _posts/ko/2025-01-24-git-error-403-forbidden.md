---
typora-root-url: ../
layout: single
title: "Git \"The requested URL returned error: 403\" 오류 해결 방법"

date: 2025-01-24T07:28:00+09:00
lang: ko
translation_id: git-error-403-forbidden
excerpt: "자격 증명을 업데이트하거나, 개인용 액세스 토큰(PAT)을 사용하거나, 더 안전한 액세스를 위해 SSH 인증으로 전환하여 Git 403 Forbidden 오류를 해결하세요."
seo_description: "자격 증명을 업데이트하거나, 개인용 액세스 토큰(PAT)을 사용하거나, 더 안전한 액세스를 위해 SSH 인증으로 전환하여 Git 403 Forbidden 오류를 해결하세요."
header:
   teaser: /images/header_images/overlay_image_git.png
   overlay_image: /images/header_images/overlay_image_git.png
   overlay_filter: 0.5
   image_description: >
     이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Git \"The requested URL returned error: 403\" 오류 해결 방법
categories:
  - ko_Troubleshooting
tags:
  - Git
  - Authentication
  - 403 Forbidden
  - HTTPS
  - SSH
---


![이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Git \"The requested URL returned error: 403\" 오류 해결 방법](/images/header_images/overlay_image_git.png)
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

## 전문 보완 체크

**Git \"The requested URL returned error: 403\" 오류 해결 방법**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 저장소 루트, 브랜치와 원격 상태, 인덱스와 작업 트리, 인증 또는 네트워크 경계를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

### 신뢰도를 높이는 증거

작업을 바꾸기 전에는 객관적인 증거를 먼저 확인해야 합니다. 쓸 만한 증거에는 `git status`, `git remote -v`, `git branch --show-current`, 실패한 정확한 명령가 포함됩니다. 증거가 서로 맞지 않으면 억지로 하나의 이야기로 합치지 말고 충돌 자체를 남겨야 합니다. 빠른 해결이 한 번 성공했더라도 같은 입력, 계정, 의존성, 기기 상태에서 다시 확인하지 않았다면 아직 확정된 해결책이라고 보기 어렵습니다.

### 검토 표

| 검토 항목 | 확인할 내용 | 중요한 이유 |
| --- | --- | --- |
| 범위 | 이 글이 다루는 정확한 사례 | 조언을 과도하게 적용하지 않게 합니다 |
| 기준 상태 | 변경 전 상태 | 되돌리기와 비교를 가능하게 합니다 |
| 변경 | 실제로 수행한 가장 작은 조치 | 숨은 부작용을 줄입니다 |
| 결과 | 변경 뒤 관찰한 출력 또는 반응 | 기대와 증거를 구분합니다 |
| 재확인 | 결론을 다시 볼 시점 | 글의 정확도를 유지합니다 |

### 예외 상황과 실패 모드

주요 위험은 증상만 고치고 원인을 남기는 상황, 서로 무관한 변경을 같은 테스트에 섞는 상황입니다. 생산 데이터, 개인정보, 돈, 건강, 법적 권리, 보안 복구가 관련되어 있다면 넓은 해결책을 바로 적용하기보다 먼저 증거를 모으는 보수적인 접근이 낫습니다. 같은 제목의 문제라도 환경이 다르면 원인이 달라질 수 있으므로, 독자는 명령이나 결정을 복사하기 전에 자신의 조건이 글의 가정과 맞는지 비교해야 합니다.

### 유지보수 기준

이 안내는 의존성, 운영체제, 빌드 도구가 바뀐 뒤 다시 확인해야 합니다. 좋은 업데이트는 글 전체를 다시 쓰는 것이 아니라 예시, 링크, 명령, 화면, 판단 기준이 현재 동작과 여전히 맞는지 확인하는 일입니다. 기존 결론이 유효하면 확인 날짜를 남기고, 바뀌었다면 무엇이 바뀌었고 왜 이전 조언만으로 부족한지 설명해야 합니다.

### 실행 전 질문

- 문제나 판단이 실제임을 보여 주는 가장 작은 관찰 신호는 무엇인가?
- 공식 출처는 무엇이고, 내부 판단은 어느 부분인가?
- 변경 전에 반드시 캡처해야 할 기록은 무엇인가?
- 어떤 결과가 나오면 이 글의 조언이 맞지 않는다고 볼 것인가?
- 같은 문제가 반복될 때 누가 이 기록을 다시 봐야 하는가?

## 함께 보면 좋은 글

같은 주제 흐름에서 이어서 읽기 좋은 글입니다.

- [SSL: CERTIFICATE_VERIFY_FAILED 오류 해결 방법 (Windows Python)](/ko_troubleshooting/python-certificate-verify-failed/)
- [Permission denied (publickey) 오류 해결 방법 (Windows Git SSH)](/ko_troubleshooting/git-permission-denied-publickey-windows/)
