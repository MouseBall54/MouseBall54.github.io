---
typora-root-url: ../
layout: single
title: "Git에서 'error: failed to push some refs to' 오류 해결 방법"

lang: ko
translation_id: git-failed-to-push-some-refs
excerpt: "원격 저장소의 최신 변경 사항을 가져온 후 자신의 변경 사항을 푸시하여 Git의 'failed to push some refs' 오류를 해결합니다."
header:
   teaser: /images/header_images/overlay_image_git.png
   overlay_image: /images/header_images/overlay_image_git.png
   overlay_filter: 0.5
categories:
  - ko_Troubleshooting
tags:
  - Git
  - Version Control
  - Troubleshooting
  - Push Error
---

## "error: failed to push some refs to"는 무엇을 의미할까?

이 일반적인 Git 오류는 로컬 변경 사항을 원격 저장소로 `git push`하려고 할 때, 원격 저장소에는 있지만 로컬 기록에는 없는 커밋이 있을 때 발생한다. Git은 원격 변경 사항을 덮어쓰고 커밋 기록을 잃는 것을 방지하기 위해 푸시를 막는다.

이 문제는 보통 마지막으로 `pull`한 이후에 다른 팀 멤버가 동일한 브랜치에 변경 사항을 푸시했을 때 발생한다.

## 일반적인 원인

근본 원인은 로컬 브랜치와 원격 브랜치 간의 차이(divergence) 때문이다. 로컬 저장소가 원격 저장소의 최신 상태를 반영하지 못하고 있다.

- **원격 브랜치:** `A -> B -> D`
- **로컬 브랜치:** `A -> B -> C`

이 시나리오에서 커밋 `D`는 원격에는 있지만 로컬에는 없다. 로컬 브랜치에는 원격에 없는 커밋 `C`가 있다. Git은 단순한 빨리 감기(fast-forward) 푸시를 수행할 수 없으므로 이를 거부한다.

## 해결 방법

해결책은 다시 푸시하기 전에 원격 변경 사항을 로컬 브랜치에 통합하는 것이다. 이는 일반적으로 `git pull`을 사용하여 수행된다.

### 1. 원격 변경 사항 가져오고 병합하기

가장 간단한 방법은 `git pull`을 사용하는 것이다. 이는 `git fetch`(원격에서 최신 변경 사항을 가져옴)와 `git merge`(로컬 변경 사항과 병합)를 합친 명령어다.

```bash
# 푸시하려는 브랜치로 전환
git checkout your-branch-name

# 원격에서 최신 변경 사항을 pull
git pull origin your-branch-name
```

### 2. 병합 충돌 해결하기 (발생 시)

로컬에서 변경한 내용이 원격의 변경 사항과 충돌하는 경우, Git은 병합 프로세스를 일시 중지하고 충돌을 해결하도록 요청한다.

1.  **충돌하는 파일 열기:** 충돌 마커(`<<<<<<<`, `=======`, `>>>>>>>`)를 찾는다.
2.  **파일 편집:** 어떤 변경 사항을 유지할지(로컬, 원격 또는 둘의 조합) 결정하고 충돌 마커를 제거한다.
3.  **해결된 파일 스테이징:** `git add`를 사용하여 충돌이 해결되었음을 표시한다.

```bash
# 편집기에서 충돌을 해결한 후
git add .
```

4.  **병합 완료:** 병합 프로세스를 계속 진행한다. `git pull`은 종종 병합 커밋을 자동으로 생성하므로, 기본 커밋 메시지를 저장하기만 하면 될 수 있다.

```bash
# 병합 커밋이 필요한 경우 Git이 편집기를 연다.
# 편집기를 저장하고 닫아 병합 커밋을 생성한다.
git commit
```

### 3. 변경 사항 푸시하기

로컬 브랜치가 최신 상태이고 모든 충돌이 해결되면, 변경 사항을 원격 저장소에 안전하게 푸시할 수 있다.

```bash
git push origin your-branch-name
```

### 대안: `rebase` 사용하기

병합의 대안으로 `rebase`를 사용할 수 있다. `git pull --rebase`는 원격 변경 사항을 가져온 다음 로컬 커밋을 원격 브랜치 기록 위에 다시 적용한다. 이는 더 깨끗하고 선형적인 프로젝트 기록을 만든다.

```bash
# rebase와 함께 pull
git pull --rebase origin your-branch-name

# 충돌이 발생하면 해결한 후 계속 진행
git add .
git rebase --continue

# rebase된 브랜치를 푸시
git push origin your-branch-name
```

**주의:** `rebase`는 커밋 기록을 재작성하므로, 익숙하지 않다면 다른 개발자와 공유하는 브랜치에서는 사용을 피하는 것이 좋다.

이 단계를 따르면 로컬 저장소를 원격과 동기화하여 변경 사항을 성공적으로 푸시할 수 있다.
