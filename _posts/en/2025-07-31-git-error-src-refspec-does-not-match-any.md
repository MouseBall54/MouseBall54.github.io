---
typora-root-url: ../
layout: single
title: "How to Fix 'error: src refspec ... does not match any' in Git"
date: 2025-07-31T23:00:00+09:00
header:
   teaser: /images/header_images/overlay_image_git.png
   overlay_image: /images/header_images/overlay_image_git.png
   overlay_filter: 0.5
excerpt: >
  Resolve the Git error "src refspec ... does not match any" by ensuring the branch you are trying to push exists locally and the name is spelled correctly.
categories:
  - en_Troubleshooting
tags:
  - Git
  - Push
  - Branch
  - Version Control
---

When you try to push changes to a remote repository, you might encounter the frustrating error: `error: src refspec <branch-name> does not match any.` This message means Git cannot find the local branch you're trying to push.

This post explains the common causes of this error and how to fix it.

### What Causes This Error?

The "src refspec ... does not match any" error typically occurs for one of two simple reasons:

1.  **The branch does not exist locally**: You are trying to push a branch that you haven't created or checked out in your local repository.
2.  **A typo in the branch name**: You have misspelled the name of the branch in your `git push` command.

For example, if you run `git push origin master` but your local branch is actually named `main`, Git won't find a branch called `master` to push.

### How to Fix the Error

The solution involves verifying the branch name and ensuring it exists locally before you push.

#### Step 1: List Your Local Branches

First, check the names of all the branches in your local repository. You can do this with the `git branch` command.

```bash
git branch
```

This command will list all your local branches and highlight the one you are currently on.

```
  feature/new-login
* main
  hotfix/bug-123
```

From this list, you can confirm the correct spelling of the branch you intend to push.

#### Step 2: Correct Your `git push` Command

Once you have the correct branch name, you can retry the `git push` command.

For instance, if you discovered your branch is named `main` instead of `master`, you would run:

```bash
git push origin main
```

If you were trying to push a feature branch, make sure the name matches exactly what you saw in the `git branch` output.

```bash
# Incorrect
git push origin feature/new-login-typo

# Correct
git push origin feature/new-login
```

#### Step 3: Create the Branch if It Doesn't Exist

If `git branch` doesn't show the branch you want to push, it means the branch doesn't exist locally. You may need to create it first.

If you are on the correct commit, you can create a new branch from your current `HEAD` position.

```bash
# Create a new branch named 'new-feature'
git branch new-feature

# Switch to the new branch
git checkout new-feature
```

Or, you can do both in one command:

```bash
git checkout -b new-feature
```

After creating and switching to the branch, you can now push it to the remote repository.

```bash
git push origin new-feature
```

### Pushing the Current Branch

A useful tip to avoid typos is to push the current branch using `HEAD`. This special pointer in Git always refers to the branch you are currently working on.

```bash
git push origin HEAD
```

This command tells Git to push the current branch to a remote branch of the same name.

### Conclusion

The "src refspec ... does not match any" error is a common and usually simple problem to solve. It's almost always caused by a typo or trying to push a non-existent local branch. By using `git branch` to verify your local branches, you can easily correct your push command and get your code to the remote repository.
