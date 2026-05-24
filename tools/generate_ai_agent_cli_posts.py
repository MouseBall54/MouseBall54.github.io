#!/usr/bin/env python3
"""Generate paired AI agent CLI setup posts with local SVG images."""

from __future__ import annotations

import html
from datetime import date, datetime, timedelta
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parents[1]
LAST_MODIFIED_AT = "2026-05-24T09:30:00+09:00"
KO_CATEGORY = "ko_AI_Trends"
EN_CATEGORY = "en_AI_Trends"
CHECKED_ON_KO = "2026년 5월 24일"
CHECKED_ON_EN = "May 24, 2026"


SOURCES = {
    "codex_readme": {
        "label": "OpenAI Codex CLI GitHub README",
        "url": "https://github.com/openai/codex",
    },
    "codex_agents": {
        "label": "OpenAI Codex AGENTS.md Guide",
        "url": "https://developers.openai.com/codex/guides/agents-md",
    },
    "codex_config": {
        "label": "OpenAI Codex Configuration Reference",
        "url": "https://developers.openai.com/codex/config-reference",
    },
    "claude_install": {
        "label": "Claude Code Installation Guide",
        "url": "https://code.claude.com/docs/en/installation",
    },
    "claude_cli": {
        "label": "Claude Code CLI Reference",
        "url": "https://code.claude.com/docs/en/cli-usage",
    },
    "claude_settings": {
        "label": "Claude Code Settings",
        "url": "https://code.claude.com/docs/en/settings",
    },
    "claude_mcp": {
        "label": "Claude Code MCP Guide",
        "url": "https://code.claude.com/docs/en/mcp",
    },
    "claude_memory": {
        "label": "Claude Code Memory Guide",
        "url": "https://code.claude.com/docs/en/memory",
    },
}


