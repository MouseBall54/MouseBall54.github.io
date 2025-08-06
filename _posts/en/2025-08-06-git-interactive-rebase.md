---
typora-root-url: ../
layout: single
title: >
   How to Use Git Interactive Rebase to Modify Commits
date: 2025-08-06T10:00:00+09:00
header:
   teaser: /images/header_images/overlay_image_git.png
   overlay_image: /images/header_images/overlay_image_git.png
   overlay_filter: 0.5
excerpt: >
    Learn how to use `git rebase -i` to combine, edit, or delete previous commits for a cleaner and more understandable project history.
categories:
  - en_Troubleshooting
tags:
  - Git
  - Rebase
  - Commit
  - History
  - Interactive
---

## What is Git Interactive Rebase?

Git interactive rebase is a powerful tool. It allows you to modify commits in various ways. You can reorder, reword, edit, squash (combine), or drop (delete) commits. This helps create a clean and logical project history.

It is especially useful before merging a feature branch into the main branch.

## Problem Scenario

Imagine you have made several small commits on your feature branch. Some commits are fixes for previous ones, and others are minor changes. The commit history might look messy.

```bash
git log --oneline
f30abf4 (HEAD -> feature) Add feature documentation
a412b9e Fix typo in feature
e85fde9 Implement the main part of the feature
cba1a2d Add initial files for feature
```

This history is not ideal. We can clean it up using `git rebase -i`.

## Solution

### 1. Start Interactive Rebase

You need to specify how far back you want to edit commits. Let's say we want to modify the last 3 commits. The base commit is `cba1a2d`.

Run the following command:

```bash
git rebase -i HEAD~3
```

Alternatively, you can use the commit hash of the parent of the first commit you want to edit.

```bash
git rebase -i cba1a2d
```

### 2. Edit the Instruction File

This command opens an editor with a list of the commits you selected.

```
pick e85fde9 Implement the main part of the feature
pick a412b9e Fix typo in feature
pick f30abf4 Add feature documentation

# Rebase cba1a2d..f30abf4 onto cba1a2d (3 commands)
#
# Commands:
# p, pick <commit> = use commit
# r, reword <commit> = use commit, but edit the commit message
# e, edit <commit> = use commit, but stop for amending
# s, squash <commit> = use commit, but meld into previous commit
# f, fixup <commit> = like "squash", but discard this commit's log message
# x, exec <command> = run command (the rest of the line) using shell
# b, break = stop here (continue rebase later with 'git rebase --continue')
# d, drop <commit> = remove commit
# l, label <label> = label current HEAD with a name
# t, label <label> = reset HEAD to a label
# m, merge [-C <commit> | -c <commit>] <label> [# <oneline>]
# .       create a merge commit using the original merge commit's
# .       message (or the oneline, if no original merge commit was
# .       specified). Use -c <commit> to re-create the merge commit
# .       from the original commit.
#
# These lines can be re-ordered; they are executed from top to bottom.
#
# If you remove a line here THAT COMMIT WILL BE LOST.
#
# However, if you remove everything, the rebase will be aborted.
#
```

### 3. Modify Commits

Let's combine the "Fix typo" commit with the implementation commit. We will use `squash` (or `s`). We also want to reword the final commit message.

Change `pick` to `squash` for the typo fix commit. Let's also `reword` the final commit.

```
pick e85fde9 Implement the main part of the feature
s a412b9e Fix typo in feature
r f30abf4 Add feature documentation
```

Save and close the file.

### 4. Finalize Changes

Git will first combine the two commits. It will then open another editor to let you write a new commit message for the combined commit.

```
# This is a combination of 2 commits.
# The first commit's message is:
Implement the main part of the feature

# This is the 2nd commit's message:
Fix typo in feature
```

Let's create a clean message: `Implement the main part of the feature`.

After saving that message, the rebase continues. It then stops to let you reword the last commit's message. Another editor opens for `f30abf4`. Let's change it to `Add documentation for the new feature`.

### 5. Check the History

Now, check the log again.

```bash
git log --oneline
a1b2c3d (HEAD -> feature) Add documentation for the new feature
d4e5f6g Implement the main part of the feature
cba1a2d Add initial files for feature
```

The history is now much cleaner and easier to understand.

## Conclusion

Interactive rebase is a powerful feature for managing commit history. Use it to make your history clean before sharing your changes with others. However, be careful not to rebase commits that have already been pushed to a shared repository, as it rewrites history and can cause issues for collaborators.
