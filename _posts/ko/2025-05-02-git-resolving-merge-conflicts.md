---
typora-root-url: ../
layout: single
title: >
   Git 병합 충돌(Merge Conflict) 해결하는 방법

date: 2025-05-02T07:36:00+09:00
lang: ko
translation_id: git-resolving-merge-conflicts
header:
   teaser: /images/header_images/overlay_image_git.png
   overlay_image: /images/header_images/overlay_image_git.png
   overlay_filter: 0.5
   image_description: >
     이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Git 병합 충돌(Merge Conflict) 해결하는 방법
excerpt: >
    Git에서 브랜치를 합칠 때 발생하는 병합 충돌을 이해하고 해결하는 단계별 가이드입니다.
seo_description: >
    Git에서 브랜치를 합칠 때 발생하는 병합 충돌을 이해하고 해결하는 단계별 가이드입니다.
categories:
  - ko_Troubleshooting
tags:
  - Git
  - Merge
  - Conflict
  - Branch
---


![이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Git 병합 충돌(Merge Conflict) 해결하는 방법](/images/header_images/overlay_image_git.png)
## 병합 충돌이란?

병합 충돌은 서로 다른 변경 사항을 가진 두 브랜치를 병합하려고 할 때 발생합니다. Git이 어떤 변경 사항을 유지해야 할지 자동으로 결정할 수 없는 경우입니다. 이는 일반적으로 동일한 파일의 동일한 코드 라인이 두 브랜치에서 모두 수정되었을 때 발생합니다.

충돌이 발생하면 Git은 병합 프로세스를 일시 중지하고 사용자가 수동으로 충돌을 해결하기를 기다립니다.

## 문제 상황

`main` 브랜치와 `feature` 브랜치가 있다고 가정해 보겠습니다. 두 브랜치 모두 `style.css` 파일에 변경 사항이 있습니다.

**`main` 브랜치에서 `style.css`는 다음과 같이 변경되었습니다:**
```css
body {
  color: #333;
  font-family: Arial, sans-serif;
}
```

**`feature` 브랜치에서 `style.css`는 다음과 같이 변경되었습니다:**
```css
body {
  color: #444;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
}
```

`feature`를 `main`으로 병합하려고 할 때:
```bash
git switch main
git merge feature
```

다음과 같은 오류 메시지가 표시됩니다.
```
Auto-merging style.css
CONFLICT (content): Merge conflict in style.css
Automatic merge failed; fix conflicts and then commit the result.
```

## 해결 방법

### 1. 충돌 파일 식별하기

Git은 어떤 파일에 충돌이 있는지 알려줍니다. `git status`를 사용하여 병합되지 않은 경로 목록을 볼 수도 있습니다.

```bash
git status
On branch main
You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
  (use "git add <file>..." to mark resolution)
        both modified:   style.css

no changes added to commit (use "git add" and/or "git commit -a")
```

### 2. 파일 열고 편집하기

코드 편집기에서 `style.css`를 엽니다. Git은 충돌 영역을 표시합니다.

```css
body {
<<<<<<< HEAD
  color: #333;
  font-family: Arial, sans-serif;
=======
  color: #444;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
>>>>>>> feature
}
```

-   `<<<<<<< HEAD`: 현재 브랜치(`main`)의 충돌 변경 사항 시작을 표시합니다.
-   `=======`: 두 충돌 변경 사항을 구분합니다.
-   `>>>>>>> feature`: 병합하려는 브랜치(`feature`)의 충돌 변경 사항 끝을 표시합니다.

### 3. 충돌 해결하기

최종 버전이 어떻게 보여야 할지 결정해야 합니다. 한 버전을 선택하거나 다른 버전을 선택하거나 둘 다의 조합을 선택할 수 있습니다.

`feature` 브랜치의 `font-family`와 `main` 브랜치의 `color`를 유지하고 싶다고 가정해 보겠습니다. 파일을 다음과 같이 편집합니다.

```css
body {
  color: #333;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
}
```

충돌 마커(`<<<<<<<`, `=======`, `>>>>>>>`)를 반드시 제거해야 합니다.

### 4. 해결된 파일 스테이징하기

파일에서 충돌을 해결한 후에는 파일을 스테이징하여 Git에 충돌이 해결되었음을 알려야 합니다.

```bash
git add style.css
```

### 5. 병합 커밋하기

모든 충돌이 해결되고 파일이 스테이징되면 병합 커밋을 생성하여 병합을 완료할 수 있습니다.

```bash
git commit
```

Git은 "Merge branch 'feature'"와 같은 미리 채워진 커밋 메시지와 함께 편집기를 엽니다. 그대로 두거나 수정할 수 있습니다. 편집기를 저장하고 닫아 커밋을 생성합니다.

이제 병합이 완료되었습니다.

## 병합 중단하기

복잡한 병합에 들어가서 다시 시작하고 싶다면 언제든지 병합 프로세스를 중단할 수 있습니다.

```bash
git merge --abort
```

이렇게 하면 브랜치가 병합을 시작하기 전의 상태로 돌아갑니다.

## 결론

병합 충돌은 Git 작업의 정상적인 부분입니다. 충돌 마커가 무엇을 의미하는지 이해하면 자신 있게 해결할 수 있습니다. 최종 결과가 올바른지 확인하기 위해 항상 변경 사항을 신중하게 검토하세요.

## 전문 보완 체크

**Git 병합 충돌(Merge Conflict) 해결하는 방법**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 저장소 루트, 브랜치와 원격 상태, 인덱스와 작업 트리, 인증 또는 네트워크 경계를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

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

독자가 **Git 병합 충돌(Merge Conflict) 해결하는 방법**의 첫 번째 권장 조치를 이미 시도했지만 결과가 여전히 불확실하다고 가정해 봅니다. 다음 단계는 여러 해결책을 한꺼번에 시험하는 것이 아니라 짧은 감사 기록을 만드는 것입니다. 먼저 어떤 판단을 하려는지 한 문장으로 쓰고, 환경을 한 문장으로 적고, 관찰된 결과를 한 문장으로 남깁니다. 그다음 저장소 루트, 브랜치와 원격 상태, 인덱스와 작업 트리, 인증 또는 네트워크 경계를 이미 확보한 사실과 대조합니다. 이렇게 해야 글이 서로 끊어진 팁 목록이 아니라 검증 가능한 절차가 됩니다.

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
