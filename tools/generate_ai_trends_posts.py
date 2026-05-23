#!/usr/bin/env python3
"""Generate paired AI Trends posts and local PNG context images."""

from __future__ import annotations

import html
import struct
import zlib
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parents[1]
POST_DATE = "2026-05-23"
LAST_MODIFIED_AT = "2026-05-23T23:30:00+09:00"
KO_CATEGORY = "ko_AI_Trends"
EN_CATEGORY = "en_AI_Trends"


SOURCES = {
    "openai_agents": {
        "ko": "OpenAI Agents Guide",
        "en": "OpenAI Agents Guide",
        "url": "https://platform.openai.com/docs/guides/agents",
    },
    "openai_responses": {
        "ko": "OpenAI Responses API Reference",
        "en": "OpenAI Responses API Reference",
        "url": "https://platform.openai.com/docs/api-reference/responses?api-mode=responses",
    },
    "openai_tools": {
        "ko": "OpenAI Tools Guide",
        "en": "OpenAI Tools Guide",
        "url": "https://platform.openai.com/docs/guides/tools",
    },
    "openai_function_calling": {
        "ko": "OpenAI Function Calling Help",
        "en": "OpenAI Function Calling Help",
        "url": "https://help.openai.com/en/articles/8555517-function-calling-in-the-openai-api",
    },
    "openai_structured_outputs": {
        "ko": "OpenAI Structured Outputs Guide",
        "en": "OpenAI Structured Outputs Guide",
        "url": "https://platform.openai.com/docs/guides/structured-outputs",
    },
    "openai_retrieval": {
        "ko": "OpenAI Retrieval Guide",
        "en": "OpenAI Retrieval Guide",
        "url": "https://platform.openai.com/docs/guides/retrieval",
    },
    "openai_evals": {
        "ko": "OpenAI Evals API Reference",
        "en": "OpenAI Evals API Reference",
        "url": "https://platform.openai.com/docs/api-reference/evals",
    },
    "openai_prompting": {
        "ko": "OpenAI Prompt Engineering Best Practices",
        "en": "OpenAI Prompt Engineering Best Practices",
        "url": "https://help.openai.com/en/articles/6654000-playground-and-prompt-engineering",
    },
    "openai_computer_env": {
        "ko": "OpenAI Responses API Computer Environment",
        "en": "OpenAI Responses API Computer Environment",
        "url": "https://openai.com/index/equip-responses-api-computer-environment/",
    },
    "nist_ai_rmf": {
        "ko": "NIST AI Risk Management Framework",
        "en": "NIST AI Risk Management Framework",
        "url": "https://www.nist.gov/itl/ai-risk-management-framework",
    },
    "nist_gai_profile": {
        "ko": "NIST Generative AI Profile",
        "en": "NIST Generative AI Profile",
        "url": "https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf",
    },
    "owasp_llm": {
        "ko": "OWASP Top 10 for LLM Applications",
        "en": "OWASP Top 10 for LLM Applications",
        "url": "https://owasp.org/www-project-top-10-for-large-language-model-applications/",
    },
    "oecd_ai": {
        "ko": "OECD Artificial Intelligence",
        "en": "OECD Artificial Intelligence",
        "url": "https://www.oecd.org/en/topics/policy-issues/artificial-intelligence.html",
    },
    "oecd_principles": {
        "ko": "OECD AI Principles",
        "en": "OECD AI Principles",
        "url": "https://www.oecd.org/en/topics/ai-principles.html",
    },
    "eu_ai": {
        "ko": "European Commission Artificial Intelligence",
        "en": "European Commission Artificial Intelligence",
        "url": "https://commission.europa.eu/topics/digital-economy-and-society/artificial-intelligence_en",
    },
    "eu_gpai": {
        "ko": "European Commission GPAI Q&A",
        "en": "European Commission GPAI Q&A",
        "url": "https://digital-strategy.ec.europa.eu/en/faqs/general-purpose-ai-models-ai-act-questions-answers",
    },
    "stanford_ai_index": {
        "ko": "Stanford HAI AI Index",
        "en": "Stanford HAI AI Index",
        "url": "https://hai.stanford.edu/ai-index",
    },
}


