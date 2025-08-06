---
typora-root-url: ../
layout: single
title: >
   Git에서 다른 브랜치의 특정 커밋 가져오기 (Cherry-Pick)

lang: ko
translation_id: git-cherry-pick
header:
   teaser: /images/header_images/overlay_image_git.png
   overlay_image: /images/header_images/overlay_image_git.png
   overlay_filter: 0.5
excerpt: >
    `git cherry-pick`을 사용하여 브랜치 전체를 병합하지 않고 다른 브랜치에 있는 특정 커밋만 현재 브랜치에 적용하는 방법을 알아보세요.
categories:
  - ko_Troubleshooting
tags:
  - Git
  - Cherry-pick
  - Commit
  - Branch
---

## Git Cherry-Pick이란?

`git cherry-pick`은 한 브랜치에서 커밋을 선택하여 다른 브랜치에 적용하는 명령어입니다. 다른 브랜치의 특정 변경 사항이 필요하지만 전체 브랜치를 병합하고 싶지 않을 때 유용합니다. 관련 없는 변경 사항이 도입되는 것을 방지합니다.

## 문제 상황

`main`과 `feature`라는 두 개의 브랜치가 있다고 가정해 보겠습니다. `feature` 브랜치에서 중요한 버그가 수정되었습니다. 아직 개발 중인 `feature` 브랜치 전체를 병합하지 않고 이 수정 사항을 즉시 `main` 브랜치에 적용해야 합니다.

**`feature` 브랜치 로그:**
```bash
git log --oneline feature
a1b2c3d (feature) Add new experimental feature
d4e5f6g Fix critical bug #123
cba1a2d Start developing feature
```

**`main` 브랜치 로그:**
```bash
git log --oneline main
f30abf4 (HEAD -> main) Release version 1.0
```

`d4e5f6g` 커밋을 `main` 브랜치로 가져와야 합니다.

## 해결 방법

### 1. 대상 브랜치로 전환하기

먼저, 커밋을 적용하려는 브랜치에 있는지 확인합니다. 이 경우 `main` 브랜치입니다.

```bash
git switch main
```

### 2. 커밋 해시 찾기

체리-픽하려는 커밋의 해시가 필요합니다. 다른 브랜치의 로그에서 이를 얻을 수 있습니다.

```bash
git log --oneline feature
```

출력에서 버그 수정에 대한 커밋 해시는 `d4e5f6g`입니다.

### 3. `git cherry-pick` 실행하기

이제 커밋 해시와 함께 `cherry-pick` 명령을 사용합니다.

```bash
git cherry-pick d4e5f6g
```

Git은 해당 커밋의 변경 사항을 가져와 현재 브랜치(`main`)에 새 커밋으로 적용합니다. 새 커밋은 다른 해시를 갖지만 동일한 변경 사항과 유사한 커밋 메시지를 포함합니다.

### 4. 결과 확인하기

`main` 브랜치의 로그를 확인하여 새 커밋을 확인합니다.

```bash
git log --oneline main
e9f8d7c (HEAD -> main) Fix critical bug #123
f30abf4 Release version 1.0
```

이제 수정 사항이 `main` 브랜치에 적용되었습니다.

## 충돌 해결하기

때때로 체리-픽은 병합 충돌을 일으킬 수 있습니다. 이는 선택한 커밋의 변경 사항이 현재 브랜치의 상태와 충돌할 때 발생합니다.

충돌이 발생하면 Git은 중지하고 해결하도록 합니다.
1.  충돌하는 파일을 엽니다.
2.  `<<<<<<<`, `=======`, `>>>>>>>` 마커를 찾아 파일을 수동으로 편집하여 충돌을 해결합니다.
3.  해결 후 `git add <file_name>`을 사용하여 변경 사항을 스테이징합니다.
4.  다음을 실행하여 체리-픽 프로세스를 계속합니다.
    ```bash
    git cherry-pick --continue
    ```

체리-픽을 중단하려면 다음을 사용할 수 있습니다.
```bash
git cherry-pick --abort
```

## 결론

`git cherry-pick`은 한 브랜치에서 다른 브랜치로 특정 커밋을 적용하는 정밀한 도구입니다. 핫픽스나 브랜치 간에 기능을 선택적으로 공유하는 것과 같은 상황에 적합합니다. 병합이 더 적절한 경우 중복 변경을 만들지 않도록 신중하게 사용하세요.
