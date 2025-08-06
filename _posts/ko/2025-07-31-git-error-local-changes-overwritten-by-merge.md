---
typora-root-url: ../
layout: single
title: >
    "Git "error: Your local changes... would be overwritten by merge" 오류 해결 방법"

lang: ko
translation_id: git-error-local-changes-overwritten-by-merge
excerpt: "pull 또는 merge 전에 로컬 변경 사항을 스태시, 커밋 또는 폐기하여 Git 병합 오류를 해결하세요."
header:
   teaser: /images/header_images/overlay_image_git.png
   overlay_image: /images/header_images/overlay_image_git.png
   overlay_filter: 0.5
categories:
  - ko_Troubleshooting
tags:
  - Git
  - Merge
  - Stash
  - Commit
  - Version Control
---

## 서론

Git 오류 메시지 `error: Your local changes to the following files would be overwritten by merge`는 사용자의 커밋되지 않은 작업을 보호하기 위한 조치다. 이 오류는 로컬 작업 디렉터리에 수정한 내용이 `git pull` 또는 `git merge` 작업으로 업데이트될 파일과 충돌할 때 발생한다. 이 가이드에서는 이 오류가 발생하는 이유를 설명하고 이를 해결하기 위한 세 가지 일반적인 방법을 제공한다.

## 이 오류는 왜 발생할까?

Git의 주요 임무는 코드 버전을 관리하는 것이다. 원격 저장소에서 `pull`하거나 브랜치를 `merge`할 때, Git은 로컬 작업 디렉터리의 파일을 업데이트해야 한다. 만약 Git이 업데이트해야 하는 파일을 사용자가 이미 변경한 경우, Git은 작업 내용을 덮어쓰는 것을 방지하기 위해 프로세스를 중단한다.

예를 들어:
1. 사용자가 `style.css` 파일을 수정했다.
2. 이 변경 사항을 커밋하지 **않았다**.
3. 그 사이 동료가 원격 저장소에 `style.css`의 새 버전을 푸시했다.
4. 사용자가 `git pull`을 실행하면, Git은 새 `style.css`를 가져와 로컬 파일을 업데이트하려고 시도한다.
5. Git은 커밋되지 않은 변경 사항을 발견하고 작업을 보호하기 위해 "overwritten by merge" 오류와 함께 작업을 중단한다.

## 해결 방법

이 문제를 해결하는 세 가지 주요 방법이 있다. 상황에 가장 적합한 방법을 선택하면 된다.

### 방법 1: 변경 사항 커밋하기

만든 변경 사항이 완료되었고 유지하고 싶다면, 가장 간단한 해결책은 pull 또는 merge 전에 변경 사항을 커밋하는 것이다.

**단계:**
1.  **변경 사항 스테이징하기**: 수정된 파일을 스테이징 영역에 추가한다.
    ```bash
    git add . 
    # 또는 더 구체적으로: git add <file1> <file2>
    ```
2.  **변경 사항 커밋하기**: 설명이 포함된 메시지와 함께 로컬 저장소에 변경 사항을 저장한다.
    ```bash
    git commit -m "나의 설명적인 커밋 메시지"
    ```
3.  **다시 Pull 또는 Merge하기**: 이제 로컬 변경 사항이 안전하게 커밋되었으므로 원래 작업을 계속할 수 있다.
    ```bash
    git pull
    # 또는 git merge <branch-name>
    ```
    만약 당신의 커밋과 들어오는 변경 사항 간에 충돌이 발생하면, Git은 이제 병합 충돌을 해결하라고 안내하지만, 당신의 작업을 덮어쓰지는 않는다.

### 방법 2: 변경 사항 스태시하기

변경 사항이 아직 커밋할 준비가 되지 않았지만 최신 업데이트를 가져오고 싶다면, `git stash`가 완벽한 도구다. 이 명령은 커밋되지 않은 변경 사항을 일시적으로 보관하여 작업 디렉터리를 깨끗하게 만들어준다.

**단계:**
1.  **로컬 변경 사항 스태시하기**: 이렇게 하면 수정 사항이 저장되고 파일이 마지막 커밋(`HEAD`) 상태로 되돌아간다.
    ```bash
    git stash
    ```
2.  **Pull 또는 Merge하기**: 이제 작업 디렉터리가 깨끗해졌으므로 안전하게 pull 또는 merge를 할 수 있다.
    ```bash
    git pull
    ```
3.  **스태시한 변경 사항 적용하기**: pull이 완료된 후, 새로 업데이트된 코드 위에 변경 사항을 다시 적용할 수 있다.
    ```bash
    git stash pop
    # 또는 git stash apply
    ```
    `git stash pop`은 변경 사항을 적용하고 스태시 목록에서 해당 스태시를 제거한다. `git stash apply`는 변경 사항을 적용하지만 스태시를 유지하여 여러 브랜치에 적용하고 싶을 때 유용하다.

### 방법 3: 변경 사항 폐기하기

로컬 변경 사항이 더 이상 필요 없고 원격 저장소의 최신 버전을 가져오고 싶다면, 변경 사항을 폐기할 수 있다.

**경고**: 이 작업은 되돌릴 수 없다. 로컬 수정 사항이 영구적으로 손실된다.

**단계:**
1.  **모든 로컬 변경 사항 폐기하기**: 이 명령은 작업 디렉터리를 정리하고 커밋되지 않은 모든 변경 사항을 제거한다.
    ```bash
    git reset --hard HEAD
    ```
    또는 특정 파일의 변경 사항만 폐기하려면:
    ```bash
    git checkout -- <file-name>
    ```
2.  **Pull 또는 Merge하기**: 깨끗한 작업 디렉터리에서 이제 문제없이 pull을 할 수 있다.
    ```bash
    git pull
    ```

이 세 가지 방법(커밋, 스태시, 폐기) 중 하나를 선택하여 로컬 작업을 안전하게 관리하고 "overwritten by merge" 오류를 해결할 수 있다.
