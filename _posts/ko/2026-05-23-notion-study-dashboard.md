---
typora-root-url: ../
layout: single
title: >
  Notion 공부 대시보드 구성: 과목, 복습, 시험을 한 화면에서 관리하는 법
seo_title: >
  Notion 공부 대시보드 구성
date: 2026-05-23T23:59:55+09:00
last_modified_at: 2026-05-23T23:59:59+09:00
lang: ko
translation_id: notion-study-dashboard
header:
   teaser: /images/2026-05-23-notion-study-dashboard/notion-study-dashboard-hero.png
   overlay_image: /images/2026-05-23-notion-study-dashboard/notion-study-dashboard-hero.png
   overlay_filter: 0.35
excerpt: >
  Notion 공부 대시보드를 과목, 과제, 간격 복습, 오답노트, 시험 일정, 주간 회고 중심으로 실용적으로 구성하는 방법을 정리합니다.
seo_description: >
  Notion 공부 대시보드를 과목, 과제, 간격 복습, 오답노트, 시험 일정, 주간 회고 중심으로 실용적으로 구성하는 방법을 정리합니다.
categories:
  - ko_Study
tags:
  - Study
  - Notion
  - Productivity
  - Dashboard
  - Learning
---

## 핵심 요약

좋은 Notion 공부 대시보드는 예쁜 홈페이지가 아닙니다.
이번 주에 끝내야 할 일과 나중에 다시 떠올려야 할 학습 내용을 연결하는 시스템입니다.
핵심 database는 과목, 과제, 복습 큐, 오답노트, 시험입니다.

![과목 카드, 캘린더, 진행 그래프, 복습 큐, 시험 추적이 있는 공부 대시보드 이미지](/images/2026-05-23-notion-study-dashboard/notion-study-dashboard-hero.png)

이미지는 실용적인 대시보드 구조를 보여줍니다.
주간 일정, 과목 카드, 복습 상태, 진행 그래프, 오답 섹션이 있습니다.
목표는 Notion을 화려하게 꾸미는 것이 아닙니다.
"공부해야 하는데 무엇부터 하지?"에서 "지금 이걸 하면 된다"로 가는 시간을 줄이는 것입니다.

## 대시보드의 원칙

공부 대시보드는 세 질문에 빠르게 답해야 합니다.

```text
무엇을 끝내야 하는가?
무엇을 복습해야 하는가?
무엇이 약해지고 있는가?
```

첫 화면이 명언, 아이콘, 쓰지 않는 widget으로 가득하면 보기에는 좋아도 역할을 못 합니다.
학생에게 필요한 것은 바쁜 주에도 버티는 시스템입니다.

Notion database와 filtered view를 사용하면 같은 공부 데이터를 여러 형태로 보여줄 수 있습니다.
복사해서 다른 페이지에 다시 적을 필요가 줄어듭니다.

## Database 1. 과목

먼저 `Courses` database를 만듭니다.
각 row는 하나의 수업, 시험 과목, 학습 트랙입니다.

추천 properties:

| Property | Type | 목적 |
| --- | --- | --- |
| Course | Title | 과목 이름 |
| Status | Select | active, paused, completed |
| Exam Date | Date | 다음 주요 시험 |
| Priority | Select | high, medium, low |
| Weekly Target | Text | 이번 주 핵심 목표 |
| Related Assignments | Relation | 과제 database 연결 |
| Related Reviews | Relation | 복습 database 연결 |

이 database는 작게 유지합니다.
모든 노트를 넣는 곳이 아니라 control panel입니다.

## Database 2. 과제

과제는 deadline 중심입니다.
숙제, 에세이, 읽기 과제, lab, coding task, project milestone이 여기에 들어갑니다.

추천 properties:

| Property | Type | 목적 |
| --- | --- | --- |
| Task | Title | 과제 이름 |
| Course | Relation | 과목 연결 |
| Due Date | Date | 마감일 |
| Status | Select | not started, doing, submitted |
| Effort | Select | small, medium, large |
| Next Step | Text | 다음 행동 하나 |

가장 중요한 view는 `Due This Week`입니다.
7일 안에 마감되는 과제만 보이게 filter하고, due date 기준으로 sort합니다.

`study`처럼 모호한 next step은 피합니다.
`문제 1-10 풀기`, `서론 초안 작성`처럼 행동으로 적습니다.

## Database 3. 복습 큐

이 부분이 대시보드를 단순 task list가 아니라 학습 시스템으로 만듭니다.
review item은 나중에 다시 떠올려야 할 모든 내용입니다.

- 공식
- 단어 묶음
- 개념
- 코딩 패턴
- 역사 날짜
- 실수 유형
- 그림

추천 properties:

| Property | Type | 목적 |
| --- | --- | --- |
| Item | Title | 복습할 내용 |
| Course | Relation | 과목 |
| Review Date | Date | 다음 복습일 |
| Confidence | Select | low, medium, high |
| Source | URL 또는 Text | 노트, 책, 강의, 문제 |
| Result | Select | recalled, slow, missed |

추천 view:

- `Review Today`
- `Review This Week`
- `Low Confidence`
- `Missed Last Time`