TOPICS = [
    {
        "slug": "codex-cli-install-login-setup",
        "ko_title": "Codex CLI install and login setup: 설치, 로그인, 버전 확인 순서",
        "en_title": "Codex CLI Install and Login Setup: Install, Sign In, and Verify",
        "ko_summary": "Codex CLI는 설치 방식, 로그인 방식, 실행 위치를 먼저 정해야 프로젝트별 에이전트 작업이 안정된다.",
        "en_summary": "Codex CLI is most reliable when installation method, sign-in method, and launch directory are fixed first.",
        "ko_answer": "Mac/Linux는 공식 설치 스크립트나 npm/Homebrew 중 하나를 선택하고, Windows는 PowerShell 설치 또는 npm을 사용한 뒤 `codex` 실행, 로그인, 버전 확인을 같은 터미널에서 끝냅니다.",
        "en_answer": "Choose one official install path, run `codex` from the project terminal, sign in, and verify the binary before asking the agent to edit files.",
        "commands": [
            "curl -fsSL https://chatgpt.com/codex/install.sh | sh",
            "npm install -g @openai/codex",
            "brew install --cask codex",
            "codex",
        ],
        "config": "Keep one installation path per machine; remove stale npm or manual binaries before debugging PATH issues.",
        "checks": ["run `codex` in a repository root", "confirm the expected account or API key path", "ask for a read-only project summary first"],
        "mistakes": ["mixing npm and native binaries", "starting outside the Git root", "letting the first prompt make broad edits"],
        "sources": ["codex_readme", "codex_config"],
        "tags": ["Codex CLI", "AI Agents", "Developer Setup", "OpenAI"],
    },
    {
        "slug": "codex-agents-md-project-instructions",
        "ko_title": "Codex AGENTS.md 설정: 프로젝트 지침을 에이전트가 읽게 만드는 법",
        "en_title": "Codex AGENTS.md Setup: Make Project Instructions Load Correctly",
        "ko_summary": "`AGENTS.md`는 Codex가 저장소 규칙, 테스트 명령, 금지 작업을 시작 시 읽는 가장 중요한 프로젝트 지침 파일이다.",
        "en_summary": "`AGENTS.md` is the project instruction file Codex reads for repository rules, test commands, and forbidden actions.",
        "ko_answer": "저장소 루트에는 공통 규칙을, 하위 디렉터리에는 더 좁은 규칙을 둡니다. 임시로 강제해야 하는 규칙은 `AGENTS.override.md`를 사용하고 작업 후 제거합니다.",
        "en_answer": "Put shared rules in the repository root, narrower rules near specialized folders, and temporary overrides in `AGENTS.override.md` only while needed.",
        "commands": [
            "mkdir -p ~/.codex",
            "printf '# Working agreements\\n- Run tests before commit.\\n' > ~/.codex/AGENTS.md",
            "codex --ask-for-approval never \"List the instruction sources you loaded.\"",
        ],
        "config": "project_doc_fallback_filenames = [\"TEAM_GUIDE.md\", \".agents.md\"]\nproject_doc_max_bytes = 65536",
        "checks": ["ask Codex to list loaded instruction files", "verify root rules appear before nested overrides", "keep secrets out of instruction files"],
        "mistakes": ["duplicating contradictory rules", "putting credentials in AGENTS.md", "forgetting to remove AGENTS.override.md"],
        "sources": ["codex_agents", "codex_config"],
        "tags": ["AGENTS.md", "Codex CLI", "Project Rules", "AI Workflow"],
    },
    {
        "slug": "codex-config-toml-approval-sandbox",
        "ko_title": "Codex config.toml approval_policy and sandbox_mode 설정 가이드",
        "en_title": "Codex config.toml approval_policy and sandbox_mode Setup Guide",
        "ko_summary": "`~/.codex/config.toml`의 approval과 sandbox 설정은 에이전트가 언제 멈추고 어떤 파일·명령에 접근할지 정한다.",
        "en_summary": "`~/.codex/config.toml` approval and sandbox settings decide when Codex pauses and what commands or files it can touch.",
        "ko_answer": "처음에는 승인 요청이 가능한 상호작용 모드와 작업공간 쓰기 범위로 시작하고, 자동화는 테스트가 안정된 뒤에만 좁은 프로필로 분리합니다.",
        "en_answer": "Start with interactive approvals and workspace-limited writes, then create narrower profiles only after tests and review rules are stable.",
        "commands": [
            "mkdir -p ~/.codex",
            "codex --profile safe-edit \"Explain the current repository structure.\"",
        ],
        "config": "model = \"gpt-5.5-codex\"\napproval_policy = \"on-request\"\nsandbox_mode = \"workspace-write\"\n\n[profiles.safe-edit]\napproval_policy = \"on-request\"\nsandbox_mode = \"workspace-write\"",
        "checks": ["confirm writes stay inside the repo", "require approval for network or privileged commands", "record the profile used in PR notes"],
        "mistakes": ["using full access for exploratory prompts", "forgetting which profile is active", "treating sandboxing as a substitute for review"],
        "sources": ["codex_config", "codex_readme"],
        "tags": ["config.toml", "Codex CLI", "Sandbox", "Permissions"],
    },
    {
        "slug": "codex-mcp-server-config",
        "ko_title": "Codex MCP server config.toml 설정: mcp_servers와 도구 승인 분리",
        "en_title": "Codex MCP Server config.toml Setup: mcp_servers and Tool Approval",
        "ko_summary": "Codex MCP 설정은 서버 실행 명령, 환경변수, 노출 도구, 도구별 승인 방식을 분리해야 운영이 안전하다.",
        "en_summary": "Codex MCP setup should separate server command, environment variables, exposed tools, and per-tool approval behavior.",
        "ko_answer": "`[mcp_servers.<name>]`에 서버를 등록하되, `enabled_tools`, `disabled_tools`, `default_tools_approval_mode`로 처음부터 최소 권한을 둡니다.",
        "en_answer": "Register the server under `[mcp_servers.<name>]`, then limit tools with `enabled_tools`, `disabled_tools`, and default approval mode.",
        "commands": [
            "codex mcp add openaiDeveloperDocs --url https://developers.openai.com/mcp",
            "codex",
        ],
        "config": "[mcp_servers.docs]\ncommand = \"npx\"\nargs = [\"-y\", \"example-docs-mcp\"]\nenv = { CACHE_DIR = \"/tmp/docs-mcp\" }\nenv_vars = [\"DOCS_TOKEN\"]\nenabled_tools = [\"search\", \"open\"]\ndefault_tools_approval_mode = \"prompt\"",
        "checks": ["start with read-only tools", "move tokens to environment variables", "disable any tool that can mutate production data"],
        "mistakes": ["exposing every MCP tool by default", "committing tokens inside config.toml", "not setting timeouts for slow servers"],
        "sources": ["codex_config", "codex_readme"],
        "tags": ["MCP", "Codex CLI", "Tool Use", "AI Security"],
    },
    {
        "slug": "codex-api-key-vs-chatgpt-login",
        "ko_title": "Codex API key vs ChatGPT login: 팀 환경에서 인증 방식을 고르는 법",
        "en_title": "Codex API Key vs ChatGPT Login: Choose Auth for Team Workflows",
        "ko_summary": "Codex 인증은 개인 ChatGPT 로그인과 API 키 기반 사용 중 어떤 비용·권한·감사 모델을 쓸지 먼저 정해야 한다.",
        "en_summary": "Codex authentication should be chosen around cost ownership, permissions, and audit expectations, not convenience alone.",
        "ko_answer": "개인 실험은 ChatGPT 로그인으로 시작해도 되지만, 팀 자동화나 비용 추적이 필요한 작업은 API 키·조직 정책·환경변수 관리를 분리합니다.",
        "en_answer": "Use ChatGPT sign-in for personal interactive work, but prefer API-key governance for team automation, cost tracking, and policy control.",
        "commands": [
            "codex",
            "export OPENAI_API_KEY=\"sk-...\"",
            "codex \"Summarize the current repository without editing files.\"",
        ],
        "config": "Never commit API keys. Prefer shell profile, secret manager, or CI secret injection depending on where Codex runs.",
        "checks": ["confirm which account pays", "rotate keys after accidental exposure", "document whether the session may call network tools"],
        "mistakes": ["sharing personal login sessions", "putting API keys in AGENTS.md", "debugging model behavior without checking the auth path"],
        "sources": ["codex_readme", "codex_config"],
        "tags": ["Codex CLI", "API Keys", "Authentication", "OpenAI"],
    },
    {
        "slug": "codex-safe-git-workflow",
        "ko_title": "Codex safe Git workflow: 작은 diff, 테스트, 커밋 경계를 고정하기",
        "en_title": "Codex Safe Git Workflow: Small Diffs, Tests, and Commit Boundaries",
        "ko_summary": "Codex 작업은 Git 상태 확인, 작은 diff, 테스트 명령, 사람이 읽을 수 있는 커밋 경계가 있을 때 리뷰 비용이 줄어든다.",
        "en_summary": "Codex work is easier to review when Git state, diff size, tests, and commit boundaries are fixed before editing.",
        "ko_answer": "항상 `git status`와 테스트 명령을 먼저 알려주고, 한 번에 하나의 실패 조건만 고치게 하며, 생성된 diff를 사람이 설명할 수 있어야 합니다.",
        "en_answer": "Give Codex the current Git state and test command, ask for one failure condition, and require a human-readable diff explanation.",
        "commands": [
            "git status --short",
            "git diff --stat",
            "npm test",
            "codex \"Fix only the failing lint rule and show the verification command.\"",
        ],
        "config": "Add repository rules in AGENTS.md: never rewrite unrelated files, keep changes scoped, and list tests before commit.",
        "checks": ["compare diff against requested scope", "run the same command before and after", "commit only after reading changed files"],
        "mistakes": ["asking for broad refactors", "accepting generated tests without running them", "mixing unrelated cleanups with a fix"],
        "sources": ["codex_agents", "codex_config"],
        "tags": ["Codex CLI", "Git", "Code Review", "Testing"],
    },
    {
        "slug": "codex-large-repo-context-control",
        "ko_title": "Codex large repo context control: 큰 저장소에서 읽을 범위를 줄이는 법",
        "en_title": "Codex Large Repo Context Control: Narrow What the Agent Reads",
        "ko_summary": "대형 저장소에서 Codex를 쓸 때는 전체 탐색보다 관련 디렉터리, 테스트, 소유자 파일을 먼저 지정해야 한다.",
        "en_summary": "In large repositories, Codex needs a narrow reading path: relevant directories, tests, and ownership files before broad exploration.",
        "ko_answer": "`--cd`, 하위 `AGENTS.md`, 파일 목록, 금지 디렉터리 규칙을 함께 사용해 에이전트가 읽는 맥락을 줄입니다.",
        "en_answer": "Use launch directory, nested instruction files, explicit file lists, and deny rules to shrink the agent's working context.",
        "commands": [
            "codex --cd services/api \"Read only the auth module and propose a test plan.\"",
            "find services/api -maxdepth 2 -type f | sort | head",
        ],
        "config": "services/api/AGENTS.md should name the local test command, generated directories, and files that must not be edited.",
        "checks": ["ask for a file map before edits", "confirm generated or vendor directories are ignored", "prefer targeted tests over full-suite guesses"],
        "mistakes": ["starting from monorepo root for a small bug", "letting context include build output", "forgetting nested team conventions"],
        "sources": ["codex_agents", "codex_config"],
        "tags": ["Codex CLI", "Monorepo", "Context", "Developer Workflow"],
    },
    {
        "slug": "codex-noninteractive-ci-checklist",
        "ko_title": "Codex non-interactive CI checklist: 자동 실행 전에 막아야 할 위험",
        "en_title": "Codex Non-Interactive CI Checklist: Risks to Block Before Automation",
        "ko_summary": "Codex를 CI나 스크립트에서 쓰려면 승인 정책, 샌드박스, 네트워크, 시크릿 노출, 산출물 검증을 먼저 고정해야 한다.",
        "en_summary": "Before using Codex in scripts or CI, fix approval policy, sandboxing, network access, secret exposure, and output validation.",
        "ko_answer": "비대화형 실행은 사람이 즉시 멈출 수 없으므로 읽기 전용 검토, 제한된 테스트, 명시적 출력 파일처럼 실패 범위가 작은 작업부터 시작합니다.",
        "en_answer": "Start non-interactive use with read-only review, limited tests, and explicit output files because no one can interrupt a bad action quickly.",
        "commands": [
            "codex \"Review this diff and return only risk notes.\"",
            "git diff --name-only origin/main...HEAD",
        ],
        "config": "[profiles.ci-review]\napproval_policy = \"never\"\nsandbox_mode = \"read-only\"",
        "checks": ["no write access for first CI use", "no production secrets in the environment", "fail the job if output is empty or malformed"],
        "mistakes": ["letting CI agents push directly", "passing all environment variables through", "treating AI review as a required approval"],
        "sources": ["codex_config", "codex_agents"],
        "tags": ["Codex CLI", "CI", "Automation", "AI Safety"],
    },
    {
        "slug": "codex-command-not-found-path",
        "ko_title": "codex command not found 해결: PATH, 설치 위치, 중복 바이너리 점검",
        "en_title": "Fix codex Command Not Found: PATH, Install Location, and Duplicate Binaries",
        "ko_summary": "`codex: command not found`는 설치 실패보다 PATH 미반영, 다른 셸, 중복 설치, 권한 문제인 경우가 많다.",
        "en_summary": "`codex: command not found` is often a PATH, shell, duplicate install, or permission issue rather than a failed install.",
        "ko_answer": "설치 직후 새 터미널을 열고 `which codex`, `command -v codex`, 설치 관리자별 위치를 확인한 뒤 한 가지 설치 방식만 남깁니다.",
        "en_answer": "Open a fresh terminal, check `which codex` or `command -v codex`, verify the installer path, and keep only one install method.",
        "commands": [
            "command -v codex",
            "which codex",
            "npm list -g @openai/codex --depth=0",
            "brew list --cask codex",
        ],
        "config": "If multiple paths return different binaries, remove the older install and reopen the shell before testing again.",
        "checks": ["same shell used for install and run", "PATH contains the installer target", "version output changes after update"],
        "mistakes": ["testing in an old terminal tab", "installing with sudo then running as a normal user", "mixing WSL and Windows PATH assumptions"],
        "sources": ["codex_readme", "codex_config"],
        "tags": ["Codex CLI", "PATH", "Troubleshooting", "Install Error"],
    },
    {
        "slug": "codex-windows-wsl-setup",
        "ko_title": "Codex Windows WSL setup: PowerShell, WSL, Git 경로를 나눠 쓰는 법",
        "en_title": "Codex Windows WSL Setup: Separate PowerShell, WSL, and Git Paths",
        "ko_summary": "Windows에서 Codex를 쓸 때는 PowerShell 프로젝트와 WSL 프로젝트를 섞지 말고 설치 위치와 Git 루트를 분리해야 한다.",
        "en_summary": "On Windows, Codex works best when PowerShell projects and WSL projects keep separate installs, paths, and Git roots.",
        "ko_answer": "Windows 네이티브 프로젝트는 PowerShell 설치를, Linux 도구체인 프로젝트는 WSL 내부 설치를 사용하고 같은 저장소를 두 환경에서 동시에 수정하지 않습니다.",
        "en_answer": "Use native Windows install for Windows projects, WSL install for Linux toolchains, and avoid editing the same checkout from both environments.",
        "commands": [
            "powershell -ExecutionPolicy ByPass -c \"irm https://chatgpt.com/codex/install.ps1 | iex\"",
            "wsl",
            "curl -fsSL https://chatgpt.com/codex/install.sh | sh",
        ],
        "config": "Keep separate ~/.codex/config.toml files for Windows and WSL. Document which terminal owns each repository.",
        "checks": ["run `git status` in the same environment as Codex", "verify line endings before committing", "keep Node and package manager inside the chosen environment"],
        "mistakes": ["installing in Windows but launching inside WSL", "editing WSL files through slow mounted paths", "mixing CRLF rules without checking diff"],
        "sources": ["codex_readme", "codex_config"],
        "tags": ["Codex CLI", "Windows", "WSL", "Developer Setup"],
    },
    {
        "slug": "claude-code-install-login-doctor",
        "ko_title": "Claude Code install, login, doctor: 설치 후 바로 점검할 것",
        "en_title": "Claude Code Install, Login, and Doctor: First Verification Steps",
        "ko_summary": "Claude Code는 설치 후 `claude --version`, 로그인 상태, `claude doctor`를 확인해야 작업 실패 원인을 빨리 줄일 수 있다.",
        "en_summary": "After installing Claude Code, verify version, authentication, and `claude doctor` before asking it to edit a project.",
        "ko_answer": "공식 설치 방식으로 설치한 뒤 같은 터미널에서 버전, 로그인, doctor 결과를 확인하고 프로젝트 루트에서 첫 세션을 엽니다.",
        "en_answer": "Install from an official method, then verify version, login, and doctor output in the same terminal before starting project work.",
        "commands": [
            "curl -fsSL https://claude.ai/install.sh | bash",
            "claude --version",
            "claude auth status",
            "claude doctor",
        ],
        "config": "Use native install, Homebrew, WinGet, or npm deliberately. Do not debug a project until the CLI itself is healthy.",
        "checks": ["supported OS and shell", "account includes Claude Code access", "doctor output has no blocking install issue"],
        "mistakes": ["using a free plan that lacks access", "running in the wrong terminal after install", "skipping doctor and blaming the repository"],
        "sources": ["claude_install", "claude_cli"],
        "tags": ["Claude Code", "Install", "CLI", "Developer Setup"],
    },
    {
        "slug": "claude-code-settings-json-permissions",
        "ko_title": "Claude Code settings.json permissions: allow, ask, deny 기본값",
        "en_title": "Claude Code settings.json Permissions: allow, ask, and deny Defaults",
        "ko_summary": "Claude Code의 `settings.json`은 권한, 환경변수, 도구 동작을 계층적으로 제어하는 핵심 설정 파일이다.",
        "en_summary": "Claude Code `settings.json` is the main hierarchical file for permissions, environment variables, and tool behavior.",
        "ko_answer": "팀 공유 설정은 `.claude/settings.json`, 개인 실험은 `.claude/settings.local.json`, 전역 기본값은 `~/.claude/settings.json`에 나눠 둡니다.",
        "en_answer": "Put team rules in `.claude/settings.json`, personal overrides in `.claude/settings.local.json`, and global defaults in `~/.claude/settings.json`.",
        "commands": [
            "mkdir -p .claude",
            "claude --permission-mode plan",
            "claude --settings .claude/settings.json",
        ],
        "config": "{\n  \"permissions\": {\n    \"allow\": [\"Bash(npm test)\", \"Bash(git diff:*)\"],\n    \"ask\": [\"Bash(git push:*)\"],\n    \"deny\": [\"Read(./.env)\", \"Read(./secrets/**)\"]\n  }\n}",
        "checks": ["deny secrets before enabling broad tools", "keep project settings reviewable", "use local settings for personal shortcuts"],
        "mistakes": ["committing personal preferences", "allowing destructive shell patterns", "forgetting managed settings can override local rules"],
        "sources": ["claude_settings", "claude_cli"],
        "tags": ["Claude Code", "settings.json", "Permissions", "AI Security"],
    },
    {
        "slug": "claude-code-claude-md-memory",
        "ko_title": "Claude Code CLAUDE.md memory setup: 프로젝트 기억 파일 작성법",
        "en_title": "Claude Code CLAUDE.md Memory Setup: Write Useful Project Context",
        "ko_summary": "`CLAUDE.md`는 Claude Code가 프로젝트 규칙, 빌드 명령, 테스트 기준을 기억하게 하는 시작 문서다.",
        "en_summary": "`CLAUDE.md` gives Claude Code durable project context such as rules, build commands, and testing expectations.",
        "ko_answer": "`/init`으로 초안을 만들고, 사람이 아는 배포 규칙, 금지 작업, 테스트 기준, 리뷰 기준을 짧게 보강합니다.",
        "en_answer": "Use `/init` for a starter file, then add human-only knowledge: release rules, forbidden actions, test gates, and review expectations.",
        "commands": [
            "claude",
            "/init",
            "git diff -- CLAUDE.md",
        ],
        "config": "# CLAUDE.md\n\n## Build and test\n- Run npm test before committing.\n\n## Safety\n- Never edit .env files or rotate production keys.",
        "checks": ["keep the file short enough to stay useful", "include exact commands", "review changes to memory like code"],
        "mistakes": ["turning memory into a long wiki", "storing secrets", "adding rules that contradict settings.json"],
        "sources": ["claude_memory", "claude_settings"],
        "tags": ["CLAUDE.md", "Claude Code", "Project Memory", "AI Workflow"],
    },
    {
        "slug": "claude-code-mcp-project-scope",
        "ko_title": "Claude Code MCP project scope: .mcp.json을 팀과 공유하는 기준",
        "en_title": "Claude Code MCP Project Scope: When to Share .mcp.json with a Team",
        "ko_summary": "Claude Code MCP 서버는 local, project, user scope에 따라 저장 위치와 공유 범위가 달라진다.",
        "en_summary": "Claude Code MCP servers behave differently by local, project, and user scope, including storage location and sharing rules.",
        "ko_answer": "팀이 같은 도구를 써야 하면 project scope로 `.mcp.json`에 저장하고, 개인 토큰이나 실험 서버는 local 또는 user scope로 둡니다.",
        "en_answer": "Use project scope and `.mcp.json` for shared team tools; keep personal tokens and experimental servers in local or user scope.",
        "commands": [
            "claude mcp add --transport http paypal --scope project https://mcp.paypal.com/mcp",
            "claude mcp add --transport http stripe --scope local https://mcp.stripe.com",
            "claude mcp reset-project-choices",
        ],
        "config": "{\n  \"mcpServers\": {\n    \"shared-server\": {\n      \"command\": \"/path/to/server\",\n      \"args\": [],\n      \"env\": {}\n    }\n  }\n}",
        "checks": ["project servers contain no personal secrets", "new project MCP choices are reviewed", "duplicate server names have expected precedence"],
        "mistakes": ["committing local credentials", "using project scope for private experiments", "forgetting approval prompts for shared .mcp.json servers"],
        "sources": ["claude_mcp", "claude_settings"],
        "tags": ["Claude Code", "MCP", "Tools", "Team Workflow"],
    },
    {
        "slug": "claude-code-permission-modes",
        "ko_title": "Claude Code permission modes: plan, acceptEdits, auto, bypassPermissions 차이",
        "en_title": "Claude Code Permission Modes: plan, acceptEdits, auto, and bypassPermissions",
        "ko_summary": "Claude Code permission mode는 세션이 계획만 할지, 편집을 받을지, 자동 승인할지, 위험한 우회를 허용할지 정한다.",
        "en_summary": "Claude Code permission mode decides whether a session plans, accepts edits, auto-approves, or bypasses prompts.",
        "ko_answer": "새 저장소는 `plan`, 일반 수정은 `acceptEdits`, 자동 모드는 신뢰된 환경에서만 사용하고 `bypassPermissions`는 조직 정책으로 막는 것을 기본값으로 둡니다.",
        "en_answer": "Use `plan` for unfamiliar repos, `acceptEdits` for normal work, reserve `auto` for trusted setups, and disable bypass where policy matters.",
        "commands": [
            "claude --permission-mode plan",
            "claude --permission-mode acceptEdits",
            "claude --permission-mode auto",
        ],
        "config": "{\n  \"permissions\": {\n    \"defaultMode\": \"acceptEdits\",\n    \"disableBypassPermissionsMode\": \"disable\"\n  }\n}",
        "checks": ["start low-trust work in plan mode", "log mode changes in handoff notes", "deny secrets regardless of mode"],
        "mistakes": ["using bypass for convenience", "letting repositories set risky local defaults", "forgetting CLI flags override settings for one session"],
        "sources": ["claude_settings", "claude_cli"],
        "tags": ["Claude Code", "Permissions", "AI Safety", "Workflow"],
    },
    {
        "slug": "claude-code-background-agents",
        "ko_title": "Claude Code background agents: 병렬 작업을 안전하게 나누는 법",
        "en_title": "Claude Code Background Agents: Split Parallel Work Safely",
        "ko_summary": "Claude Code background agents는 병렬 세션을 볼 수 있지만 작업 범위, 권한, 로그 확인 없이 쓰면 충돌이 생긴다.",
        "en_summary": "Claude Code background agents help monitor parallel sessions, but they need scope, permission, and log boundaries.",
        "ko_answer": "`claude agents --json`으로 세션을 확인하고, 각 agent에는 서로 다른 디렉터리나 검증 작업을 맡기며 같은 파일을 동시에 수정하지 않게 합니다.",
        "en_answer": "Use `claude agents --json` to inspect sessions, assign separate directories or verification jobs, and avoid concurrent edits to the same files.",
        "commands": [
            "claude agents --json",
            "claude agents --cwd .",
            "claude logs <session-id>",
            "claude attach <session-id>",
        ],
        "config": "For dispatched sessions, pass explicit --cwd, --permission-mode, --model, or --effort instead of relying on memory.",
        "checks": ["one branch or worktree per editing agent", "clear owner for each task", "read logs before merging results"],
        "mistakes": ["parallel agents editing shared files", "losing session IDs", "treating background output as reviewed code"],
        "sources": ["claude_cli", "claude_settings"],
        "tags": ["Claude Code", "Background Agents", "Parallel Work", "Code Review"],
    },
    {
        "slug": "claude-code-vscode-terminal-setup",
        "ko_title": "Claude Code VS Code terminal setup: IDE와 CLI 작업 위치 맞추기",
        "en_title": "Claude Code VS Code Terminal Setup: Align IDE and CLI Working Directory",
        "ko_summary": "VS Code 터미널에서 Claude Code를 쓸 때는 열려 있는 workspace, 현재 디렉터리, Git 상태가 같은지 먼저 확인해야 한다.",
        "en_summary": "When using Claude Code from VS Code, verify workspace, current directory, and Git state before launching the agent.",
        "ko_answer": "VS Code의 통합 터미널에서 `pwd`, `git status`, 테스트 명령을 확인한 뒤 `claude`를 실행하고, IDE 확장 자동 설치 여부는 settings에서 통제합니다.",
        "en_answer": "From the integrated terminal, confirm `pwd`, `git status`, and test commands before launching `claude`; control IDE extension behavior in settings.",
        "commands": [
            "pwd",
            "git status --short",
            "claude",
            "claude -p \"Summarize this workspace without editing.\"",
        ],
        "config": "{\n  \"autoInstallIdeExtension\": false\n}",
        "checks": ["terminal path matches open folder", "selected interpreter or Node version matches tests", "agent output references the right workspace"],
        "mistakes": ["running Claude from home directory", "using a different checkout than VS Code shows", "letting IDE auto-install surprise team machines"],
        "sources": ["claude_settings", "claude_cli"],
        "tags": ["Claude Code", "VS Code", "Terminal", "Developer Setup"],
    },
    {
        "slug": "claude-code-sensitive-file-deny",
        "ko_title": "Claude Code sensitive file deny 설정: .env와 secrets 접근 차단",
        "en_title": "Claude Code Sensitive File Deny Setup: Block .env and secrets Access",
        "ko_summary": "Claude Code는 `.env`, credentials, build output, secret directories를 `permissions.deny`로 명시 차단해야 한다.",
        "en_summary": "Claude Code should explicitly block `.env`, credentials, build output, and secret directories with `permissions.deny`.",
        "ko_answer": "프로젝트 `.claude/settings.json`에 팀 공통 deny 규칙을 넣고, 개인 로컬 설정에는 더 좁은 민감 경로를 추가합니다.",
        "en_answer": "Put team-wide deny rules in project `.claude/settings.json`, then add stricter personal paths in local settings if needed.",
        "commands": [
            "mkdir -p .claude",
            "git diff -- .claude/settings.json",
            "claude --permission-mode plan",
        ],
        "config": "{\n  \"permissions\": {\n    \"deny\": [\n      \"Read(./.env)\",\n      \"Read(./.env.*)\",\n      \"Read(./secrets/**)\",\n      \"Read(./config/credentials.json)\",\n      \"Read(./build)\"\n    ]\n  }\n}",
        "checks": ["deny files before adding MCP tools", "review settings changes in PR", "rotate secrets if they were exposed to chat"],
        "mistakes": ["assuming .gitignore blocks agent reads", "putting sample secrets in prompts", "allowing build folders with embedded credentials"],
        "sources": ["claude_settings", "claude_mcp"],
        "tags": ["Claude Code", "Secrets", "Permissions", "AI Security"],
    },
    {
        "slug": "claude-code-print-json-automation",
        "ko_title": "Claude Code print JSON automation: claude -p 출력 자동화 기본",
        "en_title": "Claude Code Print JSON Automation: Basics of claude -p Output",
        "ko_summary": "`claude -p`는 파이프와 스크립트에서 빠르게 쓸 수 있지만 출력 형식, 권한, 입력 범위를 명확히 해야 한다.",
        "en_summary": "`claude -p` is useful in pipes and scripts, but output format, permissions, and input scope must be explicit.",
        "ko_answer": "자동화에서는 `claude -p`, `--output-format json`, 제한된 입력 파일, 낮은 권한 모드를 함께 사용해 결과를 검증 가능하게 만듭니다.",
        "en_answer": "For automation, combine `claude -p`, `--output-format json`, narrow input files, and low-permission modes so output is verifiable.",
        "commands": [
            "cat logs.txt | claude -p \"Summarize errors only\"",
            "claude -p \"Check this function\" --output-format json",
            "claude -c -p \"Check for type errors\"",
        ],
        "config": "Use --bare when scripted calls should skip memory, hooks, plugins, MCP servers, and CLAUDE.md discovery.",
        "checks": ["parse JSON before trusting it", "fail scripts on empty output", "keep prompt inputs deterministic"],
        "mistakes": ["letting scripts inherit broad project tools", "mixing conversational output with machine parsing", "feeding full logs with secrets"],
        "sources": ["claude_cli", "claude_settings"],
        "tags": ["Claude Code", "Automation", "JSON", "CLI"],
    },
    {
        "slug": "claude-code-update-version-pin",
        "ko_title": "Claude Code update and version pin: 안정 버전과 최신 버전 운영법",
        "en_title": "Claude Code Update and Version Pin: Stable vs Latest Operations",
        "ko_summary": "Claude Code는 자동 업데이트, 수동 업데이트, 특정 버전 설치 방식을 팀 정책에 맞게 정해야 재현성이 생긴다.",
        "en_summary": "Claude Code updates need a team policy for auto-update, manual update, and version pinning to keep behavior reproducible.",
        "ko_answer": "개인은 자동 업데이트를 써도 되지만 팀은 stable 채널, 특정 버전, 변경 로그 확인, `claude doctor` 재검증을 운영 절차로 둡니다.",
        "en_answer": "Individuals can auto-update, but teams should define stable channel, version pinning, changelog review, and post-update doctor checks.",
        "commands": [
            "claude update",
            "claude install stable",
            "claude install latest",
            "claude --version",
        ],
        "config": "{\n  \"env\": {\n    \"DISABLE_AUTOUPDATER\": \"1\"\n  }\n}",
        "checks": ["record version in bug reports", "rerun doctor after updates", "avoid `npm update -g` for npm installs"],
        "mistakes": ["debugging without version info", "mixing package-manager updates", "updating all teammates mid-incident"],
        "sources": ["claude_install", "claude_cli"],
        "tags": ["Claude Code", "Updates", "Version Pinning", "Operations"],
    },
    {
        "slug": "ai-agent-repo-instruction-file-template",
        "ko_title": "AI agent repo instruction file template: AGENTS.md와 CLAUDE.md 공통 구조",
        "en_title": "AI Agent Repo Instruction File Template: AGENTS.md and CLAUDE.md Structure",
        "ko_summary": "AI agent 지침 파일은 도구별 문법보다 빌드 명령, 테스트, 금지 경로, 커밋 규칙을 일관되게 담는 것이 중요하다.",
        "en_summary": "AI agent instruction files work best when build commands, tests, forbidden paths, and commit rules are consistent across tools.",
        "ko_answer": "Codex에는 `AGENTS.md`, Claude에는 `CLAUDE.md`를 쓰되 같은 저장소 원칙을 공유하고 도구별 설정 파일에는 권한과 환경만 둡니다.",
        "en_answer": "Use `AGENTS.md` for Codex and `CLAUDE.md` for Claude, but keep the same repository expectations in both and put permissions in settings files.",
        "commands": [
            "cp AGENTS.md CLAUDE.md",
            "git diff -- AGENTS.md CLAUDE.md",
            "codex \"List repo rules only.\"",
            "claude -p \"List repo rules only.\"",
        ],
        "config": "## Required sections\n- Setup commands\n- Test commands\n- Files never to edit\n- Commit and review rules\n- Definition of done",
        "checks": ["same test command in both files", "no secrets in either file", "tool-specific differences are explicit"],
        "mistakes": ["making tool instructions contradict each other", "hiding safety rules in prompts only", "letting generated instructions grow forever"],
        "sources": ["codex_agents", "claude_memory", "claude_settings"],
        "tags": ["AI Agents", "AGENTS.md", "CLAUDE.md", "Workflow"],
    },
    {
        "slug": "ai-agent-mcp-security-checklist",
        "ko_title": "AI agent MCP security checklist: 도구 연결 전 최소 권한 점검",
        "en_title": "AI Agent MCP Security Checklist: Least Privilege Before Tool Access",
        "ko_summary": "MCP는 에이전트에게 외부 도구를 연결하므로 서버 범위, 환경변수, 승인 모드, 도구 allowlist를 먼저 정해야 한다.",
        "en_summary": "MCP connects agents to external tools, so server scope, environment variables, approval mode, and tool allowlists must come first.",
        "ko_answer": "처음에는 읽기 전용 도구만 노출하고, 쓰기·배포·결제·데이터 삭제 도구는 별도 승인과 감사 로그가 있을 때만 허용합니다.",
        "en_answer": "Expose read-only tools first; allow write, deploy, billing, or deletion tools only with approval rules and audit logs.",
        "commands": [
            "claude mcp add --scope project --transport http docs https://example.com/mcp",
            "codex mcp add docs --url https://example.com/mcp",
        ],
        "config": "MCP review checklist: scope, command or URL, env vars, enabled tools, disabled tools, approval mode, timeout, owner.",
        "checks": ["separate project-shared and personal servers", "store tokens outside committed config", "test tool list before first task"],
        "mistakes": ["adding production write tools first", "sharing local tokens via project config", "forgetting duplicate MCP server precedence"],
        "sources": ["codex_config", "claude_mcp", "claude_settings"],
        "tags": ["MCP", "AI Agents", "Security", "Tool Use"],
    },
    {
        "slug": "ai-agent-test-first-task-brief",
        "ko_title": "AI agent test-first task brief: 실패 조건을 먼저 주는 프롬프트",
        "en_title": "AI Agent Test-First Task Brief: Give the Failure Condition First",
        "ko_summary": "AI agent에게 작업을 맡길 때는 원하는 코드보다 실패 조건, 재현 명령, 통과 기준을 먼저 주는 것이 안전하다.",
        "en_summary": "An AI agent is safer when it receives the failure condition, reproduction command, and pass criteria before desired code.",
        "ko_answer": "프롬프트는 문제, 재현 명령, 수정 범위, 금지 파일, 검증 명령, 보고 형식 순서로 작성합니다.",
        "en_answer": "Write the prompt in this order: problem, reproduce command, allowed scope, forbidden files, verification command, and report format.",
        "commands": [
            "npm test -- --runInBand failing.test.ts",
            "git diff --stat",
            "codex \"Fix only this failing test; do not refactor unrelated files.\"",
        ],
        "config": "Task brief template: symptom, command, expected result, allowed files, denied files, tests, final summary.",
        "checks": ["one failure per task", "agent reports exact test command", "reviewer can reproduce before merging"],
        "mistakes": ["asking for a broad improvement", "not naming forbidden files", "accepting a fix without a failing-before passing-after check"],
        "sources": ["codex_agents", "claude_memory"],
        "tags": ["AI Agents", "Testing", "Prompting", "Code Quality"],
    },
    {
        "slug": "ai-agent-commit-boundary-prompt",
        "ko_title": "AI agent commit boundary prompt: 리뷰 가능한 변경 단위로 쪼개기",
        "en_title": "AI Agent Commit Boundary Prompt: Split Work into Reviewable Changes",
        "ko_summary": "AI agent 작업은 커밋 경계를 프롬프트에 넣어야 기능 수정, 테스트, 문서 변경이 한 diff에 섞이지 않는다.",
        "en_summary": "AI agent work needs commit boundaries in the prompt so feature changes, tests, and docs do not blend into one unreadable diff.",
        "ko_answer": "작업 전 산출물 단위를 정하고, 에이전트가 각 단위별 변경 파일, 테스트, 위험을 요약하게 합니다.",
        "en_answer": "Define output units before editing and ask the agent to summarize files, tests, and risks for each unit.",
        "commands": [
            "git status --short",
            "git add -p",
            "git commit -m \"fix: handle empty auth token\"",
        ],
        "config": "Commit boundary: one behavior change, one verification command, one rollback path, no opportunistic cleanup.",
        "checks": ["diff stat matches one intent", "docs changes explain behavior not style", "commit message states user-visible effect"],
        "mistakes": ["combining formatting with logic", "letting agent stage everything", "reviewing only the final summary"],
        "sources": ["codex_agents", "claude_memory"],
        "tags": ["AI Agents", "Git", "Code Review", "Commits"],
    },
    {
        "slug": "ai-agent-env-secret-hygiene",
        "ko_title": "AI agent env and secret hygiene: 환경변수와 키 노출을 줄이는 법",
        "en_title": "AI Agent Env and Secret Hygiene: Reduce Environment Variable Exposure",
        "ko_summary": "AI agent 세션에는 필요한 환경변수만 전달하고 `.env`, credential, token 로그를 읽지 못하게 막아야 한다.",
        "en_summary": "AI agent sessions should receive only required environment variables and must be blocked from `.env`, credentials, and token logs.",
        "ko_answer": "키는 셸·CI·secret manager에서 주입하고, 에이전트 설정에는 deny 규칙과 env allowlist를 둡니다.",
        "en_answer": "Inject keys from shell, CI, or a secret manager, and keep deny rules plus environment allowlists in agent configuration.",
        "commands": [
            "env | sort | rg 'KEY|TOKEN|SECRET'",
            "git ls-files | rg '(^|/)\\.env'",
            "claude --permission-mode plan",
        ],
        "config": "Deny patterns: .env, .env.*, secrets/**, credentials.json, production logs, exported shell history.",
        "checks": ["redact logs before prompts", "rotate leaked keys", "never ask the agent to print full environment"],
        "mistakes": ["pasting tokens into chat", "letting MCP inherit every env var", "assuming local files are invisible to tools"],
        "sources": ["claude_settings", "codex_config", "claude_mcp"],
        "tags": ["AI Agents", "Secrets", "Environment", "Security"],
    },
    {
        "slug": "ai-agent-review-log-template",
        "ko_title": "AI agent review log template: 사람이 검토할 기록을 남기는 법",
        "en_title": "AI Agent Review Log Template: Leave Evidence Humans Can Check",
        "ko_summary": "AI agent가 만든 변경은 요청, 변경 파일, 테스트, 실패, 미확인 위험을 한 기록으로 남겨야 신뢰가 생긴다.",
        "en_summary": "AI agent changes become trustworthy when request, files changed, tests, failures, and unresolved risks are recorded together.",
        "ko_answer": "작업 종료 시 에이전트에게 변경 요약보다 검증 로그, 실행하지 못한 테스트, 사람이 볼 위험을 먼저 보고하게 합니다.",
        "en_answer": "At the end of work, ask for verification logs, tests not run, and human-review risks before a general summary.",
        "commands": [
            "git diff --stat",
            "git diff --check",
            "npm test",
        ],
        "config": "Review log fields: request, touched files, commands run, command output summary, skipped checks, residual risks.",
        "checks": ["logs match shell history", "skipped tests are explicit", "risks map to actual files"],
        "mistakes": ["accepting confident prose without commands", "hiding failed checks", "not recording why scope changed"],
        "sources": ["codex_agents", "claude_memory"],
        "tags": ["AI Agents", "Review", "Verification", "Workflow"],
    },
    {
        "slug": "ai-agent-browser-tool-verification",
        "ko_title": "AI agent browser tool verification: UI 변경을 눈으로 확인하는 순서",
        "en_title": "AI Agent Browser Tool Verification: Check UI Changes Visually",
        "ko_summary": "AI agent가 프론트엔드를 수정했다면 빌드 통과만으로 충분하지 않고 브라우저 렌더링, 콘솔, 네트워크를 확인해야 한다.",
        "en_summary": "For frontend changes, build success is not enough; an agent should verify rendered UI, console, and network behavior.",
        "ko_answer": "개발 서버를 띄운 뒤 주요 경로, 콘솔 오류, 네트워크 404, 모바일 폭, 핵심 CTA를 체크리스트로 확인합니다.",
        "en_answer": "Run the dev server and verify key routes, console errors, network 404s, mobile width, and primary calls to action.",
        "commands": [
            "npm run build",
            "npm run dev",
            "git diff -- assets css src",
        ],
        "config": "Browser verification checklist: route loads, heading exists, no console errors, no missing assets, mobile layout usable.",
        "checks": ["test at least one real page", "capture console warnings separately from errors", "verify analytics or ad scripts do not break layout"],
        "mistakes": ["trusting screenshots alone", "checking only localhost root", "ignoring broken font or favicon requests"],
        "sources": ["codex_agents", "claude_cli"],
        "tags": ["AI Agents", "Frontend", "Browser Testing", "Verification"],
    },
    {
        "slug": "ai-agent-token-context-budgeting",
        "ko_title": "AI agent token context budgeting: 큰 작업을 잘라서 맡기는 법",
        "en_title": "AI Agent Token Context Budgeting: Split Large Work Before Context Fails",
        "ko_summary": "AI agent는 큰 작업을 한 번에 주면 오래된 맥락을 잃거나 자동 요약에 의존하므로 단계별 예산이 필요하다.",
        "en_summary": "Large AI-agent tasks need context budgeting because long sessions can lose old details or depend on automatic summaries.",
        "ko_answer": "탐색, 설계, 구현, 검증, 커밋을 분리하고 각 단계마다 입력 파일과 산출물을 명시합니다.",
        "en_answer": "Split discovery, design, implementation, verification, and commit into separate phases with explicit inputs and outputs.",
        "commands": [
            "rg --files | wc -l",
            "git diff --stat",
            "codex \"Inspect only these three files and propose a plan.\"",
        ],
        "config": "Context budget: files allowed, files forbidden, max diff size, stop condition, summary handoff format.",
        "checks": ["agent can restate the current goal", "old assumptions are revalidated", "handoff summary names exact files"],
        "mistakes": ["feeding the whole repository", "continuing after goal drift", "not resetting when the task changes"],
        "sources": ["codex_config", "claude_settings", "claude_memory"],
        "tags": ["AI Agents", "Context", "Planning", "Productivity"],
    },
    {
        "slug": "ai-agent-debug-loop-playbook",
        "ko_title": "AI agent debug loop playbook: 실패 로그에서 수정까지 반복하는 법",
        "en_title": "AI Agent Debug Loop Playbook: From Failure Log to Verified Fix",
        "ko_summary": "AI agent 디버깅은 로그 붙여넣기보다 재현 명령, 최소 실패, 가설, 한 번의 변경, 재검증 루프가 중요하다.",
        "en_summary": "AI-agent debugging works best with reproduce command, minimal failure, hypothesis, one change, and re-verification loop.",
        "ko_answer": "각 반복은 실패 증거 하나, 원인 가설 하나, 변경 하나, 검증 명령 하나로 제한합니다.",
        "en_answer": "Limit each loop to one failure artifact, one hypothesis, one change, and one verification command.",
        "commands": [
            "npm test 2>&1 | tee /tmp/test.log",
            "rg -n \"ERROR|FAILED|Traceback\" /tmp/test.log",
            "git diff --check",
        ],
        "config": "Debug loop: observe, isolate, hypothesize, patch, verify, record. Stop after repeated failures and ask for human review.",
        "checks": ["same failure reproduced before edit", "new failure is not hidden", "agent records what changed between attempts"],
        "mistakes": ["changing many files per attempt", "ignoring the first error", "rerunning different commands each time"],
        "sources": ["codex_agents", "claude_cli"],
        "tags": ["AI Agents", "Debugging", "Testing", "Workflow"],
    },
    {
        "slug": "ai-agent-human-approval-gates",
        "ko_title": "AI agent human approval gates: 자동화 전에 사람이 멈춰야 할 지점",
        "en_title": "AI Agent Human Approval Gates: Where Automation Must Pause",
        "ko_summary": "AI agent는 배포, 결제, 데이터 삭제, 권한 변경, 외부 발송 같은 행동 전에 사람 승인 게이트가 필요하다.",
        "en_summary": "AI agents need human approval gates before deploys, billing, data deletion, permission changes, or external messages.",
        "ko_answer": "승인 게이트는 도구 권한보다 업무 위험 기준으로 설계하고, 승인자·증거·되돌리기 경로를 함께 기록합니다.",
        "en_answer": "Design approval gates by business risk rather than tool name, and record approver, evidence, and rollback path.",
        "commands": [
            "git diff --stat",
            "npm run test",
            "gh pr create --draft",
        ],
        "config": "Approval matrix: read allowed, draft allowed, write asks, deploy asks, delete denied, production secrets denied.",
        "checks": ["approval is required before irreversible actions", "rollback command is known", "human sees the actual diff or payload"],
        "mistakes": ["approving categories too broadly", "letting auto mode deploy", "not logging why an approval was granted"],
        "sources": ["codex_config", "claude_settings", "claude_cli"],
        "tags": ["AI Agents", "Approvals", "Automation", "Governance"],
    },
]