TOPICS = [
    {
        "slug": "ai-agent-workflow-2026",
        "ko_title": "AI Agent Workflow 2026: 자동화보다 검증 게이트 먼저 설계하기",
        "en_title": "AI Agent Workflow 2026: Design Verification Before Automation",
        "ko_summary": "AI 에이전트는 긴 프롬프트가 아니라 목표, 도구, 상태, 검증, 중단 규칙이 연결된 업무 시스템이다.",
        "en_summary": "An AI agent is not a longer prompt; it is a work system connecting goals, tools, state, verification, and stop rules.",
        "ko_focus": "에이전트 도입의 핵심은 모델이 무엇을 할 수 있는지보다 어떤 행동을 하기 전에 멈추고 검증할지 정하는 것입니다.",
        "en_focus": "The core agent question is not what the model can do, but where it must pause before taking action.",
        "ko_actions": ["반복되는 업무 하나를 고릅니다.", "도구 권한을 읽기, 초안, 실행으로 나눕니다.", "고위험 행동은 사람 승인 뒤에만 실행합니다."],
        "en_actions": ["Choose one recurring job.", "Separate tool permissions into read, draft, and execute.", "Put human approval before high-risk actions."],
        "signals": ["tool scope", "approval gate", "trace log", "rollback path"],
        "ko_signals": ["도구 범위", "승인 게이트", "실행 로그", "되돌리기 경로"],
        "sources": ["openai_agents", "openai_responses", "nist_ai_rmf"],
        "tags": ["AI Agents", "Automation", "Workflow", "Verification"],
    },
    {
        "slug": "prompt-engineering-checklist",
        "ko_title": "Prompt Engineering 체크리스트: 좋은 프롬프트보다 반복 가능한 입력 구조",
        "en_title": "Prompt Engineering Checklist: Build Repeatable Input Structure",
        "ko_summary": "프롬프트 품질은 멋진 문장보다 역할, 목적, 자료, 제약, 출력 형식이 항상 같은 순서로 들어갈 때 안정된다.",
        "en_summary": "Prompt quality improves when role, goal, context, constraints, and output format appear in a stable order.",
        "ko_focus": "좋은 프롬프트는 한번 맞히는 문장이 아니라 팀원이 같은 방식으로 재사용할 수 있는 작업 명세서에 가깝습니다.",
        "en_focus": "A strong prompt is closer to a reusable task brief than a clever one-off instruction.",
        "ko_actions": ["목표와 금지사항을 분리합니다.", "출력 형식을 예시로 고정합니다.", "검토 기준을 프롬프트 끝에 둡니다."],
        "en_actions": ["Separate goals from constraints.", "Fix the output shape with an example.", "Place review criteria at the end."],
        "signals": ["task goal", "context boundary", "output format", "review rule"],
        "ko_signals": ["작업 목표", "맥락 경계", "출력 형식", "검토 기준"],
        "sources": ["openai_prompting", "openai_structured_outputs", "nist_ai_rmf"],
        "tags": ["Prompt Engineering", "AI Workflow", "Productivity", "Quality Control"],
    },
    {
        "slug": "rag-evaluation-checklist",
        "ko_title": "RAG 평가 체크리스트: 검색이 맞았는지와 답변이 맞았는지를 나눠 보기",
        "en_title": "RAG Evaluation Checklist: Separate Retrieval Quality from Answer Quality",
        "ko_summary": "RAG 품질은 모델 답변만 보면 안 되고 검색 문서, 인용 위치, 누락 질문, 답변 충실도를 따로 측정해야 한다.",
        "en_summary": "RAG quality requires separate checks for retrieved documents, citation location, missing questions, and answer faithfulness.",
        "ko_focus": "RAG 실패는 답변 문장이 그럴듯해서 더 위험합니다. 검색 실패와 생성 실패를 분리해야 원인을 고칠 수 있습니다.",
        "en_focus": "RAG failures are dangerous because the answer can sound plausible. Separate retrieval failure from generation failure.",
        "ko_actions": ["질문별 정답 문서를 먼저 정합니다.", "검색 결과 상위 문서의 포함 여부를 봅니다.", "답변이 출처 밖 내용을 말하는지 표시합니다."],
        "en_actions": ["Define the expected source document for each question.", "Check whether top results include that source.", "Flag answer claims outside the retrieved evidence."],
        "signals": ["retrieval hit rate", "citation span", "unsupported claim", "missing source"],
        "ko_signals": ["검색 적중률", "인용 위치", "근거 없는 주장", "누락 문서"],
        "sources": ["openai_retrieval", "openai_evals", "nist_gai_profile"],
        "tags": ["RAG", "Evaluation", "Retrieval", "AI Quality"],
    },
    {
        "slug": "ai-search-optimization",
        "ko_title": "AI Search Optimization: 검색엔진보다 답변엔진이 읽기 쉬운 글 구조",
        "en_title": "AI Search Optimization: Structure Content for Answer Engines",
        "ko_summary": "AI 검색에 노출되려면 글이 질문, 짧은 답, 근거, 단계, 날짜, 출처를 명확히 드러내야 한다.",
        "en_summary": "AI search visibility improves when content exposes questions, short answers, evidence, steps, dates, and sources clearly.",
        "ko_focus": "AI 검색은 문서의 권위를 추론하려 하므로 제목 낚시보다 구체적인 질문과 검증 가능한 문장 구조가 중요합니다.",
        "en_focus": "AI search systems infer usefulness from structure, so concrete questions and verifiable statements matter more than headline tricks.",
        "ko_actions": ["첫 문단에 짧은 답을 둡니다.", "단계와 조건을 목록으로 분리합니다.", "출처와 업데이트 날짜를 보이게 둡니다."],
        "en_actions": ["Put a short answer near the top.", "Separate steps and conditions into lists.", "Expose sources and update dates."],
        "signals": ["question match", "answer block", "source clarity", "update date"],
        "ko_signals": ["질문 일치", "답변 블록", "출처 명확성", "업데이트 날짜"],
        "sources": ["openai_retrieval", "stanford_ai_index", "oecd_ai"],
        "tags": ["AI Search", "SEO", "Content Strategy", "Information Architecture"],
    },
    {
        "slug": "ai-automation-roi",
        "ko_title": "AI Automation ROI: 자동화 전에 시간, 오류, 검토 비용부터 계산하기",
        "en_title": "AI Automation ROI: Count Time, Errors, and Review Cost First",
        "ko_summary": "AI 자동화 ROI는 절약 시간만이 아니라 검토 시간, 오류 비용, 재작업, 보안 통제 비용까지 함께 계산해야 한다.",
        "en_summary": "AI automation ROI must include review time, error cost, rework, and security controls, not only saved hours.",
        "ko_focus": "자동화 효과는 모델 호출 비용보다 업무가 실제로 줄었는지, 사람 검토가 병목이 되지 않는지에서 결정됩니다.",
        "en_focus": "Automation value depends less on token cost and more on whether work actually disappears without moving the bottleneck to reviewers.",
        "ko_actions": ["현재 업무 시간을 표본으로 잽니다.", "검토와 수정 시간을 별도 항목으로 둡니다.", "오류 1건의 복구 비용을 추정합니다."],
        "en_actions": ["Sample the current task time.", "Track review and correction time separately.", "Estimate recovery cost per error."],
        "signals": ["baseline minutes", "review minutes", "error rate", "handoff delay"],
        "ko_signals": ["기준 시간", "검토 시간", "오류율", "인계 지연"],
        "sources": ["oecd_ai", "nist_ai_rmf", "stanford_ai_index"],
        "tags": ["AI ROI", "Automation", "Operations", "Productivity"],
    },
    {
        "slug": "ai-coding-agent-workflow",
        "ko_title": "AI Coding Agent Workflow: 코드 품질을 잃지 않는 에이전트 사용법",
        "en_title": "AI Coding Agent Workflow: Use Agents Without Losing Code Quality",
        "ko_summary": "코딩 에이전트는 작은 이슈, 명확한 테스트, 좁은 diff, 리뷰 가능한 커밋 단위가 있을 때 가장 안전하다.",
        "en_summary": "Coding agents are safest with small issues, clear tests, narrow diffs, and reviewable commit boundaries.",
        "ko_focus": "코딩 에이전트의 생산성은 많은 파일을 바꾸는 속도가 아니라 변경 의도와 검증 결과를 사람이 빨리 이해하는 데 있습니다.",
        "en_focus": "Coding-agent productivity is not the speed of changing many files; it is how quickly humans can understand intent and verification.",
        "ko_actions": ["작업을 하나의 실패 조건으로 정의합니다.", "수정 전후 테스트 명령을 고정합니다.", "리뷰 가능한 작은 커밋으로 나눕니다."],
        "en_actions": ["Define the task as one failing condition.", "Fix the before-and-after test command.", "Split work into reviewable commits."],
        "signals": ["diff size", "test coverage", "review path", "rollback commit"],
        "ko_signals": ["diff 크기", "테스트 범위", "리뷰 경로", "롤백 커밋"],
        "sources": ["openai_agents", "openai_tools", "nist_ai_rmf"],
        "tags": ["Coding Agents", "Software Engineering", "Code Review", "AI Workflow"],
    },
    {
        "slug": "ai-meeting-notes-workflow",
        "ko_title": "AI Meeting Notes Workflow: 회의록을 결정, 담당자, 기한으로 바꾸기",
        "en_title": "AI Meeting Notes Workflow: Turn Calls into Decisions, Owners, and Deadlines",
        "ko_summary": "AI 회의록은 요약보다 결정 사항, 담당자, 기한, 미해결 질문을 정확히 분리할 때 업무 가치가 커진다.",
        "en_summary": "AI meeting notes are valuable when they separate decisions, owners, deadlines, and unresolved questions, not when they only summarize.",
        "ko_focus": "회의록 자동화는 말의 양을 줄이는 작업이 아니라 다음 행동을 놓치지 않게 만드는 업무 기록 시스템입니다.",
        "en_focus": "Meeting-note automation is not compression; it is a record system that prevents next actions from disappearing.",
        "ko_actions": ["요약과 액션 아이템을 분리합니다.", "담당자와 기한이 없는 항목은 질문으로 남깁니다.", "민감한 발언은 공유 전 검토합니다."],
        "en_actions": ["Separate summary from action items.", "Leave ownerless or dateless items as questions.", "Review sensitive statements before sharing."],
        "signals": ["decision", "owner", "deadline", "open question"],
        "ko_signals": ["결정 사항", "담당자", "기한", "미해결 질문"],
        "sources": ["openai_structured_outputs", "nist_ai_rmf", "oecd_principles"],
        "tags": ["Meetings", "Productivity", "AI Notes", "Workflow"],
    },
    {
        "slug": "ai-tools-function-calling",
        "ko_title": "AI Tool Calling vs Function Calling: 모델 출력과 실제 실행을 분리하기",
        "en_title": "AI Tool Calling vs Function Calling: Separate Model Output from Execution",
        "ko_summary": "도구 호출은 모델이 외부 시스템과 연결되는 지점이므로 스키마, 권한, 검증, 실행 로그를 함께 설계해야 한다.",
        "en_summary": "Tool calling connects a model to external systems, so schema, permissions, validation, and logs must be designed together.",
        "ko_focus": "함수 호출은 편리하지만 모델의 제안과 실제 시스템 실행을 같은 것으로 취급하면 보안과 데이터 문제가 생깁니다.",
        "en_focus": "Function calling is useful, but treating a model suggestion as a real system action creates security and data risk.",
        "ko_actions": ["도구 입력 스키마를 좁게 정의합니다.", "실행 전 서버 측 검증을 둡니다.", "도구 결과와 최종 답변을 로그로 남깁니다."],
        "en_actions": ["Define narrow tool input schemas.", "Validate server-side before execution.", "Log tool results and final answers."],
        "signals": ["schema field", "permission level", "validation failure", "tool result"],
        "ko_signals": ["스키마 필드", "권한 수준", "검증 실패", "도구 결과"],
        "sources": ["openai_function_calling", "openai_tools", "owasp_llm"],
        "tags": ["Function Calling", "Tool Use", "API", "AI Security"],
    },
    {
        "slug": "local-llm-vs-cloud-llm",
        "ko_title": "Local LLM vs Cloud LLM: 비용보다 데이터, 지연시간, 운영 책임 먼저 보기",
        "en_title": "Local LLM vs Cloud LLM: Compare Data, Latency, and Operations First",
        "ko_summary": "로컬 LLM과 클라우드 LLM 선택은 가격 비교가 아니라 데이터 민감도, 지연시간, 품질, 운영 책임의 균형이다.",
        "en_summary": "Choosing local or cloud LLMs is a balance of data sensitivity, latency, quality, and operating responsibility, not only price.",
        "ko_focus": "로컬 모델은 통제감을 주지만 배포, 모니터링, 업데이트, 보안 책임을 팀이 직접 져야 한다는 점을 빼면 안 됩니다.",
        "en_focus": "Local models provide control, but the team also owns deployment, monitoring, updates, and security.",
        "ko_actions": ["데이터 반출 가능 여부를 먼저 정합니다.", "응답 지연 목표를 숫자로 둡니다.", "운영자가 감당할 업데이트 주기를 정합니다."],
        "en_actions": ["Decide whether data may leave the environment.", "Set a numeric latency target.", "Define an update cadence the team can support."],
        "signals": ["data boundary", "latency target", "quality benchmark", "ops owner"],
        "ko_signals": ["데이터 경계", "지연시간 목표", "품질 벤치마크", "운영 책임자"],
        "sources": ["nist_gai_profile", "oecd_ai", "stanford_ai_index"],
        "tags": ["Local LLM", "Cloud AI", "Model Selection", "Infrastructure"],
    },
    {
        "slug": "openai-responses-api-guide",
        "ko_title": "OpenAI Responses API 실무 가이드: 입력, 도구, 구조화 출력을 한 흐름으로 보기",
        "en_title": "OpenAI Responses API Practical Guide: Inputs, Tools, and Structured Outputs",
        "ko_summary": "Responses API는 모델 응답, 도구 호출, 구조화 출력, 멀티모달 입력을 하나의 워크플로우로 설계할 때 이해하기 쉽다.",
        "en_summary": "The Responses API is easier to understand when model output, tools, structured output, and multimodal input are designed as one workflow.",
        "ko_focus": "API 선택은 최신 이름을 따라가는 문제가 아니라 상태, 도구, 출력 검증을 어떤 인터페이스로 묶을지 정하는 문제입니다.",
        "en_focus": "API selection is not about chasing the newest name; it is about how state, tools, and output validation fit together.",
        "ko_actions": ["입력 타입과 출력 형식을 먼저 정합니다.", "도구 호출이 필요한 단계만 분리합니다.", "응답 검증과 재시도 규칙을 둡니다."],
        "en_actions": ["Define input type and output shape first.", "Separate only the steps that need tools.", "Add response validation and retry rules."],
        "signals": ["input type", "tool call", "structured output", "retry rule"],
        "ko_signals": ["입력 타입", "도구 호출", "구조화 출력", "재시도 규칙"],
        "sources": ["openai_responses", "openai_tools", "openai_structured_outputs"],
        "tags": ["OpenAI", "Responses API", "API Design", "Structured Outputs"],
    },
    {
        "slug": "structured-outputs-json-schema",
        "ko_title": "Structured Outputs와 JSON Schema: 파싱 성공보다 의미 검증이 중요하다",
        "en_title": "Structured Outputs and JSON Schema: Validate Meaning, Not Only Parsing",
        "ko_summary": "구조화 출력은 JSON 파싱 실패를 줄여 주지만 값의 의미, 누락 필드, 업무 규칙 위반은 별도 검증해야 한다.",
        "en_summary": "Structured outputs reduce parsing failures, but meaning, missing fields, and business-rule violations still need validation.",
        "ko_focus": "스키마는 출력 모양을 고정하지만 업무적으로 맞는 값인지까지 보장하지 않습니다.",
        "en_focus": "A schema can fix output shape, but it does not prove that the values are correct for the business task.",
        "ko_actions": ["필수 필드와 허용 값을 정합니다.", "업무 규칙 검증을 애플리케이션에 둡니다.", "실패 유형을 파싱, 스키마, 의미 오류로 나눕니다."],
        "en_actions": ["Define required fields and allowed values.", "Keep business-rule validation in the application.", "Split failures into parsing, schema, and semantic errors."],
        "signals": ["required field", "enum value", "semantic mismatch", "retry count"],
        "ko_signals": ["필수 필드", "허용 값", "의미 불일치", "재시도 횟수"],
        "sources": ["openai_structured_outputs", "openai_function_calling", "nist_gai_profile"],
        "tags": ["Structured Outputs", "JSON Schema", "Validation", "API"],
    },
    {
        "slug": "ai-evals-scorecard",
        "ko_title": "AI Evals Scorecard: 데모가 아니라 회귀 테스트로 품질을 관리하기",
        "en_title": "AI Evals Scorecard: Manage Quality with Regression Tests",
        "ko_summary": "AI 평가는 데모 질문 몇 개가 아니라 기준 데이터, 평가자, 실패 유형, 릴리스 차단 기준을 가진 회귀 테스트여야 한다.",
        "en_summary": "AI evaluation should be a regression test with benchmark data, graders, failure types, and release gates, not a few demo prompts.",
        "ko_focus": "모델이나 프롬프트를 바꿀 때마다 좋아진 느낌이 아니라 같은 질문 세트에서 실패가 줄었는지 봐야 합니다.",
        "en_focus": "When changing a model or prompt, judge improvement by a stable question set, not by the feeling of a better demo.",
        "ko_actions": ["실제 사용자 질문 표본을 만듭니다.", "정답 기준과 금지 오류를 정의합니다.", "배포 차단 점수를 정합니다."],
        "en_actions": ["Build a sample of real user questions.", "Define expected answers and prohibited errors.", "Set a release-blocking score."],
        "signals": ["golden set", "grader rule", "failure class", "release gate"],
        "ko_signals": ["기준 질문셋", "평가 규칙", "실패 유형", "배포 차단 기준"],
        "sources": ["openai_evals", "nist_ai_rmf", "stanford_ai_index"],
        "tags": ["AI Evaluation", "Evals", "Quality Assurance", "Regression Testing"],
    },
    {
        "slug": "retrieval-vector-store-governance",
        "ko_title": "Retrieval과 Vector Store 거버넌스: 문서 수집보다 삭제와 버전 관리",
        "en_title": "Retrieval and Vector Store Governance: Version and Delete, Not Only Upload",
        "ko_summary": "벡터 저장소는 문서를 많이 넣는 것보다 소스 버전, 삭제 지연, 접근권한, 검색 품질을 관리할 때 신뢰할 수 있다.",
        "en_summary": "Vector stores become trustworthy when source versions, deletion lag, access rights, and search quality are managed.",
        "ko_focus": "RAG 저장소는 지식창고가 아니라 계속 바뀌는 운영 데이터베이스입니다.",
        "en_focus": "A RAG store is not a static knowledge vault; it is an operating database that keeps changing.",
        "ko_actions": ["문서 원본과 업로드 버전을 연결합니다.", "삭제 후 검색 잔존 여부를 점검합니다.", "권한별 검색 범위를 테스트합니다."],
        "en_actions": ["Link uploaded chunks to source versions.", "Test whether deleted content still appears.", "Test retrieval scope by permission level."],
        "signals": ["source version", "deleted file", "permission filter", "stale answer"],
        "ko_signals": ["원본 버전", "삭제 파일", "권한 필터", "오래된 답변"],
        "sources": ["openai_retrieval", "nist_gai_profile", "owasp_llm"],
        "tags": ["Retrieval", "Vector Store", "RAG", "Governance"],
    },
    {
        "slug": "ai-agent-human-in-loop",
        "ko_title": "Human-in-the-Loop AI: 사람 검토를 병목이 아니라 안전장치로 설계하기",
        "en_title": "Human-in-the-Loop AI: Design Review as a Safety Control",
        "ko_summary": "사람 검토는 모든 결과를 다시 읽는 일이 아니라 위험도에 따라 승인, 샘플링, 예외 처리로 나누는 통제 장치다.",
        "en_summary": "Human review should be a risk-based control with approval, sampling, and exception handling, not rereading every output.",
        "ko_focus": "검토자가 항상 마지막에 모든 것을 고치면 자동화는 비용만 옮깁니다.",
        "en_focus": "If reviewers fix everything at the end, automation only moves the cost downstream.",
        "ko_actions": ["위험도를 낮음, 중간, 높음으로 나눕니다.", "낮은 위험은 표본 검토로 둡니다.", "높은 위험은 실행 전 승인으로 막습니다."],
        "en_actions": ["Classify risk as low, medium, or high.", "Use sampling review for low-risk output.", "Require approval before high-risk execution."],
        "signals": ["risk tier", "sample rate", "approval queue", "exception reason"],
        "ko_signals": ["위험 등급", "표본 비율", "승인 대기열", "예외 사유"],
        "sources": ["nist_ai_rmf", "oecd_principles", "eu_ai"],
        "tags": ["Human Review", "AI Governance", "Risk Management", "Operations"],
    },
    {
        "slug": "ai-workflow-cost-control",
        "ko_title": "AI Workflow Cost Control: 토큰보다 재시도, 검색, 검토 비용을 함께 보기",
        "en_title": "AI Workflow Cost Control: Track Retries, Retrieval, and Review",
        "ko_summary": "AI 비용 관리는 토큰 단가보다 재시도 횟수, 검색 저장소, 도구 호출, 사람 검토 시간이 누적될 때 중요해진다.",
        "en_summary": "AI cost control depends on retries, retrieval storage, tool calls, and review time, not only token price.",
        "ko_focus": "프로토타입 비용은 작아 보여도 운영에서는 실패 재시도와 검토 대기열이 더 큰 비용이 될 수 있습니다.",
        "en_focus": "Prototype cost can look small while production retries and review queues become the larger bill.",
        "ko_actions": ["작업 1건당 전체 호출 수를 기록합니다.", "검색 저장소와 파일 수명주기를 관리합니다.", "사람 검토 시간을 비용표에 넣습니다."],
        "en_actions": ["Record total calls per completed task.", "Manage retrieval storage and file lifecycle.", "Put human review time in the cost table."],
        "signals": ["calls per task", "retry rate", "storage growth", "review queue"],
        "ko_signals": ["작업당 호출 수", "재시도율", "저장소 증가", "검토 대기열"],
        "sources": ["openai_responses", "openai_retrieval", "oecd_ai"],
        "tags": ["AI Cost", "Operations", "Automation", "FinOps"],
    },
    {
        "slug": "ai-data-privacy-redaction",
        "ko_title": "AI Data Privacy Redaction: 프롬프트에 넣기 전 줄여야 할 개인정보",
        "en_title": "AI Data Privacy Redaction: Reduce Sensitive Data Before Prompting",
        "ko_summary": "AI 입력 데이터는 보내기 전에 목적, 최소 필요 정보, 식별자, 보관 기간을 기준으로 줄여야 한다.",
        "en_summary": "AI input data should be reduced before prompting based on purpose, minimum necessary fields, identifiers, and retention period.",
        "ko_focus": "프라이버시 보호는 모델이 안전하다고 믿는 문제가 아니라 보내지 않아도 되는 데이터를 먼저 제거하는 문제입니다.",
        "en_focus": "Privacy protection starts by removing data that does not need to be sent, not by assuming a model is safe.",
        "ko_actions": ["업무 목적에 필요한 필드만 남깁니다.", "이름, 연락처, 계정번호를 별도 토큰으로 치환합니다.", "원본과 치환본 접근권한을 분리합니다."],
        "en_actions": ["Keep only fields needed for the task.", "Replace names, contacts, and account numbers with tokens.", "Separate access to originals and redacted copies."],
        "signals": ["personal identifier", "minimum field", "retention rule", "access log"],
        "ko_signals": ["개인 식별자", "최소 필드", "보관 규칙", "접근 로그"],
        "sources": ["nist_gai_profile", "owasp_llm", "oecd_principles"],
        "tags": ["AI Privacy", "Data Protection", "Redaction", "Governance"],
    },
    {
        "slug": "llm-security-prompt-injection",
        "ko_title": "LLM Prompt Injection 대응: 지시문보다 권한과 데이터 경계를 먼저 막기",
        "en_title": "LLM Prompt Injection Defense: Bound Permissions and Data First",
        "ko_summary": "프롬프트 인젝션은 문장 필터만으로 막기 어렵고 도구 권한, 검색 자료, 출력 처리, 승인 흐름을 함께 제한해야 한다.",
        "en_summary": "Prompt injection cannot be solved by text filters alone; tool permissions, retrieved data, output handling, and approvals must be bounded.",
        "ko_focus": "LLM 보안의 핵심은 모델이 악성 문장을 보지 않게 하는 것이 아니라 보더라도 할 수 있는 일을 제한하는 것입니다.",
        "en_focus": "The security goal is not that the model never sees hostile text; it is that hostile text cannot grant power.",
        "ko_actions": ["사용자 입력과 시스템 지시를 분리합니다.", "도구 실행 권한을 최소화합니다.", "외부 출력은 실행 전 검증합니다."],
        "en_actions": ["Separate user input from system instructions.", "Minimize tool execution permissions.", "Validate external output before execution."],
        "signals": ["untrusted text", "tool permission", "output handling", "data exfiltration"],
        "ko_signals": ["신뢰 불가 텍스트", "도구 권한", "출력 처리", "데이터 유출"],
        "sources": ["owasp_llm", "nist_gai_profile", "openai_tools"],
        "tags": ["LLM Security", "Prompt Injection", "OWASP", "AI Risk"],
    },
    {
        "slug": "ai-content-provenance-watermark",
        "ko_title": "AI Content Provenance: 워터마크보다 제작 경로와 검토 기록 남기기",
        "en_title": "AI Content Provenance: Keep Creation Path and Review Records",
        "ko_summary": "AI 콘텐츠 신뢰성은 워터마크 하나보다 생성 도구, 원본 자료, 편집자, 검토 날짜를 함께 기록할 때 높아진다.",
        "en_summary": "AI content trust improves when generation tool, source material, editor, and review date are recorded together.",
        "ko_focus": "합성 콘텐츠가 늘수록 중요한 것은 표시 여부뿐 아니라 누가 어떤 자료로 만들고 언제 검토했는지입니다.",
        "en_focus": "As synthetic content grows, the key question is who made it, from what source, and when it was reviewed.",
        "ko_actions": ["생성 도구와 사용 목적을 기록합니다.", "사람 편집자와 승인 날짜를 남깁니다.", "외부 공개물에는 출처와 수정 여부를 표시합니다."],
        "en_actions": ["Record generation tool and purpose.", "Store human editor and approval date.", "Label source and edits on public material."],
        "signals": ["generation source", "editor review", "public label", "source evidence"],
        "ko_signals": ["생성 출처", "편집 검토", "공개 표시", "원본 근거"],
        "sources": ["eu_gpai", "oecd_principles", "nist_gai_profile"],
        "tags": ["AI Content", "Provenance", "Trust", "Governance"],
    },
    {
        "slug": "multimodal-ai-workflow",
        "ko_title": "Multimodal AI Workflow: 텍스트, 이미지, 음성을 한 번에 믿지 않기",
        "en_title": "Multimodal AI Workflow: Verify Text, Image, and Audio Separately",
        "ko_summary": "멀티모달 AI는 입력이 풍부해질수록 오류 경로도 늘어나므로 텍스트, 이미지, 음성의 검증 기준을 따로 둬야 한다.",
        "en_summary": "Multimodal AI adds value and error paths, so text, image, and audio need separate verification rules.",
        "ko_focus": "사진과 음성이 들어오면 답변이 더 사실처럼 보이지만 실제로는 캡션 오류, 맥락 누락, 권리 문제가 함께 늘어납니다.",
        "en_focus": "Images and audio can make answers feel more factual while adding caption errors, missing context, and rights issues.",
        "ko_actions": ["입력 유형별 허용 용도를 정합니다.", "이미지 판단은 원본과 캡션을 함께 검토합니다.", "음성 기록은 중요한 결정 전에 확인합니다."],
        "en_actions": ["Define allowed use by input type.", "Review image claims with the original and caption.", "Confirm audio transcripts before decisions."],
        "signals": ["input modality", "caption claim", "transcript error", "rights issue"],
        "ko_signals": ["입력 유형", "캡션 주장", "전사 오류", "권리 문제"],
        "sources": ["openai_responses", "nist_gai_profile", "oecd_ai"],
        "tags": ["Multimodal AI", "AI Workflow", "Verification", "Content"],
    },
    {
        "slug": "voice-realtime-ai-use-cases",
        "ko_title": "Voice와 Realtime AI Use Cases: 빠른 응답보다 중단 규칙이 먼저다",
        "en_title": "Voice and Realtime AI Use Cases: Stop Rules Before Speed",
        "ko_summary": "실시간 음성 AI는 지연시간이 낮을수록 유용하지만 결제, 의료, 법률, 신원확인 같은 상황에서는 중단 규칙이 더 중요하다.",
        "en_summary": "Realtime voice AI benefits from low latency, but stop rules matter more in payment, medical, legal, or identity contexts.",
        "ko_focus": "목소리 인터페이스는 사용자가 검토할 시간을 줄이므로 잘못된 자동 실행을 막는 경계가 필요합니다.",
        "en_focus": "Voice interfaces reduce review time, so boundaries against mistaken execution are essential.",
        "ko_actions": ["실시간 답변과 실행 행동을 분리합니다.", "민감한 요청은 텍스트 확인 단계로 넘깁니다.", "녹취와 동의 보관 규칙을 정합니다."],
        "en_actions": ["Separate realtime answers from execution actions.", "Move sensitive requests to text confirmation.", "Define consent and transcript retention rules."],
        "signals": ["latency target", "sensitive action", "identity check", "transcript record"],
        "ko_signals": ["지연시간 목표", "민감 행동", "신원 확인", "전사 기록"],
        "sources": ["openai_responses", "nist_ai_rmf", "oecd_principles"],
        "tags": ["Voice AI", "Realtime AI", "User Experience", "Safety"],
    },
    {
        "slug": "ai-customer-support-knowledge-base",
        "ko_title": "AI Customer Support Knowledge Base: 답변 자동화보다 근거 연결",
        "en_title": "AI Customer Support Knowledge Base: Connect Answers to Evidence",
        "ko_summary": "고객지원 AI는 빠른 답변보다 정책 문서, 계정 상태, 예외 조건, 상담원 승인 경로를 정확히 연결해야 한다.",
        "en_summary": "Customer-support AI must connect policy documents, account state, exceptions, and agent approval paths before it speeds up replies.",
        "ko_focus": "지원 자동화는 고객에게 그럴듯한 답을 내는 것이 아니라 회사가 실제로 지킬 수 있는 답을 내는 일입니다.",
        "en_focus": "Support automation should produce answers the company can stand behind, not just plausible replies.",
        "ko_actions": ["정책 문서와 답변 문장을 연결합니다.", "환불, 해지, 보상 예외를 따로 둡니다.", "상담원 승인 조건을 명확히 합니다."],
        "en_actions": ["Link answer sentences to policy documents.", "Separate refund, cancellation, and compensation exceptions.", "Define escalation-to-agent conditions."],
        "signals": ["policy source", "account state", "exception rule", "agent handoff"],
        "ko_signals": ["정책 원문", "계정 상태", "예외 규칙", "상담원 인계"],
        "sources": ["openai_retrieval", "openai_structured_outputs", "nist_ai_rmf"],
        "tags": ["Customer Support", "Knowledge Base", "RAG", "AI Operations"],
    },
    {
        "slug": "ai-sales-research-workflow",
        "ko_title": "AI Sales Research Workflow: 리드 점수보다 근거와 최신성 확인",
        "en_title": "AI Sales Research Workflow: Check Evidence and Freshness",
        "ko_summary": "영업 리서치 AI는 리드 점수보다 출처 날짜, 회사 변화, 담당자 근거, 연락 금지 조건을 먼저 확인해야 한다.",
        "en_summary": "Sales research AI should check source dates, company changes, contact evidence, and do-not-contact rules before scoring leads.",
        "ko_focus": "영업 자동화의 위험은 잘못된 연락처보다 오래된 정보로 신뢰를 잃는 데 있습니다.",
        "en_focus": "The risk in sales automation is not only wrong contact data; it is losing trust through stale claims.",
        "ko_actions": ["출처 날짜와 회사 이벤트를 함께 저장합니다.", "담당자 추정 근거를 별도 필드로 둡니다.", "연락 금지와 지역 규칙을 확인합니다."],
        "en_actions": ["Store source date with company events.", "Keep contact inference evidence in a separate field.", "Check do-not-contact and regional rules."],
        "signals": ["source date", "company event", "contact evidence", "outreach rule"],
        "ko_signals": ["출처 날짜", "회사 이벤트", "담당자 근거", "연락 규칙"],
        "sources": ["openai_structured_outputs", "nist_ai_rmf", "oecd_principles"],
        "tags": ["Sales AI", "Research Workflow", "Automation", "Data Quality"],
    },
    {
        "slug": "ai-education-study-tutor",
        "ko_title": "AI Study Tutor 설계: 정답 대신 힌트, 회상, 오답 분석",
        "en_title": "AI Study Tutor Design: Hints, Recall, and Mistake Analysis",
        "ko_summary": "AI 튜터는 정답을 바로 주기보다 힌트 단계, 능동 회상, 오답 원인, 다음 복습 계획을 만드는 데 강점을 둬야 한다.",
        "en_summary": "AI tutors are strongest when they guide hints, active recall, mistake causes, and next review plans instead of giving answers immediately.",
        "ko_focus": "학습용 AI는 편한 답안 생성기가 되면 오히려 기억 형성을 방해할 수 있습니다.",
        "en_focus": "An AI tutor can hurt learning if it becomes a convenient answer generator instead of a recall partner.",
        "ko_actions": ["정답 공개 전 힌트 단계를 둡니다.", "학생이 먼저 설명하게 합니다.", "오답 유형과 다음 복습일을 기록합니다."],
        "en_actions": ["Add hint stages before revealing answers.", "Ask the learner to explain first.", "Record mistake type and next review date."],
        "signals": ["hint level", "learner explanation", "mistake type", "review date"],
        "ko_signals": ["힌트 단계", "학습자 설명", "오답 유형", "복습 날짜"],
        "sources": ["oecd_ai", "nist_ai_rmf", "stanford_ai_index"],
        "tags": ["AI Education", "Study", "Tutoring", "Learning"],
    },
    {
        "slug": "ai-hr-screening-risk",
        "ko_title": "AI HR Screening Risk: 채용 자동화에서 설명 가능성과 차별 위험 보기",
        "en_title": "AI HR Screening Risk: Watch Explainability and Discrimination",
        "ko_summary": "채용 AI는 속도보다 평가 기준, 데이터 편향, 설명 가능성, 이의제기 경로를 먼저 갖춰야 한다.",
        "en_summary": "Hiring AI needs criteria, bias checks, explainability, and appeal paths before speed.",
        "ko_focus": "사람의 기회를 제한하는 AI는 내부 효율성만으로 정당화하기 어렵습니다.",
        "en_focus": "AI that affects employment opportunities cannot be justified by internal efficiency alone.",
        "ko_actions": ["평가 기준을 직무 요건과 연결합니다.", "데이터 편향과 대리 변수를 점검합니다.", "지원자 이의제기 경로를 둡니다."],
        "en_actions": ["Connect scoring criteria to job requirements.", "Check data bias and proxy variables.", "Provide an appeal path for candidates."],
        "signals": ["job criterion", "proxy variable", "bias test", "appeal process"],
        "ko_signals": ["직무 기준", "대리 변수", "편향 테스트", "이의제기 절차"],
        "sources": ["eu_ai", "oecd_principles", "nist_ai_rmf"],
        "tags": ["HR AI", "AI Risk", "Governance", "Fairness"],
    },
    {
        "slug": "ai-legal-contract-review-limits",
        "ko_title": "AI Contract Review 한계: 조항 요약과 법률 판단을 분리하기",
        "en_title": "AI Contract Review Limits: Separate Clause Summary from Legal Judgment",
        "ko_summary": "계약서 AI는 조항 요약, 누락 탐지, 질문 목록에는 유용하지만 법률 판단과 협상 책임을 대신할 수 없다.",
        "en_summary": "Contract-review AI can summarize clauses, flag omissions, and draft questions, but it cannot replace legal judgment or negotiation responsibility.",
        "ko_focus": "계약 문서에서 AI의 역할은 판단자가 아니라 놓친 부분을 빨리 찾는 보조 검토자입니다.",
        "en_focus": "For contracts, AI should be a review assistant that finds issues faster, not the final legal decision-maker.",
        "ko_actions": ["조항 요약과 위험 추정을 분리합니다.", "관할 법률과 버전을 표시합니다.", "전문가 검토가 필요한 항목을 따로 뽑습니다."],
        "en_actions": ["Separate clause summary from risk inference.", "Mark jurisdiction and document version.", "List items requiring professional review."],
        "signals": ["clause version", "jurisdiction", "missing term", "expert review"],
        "ko_signals": ["조항 버전", "관할", "누락 조건", "전문가 검토"],
        "sources": ["nist_gai_profile", "oecd_principles", "eu_ai"],
        "tags": ["Legal AI", "Contracts", "Risk", "Document Review"],
    },
    {
        "slug": "ai-health-information-triage-limits",
        "ko_title": "AI Health Information Triage 한계: 증상 설명과 진단을 분리하기",
        "en_title": "AI Health Information Triage Limits: Separate Symptom Explanation from Diagnosis",
        "ko_summary": "건강 정보 AI는 질문 정리와 일반 정보 안내에는 도움이 되지만 진단, 치료, 복용량 판단은 의료진 확인이 필요하다.",
        "en_summary": "Health-information AI can organize questions and general information, but diagnosis, treatment, and dosage decisions require medical professionals.",
        "ko_focus": "건강 분야 AI는 불안을 줄일 수 있지만 잘못된 안심을 주면 위험이 커집니다.",
        "en_focus": "Health AI can reduce confusion, but false reassurance can create serious risk.",
        "ko_actions": ["증상 시작일과 변화 기록을 돕습니다.", "응급 신호는 즉시 전문가 안내로 넘깁니다.", "진단이나 복용량 표현을 금지합니다."],
        "en_actions": ["Help record symptom start and changes.", "Route red flags to professional care guidance.", "Prohibit diagnosis or dosage language."],
        "signals": ["symptom timeline", "red flag", "medical claim", "care referral"],
        "ko_signals": ["증상 타임라인", "위험 신호", "의학 주장", "진료 안내"],
        "sources": ["nist_gai_profile", "oecd_principles", "eu_ai"],
        "tags": ["Health AI", "Safety", "Triage", "AI Risk"],
    },
    {
        "slug": "ai-copyright-training-data-risk",
        "ko_title": "AI Copyright와 Training Data Risk: 생성물보다 입력 자료 기록부터",
        "en_title": "AI Copyright and Training Data Risk: Track Inputs Before Outputs",
        "ko_summary": "AI 저작권 리스크는 생성물만 보는 것이 아니라 입력 자료의 권리, 사용 목적, 보관, 공개 범위를 함께 관리해야 한다.",
        "en_summary": "AI copyright risk requires managing input rights, purpose, retention, and publication scope, not only the generated output.",
        "ko_focus": "콘텐츠 팀은 AI가 만든 문장보다 어떤 자료를 넣었고 어디까지 공개할지 먼저 기록해야 합니다.",
        "en_focus": "Content teams should record what material entered the workflow and where the result will be published.",
        "ko_actions": ["입력 자료의 권리 상태를 표시합니다.", "외부 공개 여부에 따라 검토 수준을 바꿉니다.", "유사성 검토와 사람 편집 기록을 남깁니다."],
        "en_actions": ["Mark rights status of input material.", "Change review level by publication scope.", "Keep similarity checks and human-edit records."],
        "signals": ["input rights", "publication scope", "similarity check", "editor record"],
        "ko_signals": ["입력 권리", "공개 범위", "유사성 검토", "편집 기록"],
        "sources": ["eu_gpai", "oecd_principles", "nist_gai_profile"],
        "tags": ["AI Copyright", "Training Data", "Content", "Governance"],
    },
    {
        "slug": "eu-ai-act-business-checklist",
        "ko_title": "EU AI Act Business Checklist: 유럽 고객이 없어도 볼 이유",
        "en_title": "EU AI Act Business Checklist: Why Non-EU Teams Should Watch It",
        "ko_summary": "EU AI Act는 유럽 사업자만의 문제가 아니라 글로벌 고객, 공급망, 벤더 계약, 제품 문서 요구로 번질 수 있다.",
        "en_summary": "The EU AI Act can affect global customers, supply chains, vendor contracts, and product documentation beyond EU-only teams.",
        "ko_focus": "규제는 국경 밖 팀에게도 고객 요구사항과 조달 체크리스트 형태로 먼저 도착할 수 있습니다.",
        "en_focus": "Regulation can reach non-EU teams first as customer requirements and procurement checklists.",
        "ko_actions": ["AI 시스템의 사용 목적을 분류합니다.", "고위험 가능성과 사용자 고지를 확인합니다.", "벤더 문서와 내부 기록을 연결합니다."],
        "en_actions": ["Classify the AI system purpose.", "Check high-risk possibility and user notice requirements.", "Link vendor documents to internal records."],
        "signals": ["system purpose", "risk class", "user notice", "vendor documentation"],
        "ko_signals": ["시스템 목적", "위험 등급", "사용자 고지", "벤더 문서"],
        "sources": ["eu_ai", "eu_gpai", "oecd_principles"],
        "tags": ["EU AI Act", "AI Governance", "Compliance", "Business"],
    },
    {
        "slug": "nist-ai-rmf-team-checklist",
        "ko_title": "NIST AI RMF Team Checklist: 거버넌스를 문서가 아니라 운영 루틴으로 만들기",
        "en_title": "NIST AI RMF Team Checklist: Turn Governance into Operating Routines",
        "ko_summary": "NIST AI RMF는 AI 리스크를 지도화, 측정, 관리, 거버넌스 루틴으로 나눠 팀 운영에 적용하기 좋다.",
        "en_summary": "The NIST AI RMF helps teams translate AI risk into mapping, measuring, managing, and governance routines.",
        "ko_focus": "AI 거버넌스는 정책 문서 하나가 아니라 출시 전후에 반복되는 질문 목록이어야 합니다.",
        "en_focus": "AI governance should be a recurring question set before and after release, not a single policy document.",
        "ko_actions": ["사용자와 피해 가능성을 지도화합니다.", "품질과 안전 지표를 측정합니다.", "릴리스 후 사고 대응 책임자를 정합니다."],
        "en_actions": ["Map users and possible harms.", "Measure quality and safety signals.", "Assign post-release incident owners."],
        "signals": ["mapped use case", "measured metric", "managed risk", "governance owner"],
        "ko_signals": ["사용 사례 지도", "측정 지표", "관리 리스크", "거버넌스 책임자"],
        "sources": ["nist_ai_rmf", "nist_gai_profile", "oecd_principles"],
        "tags": ["NIST AI RMF", "AI Governance", "Risk Management", "Team Process"],
    },
    {
        "slug": "ai-procurement-vendor-evaluation",
        "ko_title": "AI Vendor Evaluation: 데모보다 데이터, 보안, 탈출 비용 묻기",
        "en_title": "AI Vendor Evaluation: Ask About Data, Security, and Exit Cost",
        "ko_summary": "AI 벤더 평가는 멋진 데모보다 데이터 처리, 모델 변경, 보안 통제, 로그, 계약 종료 시 이전 비용을 확인해야 한다.",
        "en_summary": "AI vendor evaluation should check data handling, model changes, security controls, logs, and exit cost before demo polish.",
        "ko_focus": "구매 전 질문이 부족하면 나중에 데이터 반출, 품질 저하, 가격 변경을 협상하기 어렵습니다.",
        "en_focus": "If procurement questions are weak, data export, quality drift, and pricing changes become difficult to negotiate later.",
        "ko_actions": ["데이터 사용과 학습 사용 여부를 묻습니다.", "모델 변경 공지와 평가 자료를 요구합니다.", "계약 종료 시 데이터 회수 절차를 확인합니다."],
        "en_actions": ["Ask how data is used and whether it trains models.", "Require model-change notice and evaluation records.", "Check data return process at contract end."],
        "signals": ["data use", "model change", "security control", "exit path"],
        "ko_signals": ["데이터 사용", "모델 변경", "보안 통제", "종료 경로"],
        "sources": ["nist_ai_rmf", "owasp_llm", "oecd_principles"],
        "tags": ["AI Procurement", "Vendor Risk", "Security", "Governance"],
    },
]


