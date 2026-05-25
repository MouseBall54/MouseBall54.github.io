---
layout: single
title: >
  Claude Code settings.json permissions: allow, ask, deny 기본값
seo_title: >
  Claude Code settings.json permissions: allow, ask, deny 기본값
date: 2026-02-19T09:21:00+09:00
last_modified_at: 2026-05-24T09:30:00+09:00
lang: ko
translation_id: ai-agent-cli-claude-code-settings-json-permissions
header:
  teaser: /images/2026-02-19-claude-code-settings-json-permissions/hero.svg
  overlay_image: /images/2026-02-19-claude-code-settings-json-permissions/hero.svg
  overlay_filter: 0.45
  image_description: >
    AI agent CLI setup guide image for Codex, Claude Code, permissions, and verification workflow.
excerpt: >
  Claude Code의 `settings.json`은 권한, 환경변수, 도구 동작을 계층적으로 제어하는 핵심 설정 파일이다.
seo_description: >
  Claude Code의 `settings.json`은 권한, 환경변수, 도구 동작을 계층적으로 제어하는 핵심 설정 파일이다.
categories:
  - ko_AI_Trends
tags:
  - Claude Code
  - settings.json
  - Permissions
  - AI Security
---
2026년 5월 24일 기준 공식 문서와 CLI 동작을 기준으로, 이 글은 **Claude Code settings.json permissions: allow, ask, deny 기본값**에서 먼저 확인할 설정과 실패 지점을 정리합니다. 핵심 판단은 팀 공유 설정은 `.claude/settings.json`, 개인 실험은 `.claude/settings.local.json`, 전역 기본값은 `~/.claude/settings.json`에 나눠 둡니다.

## 빠른 답

팀 공유 설정은 `.claude/settings.json`, 개인 실험은 `.claude/settings.local.json`, 전역 기본값은 `~/.claude/settings.json`에 나눠 둡니다.

실무 원칙은 단순합니다. 에이전트 권한은 작업 범위보다 좁아야 합니다. 설치, 설정, MCP 도구, 저장소 지침은 일회성 준비가 아니라 코드 품질을 지키는 운영 장치로 봐야 합니다.

![Claude Code settings.json permissions: allow, ask, deny 기본값 workflow diagram](/images/2026-02-19-claude-code-settings-json-permissions/hero.svg)

## 언제 중요한가

Claude Code의 `settings.json`은 권한, 환경변수, 도구 동작을 계층적으로 제어하는 핵심 설정 파일이다. 이 설정은 긴 프롬프트 하나로 모든 일을 맡기려는 상황보다, 반복 가능한 AI agent 작업 흐름을 만들 때 중요합니다. 좋은 설정은 세 가지를 분명히 합니다. agent가 읽어도 되는 것, 바꿔도 되는 것, 사람이 검증할 방법입니다.

팀에 도입한다면 넓게 쓰기 전에 결정을 문서화하세요. 어떤 계정이나 인증 방식을 쓸지, 어느 디렉터리에서 시작할지, 어떤 파일은 건드리면 안 되는지, 어떤 명령이 통과 기준인지 먼저 정해야 합니다.

## 기본 명령

```bash
mkdir -p .claude
claude --permission-mode plan
claude --settings .claude/settings.json
```

명령은 agent가 실제로 작업할 같은 셸과 프로젝트 루트에서 실행하세요. 어떤 터미널에서는 되고 다른 터미널에서는 안 된다면, 코드 수정 전에 PATH, 셸, 계정, 현재 디렉터리 문제를 먼저 해결해야 합니다.

## 설정 패턴

```text
{
  "permissions": {
    "allow": ["Bash(npm test)", "Bash(git diff:*)"],
    "ask": ["Bash(git push:*)"],
    "deny": ["Read(./.env)", "Read(./secrets/**)"]
  }
}
```

이 블록은 그대로 복사할 정답이 아니라 시작 패턴입니다. 개인 노트북, 회사 보안 장비, CI 작업은 같은 권한 모델을 쓰면 안 됩니다. 저장소 테스트와 롤백 경로가 분명해질 때까지는 읽기 전용 또는 계획 모드가 안전합니다.

반복해서 쓸 설정이라면 저장소 옆에 짧은 운영 메모를 남기세요. CLI 버전, 선택한 permission mode, 실제로 로드된 지침 파일, 마지막 검증 명령을 함께 적어두면 팀원이 다른 결과를 봤을 때 기준선을 빠르게 맞출 수 있습니다.

## 검증 체크리스트

- deny secrets before enabling broad tools.
- keep project settings reviewable.
- use local settings for personal shortcuts.

설정이 동작하면 바로 편집을 맡기지 말고 먼저 읽기 전용 요약을 요청하세요. 그다음 좁은 계획을 요청합니다. 두 응답이 저장소 현실과 맞을 때만 파일 수정이나 외부 도구 호출을 허용하는 편이 안전합니다.

## 흔한 실수

- committing personal preferences.
- allowing destructive shell patterns.
- forgetting managed settings can override local rules.

