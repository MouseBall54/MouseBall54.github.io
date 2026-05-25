---
typora-root-url: ../
layout: single
title: "Git 오류 'fatal: remote origin already exists' 해결 방법"

date: 2025-01-07T07:11:00+09:00
lang: ko
translation_id: git-fatal-remote-origin-already-exists
excerpt: "'fatal: remote origin already exists'는 원격 저장소를 추가하려 할 때 'origin'이라는 이름이 이미 사용 중일 때 발생하는 오류입니다. 이 글에서는 원인과 해결 방법을 알아봅니다."
seo_description: "'fatal: remote origin already exists'는 원격 저장소를 추가하려 할 때 'origin'이라는 이름이 이미 사용 중일 때 발생하는 오류입니다. 이 글에서는 원인과 해결 방법을 알아봅니다."
header:
   teaser: /images/header_images/overlay_image_git.png
   overlay_image: /images/header_images/overlay_image_git.png
   overlay_filter: 0.5
   image_description: >
     이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Git 오류 'fatal: remote origin already exists' 해결 방법
categories:
  - ko_Troubleshooting
tags:
  - Git
  - Troubleshooting
  - Version Control
  - Remote
---


![이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Git 오류 'fatal: remote origin already exists' 해결 방법](/images/header_images/overlay_image_git.png)
## 'fatal: remote origin already exists' 오류란?

`fatal: remote origin already exists` 오류는 `git remote add origin <저장소_URL>` 명령을 실행했을 때, 이미 `origin`이라는 이름의 원격 저장소가 설정되어 있는 경우에 발생한다.
Git에서 원격 저장소의 별칭(이름)은 고유해야 하므로, 중복된 이름을 사용하려고 하면 이 오류 메시지가 나타난다.
`origin`은 `git clone` 명령을 사용할 때 기본적으로 생성되는 원격 저장소의 기본 이름이다.

## 주요 원인

### 1. `git clone` 이후 `git remote add` 실행
`git clone`으로 원격 저장소를 복제하면, Git은 자동으로 해당 원격 저장소를 `origin`이라는 이름으로 등록한다.
이후 사용자가 같은 저장소나 다른 저장소를 `origin`이라는 이름으로 또 추가하려고 시도하면 오류가 발생한다.

```bash
# 저장소를 클론하면 'origin'이 자동으로 설정됨
git clone https://github.com/user/repo.git
cd repo

# 이미 'origin'이 존재하므로 오류 발생
git remote add origin https://github.com/user/repo.git
# fatal: remote origin already exists.
```

### 2. 수동으로 원격 저장소를 추가한 후 다시 추가
`git init`으로 로컬 저장소를 만든 후, `git remote add origin` 명령으로 원격 저장소를 연결했다.
이후 같은 명령을 다시 실행하면 당연히 이름이 중복되어 오류가 발생한다.

## 해결 방법

해결 방법은 현재 설정된 `origin`을 어떻게 처리할지에 따라 달라진다.

### 1. 기존 원격 저장소의 URL 변경
만약 기존에 설정된 `origin`의 URL을 단순히 다른 URL로 변경하고 싶다면, `set-url` 명령을 사용하면 된다.

```bash
# 현재 설정된 원격 저장소 확인
git remote -v
# origin  https://github.com/old/repo.git (fetch)
# origin  https://github.com/old/repo.git (push)

# 'origin'의 URL을 새로운 URL로 변경
git remote set-url origin https://github.com/new/repo.git

# 변경된 내용 확인
git remote -v
# origin  https://github.com/new/repo.git (fetch)
# origin  https://github.com/new/repo.git (push)
```
이 방법은 기존의 `origin` 이름을 유지하면서 주소만 바꾸고 싶을 때 가장 적합하다.

### 2. 기존 원격 저장소 삭제 후 새로 추가
기존 `origin` 설정이 완전히 잘못되었거나 더 이상 필요 없다면, 삭제하고 새로 추가할 수 있다.

```bash
# 기존 'origin' 원격 저장소 삭제
git remote remove origin

# 새로운 원격 저장소를 'origin'으로 추가
git remote add origin https://github.com/another/repo.git

# 설정된 내용 확인
git remote -v
# origin  https://github.com/another/repo.git (fetch)
# origin  https://github.com/another/repo.git (push)
```

### 3. 다른 이름으로 원격 저장소 추가
`origin`이라는 이름은 유지하면서, 또 다른 원격 저장소를 추가하고 싶다면 다른 이름을 사용하면 된다.
예를 들어, `upstream`이나 `backup` 같은 이름을 사용할 수 있다.

```bash
# 'origin'은 그대로 두고, 'upstream'이라는 이름으로 새 원격 저장소 추가
git remote add upstream https://github.com/different/repo.git

# 설정된 원격 저장소 목록 확인
git remote -v
# origin    https://github.com/original/repo.git (fetch)
# origin    https://github.com/original/repo.git (push)
# upstream  https://github.com/different/repo.git (fetch)
# upstream  https://github.com/different/repo.git (push)
```
이 방법은 여러 원격 저장소를 동시에 관리해야 할 때 유용하다.

## 결론

`fatal: remote origin already exists` 오류는 Git의 원격 저장소 이름이 중복될 때 발생하는 자연스러운 현상이다.
`git remote -v` 명령으로 현재 설정된 원격 저장소 목록을 먼저 확인하는 습관을 들이는 것이 중요하다.
상황에 맞게 `set-url`로 URL을 변경하거나, `remove`로 삭제 후 다시 추가하거나, 혹은 새로운 이름으로 다른 원격 저장소를 추가하는 방법을 사용하면 쉽게 문제를 해결할 수 있다.

## 전문 보완 체크

**Git 오류 'fatal: remote origin already exists' 해결 방법**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 저장소 루트, 브랜치와 원격 상태, 인덱스와 작업 트리, 인증 또는 네트워크 경계를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

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

독자가 **Git 오류 'fatal: remote origin already exists' 해결 방법**의 첫 번째 권장 조치를 이미 시도했지만 결과가 여전히 불확실하다고 가정해 봅니다. 다음 단계는 여러 해결책을 한꺼번에 시험하는 것이 아니라 짧은 감사 기록을 만드는 것입니다. 먼저 어떤 판단을 하려는지 한 문장으로 쓰고, 환경을 한 문장으로 적고, 관찰된 결과를 한 문장으로 남깁니다. 그다음 저장소 루트, 브랜치와 원격 상태, 인덱스와 작업 트리, 인증 또는 네트워크 경계를 이미 확보한 사실과 대조합니다. 이렇게 해야 글이 서로 끊어진 팁 목록이 아니라 검증 가능한 절차가 됩니다.

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
