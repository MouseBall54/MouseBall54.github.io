---
typora-root-url: ../
layout: single
title: >
   .gitignore 파일을 사용하여 Git 추적에서 파일 제외하는 방법

lang: ko
translation_id: git-using-gitignore
header:
   teaser: /images/header_images/overlay_image_git.png
   overlay_image: /images/header_images/overlay_image_git.png
   overlay_filter: 0.5
excerpt: >
    `.gitignore` 파일을 생성하고 사용하여 특정 파일 및 디렉터리가 Git 저장소에 추가되는 것을 방지하는 방법을 알아보세요.
categories:
  - ko_Troubleshooting
tags:
  - Git
  - gitignore
  - Tracking
  - Files
---

## `.gitignore`란?

`.gitignore` 파일은 Git에게 프로젝트에서 어떤 파일이나 폴더를 무시할지 알려주는 텍스트 파일입니다. 무시된 파일은 Git에 의해 추적되지 않으므로 스테이징되거나 커밋되지 않습니다. 이는 로그 파일, 컴파일된 코드 또는 `node_modules`와 같은 의존성 폴더와 같이 컴퓨터나 빌드 프로세스에 의해 생성되는 파일에 유용합니다.

## 문제 상황

`git status`를 실행하면 커밋하고 싶지 않은 추적되지 않은 파일의 긴 목록이 표시됩니다. 이들은 시스템 파일, 편집기 구성 파일 또는 빌드 아티팩트일 수 있습니다.

```bash
git status
On branch main
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .DS_Store
        logs/debug.log
        build/
        node_modules/
```

이러한 파일을 커밋하면 저장소가 불필요하게 부풀려지고 다른 협업자에게 문제를 일으킬 수 있습니다.

## 해결 방법

### 1. `.gitignore` 파일 생성하기

Git 저장소의 루트 디렉터리에 `.gitignore`라는 이름의 파일을 만듭니다.

텍스트 편집기나 명령줄 도구를 사용하여 만들 수 있습니다.
```bash
touch .gitignore
```

### 2. `.gitignore`에 패턴 추가하기

`.gitignore` 파일을 열고 무시하려는 파일 및 디렉터리에 대한 패턴을 추가합니다. 각 패턴은 새 줄에 있어야 합니다.

```gitignore
# macOS 시스템 파일 무시
.DS_Store

# 로그 파일 무시
logs/
*.log

# 빌드 출력 디렉터리 무시
build/

# 의존성 디렉터리 무시
node_modules/
```

-   `#`: 해시로 시작하는 줄은 주석입니다.
-   `logs/`: 전체 `logs` 디렉터리를 무시합니다.
-   `*.log`: `.log` 확장자를 가진 모든 파일(예: `debug.log`, `error.log`)을 무시합니다.
-   `build/`: `build` 디렉터리를 무시합니다.
-   `node_modules/`: `node_modules` 디렉터리를 무시합니다.

### 3. `.gitignore` 파일 커밋하기

`.gitignore` 파일 자체는 저장소에 커밋해야 합니다. 이렇게 하면 모든 협업자에게 동일한 무시 규칙이 적용됩니다.

```bash
git add .gitignore
git commit -m "Add .gitignore file"
```

이제 `git status`를 실행하면 무시된 파일이 더 이상 추적되지 않은 파일 목록에 나타나지 않습니다.

## 이미 추적된 파일 무시하기

실수로 무시해야 할 파일을 커밋했다면 어떻게 해야 할까요? 단순히 `.gitignore`에 파일을 추가하는 것만으로는 Git이 추적을 멈추지 않습니다.

먼저 `git rm --cached`를 사용하여 Git에게 파일 추적을 중지하도록 알려야 합니다.

예를 들어, `config.local` 파일 추적을 중지하려면:
1.  `.gitignore` 파일에 `config.local`을 추가합니다.
2.  다음 명령을 실행합니다.
    ```bash
    git rm --cached config.local
    ```
3.  변경 사항을 커밋합니다.
    ```bash
    git commit -m "Stop tracking config.local"
    ```

`--cached` 옵션은 Git의 추적에서 파일을 제거하지만 로컬 디렉터리에는 그대로 유지됩니다.

## 전역 `.gitignore`

시스템의 모든 저장소에 대한 전역 `.gitignore` 파일을 만들 수도 있습니다. 이는 운영 체제나 편집기 관련 파일을 무시하는 데 유용합니다.

1.  예를 들어 `~/.gitignore_global` 파일을 만듭니다.
2.  Git이 이 파일을 사용하도록 구성합니다.
    ```bash
    git config --global core.excludesfile ~/.gitignore_global
    ```
3.  이 파일에 전역 패턴을 추가합니다.

## 결론

`.gitignore` 파일을 사용하는 것은 저장소를 깨끗하게 유지하고 중요한 소스 코드에 집중하는 데 필수적입니다. 불필요한 파일이 커밋되고 공유되는 것을 방지합니다. 다양한 프로그래밍 언어 및 프레임워크에 대한 많은 템플릿이 온라인에서 제공되므로 시작하는 데 도움이 될 수 있습니다.
