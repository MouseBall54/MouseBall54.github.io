---
typora-root-url: ../
layout: single
title: >
  "Git "fatal: pathspec '...' did not match any files" 오류 해결 방법"

date: 2025-01-28T07:32:00+09:00
lang: ko
translation_id: git-fatal-pathspec-did-not-match
excerpt: >
  "오타, 올바른 파일 경로를 확인하고, 필요 시 파일이 Git에 의해 추적되고 있는지 확인하여 "fatal: pathspec '...' did not match any files" Git 오류를 해결하세요."
seo_description: >
  "오타, 올바른 파일 경로를 확인하고, 필요 시 파일이 Git에 의해 추적되고 있는지 확인하여 "fatal: pathspec '...' did not match any files" Git 오류를 해결하세요."
header:
   teaser: /images/header_images/overlay_image_git.png
   overlay_image: /images/header_images/overlay_image_git.png
   overlay_filter: 0.5
   image_description: >
     이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Git "fatal: pathspec '...' did not match any files" 오류 해결 방법
categories:
  - ko_Troubleshooting
tags:
  - Git
  - Pathspec
  - Version Control
  - Debugging
---


![이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Git "fatal: pathspec '...' did not match any files" 오류 해결 방법](/images/header_images/overlay_image_git.png)
## 서론

Git에서 `fatal: pathspec '...' did not match any files` 오류는 `git add`, `git rm`, 또는 `git checkout`과 같은 명령을 Git이 찾을 수 없는 파일에 대해 실행하려고 할 때 나타나는 일반적인 메시지다. 이 가이드에서는 이 오류가 발생하는 간단한 이유와 신속하게 해결하는 방법을 안내한다.

## "Pathspec"이란 무엇인가?

Git에서 "pathspec"은 단순히 파일이나 디렉터리 경로를 참조하는 방식을 의미한다. 예를 들어, `git add index.html` 명령에서 pathspec은 `index.html`이다. 오류 메시지는 사용자가 제공한 경로가 해당 명령의 컨텍스트에서 Git이 알고 있는 어떤 파일과도 일치하지 않았음을 알려주는 것이다.

## 일반적인 원인과 해결책

이 오류의 가장 빈번한 원인과 해결 방법을 살펴보자.

### 1. 원인: 파일명 또는 경로의 오타

이것이 가장 흔한 원인이다. 파일이나 해당 파일이 있는 디렉터리의 이름을 단순히 잘못 입력했을 수 있다.

**예시:**
`styles.css`를 추가하고 싶지만 다음과 같이 입력한 경우:
```bash
git add style.css 
# fatal: pathspec 'style.css' did not match any files
```

**해결책:**
- **철자 확인**: 파일명과 경로에 오타가 없는지 주의 깊게 다시 확인한다.
- **탭 자동 완성 사용**: 터미널에서 파일명을 입력하기 시작하고 `Tab` 키를 누른다. 셸이 올바른 경우 이름을 자동으로 완성해주고, 그렇지 않으면 아무 일도 일어나지 않는다. 이는 오타를 피하는 좋은 방법이다.
- **파일 목록 확인**: `ls`(Linux/macOS) 또는 `dir`(Windows)를 사용하여 현재 디렉터리의 파일 목록을 보고 올바른 이름을 확인한다.

### 2. 원인: 잘못된 파일 경로

잘못된 디렉터리에 있을 수 있다. 실행하는 명령은 상대 경로나 절대 경로를 제공하지 않는 한 현재 디렉터리에서만 파일을 찾는다.

**예시:**
`index.html` 파일이 `src` 하위 디렉터리에 있지만, 프로젝트의 루트 디렉터리에 있는 경우.
```bash
# /my-project/ 에 있는 경우
git add index.html
# fatal: pathspec 'index.html' did not match any files
```

**해결책:**
- **올바른 경로 제공**: 현재 위치에서 파일까지의 전체 경로를 포함한다.
  ```bash
  git add src/index.html
  ```
- **디렉터리 변경**: 먼저 올바른 디렉터리로 이동한 다음 명령을 실행한다.
  ```bash
  cd src
  git add index.html
  ```

### 3. 원인: Git이 추적하지 않는 파일 (git rm의 경우)

`git rm` 명령은 Git 저장소에서 파일을 제거하는 데 사용된다. 아직 저장소에 커밋되지 않은 파일(즉, 추적되지 않는 파일)에 이 명령을 사용하려고 하면, Git은 추적 인덱스에 파일이 존재하지 않기 때문에 pathspec 오류를 발생시킨다.

**예시:**
아직 추가하거나 커밋하지 않은 새 파일 `temp.log`가 있는 경우.
```bash
git rm temp.log
# fatal: pathspec 'temp.log' did not match any files
```

**해결책:**
- **표준 `rm` 명령 사용**: 로컬 파일 시스템에서 파일을 삭제하고 싶고 Git이 추적하지 않는 경우, `git rm` 대신 표준 셸 명령을 사용한다.
  - Linux/macOS: `rm temp.log`
  - Windows: `del temp.log`
- **파일이 추적되는 경우**: Git이 추적하고 있지만 로컬 수정 사항도 있는 파일을 제거하려면 `-f`(force) 옵션을 사용해야 할 수 있다.
  ```bash
  git rm -f some-file.txt
  ```

### 4. 원인: 따옴표의 잘못된 사용

파일명에 공백이나 특수 문자가 포함된 경우, 따옴표로 묶어야 한다. 이를 잊으면 Git이 혼동할 수 있다.

**예시:**
```bash
git add my new file.txt
# Git은 'my', 'new', 'file.txt' 세 개의 개별 파일을 추가하려는 것으로 생각한다
# fatal: pathspec 'my' did not match any files
```

**해결책:**
- **따옴표 사용**: 전체 파일명을 큰따옴표로 묶는다.
  ```bash
  git add "my new file.txt"
  ```

이 네 가지 일반적인 문제(오타, 잘못된 경로, 추적되지 않는 파일, 따옴표 누락)를 확인하면 `fatal: pathspec '...' did not match any files` 오류를 쉽게 해결할 수 있다.

## 전문 보완 체크

**"Git "fatal: pathspec '...' did not match any files" 오류 해결 방법"**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 저장소 루트, 브랜치와 원격 상태, 인덱스와 작업 트리, 인증 또는 네트워크 경계를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

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
