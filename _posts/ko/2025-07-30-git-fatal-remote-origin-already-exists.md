---
typora-root-url: ../
layout: single
title: "Git 오류 'fatal: remote origin already exists' 해결 방법"

lang: ko
translation_id: git-fatal-remote-origin-already-exists
excerpt: "'fatal: remote origin already exists'는 원격 저장소를 추가하려 할 때 'origin'이라는 이름이 이미 사용 중일 때 발생하는 오류입니다. 이 글에서는 원인과 해결 방법을 알아봅니다."
header:
   teaser: /images/header_images/overlay_image_git.png
   overlay_image: /images/header_images/overlay_image_git.png
   overlay_filter: 0.5
categories:
  - ko_Troubleshooting
tags:
  - Git
  - Troubleshooting
  - Version Control
  - Remote
---

## 'fatal: remote origin already exists' 오류란?

`fatal: remote origin already exists` 오류는 `git remote add origin <저장소_URL>` 명령을 실행했을 때, 이미 `origin`이라는 이름의 원격 저장소가 설정되어 있는 경우에 발생한다.
Git에서 원격 저장소의 별칭(이름)은 고유해야 하므로, 중복된 이름을 사용하려고 하면 이 오류 메시지가 나타난다.
`origin`은 `git clone` 명령을 사용할 때 기본적으로 생성되는 원격 저장소의 기본 이름이다.

## 주요 원인

### 1. `git clone` 이후 `git remote add` 실행
`git clone`으로 원격 저장소를 복제하면, Git은 자동으로 해당 원격 저장소를 `origin`이라는 이름으로 등록한다.
이후 사용자가 같은 저장소나 다른 저장소를 `origin`이라는 이름으로 또 추가하려고 시도하면 오류가 발생한다.

```bash
# 저장소를 클론하면 'origin'이 자동으로 설정됨
git clone https://github.com/user/repo.git
cd repo

# 이미 'origin'이 존재하므로 오류 발생
git remote add origin https://github.com/user/repo.git
# fatal: remote origin already exists.
```

### 2. 수동으로 원격 저장소를 추가한 후 다시 추가
`git init`으로 로컬 저장소를 만든 후, `git remote add origin` 명령으로 원격 저장소를 연결했다.
이후 같은 명령을 다시 실행하면 당연히 이름이 중복되어 오류가 발생한다.

## 해결 방법

해결 방법은 현재 설정된 `origin`을 어떻게 처리할지에 따라 달라진다.

### 1. 기존 원격 저장소의 URL 변경
만약 기존에 설정된 `origin`의 URL을 단순히 다른 URL로 변경하고 싶다면, `set-url` 명령을 사용하면 된다.

```bash
# 현재 설정된 원격 저장소 확인
git remote -v
# origin  https://github.com/old/repo.git (fetch)
# origin  https://github.com/old/repo.git (push)

# 'origin'의 URL을 새로운 URL로 변경
git remote set-url origin https://github.com/new/repo.git

# 변경된 내용 확인
git remote -v
# origin  https://github.com/new/repo.git (fetch)
# origin  https://github.com/new/repo.git (push)
```
이 방법은 기존의 `origin` 이름을 유지하면서 주소만 바꾸고 싶을 때 가장 적합하다.

### 2. 기존 원격 저장소 삭제 후 새로 추가
기존 `origin` 설정이 완전히 잘못되었거나 더 이상 필요 없다면, 삭제하고 새로 추가할 수 있다.

```bash
# 기존 'origin' 원격 저장소 삭제
git remote remove origin

# 새로운 원격 저장소를 'origin'으로 추가
git remote add origin https://github.com/another/repo.git

# 설정된 내용 확인
git remote -v
# origin  https://github.com/another/repo.git (fetch)
# origin  https://github.com/another/repo.git (push)
```

### 3. 다른 이름으로 원격 저장소 추가
`origin`이라는 이름은 유지하면서, 또 다른 원격 저장소를 추가하고 싶다면 다른 이름을 사용하면 된다.
예를 들어, `upstream`이나 `backup` 같은 이름을 사용할 수 있다.

```bash
# 'origin'은 그대로 두고, 'upstream'이라는 이름으로 새 원격 저장소 추가
git remote add upstream https://github.com/different/repo.git

# 설정된 원격 저장소 목록 확인
git remote -v
# origin    https://github.com/original/repo.git (fetch)
# origin    https://github.com/original/repo.git (push)
# upstream  https://github.com/different/repo.git (fetch)
# upstream  https://github.com/different/repo.git (push)
```
이 방법은 여러 원격 저장소를 동시에 관리해야 할 때 유용하다.

## 결론

`fatal: remote origin already exists` 오류는 Git의 원격 저장소 이름이 중복될 때 발생하는 자연스러운 현상이다.
`git remote -v` 명령으로 현재 설정된 원격 저장소 목록을 먼저 확인하는 습관을 들이는 것이 중요하다.
상황에 맞게 `set-url`로 URL을 변경하거나, `remove`로 삭제 후 다시 추가하거나, 혹은 새로운 이름으로 다른 원격 저장소를 추가하는 방법을 사용하면 쉽게 문제를 해결할 수 있다.