def yaml_list(items: list[str]) -> str:
    return "\n".join(f"  - {item}" for item in items)


def escape_svg_text(value: object) -> str:
    return html.escape(str(value), quote=False)


def wrap_words(text: str, limit: int = 34) -> list[str]:
    words = str(text).split()
    lines: list[str] = []
    current: list[str] = []
    current_len = 0
    for word in words:
        extra = 1 if current else 0
        if current and current_len + len(word) + extra > limit:
            lines.append(" ".join(current))
            current = [word]
            current_len = len(word)
        else:
            current.append(word)
            current_len += len(word) + extra
    if current:
        lines.append(" ".join(current))
    return lines[:4]


def source_notes(source_keys: list[str], lang: str) -> str:
    return "\n".join(f"- [{SOURCES[key][lang]}]({SOURCES[key]['url']})" for key in source_keys)


def related_links(index: int, lang: str) -> str:
    related = [TOPICS[(index + 1) % len(TOPICS)], TOPICS[(index + 11) % len(TOPICS)]]
    category_path = KO_CATEGORY.lower() if lang == "ko" else EN_CATEGORY.lower()
    if lang == "ko":
        return "\n".join(f"- [{topic['ko_title']}](/{{category}}/{topic['slug']}/)".replace("{category}", category_path) for topic in related)
    return "\n".join(f"- [{topic['en_title']}](/{{category}}/{topic['slug']}/)".replace("{category}", category_path) for topic in related)


