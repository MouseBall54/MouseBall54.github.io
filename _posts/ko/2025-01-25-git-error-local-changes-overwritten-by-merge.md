---
typora-root-url: ../
layout: single
title: >
    "Git "error: Your local changes... would be overwritten by merge" 오류 해결 방법"

date: 2025-01-25T07:29:00+09:00
lang: ko
translation_id: git-error-local-changes-overwritten-by-merge
excerpt: "pull 또는 merge 전에 로컬 변경 사항을 스태시, 커밋 또는 폐기하여 Git 병합 오류를 해결하세요."
seo_description: "pull 또는 merge 전에 로컬 변경 사항을 스태시, 커밋 또는 폐기하여 Git 병합 오류를 해결하세요."
header:
   teaser: /images/header_images/overlay_image_git.png
   overlay_image: /images/header_images/overlay_image_git.png
   overlay_filter: 0.5
   image_description: >
     이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Git "error: Your local changes... would be overwritten by merge" 오류 해결 방법
categories:
  - ko_Troubleshooting
tags:
  - Git
  - Merge
  - Stash
  - Commit
  - Version Control
---


![이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Git "error: Your local changes... would be overwritten by merge" 오류 해결 방법](/images/header_images/overlay_image_git.png)
## 서론

Git 오류 메시지 `error: Your local changes to the following files would be overwritten by merge`는 사용자의 커밋되지 않은 작업을 보호하기 위한 조치다. 이 오류는 로컬 작업 디렉터리에 수정한 내용이 `git pull` 또는 `git merge` 작업으로 업데이트될 파일과 충돌할 때 발생한다. 이 가이드에서는 이 오류가 발생하는 이유를 설명하고 이를 해결하기 위한 세 가지 일반적인 방법을 제공한다.

## 이 오류는 왜 발생할까?

Git의 주요 임무는 코드 버전을 관리하는 것이다. 원격 저장소에서 `pull`하거나 브랜치를 `merge`할 때, Git은 로컬 작업 디렉터리의 파일을 업데이트해야 한다. 만약 Git이 업데이트해야 하는 파일을 사용자가 이미 변경한 경우, Git은 작업 내용을 덮어쓰는 것을 방지하기 위해 프로세스를 중단한다.

예를 들어:
1. 사용자가 `style.css` 파일을 수정했다.
2. 이 변경 사항을 커밋하지 **않았다**.
3. 그 사이 동료가 원격 저장소에 `style.css`의 새 버전을 푸시했다.
4. 사용자가 `git pull`을 실행하면, Git은 새 `style.css`를 가져와 로컬 파일을 업데이트하려고 시도한다.
5. Git은 커밋되지 않은 변경 사항을 발견하고 작업을 보호하기 위해 "overwritten by merge" 오류와 함께 작업을 중단한다.

## 해결 방법

이 문제를 해결하는 세 가지 주요 방법이 있다. 상황에 가장 적합한 방법을 선택하면 된다.

### 방법 1: 변경 사항 커밋하기

만든 변경 사항이 완료되었고 유지하고 싶다면, 가장 간단한 해결책은 pull 또는 merge 전에 변경 사항을 커밋하는 것이다.

**단계:**
1.  **변경 사항 스테이징하기**: 수정된 파일을 스테이징 영역에 추가한다.
    ```bash
    git add . 
    # 또는 더 구체적으로: git add <file1> <file2>
    ```
2.  **변경 사항 커밋하기**: 설명이 포함된 메시지와 함께 로컬 저장소에 변경 사항을 저장한다.
    ```bash
    git commit -m "나의 설명적인 커밋 메시지"
    ```
3.  **다시 Pull 또는 Merge하기**: 이제 로컬 변경 사항이 안전하게 커밋되었으므로 원래 작업을 계속할 수 있다.
    ```bash
    git pull
    # 또는 git merge <branch-name>
    ```
    만약 당신의 커밋과 들어오는 변경 사항 간에 충돌이 발생하면, Git은 이제 병합 충돌을 해결하라고 안내하지만, 당신의 작업을 덮어쓰지는 않는다.

### 방법 2: 변경 사항 스태시하기

변경 사항이 아직 커밋할 준비가 되지 않았지만 최신 업데이트를 가져오고 싶다면, `git stash`가 완벽한 도구다. 이 명령은 커밋되지 않은 변경 사항을 일시적으로 보관하여 작업 디렉터리를 깨끗하게 만들어준다.

**단계:**
1.  **로컬 변경 사항 스태시하기**: 이렇게 하면 수정 사항이 저장되고 파일이 마지막 커밋(`HEAD`) 상태로 되돌아간다.
    ```bash
    git stash
    ```
2.  **Pull 또는 Merge하기**: 이제 작업 디렉터리가 깨끗해졌으므로 안전하게 pull 또는 merge를 할 수 있다.
    ```bash
    git pull
    ```
3.  **스태시한 변경 사항 적용하기**: pull이 완료된 후, 새로 업데이트된 코드 위에 변경 사항을 다시 적용할 수 있다.
    ```bash
    git stash pop
    # 또는 git stash apply
    ```
    `git stash pop`은 변경 사항을 적용하고 스태시 목록에서 해당 스태시를 제거한다. `git stash apply`는 변경 사항을 적용하지만 스태시를 유지하여 여러 브랜치에 적용하고 싶을 때 유용하다.

### 방법 3: 변경 사항 폐기하기

로컬 변경 사항이 더 이상 필요 없고 원격 저장소의 최신 버전을 가져오고 싶다면, 변경 사항을 폐기할 수 있다.

**경고**: 이 작업은 되돌릴 수 없다. 로컬 수정 사항이 영구적으로 손실된다.

**단계:**
1.  **모든 로컬 변경 사항 폐기하기**: 이 명령은 작업 디렉터리를 정리하고 커밋되지 않은 모든 변경 사항을 제거한다.
    ```bash
    git reset --hard HEAD
    ```
    또는 특정 파일의 변경 사항만 폐기하려면:
    ```bash
    git checkout -- <file-name>
    ```
2.  **Pull 또는 Merge하기**: 깨끗한 작업 디렉터리에서 이제 문제없이 pull을 할 수 있다.
    ```bash
    git pull
    ```

이 세 가지 방법(커밋, 스태시, 폐기) 중 하나를 선택하여 로컬 작업을 안전하게 관리하고 "overwritten by merge" 오류를 해결할 수 있다.

## 전문 보완 체크

**"Git "error: Your local changes... would be overwritten by merge" 오류 해결 방법"**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 저장소 루트, 브랜치와 원격 상태, 인덱스와 작업 트리, 인증 또는 네트워크 경계를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

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
