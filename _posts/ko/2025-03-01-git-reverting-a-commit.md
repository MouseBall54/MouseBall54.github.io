---
typora-root-url: ../
layout: single
title: >
    Git revert와 reset 차이: 안전하게 커밋 되돌리기

date: 2025-03-01T07:19:00+09:00
lang: ko
translation_id: git-revert-vs-reset-safe-undo
permalink: /ko_troubleshooting/git-revert-vs-reset-safe-undo/
header:
   teaser: /images/header_images/overlay_image_git.png
   overlay_image: /images/header_images/overlay_image_git.png
   overlay_filter: 0.5
   image_description: >
     이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Git revert와 reset 차이: 안전하게 커밋 되돌리기
excerpt: >
    공유 브랜치에서 Git 커밋을 되돌릴 때 git revert와 git reset 중 무엇을 써야 하는지, 안전한 선택 기준을 정리합니다.
seo_description: >
    공유 브랜치에서 Git 커밋을 되돌릴 때 git revert와 git reset 중 무엇을 써야 하는지, 안전한 선택 기준을 정리합니다.
categories:
  - ko_Troubleshooting
tags:
  - Git
  - git revert
  - git reset
  - Version Control
---


![이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Git revert와 reset 차이: 안전하게 커밋 되돌리기](/images/header_images/overlay_image_git.png)
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

## 전문 보완 체크

**Git revert와 reset 차이: 안전하게 커밋 되돌리기**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 저장소 루트, 브랜치와 원격 상태, 인덱스와 작업 트리, 인증 또는 네트워크 경계를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

### 신뢰도를 높이는 증거

작업을 바꾸기 전에는 객관적인 증거를 먼저 확인해야 합니다. 쓸 만한 증거에는 `git status`, `git remote -v`, `git branch --show-current`, 실패한 정확한 명령가 포함됩니다. 증거가 서로 맞지 않으면 억지로 하나의 이야기로 합치지 말고 충돌 자체를 남겨야 합니다. 빠른 해결이 한 번 성공했더라도 같은 입력, 계정, 의존성, 기기 상태에서 다시 확인하지 않았다면 아직 확정된 해결책이라고 보기 어렵습니다.

### 검토 표

| 검토 항목 | 확인할 내용 | 중요한 이유 |
| --- | --- | --- |
| 범위 | 이 글이 다루는 정확한 사례 | 조언을 과도하게 적용하지 않게 합니다 |
| 기준 상태 | 변경 전 상태 | 되돌리기와 비교를 가능하게 합니다 |
| 변경 | 실제로 수행한 가장 작은 조치 | 숨은 부작용을 줄입니다 |
| 결과 | 변경 뒤 관찰한 출력 또는 반응 | 기대와 증거를 구분합니다 |
| 재확인 | 결론을 다시 볼 시점 | 글의 정확도를 유지합니다 |

### 예외 상황과 실패 모드

주요 위험은 증상만 고치고 원인을 남기는 상황, 서로 무관한 변경을 같은 테스트에 섞는 상황입니다. 생산 데이터, 개인정보, 돈, 건강, 법적 권리, 보안 복구가 관련되어 있다면 넓은 해결책을 바로 적용하기보다 먼저 증거를 모으는 보수적인 접근이 낫습니다. 같은 제목의 문제라도 환경이 다르면 원인이 달라질 수 있으므로, 독자는 명령이나 결정을 복사하기 전에 자신의 조건이 글의 가정과 맞는지 비교해야 합니다.

### 유지보수 기준

이 안내는 의존성, 운영체제, 빌드 도구가 바뀐 뒤 다시 확인해야 합니다. 좋은 업데이트는 글 전체를 다시 쓰는 것이 아니라 예시, 링크, 명령, 화면, 판단 기준이 현재 동작과 여전히 맞는지 확인하는 일입니다. 기존 결론이 유효하면 확인 날짜를 남기고, 바뀌었다면 무엇이 바뀌었고 왜 이전 조언만으로 부족한지 설명해야 합니다.

### 실행 전 질문

- 문제나 판단이 실제임을 보여 주는 가장 작은 관찰 신호는 무엇인가?
- 공식 출처는 무엇이고, 내부 판단은 어느 부분인가?
- 변경 전에 반드시 캡처해야 할 기록은 무엇인가?
- 어떤 결과가 나오면 이 글의 조언이 맞지 않는다고 볼 것인가?
- 같은 문제가 반복될 때 누가 이 기록을 다시 봐야 하는가?

## 함께 보면 좋은 글

같은 주제 흐름에서 이어서 읽기 좋은 글입니다.

- [SSL: CERTIFICATE_VERIFY_FAILED 오류 해결 방법 (Windows Python)](/ko_troubleshooting/python-certificate-verify-failed/)
- [Permission denied (publickey) 오류 해결 방법 (Windows Git SSH)](/ko_troubleshooting/git-permission-denied-publickey-windows/)
