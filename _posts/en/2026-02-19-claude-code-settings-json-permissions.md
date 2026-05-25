---
layout: single
title: >
  Claude Code settings.json Permissions: allow, ask, and deny Defaults
seo_title: >
  Claude Code settings.json Permissions: allow, ask, and deny Defaults
date: 2026-02-19T09:21:00+09:00
last_modified_at: 2026-05-24T09:30:00+09:00
lang: en
translation_id: ai-agent-cli-claude-code-settings-json-permissions
header:
  teaser: /images/2026-02-19-claude-code-settings-json-permissions/hero.svg
  overlay_image: /images/2026-02-19-claude-code-settings-json-permissions/hero.svg
  overlay_filter: 0.45
  image_description: >
    AI agent CLI setup guide image for Codex, Claude Code, permissions, and verification workflow.
excerpt: >
  Claude Code `settings.json` is the main hierarchical file for permissions, environment variables, and tool behavior.
seo_description: >
  Claude Code `settings.json` is the main hierarchical file for permissions, environment variables, and tool behavior.
categories:
  - en_AI_Trends
tags:
  - Claude Code
  - settings.json
  - Permissions
  - AI Security
---
Checked against official documentation on May 24, 2026, this post focuses on the setup and failure points behind **Claude Code settings.json Permissions: allow, ask, and deny Defaults**. The practical baseline is: Put team rules in `.claude/settings.json`, personal overrides in `.claude/settings.local.json`, and global defaults in `~/.claude/settings.json`.

## Quick Answer

Put team rules in `.claude/settings.json`, personal overrides in `.claude/settings.local.json`, and global defaults in `~/.claude/settings.json`.

The practical rule is simple: keep the agent's authority narrower than the task. Installation, settings, MCP tools, and repository instructions should be treated as part of the engineering system, not as one-time setup trivia.

![Claude Code settings.json Permissions: allow, ask, and deny Defaults workflow diagram](/images/2026-02-19-claude-code-settings-json-permissions/hero.svg)

## When This Setup Matters

Claude Code `settings.json` is the main hierarchical file for permissions, environment variables, and tool behavior. This matters when a developer wants repeatable AI-agent help instead of a long ad hoc prompt. A good setup makes three things visible: what the agent may read, what it may change, and how the human will verify the result.

If the tool is being introduced to a team, write the decision down before broad use. Name the account or authentication path, the directory where the agent should start, the files it must not touch, and the command that proves a change is acceptable.

## Baseline Commands

```bash
mkdir -p .claude
claude --permission-mode plan
claude --settings .claude/settings.json
```

Run commands from the same shell and project root where the agent will work. If a command succeeds in one terminal but fails in another, fix the shell, PATH, account, or working-directory issue before asking the agent to edit code.

## Configuration Pattern

```text
{
  "permissions": {
    "allow": ["Bash(npm test)", "Bash(git diff:*)"],
    "ask": ["Bash(git push:*)"],
    "deny": ["Read(./.env)", "Read(./secrets/**)"]
  }
}
```

Treat this block as a starting pattern, not a universal default. A personal laptop, a locked-down company workstation, and a CI job should not have the same permission model. Prefer read-only or planning modes until the repository's tests and rollback path are clear.

For recurring use, keep a short setup note beside the repository. Include the CLI version, the selected permission mode, the instruction file that loaded, and the exact command used for the final verification. That note becomes the baseline when a teammate reports different behavior.

## Verification Checklist

- Deny secrets before enabling broad tools.
- Keep project settings reviewable.
- Use local settings for personal shortcuts.

After the setup works, ask the agent for a read-only summary first. Then ask for a narrow plan. Only after those two responses match the repository reality should you allow edits or tool calls that can change files.

## Common Mistakes

- Committing personal preferences.
- Allowing destructive shell patterns.
- Forgetting managed settings can override local rules.

The costly mistake is usually not a bad model answer; it is an unclear operating boundary. If authentication, MCP scope, settings precedence, or instruction files are ambiguous, the session can appear productive while quietly moving risk into code review.

## FAQ

### Should this be configured globally or per project?

Put personal preferences globally, but put repository rules in project files so every teammate and future session sees the same constraints. Secrets, local paths, and experiments should stay out of committed project files.

### When should I allow the agent to edit files?

Allow edits only after the agent can restate the task, name the files it expects to touch, and identify the verification command. For unfamiliar repositories, start in planning or read-only mode.

### What should I record after the setup works?

Record the install method, version check, account or API-key policy, permission mode, instruction file location, MCP scope, and the first verification command. This gives the next session a reproducible baseline.

## Professional Depth Check

For **Claude Code settings.json Permissions: allow, ask, and deny Defaults**, the practical standard is not whether the reader can repeat one instruction once. Treat the topic as an AI governance and workflow decision: verify task boundary, evaluation data, human review trigger, and cost and latency budget before drawing a conclusion. The result should be written as a small decision record, because future readers need to know which fact was observed, which assumption was used, and which condition would change the answer.

### Evidence That Makes the Guidance Reliable

Use objective evidence before changing a workflow. Good evidence includes eval results, sample prompts, tool traces, and failure examples. If two pieces of evidence conflict, keep the conflict visible instead of smoothing it over. For example, a successful quick fix is still weak evidence if the same input, account, dependency, or device state has not been tested again. A durable article should help the reader distinguish a confirmed fix from a plausible fix.

### Review Table

| Review Item | What To Confirm | Why It Matters |
| --- | --- | --- |
| Scope | The exact case covered by this article | Prevents over-applying the advice |
| Baseline | The state before any change | Makes rollback and comparison possible |
| Change | The smallest action taken | Reduces hidden side effects |
| Result | The observed output after the change | Separates evidence from expectation |
| Recheck | When to revisit the conclusion | Keeps the post accurate over time |

## Source Notes

- [Claude Code Settings](https://code.claude.com/docs/en/settings)
- [Claude Code CLI Reference](https://code.claude.com/docs/en/cli-usage)

## Related Reading

- [AI Agent Workflow 2026: Design Verification Before Automation](/en_ai_trends/ai-agent-workflow-2026/)
- [AI Coding Agent Workflow: Use Agents Without Losing Code Quality](/en_ai_trends/ai-coding-agent-workflow/)