def normalize_markdown(text: str) -> str:
    normalized = "\n".join(line[4:] if line.startswith("    ") else line for line in text.splitlines()).lstrip()
    return normalized.replace("sidebar:\nnav:", "sidebar:\n    nav:") + "\n"


def hex_to_rgb(value: str) -> tuple[int, int, int]:
    value = value.lstrip("#")
    return tuple(int(value[index : index + 2], 16) for index in (0, 2, 4))


def blend(a: tuple[int, int, int], b: tuple[int, int, int], ratio: float) -> tuple[int, int, int]:
    return tuple(int(a[i] * (1 - ratio) + b[i] * ratio) for i in range(3))


def png_chunk(kind: bytes, data: bytes) -> bytes:
    return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data) & 0xFFFFFFFF)


def write_png(path: Path, title: str, labels: list[str], palette: tuple[str, str], variant: int) -> None:
    width, height = 1200, 675
    base = hex_to_rgb(palette[0])
    accent = hex_to_rgb(palette[1])
    deep = (15, 23, 42)
    rows: list[bytes] = []
    label_count = max(1, len(labels))
    title_weight = min(220, sum(ord(ch) for ch in title) % 220)

    for y in range(height):
        vertical = y / (height - 1)
        left = blend(base, deep, min(0.70, vertical * 0.48))
        middle = blend(base, deep, min(0.86, 0.28 + vertical * 0.36))
        right = blend(deep, accent, 0.16 + (variant * 0.04))
        card = blend((2, 6, 23), accent, 0.08)
        bar = blend(accent, (255, 255, 255), 0.16 + ((title_weight % 5) * 0.02))

        if y % 64 == 0:
            row = bytes(blend(left, (255, 255, 255), 0.12)) * width
        elif 302 <= y <= 544:
            row = (
                bytes(left) * 66
                + bytes(card) * 560
                + bytes(middle) * 140
                + bytes(right) * 434
            )
        elif 186 + variant * 24 <= y <= 214 + variant * 24:
            row = bytes(left) * 690 + bytes(bar) * 390 + bytes(right) * 120
        elif 252 <= y <= 502 and (y - 252) % max(36, 58 - label_count * 2) < 18:
            row = bytes(left) * 72 + bytes(middle) * 620 + bytes(bar) * 348 + bytes(right) * 160
        else:
            row = bytes(left) * 620 + bytes(middle) * 260 + bytes(right) * 320
        rows.append(b"\x00" + row)

    raw = b"".join(rows)
    png = (
        b"\x89PNG\r\n\x1a\n"
        + png_chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0))
        + png_chunk(b"IDAT", zlib.compress(raw, 6))
        + png_chunk(b"IEND", b"")
    )
    path.write_bytes(png)


