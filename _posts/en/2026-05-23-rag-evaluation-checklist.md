---
typora-root-url: ../
layout: single
title: >
  RAG Evaluation Checklist: How to Measure Retrieval and Answer Quality
seo_title: >
  RAG Evaluation Checklist
date: 2026-05-23T23:59:56+09:00
lang: en
translation_id: rag-evaluation-checklist
header:
   teaser: /images/2026-05-23-rag-evaluation-checklist/rag-evaluation-hero.png
   overlay_image: /images/2026-05-23-rag-evaluation-checklist/rag-evaluation-hero.png
   overlay_filter: 0.35
excerpt: >
  Evaluate RAG systems by checking retrieval coverage, source relevance, grounded answers, citation accuracy, refusal behavior, and failure patterns.
seo_description: >
  Evaluate RAG systems by checking retrieval coverage, source relevance, grounded answers, citation accuracy, refusal behavior, and failure patterns.
categories:
  - en_AI_Trends
tags:
  - AI
  - RAG
  - Evaluation
  - OpenAI
  - Workflow
---

## Quick Answer

A RAG system should be evaluated in two layers: retrieval quality and answer quality.
If retrieval fails, the model may never see the right evidence.
If answer quality fails, the model may have the right evidence but still produce an unsupported or incomplete answer.

![RAG evaluation workflow with retrieval checks, answer checks, citations, and failure analysis](/images/2026-05-23-rag-evaluation-checklist/rag-evaluation-hero.png)

The image shows a practical RAG evaluation flow: documents, search results, answer generation, citation checks, and failure analysis.
The goal is not only to get a high score.
The goal is to know which part of the pipeline broke.

## The Core Checklist

Use this checklist for every RAG test set:

```text
[ ] Does retrieval return the source that contains the answer?
[ ] Are the top results relevant to the question?
[ ] Is the answer grounded in retrieved sources?
[ ] Are citations attached to the exact claims they support?
[ ] Does the system refuse when sources do not contain the answer?
[ ] Does the answer avoid unsupported facts?
[ ] Are failures grouped by root cause?
```

Do not evaluate only the final answer.
That hides retrieval problems.

## Split the Evaluation

Use separate columns:

| Layer | Question | Example metric |
| --- | --- | --- |
| Retrieval | Did we fetch the right documents? | recall@k, hit rate |
| Ranking | Are the best chunks near the top? | relevance score |
| Grounding | Is the answer supported by sources? | faithfulness |
| Citation | Are cited sources correct? | citation precision |
| Helpfulness | Does it answer the user? | human rating |
| Safety | Does it refuse unsupported requests? | refusal accuracy |

This split matters.
Improving the prompt cannot fix a missing document.
Improving embeddings cannot fix an answer that ignores evidence.

## Build a Small Gold Test Set

Start with 30-100 questions.
Each item should include:

```text
question
expected source document
expected answer summary
must-cite facts
should-refuse flag
notes
```

Include normal questions and edge cases.

Good test cases:

- answer is in one document
- answer needs two documents
- answer is not in the corpus
- source documents disagree
- question contains outdated wording
- similar documents can confuse retrieval

Small, well-labeled test sets are more useful than thousands of unlabeled examples.

## Common Failure Types

Track failures by type:

| Failure | Meaning | Fix direction |
| --- | --- | --- |
| Missing retrieval | The right document was not returned | chunking, embeddings, query rewrite |
| Poor ranking | Right document exists but is too low | reranking, metadata filters |
| Bad grounding | Answer ignores or distorts source | prompt, context formatting |
| Bad citation | Citation does not support the claim | citation instructions, post-check |
| Over-answering | Model answers without evidence | refusal rule, source-only instruction |
| Under-answering | Model refuses despite sufficient evidence | prompt and evaluation examples |

This turns evaluation into an engineering loop.

## Manual Review Template

Use this when reviewing outputs:

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

Keep the template short enough that you can apply it repeatedly.

## Related Posts

- [AI Agent Workflow 2026](/en_AI_Trends/ai-agent-workflow-2026/)
- [AI Tool Calling vs Function Calling](/en_AI_Trends/ai-tools-function-calling/)
- [OpenAI Responses API Practical Guide](/en_AI_Trends/openai-responses-api-guide/)

## FAQ

### When should I use this guide?

Use it before adopting a new AI workflow, especially when the task is repeated often and the output can be reviewed against a clear standard.

### What should beginners verify first?

Start with the input data, evaluation rule, failure mode, and human review path. A useful AI workflow needs verification before scale.

### Which keywords should I search next?

Search for "RAG Evaluation Checklist: How to Measure Retrieval and Answer Quality" together with evaluation, workflow, guardrail, structured output, and agent design keywords.

## Sources

- OpenAI Evals guide: https://platform.openai.com/docs/guides/evals
- OpenAI tools guide: https://developers.openai.com/api/docs/guides/tools
- RAGAS paper: https://arxiv.org/abs/2309.15217
