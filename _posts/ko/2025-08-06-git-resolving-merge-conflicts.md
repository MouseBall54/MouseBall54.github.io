---
typora-root-url: ../
layout: single
title: >
   Git 병합 충돌(Merge Conflict) 해결하는 방법
date: 2025-08-06T10:10:00+09:00
header:
   teaser: /images/header_images/overlay_image_git.png
   overlay_image: /images/header_images/overlay_image_git.png
   overlay_filter: 0.5
excerpt: >
    Git에서 브랜치를 합칠 때 발생하는 병합 충돌을 이해하고 해결하는 단계별 가이드입니다.
categories:
  - ko_Troubleshooting
tags:
  - Git
  - Merge
  - Conflict
  - Branch
---

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