def bounded_text(value: str, minimum: int, maximum: int, suffix: str) -> str:
    text = value if len(value) >= minimum else f"{value} {suffix}"
    if len(text) > maximum:
        text = text[: maximum - 3].rstrip() + "..."
    return text


def seo_title(topic: dict[str, object], lang: str) -> str:
    title = str(topic["ko_title"] if lang == "ko" else topic["en_title"])
    return bounded_text(title, 10 if lang == "ko" else 20, 70, "AI guide")


def seo_description(topic: dict[str, object], lang: str) -> str:
    if lang == "ko":
        return bounded_text(
            str(topic["ko_summary"]),
            60,
            170,
            "도입 전 확인할 검증 기준, 운영 책임, 보안 통제, 사람 검토 지점을 함께 정리합니다.",
        )
    return bounded_text(
        str(topic["en_summary"]),
        80,
        170,
        "It adds verification steps, risk controls, and operating questions for practical adoption.",
    )


def ko_intro(topic: dict[str, object]) -> str:
    first = topic["ko_signals"][0]
    return (
        f"AI 트렌드는 모델 이름을 따라가는 뉴스가 아니라 **{first}**처럼 실제 업무 품질을 바꾸는 신호를 읽는 일입니다. "
        f"이 글은 **{topic['ko_title']}** 주제를 도입 전 의사결정, 검증, 운영 책임 관점에서 정리합니다."
    )


