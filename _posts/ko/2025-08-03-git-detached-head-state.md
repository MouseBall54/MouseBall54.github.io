---
typora-root-url: ../
layout: single
title: >
    Git "Detached HEAD" 상태 해결 방법
date: 2025-08-03T10:10:00+09:00
header:
   teaser: /images/header_images/overlay_image_git.png
   overlay_image: /images/header_images/overlay_image_git.png
   overlay_filter: 0.5
excerpt: >
    Git의 "Detached HEAD" 상태가 무엇인지, 왜 발생하는지, 그리고 작업을 잃지 않고 안전하게 브랜치로 돌아가는 방법을 이해합니다.
categories:
  - ko_Troubleshooting
tags:
  - Git
  - Version Control
  - Detached HEAD
  - Branching
---

## Git의 "Detached HEAD" 상태란?

Git에서 `HEAD`는 일반적으로 현재 작업 중인 브랜치의 최신 커밋을 가리키는 포인터입니다. 예를 들어, `main` 브랜치에 있다면 `HEAD`는 `main`을 가리킵니다.

"Detached HEAD" 상태는 `HEAD`가 브랜치 대신 특정 커밋을 직접 가리킬 때 발생합니다. 이는 더 이상 어떤 브랜치에도 속해 있지 않음을 의미합니다. 코드를 둘러보고, 실험적인 변경을 하고, 심지어 커밋도 할 수 있지만, 이 새로운 커밋들은 어떤 브랜치에도 속하지 않습니다. 이 커밋들은 "떠다니는" 상태이며, 저장하지 않고 다른 브랜치로 전환하면 쉽게 잃어버릴 수 있습니다.

이 상태는 종종 코드의 이전 버전을 검사하기 위해 의도적으로 들어가지만, 실수로 이 상태에 들어간 개발자에게는 혼란스러울 수 있습니다.

## 어떻게 Detached HEAD 상태가 되는가?

이 상태에 들어가는 가장 일반적인 방법은 특정 커밋 해시, 태그 또는 원격 브랜치를 체크아웃하는 것입니다.

```bash
# 특정 커밋 해시 체크아웃
git checkout a1b2c3d4

# 태그 체크아웃
git checkout v1.2.0

# 원격 브랜치 직접 체크아웃
git checkout origin/feature-branch
```

이러한 명령을 실행하면 Git은 "detached HEAD" 상태에 있으며 어떻게 해야 하는지에 대한 긴 설명 메시지를 표시합니다.

## Detached HEAD 해결 방법

해결 방법은 detached 상태에서 무엇을 했는지에 따라 다릅니다.

### 시나리오 1: 변경 사항이 없는 경우

단순히 코드를 살펴보고 커밋을 하지 않았다면, 원하는 브랜치로 다시 전환하기만 하면 됩니다.

```bash
# main 브랜치로 다시 전환
git checkout main

# 또는 기능 브랜치로 다시 전환
git checkout my-feature-branch
```
이렇게 하면 `HEAD`가 다시 브랜치를 가리키게 되어 detached 상태에서 벗어날 수 있습니다.

### 시나리오 2: 커밋을 했고 이를 유지하고 싶은 경우

이것이 더 중요한 시나리오입니다. detached HEAD 상태에서 커밋을 했다면, 그 커밋들은 어떤 브랜치에도 연결되어 있지 않습니다. 지금 브랜치를 전환하면 해당 커밋들은 "고아(orphaned)"가 되고 결국 Git의 가비지 컬렉션 프로세스에 의해 삭제됩니다.

작업을 저장하려면 커밋을 담을 새 브랜치를 만들어야 합니다.

**1단계: 새 브랜치 생성**

아직 detached HEAD 상태에 있는 동안 새 브랜치를 만듭니다. 이렇게 하면 새 브랜치가 최신 커밋을 가리키게 됩니다.

```bash
# 현재 커밋에서 'new-feature'라는 이름의 새 브랜치 생성
git branch new-feature
```
또는 `git checkout -b`를 사용하여 새 브랜치를 만들고 한 번에 해당 브랜치로 전환할 수 있습니다.

```bash
# 'new-feature'라는 이름의 새 브랜치를 만들고 전환
git checkout -b new-feature
```

이제 새로운 커밋들은 `new-feature` 브랜치에 안전하게 보관됩니다. `HEAD`는 더 이상 detached 상태가 아니며, 새 브랜치를 가리킵니다.

**2단계 (선택 사항): 새 브랜치 병합**

이 변경 사항을 주 개발 라인(예: `main` 브랜치)에 통합하려면 이제 새 브랜치를 병합할 수 있습니다.

```bash
# main 브랜치로 전환
git checkout main

# new-feature 브랜치를 main에 병합
git merge new-feature
```

## 커밋 손실을 피하는 방법

이미 detached HEAD 커밋에서 벗어나 작업을 잃어버렸다고 생각되면 아직 당황하지 마세요. Git은 "고아" 커밋을 삭제하기 전에 한동안 보관합니다. `git reflog` 명령을 사용하여 종종 찾을 수 있습니다.

`git reflog`는 `HEAD`가 가리켰던 기록을 보여줍니다. detached 상태였을 때의 커밋 해시를 찾으세요. 커밋 해시(예: `a1b2c3d4`)를 찾으면 해당 커밋에서 브랜치를 만들어 복구할 수 있습니다.

```bash
git checkout a1b2c3d4
git checkout -b recovered-feature
```

## 결론

"Detached HEAD"는 Git의 정상적인 부분이지만, 조심하지 않으면 위험할 수 있습니다. 핵심은 detached HEAD 상태에서 커밋을 했다면, **다른 곳으로 전환하기 전에 해당 커밋을 위한 새 브랜치를 만드는 것**입니다. 이렇게 하면 작업이 항상 안전하게 브랜치에 연결되도록 할 수 있습니다.
