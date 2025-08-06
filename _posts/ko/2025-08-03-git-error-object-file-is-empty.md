---
typora-root-url: ../
layout: single
title: >
    Git "error: object file ... is empty" 해결 방법

lang: ko
translation_id: git-error-object-file-is-empty
header:
    teaser: /images/header_images/overlay_image_git.png
    overlay_image: /images/header_images/overlay_image_git.png
    overlay_filter: 0.5
excerpt: >
    Git에서 "error: object file ... is empty"는 Git 객체 파일이 손상되어 내용이 비어있을 때 발생합니다. 이 글에서는 오류의 원인과 해결 방법을 알아봅니다.
categories:
    - ko_Troubleshooting
tags:
    - Git
    - Object File
    - Corruption
---

## Git "error: object file ... is empty"란?

이 오류는 Git 저장소의 내부 데이터베이스에 있는 객체(object) 파일 중 하나가 비어 있거나 손상되었음을 의미합니다. Git은 모든 데이터를 `.git/objects` 디렉터리 내에 "객체"(커밋, 트리, 블롭 등)로 저장합니다. 어떤 이유로든 이 파일들 중 하나가 0바이트 크기의 빈 파일이 되면, Git은 해당 객체를 읽을 수 없으므로 이 오류를 보고합니다.

이 오류는 `git status`, `git pull`, `git checkout` 등 저장소의 데이터를 읽어야 하는 거의 모든 Git 명령어에서 발생할 수 있습니다.

## 오류의 일반적인 원인

1.  **비정상적인 시스템 종료**: Git이 객체 파일을 디스크에 쓰는 도중에 컴퓨터가 갑자기 꺼지거나 충돌하는 경우 파일이 불완전하게 쓰여 빈 파일로 남을 수 있습니다.
2.  **디스크 공간 부족**: 디스크 공간이 꽉 찬 상태에서 Git이 새 객체를 쓰려고 하면 실패하여 0바이트 파일이 생성될 수 있습니다.
3.  **파일 시스템 오류**: 하드 드라이브의 물리적 또는 논리적 오류로 인해 파일 내용이 손상될 수 있습니다.
4.  **외부 프로그램의 간섭**: 바이러스 백신이나 파일 동기화 프로그램(예: Dropbox, Google Drive)이 `.git` 디렉터리의 파일을 잘못 처리하여 손상을 유발할 수 있습니다.

## 오류 해결 방법

**경고**: 아래의 해결 방법들은 `.git` 디렉터리를 직접 조작할 수 있습니다. 진행하기 전에 반드시 **저장소 전체를 백업**하세요.

### 방법 1: 손상된 객체 파일 제거 후 `git fsck` 실행

가장 간단한 방법은 오류 메시지에 명시된 빈 객체 파일을 직접 삭제하는 것입니다.

1.  **오류 메시지에서 파일 경로 확인**:
    오류 메시지는 보통 다음과 같은 형식을 가집니다:
    `error: object file .git/objects/ab/cdef... is empty`
    여기서 `ab/cdef...`가 객체 파일의 경로와 이름입니다.

2.  **해당 파일 삭제**:
    터미널에서 다음 명령을 실행하여 빈 객체 파일을 삭제합니다.
    ```bash
    # Linux/macOS
    rm .git/objects/ab/cdef...

    # Windows
    del .git\objects\ab\cdef...
    ```

3.  **저장소 상태 확인**:
    `git fsck` (file system check) 명령을 실행하여 저장소에 다른 문제가 있는지 확인합니다.
    ```bash
    git fsck --full
    ```
    `dangling blob`이나 `dangling commit` 같은 메시지가 나올 수 있지만, 이는 보통 심각한 문제가 아닙니다. 하지만 `missing` 관련 오류가 나타난다면 다른 객체도 손상되었을 수 있습니다.

4.  **원격 저장소에서 다시 가져오기 (가능한 경우)**:
    만약 손상된 객체가 원격 저장소(예: GitHub)에 존재한다면, `git fetch`를 통해 복구할 수 있습니다.
    ```bash
    git fetch origin
    ```

### 방법 2: 로컬 저장소를 새로 복제(Clone)

원격 저장소에 최신 변경 사항이 모두 푸시되어 있다면, 가장 안전하고 확실한 방법은 로컬 저장소를 삭제하고 원격 저장소에서 새로 복제하는 것입니다.

1.  현재 로컬 저장소의 이름을 변경하거나 삭제합니다.
    ```bash
    # 현재 디렉터리 밖으로 이동
    cd ..

    # 폴더 이름 변경 (백업용)
    mv your-repo-name your-repo-name-backup
    ```

2.  원격 저장소에서 다시 복제합니다.
    ```bash
    git clone <your-remote-repository-url>
    ```

이 방법은 커밋하지 않은 로컬 변경 사항이나 스태시(stash)가 없는 경우에 가장 이상적입니다.

### 방법 3: 다른 개발자의 저장소에서 객체 복사

팀 프로젝트를 진행 중이고 원격 저장소에 푸시되지 않은 커밋이 로컬에 있는 경우, 다른 팀원의 정상적인 저장소에서 손상된 객체 파일을 복사해올 수 있습니다.

1.  손상된 객체 파일의 경로(`.git/objects/ab/cdef...`)를 확인합니다.
2.  다른 팀원의 컴퓨터에서 해당 경로의 파일을 찾아 복사합니다.
3.  내 로컬 저장소의 동일한 위치에 붙여넣습니다.
4.  `git fsck`로 저장소 상태를 다시 확인합니다.

## 예방 조치

-   `.git` 디렉터리를 파일 동기화 서비스의 동기화 대상에서 제외합니다.
-   중요한 작업을 마친 후에는 주기적으로 원격 저장소에 푸시합니다.
-   디스크 공간을 정기적으로 확인합니다.

## 결론

`error: object file ... is empty` 오류는 Git의 내부 데이터베이스 손상으로 인해 발생하며, 보통 시스템의 비정상적인 종료나 외부 요인에 의해 유발됩니다. 가장 간단한 해결책은 손상된 객체를 제거하고 원격 저장소에서 다시 가져오는 것이며, 문제가 심각하거나 원격 저장소가 최신 상태일 경우 새로 복제하는 것이 가장 안전합니다. 작업 전에는 항상 저장소를 백업하는 습관을 들이는 것이 중요합니다.
