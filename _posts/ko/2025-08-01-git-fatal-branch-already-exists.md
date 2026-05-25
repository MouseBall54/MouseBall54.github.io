---
typora-root-url: ../
layout: single
title: "Git 'fatal: A branch named '...' already exists' 오류 해결 방법"

date: 2025-08-01T00:00:00+09:00
lang: ko
translation_id: git-fatal-branch-already-exists
header:
   teaser: /images/header_images/overlay_image_git.png
   overlay_image: /images/header_images/overlay_image_git.png
   overlay_filter: 0.5
   image_description: >
     이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Git 'fatal: A branch named '...' already exists' 오류 해결 방법
excerpt: >
  다른 이름을 선택하거나, 이전 브랜치를 삭제하거나, 기존 브랜치로 체크아웃하여 Git의 "fatal: A branch named '...' already exists" 오류를 해결하는 방법을 알아봅니다.
seo_description: >
  다른 이름을 선택하거나, 이전 브랜치를 삭제하거나, 기존 브랜치로 체크아웃하여 Git의 "fatal: A branch named '...' already exists" 오류를 해결하는 방법을 알아봅니다.
categories:
  - ko_Troubleshooting
tags:
  - Git
  - Branch
  - Version Control
  - fatal error
---


![이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Git 'fatal: A branch named '...' already exists' 오류 해결 방법](/images/header_images/overlay_image_git.png)
`git branch <브랜치-이름>` 또는 `git checkout -b <브랜치-이름>`을 사용하여 Git에서 새 브랜치를 생성할 때 `fatal: A branch named '<브랜치-이름>' already exists.` 오류를 만날 수 있습니다.

이는 사용하려는 이름이 로컬 저장소에서 이미 사용 중임을 나타내는 Git의 간단한 메시지입니다. 이 가이드에서는 이 상황을 처리하는 방법을 보여줍니다.

### 이 오류는 왜 발생하나요?

Git은 저장소의 모든 브랜치가 고유한 이름을 갖도록 요구합니다. 동일한 이름을 가진 두 개의 로컬 브랜치를 가질 수 없습니다. 이 오류는 단순히 그 규칙을 강제하는 것입니다.

이 오류가 발생하는 가장 일반적인 이유는 다음과 같습니다.
1.  해당 이름으로 브랜치를 이미 만들었다는 사실을 잊어버렸습니다.
2.  다른 사람들과 협업 중이며, 지금 사용하려는 이름과 동일한 이름의 브랜치를 원격 저장소에서 가져왔습니다.
3.  다른 이름을 입력하려다 간단한 오타가 발생했습니다.

### "Branch Already Exists" 오류 해결 방법

원하는 목표에 따라 몇 가지 옵션이 있습니다.

#### 옵션 1: 다른 브랜치 이름 선택하기

가장 간단한 해결책은 아직 사용되지 않은 이름을 선택하는 것입니다. 이름 자체가 중요하지 않다면, 그냥 새 이름으로 다시 시도하세요.

```bash
# 실패한 명령어
git checkout -b feature/login

# 더 구체적인 이름으로 시도
git checkout -b feature/login-v2
```

#### 옵션 2: 기존 브랜치로 체크아웃하기

이 오류가 표시되면 새 브랜치가 필요 없다는 것을 깨달을 수 있습니다. 단지 기존 브랜치로 전환하고 싶을 뿐입니다. 이 경우 `-b` 플래그 없이 `git checkout`을 사용하세요.

```bash
# 새 브랜치를 만드는 대신...
git checkout -b my-feature

# ...기존 브랜치로 전환하기
git checkout my-feature
```

모든 로컬 브랜치 목록을 보고 이름을 확인하려면 언제든지 다음을 사용할 수 있습니다.
```bash
git branch
```

#### 옵션 3: 이전 브랜치 삭제하기

기존 브랜치가 오래되었거나, 구식이거나, 더 이상 필요하지 않은 경우, 해당 브랜치를 삭제한 다음 같은 이름으로 새 브랜치를 만들 수 있습니다.

**경고**: 브랜치를 삭제하면 해당 브랜치의 커밋이 다른 곳에 병합되지 않은 경우 데이터가 손실될 수 있습니다. 이전 브랜치의 변경 사항이 더 이상 필요 없는지 확인하세요.

1.  **로컬 브랜치 삭제:**
    `-d` 플래그는 완전히 병합된 브랜치만 삭제합니다. 더 안전한 옵션을 위해 먼저 이것을 사용하세요.
    ```bash
    git branch -d old-feature
    ```
    병합되지 않았더라도 브랜치를 삭제하고 싶다면 `-D` 플래그(강제 삭제)를 사용하세요.
    ```bash
    git branch -D old-feature
    ```

2.  **새 브랜치 생성:**
    이제 이전 이름이 비었으므로 새 브랜치를 만들 수 있습니다.
    ```bash
    git checkout -b old-feature
    ```

#### 옵션 4: 기존 브랜치를 새 시작 지점으로 재설정하기

때로는 브랜치를 삭제하는 대신 다른 커밋에서 "다시 시작"하고 싶을 때가 있습니다. 예를 들어, `feature/login`을 최신 `main` 브랜치에서 시작하고 싶을 수 있습니다. `git checkout`의 `--force` 옵션을 사용하거나 재설정하여 이 작업을 수행할 수 있습니다.

**`checkout` 사용 (더 간단함):**
현재 `HEAD`에서 새 `feature/login`을 시작하고 이전 것은 버리려면:
```bash
git checkout -B feature/login
```
`-B` 플래그는 브랜치가 없으면 생성하고, 있으면 현재 커밋으로 재설정하라는 편리한 단축키입니다.

**`reset` 사용 (더 명시적임):**
```bash
# 재설정하려는 브랜치로 전환
git checkout feature/login

# 'main'의 최신 커밋으로 재설정
git reset --hard main

# 이제 'feature/login' 브랜치는 'main'과 동일합니다
```

### 결론

"fatal: A branch named '...' already exists" 오류는 Git의 간단한 안전장치입니다. 이 오류가 표시되면 잠시 시간을 내어 `git branch`로 로컬 브랜치를 확인하세요. 거기서부터 다른 이름을 사용할지, 기존 브랜치로 전환할지, 또는 새 브랜치를 위해 이전 브랜치를 삭제/재설정할지 결정할 수 있습니다.

## 전문 보완 체크

**Git 'fatal: A branch named '...' already exists' 오류 해결 방법**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 저장소 루트, 브랜치와 원격 상태, 인덱스와 작업 트리, 인증 또는 네트워크 경계를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

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
