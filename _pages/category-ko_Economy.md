---
title: "Economy"
layout: archive
permalink: /ko_economy/
lang: ko
seo_description: >
  금리, 물가, 환율, GDP, 고용, 가계부채, 예산, 비상금, ETF와 펀드 차이처럼 경제 뉴스와 생활비 판단을 연결하는 교육용 경제 가이드입니다.
sidebar:
    nav: "sidebar-category"
---

Economy 카테고리는 투자 추천이 아니라 경제지표와 생활비 판단을 연결하는 교육용 글을 모읍니다. 금리, 물가, 환율, GDP, 고용, 가계부채, 예산, 비상금, 수출입, 유가, 반도체 경기처럼 검색 수요가 꾸준하고 실생활 판단에 영향을 주는 주제를 다룹니다.

각 글은 IMF, World Bank, OECD, Federal Reserve, BEA, BLS, FRED, Bank of Korea, KOSIS, CFPB, SEC, FDIC 등 공식 또는 제도권 자료를 참고합니다. 모든 글은 개인별 투자 조언이나 재무 조언이 아니라 숫자를 읽고 가정을 점검하기 위한 자료입니다.

처음에는 예산, 비상금, 금리와 물가, 환율, 경기 침체 지표 글을 읽고, 그다음 GDP, 고용, 유가, 가계부채, 수익률 곡선 글로 확장하면 좋습니다.

## 먼저 읽기

- [50/30/20 예산법](/ko_economy/household-budget-50-30-20/)
- [비상금은 얼마가 적당할까](/ko_economy/emergency-fund-how-much/)
- [금리와 물가 기초](/ko_economy/interest-rate-inflation-basics/)
- [환율 기초](/ko_economy/exchange-rate-basics/)
- [경기 침체 지표 읽기](/ko_economy/recession-indicators-basics/)

## 최신 글

{% assign posts = site.categories["ko_Economy"] %}
{% for post in posts %}
  {% include archive-single.html type=page.entries_layout %}
{% endfor %}
