---
typora-root-url: ../
layout: single
title: "Git에서 'fatal: refusing to merge unrelated histories' 오류 해결 방법"

date: 2025-02-01T07:36:00+09:00
lang: ko
translation_id: git-refusing-to-merge-unrelated-histories
excerpt: "두 프로젝트의 커밋 기록이 다를 때 `--allow-unrelated-histories` 플래그를 사용하여 Git의 'fatal: refusing to merge unrelated histories' 오류를 해결하는 방법을 알아봅니다."
seo_description: "두 프로젝트의 커밋 기록이 다를 때 `--allow-unrelated-histories` 플래그를 사용하여 Git의 'fatal: refusing to merge unrelated histories' 오류를 해결하는 방법을 알아봅니다."
header:
   teaser: /images/header_images/overlay_image_git.png
   overlay_image: /images/header_images/overlay_image_git.png
   overlay_filter: 0.5
   image_description: >
     이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Git에서 'fatal: refusing to merge unrelated histories' 오류 해결 방법
categories:
  - ko_Troubleshooting
tags:
  - Git
  - Version Control
  - Merge
  - Troubleshooting
---


![이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Git에서 'fatal: refusing to merge unrelated histories' 오류 해결 방법](/images/header_images/overlay_image_git.png)
## "fatal: refusing to merge unrelated histories" 오류란 무엇인가?

이 Git 오류는 공통 커밋 기록을 공유하지 않는 두 브랜치를 `git pull` 또는 `git merge`하려고 할 때 발생한다. 이는 사용자가 관련 없는 두 프로젝트를 실수로 병합하는 것을 방지하기 위해 Git 2.9 버전에 도입된 안전 기능이다.

이 상황은 종종 다음과 같은 경우에 발생한다:

1.  자체 커밋이 있는 새 로컬 저장소를 만든 다음, 자체적인 별도 기록이 있는 원격 저장소에서 `pull`하려고 할 때.
2.  프로젝트의 `.git` 디렉터리가 삭제되고 다시 초기화되어 원래 커밋 기록을 잃어버린 후, 원격 사본과 조정하려고 할 때.

## 일반적인 원인

근본적인 원인은 병합하려는 두 브랜치가 완전히 분리되고 독립적인 기록을 가지고 있기 때문이다. Git은 병합의 기준으로 사용할 공통 조상 커밋을 찾을 수 없으므로, 중지하고 명시적인 확인을 요청하기 위해 이 오류를 표시한다.

- **저장소 A 기록:** `A -> B -> C`
- **저장소 B 기록:** `X -> Y -> Z`

이 두 기록을 병합하는 것은 공유된 시작점이 없기 때문에 간단한 과정이 아니다.

## 해결 방법

이 두 관련 없는 기록을 병합하려는 것이 확실하다면, `--allow-unrelated-histories` 플래그를 사용할 수 있다. 이 플래그는 Git에게 상황을 이해하고 병합을 진행하기를 원한다고 명시적으로 알려준다.

### 1단계: 병합 확인

플래그를 사용하기 전에, 올바른 저장소에 있는지, 그리고 이 기록들을 병합하는 것이 정말로 원하는 작업인지 다시 확인한다. 이 작업은 일반적으로 되돌릴 수 없다.

### 2단계: 플래그를 사용하여 병합 수행

`git pull` 또는 `git merge`를 실행할 때 `--allow-unrelated-histories` 옵션을 추가한다.

#### `git pull`의 경우:

원격 저장소에서 `pull`하는 경우:

```bash
# 예시: origin 원격의 main 브랜치에서 pull
git pull origin main --allow-unrelated-histories
```

이렇게 하면 원격 브랜치를 가져와 현재 로컬 브랜치에 병합하고, 두 기록을 하나로 묶는 새 병합 커밋을 생성한다.

#### `git merge`의 경우:

두 로컬 브랜치를 병합하는 경우:

```bash
# 예시: 'unrelated-branch'라는 이름의 브랜치 병합
git merge unrelated-branch --allow-unrelated-histories
```

### 3단계: 병합 충돌 해결 (필요 시)

프로젝트가 관련이 없기 때문에, 특히 두 프로젝트 모두에 존재할 수 있는 `README.md` 또는 `.gitignore`와 같은 파일에서 병합 충돌이 발생할 가능성이 높다.

1.  **충돌하는 파일을 열고** 필요에 따라 차이점을 해결한다.
2.  `git add`를 사용하여 **해결된 파일을 스테이징**한다.
3.  **병합을 커밋**하여 프로세스를 마무리한다.

```bash
# 충돌 해결 후
git add .
git commit -m "관련 없는 기록 병합"
```

### 언제 유용한가?

- **템플릿을 기반으로 새 프로젝트 시작**: 로컬 저장소를 초기화한 다음 원격 템플릿을 가져오기로 결정할 수 있다.
- **저장소 마이그레이션**: 한 버전 관리 시스템에서 다른 시스템으로 또는 한 Git 호스트에서 다른 호스트로 이동할 때 기록이 연결되지 않을 수 있다.
- **손상된 저장소 복구**: 로컬 `.git` 디렉터리가 손실된 경우 원격 백업과 강제로 병합해야 할 수 있다.

`--allow-unrelated-histories` 플래그를 사용하면 Git의 기본 안전 검사를 무시하고 별도의 커밋 기록을 가진 두 프로젝트를 성공적으로 결합할 수 있다.

## 전문 보완 체크

**Git에서 'fatal: refusing to merge unrelated histories' 오류 해결 방법**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 저장소 루트, 브랜치와 원격 상태, 인덱스와 작업 트리, 인증 또는 네트워크 경계를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

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