이 구조는 active recall과 spaced repetition을 돕습니다.
노트를 모으는 것이 아니라 retrieval을 예약하는 방식입니다.

## Database 4. 오답노트

오답노트는 일반 노트와 다릅니다.
왜 틀렸는지와 다음에 어떻게 막을지를 기록해야 합니다.

추천 구조:

| Property | Type | 목적 |
| --- | --- | --- |
| Mistake | Title | 짧은 실수 이름 |
| Course | Relation | 과목 |
| Type | Select | concept, procedure, careless, memory, strategy |
| Cause | Text | 왜 발생했는가 |
| Prevention | Text | 다음에 무엇을 할 것인가 |
| Retest Date | Date | 다시 풀 날짜 |

가장 중요한 것은 prevention입니다.
"조심하기"는 예방 규칙이 아닙니다.
"미분 전에 outer function과 inner function을 표시한다"는 예방 규칙입니다.

## Database 5. 시험

시험 계획은 deadline과 복습 압박을 연결해야 합니다.
`Exams` database에는 아래 항목을 둡니다.

- 시험 이름
- 과목
- 날짜
- 범위
- 반영 비율
- 준비도
- 다음 모의 테스트 날짜

그리고 dashboard에는 날짜순 view를 둡니다.
시험이 가까운데 준비도가 낮다면 검색하지 않아도 바로 보여야 합니다.

## 추천 대시보드 레이아웃

한 페이지에 아래처럼 배치합니다.

```text
상단:
- Due this week
- Review today
- Upcoming exams

중단:
- Courses
- Retest가 필요한 오답
- Low-confidence review items

하단:
- Weekly study review
- Completed this week
- Notes inbox
```

모든 database view를 한 화면에 넣지 마세요.
대시보드는 archive가 아닙니다.
오늘의 공부 판단이 일어나는 곳입니다.

## 주간 사용 흐름

대시보드는 이렇게 사용합니다.

```text
매일 아침:
1. Due this week 확인
2. Review today 확인
3. Deep work block 하나 선택

공부 후:
1. 약한 개념을 Review Queue에 추가
2. 반복 실수를 Mistake Notes에 추가
3. 과제 상태 갱신

주말:
1. 주간 공부 회고 실행
2. 놓친 항목을 다음 주로 이동
3. 과목 우선순위 갱신
```

이 흐름이 있어야 시스템이 살아 있습니다.
한 번 멋지게 만들고 업데이트하지 않으면 대시보드는 전시물이 됩니다.

## 흔한 실수

첫 번째 실수는 과하게 만드는 것입니다.
어디를 클릭해야 할지 결정하는 데 10분이 걸리면 너무 복잡합니다.

두 번째 실수는 노트와 task를 한 database에 섞는 것입니다.
노트는 참고 자료입니다.
task에는 due date와 next action이 필요합니다.
review item에는 recall date가 필요합니다.

세 번째 실수는 filtered view를 쓰지 않는 것입니다.
같은 assignment database로 `due today`, `due this week`, `submitted`를 중복 없이 보여줄 수 있습니다.

네 번째 실수는 지표를 너무 많이 추적하는 것입니다.
행동을 바꾸는 데 필요한 만큼만 추적하세요.
대부분의 학생에게는 deadline, confidence, review date, mistake type이면 충분합니다.

## 함께 보면 좋은 글

- [주간 공부 회고 템플릿](/ko_Study/weekly-study-review/)
- [Spaced Repetition Schedule](/ko_Study/spaced-repetition-schedule/)
- [Active Recall Study Method](/ko_Study/active-recall-study-method/)
- [Notion Help: Database views](https://www.notion.com/help/views)

## 최종 체크리스트

사용 전 확인합니다.

```text
[ ] 과목과 과제가 분리되어 있다.
[ ] 복습 항목에 다음 복습일이 있다.
[ ] 오답에는 원인과 예방 규칙이 있다.
[ ] 첫 화면에 이번 주 실제 할 일이 보인다.
[ ] 오래된 완료 항목은 메인 화면에서 숨겨져 있다.
[ ] 주말 회고가 다음 주 우선순위를 갱신한다.
```

좋은 Notion 공부 대시보드는 조용하고 유용합니다.
다음 행동을 보여줘야지, 미루기 위한 새 공간이 되면 안 됩니다.

## 자주 묻는 질문

### 이 글은 언제 먼저 적용하면 좋나요?

시험 준비, 개발 공부, 언어 학습처럼 배운 내용을 실제로 꺼내 써야 하는 상황에서 가장 효과적입니다.

### 초보자가 가장 먼저 확인할 부분은 무엇인가요?

처음에는 공부 시간을 늘리기보다 오늘 설명할 수 있는 내용, 풀 수 있는 문제, 다시 틀린 부분을 기록하세요.

### 더 찾아볼 때 어떤 키워드를 쓰면 좋나요?

추가 검색할 때는 "Notion 공부 대시보드 구성: 과목, 복습, 시험을 한 화면에서 관리하는 법" 같은 핵심 문구와 active recall, spaced repetition, study plan, mistake note 같은 학습 키워드를 붙이면 좋습니다.
