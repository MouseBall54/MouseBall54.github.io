---
typora-root-url: ../
layout: single
title: >
  RAG 답변 품질 평가 체크리스트: Retrieval과 Answer를 따로 봐야 합니다
seo_title: >
  RAG 답변 품질 평가 체크리스트
date: 2026-05-23T23:59:56+09:00
last_modified_at: 2026-05-23T23:59:59+09:00
lang: ko
translation_id: rag-evaluation-checklist
header:
   teaser: /images/2026-05-23-rag-evaluation-checklist/rag-evaluation-hero.png
   overlay_image: /images/2026-05-23-rag-evaluation-checklist/rag-evaluation-hero.png
   overlay_filter: 0.35
excerpt: >
  RAG 시스템은 retrieval coverage, source relevance, grounded answer, citation accuracy, refusal behavior, failure pattern을 나누어 평가해야 합니다.
seo_description: >
  RAG 시스템은 retrieval coverage, source relevance, grounded answer, citation accuracy, refusal behavior, failure pattern을 나누어 평가해야 합니다.
categories:
  - ko_AI_Trends
tags:
  - AI
  - RAG
  - Evaluation
  - OpenAI
  - Workflow
---

## 핵심 요약

RAG 시스템은 retrieval quality와 answer quality를 따로 평가해야 합니다.
Retrieval이 실패하면 모델은 올바른 근거를 보지 못합니다.
Answer quality가 실패하면 올바른 근거를 봤는데도 지원되지 않는 답을 만들 수 있습니다.

![Retrieval check, answer check, citation, failure analysis로 이어지는 RAG evaluation workflow](/images/2026-05-23-rag-evaluation-checklist/rag-evaluation-hero.png)

이미지는 RAG evaluation의 실무 흐름을 보여줍니다.
문서, 검색 결과, 답변 생성, citation check, failure analysis가 이어집니다.
목표는 점수 하나를 높이는 것이 아니라 pipeline의 어느 부분이 깨졌는지 아는 것입니다.

## 핵심 체크리스트

RAG test set마다 아래를 확인합니다.

```text
[ ] 답이 들어 있는 source를 retrieval했는가?
[ ] Top result가 질문과 관련 있는가?
[ ] 답변이 retrieved source에 grounded되어 있는가?
[ ] Citation이 실제 claim을 뒷받침하는가?
[ ] Source에 답이 없을 때 거절하는가?
[ ] 근거 없는 사실을 만들지 않는가?
[ ] Failure를 root cause별로 묶었는가?
```

최종 답변만 평가하면 안 됩니다.
그렇게 하면 retrieval 문제가 숨습니다.

## 평가를 나누기

열을 분리합니다.

| Layer | 질문 | Example metric |
| --- | --- | --- |
| Retrieval | 올바른 문서를 가져왔는가? | recall@k, hit rate |
| Ranking | 좋은 chunk가 위에 있는가? | relevance score |
| Grounding | 답이 source에 의해 뒷받침되는가? | faithfulness |
| Citation | Citation이 맞는가? | citation precision |
| Helpfulness | 사용자 질문에 답하는가? | human rating |
| Safety | 근거 없는 요청을 거절하는가? | refusal accuracy |

이 분리는 중요합니다.
Prompt 개선으로 없는 문서를 가져올 수는 없습니다.
Embedding 개선으로 근거를 무시하는 답변을 고칠 수도 없습니다.

## 작은 Gold Test Set 만들기

처음에는 30-100개 질문이면 충분합니다.
각 항목에는 아래를 둡니다.

```text
question
expected source document
expected answer summary
must-cite facts
should-refuse flag
notes
```

정상 질문과 edge case를 함께 넣습니다.

좋은 test case:

- 답이 한 문서에 있음
- 답이 두 문서 조합에 있음
- corpus에 답이 없음
- source document끼리 충돌함
- 질문이 오래된 표현을 사용함
- 비슷한 문서가 retrieval을 헷갈리게 함

작고 잘 라벨링된 test set이 라벨 없는 대량 예시보다 유용합니다.

## 흔한 Failure Type

실패를 유형별로 기록합니다.

| Failure | 의미 | Fix direction |
| --- | --- | --- |
| Missing retrieval | 올바른 문서가 반환되지 않음 | chunking, embeddings, query rewrite |
| Poor ranking | 문서는 있지만 너무 아래 있음 | reranking, metadata filters |
| Bad grounding | 답이 source를 왜곡하거나 무시함 | prompt, context formatting |
| Bad citation | citation이 claim을 뒷받침하지 않음 | citation instructions, post-check |
| Over-answering | 근거 없이 답함 | refusal rule, source-only instruction |
| Under-answering | 충분한 근거가 있는데 거절함 | prompt와 evaluation example |

이렇게 하면 evaluation이 engineering loop가 됩니다.

## Manual Review Template

Output review에 아래 template을 씁니다.

```text
Question:
Retrieved sources:
Expected source present: yes/no
Answer supported by source: yes/no/partial
Citation correct: yes/no/partial
Missing fact:
Unsupported claim:
Failure type:
Fix idea:
```

반복해서 사용할 수 있을 만큼 짧게 유지합니다.

## 관련 글

- [AI agent workflow 2026](/ko_AI_Trends/ai-agent-workflow-2026/)
- [AI tool calling과 function calling 차이](/ko_AI_Trends/ai-tools-function-calling/)
- [OpenAI Responses API 사용 흐름](/ko_AI_Trends/openai-responses-api-guide/)

## 자주 묻는 질문

### 이 글은 언제 먼저 적용하면 좋나요?

새 도구를 바로 도입하기 전, 반복 업무와 검증 기준이 이미 있는지 확인할 때 먼저 적용하면 좋습니다.

### 초보자가 가장 먼저 확인할 부분은 무엇인가요?

처음에는 모델 성능보다 입력 데이터, 검증 기준, 실패 시 복구 방법을 먼저 정하세요. AI workflow는 자동화보다 검증 설계가 먼저입니다.

### 더 찾아볼 때 어떤 키워드를 쓰면 좋나요?

추가 검색할 때는 "RAG 답변 품질 평가 체크리스트: Retrieval과 Answer를 따로 봐야 합니다" 같은 핵심 문구와 evaluation, workflow, guardrail, structured output, agent 같은 실무 키워드를 조합해 보세요.

## 참고 자료

- OpenAI Evals guide: https://platform.openai.com/docs/guides/evals
- OpenAI tools guide: https://developers.openai.com/api/docs/guides/tools
- RAGAS paper: https://arxiv.org/abs/2309.15217