def post_dates() -> list[str]:
    start = date(2026, 1, 6)
    return [(start + timedelta(days=index * 4)).isoformat() for index in range(len(TOPICS))]


def make_svg(title: str, subtitle: str, accent: str) -> str:
    safe_title = html.escape(title)
    safe_subtitle = html.escape(subtitle)
    safe_accent = html.escape(accent)
    return dedent(
        f"""\
        <svg xmlns="http://www.w3.org/2000/svg" width="1400" height="760" viewBox="0 0 1400 760" role="img" aria-labelledby="title desc">
          <title id="title">{safe_title}</title>
          <desc id="desc">{safe_subtitle}</desc>
          <defs>
            <linearGradient id="bg" x1="0" x2="1" y1="0" y2="1">
              <stop offset="0%" stop-color="#fffdf7"/>
              <stop offset="58%" stop-color="#eef6fa"/>
              <stop offset="100%" stop-color="#f4ead9"/>
            </linearGradient>
            <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
              <feDropShadow dx="0" dy="24" stdDeviation="26" flood-color="#172033" flood-opacity="0.16"/>
            </filter>
          </defs>
          <rect width="1400" height="760" fill="url(#bg)"/>
          <circle cx="1150" cy="120" r="210" fill="#b78a3c" opacity="0.18"/>
          <circle cx="180" cy="650" r="260" fill="#1f5f8b" opacity="0.14"/>
          <g filter="url(#shadow)">
            <rect x="110" y="120" width="1180" height="520" rx="42" fill="#fffdf7" opacity="0.94"/>
          </g>
          <text x="165" y="210" fill="#b78a3c" font-family="Noto Sans KR, Arial, sans-serif" font-size="30" font-weight="800" letter-spacing="4">{safe_accent}</text>
          <foreignObject x="160" y="245" width="870" height="210">
            <div xmlns="http://www.w3.org/1999/xhtml" style="font-family: 'Noto Sans KR', Arial, sans-serif; color:#172033; font-size:58px; line-height:1.08; font-weight:800; letter-spacing:-1.6px;">{safe_title}</div>
          </foreignObject>
          <foreignObject x="165" y="480" width="780" height="100">
            <div xmlns="http://www.w3.org/1999/xhtml" style="font-family: 'Noto Sans KR', Arial, sans-serif; color:#667085; font-size:28px; line-height:1.35; font-weight:500;">{safe_subtitle}</div>
          </foreignObject>
          <g transform="translate(990 255)">
            <rect x="0" y="0" width="210" height="260" rx="30" fill="#143d59"/>
            <rect x="34" y="48" width="142" height="18" rx="9" fill="#fffdf7" opacity="0.84"/>
            <rect x="34" y="92" width="112" height="18" rx="9" fill="#fffdf7" opacity="0.62"/>
            <rect x="34" y="136" width="138" height="18" rx="9" fill="#fffdf7" opacity="0.74"/>
            <path d="M54 206 L94 226 L160 184" fill="none" stroke="#b78a3c" stroke-width="15" stroke-linecap="round" stroke-linejoin="round"/>
          </g>
        </svg>
        """
    )


