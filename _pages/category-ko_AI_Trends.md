---
title: "AI Trends"
layout: archive
permalink: /ko_AI_Trends/
lang: ko
seo_description: >
  AI agent, prompt engineering, RAG, OpenAI API, AI search처럼 실무자가 자주 찾는 AI 동향과 워크플로우를 정리한 글 모음입니다.
sidebar:
    nav: "sidebar-category"
---

AI Trends 카테고리는 AI 도구를 실제 업무와 개발 흐름에 적용할 때 필요한 판단 기준을 모읍니다. 단순한 뉴스보다 검증, 자동화 범위, 비용, 품질 관리, 검색 최적화처럼 바로 적용할 수 있는 주제를 우선합니다.

처음 방문했다면 agent workflow, prompt engineering, RAG 평가, AI 검색 최적화 순서로 읽으면 좋습니다.

각 글은 개념 설명에서 끝나지 않고 실무 적용 기준, 실패를 줄이는 검증 방법, 함께 읽을 다음 글을 포함합니다. AI 도구를 팀 업무에 붙이기 전에 작은 실험 범위를 정할 때 활용하기 좋습니다.

## 먼저 읽기

- [AI agent workflow 2026](/ko_AI_Trends/ai-agent-workflow-2026/)
- [Prompt engineering 체크리스트](/ko_AI_Trends/prompt-engineering-checklist/)
- [RAG 평가 체크리스트](/ko_AI_Trends/rag-evaluation-checklist/)

## 최신 글

{% assign posts = site.categories.ko_AI_Trends %}
{% for post in posts %}
  {% include archive-single.html type=page.entries_layout %}
{% endfor %}
