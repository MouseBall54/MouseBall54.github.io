---
layout: single
title: >
  Codex MCP Server config.toml Setup: mcp_servers and Tool Approval
seo_title: >
  Codex MCP Server config.toml Setup: mcp_servers and Tool Approval
date: 2026-01-18T09:13:00+09:00
last_modified_at: 2026-05-24T09:30:00+09:00
lang: en
translation_id: ai-agent-cli-codex-mcp-server-config
header:
  teaser: /images/2026-01-18-codex-mcp-server-config/hero.svg
  overlay_image: /images/2026-01-18-codex-mcp-server-config/hero.svg
  overlay_filter: 0.45
  image_description: >
    AI agent CLI setup guide image for Codex, Claude Code, permissions, and verification workflow.
excerpt: >
  Codex MCP setup should separate server command, environment variables, exposed tools, and per-tool approval behavior.
seo_description: >
  Codex MCP setup should separate server command, environment variables, exposed tools, and per-tool approval behavior.
categories:
  - en_AI_Trends
tags:
  - MCP
  - Codex CLI
  - Tool Use
  - AI Security
---
Checked against official documentation on May 24, 2026, this post focuses on the setup and failure points behind **Codex MCP Server config.toml Setup: mcp_servers and Tool Approval**. The practical baseline is: Register the server under `[mcp_servers.<name>]`, then limit tools with `enabled_tools`, `disabled_tools`, and default approval mode.

## Quick Answer

Register the server under `[mcp_servers.<name>]`, then limit tools with `enabled_tools`, `disabled_tools`, and default approval mode.

The practical rule is simple: keep the agent's authority narrower than the task. Installation, settings, MCP tools, and repository instructions should be treated as part of the engineering system, not as one-time setup trivia.

![Codex MCP Server config.toml Setup: mcp_servers and Tool Approval workflow diagram](/images/2026-01-18-codex-mcp-server-config/hero.svg)

## When This Setup Matters

Codex MCP setup should separate server command, environment variables, exposed tools, and per-tool approval behavior. This matters when a developer wants repeatable AI-agent help instead of a long ad hoc prompt. A good setup makes three things visible: what the agent may read, what it may change, and how the human will verify the result.

If the tool is being introduced to a team, write the decision down before broad use. Name the account or authentication path, the directory where the agent should start, the files it must not touch, and the command that proves a change is acceptable.

## Baseline Commands

```bash
codex mcp add openaiDeveloperDocs --url https://developers.openai.com/mcp
codex
```

Run commands from the same shell and project root where the agent will work. If a command succeeds in one terminal but fails in another, fix the shell, PATH, account, or working-directory issue before asking the agent to edit code.

## Configuration Pattern

```text
[mcp_servers.docs]
command = "npx"
args = ["-y", "example-docs-mcp"]
env = { CACHE_DIR = "/tmp/docs-mcp" }
env_vars = ["DOCS_TOKEN"]
enabled_tools = ["search", "open"]
default_tools_approval_mode = "prompt"
```

Treat this block as a starting pattern, not a universal default. A personal laptop, a locked-down company workstation, and a CI job should not have the same permission model. Prefer read-only or planning modes until the repository's tests and rollback path are clear.

For recurring use, keep a short setup note beside the repository. Include the CLI version, the selected permission mode, the instruction file that loaded, and the exact command used for the final verification. That note becomes the baseline when a teammate reports different behavior.

## Verification Checklist

- Start with read-only tools.
- Move tokens to environment variables.
- Disable any tool that can mutate production data.

After the setup works, ask the agent for a read-only summary first. Then ask for a narrow plan. Only after those two responses match the repository reality should you allow edits or tool calls that can change files.

## Common Mistakes

- Exposing every mcp tool by default.
- Committing tokens inside config.toml.
- Not setting timeouts for slow servers.

The costly mistake is usually not a bad model answer; it is an unclear operating boundary. If authentication, MCP scope, settings precedence, or instruction files are ambiguous, the session can appear productive while quietly moving risk into code review.

## FAQ

### Should this be configured globally or per project?

Put personal preferences globally, but put repository rules in project files so every teammate and future session sees the same constraints. Secrets, local paths, and experiments should stay out of committed project files.

### When should I allow the agent to edit files?

Allow edits only after the agent can restate the task, name the files it expects to touch, and identify the verification command. For unfamiliar repositories, start in planning or read-only mode.

### What should I record after the setup works?

Record the install method, version check, account or API-key policy, permission mode, instruction file location, MCP scope, and the first verification command. This gives the next session a reproducible baseline.

## Source Notes

- [OpenAI Codex Configuration Reference](https://developers.openai.com/codex/config-reference)
- [OpenAI Codex CLI GitHub README](https://github.com/openai/codex)

## Related Reading

- [AI Agent Workflow 2026: Design Verification Before Automation](/en_ai_trends/ai-agent-workflow-2026/)
- [AI Coding Agent Workflow: Use Agents Without Losing Code Quality](/en_ai_trends/ai-coding-agent-workflow/)