def yaml_list(values: list[str]) -> str:
    return "\n".join(f"- {value}" for value in values)


def indent_text(value: str, prefix: str) -> str:
    return "\n".join(f"{prefix}{line}" if line else line for line in value.splitlines())


def block(value: str) -> str:
    return "\n".join(line[1:] if line.startswith("|") else line for line in value.splitlines()).strip() + "\n"


def source_notes(topic: dict[str, object]) -> str:
    return "\n".join(f"- [{SOURCES[key]['label']}]({SOURCES[key]['url']})" for key in topic["sources"])


def command_block(commands: list[str]) -> str:
    return "\n".join(commands)


def front_matter(topic: dict[str, object], lang: str, current_date: str, minute: int, image_path: str) -> str:
    title = topic[f"{lang}_title"]
    summary = topic[f"{lang}_summary"]
    category = KO_CATEGORY if lang == "ko" else EN_CATEGORY
    description = summary
    tags = indent_text(yaml_list(topic["tags"]), "  ")
    return block(
        f"""\
|---
|layout: single
|title: >
|  {title}
|seo_title: >
|  {title[:68]}
|date: {current_date}T09:{minute:02d}:00+09:00
|last_modified_at: {LAST_MODIFIED_AT}
|lang: {lang}
|translation_id: ai-agent-cli-{topic["slug"]}
|header:
|  teaser: {image_path}
|  overlay_image: {image_path}
|  overlay_filter: 0.45
|  image_description: >
|    AI agent CLI setup guide image for Codex, Claude Code, permissions, and verification workflow.
|excerpt: >
|  {summary}
|seo_description: >
|  {description}
|categories:
|  - {category}
|tags:
{tags}
|---
"""
    )


