---
typora-root-url: ../
layout: single
title: >
   How to Resolve Merge Conflicts in Git
date: 2025-08-06T10:10:00+09:00
header:
   teaser: /images/header_images/overlay_image_git.png
   overlay_image: /images/header_images/overlay_image_git.png
   overlay_filter: 0.5
excerpt: >
    A step-by-step guide to understanding and resolving merge conflicts that occur when combining branches in Git.
categories:
  - en_Troubleshooting
tags:
  - Git
  - Merge
  - Conflict
  - Branch
---

## What is a Merge Conflict?

A merge conflict occurs when you try to merge two branches that have competing changes. Git is unable to automatically decide which change to keep. This typically happens when the same line of code in the same file is modified on both branches.

When a conflict happens, Git pauses the merge process and waits for you to resolve the conflict manually.

## Problem Scenario

Let's say you have a `main` branch and a `feature` branch. Both branches have changes in the same file, `style.css`.

**On the `main` branch, `style.css` was changed to:**
```css
body {
  color: #333;
  font-family: Arial, sans-serif;
}
```

**On the `feature` branch, `style.css` was changed to:**
```css
body {
  color: #444;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
}
```

When you try to merge `feature` into `main`:
```bash
git switch main
git merge feature
```

You will see an error message:
```
Auto-merging style.css
CONFLICT (content): Merge conflict in style.css
Automatic merge failed; fix conflicts and then commit the result.
```

## Solution

### 1. Identify Conflicting Files

Git tells you which files have conflicts. You can also use `git status` to see a list of unmerged paths.

```bash
git status
On branch main
You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
  (use "git add <file>..." to mark resolution)
        both modified:   style.css

no changes added to commit (use "git add" and/or "git commit -a")
```

### 2. Open and Edit the File

Open `style.css` in your code editor. Git marks the conflicting areas:

```css
body {
<<<<<<< HEAD
  color: #333;
  font-family: Arial, sans-serif;
=======
  color: #444;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
>>>>>>> feature
}
```

-   `<<<<<<< HEAD`: This marks the beginning of the conflicting change from your current branch (`main`).
-   `=======`: This separates the two conflicting changes.
-   `>>>>>>> feature`: This marks the end of the conflicting change from the branch you are merging (`feature`).

### 3. Resolve the Conflict

You need to decide what the final version should look like. You can choose one version, the other, or a combination of both.

Let's say we want to keep the `font-family` from the `feature` branch and the `color` from the `main` branch. Edit the file to look like this:

```css
body {
  color: #333;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
}
```

Make sure to remove the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`).

### 4. Stage the Resolved File

After you have resolved the conflict in the file, you need to tell Git that the conflict is resolved by staging the file.

```bash
git add style.css
```

### 5. Commit the Merge

Once all conflicts are resolved and the files are staged, you can complete the merge by creating a merge commit.

```bash
git commit
```

Git will open an editor with a pre-populated commit message like "Merge branch 'feature'". You can keep it as is or modify it. Save and close the editor to create the commit.

The merge is now complete.

## Aborting a Merge

If you get into a complicated merge and want to start over, you can always abort the merge process.

```bash
git merge --abort
```

This will return your branch to the state it was in before you started the merge.

## Conclusion

Merge conflicts are a normal part of working with Git. By understanding what the conflict markers mean, you can resolve them confidently. Always review the changes carefully to ensure the final result is correct.
