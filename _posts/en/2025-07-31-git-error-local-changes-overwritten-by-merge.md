---
typora-root-url: ../
layout: single
title: "How to Fix \"error: Your local changes to the following files would be overwritten by merge\" in Git"

lang: en
translation_id: git-error-local-changes-overwritten-by-merge
excerpt: "Resolve the Git merge error by stashing, committing, or discarding your local changes before pulling or merging."
header:
   teaser: /images/header_images/overlay_image_git.png
   overlay_image: /images/header_images/overlay_image_git.png
   overlay_filter: 0.5
categories:
  - en_Troubleshooting
tags:
  - Git
  - Merge
  - Stash
  - Commit
  - Version Control
---

## Introduction

The Git error message `error: Your local changes to the following files would be overwritten by merge` is a protective measure. It prevents you from losing uncommitted work. This error occurs when you have local modifications in your working directory that conflict with files being updated by a `git pull` or `git merge` operation. This guide explains why this happens and provides three common ways to resolve it.

## Why Does This Error Occur?

Git's primary job is to manage versions of your code. When you `pull` from a remote repository or `merge` a branch, Git needs to update files in your local working directory. If you have made changes to a file that Git also needs to update, it stops the process to avoid overwriting your work.

For example:
1. You modified a file, say `style.css`.
2. You did **not** commit this change.
3. Meanwhile, a collaborator pushed a new version of `style.css` to the remote repository.
4. When you run `git pull`, Git tries to fetch the new `style.css` and update your local file.
5. Git sees your uncommitted changes and aborts the operation with the "overwritten by merge" error to protect your work.

## How to Fix It

There are three primary methods to solve this issue. Choose the one that best fits your situation.

### Method 1: Commit Your Changes

If the changes you made are complete and you want to keep them, the most straightforward solution is to commit them before you pull or merge.

**Steps:**
1.  **Stage your changes**: Add the modified files to the staging area.
    ```bash
    git add .
    # Or be more specific: git add <file1> <file2>
    ```
2.  **Commit the changes**: Save your changes to your local repository with a descriptive message.
    ```bash
    git commit -m "My descriptive commit message"
    ```
3.  **Pull or merge again**: Now that your local changes are safely committed, you can proceed with the original operation.
    ```bash
    git pull
    # Or git merge <branch-name>
    ```
    If there are conflicts between your commit and the incoming changes, Git will now prompt you to resolve the merge conflicts, but it won't overwrite your work.

### Method 2: Stash Your Changes

If your changes are not ready to be committed, but you still want to pull the latest updates, `git stash` is the perfect tool. It temporarily shelves (or stashes) your uncommitted changes, allowing you to have a clean working directory.

**Steps:**
1.  **Stash your local changes**: This will save your modifications and revert the files to match the last commit (`HEAD`).
    ```bash
    git stash
    ```
2.  **Pull or merge**: Your working directory is now clean, so you can safely pull or merge.
    ```bash
    git pull
    ```
3.  **Apply your stashed changes**: After the pull is complete, you can reapply your changes on top of the newly updated code.
    ```bash
    git stash pop
    # Or git stash apply
    ```
    `git stash pop` applies the changes and removes the stash from the list. `git stash apply` applies the changes but keeps the stash, which can be useful if you want to apply it to multiple branches.

### Method 3: Discard Your Changes

If you decide that your local changes are no longer needed and you just want to get the latest version from the remote, you can discard them.

**Warning**: This action is irreversible. You will lose your local modifications permanently.

**Steps:**
1.  **Discard all local changes**: This command will clean your working directory, removing all uncommitted changes.
    ```bash
    git reset --hard HEAD
    ```
    Or, to discard changes in a specific file:
    ```bash
    git checkout -- <file-name>
    ```
2.  **Pull or merge**: With a clean working directory, you can now pull without any issues.
    ```bash
    git pull
    ```

By choosing one of these three methods—commit, stash, or discard—you can safely manage your local work and resolve the "overwritten by merge" error.
