---
typora-root-url: ../
layout: single
title: >
  Spaced repetition 복습 일정: 실제로 유지할 수 있는 반복 학습 계획
seo_title: >
  Spaced repetition 복습 일정
date: 2026-05-23T23:58:00+09:00
last_modified_at: 2026-05-23T23:59:59+09:00
lang: ko
translation_id: spaced-repetition-schedule
header:
   teaser: /images/2026-05-23-spaced-repetition-schedule/spaced-repetition-hero.png
   overlay_image: /images/2026-05-23-spaced-repetition-schedule/spaced-repetition-hero.png
   overlay_filter: 0.35
excerpt: >
  Spaced repetition은 같은 내용을 몰아서 반복하지 않고, 시간이 지난 뒤 다시 떠올리게 만드는 복습 일정입니다.
seo_description: >
  Spaced repetition은 같은 내용을 몰아서 반복하지 않고, 시간이 지난 뒤 다시 떠올리게 만드는 복습 일정입니다.
categories:
  - ko_Study
tags:
  - Study
  - SpacedRepetition
  - Learning
  - Memory
  - Productivity
---

## 핵심 요약

Spaced repetition은 한 번에 여러 번 반복하는 대신, 점점 벌어지는 간격으로 다시 복습하는 방법입니다.
처음 시작할 때는 아래 일정이면 충분합니다.

```text
Day 0: 배우고 스스로 테스트
Day 1: 첫 지연 복습
Day 3: 두 번째 복습
Day 7: 주간 복습
Day 14: 긴 간격 복습
Day 30: 유지 여부 확인
```

![기억 checkpoint가 표시된 spaced repetition 복습 calendar](/images/2026-05-23-spaced-repetition-schedule/spaced-repetition-hero.png)

이미지는 복습 지점이 시간 위에 흩어져 있는 구조를 보여줍니다.
목표는 모든 노트를 매일 보는 것이 아닙니다.
기억이 완전히 사라지기 전, 다시 떠올리기 조금 어려운 시점에 만나는 것이 목표입니다.

## Spacing이 작동하는 이유

같은 내용을 하루 밤에 다섯 번 보면 익숙하게 느껴집니다.
하지만 그 익숙함은 오래가지 않을 수 있습니다.
시간 간격을 둔 복습은 다음 review에서 약간의 노력을 만들고, 그 retrieval effort가 기억을 강화하는 데 도움이 됩니다.

Spaced repetition은 active recall과 함께 쓸 때 효과가 좋습니다.
Card를 그냥 다시 읽지 말고 먼저 답해야 합니다.

아래처럼 나누어 생각하면 쉽습니다.

```text
spacing = 언제 복습할 것인가
active recall = 어떻게 복습할 것인가
```

다시 읽기만 일정에 넣으면 calendar는 성실해 보이지만 기억 효과는 약할 수 있습니다.

## 초보자용 일정

처음 시작한다면 아래 표를 사용합니다.

| Review | Timing | 할 일 |
| --- | --- | --- |
| Learn | Day 0 | 읽기, 풀기, 요약 |
| First review | Day 0 늦게 또는 Day 1 | 기억에서 답하기 |
| Second review | Day 3 | 약한 부분 다시 테스트 |
| Third review | Day 7 | 오래된 주제와 섞기 |
| Fourth review | Day 14 | 약한 card만 active로 유지 |
| Retention check | Day 30 | 힌트 없이 테스트 |

이 일정은 법칙이 아닙니다.
출발점입니다.
어려운 내용은 더 짧은 간격이 필요하고, 쉬운 내용은 더 오래 기다릴 수 있습니다.

## 무엇을 일정에 넣을까

모든 문장을 flashcard app에 넣지 않습니다.
그렇게 하면 공부가 아니라 관리 업무가 됩니다.

좋은 후보:

- 정확히 말해야 하는 definition
- formula
- command
- vocabulary
- diagram
- common mistake
- 헷갈리기 쉬운 구분

나쁜 후보:

- 긴 문단 전체
- 애매한 reminder
- 하나의 card 안에 여러 질문이 섞인 것
- 쉽게 찾아볼 수 있고 외울 필요가 낮은 사실

좋은 card는 한 가지만 묻습니다.
One card, one answer입니다.

