---
title: "Health Literacy"
layout: archive
permalink: /ko_health_literacy/
lang: ko
seo_description: >
  수면, 운동, 식단, 혈압, 당뇨병 전단계, 호흡기 감염 예방, 약 안전, 통증 기록, 정신건강 신호, 응급 준비를 다루는 교육용 건강 리터러시 글 모음입니다.
sidebar:
    nav: "sidebar-category"
---

Health Literacy 카테고리는 건강 정보를 스스로 진단하는 도구가 아니라, 증상과 생활습관을 더 안전하게 기록하고 필요한 때 전문가에게 연결하기 위한 교육용 글을 모읍니다. 수면, 걷기, 식단, 수분, 혈압, 예방접종, 약 라벨, 통증, 스트레스, 응급 준비처럼 일상에서 자주 검색하는 주제를 다룹니다.

모든 글은 CDC, WHO, FDA, NIH MedlinePlus, NIMH, ODPHP 같은 공식 자료를 우선 참고합니다. 특정 치료를 지시하지 않으며, 심한 증상이나 안전 문제가 있으면 지역 응급번호나 의료기관에 즉시 문의해야 한다는 원칙을 반복합니다.

처음 읽는다면 수면 루틴, 걷기 운동, 건강한 식단 글로 생활기반을 잡고, 그다음 혈압 측정, 예방접종 기록, 진료 전 질문 목록 글로 건강 기록 체계를 만들어 보세요.

## 먼저 읽기

- [성인 수면 루틴 만들기](/ko_health_literacy/sleep-routine-adults/)
- [걷기 운동 시작법](/ko_health_literacy/walking-activity-start/)
- [진료 전 질문 목록 만들기](/ko_health_literacy/doctor-visit-question-list/)

## 최신 글

{% assign posts = site.categories["ko_Health_Literacy"] %}
{% for post in posts %}
  {% include archive-single.html type=page.entries_layout %}
{% endfor %}