def en_intro(topic: dict[str, object]) -> str:
    first = topic["signals"][0]
    return (
        f"AI trends are not only model-name news. They are signals such as **{first}** that change real workflow quality. "
        f"This guide reads **{topic['en_title']}** through adoption, verification, and operating responsibility."
    )


def ko_risk_frame(topic: dict[str, object]) -> str:
    first = topic["ko_signals"][0]
    second = topic["ko_signals"][1]
    return (
        f"이 주제에서 먼저 볼 것은 **{first}**, **{second}** 두 항목입니다. 둘 중 하나가 흐리면 AI가 빠르게 보이더라도 "
        "결과 검토, 비용 통제, 책임 소재가 뒤로 밀려 실제 운영에서는 품질 문제가 생깁니다."
    )


def en_risk_frame(topic: dict[str, object]) -> str:
    first = topic["signals"][0]
    second = topic["signals"][1]
    return (
        f"For this topic, start with **{first}** and **{second}**. If either is vague, the workflow can look fast while "
        "review, cost control, and accountability move downstream."
    )


def ko_signal_items(topic: dict[str, object]) -> str:
    title = topic["ko_title"]
    return "\n".join(
        f"- **{signal}**: {title} 주제에서 이 항목의 기준, 책임자, 실패 시 대응을 함께 기록합니다."
        for signal in topic["ko_signals"]
    )


