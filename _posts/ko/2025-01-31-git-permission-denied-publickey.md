---
typora-root-url: ../
layout: single
title: "Git 오류 해결: Permission Denied (publickey)"

date: 2025-01-31T07:35:00+09:00
lang: ko
translation_id: git-permission-denied-publickey
excerpt: "SSH 키를 올바르게 생성하고, ssh-agent에 추가하고, Git 호스팅 제공업체에 등록하여 Git의 'Permission denied (publickey)' 오류를 해결하는 방법을 알아봅니다."
seo_description: "SSH 키를 올바르게 생성하고, ssh-agent에 추가하고, Git 호스팅 제공업체에 등록하여 Git의 'Permission denied (publickey)' 오류를 해결하는 방법을 알아봅니다."
header:
   teaser: /images/header_images/overlay_image_git.png
   overlay_image: /images/header_images/overlay_image_git.png
   overlay_filter: 0.5
   image_description: >
     이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Git 오류 해결: Permission Denied (publickey)
categories:
  - ko_Troubleshooting
tags:
  - Git
  - SSH
  - Authentication
  - Troubleshooting
---


![이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Git 오류 해결: Permission Denied (publickey)](/images/header_images/overlay_image_git.png)
## "Permission denied (publickey)" 오류란 무엇인가?

`Permission denied (publickey)` 오류는 SSH 프로토콜을 사용하여 원격 Git 저장소(예: GitHub, GitLab, Bitbucket)에 연결하려고 할 때 발생하는 일반적인 문제이다. 이는 원격 서버가 제공한 SSH 키로 사용자를 인증할 수 없었기 때문에 연결을 거부했음을 의미한다.

기본적으로, 사용자의 컴퓨터가 저장소에 접근할 수 있는 올바른 자격 증명을 가지고 있음을 서버에 증명하지 못한 것이다.

## 일반적인 원인

1.  **SSH 키 없음**: 로컬 컴퓨터에서 SSH 키를 생성하지 않았다.
2.  **SSH 키가 에이전트에 추가되지 않음**: SSH 키는 존재하지만 `ssh-agent`(SSH 키를 처리하는 백그라운드 프로그램)가 이를 알지 못한다.
3.  **공개 키가 Git 호스트에 추가되지 않음**: SSH 키는 있지만, 공개 키 부분을 Git 호스팅 서비스(예: GitHub)의 계정에 업로드하지 않았다.
4.  **잘못된 저장소 URL**: 원격 저장소에 SSH URL 대신 HTTPS URL을 사용하고 있다. SSH 인증은 SSH URL(예: `git@github.com:user/repo.git`)에서만 작동한다.
5.  **권한 문제**: `.ssh` 디렉터리 또는 키 파일의 권한이 너무 개방적이어서 SSH가 보안상의 이유로 이를 무시한다.

## 해결 방법

이 오류를 해결하기 위한 단계별 가이드는 다음과 같다.

### 1단계: 기존 SSH 키 확인

먼저, 이미 SSH 키가 있는지 확인한다. 기본적으로 키는 `~/.ssh` 디렉터리(Linux/macOS의 경우) 또는 `C:\Users\사용자이름\.ssh`(Windows의 경우)에 저장된다.

```bash
ls -al ~/.ssh
# id_rsa.pub, id_ed25519.pub 등과 같은 이름의 파일을 찾는다
```

`.pub` 파일이 보이면 이미 키가 있는 것이다. 3단계로 건너뛸 수 있다.

### 2단계: 새 SSH 키 생성

키가 없으면 새 키를 생성한다. Ed25519 알고리즘이 권장된다.

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

"Enter a file in which to save the key"라는 메시지가 표시되면 Enter 키를 눌러 기본 위치를 수락한다. 추가 보안을 위해 선택적으로 암호를 입력할 수 있다.

### 3단계: ssh-agent에 SSH 키 추가

`ssh-agent`가 키를 관리한다. 에이전트가 실행 중인지 확인하고 새 키를 추가한다.

```bash
# 백그라운드에서 ssh-agent 시작
eval "$(ssh-agent -s)"

# SSH 개인 키를 에이전트에 추가
ssh-add ~/.ssh/id_ed25519
```

### 4단계: Git 호스트에 공개 키 추가

저장소를 호스팅하는 서비스에 공개 키를 제공해야 한다.

