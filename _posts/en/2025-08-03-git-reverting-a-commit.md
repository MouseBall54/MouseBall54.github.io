---
typora-root-url: ../
layout: single
title: >
    How to Revert a Commit in Git: A Guide to `git revert`

lang: en
translation_id: git-reverting-a-commit
header:
   teaser: /images/header_images/overlay_image_git.png
   overlay_image: /images/header_images/overlay_image_git.png
   overlay_filter: 0.5
excerpt: >
    Learn how to safely undo the changes from a specific commit using the `git revert` command and understand its difference from `git reset`.
categories:
  - en_Troubleshooting
tags:
  - Git
  - git revert
  - git reset
  - Version Control
---

## The Problem

While managing a project with Git, you often realize that a specific commit introduced a problem. For example, you might have committed code that causes a bug, or included a wrong file, and already pushed it to the remote repository.

In such cases, you want to safely remove the changes from that commit. However, forcibly altering the project's history can be dangerous, especially on a shared branch where other team members are working. Using commands like `git reset` on a public branch is strongly discouraged.

## The Solution: Using `git revert`

`git revert` is a command that creates a **new commit** that applies the inverse of the changes introduced by a specific commit. In other words, instead of deleting or altering the existing commit history, it adds a new commit that undoes the problematic one.

This approach has significant advantages:
- **It's Safe**: It preserves the existing commit history, avoiding conflicts for your teammates.
- **It's Clear**: It leaves a clear and explicit record that a specific commit was undone.

### How to Use `git revert`

1.  **Identify the Commit to Revert**

    First, use `git log` to view the commit history and find the hash of the commit you want to undo.

    ```bash
    git log --oneline
    # c4a2f85 (HEAD -> main) feat: Add user profile feature
    # a1b3c4d fix: Correct login validation
    # f9e8d7c chore: Update documentation
    ```
    Let's assume the commit `a1b3c4d` is the one causing issues.

2.  **Run `git revert`**

    Use the following command to revert that commit:

    ```bash
    git revert a1b3c4d
    ```

3.  **Write the Commit Message**

    After you run the command, Git will open a text editor for you to write a commit message for the new "revert" commit. By default, it will generate a message like "Revert "fix: Correct login validation"".
    
    You can add more details explaining why this commit is being reverted. Once you save the message and close the editor, the new commit will be created.

    If you want to skip editing the commit message, you can use the `--no-edit` option.
    ```bash
    git revert --no-edit a1b3c4d
    ```

4.  **Push to the Remote Repository**

    Once the revert commit is created locally, push this change to the remote repository to share it with your team.

    ```bash
    git push origin main
    ```

Now, if you check the `git log` again, you will see that the original commits are still there, and a new "Revert" commit has been added on top.

```bash
git log --oneline
# 3d5e6f7 (HEAD -> main) Revert "fix: Correct login validation"
# c4a2f85 feat: Add user profile feature
# a1b3c4d fix: Correct login validation
# f9e8d7c chore: Update documentation
```

## `git revert` vs. `git reset`

| Feature | `git revert` | `git reset` |
| --- | --- | --- |
| **Action** | Creates a **new commit** that undoes changes. | **Moves the HEAD pointer** to a previous commit. |
| **History** | **Preserves** the existing history (safe). | **Alters/deletes** the existing history (risky). |
| **Primary Use Case** | Reverting commits on a **shared branch** (e.g., `main`, `develop`). | Cleaning up commits on a **private, local branch** that hasn't been shared. |

Because `git reset` erases commit history, using it on a commit that has already been shared with your team can cause serious conflicts with their work. Therefore, **on shared branches, you should always use `git revert`**.

## Conclusion

`git revert` is a powerful and essential tool for safely undoing changes that have already been committed, especially those shared on a remote repository.

-   When you need to undo a problematic commit, use `git revert <commit-hash>`.
-   This command creates a **new commit** that reverses the changes, rather than rewriting history.
-   As a rule, **use `git revert` instead of `git reset` on any shared branch**.

Fixing mistakes is a natural part of the development process. Use `git revert` correctly to keep your project's history clean and safe.
