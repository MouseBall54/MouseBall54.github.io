---
typora-root-url: ../
layout: single
title: "How to Fix 'fatal: refusing to merge unrelated histories' in Git"
date: 2025-07-31T15:10:00+09:00
excerpt: "Learn how to resolve the 'fatal: refusing to merge unrelated histories' error in Git by using the `--allow-unrelated-histories` flag when two projects have different commit histories."
header:
   teaser: /images/header_images/overlay_image_git.png
   overlay_image: /images/header_images/overlay_image_git.png
   overlay_filter: 0.5
categories:
  - en_Troubleshooting
tags:
  - Git
  - Version Control
  - Merge
  - Troubleshooting
---

## What is the "fatal: refusing to merge unrelated histories" Error?

This Git error occurs when you try to `git pull` or `git merge` two branches that do not share a common commit history. It's a safety feature introduced in Git 2.9 to prevent users from accidentally merging two unrelated projects.

This situation often arises when:

1.  You have created a new local repository with its own commits and are now trying to pull from a remote repository that also has its own separate history.
2.  A project's `.git` directory was deleted and re-initialized, losing the original commit history, and you are now trying to reconcile it with a remote copy.

## Common Cause

The fundamental cause is that the two branches you are trying to merge have entirely separate and independent histories. Git cannot find a common ancestor commit to use as a base for the merge, so it stops and displays this error to ask for explicit confirmation.

- **Repository A History:** `A -> B -> C`
- **Repository B History:** `X -> Y -> Z`

Merging these two is not a straightforward process because there is no shared starting point.

## How to Fix It

If you are certain that you want to merge these two unrelated histories, you can use the `--allow-unrelated-histories` flag. This flag explicitly tells Git that you understand the situation and want to proceed with the merge.

### Step 1: Confirm the Merge

Before using the flag, double-check that you are in the correct repository and that merging these histories is indeed what you want to do. This action is usually irreversible.

### Step 2: Perform the Merge with the Flag

When you execute `git pull` or `git merge`, add the `--allow-unrelated-histories` option.

#### For `git pull`:

If you are pulling from a remote repository:

```bash
# Example: Pulling from the main branch of the origin remote
git pull origin main --allow-unrelated-histories
```

This will fetch the remote branch and then merge it into your current local branch, creating a new merge commit that ties the two histories together.

#### For `git merge`:

If you are merging two local branches:

```bash
# Example: Merging a branch named 'unrelated-branch'
git merge unrelated-branch --allow-unrelated-histories
```

### Step 3: Handle Merge Conflicts (If Necessary)

Because the projects are unrelated, it is highly likely that you will encounter merge conflicts, especially with files like `README.md` or `.gitignore` that may exist in both projects.

1.  **Open the conflicting files** and resolve the differences as needed.
2.  **Stage the resolved files** using `git add`.
3.  **Commit the merge** to finalize the process.

```bash
# After resolving conflicts
git add .
git commit -m "Merge unrelated histories"
```

### When Is This Useful?

- **Starting a new project based on a template**: You might initialize a local repository and then decide to pull in a remote template.
- **Migrating a repository**: When moving from one version control system to another, or from one Git host to another, histories can sometimes become disconnected.
- **Recovering from a corrupted repository**: If the local `.git` directory is lost, you may need to force a merge with the remote backup.

By using the `--allow-unrelated-histories` flag, you can override Git's default safety check and successfully combine two projects with separate commit histories.
