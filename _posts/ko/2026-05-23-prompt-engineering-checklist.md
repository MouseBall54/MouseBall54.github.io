---
typora-root-url: ../
layout: single
title: >
  Prompt engineering 체크리스트: 더 좋은 AI 프롬프트를 반복해서 쓰는 구조
seo_title: >
  Prompt engineering 체크리스트
date: 2026-05-23T23:59:10+09:00
lang: ko
translation_id: prompt-engineering-checklist
header:
   teaser: /images/2026-05-23-prompt-engineering-checklist/prompt-engineering-hero.png
   overlay_image: /images/2026-05-23-prompt-engineering-checklist/prompt-engineering-hero.png
   overlay_filter: 0.35
excerpt: >
  Prompt engineering은 긴 요청을 쓰는 일이 아니라 task, audience, context, constraints, examples, output format, verification을 명확히 하는 일입니다.
seo_description: >
  Prompt engineering은 긴 요청을 쓰는 일이 아니라 task, audience, context, constraints, examples, output format, verification을 명확히 하는 일입니다.
categories:
  - ko_AI_Trends
tags:
  - AI
  - PromptEngineering
  - OpenAI
  - Productivity
  - Workflow
---

## 핵심 요약

좋은 prompt는 단순히 긴 요청이 아닙니다.
작은 task specification에 가깝습니다.
Prompt를 보내기 전에 goal, audience, context, constraints, examples, output format, verification rule을 정해야 합니다.

![Task card, checklist, validated output으로 이어지는 prompt engineering workflow](/images/2026-05-23-prompt-engineering-checklist/prompt-engineering-hero.png)

이미지는 모호한 요청이 구조화된 card와 checklist를 거쳐 검증 가능한 output이 되는 흐름을 보여줍니다.
Prompt engineering의 핵심은 모델이 생성하기 전에 모호함을 줄이는 것입니다.

## 체크리스트

중요한 prompt를 쓰기 전에 아래를 확인합니다.

```text
[ ] Task: 모델이 정확히 무엇을 해야 하는가?
[ ] Audience: 누가 이 답을 읽거나 사용하는가?
[ ] Context: 어떤 사실, 파일, 제약, 예시가 중요한가?
[ ] Output: 어떤 형식으로 답해야 하는가?
[ ] Boundaries: 무엇을 피해야 하는가?
[ ] Reasoning target: 어떤 tradeoff를 고려해야 하는가?
[ ] Verification: 답이 쓸 만한지 어떻게 확인할 것인가?
```

이 항목을 채울 수 없다면 모델은 추측합니다.
Brainstorming에서는 괜찮을 수 있습니다.
하지만 production writing, coding, analysis, customer work에서는 추측이 비용이 됩니다.

## 나쁜 Prompt와 더 나은 Prompt

약한 prompt:

```text
ETF에 대해 써줘.
```

더 나은 prompt:

```text
ETF vs mutual fund를 초보자에게 설명하는 글을 작성해줘.
Audience: 기본 저축은 알지만 투자 상품은 잘 모르는 사람.
Cover: 거래 시간, 수수료, 세금, 최소 투자금, 흔한 실수.
Tone: 교육용이며 투자 조언처럼 쓰지 말 것.
Output: H2 sections, comparison table 1개, 짧은 checklist.
Avoid: 특정 fund 추천, 수익률 보장 표현.
```

두 번째 prompt는 audience, scope, risk boundary를 모델이 추측하지 않게 합니다.

## 1. Task 정의하기

동사로 시작합니다.

좋은 task 동사:

- explain
- compare
- summarize
- rewrite
- extract
- classify
- generate
- critique
- validate

약한 task:

```text
이것 좀 도와줘.
```

더 나은 task:

```text
이 GitHub Actions log에서 error message, likely cause, safe fix, verification command를 추출해줘.
```

목표를 말하지 않으면 모델은 목표에 맞게 최적화할 수 없습니다.

## 2. Audience 적기

Audience가 바뀌면 답도 바뀝니다.
초보자, senior engineer, 학생, 부모, 투자자, product manager는 필요한 설명 수준이 다릅니다.

예시:

```text
Audience: 컴퓨터공학 1학년 학생.
Audience: REST에서 event-driven system으로 넘어가는 backend engineer.
Audience: 처음으로 월간 예산을 만드는 사람.
```

"쉽게 써줘"만 쓰지 않습니다.
누구에게 쉬워야 하는지 정해야 합니다.

## 3. Context 제공하기

