---
title: "Study"
layout: archive
permalink: /ko_Study/
lang: ko
seo_description: >
  Active recall, spaced repetition, 오답노트, 코딩 공부 로드맵처럼 검색 수요가 높은 학습법과 공부 시스템을 정리한 글 모음입니다.
sidebar:
    nav: "sidebar-category"
---

Study 카테고리는 공부 시간을 늘리는 방법보다 결과가 남는 학습 시스템을 다룹니다. 기억에서 꺼내 쓰기, 복습 간격, 오답 관리, 집중 시간 설계처럼 시험과 개발 공부에 모두 적용할 수 있는 주제를 모았습니다.

처음에는 active recall과 spaced repetition을 읽고, 이후 오답노트와 주간 리뷰로 공부 루프를 만들면 좋습니다.

각 글은 바로 따라 할 수 있는 템플릿이나 점검 기준을 포함합니다. 공부법을 많이 모으기보다 하나의 루틴을 정하고, 주간 리뷰로 실제 성과를 확인하는 방향을 권장합니다.

## 먼저 읽기

- [Active Recall 공부법](/ko_Study/active-recall-study-method/)
- [Spaced Repetition 복습 일정 만들기](/ko_Study/spaced-repetition-schedule/)
- [오답노트 시스템 만드는 법](/ko_Study/exam-mistake-note-system/)

## 최신 글

{% assign posts = site.categories.ko_Study %}
{% for post in posts %}
  {% include archive-single.html type=page.entries_layout %}
{% endfor %}
