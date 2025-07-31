---
typora-root-url: ../
layout: single
title: "Git 오류 'fatal: not a git repository' 해결 방법"
date: 2025-07-30T11:00:00+09:00
excerpt: "'fatal: not a git repository'는 Git 명령을 Git 저장소가 아닌 디렉터리에서 실행했을 때 발생하는 일반적인 오류입니다. 이 글에서는 원인과 해결 방법을 알아봅니다."
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
---

## 'fatal: not a git repository' 오류란?

`fatal: not a git repository (or any of the parent directories): .git` 메시지는 현재 디렉터리나 그 상위 경로에 `.git` 폴더가 없어 Git 저장소로 인식되지 않을 때 나타나는 오류다.
Git은 `.git` 디렉터리를 통해 버전 관리 정보를 추적하므로, 이 디렉터리가 없으면 어떤 Git 명령도 실행할 수 없다.

## 주요 원인

이 오류의 원인은 크게 두 가지로 나눌 수 있다.

### 1. Git 저장소가 아닌 디렉터리에서 명령 실행

가장 흔한 원인이다. 사용자가 Git 프로젝트 디렉터리가 아닌 곳에서 `git status`, `git pull` 같은 명령을 실행하려고 할 때 발생한다.
예를 들어, `C:\Users\MyUser` 같은 개인 홈 디렉터리에서 Git 명령을 실행하면 이 오류를 마주하게 된다.

### 2. `.git` 디렉터리 손상 또는 삭제

드물지만 `.git` 디렉터리가 실수로 삭제되거나 이름이 변경된 경우, 또는 내부 파일이 손상된 경우에도 발생할 수 있다.
이 경우 Git은 더 이상 해당 디렉터리를 저장소로 인식하지 못한다.

## 해결 방법

해결 방법은 원인에 따라 간단하게 적용할 수 있다.

### 1. 올바른 디렉터리로 이동

대부분의 경우, 올바른 Git 프로젝트 디렉터리로 이동하는 것만으로 문제가 해결된다.
`cd` 명령어를 사용하여 작업하려는 Git 저장소의 루트 디렉터리로 이동한 후 다시 Git 명령을 실행한다.

```bash
# 다른 디렉터리에 있다고 가정
cd C:\path\to\your\git-project

# 이제 Git 명령이 정상적으로 작동
git status
```

만약 프로젝트 경로가 기억나지 않는다면, 파일 탐색기나 `dir` / `ls` 명령어를 통해 프로젝트 위치를 먼저 확인해야 한다.

### 2. 새로운 Git 저장소 초기화

만약 현재 디렉터리를 새로운 Git 저장소로 만들고 싶다면 `git init` 명령을 사용하면 된다.
이 명령은 현재 디렉터리에 `.git` 폴더를 생성하여 새로운 Git 저장소로 초기화한다.

```bash
# 새로운 프로젝트 디렉터리 생성
mkdir my-new-project
cd my-new-project

# Git 저장소로 초기화
git init
```

이후에는 `git add`, `git commit` 등의 명령을 정상적으로 사용할 수 있다.

### 3. 기존 원격 저장소 복제 (Clone)

만약 작업하려는 프로젝트가 GitHub, GitLab 등 원격 저장소에 이미 존재한다면 `git clone` 명령으로 로컬에 복제하는 것이 올바른 방법이다.

```bash
# 원격 저장소를 로컬에 복제
git clone https://github.com/example/repository.git

# 복제된 디렉터리로 이동
cd repository

# Git 명령 실행
git status
```

`git clone`은 원격 저장소의 모든 내역과 함께 `.git` 디렉터리를 자동으로 생성하므로 즉시 작업을 시작할 수 있다.

## 결론

'fatal: not a git repository' 오류는 대부분 사용자가 잘못된 위치에서 Git 명령을 실행했기 때문에 발생한다.
작업 전 항상 현재 디렉터리가 올바른 Git 저장소인지 확인하는 습관을 들이는 것이 중요하다.
만약 새로운 프로젝트를 시작하거나 기존 프로젝트를 내려받는 경우라면 `git init` 또는 `git clone`을 적절히 사용하여 저장소를 올바르게 설정해야 한다.

```