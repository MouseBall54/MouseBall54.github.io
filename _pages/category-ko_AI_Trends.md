---
title: "AI Trends"
layout: archive
permalink: /ko_ai_trends/
lang: ko
seo_description: >
  AI agent, prompt engineering, RAG, OpenAI API, structured outputs, AI security, EU AI Act, NIST AI RMF처럼 실무자가 자주 찾는 AI 동향과 워크플로우를 공식 자료 기반으로 정리한 글 모음입니다.
sidebar:
    nav: "sidebar-category"
---

AI Trends 카테고리는 AI 도구를 실제 업무와 개발 흐름에 적용할 때 필요한 판단 기준을 모읍니다. 단순한 뉴스보다 검증, 자동화 범위, 비용, 보안, 데이터 거버넌스, 검색 최적화처럼 바로 적용할 수 있는 주제를 우선합니다.

각 글은 OpenAI 공식 문서, NIST AI RMF, OWASP LLM 보안 자료, OECD AI Principles, EU AI Act 관련 공식 자료, Stanford AI Index처럼 확인 가능한 출처를 참고합니다. 목적은 특정 모델을 홍보하는 것이 아니라 AI를 도입하기 전 질문, 검증 방식, 운영 책임을 명확히 하는 것입니다.

처음 방문했다면 agent workflow, prompt engineering, RAG 평가, structured outputs, LLM 보안 글부터 읽으면 좋습니다.

## 먼저 읽기

- [AI Agent Workflow 2026](/ko_ai_trends/ai-agent-workflow-2026/)
- [Prompt Engineering 체크리스트](/ko_ai_trends/prompt-engineering-checklist/)
- [RAG 평가 체크리스트](/ko_ai_trends/rag-evaluation-checklist/)
- [Structured Outputs와 JSON Schema](/ko_ai_trends/structured-outputs-json-schema/)
- [LLM Prompt Injection 대응](/ko_ai_trends/llm-security-prompt-injection/)

## 최신 글

{% assign posts = site.categories["ko_AI_Trends"] %}
{% for post in posts %}
  {% include archive-single.html type=page.entries_layout %}
{% endfor %}