## 실전 Card Format

아래 구조를 사용합니다.

```text
Question:
Answer:
Example:
Source:
Next review:
Difficulty:
```

Programming 예시:

```text
Question: Windows에서 Python venv를 어떻게 activate하는가?
Answer: .\.venv\Scripts\activate
Example: python -m venv .venv 후 실행
Source: project notes
Next review: Day 3
Difficulty: medium
```

Economy 예시:

```text
Question: 복리란 무엇인가?
Answer: 원금과 이미 붙은 이자에 다시 이자가 붙는 구조
Example: 1,050의 5%는 50이 아니라 52.50
Source: Investor.gov
Next review: Day 7
Difficulty: easy
```

## 주간 정리 루틴

Spaced repetition system은 queue가 너무 커지면 실패합니다.
주간 정리 루틴을 넣어야 합니다.

매주 아래를 확인합니다.

```text
1. 너무 쉬운 card를 삭제한다.
2. 질문이 두 개인 card를 나눈다.
3. 헷갈리는 prompt를 다시 쓴다.
4. 가치가 낮은 card는 archive로 옮긴다.
5. 자주 틀리는 card만 active로 유지한다.
```

시스템은 공부를 가볍게 만들어야 합니다.
두 번째 일처럼 느껴진다면 card design이 잘못됐을 가능성이 큽니다.

## Active Recall과 함께 쓰기

Spaced repetition은 복습 시점이고, active recall은 복습 행동입니다.

Review session은 이렇게 진행합니다.

```text
1. 질문만 읽는다.
2. 보지 않고 답한다.
3. 정답을 확인한다.
4. easy, medium, hard로 표시한다.
5. 난이도에 따라 다음 복습을 예약한다.
```

어떤 card가 계속 어렵다면 간격만 줄이지 않습니다.
Card 자체를 고칩니다.
너무 넓은 질문일 수 있습니다.
예시가 부족할 수 있습니다.
원래 source 설명이 약했을 수도 있습니다.

관련 글:

- [Active recall 공부법](/ko_Study/active-recall-study-method/)
- [Python 가상환경이 활성화되지 않을 때](/ko_Troubleshooting/python-venv-not-activating/)
- [복리 계산 예시](/ko_Economy/compound-interest-example/)

## 흔한 실수

- 모든 내용을 매일 복습합니다.
- 밑줄 친 문장을 그대로 card로 만듭니다.
- Recall 없이 다시 읽기만 합니다.
- 가치가 낮은 card를 너무 많이 유지합니다.
- 유지하기 어려울 정도로 엄격한 schedule을 씁니다.
- 실제 시험 성과가 좋아지는지 확인하지 않습니다.

## 함께 보면 좋은 글

- [Active Recall 공부법](/ko_Study/active-recall-study-method/)
- [오답노트 시스템 만드는 법](/ko_Study/exam-mistake-note-system/)
- [주간 공부 리뷰 루틴](/ko_Study/weekly-study-review/)

## 자주 묻는 질문

### 이 글은 언제 먼저 적용하면 좋나요?

시험 준비, 개발 공부, 언어 학습처럼 배운 내용을 실제로 꺼내 써야 하는 상황에서 가장 효과적입니다.

### 초보자가 가장 먼저 확인할 부분은 무엇인가요?

처음에는 공부 시간을 늘리기보다 오늘 설명할 수 있는 내용, 풀 수 있는 문제, 다시 틀린 부분을 기록하세요.

### 더 찾아볼 때 어떤 키워드를 쓰면 좋나요?

추가 검색할 때는 "Spaced repetition 복습 일정: 실제로 유지할 수 있는 반복 학습 계획" 같은 핵심 문구와 active recall, spaced repetition, study plan, mistake note 같은 학습 키워드를 붙이면 좋습니다.

## 참고 자료

- Dunlosky et al., *Improving Students' Learning With Effective Learning Techniques*: https://pubmed.ncbi.nlm.nih.gov/26173288/
- Roediger and Karpicke, *Test-enhanced learning*: https://pubmed.ncbi.nlm.nih.gov/16507066/
- Carnegie Mellon Eberly Center, Retrieval Practice: https://www.cmu.edu/teaching/resources/instructionalstrategies/activelearningstrategies/retrievalpractice/index.html
