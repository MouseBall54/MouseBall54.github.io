---
typora-root-url: ../
layout: single
title: "Git 오류 해결: Permission Denied (publickey)"
date: 2025-07-31T15:00:00+09:00
excerpt: "SSH 키를 올바르게 생성하고, ssh-agent에 추가하고, Git 호스팅 제공업체에 등록하여 Git의 'Permission denied (publickey)' 오류를 해결하는 방법을 알아봅니다."
categories:
  - ko_Troubleshooting
tags:
  - Git
  - SSH
  - Authentication
  - Troubleshooting
---

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
