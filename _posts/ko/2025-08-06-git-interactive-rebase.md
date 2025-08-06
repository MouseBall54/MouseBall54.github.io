---
typora-root-url: ../
layout: single
title: >
   Git Interactive Rebase로 커밋 수정하는 방법

lang: ko
translation_id: git-interactive-rebase
header:
   teaser: /images/header_images/overlay_image_git.png
   overlay_image: /images/header_images/overlay_image_git.png
   overlay_filter: 0.5
excerpt: >
    `git rebase -i`를 사용하여 이전 커밋들을 합치거나, 수정하거나, 삭제하는 방법을 배워보세요. 프로젝트 히스토리를 더 깔끔하고 이해하기 쉽게 만들 수 있습니다.
categories:
  - ko_Troubleshooting
tags:
  - Git
  - Rebase
  - Commit
  - History
  - Interactive
---

## Git Interactive Rebase란?

Git interactive rebase는 강력한 도구입니다. 다양한 방법으로 커밋을 수정할 수 있게 해줍니다. 커밋의 순서를 바꾸거나, 메시지를 변경하거나, 수정하거나, 합치거나(squash), 삭제(drop)할 수 있습니다. 이를 통해 깨끗하고 논리적인 프로젝트 히스토리를 만들 수 있습니다.

특히 기능 브랜치를 메인 브랜치에 병합하기 전에 유용합니다.

## 문제 상황

기능 브랜치에서 여러 개의 작은 커밋을 했다고 상상해 보세요. 일부 커밋은 이전 커밋의 수정 사항이고, 다른 커밋은 사소한 변경 사항입니다. 커밋 히스토리가 지저분해 보일 수 있습니다.

```bash
git log --oneline
f30abf4 (HEAD -> feature) Add feature documentation
a412b9e Fix typo in feature
e85fde9 Implement the main part of the feature
cba1a2d Add initial files for feature
```

이 히스토리는 이상적이지 않습니다. `git rebase -i`를 사용하여 정리할 수 있습니다.

## 해결 방법

### 1. Interactive Rebase 시작하기

얼마나 이전의 커밋까지 수정할지 지정해야 합니다. 마지막 3개의 커밋을 수정하고 싶다고 가정해 보겠습니다. 베이스 커밋은 `cba1a2d`입니다.

다음 명령을 실행합니다.

```bash
git rebase -i HEAD~3
```

또는 수정하려는 첫 번째 커밋의 부모 커밋 해시를 사용할 수 있습니다.

```bash
git rebase -i cba1a2d
```

### 2. 지시 파일 수정하기

이 명령은 선택한 커밋 목록이 포함된 편집기를 엽니다.

```
pick e85fde9 Implement the main part of the feature
pick a412b9e Fix typo in feature
pick f30abf4 Add feature documentation

# Rebase cba1a2d..f30abf4 onto cba1a2d (3 commands)
#
# Commands:
# p, pick <commit> = use commit
# r, reword <commit> = use commit, but edit the commit message
# e, edit <commit> = use commit, but stop for amending
# s, squash <commit> = use commit, but meld into previous commit
# f, fixup <commit> = like "squash", but discard this commit's log message
# x, exec <command> = run command (the rest of the line) using shell
# b, break = stop here (continue rebase later with 'git rebase --continue')
# d, drop <commit> = remove commit
# l, label <label> = label current HEAD with a name
# t, label <label> = reset HEAD to a label
# m, merge [-C <commit> | -c <commit>] <label> [# <oneline>]
# .       create a merge commit using the original merge commit's
# .       message (or the oneline, if no original merge commit was
# .       specified). Use -c <commit> to re-create the merge commit
# .       from the original commit.
#
# These lines can be re-ordered; they are executed from top to bottom.
#
# If you remove a line here THAT COMMIT WILL BE LOST.
#
# However, if you remove everything, the rebase will be aborted.
#
```

### 3. 커밋 수정하기

"Fix typo" 커밋을 구현 커밋과 합쳐 보겠습니다. `squash` (또는 `s`)를 사용합니다. 또한 마지막 커밋 메시지를 변경하고 싶습니다.

오타 수정 커밋의 `pick`을 `squash`로 변경합니다. 마지막 커밋은 `reword`로 변경해 보겠습니다.

```
pick e85fde9 Implement the main part of the feature
s a412b9e Fix typo in feature
r f30abf4 Add feature documentation
```

파일을 저장하고 닫습니다.

### 4. 변경 사항 완료하기

Git은 먼저 두 커밋을 합칩니다. 그런 다음 합쳐진 커밋에 대한 새 커밋 메시지를 작성하도록 다른 편집기를 엽니다.

```
# This is a combination of 2 commits.
# The first commit's message is:
Implement the main part of the feature

# This is the 2nd commit's message:
Fix typo in feature
```

`Implement the main part of the feature`라는 깔끔한 메시지를 만듭니다.

해당 메시지를 저장하면 rebase가 계속됩니다. 그런 다음 마지막 커밋의 메시지를 변경하기 위해 멈춥니다. `f30abf4`에 대한 다른 편집기가 열립니다. `Add documentation for the new feature`로 변경해 보겠습니다.

### 5. 히스토리 확인하기

이제 로그를 다시 확인합니다.

```bash
git log --oneline
a1b2c3d (HEAD -> feature) Add documentation for the new feature
d4e5f6g Implement the main part of the feature
cba1a2d Add initial files for feature
```

이제 히스토리가 훨씬 깨끗하고 이해하기 쉬워졌습니다.

## 결론

Interactive rebase는 커밋 히스토리를 관리하는 강력한 기능입니다. 변경 사항을 다른 사람과 공유하기 전에 히스토리를 깔끔하게 만드는 데 사용하세요. 그러나 이미 공유 저장소에 푸시된 커밋은 rebase하지 않도록 주의해야 합니다. 히스토리를 다시 작성하여 협업자에게 문제를 일으킬 수 있기 때문입니다.
