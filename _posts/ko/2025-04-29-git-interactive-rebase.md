---
typora-root-url: ../
layout: single
title: >
   Git Interactive Rebase로 커밋 수정하는 방법

date: 2025-04-29T07:33:00+09:00
lang: ko
translation_id: git-interactive-rebase
header:
   teaser: /images/header_images/overlay_image_git.png
   overlay_image: /images/header_images/overlay_image_git.png
   overlay_filter: 0.5
   image_description: >
     이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Git Interactive Rebase로 커밋 수정하는 방법
excerpt: >
    `git rebase -i`를 사용하여 이전 커밋들을 합치거나, 수정하거나, 삭제하는 방법을 배워보세요. 프로젝트 히스토리를 더 깔끔하고 이해하기 쉽게 만들 수 있습니다.
seo_description: >
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


![이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Git Interactive Rebase로 커밋 수정하는 방법](/images/header_images/overlay_image_git.png)
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

## 전문 보완 체크

**Git Interactive Rebase로 커밋 수정하는 방법**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 저장소 루트, 브랜치와 원격 상태, 인덱스와 작업 트리, 인증 또는 네트워크 경계를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

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

## 적용 검토 시나리오

독자가 **Git Interactive Rebase로 커밋 수정하는 방법**의 첫 번째 권장 조치를 이미 시도했지만 결과가 여전히 불확실하다고 가정해 봅니다. 다음 단계는 여러 해결책을 한꺼번에 시험하는 것이 아니라 짧은 감사 기록을 만드는 것입니다. 먼저 어떤 판단을 하려는지 한 문장으로 쓰고, 환경을 한 문장으로 적고, 관찰된 결과를 한 문장으로 남깁니다. 그다음 저장소 루트, 브랜치와 원격 상태, 인덱스와 작업 트리, 인증 또는 네트워크 경계를 이미 확보한 사실과 대조합니다. 이렇게 해야 글이 서로 끊어진 팁 목록이 아니라 검증 가능한 절차가 됩니다.

### 감사 기록 양식

| 항목 | 예시 기준 | 이유 |
| --- | --- | --- |
| 관찰 | 조치 전 실제로 본 내용 | 기준 상태를 객관화합니다 |
| 증거 | `git status`, `git remote -v` | 판단을 기록에 연결합니다 |
| 가정 | 믿고 있지만 아직 증명하지 못한 내용 | 숨은 추정을 드러냅니다 |
| 조치 | 한 번에 하나의 변경 | 결과의 원인을 추적하게 합니다 |
| 중단 기준 | 멈추고 도움을 요청할 조건 | 반복적인 시행착오를 줄입니다 |

### 품질 경계

같은 결과가 통제된 재확인 뒤에도 반복될 때만 이 안내를 강한 결론으로 보아야 합니다. 계정, 기기, 데이터 샘플, 의존성 버전, 계약 조건, 공식 규칙이 달라졌다면 결론의 강도를 낮추고 가설로 다루는 편이 안전합니다. 검색 독자는 급한 문제를 안고 들어오는 경우가 많아 맥락을 건너뛰기 쉽습니다. 전문적인 글은 위험한 판단을 천천히 하게 만들면서도 다음 행동은 분명하게 제시해야 합니다.

## 함께 보면 좋은 글

같은 주제 흐름에서 이어서 읽기 좋은 글입니다.

- [SSL: CERTIFICATE_VERIFY_FAILED 오류 해결 방법 (Windows Python)](/ko_troubleshooting/python-certificate-verify-failed/)
- [Permission denied (publickey) 오류 해결 방법 (Windows Git SSH)](/ko_troubleshooting/git-permission-denied-publickey-windows/)