비싼 실수는 대개 모델 답변 하나가 틀린 것이 아니라 운영 경계가 모호한 것입니다. 인증, MCP scope, 설정 우선순위, 지침 파일이 불명확하면 세션은 생산적으로 보이지만 위험은 코드 리뷰 단계로 밀려납니다.

## 자주 묻는 질문

### 전역 설정과 프로젝트 설정 중 어디에 둬야 하나요?

개인 취향은 전역에 두고, 저장소 규칙은 프로젝트 파일에 둡니다. 그래야 팀원과 이후 세션이 같은 제약을 봅니다. 비밀값, 개인 로컬 경로, 실험 설정은 커밋되는 프로젝트 파일에 넣지 않습니다.

### 언제 agent에게 파일 수정을 허용해야 하나요?

agent가 작업 목표, 수정할 파일, 검증 명령을 먼저 정확히 말할 수 있을 때 허용합니다. 낯선 저장소에서는 계획 모드나 읽기 전용 검토부터 시작하세요.

### 설정이 끝난 뒤 무엇을 기록해야 하나요?

설치 방식, 버전 확인, 계정 또는 API 키 정책, permission mode, 지침 파일 위치, MCP scope, 첫 검증 명령을 기록합니다. 그래야 다음 세션도 같은 기준에서 시작할 수 있습니다.

## 전문 보완 체크

**Claude Code settings.json permissions: allow, ask, deny 기본값**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 AI 거버넌스와 워크플로 의사결정로 다루는 편이 안전합니다. 결론을 내리기 전에 작업 경계, 평가 데이터, 사람 검토 조건, 비용과 지연시간 예산를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

### 신뢰도를 높이는 증거

작업을 바꾸기 전에는 객관적인 증거를 먼저 확인해야 합니다. 쓸 만한 증거에는 평가 결과, 샘플 프롬프트, 도구 실행 기록, 실패 사례가 포함됩니다. 증거가 서로 맞지 않으면 억지로 하나의 이야기로 합치지 말고 충돌 자체를 남겨야 합니다. 빠른 해결이 한 번 성공했더라도 같은 입력, 계정, 의존성, 기기 상태에서 다시 확인하지 않았다면 아직 확정된 해결책이라고 보기 어렵습니다.

### 검토 표

| 검토 항목 | 확인할 내용 | 중요한 이유 |
| --- | --- | --- |
| 범위 | 이 글이 다루는 정확한 사례 | 조언을 과도하게 적용하지 않게 합니다 |
| 기준 상태 | 변경 전 상태 | 되돌리기와 비교를 가능하게 합니다 |
| 변경 | 실제로 수행한 가장 작은 조치 | 숨은 부작용을 줄입니다 |
| 결과 | 변경 뒤 관찰한 출력 또는 반응 | 기대와 증거를 구분합니다 |
| 재확인 | 결론을 다시 볼 시점 | 글의 정확도를 유지합니다 |

### 예외 상황과 실패 모드

주요 위험은 실패 사례를 모으기 전에 자동화하는 상황, 벤더 주장으로 내부 측정을 대체하는 상황입니다. 생산 데이터, 개인정보, 돈, 건강, 법적 권리, 보안 복구가 관련되어 있다면 넓은 해결책을 바로 적용하기보다 먼저 증거를 모으는 보수적인 접근이 낫습니다. 같은 제목의 문제라도 환경이 다르면 원인이 달라질 수 있으므로, 독자는 명령이나 결정을 복사하기 전에 자신의 조건이 글의 가정과 맞는지 비교해야 합니다.

### 유지보수 기준

이 안내는 모델, 프롬프트, 도구 권한, 데이터 소스가 바뀔 때 다시 확인해야 합니다. 좋은 업데이트는 글 전체를 다시 쓰는 것이 아니라 예시, 링크, 명령, 화면, 판단 기준이 현재 동작과 여전히 맞는지 확인하는 일입니다. 기존 결론이 유효하면 확인 날짜를 남기고, 바뀌었다면 무엇이 바뀌었고 왜 이전 조언만으로 부족한지 설명해야 합니다.

### 실행 전 질문

- 문제나 판단이 실제임을 보여 주는 가장 작은 관찰 신호는 무엇인가?
- 공식 출처는 무엇이고, 내부 판단은 어느 부분인가?
- 변경 전에 반드시 캡처해야 할 기록은 무엇인가?
- 어떤 결과가 나오면 이 글의 조언이 맞지 않는다고 볼 것인가?
- 같은 문제가 반복될 때 누가 이 기록을 다시 봐야 하는가?

## Source Notes

- [Claude Code Settings](https://code.claude.com/docs/en/settings)
- [Claude Code CLI Reference](https://code.claude.com/docs/en/cli-usage)

## 관련 글

- [AI Agent Workflow 2026: 자동화보다 검증 게이트 먼저 설계하기](/ko_ai_trends/ai-agent-workflow-2026/)
- [AI Coding Agent Workflow: 코드 품질을 잃지 않는 에이전트 사용법](/ko_ai_trends/ai-coding-agent-workflow/)
