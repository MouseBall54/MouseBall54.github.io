---
typora-root-url: ../
layout: single
title: "How to Fix \"fatal: pathspec '...' did not match any files\" in Git"
date: 2025-07-31T22:15:00+09:00
excerpt: "Resolve the Git error \"fatal: pathspec '...' did not match any files\" by checking for typos, correct file paths, and ensuring the file is tracked by Git when necessary."
header:
   teaser: /images/header_images/overlay_image_git.png
   overlay_image: /images/header_images/overlay_image_git.png
   overlay_filter: 0.5
categories:
  - en_Troubleshooting
tags:
  - Git
  - Pathspec
  - Version Control
  - Debugging
---

## Introduction

The `fatal: pathspec '...' did not match any files` error in Git is a common message that appears when you try to run a command like `git add`, `git rm`, or `git checkout` on a file that Git cannot find. This guide will walk you through the simple reasons why this error occurs and how to quickly resolve it.

## What is a "Pathspec"?

In Git, a "pathspec" is simply the way you refer to a file or directory path. For example, in the command `git add index.html`, the pathspec is `index.html`. The error message is telling you that the path you provided did not match any files that Git knows about in the context of your command.

## Common Causes and Solutions

Let's look at the most frequent reasons for this error and how to fix them.

### 1. Cause: Typo in the Filename or Path

This is the most common cause. You may have simply misspelled the name of the file or the directory it's in.

**Example:**
You want to add `styles.css`, but you type:
```bash
git add style.css 
# fatal: pathspec 'style.css' did not match any files
```

**Solution:**
- **Check your spelling**: Carefully re-examine the filename and path for any typos.
- **Use Tab Completion**: In your terminal, start typing the filename and press the `Tab` key. The shell will automatically complete the name if it's correct, or do nothing if it's not. This is a great way to avoid typos.
- **List files**: Use `ls` (on Linux/macOS) or `dir` (on Windows) to list the files in the current directory and verify the correct name.

### 2. Cause: Incorrect File Path

You might be in the wrong directory. The command you are running only looks for the file in the current directory unless you provide a relative or absolute path.

**Example:**
Your file `index.html` is in the `src` subdirectory, but you are in the project's root directory.
```bash
# You are in /my-project/
git add index.html
# fatal: pathspec 'index.html' did not match any files
```

**Solution:**
- **Provide the correct path**: Include the full path to the file from your current location.
  ```bash
  git add src/index.html
  ```
- **Change directory**: Navigate to the correct directory first, then run the command.
  ```bash
  cd src
  git add index.html
  ```

### 3. Cause: File is Not Tracked by Git (for `git rm`)

The `git rm` command is used to remove files from the Git repository. If you try to use it on a file that has not been committed to the repository yet (i.e., it's untracked), Git will throw the pathspec error because the file doesn't exist in its tracking index.

**Example:**
You have a new file `temp.log` that you haven't added or committed.
```bash
git rm temp.log
# fatal: pathspec 'temp.log' did not match any files
```

**Solution:**
- **Use the standard `rm` command**: If you just want to delete a file from your local filesystem (and it's not tracked by Git), use the standard shell command instead of `git rm`.
  - On Linux/macOS: `rm temp.log`
  - On Windows: `del temp.log`
- **If the file is tracked**: If you want to remove a file that *is* tracked by Git but also has local modifications, you might need to use the `-f` (force) option.
  ```bash
  git rm -f some-file.txt
  ```

### 4. Cause: Using Quotes Incorrectly

If your filename contains spaces or special characters, you need to wrap it in quotes. Forgetting to do so can confuse Git.

**Example:**
```bash
git add my new file.txt
# Git thinks you are trying to add three separate files: 'my', 'new', and 'file.txt'
# fatal: pathspec 'my' did not match any files
```

**Solution:**
- **Use quotes**: Enclose the entire filename in double quotes.
  ```bash
  git add "my new file.txt"
  ```

By checking for these four common issues—typos, incorrect paths, untracked files, and missing quotes—you can easily resolve the `fatal: pathspec '...' did not match any files` error.

```