Context는 관련 있고 경계가 있어야 합니다.
모델이 반드시 사용해야 할 사실을 주되, 관련 없는 메모를 한꺼번에 던지지 않습니다.

유용한 context:

- target platform
- version
- existing code
- exact error message
- source links
- current draft
- business rule
- reader knowledge level

Technical prompt에는 version과 command를 넣습니다.
금융 또는 정책성 글에는 source date와 개인 조언을 피해야 한다는 조건을 넣습니다.

## 4. Output Format 지정하기

특정 형식이 필요하면 명시합니다.

예시:

```text
Cause, Symptom, Fix, Verification 열을 가진 Markdown table로 반환해줘.
title, slug, primary_keyword, outline을 가진 JSON으로 반환해줘.
각 단계가 한 문장인 7-step checklist로 작성해줘.
```

Output format은 다른 사람이나 프로그램이 답을 사용할 때 중요합니다.
CMS, spreadsheet, code review, support tool로 들어가는 답이라면 구조가 시간을 줄여줍니다.

## 5. Boundaries 설정하기

Boundary는 그럴듯하지만 쓸 수 없는 답을 줄입니다.

예시:

```text
특정 투자 상품을 추천하지 마세요.
명령어 실행 결과를 지어내지 마세요.
관련 없는 파일을 수정하지 마세요.
유료 도구가 필요한 예시는 쓰지 마세요.
아래 source에 없는 내용은 citation하지 마세요.
```

Negative instruction이 완벽한 안전장치는 아닙니다.
하지만 명확한 boundary는 답을 검토하기 쉽게 만들고 결과 품질을 높입니다.

## 6. 예시 추가하기

Output style이 중요할 때는 예시가 강력합니다.

예시:

```text
이 style을 사용해줘:
Problem: 한 문장
Cause: 한 문장
Fix: command block
Verify: command block
```

좋은 예시 하나가 추상적인 설명 다섯 문단보다 나을 수 있습니다.
원하는 결과와 충돌하는 예시는 넣지 않습니다.

## 7. Verification Rule 넣기

가장 좋은 prompt에는 답을 확인하는 기준이 있습니다.

예시:

```text
모든 command에 verification step이 있어야 acceptable하다.
글은 official source를 최소 2개 포함해야 acceptable하다.
JSON은 required field가 모두 비어 있지 않아야 acceptable하다.
Code는 public API behavior를 바꾸지 않아야 acceptable하다.
```

Verification은 prompt를 단순 요청이 아니라 workflow로 바꿉니다.

## 재사용 Template

아래를 복사해 사용할 수 있습니다.

```text
Task:
Audience:
Context:
Input:
Output format:
Constraints:
Examples:
Verification:
```

Blog post 예시:

```text
Task: spaced repetition에 대한 실용 글을 작성한다.
Audience: 유지 가능한 schedule을 원하는 바쁜 학생.
Context: spacing과 active recall을 함께 설명한다.
Output format: H2 heading, schedule table 1개, template 1개.
Constraints: 기억 효과를 과장하지 않는다.
Verification: source와 weekly cleanup routine을 포함한다.
```

## 흔한 실수

- 목표를 정의하지 않고 "best"를 요청합니다.
- 하나의 prompt에 세 가지 일을 섞습니다.
- 중요한 constraint를 맨 끝에 숨깁니다.
- Citation을 요청하면서 source rule을 정하지 않습니다.
- JSON을 요청하고 invalid field를 그대로 받습니다.
- 첫 답을 최종 답으로 취급합니다.
- code, retrieval, tool로 해결해야 할 문제를 prompt만으로 해결하려 합니다.

## AI Workflow와 함께 쓰기

Prompt engineering은 한 층입니다.
중요한 workflow에서는 아래와 함께 써야 합니다.

- structured output
- tool calling
- evaluation
- human review
- logging
- versioned instructions

관련 글:

- [OpenAI Responses API 사용 흐름](/ko_AI_Trends/openai-responses-api-guide/)
- [AI agent workflow 2026](/ko_AI_Trends/ai-agent-workflow-2026/)
- [Spaced repetition 복습 일정](/ko_Study/spaced-repetition-schedule/)

## 참고 자료

- OpenAI Prompt engineering guide: https://developers.openai.com/api/docs/guides/prompt-engineering
- OpenAI Prompt guidance: https://developers.openai.com/api/docs/guides/prompting
- OpenAI Structured outputs guide: https://platform.openai.com/docs/guides/structured-outputs
