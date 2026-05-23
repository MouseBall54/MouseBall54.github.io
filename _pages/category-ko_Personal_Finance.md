---
title: "Personal Finance"
layout: archive
permalink: /ko_personal_finance/
lang: ko
seo_description: >
  예산, 비상금, 부채 상환, 신용점수, 대출 총비용, 세금 준비, ETF, 자산배분, 은퇴저축, 투자 사기 예방을 다루는 교육용 개인재무 가이드입니다.
sidebar:
    nav: "sidebar-category"
---

Personal Finance 카테고리는 개인과 가정이 매달 반복해서 마주치는 돈 문제를 교육용 관점에서 정리합니다. 예산표, 비상금, 신용점수, 대출, 세금 준비, 투자 위험관리, 은퇴저축, 투자 사기 예방처럼 검색 수요가 꾸준하고 실제 판단에 바로 연결되는 주제를 다룹니다.

이 카테고리는 특정 상품 추천이나 개인별 투자 조언을 제공하지 않습니다. CFPB, SEC Investor.gov, FINRA, IRS, FTC, 서민금융진흥원 같은 공식 자료를 참고해 스스로 확인해야 할 숫자, 질문, 실행 순서를 제시합니다.

처음 읽는다면 월급날 예산 캘린더, 비상금 3단계, 부채 상환 방식부터 시작하세요. 투자 글은 위험감내도와 기간, 자산배분, 수수료 글을 먼저 읽은 뒤 개별 상품을 보는 순서가 안전합니다.

## 먼저 읽기

- [월급날 예산 캘린더 만들기](/ko_personal_finance/paycheck-budget-calendar/)
- [비상금 3단계 설계](/ko_personal_finance/emergency-fund-tiers/)
- [투자 위험감내도와 기간](/ko_personal_finance/risk-tolerance-time-horizon/)

## 최신 글

{% assign posts = site.categories["ko_Personal_Finance"] %}
{% for post in posts %}
  {% include archive-single.html type=page.entries_layout %}
{% endfor %}
