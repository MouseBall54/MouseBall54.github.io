---
typora-root-url: ../
layout: single
title: >
  How to Fix GitHub Actions Build Failed
seo_title: >
  How to Fix GitHub Actions Build Failed
date: 2026-05-23T19:00:00+09:00
lang: en
translation_id: github-actions-build-failed
header:
   teaser: /images/2026-05-23-github-actions-build-failed/github-actions-build-failed-hero.png
   overlay_image: /images/2026-05-23-github-actions-build-failed/github-actions-build-failed-hero.png
   overlay_filter: 0.5
excerpt: >
  Fix GitHub Actions build failed errors by reading the failed step log, checking workflow YAML, dependency install commands, runner versions, secrets, and branch triggers.
seo_description: >
  Fix GitHub Actions build failed errors by reading the failed step log, checking workflow YAML, dependency install commands, runner versions, secrets, and branch triggers.
categories:
  - en_Troubleshooting
tags:
  - GitHubActions
  - CI
  - GitHub
  - Build
---

## Problem

A pull request or push shows a failed GitHub Actions check:

![How to Fix GitHub Actions Build Failed explanatory image](/images/2026-05-23-github-actions-build-failed/github-actions-build-failed-hero.png)

```text
build failed
Process completed with exit code 1
```

or:

```text
The workflow is not valid
```

The fix depends on where the failure happened.
Do not start by editing random YAML.
Open the failed workflow run, find the failed job, and read the first failed step.

## Cause

GitHub Actions builds usually fail for one of these reasons:

- The workflow file has invalid YAML or is in the wrong path.
- The workflow trigger does not match the branch or event.
- Dependencies were not installed before the build step.
- The CI runner uses a different Node, Python, Java, or Ruby version.
- A secret or environment variable is missing.
- A test, lint, typecheck, or build command really failed.
- A cache restored stale dependencies.
- The deploy step has insufficient permissions.

GitHub workflow files must be stored under `.github/workflows` and use `.yml` or `.yaml`.
If the file itself is invalid, every new commit can create a failed workflow run until the YAML is fixed.

## Quick Diagnosis

Open the failing run:

1. Go to the repository on GitHub.
2. Open the **Actions** tab.
3. Select the failed workflow.
4. Open the failed run.
5. Click the failed job.
6. Expand the failed step and read the first real error.

If you use GitHub CLI, check recent runs:

```bash
gh run list
gh run view --log
```

Search the log for:

```text
Error:
failed
exit code
not found
permission
```

The useful error is often above `Process completed with exit code 1`.

## Step-by-Step Fix

### 1. Fix Invalid Workflow YAML

A valid workflow file should be under:

```text
.github/workflows/ci.yml
```

Basic example:

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Show working directory
        run: pwd
```

Check for:

- tabs instead of spaces
- wrong indentation
- missing colon
- duplicate keys
- file saved outside `.github/workflows`
- unsupported expression syntax

YAML errors must be fixed before package or test errors matter.

### 2. Confirm the Trigger

If the workflow does not run when expected, check `on`.

This only runs on pushes to `main`:

```yaml
on:
  push:
    branches: [main]
```

If you are testing in a feature branch, add `pull_request` or include that branch.

```yaml
on:
  push:
  pull_request:
```

If `paths` or `paths-ignore` is configured, the workflow may skip changes outside those paths.

### 3. Match Runtime Versions

CI often fails because the runner version differs from local development.

Node example:

```yaml
- uses: actions/setup-node@v4
  with:
    node-version: 20
    cache: npm

- run: npm ci
- run: npm run build
```

Python example:

```yaml
- uses: actions/setup-python@v5
  with:
    python-version: "3.12"

- run: python -m pip install -r requirements.txt
- run: pytest
```

Use the same version as `.nvmrc`, `.python-version`, `package.json`, `pyproject.toml`, or project documentation.

### 4. Use the Right Install Command

Use lockfile-aware commands in CI.

For npm projects:

```yaml
- run: npm ci
- run: npm test
- run: npm run build
```

For pnpm:

```yaml
- uses: pnpm/action-setup@v4
- run: pnpm install --frozen-lockfile
- run: pnpm build
```

For Bundler:

```yaml
- run: bundle install
- run: bundle exec jekyll build --trace
```

If the log says `command not found`, install the tool or use the setup action before running it.

### 5. Check Secrets and Permissions

If the log mentions authentication, token, or permission errors, check repository secrets and workflow permissions.

Common symptoms:

```text
Context access might be invalid: SECRET_NAME
Resource not accessible by integration
Permission denied
```

Make sure the secret exists in:

```text
Settings > Secrets and variables > Actions
```

For workflows that push, deploy, or publish packages, check permissions:

```yaml
permissions:
  contents: read
  pages: write
  id-token: write
```

Only grant the permissions the job needs.

### 6. Reproduce the Failing Command Locally

Run the same command from the failed step:

```bash
npm ci
npm run build
```

or:

```bash
bundle install
bundle exec jekyll build --trace
```

If it fails locally, fix the project.
If it only fails in GitHub Actions, compare versions, environment variables, file paths, and OS differences.

### 7. Clear Cache Only When the Log Points There

Cache issues happen, but they are not the first assumption.

If dependency errors remain after lockfile changes, temporarily disable cache or change the cache key.
Do not delete lockfiles just to make CI green.
The lockfile is part of the reproducible build.

## How to Verify

After fixing the workflow or project files:

```bash
git add .
git commit -m "Fix CI build"
git push
```

Then check:

- The workflow starts on the expected branch or pull request.
- The previously failed step now passes.
- Tests and build both pass.
- Deploy steps have the expected permissions.

If the workflow fails again at a later step, treat it as a new error and read that step's log.

## Common Mistakes

- Reading only `exit code 1` and missing the real error above it.
- Editing the wrong workflow file.
- Using `npm install` in CI when the project expects `npm ci`.
- Forgetting to install the runtime before running commands.
- Relying on local secrets that do not exist in GitHub Actions.
- Giving broad permissions instead of fixing the required permission.
- Deleting the lockfile to avoid dependency conflicts.

## Official References

- [Using workflow run logs](https://docs.github.com/en/actions/how-tos/monitor-workflows/use-workflow-run-logs)
- [Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax)

## Related Posts

- [How to Fix Git Failed to Push Some Refs Error](/en_Troubleshooting/git-failed-to-push-some-refs/)
- [How to Resolve Git Merge Conflicts](/en_Troubleshooting/git-resolving-merge-conflicts/)
- [How to Fix Git fatal: could not read Username Error](/en_Troubleshooting/git-fatal-could-not-read-username/)
