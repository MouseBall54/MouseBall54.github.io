---
title: "Climate & Energy"
layout: archive
permalink: /ko_climate_energy/
lang: ko
seo_description: >
  전력망, AI 데이터센터, 재생에너지, 배터리, 핵심광물, 탄소가격, 폭염, 홍수, 기후적응, 한국 산업 리스크를 공식 자료 기반으로 읽는 기후·에너지 글 모음입니다.
sidebar:
    nav: "sidebar-category"
---

Climate & Energy 카테고리는 기후와 에너지를 환경 구호가 아니라 **전력망, 산업 경쟁력, 생활비, 공급망, 재난 회복력**의 관점에서 읽기 위한 브리핑 모음입니다.

각 글은 IEA, IPCC, WMO, UNEP, UNFCCC, World Bank, OECD, EIA, 한국 에너지·기후 관련 공식 자료를 우선 참고합니다. 목표는 특정 정책이나 기술을 홍보하는 것이 아니라, 다음 뉴스가 나왔을 때 수요, 공급, 가격, 리스크, 국내 전달 경로를 차분히 나누어 보는 기준을 만드는 것입니다.

처음 읽는다면 AI 데이터센터 전력 수요, 전력망 병목, 재생에너지 전망으로 큰 지도를 잡고, 그다음 배터리·핵심광물·RE100·폭염·홍수 적응 글로 확장하는 순서가 좋습니다.

## 먼저 읽기

- [AI 데이터센터 전력 수요](/ko_climate_energy/ai-data-center-electricity-demand/)
- [에너지 전환의 병목은 전력망이다](/ko_climate_energy/power-grid-bottlenecks-transition/)
- [기후·에너지 정책 뉴스 읽는 시스템](/ko_climate_energy/climate-policy-news-reading-system/)

## 최신 글

{% assign posts = site.categories["ko_Climate_Energy"] %}
{% for post in posts %}
  {% include archive-single.html type=page.entries_layout %}
{% endfor %}