def en_signal_items(topic: dict[str, object]) -> str:
    title = topic["en_title"]
    return "\n".join(
        f"- **{signal}**: for {title}, record the standard, owner, and failure response for this item."
        for signal in topic["signals"]
    )


def ko_action_items(topic: dict[str, object]) -> str:
    return "\n".join(f"- {action}" for action in topic["ko_actions"])


def en_action_items(topic: dict[str, object]) -> str:
    return "\n".join(f"- {action}" for action in topic["en_actions"])


def ko_failure_context(topic: dict[str, object]) -> str:
    first = topic["ko_signals"][0]
    action = topic["ko_actions"][0]
    return (
        f"가장 흔한 실패는 **{first}** 항목이 명확하지 않은 상태에서 자동화 범위를 넓히는 것입니다. "
        f"따라서 첫 단계는 '{action}'이고, 이후에도 검토 결과를 기준으로 범위를 넓혀야 합니다."
    )


def en_failure_context(topic: dict[str, object]) -> str:
    first = topic["signals"][0]
    action = str(topic["en_actions"][0]).rstrip(".")
    return (
        f"The common failure is expanding automation before **{first}** is clear. "
        f"Start with '{action}', then widen scope only after review results are stable."
    )


def ko_operations_context(topic: dict[str, object]) -> str:
    first = topic["ko_signals"][0]
    second = topic["ko_signals"][1]
    return (
        f"운영 단계에서는 **{first}**를 한 번 정하고 끝내지 말아야 합니다. 모델, 프롬프트, 데이터, 도구 권한이 바뀌면 "
        f"**{second}** 기준도 같이 다시 확인해야 합니다. 특히 사용자에게 영향을 주는 결과라면 근거 문서, 로그 위치, "
        "수정 요청 경로를 같은 화면이나 문서에서 찾을 수 있어야 합니다."
    )


def en_operations_context(topic: dict[str, object]) -> str:
    first = topic["signals"][0]
    second = topic["signals"][1]
    return (
        f"In operation, **{first}** is not a one-time setup. When the model, prompt, data, or tool permission changes, "
        f"recheck **{second}** as well. For outputs that affect users, the evidence document, log location, and correction path "
        "should be easy to find from the same operating record."
    )


def ko_disclaimer(topic: dict[str, object]) -> str:
    first = topic["ko_signals"][0]
    return (
        f"이 글은 특정 모델이나 벤더를 추천하지 않습니다. **{topic['ko_title']}**를 실제 업무에 적용하기 전에 "
        f"**{first}** 기준, 검토 책임, 운영 로그를 어떻게 확인할지 정리하는 교육용 가이드입니다."
    )


def en_disclaimer(topic: dict[str, object]) -> str:
    first = topic["signals"][0]
    return (
        f"This article is educational and does not recommend a specific model or vendor. For **{topic['en_title']}**, "
        f"it focuses on the **{first}** rule, review ownership, and operating records before adoption."
    )


def ko_team_checklist(topic: dict[str, object]) -> str:
    first = topic["ko_signals"][0]
    second = topic["ko_signals"][1]
    action = topic["ko_actions"][0]
    return "\n".join(
        [
            f"- 도입 목적과 금지 용도를 **{first}** 기준 옆에 함께 적습니다.",
            f"- '{action}' 이후 모델, 프롬프트, 데이터가 바뀌면 **{second}** 기준으로 다시 확인합니다.",
            "- 사용자에게 영향을 주는 결과는 로그, 근거, 이의제기 또는 수정 경로를 남깁니다.",
        ]
    )


def en_team_checklist(topic: dict[str, object]) -> str:
    first = topic["signals"][0]
    second = topic["signals"][1]
    action = str(topic["en_actions"][0]).rstrip(".")
    return "\n".join(
        [
            f"- Keep the adoption goal and prohibited uses next to the **{first}** rule.",
            f"- After '{action}', rerun the same review whenever the model, prompt, data, or **{second}** rule changes.",
            "- For user-impacting outputs, keep logs, evidence, and a path for correction or appeal.",
        ]
    )


def ko_field_example(topic: dict[str, object]) -> str:
    first = topic["ko_signals"][0]
    second = topic["ko_signals"][1]
    action = topic["ko_actions"][0]
    return (
        f"작게 시작하려면 한 팀, 한 문서, 한 업무 흐름을 정하고 **{first}** 기준을 표로 남깁니다. 그 다음 '{action}' 단계를 "
        f"실제 사례 10건에 적용해 성공, 보류, 실패를 나눕니다. 이때 **{second}** 기준은 나중에 기억으로 판단하지 말고 "
        "검토자가 같은 화면에서 볼 수 있는 체크 항목으로 둡니다. 이런 방식이면 AI가 만든 결과가 좋아 보이는지보다 "
        "사람이 검증하고 되돌릴 수 있는지가 먼저 드러납니다."
    )


def en_field_example(topic: dict[str, object]) -> str:
    first = topic["signals"][0]
    second = topic["signals"][1]
    action = str(topic["en_actions"][0]).rstrip(".")
    return (
        f"A practical pilot can stay small: choose one team, one document type, and one workflow, then write the **{first}** rule as a table. "
        f"Apply '{action}' to ten real cases and mark each result as accepted, held for review, or rejected. Keep the **{second}** rule visible "
        "to the reviewer instead of leaving it as tribal memory. This makes the test about controllable quality, not about whether the output "
        "looks impressive in a demo."
    )


def ko_faq(topic: dict[str, object]) -> str:
    first = topic["ko_signals"][0]
    second = topic["ko_signals"][1]
    action = topic["ko_actions"][0]
    return dedent(f"""\
    ### 이 주제는 언제 먼저 적용해야 하나요?

    반복 빈도가 높고 실패 비용이 낮은 업무부터 시작하는 것이 안전합니다. **{topic["ko_title"]}** 주제라도 바로 전면 자동화하지 말고, 먼저 '{action}' 단계와 검토 책임자를 정한 뒤 작은 표본으로 성과와 오류를 확인합니다.

    ### 자동화해도 되는지 판단하는 기준은 무엇인가요?

    **{first}** 기준이 문서화되어 있고, **{second}** 기준을 다른 검토자가 같은 방식으로 확인할 수 있어야 합니다. 기준이 사람마다 다르면 모델 성능 문제가 아니라 운영 설계 문제일 가능성이 큽니다.

    ### 실패했을 때 무엇을 남겨야 하나요?

    입력 자료, 모델 또는 도구 설정, **{first}** 검토 판단, 수정 결과를 함께 남깁니다. 그래야 다음 변경 때 같은 오류가 줄었는지 볼 수 있고, 사용자에게 영향을 준 결과도 설명하거나 되돌릴 수 있습니다.
    """)


