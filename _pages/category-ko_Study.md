---
title: "Study"
layout: archive
permalink: /ko_study/
lang: ko
seo_description: >
  Active recall, spaced repetition, 오답노트, 집중 루틴, 코딩 공부, 영어 단어, 노트 정리, 시험 전략처럼 근거 있는 학습 시스템을 정리한 글 모음입니다.
sidebar:
    nav: "sidebar-category"
---

Study 카테고리는 공부 시간을 늘리는 방법보다 결과가 남는 학습 시스템을 다룹니다. 기억에서 꺼내 쓰기, 복습 간격, 오답 관리, 집중 시간 설계, 필기와 독해, 코딩 연습, 언어 학습처럼 시험과 실무 공부에 모두 적용할 수 있는 주제를 모았습니다.

각 글은 IES, EEF, CDC, NIH MedlinePlus, Purdue OWL, Cornell Learning Strategies Center, Python.org, MDN, Pro Git 같은 교육·기관 자료를 참고합니다. 목표는 공부법을 많이 모으는 것이 아니라 한 번의 세션에서 회상, 피드백, 다음 복습이 남는 루틴을 만드는 것입니다.

처음에는 active recall과 spaced repetition을 읽고, 이후 오답노트, 질문은행, 주간 리뷰, 수면과 집중 루틴으로 공부 루프를 넓히면 좋습니다.

## 먼저 읽기

- [Active Recall 공부법](/ko_study/active-recall-study-method/)
- [Spaced Repetition 복습 일정](/ko_study/spaced-repetition-schedule/)
- [오답노트 시스템](/ko_study/exam-mistake-note-system/)
- [질문은행 만들기](/ko_study/question-bank-system/)
- [수면과 공부 성과](/ko_study/sleep-study-performance/)

## 최신 글

{% assign posts = site.categories["ko_Study"] %}
{% for post in posts %}
  {% include archive-single.html type=page.entries_layout %}
{% endfor %}