def render_en(topic: dict[str, object], current_date: str, minute: int) -> str:
    image_path = f"/images/{current_date}-{topic['slug']}/hero.svg"
    commands = command_block(topic["commands"])
    checks = "\n".join(f"- {item.capitalize()}." for item in topic["checks"])
    mistakes = "\n".join(f"- {item.capitalize()}." for item in topic["mistakes"])
    return front_matter(topic, "en", current_date, minute, image_path) + block(
        f"""\
|This guide is checked against official documentation on {CHECKED_ON_EN}. CLI behavior changes, so verify the version and linked source notes before copying a setting into a production workflow.
|
|## Quick Answer
|
|{topic["en_answer"]}
|
|The practical rule is simple: keep the agent's authority narrower than the task. Installation, settings, MCP tools, and repository instructions should be treated as part of the engineering system, not as one-time setup trivia.
|
|![{topic["en_title"]} workflow diagram]({image_path})
|
|## When This Setup Matters
|
|{topic["en_summary"]} This matters when a developer wants repeatable AI-agent help instead of a long ad hoc prompt. A good setup makes three things visible: what the agent may read, what it may change, and how the human will verify the result.
|
|If the tool is being introduced to a team, write the decision down before broad use. Name the account or authentication path, the directory where the agent should start, the files it must not touch, and the command that proves a change is acceptable.
|
|## Baseline Commands
|
|```bash
|{commands}
|```
|
|Run commands from the same shell and project root where the agent will work. If a command succeeds in one terminal but fails in another, fix the shell, PATH, account, or working-directory issue before asking the agent to edit code.
|
|## Configuration Pattern
|
|```text
|{topic["config"]}
|```
|
|Treat this block as a starting pattern, not a universal default. A personal laptop, a locked-down company workstation, and a CI job should not have the same permission model. Prefer read-only or planning modes until the repository's tests and rollback path are clear.
|
|For recurring use, keep a short setup note beside the repository. Include the CLI version, the selected permission mode, the instruction file that loaded, and the exact command used for the final verification. That note becomes the baseline when a teammate reports different behavior.
|
|## Verification Checklist
|
|{checks}
|
|After the setup works, ask the agent for a read-only summary first. Then ask for a narrow plan. Only after those two responses match the repository reality should you allow edits or tool calls that can change files.
|
|## Common Mistakes
|
|{mistakes}
|
|The costly mistake is usually not a bad model answer; it is an unclear operating boundary. If authentication, MCP scope, settings precedence, or instruction files are ambiguous, the session can appear productive while quietly moving risk into code review.
|
|## FAQ
|
|### Should this be configured globally or per project?
|
|Put personal preferences globally, but put repository rules in project files so every teammate and future session sees the same constraints. Secrets, local paths, and experiments should stay out of committed project files.
|
|### When should I allow the agent to edit files?
|
|Allow edits only after the agent can restate the task, name the files it expects to touch, and identify the verification command. For unfamiliar repositories, start in planning or read-only mode.
|
|### What should I record after the setup works?
|
|Record the install method, version check, account or API-key policy, permission mode, instruction file location, MCP scope, and the first verification command. This gives the next session a reproducible baseline.
|
|## Source Notes
|
|{source_notes(topic)}
|
|## Related Reading
|
|- [AI Agent Workflow 2026: Design Verification Before Automation](/en_ai_trends/ai-agent-workflow-2026/)
|- [AI Coding Agent Workflow: Use Agents Without Losing Code Quality](/en_ai_trends/ai-coding-agent-workflow/)
"""
    )


