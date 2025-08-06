---
typora-root-url: ../
layout: single
title: >
    Git "fatal: index file corrupt" 해결 방법

lang: ko
translation_id: git-fatal-index-file-corrupt
header:
    teaser: /images/header_images/overlay_image_git.png
    overlay_image: /images/header_images/overlay_image_git.png
    overlay_filter: 0.5
excerpt: >
    Git에서 "fatal: index file corrupt"는 스테이징 영역의 상태를 추적하는 인덱스 파일이 손상되었을 때 발생합니다. 이 글에서는 오류의 원인과 해결 방법을 알아봅니다.
categories:
    - ko_Troubleshooting
tags:
    - Git
    - Index
    - Corruption
---

## Git "fatal: index file corrupt"란?

`fatal: index file corrupt` 오류는 Git의 핵심 파일 중 하나인 **인덱스(index) 파일**이 손상되었음을 의미합니다. 인덱스 파일(`.git/index`)은 "스테이징 영역(Staging Area)"이라고도 불리며, 다음 커밋에 포함될 변경 사항들의 목록을 추적하는 중요한 파일입니다. 이 파일이 손상되면 Git은 어떤 파일이 추적되고 있는지, 어떤 내용이 스테이징되었는지 알 수 없게 되어 대부분의 Git 명령이 실패하게 됩니다.

## 오류의 일반적인 원인

`object file is empty` 오류와 유사하게, 인덱스 파일 손상은 주로 다음과 같은 상황에서 발생합니다:

1.  **비정상적인 종료**: Git 명령(특히 `git add`, `git reset`, `git commit` 등 인덱스를 수정하는 명령) 실행 중에 컴퓨터가 갑자기 꺼지는 경우.
2.  **파일 시스템 오류**: 디스크 자체의 문제로 파일 내용이 깨지는 경우.
3.  **외부 프로그램의 간섭**: 파일 동기화 프로그램이나 일부 백신 프로그램이 `.git/index` 파일을 잘못 건드리는 경우.
4.  **동시에 여러 Git 프로세스 실행**: 하나의 저장소에서 동시에 여러 Git 명령이 인덱스 파일을 수정하려고 할 때 충돌이 발생하여 손상될 수 있습니다.

## 오류 해결 방법

**경고**: `.git` 디렉터리를 직접 조작하기 전에, 만일을 대비해 **저장소 전체를 백업**하는 것이 좋습니다.

인덱스 파일은 Git 저장소의 다른 객체들과 달리, 문제가 생겼을 때 비교적 안전하게 **재생성**할 수 있습니다. 인덱스는 기본적으로 현재 브랜치의 `HEAD` 커밋 상태와 워킹 디렉터리의 상태를 기반으로 다시 만들어질 수 있습니다.

### 방법 1: 인덱스 파일 삭제 후 리셋

가장 일반적이고 효과적인 해결 방법은 손상된 인덱스 파일을 삭제하고 Git이 새로 생성하도록 하는 것입니다.

1.  **`.git/index` 파일 삭제**:
    저장소의 루트 디렉터리에서 다음 명령을 실행하여 인덱스 파일을 제거합니다.
    ```bash
    # Linux/macOS
    rm .git/index

    # Windows
    del .git\index
    ```
    이 작업을 수행하면 스테이징했던 모든 변경 사항이 사라집니다 (커밋되지 않은 변경 사항은 워킹 디렉터리에 그대로 남아있습니다).

2.  **Git 상태 리셋**:
    `git reset` 명령을 실행하여 `HEAD` 커밋 기준으로 인덱스를 새로 생성합니다. 이 명령은 워킹 디렉터리의 파일들은 건드리지 않습니다.
    ```bash
    git reset
    ```
    이제 `git status` 명령을 실행하면, 마지막 커밋 이후 변경된 모든 파일들이 "Changes not staged for commit" (스테이징되지 않은 변경 사항) 목록에 나타날 것입니다.

3.  **변경 사항 다시 스테이징**:
    필요한 변경 사항들을 다시 `git add` 명령으로 스테이징합니다.
    ```bash
    git add <file1> <file2> ...
    # 또는 모든 변경 사항을 스테이징
    git add .
    ```

### 방법 2: 로컬 저장소를 새로 복제 (Clone)

만약 위 방법으로 해결되지 않거나, 로컬에 중요한 커밋되지 않은 변경 사항이 없다면 원격 저장소에서 새로 복제하는 것이 가장 깔끔한 해결책입니다.

1.  현재 로컬 저장소 폴더의 이름을 바꾸거나 삭제합니다.
    ```bash
    cd ..
    mv your-repo-name your-repo-name-backup
    ```

2.  원격 저장소에서 다시 복제합니다.
    ```bash
    git clone <your-remote-repository-url>
    ```

## 예방 조치

-   Git 명령 실행 중에는 컴퓨터를 강제로 종료하지 않도록 주의합니다.
-   `.git` 디렉터리는 파일 동기화 대상에서 제외하는 것이 안전합니다.
-   중요한 변경 사항은 작업 후 바로 커밋하고 원격 저장소에 푸시하는 습관을 들입니다.

## 결론

`fatal: index file corrupt` 오류는 당황스러울 수 있지만, 다행히 인덱스 파일은 Git 저장소의 핵심 데이터(객체)와는 분리되어 있어 상대적으로 쉽게 복구할 수 있습니다. 손상된 인덱스 파일을 삭제하고 `git reset`을 통해 새로 생성하는 방법으로 대부분의 문제를 해결할 수 있습니다. 이 과정에서 스테이징했던 내용은 사라지지만, 워킹 디렉터리의 실제 파일 변경 내용은 보존되므로 안전합니다.
