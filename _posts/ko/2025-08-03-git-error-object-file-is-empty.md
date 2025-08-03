---
typora-root-url: ../
layout: single
title: >
    Git error: object file ... is empty 해결 방법
date: 2025-08-03T11:00:00+09:00
header:
   teaser: /images/header_images/overlay_image_git.png
   overlay_image: /images/header_images/overlay_image_git.png
   overlay_filter: 0.5
excerpt: >
    Git 저장소의 객체 파일이 손상되어 비어 있을 때 발생하는 `error: object file ... is empty` 오류의 원인과 복구 방법을 알아봅니다.
categories:
  - ko_Troubleshooting
tags:
  - Git
  - Git Error
  - git fsck
  - Repository Corruption
---

## 문제 상황

`git status`, `git pull`, `git checkout` 등 다양한 Git 명령을 실행할 때 다음과 같은 오류 메시지가 나타날 수 있습니다.

```
error: object file .git/objects/xx/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx is empty
fatal: loose object xx... (stored in .git/objects/xx/...) is corrupt
```

이 오류는 Git이 내부적으로 데이터를 저장하는 **객체(object) 파일이 손상되었거나, 어떤 이유로 0바이트의 빈 파일이 되었음**을 의미합니다. Git은 커밋, 트리, 블롭(파일 내용) 등의 모든 정보를 객체 파일로 `.git/objects/` 디렉터리 안에 저장합니다. 이 파일들 중 하나라도 문제가 생기면 저장소의 무결성이 깨져 정상적인 작업이 불가능해집니다.

이러한 손상은 보통 다음과 같은 경우에 발생할 수 있습니다.
- 컴퓨터가 갑작스럽게 종료되거나 재부팅될 때
- 디스크 공간 부족 또는 하드웨어 오류
- 파일 동기화 프로그램(Dropbox, Google Drive 등)의 비정상적인 동작

## 해결 방법

이 문제는 로컬 저장소의 손상에 해당하므로, 대부분 원격 저장소(GitHub, GitLab 등)의 데이터는 안전합니다. 해결의 핵심은 **손상된 로컬 객체를 제거하고 원격 저장소에서 건강한 객체를 다시 받아오는 것**입니다.

### 1단계: 저장소 상태 확인하기

먼저 `git fsck` (file system check) 명령을 사용하여 저장소에 다른 문제는 없는지 확인합니다.

```bash
git fsck --full
```

이 명령은 저장소의 무결성을 검사하고, 위와 같은 `dangling` 또는 `corrupt` 객체 목록을 보여줄 것입니다.

### 2단계: 손상된 객체 파일 직접 삭제하기

오류 메시지에 명시된 경로의 빈 객체 파일을 직접 삭제합니다.

-   오류 메시지: `error: object file .git/objects/xx/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx is empty`
-   삭제할 파일 경로: `.git/objects/xx/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

Windows의 파일 탐색기나 macOS/Linux의 `rm` 명령을 사용하여 해당 파일을 제거합니다.

```bash
# Linux / macOS / Git Bash
rm .git/objects/xx/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

**주의:** `.git` 디렉터리 안의 파일을 수정하는 것은 위험할 수 있으므로, 정확한 경로의 파일만 삭제하도록 주의해야 합니다.

### 3단계: 원격 저장소에서 데이터 다시 가져오기

손상된 객체를 삭제했으므로, 이제 원격 저장소에서 최신 데이터를 다시 가져와 로컬 저장소를 복구합니다.

```bash
git fetch
```

`git fetch` 명령은 원격 저장소에는 있지만 로컬에는 없는 모든 객체를 다운로드합니다. 이 과정에서 삭제했던 손상된 객체도 건강한 버전으로 다시 받아오게 됩니다.

### 4단계: 최종 확인

다시 `git fsck`를 실행하여 문제가 해결되었는지 확인합니다.

```bash
git fsck
```

아무런 오류 메시지가 출력되지 않는다면 저장소가 성공적으로 복구된 것입니다. 이제 평소처럼 `git pull`이나 `git status` 등의 명령을 사용할 수 있습니다.

만약 `git fetch` 후에도 문제가 계속된다면, 가장 확실한 방법은 현재 로컬 저장소를 백업하고 원격 저장소에서 새로 `clone`하는 것입니다.

```bash
# 1. 현재 디렉터리 밖으로 이동
cd ..

# 2. 기존 저장소를 백업용으로 이름 변경
mv your-project-name your-project-name-backup

# 3. 원격 저장소에서 새로 클론
git clone <your-remote-repository-url>
```

## 결론

`error: object file ... is empty` 오류는 Git 객체 파일 손상으로 인해 발생하지만, 원격 저장소가 있다면 보통 쉽게 해결할 수 있습니다.

1.  `git fsck`로 문제를 확인합니다.
2.  오류 메시지에 나온 **빈 객체 파일을 직접 삭제**합니다.
3.  `git fetch`로 원격 저장소에서 데이터를 다시 받아옵니다.
4.  다시 `git fsck`로 해결되었는지 확인합니다.

이러한 문제를 예방하기 위해 중요한 작업을 마친 후에는 항상 원격 저장소에 `push`하는 습관을 들이는 것이 좋습니다.
