typora-root-url: ../
layout: single
title: >
    How to Revert a Commit in Git (git revert)
seo_title: >
    How to Revert a Commit in Git (git revert)
date: 2025-08-05T21:40:00+09:00
header:
   teaser: /images/header_images/overlay_image_git.png
   overlay_image: /images/header_images/overlay_image_git.png
   overlay_filter: 0.5
excerpt: >
    Sometimes you need to safely undo the changes from a specific commit in Git. 'git revert' solves this by creating a new commit that undoes the changes without deleting the original commit. This post explains how to use git revert and its advantages.
seo_description: >
    Sometimes you need to safely undo the changes from a specific commit in Git. 'git revert' solves this by creating a new commit that undoes the changes without deleting the original commit. This post explains how to use git revert and its advantages.
categories:
  - en_Troubleshooting
tags:
  - Git
  - Revert
  - Commit
  - VersionControl
---

## The Problem

While managing a project with Git, you may find that changes included in a specific commit are causing issues or are no longer needed.
For example, you might have pushed a commit that introduced a bug to the remote repository.
Using `git reset` to force-modify the project history can cause serious conflicts when collaborating with other team members.
How can you safely undo the changes from a specific commit?

## Cause Analysis

The core of the issue lies in **how to safely modify a shared commit history**.
`git reset` deletes commits and rewrites history, so if another team member was working based on that deleted commit, their work foundation disappears.
This leads to a divergence between the remote and local repository histories, causing complex problems.

Therefore, when undoing a commit that has already been shared (pushed), you need a method that **adds a new commit to undo the changes** instead of deleting history.
The command that does this is `git revert`.

## Solution

`git revert` creates a new commit that applies the exact opposite of the changes from a specified commit.
For example, if a commit added a line to a file, the `revert` commit will delete that line.
This allows you to safely undo the desired changes while keeping the existing history intact.

### 1. Identify the Commit to Revert

First, use the `git log` command to find the hash of the commit you want to revert.

```bash
git log --oneline

# Example output
# a1b2c3d (HEAD -> main) Feat: Add new feature
# e4f5g6h Bug: Fix login logic (this is the commit to revert)
# i7j8k9l Docs: Update documentation
```

Let's assume we want to revert the commit `e4f5g6h`.

### 2. Run `git revert`

Enter the following command in your terminal:

```bash
git revert e4f5g6h
```

When you run this command, Git performs two main actions:

1.  It applies the inverse of the changes from commit `e4f5g6h` to your working directory.
2.  It opens your default text editor to allow you to write a new commit message. The default message will typically be something like "Revert \"Bug: Fix login logic\"".

Once you save the commit message and close the editor, a new commit containing the reverted changes is created.

```bash
git log --oneline

# Example output
# cba321d (HEAD -> main) Revert "Bug: Fix login logic"
# a1b2c3d Feat: Add new feature
# e4f5g6h Bug: Fix login logic
# i7j8k9l Docs: Update documentation
```

A new commit `cba321d` has been added, and the changes from `e4f5g6h` are now undone.

### 3. The `--no-edit` Option

If you want to use the default commit message without opening the editor, you can add the `--no-edit` option.

```bash
git revert e4f5g6h --no-edit
```

### 4. Reverting Multiple Commits

You can also revert multiple commits at once. However, be mindful of the order.

```bash
# Revert from the oldest to the newest commit
git revert <oldest-commit-hash> <newest-commit-hash>
```

### 5. Push to the Remote Repository

After successfully creating the revert commit locally, you should push it to the remote repository to share the changes with your team.

```bash
git push origin main
```

Since `git revert` adds a new commit, `git push` will work smoothly without causing conflicts.

## `git revert` vs. `git reset`

| Feature | `git revert` | `git reset` |
| --- | --- | --- |
| **History** | Preserves existing history and adds a new commit to revert changes | Deletes and modifies existing history |
| **Safety** | Safe to use on shared (pushed) branches | Very risky to use on shared branches |
| **Use Case** | Public commits, bug fixes in collaborative projects | Cleaning up commits on a private, local branch |

## Conclusion

`git revert` is a powerful and essential command for safely undoing changes from commits that have already been pushed to a remote repository.
It allows you to maintain a clean and intact project history, ensuring smooth collaboration with your team.
If you accidentally push a problematic commit, it is always better to use `git revert` to safely undo it rather than attempting to erase history with `git reset`.
