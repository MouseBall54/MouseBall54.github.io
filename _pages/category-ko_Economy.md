---
title: "Economy"
layout: archive
permalink: /ko_Economy/
lang: ko
seo_description: >
  복리, 비상금, 예산법, 금리, 물가, 환율, ETF와 펀드 차이처럼 개인 재무 기초와 경제 흐름을 쉽게 정리한 교육용 경제 가이드 글 모음입니다.
sidebar:
    nav: "sidebar-category"
---

Economy 카테고리는 투자 추천이 아니라 개인 재무와 경제 기초를 이해하기 위한 교육용 글을 모읍니다. 예산, 비상금, 복리, 금리와 물가, 환율처럼 검색 수요가 꾸준하고 생활 판단에 자주 쓰이는 주제를 다룹니다.

처음에는 예산과 비상금으로 기준을 잡고, 그다음 복리, 금리, 환율 글로 숫자를 해석하는 힘을 키우면 좋습니다.

경제 글은 모두 교육용이며 개인별 투자 판단을 대신하지 않습니다. 숫자를 볼 때는 소득, 기간, 위험 감내도, 수수료, 세금 같은 조건을 함께 적어 두고 비교하는 방식으로 읽는 것이 좋습니다.

## 먼저 읽기

- [50/30/20 예산법 쓰는 법](/ko_Economy/household-budget-50-30-20/)
- [비상금은 얼마가 적당할까](/ko_Economy/emergency-fund-how-much/)
- [복리 계산 예시](/ko_Economy/compound-interest-example/)

## 최신 글

{% assign posts = site.categories["ko_Economy"] %}
{% for post in posts %}
  {% include archive-single.html type=page.entries_layout %}
{% endfor %}
