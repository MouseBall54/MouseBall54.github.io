---
typora-root-url: ../
layout: single
title: >
    How to Fix Git "Detached HEAD" State
date: 2025-08-03T10:10:00+09:00
header:
   teaser: /images/header_images/overlay_image_git.png
   overlay_image: /images/header_images/overlay_image_git.png
   overlay_filter: 0.5
excerpt: >
    Understand what a "Detached HEAD" state in Git is, why it happens, and how to safely get back to a branch without losing your work.
categories:
  - en_Troubleshooting
tags:
  - Git
  - Version Control
  - Detached HEAD
  - Branching
---

## What is a "Detached HEAD" State in Git?

In Git, `HEAD` is a pointer that normally points to the latest commit of the branch you are currently on. For example, if you are on the `main` branch, `HEAD` points to `main`.

A "detached HEAD" state occurs when `HEAD` is pointing directly to a specific commit, instead of a branch. This means you are no longer on any branch. You can look around, make experimental changes, and even commit them, but these new commits do not belong to any branch. They are "floating" and can be easily lost if you switch to another branch without saving them.

This state is often entered intentionally to inspect an old version of the code, but it can be confusing for developers who enter it by accident.

## How Do You Get into a Detached HEAD State?

The most common way to enter this state is by checking out a specific commit hash, a tag, or a remote branch.

```bash
# Checking out a specific commit hash
git checkout a1b2c3d4

# Checking out a tag
git checkout v1.2.0

# Checking out a remote branch directly
git checkout origin/feature-branch
```

When you run any of these commands, Git will give you a lengthy message explaining that you are in a "detached HEAD" state and what you can do about it.

## How to Fix a Detached HEAD

The fix depends on what you did while in the detached state.

### Scenario 1: You Haven't Made Any Changes

If you just wanted to look at the code and haven't made any commits, you can simply switch back to your desired branch.

```bash
# Switch back to the main branch
git checkout main

# Or switch back to your feature branch
git checkout my-feature-branch
```
This will move `HEAD` back to pointing at the branch, and you'll be out of the detached state.

### Scenario 2: You Have Made Commits and Want to Keep Them

This is the more critical scenario. If you've made commits in a detached HEAD state, they are not attached to any branch. If you switch branches now, those commits will be "orphaned" and eventually deleted by Git's garbage collection process.

To save your work, you need to create a new branch to hold your commits.

**Step 1: Create a new branch**

While still in the detached HEAD state, create a new branch. This will make the new branch point to your latest commit.

```bash
# Create a new branch named 'new-feature' from your current commit
git branch new-feature
```
Alternatively, you can use `git checkout -b` which creates the new branch and switches to it in one step.

```bash
# Create and switch to a new branch named 'new-feature'
git checkout -b new-feature
```

Now, your new commits are safe on the `new-feature` branch. `HEAD` is no longer detached; it points to your new branch.

**Step 2 (Optional): Merge the new branch**

If you want to integrate these changes into your main development line (e.g., the `main` branch), you can now merge your new branch.

```bash
# Switch to the main branch
git checkout main

# Merge the new-feature branch into main
git merge new-feature
```

## How to Avoid Losing Commits

If you've already switched away from your detached HEAD commits and think you've lost them, don't panic yet. Git keeps "orphaned" commits for a while before deleting them. You can often find them using the `git reflog` command.

`git reflog` shows a history of where `HEAD` has pointed. Look for the commit hash from when you were in the detached state. Once you find the commit hash (e.g., `a1b2c3d4`), you can recover it by creating a branch from it:

```bash
git checkout a1b2c3d4
git checkout -b recovered-feature
```

## Conclusion

A "detached HEAD" is a normal part of Git, but it can be risky if you're not careful. The key takeaway is: if you make commits in a detached HEAD state, **create a new branch for them before you switch away**. By doing this, you can ensure your work is always safe and attached to a branch.
