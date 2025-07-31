---
typora-root-url: ../
layout: single
title: "Git 'error: src refspec ... does not match any' 오류 해결 방법"
date: 2025-07-31T23:00:00+09:00
header:
   teaser: /images/header_images/overlay_image_git.png
   overlay_image: /images/header_images/overlay_image_git.png
   overlay_filter: 0.5
excerpt: >
  푸시하려는 브랜치가 로컬에 존재하고 이름이 올바르게 입력되었는지 확인하여 Git "src refspec ... does not match any" 오류를 해결하는 방법을 알아봅니다.
categories:
  - ko_Troubleshooting
tags:
  - Git
  - Push
  - Branch
  - Version Control
---

원격 저장소로 변경 사항을 푸시하려고 할 때, `error: src refspec <브랜치-이름> does not match any.` 라는 당황스러운 오류를 만날 수 있습니다. 이 메시지는 Git이 푸시하려는 로컬 브랜치를 찾을 수 없다는 의미입니다.

이 포스트에서는 이 오류의 일반적인 원인과 해결 방법을 설명합니다.

### 이 오류의 원인은 무엇인가요?

"src refspec ... does not match any" 오류는 일반적으로 두 가지 간단한 이유 중 하나로 발생합니다.

1.  **로컬에 브랜치가 존재하지 않음**: 로컬 저장소에서 생성하거나 체크아웃하지 않은 브랜치를 푸시하려고 합니다.
2.  **브랜치 이름의 오타**: `git push` 명령어에 브랜치 이름을 잘못 입력했습니다.

예를 들어, `git push origin master`를 실행했지만 실제 로컬 브랜치 이름이 `main`이라면, Git은 푸시할 `master`라는 브랜치를 찾지 못합니다.

### 오류 해결 방법

해결책은 푸시하기 전에 브랜치 이름을 확인하고 로컬에 존재하는지 확인하는 것입니다.

#### 1단계: 로컬 브랜치 목록 확인하기

먼저, 로컬 저장소에 있는 모든 브랜치의 이름을 확인합니다. `git branch` 명령어로 이 작업을 수행할 수 있습니다.

```bash
git branch
```

이 명령어는 모든 로컬 브랜치를 나열하고 현재 작업 중인 브랜치를 강조 표시합니다.

```
  feature/new-login
* main
  hotfix/bug-123
```

이 목록에서 푸시하려는 브랜치의 정확한 철자를 확인할 수 있습니다.

#### 2단계: `git push` 명령어 수정하기

올바른 브랜치 이름을 확인했다면, `git push` 명령어를 다시 시도할 수 있습니다.

예를 들어, 브랜치 이름이 `master`가 아닌 `main`이라는 것을 발견했다면 다음을 실행합니다.

```bash
git push origin main
```

피처 브랜치를 푸시하려는 경우, 이름이 `git branch` 출력에서 본 것과 정확히 일치하는지 확인하세요.

```bash
# 잘못된 경우
git push origin feature/new-login-typo

# 올바른 경우
git push origin feature/new-login
```

#### 3단계: 브랜치가 존재하지 않으면 생성하기

만약 `git branch`가 푸시하려는 브랜치를 보여주지 않는다면, 이는 브랜치가 로컬에 존재하지 않는다는 의미입니다. 먼저 브랜치를 생성해야 할 수 있습니다.

올바른 커밋 위에 있다면, 현재 `HEAD` 위치에서 새 브랜치를 생성할 수 있습니다.

```bash
# 'new-feature'라는 새 브랜치 생성
git branch new-feature

# 새 브랜치로 전환
git checkout new-feature
```

또는 한 번에 두 작업을 모두 수행할 수 있습니다.

```bash
git checkout -b new-feature
```

브랜치를 생성하고 전환한 후, 이제 원격 저장소로 푸시할 수 있습니다.

```bash
git push origin new-feature
```

### 현재 브랜치 푸시하기

오타를 피하는 유용한 팁은 `HEAD`를 사용하여 현재 브랜치를 푸시하는 것입니다. Git의 이 특별한 포인터는 항상 현재 작업 중인 브랜치를 가리킵니다.

```bash
git push origin HEAD
```

이 명령어는 Git에게 현재 브랜치를 같은 이름의 원격 브랜치로 푸시하라고 지시합니다.

### 결론

"src refspec ... does not match any" 오류는 흔하고 보통 해결하기 쉬운 문제입니다. 거의 항상 오타나 존재하지 않는 로컬 브랜치를 푸시하려고 할 때 발생합니다. `git branch`를 사용하여 로컬 브랜치를 확인함으로써, 푸시 명령어를 쉽게 수정하고 코드를 원격 저장소로 보낼 수 있습니다.
