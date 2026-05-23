---
typora-root-url: ../
layout: single
title: >
  코딩 공부 로드맵: 기초부터 포트폴리오 프로젝트까지 가는 실전 순서
seo_title: >
  코딩 공부 로드맵과 포트폴리오 순서
date: 2026-05-23T23:59:57+09:00
last_modified_at: 2026-05-23T23:59:59+09:00
lang: ko
translation_id: coding-study-roadmap
header:
   teaser: /images/2026-05-23-coding-study-roadmap/coding-roadmap-hero.png
   overlay_image: /images/2026-05-23-coding-study-roadmap/coding-roadmap-hero.png
   overlay_filter: 0.35
   image_description: >
     코딩 공부 로드맵: 기초부터 포트폴리오 프로젝트까지 가는 실전 순서 주제를 한눈에 설명하는 시각 자료입니다.
excerpt: >
  코딩 공부는 한 언어의 기초, 작은 문제 풀이, 디버깅, Git, 작은 프로젝트, 배포, 포트폴리오 순서로 진행하는 것이 현실적입니다.
seo_description: >
  코딩 공부는 한 언어의 기초, 작은 문제 풀이, 디버깅, Git, 작은 프로젝트, 배포, 포트폴리오 순서로 진행하는 것이 현실적입니다.
categories:
  - ko_Study
tags:
  - Coding
  - Study
  - Roadmap
  - Programming
  - Portfolio
---

## 핵심 요약

실전적인 코딩 공부 로드맵은 모든 언어와 framework를 한꺼번에 시작하지 않습니다.
한 언어를 고르고, 기초 문법을 익히고, 작은 문제를 풀고, 작은 프로젝트를 만들고, debugging과 Git을 배우고, 포트폴리오 프로젝트를 공개하는 순서가 좋습니다.

![기초, 문제 풀이, 디버깅, Git, 포트폴리오 milestone으로 이어지는 coding study roadmap](/images/2026-05-23-coding-study-roadmap/coding-roadmap-hero.png)

이미지는 milestone path를 보여줍니다.
목표는 강의를 모으는 것이 아닙니다.
작동하는 코드를 만들고, 오류를 고치고, 내가 만든 것을 설명하는 것입니다.

## 기본 로드맵

아래 순서를 사용합니다.

```text
1. 언어 하나를 고른다.
2. 문법과 control flow를 익힌다.
3. data structure를 연습한다.
4. 작은 문제를 푼다.
5. 작은 project를 만든다.
6. debugging을 배운다.
7. Git과 GitHub를 배운다.
8. project 하나를 배포하거나 공개한다.
9. 회고하고 반복한다.
```

이 순서는 학습을 output과 연결합니다.

## Track 하나 고르기

처음 8-12주는 track 하나만 고릅니다.

| Goal | Good first stack |
| --- | --- |
| Web frontend | HTML, CSS, JavaScript |
| Backend | Python 또는 JavaScript, HTTP, database basics |
| Data analysis | Python, pandas, notebooks, visualization |
| Automation | Python, files, APIs, scheduling |
| Mobile later | 기초 후 JavaScript 또는 platform-specific basics |

처음부터 다섯 stack을 시작하지 않습니다.
넓게 보는 것은 생산적으로 느껴지지만, 초반 switching은 feedback을 늦춥니다.

## 주간 계획

반복 가능한 1주 구조를 씁니다.

```text
2일: concept 하나 배우기
2일: 작은 exercise 풀기
1일: tiny feature 만들기
1일: debug하고 note 쓰기
1일: review하고 다음 주 계획
```

시간이 부족하면 feedback을 줄이지 말고 범위를 줄입니다.
매주 작은 working feature 하나만 만들어도 충분히 의미 있습니다.

## 처음 만들기 좋은 것

초보자에게 좋은 프로젝트:

- local storage를 쓰는 todo list
- expense tracker
- flashcard app
- weather lookup
- Markdown note viewer
- simple blog
- file organizer script
- API data dashboard

처음부터 거대한 clone project를 만들지 않습니다.
끝내고 설명할 수 있을 만큼 작은 것을 만듭니다.

## Debugging Checklist

초보자에게 debugging 연습은 필수입니다.

```text
[ ] 문제를 재현할 수 있는가?
[ ] 정확한 error message는 무엇인가?
[ ] 최근 무엇이 바뀌었는가?
[ ] 예제를 더 작게 줄일 수 있는가?
[ ] input과 output을 확인했는가?
[ ] stack trace를 읽었는가?
[ ] fix가 실제로 해결됐는지 검증했는가?
```

관련 기술 글:

- [Python pip install 실패 해결](/ko_troubleshooting/python-pip-install-failed/)
- [Windows에서 python 명령어가 안 될 때](/ko_troubleshooting/python-command-not-found-windows/)
- [GitHub Actions build failed 해결 방법](/ko_troubleshooting/github-actions-build-failed/)

## Portfolio Rule

포트폴리오 프로젝트에는 아래가 보여야 합니다.

- 해결한 문제
- screenshot 또는 demo
- setup instructions
- main features
- tradeoffs
- 다음에 개선할 점

작지만 끝난 프로젝트가 크지만 끝나지 않은 프로젝트보다 낫습니다.

## 흔한 실수

- 매주 언어를 바꿉니다.
- 강의만 보고 코드를 쓰지 않습니다.
- 오류를 피하고 debugging을 배우지 않습니다.
- 끝낼 수 없을 만큼 큰 프로젝트를 시작합니다.
- Git을 마지막까지 미룹니다.
- README를 쓰지 않습니다.
- 공부 시간을 course hour로만 측정합니다.

## 함께 보면 좋은 글

- [Active Recall 공부법](/ko_study/active-recall-study-method/)
- [Pomodoro와 Deep Work](/ko_study/pomodoro-deep-work/)
- [Notion 공부 대시보드 구성](/ko_study/notion-study-dashboard/)

## 자주 묻는 질문

### 이 글은 언제 먼저 적용하면 좋나요?

시험 준비, 개발 공부, 언어 학습처럼 배운 내용을 실제로 꺼내 써야 하는 상황에서 가장 효과적입니다.

### 초보자가 가장 먼저 확인할 부분은 무엇인가요?

처음에는 공부 시간을 늘리기보다 오늘 설명할 수 있는 내용, 풀 수 있는 문제, 다시 틀린 부분을 기록하세요.

### 더 찾아볼 때 어떤 키워드를 쓰면 좋나요?

추가 검색할 때는 "코딩 공부 로드맵: 기초부터 포트폴리오 프로젝트까지 가는 실전 순서" 같은 핵심 문구와 active recall, spaced repetition, study plan, mistake note 같은 학습 키워드를 붙이면 좋습니다.

## 참고 자료

- roadmap.sh developer roadmaps: https://roadmap.sh/
- MDN Learn Web Development: https://developer.mozilla.org/en-US/docs/Learn
- GitHub Skills: https://skills.github.com/
