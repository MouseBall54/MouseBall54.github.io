---
title: "Global Affairs"
layout: archive
permalink: /ko_global_affairs/
lang: ko
seo_description: >
  세계 성장, 무역 분절화, 에너지 안보, 핵심광물, 방위비, 기후 리스크, 이민, 한국 수출 노출도를 공식 자료 기반으로 읽는 한국어 세계정세 브리핑 모음입니다.
sidebar:
    nav: "sidebar-category"
---

Global Affairs 카테고리는 세계정세를 헤드라인 중심이 아니라 **성장, 에너지, 무역, 금융, 사회안정, 한국 연결 경로**로 나누어 읽기 위한 브리핑 모음입니다.

각 글은 IMF, World Bank, WTO, OECD, IEA, SIPRI, UNHCR, WMO, UNEP, FAO, BIS, UNCTAD, KDI, MOTIR 같은 공식 자료를 우선 참고합니다. 목적은 단기 전망을 맞히는 것이 아니라, 다음 뉴스를 볼 때 어떤 지표와 경로를 먼저 확인해야 하는지 정리하는 것입니다.

처음 읽는다면 세계 성장과 무역 분절화로 큰 지도를 잡고, 그다음 에너지·핵심광물·반도체 글로 한국 경제와의 연결을 확인하는 순서가 좋습니다. 생활비 관점이 필요하다면 식량안보와 가계비용 글을 함께 읽어 보세요.

## 먼저 읽기

- [2026년 세계 성장 둔화와 분절화](/ko_global_affairs/global-growth-fragmentation-2026/)
- [관세와 무역 분절화 리스크](/ko_global_affairs/trade-fragmentation-tariff-risk/)
- [한국 수출과 세계 분절화](/ko_global_affairs/korea-export-exposure-global-fragmentation/)

## 최신 글

{% assign posts = site.categories["ko_Global_Affairs"] %}
{% for post in posts %}
  {% include archive-single.html type=page.entries_layout %}
{% endfor %}
