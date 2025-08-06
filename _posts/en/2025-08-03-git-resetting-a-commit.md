---
typora-root-url: ../
layout: single
title: >
    Undoing a Commit in Git: A Complete Guide to the Three Options of git reset (soft, mixed, hard)

lang: en
translation_id: git-resetting-a-commit
header:
    teaser: /images/header_images/overlay_image_git.png
    overlay_image: /images/header_images/overlay_image_git.png
    overlay_filter: 0.5
excerpt: >
    git reset is a powerful command for reverting a project's state to a specific commit. This article explains the differences and usage of the three main options of git reset: --soft, --mixed, and --hard.
categories:
    - en_Troubleshooting
tags:
    - Git
    - Reset
    - Commit
    - Soft
    - Hard
---

## What is `git reset`?

`git reset` is a powerful and versatile command used to revert a Git repository's state to a specific commit. Its primary function is to move the `HEAD` pointer of a branch to a previous commit. However, the impact of `reset` on the index (Staging Area) and the working directory varies significantly depending on the option used, so it is crucial to understand the differences between each option.

First, you need to understand Git's three state areas:
1.  **Working Directory**: The actual files you are currently working on.
2.  **Index / Staging Area**: A list of changes that will be included in the next commit.
3.  **HEAD**: The last commit that the current branch points to.

## The Three Options of `git reset`

The core of `git reset` is deciding how far back to revert among these three areas.

### 1. `git reset --soft <commit>`

The `--soft` option is the most conservative reset. This command moves **only the `HEAD` pointer** to the specified commit. It does not touch the index or the working directory at all.

-   **Action**: Moves `HEAD` to `<commit>`.
-   **Result**:
    -   The commit that `HEAD` points to is changed.
    -   The index (Staging Area) remains unchanged. This means all changes between the original `HEAD` and `<commit>` are left in a staged state.
    -   The files in the working directory are not changed at all.
-   **Primary Use Case**: Useful for squashing multiple commits into one. For example, if you want to undo the last three commits and re-create them as a single commit, you can run `git reset --soft HEAD~3`. All the changes from the last three commits will be ready in the staging area.

**Command Example:**
```bash
# Undo the last commit, but keep the changes staged.
git reset --soft HEAD~
```

### 2. `git reset --mixed <commit>` (Default Option)

`--mixed` is the **default option** for `git reset`. If you run the `reset` command without any options, it will behave as `--mixed`. This option reverts `HEAD` and the index to the state of the specified commit.

-   **Action**: Reverts `HEAD` and the index to the state of `<commit>`.
-   **Result**:
    -   The commit that `HEAD` points to is changed.
    -   The index is reset to the state of `<commit>`. This means all staged changes are unstaged and moved to the working directory.
    -   The files in the working directory are not changed.
-   **Primary Use Case**: Used when you want to undo a commit but keep the file changes. It is useful for modifying staged content or re-staging only some of the changes.

**Command Example:**
```bash
# Undo the last commit and leave the changes only in the working directory (unstaged).
git reset --mixed HEAD~ # Same as `git reset HEAD~`
```

### 3. `git reset --hard <commit>`

`--hard` is the most powerful and **destructive** option. This command reverts `HEAD`, the index, and **even the working directory** to the state of the specified commit.

-   **Action**: Reverts `HEAD`, the index, and the working directory to the state of `<commit>`.
-   **Result**:
    -   The commit that `HEAD` points to is changed.
    -   The index is reset to the state of `<commit>`.
    -   **All changes in the working directory are permanently deleted.** Any work done since `<commit>` will be lost, so extreme caution is required when using this option.
-   **Primary Use Case**: Used when you want to completely discard all recent changes (commits, staging, and working directory changes) and return to a clean state at a specific point in time.

**Command Example:**
```bash
# Completely delete all changes related to the last commit (including staging and working directory content).
git reset --hard HEAD~
```

## Summary

| Option      | `HEAD` (Branch Pointer) | Index (Staging Area) | Working Directory (Files) | Primary Use                                       |
| :-------- | :-------------------- | :------------------- | :------------------------ | :------------------------------------------------ |
| `--soft`  | Moves (Yes)           | No Change (No)       | No Change (No)            | Squashing commits (all changes remain staged)     |
| `--mixed` | Moves (Yes)           | Resets (Yes)         | No Change (No)            | Undoing a commit and modifying staging (changes preserved) |
| `--hard`  | Moves (Yes)           | Resets (Yes)         | Resets (Yes)              | Completely discarding all changes                 |

## Caution

-   `git reset` is an operation that changes the local repository's commit history. If you reset a commit that has already been pushed to a remote repository, you will need the `--force` option to push it again. This can cause conflicts with your teammates' history, so it is safer to use `git revert` on shared branches.
-   `git reset --hard` is an irreversible operation, so it is a good idea to double-check your current status with `git status` or `git log` before running it.
