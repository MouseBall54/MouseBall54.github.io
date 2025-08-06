---
typora-root-url: ../
layout: single
title: "Git에서 'fatal: refusing to merge unrelated histories' 오류 해결 방법"

lang: ko
translation_id: git-refusing-to-merge-unrelated-histories
excerpt: "두 프로젝트의 커밋 기록이 다를 때 `--allow-unrelated-histories` 플래그를 사용하여 Git의 'fatal: refusing to merge unrelated histories' 오류를 해결하는 방법을 알아봅니다."
header:
   teaser: /images/header_images/overlay_image_git.png
   overlay_image: /images/header_images/overlay_image_git.png
   overlay_filter: 0.5
categories:
  - ko_Troubleshooting
tags:
  - Git
  - Version Control
  - Merge
  - Troubleshooting
---

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