def render_ko(topic: dict[str, object], current_date: str, minute: int) -> str:
    image_path = f"/images/{current_date}-{topic['slug']}/hero.svg"
    commands = command_block(topic["commands"])
    checks = "\n".join(f"- {item}." for item in topic["checks"])
    mistakes = "\n".join(f"- {item}." for item in topic["mistakes"])
    return front_matter(topic, "ko", current_date, minute, image_path) + block(
        f"""\
|이 글은 {CHECKED_ON_KO} 기준 공식 문서를 확인해 작성했습니다. CLI 도구는 업데이트가 빠르므로 운영 환경에 복사하기 전 버전과 하단의 Source Notes를 다시 확인하세요.
|
|## 빠른 답
|
|{topic["ko_answer"]}
|
|실무 원칙은 단순합니다. 에이전트 권한은 작업 범위보다 좁아야 합니다. 설치, 설정, MCP 도구, 저장소 지침은 일회성 준비가 아니라 코드 품질을 지키는 운영 장치로 봐야 합니다.
|
|![{topic["ko_title"]} workflow diagram]({image_path})
|
|## 언제 중요한가
|
|{topic["ko_summary"]} 이 설정은 긴 프롬프트 하나로 모든 일을 맡기려는 상황보다, 반복 가능한 AI agent 작업 흐름을 만들 때 중요합니다. 좋은 설정은 세 가지를 분명히 합니다. agent가 읽어도 되는 것, 바꿔도 되는 것, 사람이 검증할 방법입니다.
|
|팀에 도입한다면 넓게 쓰기 전에 결정을 문서화하세요. 어떤 계정이나 인증 방식을 쓸지, 어느 디렉터리에서 시작할지, 어떤 파일은 건드리면 안 되는지, 어떤 명령이 통과 기준인지 먼저 정해야 합니다.
|
|## 기본 명령
|
|```bash
|{commands}
|```
|
|명령은 agent가 실제로 작업할 같은 셸과 프로젝트 루트에서 실행하세요. 어떤 터미널에서는 되고 다른 터미널에서는 안 된다면, 코드 수정 전에 PATH, 셸, 계정, 현재 디렉터리 문제를 먼저 해결해야 합니다.
|
|## 설정 패턴
|
|```text
|{topic["config"]}
|```
|
|이 블록은 그대로 복사할 정답이 아니라 시작 패턴입니다. 개인 노트북, 회사 보안 장비, CI 작업은 같은 권한 모델을 쓰면 안 됩니다. 저장소 테스트와 롤백 경로가 분명해질 때까지는 읽기 전용 또는 계획 모드가 안전합니다.
|
|반복해서 쓸 설정이라면 저장소 옆에 짧은 운영 메모를 남기세요. CLI 버전, 선택한 permission mode, 실제로 로드된 지침 파일, 마지막 검증 명령을 함께 적어두면 팀원이 다른 결과를 봤을 때 기준선을 빠르게 맞출 수 있습니다.
|
|## 검증 체크리스트
|
|{checks}
|
|설정이 동작하면 바로 편집을 맡기지 말고 먼저 읽기 전용 요약을 요청하세요. 그다음 좁은 계획을 요청합니다. 두 응답이 저장소 현실과 맞을 때만 파일 수정이나 외부 도구 호출을 허용하는 편이 안전합니다.
|
|## 흔한 실수
|
|{mistakes}
|
|비싼 실수는 대개 모델 답변 하나가 틀린 것이 아니라 운영 경계가 모호한 것입니다. 인증, MCP scope, 설정 우선순위, 지침 파일이 불명확하면 세션은 생산적으로 보이지만 위험은 코드 리뷰 단계로 밀려납니다.
|
|## 자주 묻는 질문
|
|### 전역 설정과 프로젝트 설정 중 어디에 둬야 하나요?
|
|개인 취향은 전역에 두고, 저장소 규칙은 프로젝트 파일에 둡니다. 그래야 팀원과 이후 세션이 같은 제약을 봅니다. 비밀값, 개인 로컬 경로, 실험 설정은 커밋되는 프로젝트 파일에 넣지 않습니다.
|
|### 언제 agent에게 파일 수정을 허용해야 하나요?
|
|agent가 작업 목표, 수정할 파일, 검증 명령을 먼저 정확히 말할 수 있을 때 허용합니다. 낯선 저장소에서는 계획 모드나 읽기 전용 검토부터 시작하세요.
|
|### 설정이 끝난 뒤 무엇을 기록해야 하나요?
|
|설치 방식, 버전 확인, 계정 또는 API 키 정책, permission mode, 지침 파일 위치, MCP scope, 첫 검증 명령을 기록합니다. 그래야 다음 세션도 같은 기준에서 시작할 수 있습니다.
|
|## Source Notes
|
|{source_notes(topic)}
|
|## 관련 글
|
|- [AI Agent Workflow 2026: 자동화보다 검증 게이트 먼저 설계하기](/ko_ai_trends/ai-agent-workflow-2026/)
|- [AI Coding Agent Workflow: 코드 품질을 잃지 않는 에이전트 사용법](/ko_ai_trends/ai-coding-agent-workflow/)
"""
    )


def write_post(lang: str, topic: dict[str, object], current_date: str, minute: int) -> None:
    relative = ROOT / "_posts" / lang / f"{current_date}-{topic['slug']}.md"
    content = render_ko(topic, current_date, minute) if lang == "ko" else render_en(topic, current_date, minute)
    relative.write_text(content, encoding="utf-8")


def write_image(topic: dict[str, object], current_date: str) -> None:
    image_dir = ROOT / "images" / f"{current_date}-{topic['slug']}"
    image_dir.mkdir(parents=True, exist_ok=True)
    svg = make_svg(topic["en_title"], topic["en_summary"], "AI AGENT CLI")
    (image_dir / "hero.svg").write_text(svg, encoding="utf-8")


def main() -> None:
    dates = post_dates()
    for index, topic in enumerate(TOPICS):
        current_date = dates[index]
        minute = 10 + (index % 45)
        write_image(topic, current_date)
        write_post("ko", topic, current_date, minute)
        write_post("en", topic, current_date, minute)

    print(f"Generated {len(TOPICS) * 2} paired AI agent CLI posts.")


if __name__ == "__main__":
    main()