def en_faq(topic: dict[str, object]) -> str:
    first = topic["signals"][0]
    second = topic["signals"][1]
    action = str(topic["en_actions"][0]).rstrip(".")
    return dedent(f"""\
    ### When should this topic be applied first?

    Start with work that is frequent and has a low cost of failure. Even for **{topic["en_title"]}**, avoid full automation at the beginning. Define the '{action}' step, name the reviewer, and test outcomes and errors on a small sample.

    ### How do we know whether the {first} rule is safe enough?

    The **{first}** rule should be written down, and another reviewer should be able to check the **{second}** rule in the same way. If every reviewer interprets the rule differently, the issue is usually operating design rather than model capability.

    ### What should be logged when the workflow fails?

    Keep the input evidence, model or tool setting, **{first}** reviewer decision, and correction result together. This lets the team see whether later changes reduce the same error and gives a way to explain or reverse user-impacting output.
    """)


def ko_post(topic: dict[str, object], index: int) -> str:
    slug = topic["slug"]
    image_dir = f"/images/{POST_DATE}-{slug}"
    return dedent(f"""\
    ---
    layout: single
    title: >
      {topic["ko_title"]}
    seo_title: >
      {seo_title(topic, "ko")}
    date: {POST_DATE}T{9 + index // 3:02d}:{(index % 3) * 20:02d}:00+09:00
    last_modified_at: {LAST_MODIFIED_AT}
    lang: ko
    translation_id: ai-trends-{slug}
    header:
      teaser: {image_dir}/hero.png
      overlay_image: {image_dir}/hero.png
      overlay_filter: 0.45
      image_description: >
        {topic["ko_title"]}의 핵심 신호와 실무 적용 순서를 요약한 AI 트렌드 이미지입니다.
    excerpt: >
      {topic["ko_summary"]}
    seo_description: >
      {seo_description(topic, "ko")}
    categories:
      - {KO_CATEGORY}
    tags:
    {yaml_list(topic["tags"])}
    ---

    {ko_intro(topic)}

    {topic["ko_summary"]}

    {ko_disclaimer(topic)}

    ![{topic["ko_title"]} 핵심 흐름]({image_dir}/hero.png)

    ## 왜 지금 중요한가

    {topic["ko_focus"]}

    {ko_risk_frame(topic)}

    ## 먼저 볼 신호

    {ko_signal_items(topic)}

    ![{topic["ko_title"]} 검증 체크리스트]({image_dir}/checklist.png)

    ## 실무 적용 순서

    {ko_action_items(topic)}

    {ko_failure_context(topic)}

    ## 현장 적용 예시

    {ko_field_example(topic)}

    ## 운영 시 주의할 점

    {ko_operations_context(topic)}

    ## 팀 체크리스트

    {ko_team_checklist(topic)}

    ## 자주 묻는 질문

    {ko_faq(topic)}

    ## 참고할 공식 자료

    {source_notes(topic["sources"], "ko")}

    ## 함께 보면 좋은 글

    {related_links(index, "ko")}
    """)


def en_post(topic: dict[str, object], index: int) -> str:
    slug = topic["slug"]
    image_dir = f"/images/{POST_DATE}-{slug}"
    return dedent(f"""\
    ---
    layout: single
    title: >
      {topic["en_title"]}
    seo_title: >
      {seo_title(topic, "en")}
    date: {POST_DATE}T{9 + index // 3:02d}:{(index % 3) * 20:02d}:00+09:00
    last_modified_at: {LAST_MODIFIED_AT}
    lang: en
    translation_id: ai-trends-{slug}
    header:
      teaser: {image_dir}/hero.png
      overlay_image: {image_dir}/hero.png
      overlay_filter: 0.45
      image_description: >
        An AI trends image summarizing core signals and practical adoption order for this topic.
    excerpt: >
      {topic["en_summary"]}
    seo_description: >
      {seo_description(topic, "en")}
    categories:
      - {EN_CATEGORY}
    tags:
    {yaml_list(topic["tags"])}
    ---

    {en_intro(topic)}

    {topic["en_summary"]}

    {en_disclaimer(topic)}

    ![{topic["en_title"]} core flow]({image_dir}/hero.png)

    ## Why This Matters Now

    {topic["en_focus"]}

    {en_risk_frame(topic)}

    ## Signals To Check First

    {en_signal_items(topic)}

    ![{topic["en_title"]} verification checklist]({image_dir}/checklist.png)

    ## Practical Adoption Order

    {en_action_items(topic)}

    {en_failure_context(topic)}

    ## Field Pilot Example

    {en_field_example(topic)}

    ## Operating Notes

    {en_operations_context(topic)}

    ## Team Checklist

    {en_team_checklist(topic)}

    ## FAQ

    {en_faq(topic)}

    ## Source Notes

    {source_notes(topic["sources"], "en")}

    ## Related Reading

    {related_links(index, "en")}
    """)


def category_page(lang: str) -> str:
    if lang == "ko":
        return dedent("""\
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
        """)
    return dedent("""\
    ---
    title: "AI Trends"
    layout: archive
    permalink: /en_ai_trends/
    lang: en
    seo_description: >
      Practical AI trend guides covering AI agents, prompt engineering, RAG, OpenAI APIs, structured outputs, AI security, EU AI Act, NIST AI RMF, and workflow governance.
    sidebar:
        nav: "sidebar-category"
    ---

    The AI Trends category collects practical guides for applying AI tools to real work and software workflows. It prioritizes verification, automation scope, cost, security, data governance, and search visibility over broad news summaries.

    The articles refer to checkable sources such as OpenAI documentation, the NIST AI Risk Management Framework, OWASP LLM security guidance, OECD AI Principles, EU AI Act resources, and the Stanford AI Index. The goal is not to promote a model. The goal is to make adoption questions, evaluation methods, and operating responsibility explicit.

    Start with agent workflow, prompt engineering, RAG evaluation, structured outputs, and LLM security if you want a practical reading path.

    ## Start Here

    - [AI Agent Workflow 2026](/en_ai_trends/ai-agent-workflow-2026/)
    - [Prompt Engineering Checklist](/en_ai_trends/prompt-engineering-checklist/)
    - [RAG Evaluation Checklist](/en_ai_trends/rag-evaluation-checklist/)
    - [Structured Outputs and JSON Schema](/en_ai_trends/structured-outputs-json-schema/)
    - [LLM Prompt Injection Defense](/en_ai_trends/llm-security-prompt-injection/)

    ## Latest Articles

    {% assign posts = site.categories["en_AI_Trends"] %}
    {% for post in posts %}
      {% include archive-single.html type=page.entries_layout %}
    {% endfor %}
    """)


def main() -> None:
    palettes = [
        ("#0f172a", "#38bdf8"),
        ("#111827", "#22c55e"),
        ("#1e293b", "#f97316"),
        ("#172554", "#a78bfa"),
    ]
    for index, topic in enumerate(TOPICS):
        slug = str(topic["slug"])
        image_dir = ROOT / "images" / f"{POST_DATE}-{slug}"
        image_dir.mkdir(parents=True, exist_ok=True)
        palette = palettes[index % len(palettes)]
        for legacy_name in ("hero.svg", "checklist.svg"):
            legacy_path = image_dir / legacy_name
            if legacy_path.exists():
                legacy_path.unlink()
        write_png(
            image_dir / "hero.png",
            str(topic["en_title"]),
            [str(item) for item in topic["signals"]],
            palette,
            index % 3,
        )
        write_png(
            image_dir / "checklist.png",
            str(topic["en_title"]),
            [str(item) for item in topic["en_actions"]],
            (palette[0], "#facc15"),
            (index + 1) % 3,
        )
        (ROOT / "_posts" / "ko" / f"{POST_DATE}-{slug}.md").write_text(normalize_markdown(ko_post(topic, index)), encoding="utf-8")
        (ROOT / "_posts" / "en" / f"{POST_DATE}-{slug}.md").write_text(normalize_markdown(en_post(topic, index)), encoding="utf-8")
    (ROOT / "_pages" / "category-ko_AI_Trends.md").write_text(normalize_markdown(category_page("ko")), encoding="utf-8")
    (ROOT / "_pages" / "category-en_AI_Trends.md").write_text(normalize_markdown(category_page("en")), encoding="utf-8")
    print(f"Generated {len(TOPICS)} paired AI Trends topics.")


if __name__ == "__main__":
    main()
