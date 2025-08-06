---
typora-root-url: ../
layout: single
title: >
   `git bisect`를 사용하여 버그를 유발한 커밋 찾기
date: 2025-08-06T10:55:00+09:00
header:
   teaser: /images/header_images/overlay_image_git.png
   overlay_image: /images/header_images/overlay_image_git.png
   overlay_filter: 0.5
excerpt: >
    `git bisect`를 사용하여 커밋 히스토리에서 이진 검색을 수행하고 버그를 유발한 정확한 커밋을 신속하게 찾아내는 방법에 대한 단계별 가이드입니다.
categories:
  - ko_Troubleshooting
tags:
  - Git
  - Bisect
  - Debugging
  - Bug
  - Commit
---

## `git bisect`란?

`git bisect`는 Git의 강력한 디버깅 도구입니다. 프로젝트의 커밋 히스토리를 통해 자동화된 이진 검색을 수행하여 버그를 유발한 특정 커밋을 찾는 데 도움이 됩니다.

각 커밋을 하나씩 수동으로 체크아웃하고 테스트하는 대신, `git bisect`는 검색 공간을 빠르게 좁혀 프로세스를 훨씬 빠르고 효율적으로 만듭니다.

## 문제 상황

일주일 전에는 애플리케이션이 제대로 작동했지만 지금은 기능이 손상되었습니다. 마지막으로 알려진 정상 상태와 현재 손상된 상태 사이에 수백 개의 커밋이 있습니다. 문제를 일으킨 정확한 커밋을 찾는 것은 매우 시간이 많이 걸립니다.

## 해결 방법: `git bisect` 사용하기

다음은 `git bisect`를 사용하여 문제가 있는 커밋을 찾는 방법입니다.

### 1. Bisect 프로세스 시작하기

먼저, bisect 세션을 시작해야 합니다.

```bash
git bisect start
```

### 2. 나쁜 커밋과 좋은 커밋 표시하기

다음으로 Git에 두 가지를 알려줘야 합니다.
-   버그가 있는 "나쁜" 커밋.
-   버그가 없는 "좋은" 커밋.

일반적으로 현재 커밋(`HEAD`)이 나쁜 커밋입니다.
```bash
git bisect bad HEAD
```

그런 다음, 제대로 작동했다고 알고 있는 커밋의 해시나 태그를 제공합니다.
```bash
git bisect good <commit_hash_or_tag>
# 예시:
git bisect good v1.0.0
```

### 3. 테스트하고 반복하기

좋은 커밋과 나쁜 커밋을 표시하면 `git bisect`는 그 사이의 중간에 있는 커밋을 체크아웃합니다. 그러면 다음과 같은 메시지가 표시됩니다.

```
Bisecting: 675 revisions left to test after this (roughly 10 steps)
```

이제 이 커밋에서 코드를 테스트하여 버그가 있는지 확인해야 합니다.
-   버그가 **있는 경우**, Git에 이 커밋이 "나쁘다"고 알립니다.
    ```bash
    git bisect bad
    ```
-   버그가 **없는 경우**, Git에 이 커밋이 "좋다"고 알립니다.
    ```bash
    git bisect good
    ```

그러면 Git은 새로운 좋은 경계와 나쁜 경계 사이의 중간에 있는 다른 커밋을 체크아웃합니다. 이 테스트 및 커밋을 `good` 또는 `bad`로 표시하는 과정을 반복합니다.

### 4. 첫 번째 나쁜 커밋 식별하기

몇 단계 후 Git은 가능성을 단일 커밋으로 좁힙니다. 다음과 같은 메시지를 인쇄합니다.

```
c1a2b3d is the first bad commit
commit c1a2b3d
Author: John Doe <john.doe@example.com>
Date:   Mon Aug 5 10:00:00 2025 +0000

    Refactor the login module

... file changes ...
```

이것이 버그를 유발한 커밋입니다. 이제 변경 사항을 검토하여 무엇이 잘못되었는지 이해할 수 있습니다.

### 5. Bisect 세션 종료하기

나쁜 커밋을 찾았으면 bisect 세션을 종료하여 원래 상태(`HEAD`)로 돌아가야 합니다.

```bash
git bisect reset
```

## 프로세스 자동화하기

코드가 좋은지 나쁜지를 판단할 수 있는 스크립트(예: 테스트 스위트)가 있는 경우 테스트 단계를 자동화할 수도 있습니다.

`git bisect run` 명령은 스크립트를 인수로 받습니다. Git은 각 단계에서 스크립트를 실행합니다.
-   스크립트가 코드 `0`으로 종료되면 커밋이 `good`으로 표시됩니다.
-   다른 코드( `1`에서 `127` 사이, `125` 제외)로 종료되면 `bad`로 표시됩니다.

```bash
# 예시: 테스트 스크립트 사용
git bisect run npm test
```

## 결론

`git bisect`는 코드베이스의 회귀를 신속하게 추적하는 데 매우 유용한 도구입니다. 버그를 유발하는 커밋 검색을 자동화하여 디버깅 프로세스에서 상당한 시간과 노력을 절약할 수 있습니다.
