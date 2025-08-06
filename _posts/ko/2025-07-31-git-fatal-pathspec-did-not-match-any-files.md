---
typora-root-url: ../
layout: single
title: "Git 오류 해결: pathspec '...' did not match any files"

lang: ko
translation_id: git-fatal-pathspec-did-not-match-any-files
excerpt: "Git의 'pathspec did not match any files' 오류를 오타 확인, 파일 경로 검증, 특수 문자 처리 방법 이해를 통해 해결하세요. 이 흔한 문제를 진단하고 고치는 법을 배웁니다."
header:
   teaser: /images/header_images/overlay_image_git.png
   overlay_image: /images/header_images/overlay_image_git.png
   overlay_filter: 0.5
categories:
  - ko_Troubleshooting
tags:
  - Git
  - pathspec
  - Troubleshooting
  - Version Control
---

## "pathspec '...' did not match any files" 오류란?

Git을 사용하다 보면 `fatal: pathspec '...' did not match any files`라는 오류 메시지를 마주칠 수 있다. 이 오류는 보통 `git add`나 `git rm` 같은 명령을 Git이 찾을 수 없는 파일에 대해 실행하려고 할 때 발생한다. 여기서 "pathspec"은 Git에게 작업을 지시하려는 파일이나 디렉터리의 경로를 의미한다.

이 오류는 명령에 지정한 파일이나 경로가 현재 컨텍스트에서 Git이 아는 어떤 파일과도 일치하지 않는다는 뜻이다.

## 주요 원인과 해결 방법

이 오류의 가장 흔한 원인과 해결 방법을 살펴보자.

### 1. 파일 이름 또는 경로의 오타

가장 빈번한 원인은 파일 이름이나 경로에 단순한 오타가 있는 경우다.

#### 문제 명령어

`my-script.js`라는 파일이 있는데, 다음과 같이 입력했다고 가정해 보자.

```bash
git add my_script.js
```

Git은 다음과 같이 응답할 것이다.

```
fatal: pathspec 'my_script.js' did not match any files
```

#### 해결 방법

파일 이름과 경로에 오타가 없는지 다시 확인한다. 대소문자, 하이픈(-), 밑줄(_), 파일 확장자가 올바른지 확인해야 한다. `ls` (Windows에서는 `dir`) 명령어를 사용하여 현재 디렉터리의 파일 목록을 보고 올바른 이름을 확인할 수 있다.

```bash
ls # macOS/Linux에서
dir # Windows에서
```

올바른 이름을 확인한 후 명령어를 다시 실행한다.

```bash
git add my-script.js
```

### 2. 잘못된 디렉터리에서 명령어 실행

올바른 디렉터리에 있지 않으면 Git은 파일을 찾을 수 없다. 예를 들어, `my-script.js`가 `src/` 디렉터리에 있는데 프로젝트의 루트 디렉터리에서 다음 명령을 실행하면 실패할 것이다.

```bash
# 루트 디렉터리에 있다고 가정
git add my-script.js 
```

#### 해결 방법

`cd`를 사용하여 올바른 디렉터리로 이동하거나, 현재 위치에서 파일의 전체 경로를 제공하면 된다.

**옵션 A: 디렉터리 변경**

```bash
cd src
git add my-script.js
```

**옵션 B: 전체 경로 제공**

```bash
# 루트 디렉터리에서
git add src/my-script.js
```

### 3. 파일이 추적되지 않거나 무시됨

작업하려는 파일이 `.gitignore` 파일에 포함되어 있거나, Git 저장소의 일부가 아닐 수 있다 (예: 아직 생성되지 않음).

#### 문제 시나리오

만약 `.gitignore` 파일에 `*.log`라는 줄이 포함되어 있다면, 로그 파일을 추가하려는 모든 시도는 실패할 것이다.

```bash
git add application.log
```

Git은 이 파일을 무시하도록 설정되어 있기 때문에 `pathspec` 오류를 표시할 것이다.

#### 해결 방법

먼저 `.gitignore` 파일을 확인하여 추가하려는 파일과 일치하는 패턴이 있는지 확인한다. 무시된 파일을 강제로 추가하고 싶다면 `-f` 또는 `--force` 옵션을 사용할 수 있다.

```bash
git add -f application.log
```

하지만 강제 추가는 신중해야 한다. 대부분의 파일은 민감한 데이터나 로컬 설정을 저장소에서 제외하는 등 타당한 이유로 무시된다.

새로운 파일을 추적하고 싶다면, `.gitignore`의 광범위한 패턴에 포함되지 않는지 확인해야 한다.

### 4. 특수 문자 또는 와일드카드 사용

때때로 셸이 Git보다 먼저 특수 문자나 와일드카드(`*`, `?`, `[]`)를 해석할 수 있다. 이는 예상치 못한 동작으로 이어질 수 있다.

#### 문제 명령어

특수 문자가 포함된 디렉터리의 모든 파일을 추가하고 싶을 때, 셸이 경로를 잘못 확장할 수 있다.

```bash
# 셸이 문자를 잘못 해석하면 실패할 수 있다
git add "files with spaces/"
```

#### 해결 방법

경로를 따옴표로 감싸서 셸이 해석하지 못하게 한다. 이렇게 하면 전체 문자열이 Git에 직접 전달된다.

```bash
git add "path/with special characters/my file.txt"
```

와일드카드를 사용하는 경우, 추가하려는 파일과 일치하는지 확인해야 한다. 예를 들어, `src` 디렉터리의 모든 `.js` 파일을 추가하려면 다음과 같이 한다.

```bash
git add 'src/*.js'
```

작은따옴표를 사용하면 셸이 와일드카드를 확장하는 것을 막고 Git이 대신 처리하게 할 수 있다.

## 결론

`pathspec '...' did not match any files` 오류는 보통 간단히 해결할 수 있다. 거의 항상 오타, 잘못된 디렉터리, 또는 `.gitignore` 규칙 문제로 귀결된다. 이러한 일반적인 원인들을 체계적으로 확인하면 문제를 신속하게 해결하고 다시 작업으로 돌아갈 수 있다.
