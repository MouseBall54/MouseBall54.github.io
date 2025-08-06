---
typora-root-url: ../
layout: single
title: >
    Git 커밋 되돌리기: git revert 사용법

lang: ko
translation_id: git-reverting-a-commit
header:
   teaser: /images/header_images/overlay_image_git.png
   overlay_image: /images/header_images/overlay_image_git.png
   overlay_filter: 0.5
excerpt: >
    Git에서 특정 커밋의 변경 사항을 안전하게 취소하는 `git revert` 명령어의 사용법과 `git reset`과의 차이점을 알아봅니다.
categories:
  - ko_Troubleshooting
tags:
  - Git
  - git revert
  - git reset
  - Version Control
---

## 문제 상황

Git으로 프로젝트를 관리하다 보면, 특정 커밋에 문제가 있다는 것을 뒤늦게 발견하는 경우가 많습니다. 예를 들어, 버그를 유발하는 코드를 커밋했거나, 잘못된 파일을 포함하여 이미 원격 저장소(remote repository)에 `push`까지 완료했을 수 있습니다.

이럴 때 해당 커밋의 변경 사항만 안전하게 제거하고 싶지만, 프로젝트 히스토리를 강제로 수정하는 것은 위험할 수 있습니다. 특히 여러 명의 팀원과 함께 작업하는 공유 브랜치에서는 `git reset`과 같은 히스토리 변경 명령어를 사용하기 어렵습니다.

## 해결 방법: `git revert` 사용하기

`git revert`는 특정 커밋의 변경 내용을 **반대(opposite)로 적용하는 새로운 커밋**을 생성하는 명령어입니다. 즉, 기존의 커밋 히스토리를 삭제하거나 수정하는 대신, 문제가 된 커밋을 되돌리는 새로운 기록을 추가합니다.

이 방식은 다음과 같은 장점이 있습니다.
- **안전함**: 기존 커밋 히스토리를 보존하므로, 팀원들과의 충돌을 피할 수 있습니다.
- **명확함**: 어떤 커밋이 되돌려졌는지 명확한 기록이 남습니다.

### `git revert` 사용법

1.  **되돌릴 커밋 확인하기**

    먼저 `git log` 명령어로 커밋 히스토리를 확인하고, 되돌리고 싶은 커밋의 해시(hash) 값을 찾습니다.

    ```bash
    git log --oneline
    # c4a2f85 (HEAD -> main) feat: Add user profile feature
    # a1b3c4d fix: Correct login validation
    # f9e8d7c chore: Update documentation
    ```
    여기서 `a1b3c4d` 커밋에 문제가 있다고 가정해 보겠습니다.

2.  **`git revert` 실행하기**

    다음 명령어를 사용하여 해당 커밋을 되돌립니다.

    ```bash
    git revert a1b3c4d
    ```

3.  **커밋 메시지 작성하기**

    명령을 실행하면, Git은 새로운 "Revert" 커밋을 위한 메시지를 작성하도록 텍스트 편집기를 엽니다. 기본적으로 "Revert "fix: Correct login validation""과 같은 메시지가 자동으로 생성됩니다.
    
    필요하다면 왜 이 커밋을 되돌리는지에 대한 설명을 추가할 수 있습니다. 메시지를 저장하고 편집기를 닫으면 새로운 커밋이 생성됩니다.

    만약 커밋 메시지 수정을 건너뛰고 싶다면 `--no-edit` 옵션을 사용할 수 있습니다.
    ```bash
    git revert --no-edit a1b3c4d
    ```

4.  **원격 저장소에 푸시하기**

    로컬에서 되돌리기 커밋이 완료되었다면, 이 변경 사항을 원격 저장소에 `push`하여 팀원들과 공유합니다.

    ```bash
    git push origin main
    ```

이제 `git log`를 다시 확인해보면, 기존 커밋들은 그대로 있고 "Revert" 커밋이 그 위에 새로 추가된 것을 볼 수 있습니다.

```bash
git log --oneline
# 3d5e6f7 (HEAD -> main) Revert "fix: Correct login validation"
# c4a2f85 feat: Add user profile feature
# a1b3c4d fix: Correct login validation
# f9e8d7c chore: Update documentation
```

## `git revert` vs `git reset`

| 특징 | `git revert` | `git reset` |
| --- | --- | --- |
| **동작 방식** | 변경 사항을 되돌리는 **새로운 커밋**을 생성 | HEAD 포인터를 과거의 특정 커밋으로 **이동** |
| **히스토리** | 기존 히스토리를 **보존** (안전) | 기존 히스토리를 **변경/삭제** (위험) |
| **주 사용처** | **공유된 브랜치** (예: `main`, `develop`)의 커밋을 되돌릴 때 | **개인 로컬 브랜치**에서 아직 공유되지 않은 커밋을 정리할 때 |

`git reset`은 커밋 히스토리 자체를 지우기 때문에, 이미 팀원들과 공유된 커밋에 사용하면 다른 사람들의 작업과 심각한 충돌을 일으킬 수 있습니다. 따라서 **공유된 브랜치에서는 항상 `git revert`를 사용하는 것이 안전합니다.**

## 결론

`git revert`는 이미 커밋된, 특히 원격 저장소에 공유된 변경 사항을 안전하게 되돌릴 수 있는 강력하고 필수적인 도구입니다.

-   문제가 되는 커밋을 되돌려야 할 때는 `git revert <commit-hash>`를 사용하세요.
-   이 명령은 히스토리를 덮어쓰는 대신, 되돌리는 내용의 **새로운 커밋**을 만듭니다.
-   팀원과 함께 작업하는 **공유 브랜치에서는 `git reset` 대신 `git revert`를 사용**하는 것이 원칙입니다.

실수를 바로잡는 것은 개발 과정의 일부입니다. `git revert`를 올바르게 사용하여 프로젝트 히스토리를 깨끗하고 안전하게 관리하세요.