1.  **공개 키를 클립보드에 복사한다.**

    ```bash
    # macOS/Linux의 경우
    cat ~/.ssh/id_ed25519.pub | clip

    # Windows의 경우 (Git Bash에서)
    cat ~/.ssh/id_ed25519.pub | clip
    # clip 명령어를 사용할 수 없는 경우, 파일을 열어 내용을 수동으로 복사한다
    ```

2.  **Git 호스트 웹사이트로 이동한다**:
    - **GitHub**: `Settings` > `SSH and GPG keys` > `New SSH key`로 이동한다.
    - **GitLab**: `Preferences` > `SSH Keys`로 이동한다.
3.  **키 붙여넣기**: 설명적인 제목(예: "내 업무용 노트북")을 지정하고 복사한 공개 키를 "Key" 필드에 붙여넣는다.

### 5단계: SSH 연결 테스트

키를 추가한 후 Git 호스트에 대한 연결을 테스트한다.

```bash
# GitHub의 경우
ssh -T git@github.com

# GitLab의 경우
ssh -T git@gitlab.com
```

`Hi [사용자이름]! You've successfully authenticated...`와 같은 메시지가 표시되어야 한다. 이 메시지가 보이면 설정이 올바른 것이다.

### 6단계: SSH URL을 사용하고 있는지 확인

마지막으로, 저장소의 원격 URL이 HTTPS가 아닌 SSH 버전으로 설정되어 있는지 확인한다.

```bash
# 현재 원격 URL 확인
git remote -v

# https:// URL이 표시되면 변경한다
git remote set-url origin git@github.com:사용자이름/저장소이름.git
```

이 단계를 따르면 `Permission denied (publickey)` 오류를 해결하고 원격 저장소에 안전하게 연결할 수 있다.

## 전문 보완 체크

**Git 오류 해결: Permission Denied (publickey)**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 저장소 루트, 브랜치와 원격 상태, 인덱스와 작업 트리, 인증 또는 네트워크 경계를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

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

## 적용 검토 시나리오

독자가 **Git 오류 해결: Permission Denied (publickey)**의 첫 번째 권장 조치를 이미 시도했지만 결과가 여전히 불확실하다고 가정해 봅니다. 다음 단계는 여러 해결책을 한꺼번에 시험하는 것이 아니라 짧은 감사 기록을 만드는 것입니다. 먼저 어떤 판단을 하려는지 한 문장으로 쓰고, 환경을 한 문장으로 적고, 관찰된 결과를 한 문장으로 남깁니다. 그다음 저장소 루트, 브랜치와 원격 상태, 인덱스와 작업 트리, 인증 또는 네트워크 경계를 이미 확보한 사실과 대조합니다. 이렇게 해야 글이 서로 끊어진 팁 목록이 아니라 검증 가능한 절차가 됩니다.

### 감사 기록 양식

| 항목 | 예시 기준 | 이유 |
| --- | --- | --- |
| 관찰 | 조치 전 실제로 본 내용 | 기준 상태를 객관화합니다 |
| 증거 | `git status`, `git remote -v` | 판단을 기록에 연결합니다 |
| 가정 | 믿고 있지만 아직 증명하지 못한 내용 | 숨은 추정을 드러냅니다 |
| 조치 | 한 번에 하나의 변경 | 결과의 원인을 추적하게 합니다 |
| 중단 기준 | 멈추고 도움을 요청할 조건 | 반복적인 시행착오를 줄입니다 |

### 품질 경계

같은 결과가 통제된 재확인 뒤에도 반복될 때만 이 안내를 강한 결론으로 보아야 합니다. 계정, 기기, 데이터 샘플, 의존성 버전, 계약 조건, 공식 규칙이 달라졌다면 결론의 강도를 낮추고 가설로 다루는 편이 안전합니다. 검색 독자는 급한 문제를 안고 들어오는 경우가 많아 맥락을 건너뛰기 쉽습니다. 전문적인 글은 위험한 판단을 천천히 하게 만들면서도 다음 행동은 분명하게 제시해야 합니다.

## 함께 보면 좋은 글

같은 주제 흐름에서 이어서 읽기 좋은 글입니다.

- [SSL: CERTIFICATE_VERIFY_FAILED 오류 해결 방법 (Windows Python)](/ko_troubleshooting/python-certificate-verify-failed/)
- [Permission denied (publickey) 오류 해결 방법 (Windows Git SSH)](/ko_troubleshooting/git-permission-denied-publickey-windows/)
