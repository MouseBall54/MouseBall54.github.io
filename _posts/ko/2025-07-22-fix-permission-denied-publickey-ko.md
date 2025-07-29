---
typora-root-url: ../
layout: single
title: "Permission denied (publickey) 오류 해결 방법 (Windows Git SSH)"
date: 2025-07-22T22:00:00+09:00
excerpt: "Git SSH 연결 시 발생하는 “Permission denied (publickey)” 오류를 SSH 키 생성, 에이전트 등록, 공개키 업로드로 해결하는 방법."
categories:
  - ko_Troubleshooting
tags:
  - Git
  - SSH
  - Windows
  - Authentication
---

## 소개

SSH를 이용한 Git 인증 과정에서 비밀번호 대신 키를 사용함.
키가 없거나 등록되지 않으면 오류 발생.
Windows 환경에서 단계별로 해결 방법을 정리함.

## 오류 내용

```
Permission denied (publickey).
fatal: Could not read from remote repository.
```

SSH 클라이언트가 유효한 키를 찾지 못해 인증에 실패함.

## 주요 원인

* SSH 키를 생성하지 않음.
* SSH 에이전트가 실행 중 아니거나 키가 추가되지 않음.
* Git 호스트에 공개키를 등록하지 않음.
* 파일 권한이나 설정 오류.

## 해결 방법 1: SSH 키 생성

1. Git Bash 실행.
2. 명령어 입력:

   ```bash
   ssh-keygen -t ed25519 -C "you@example.com"
   ```
3. 기본 경로로 저장(Enter).
4. 필요 시 패스프레이즈 설정.

## 해결 방법 2: SSH 에이전트에 키 추가

### Git Bash

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

### PowerShell

1. 에이전트 서비스 시작:

   ```powershell
   Start-Service ssh-agent
   ```
2. 키 추가 (경로 조정):

   ```powershell
   ssh-add C:\Users\<사용자이름>\.ssh\id_ed25519
   ```

## 해결 방법 3: 공개키 Git 호스트에 등록

1. 공개키 복사:

   ```bash
   cat ~/.ssh/id_ed25519.pub
   ```
2. GitHub/GitLab/Bitbucket 설정 이동.
3. SSH 및 GPG 키 추가 메뉴 선택.
4. 공개키 붙여넣기 후 저장.

## 해결 방법 4: SSH 연결 확인

```bash
ssh -T git@github.com
```

성공 시:

```
Hi <username>! You've successfully authenticated.
```

## 추가 팁

* `~/.ssh/config` 파일에 호스트와 키 지정 가능.

  ```text
  Host github.com
    User git
    HostName github.com
    IdentityFile ~/.ssh/id_ed25519
  ```
* 개인 키 권한 설정 (Git Bash):

  ```bash
  chmod 600 ~/.ssh/id_ed25519
  ```
* `ssh-add -l`로 로드된 키 확인.

## 결론

SSH 키 생성, 에이전트 등록, 공개키 업로드 과정을 차례대로 수행하면 “Permission denied (publickey)” 오류를 해결할 수 있음.
