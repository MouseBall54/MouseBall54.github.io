---
layout: single
title: >
  Codex config.toml approval_policy and sandbox_mode 설정 가이드
seo_title: >
  Codex config.toml approval_policy and sandbox_mode 설정 가이드
date: 2026-01-14T09:12:00+09:00
last_modified_at: 2026-05-24T09:30:00+09:00
lang: ko
translation_id: ai-agent-cli-codex-config-toml-approval-sandbox
header:
  teaser: /images/2026-01-14-codex-config-toml-approval-sandbox/hero.svg
  overlay_image: /images/2026-01-14-codex-config-toml-approval-sandbox/hero.svg
  overlay_filter: 0.45
  image_description: >
    AI agent CLI setup guide image for Codex, Claude Code, permissions, and verification workflow.
excerpt: >
  `~/.codex/config.toml`의 approval과 sandbox 설정은 에이전트가 언제 멈추고 어떤 파일·명령에 접근할지 정한다.
seo_description: >
  `~/.codex/config.toml`의 approval과 sandbox 설정은 에이전트가 언제 멈추고 어떤 파일·명령에 접근할지 정한다.
categories:
  - ko_AI_Trends
tags:
  - config.toml
  - Codex CLI
  - Sandbox
  - Permissions
---
2026년 5월 24일 기준 공식 문서와 CLI 동작을 기준으로, 이 글은 **Codex config.toml approval_policy and sandbox_mode 설정 가이드**에서 먼저 확인할 설정과 실패 지점을 정리합니다. 핵심 판단은 처음에는 승인 요청이 가능한 상호작용 모드와 작업공간 쓰기 범위로 시작하고, 자동화는 테스트가 안정된 뒤에만 좁은 프로필로 분리합니다.

## 빠른 답

처음에는 승인 요청이 가능한 상호작용 모드와 작업공간 쓰기 범위로 시작하고, 자동화는 테스트가 안정된 뒤에만 좁은 프로필로 분리합니다.

실무 원칙은 단순합니다. 에이전트 권한은 작업 범위보다 좁아야 합니다. 설치, 설정, MCP 도구, 저장소 지침은 일회성 준비가 아니라 코드 품질을 지키는 운영 장치로 봐야 합니다.

![Codex config.toml approval_policy and sandbox_mode 설정 가이드 workflow diagram](/images/2026-01-14-codex-config-toml-approval-sandbox/hero.svg)

## 언제 중요한가

`~/.codex/config.toml`의 approval과 sandbox 설정은 에이전트가 언제 멈추고 어떤 파일·명령에 접근할지 정한다. 이 설정은 긴 프롬프트 하나로 모든 일을 맡기려는 상황보다, 반복 가능한 AI agent 작업 흐름을 만들 때 중요합니다. 좋은 설정은 세 가지를 분명히 합니다. agent가 읽어도 되는 것, 바꿔도 되는 것, 사람이 검증할 방법입니다.

팀에 도입한다면 넓게 쓰기 전에 결정을 문서화하세요. 어떤 계정이나 인증 방식을 쓸지, 어느 디렉터리에서 시작할지, 어떤 파일은 건드리면 안 되는지, 어떤 명령이 통과 기준인지 먼저 정해야 합니다.

## 기본 명령

```bash
mkdir -p ~/.codex
codex --profile safe-edit "Explain the current repository structure."
```

명령은 agent가 실제로 작업할 같은 셸과 프로젝트 루트에서 실행하세요. 어떤 터미널에서는 되고 다른 터미널에서는 안 된다면, 코드 수정 전에 PATH, 셸, 계정, 현재 디렉터리 문제를 먼저 해결해야 합니다.

## 설정 패턴

```text
model = "gpt-5.5-codex"
approval_policy = "on-request"
sandbox_mode = "workspace-write"

[profiles.safe-edit]
approval_policy = "on-request"
sandbox_mode = "workspace-write"
```

이 블록은 그대로 복사할 정답이 아니라 시작 패턴입니다. 개인 노트북, 회사 보안 장비, CI 작업은 같은 권한 모델을 쓰면 안 됩니다. 저장소 테스트와 롤백 경로가 분명해질 때까지는 읽기 전용 또는 계획 모드가 안전합니다.

반복해서 쓸 설정이라면 저장소 옆에 짧은 운영 메모를 남기세요. CLI 버전, 선택한 permission mode, 실제로 로드된 지침 파일, 마지막 검증 명령을 함께 적어두면 팀원이 다른 결과를 봤을 때 기준선을 빠르게 맞출 수 있습니다.

## 검증 체크리스트

- confirm writes stay inside the repo.
- require approval for network or privileged commands.
- record the profile used in PR notes.

설정이 동작하면 바로 편집을 맡기지 말고 먼저 읽기 전용 요약을 요청하세요. 그다음 좁은 계획을 요청합니다. 두 응답이 저장소 현실과 맞을 때만 파일 수정이나 외부 도구 호출을 허용하는 편이 안전합니다.

## 흔한 실수

- using full access for exploratory prompts.
- forgetting which profile is active.
- treating sandboxing as a substitute for review.

비싼 실수는 대개 모델 답변 하나가 틀린 것이 아니라 운영 경계가 모호한 것입니다. 인증, MCP scope, 설정 우선순위, 지침 파일이 불명확하면 세션은 생산적으로 보이지만 위험은 코드 리뷰 단계로 밀려납니다.

## 자주 묻는 질문

### 전역 설정과 프로젝트 설정 중 어디에 둬야 하나요?

개인 취향은 전역에 두고, 저장소 규칙은 프로젝트 파일에 둡니다. 그래야 팀원과 이후 세션이 같은 제약을 봅니다. 비밀값, 개인 로컬 경로, 실험 설정은 커밋되는 프로젝트 파일에 넣지 않습니다.

### 언제 agent에게 파일 수정을 허용해야 하나요?

agent가 작업 목표, 수정할 파일, 검증 명령을 먼저 정확히 말할 수 있을 때 허용합니다. 낯선 저장소에서는 계획 모드나 읽기 전용 검토부터 시작하세요.

### 설정이 끝난 뒤 무엇을 기록해야 하나요?

설치 방식, 버전 확인, 계정 또는 API 키 정책, permission mode, 지침 파일 위치, MCP scope, 첫 검증 명령을 기록합니다. 그래야 다음 세션도 같은 기준에서 시작할 수 있습니다.

## Source Notes

- [OpenAI Codex Configuration Reference](https://developers.openai.com/codex/config-reference)
- [OpenAI Codex CLI GitHub README](https://github.com/openai/codex)

## 관련 글

- [AI Agent Workflow 2026: 자동화보다 검증 게이트 먼저 설계하기](/ko_ai_trends/ai-agent-workflow-2026/)
- [AI Coding Agent Workflow: 코드 품질을 잃지 않는 에이전트 사용법](/ko_ai_trends/ai-coding-agent-workflow/)
