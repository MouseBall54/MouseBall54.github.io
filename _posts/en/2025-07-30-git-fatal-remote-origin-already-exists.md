---
typora-root-url: ../
layout: single
title: "How to Fix 'fatal: remote origin already exists' in Git"

lang: en
translation_id: git-fatal-remote-origin-already-exists
excerpt: "The 'fatal: remote origin already exists' error occurs when you try to add a remote named 'origin' that is already in use. This article explains the cause and how to resolve it."
header:
   teaser: /images/header_images/overlay_image_git.png
   overlay_image: /images/header_images/overlay_image_git.png
   overlay_filter: 0.5
categories:
  - en_Troubleshooting
tags:
  - Git
  - Troubleshooting
  - Version Control
  - Remote
---

## What is the 'fatal: remote origin already exists' Error?

The `fatal: remote origin already exists` error occurs when you run the command `git remote add origin <repository_URL>` and a remote repository named `origin` is already configured.
In Git, aliases (names) for remote repositories must be unique, so this error message appears if you try to use a duplicate name.
`origin` is the default name for a remote repository that is automatically created when you use the `git clone` command.

## Main Causes

### 1. Running `git remote add` after `git clone`
When you clone a remote repository with `git clone`, Git automatically registers that remote repository under the name `origin`.
If you then attempt to add the same or another repository with the name `origin`, the error will occur.

```bash
# Cloning the repository automatically sets 'origin'
git clone https://github.com/user/repo.git
cd repo

# Error occurs because 'origin' already exists
git remote add origin https://github.com/user/repo.git
# fatal: remote origin already exists.
```

### 2. Adding a Remote Manually and Then Adding It Again
You created a local repository with `git init` and then connected a remote repository using the `git remote add origin` command.
If you run the same command again, the name will naturally be duplicated, causing the error.

## How to Fix It

The solution depends on how you want to handle the existing `origin` configuration.

### 1. Change the URL of the Existing Remote
If you simply want to change the URL of the existing `origin` to a different one, you can use the `set-url` command.

```bash
# Check the currently configured remotes
git remote -v
# origin  https://github.com/old/repo.git (fetch)
# origin  https://github.com/old/repo.git (push)

# Change the URL of 'origin' to the new URL
git remote set-url origin https://github.com/new/repo.git

# Verify the changes
git remote -v
# origin  https://github.com/new/repo.git (fetch)
# origin  https://github.com/new/repo.git (push)
```
This method is most suitable when you want to keep the `origin` name but just change the address.

### 2. Remove the Existing Remote and Add a New One
If the existing `origin` configuration is completely wrong or no longer needed, you can remove it and add a new one.

```bash
# Remove the existing 'origin' remote
git remote remove origin

# Add the new remote as 'origin'
git remote add origin https://github.com/another/repo.git

# Verify the configuration
git remote -v
# origin  https://github.com/another/repo.git (fetch)
# origin  https://github.com/another/repo.git (push)
```

### 3. Add a Remote with a Different Name
If you want to keep the name `origin` but also add another remote repository, you can use a different name.
For example, you could use a name like `upstream` or `backup`.

```bash
# Keep 'origin' and add a new remote named 'upstream'
git remote add upstream https://github.com/different/repo.git

# Check the list of configured remotes
git remote -v
# origin    https://github.com/original/repo.git (fetch)
# origin    https://github.com/original/repo.git (push)
# upstream  https://github.com/different/repo.git (fetch)
# upstream  https://github.com/different/repo.git (push)
```
This method is useful when you need to manage multiple remote repositories simultaneously.

## Conclusion

The `fatal: remote origin already exists` error is a natural occurrence in Git when remote repository names conflict.
It is important to get into the habit of first checking the currently configured remotes with the `git remote -v` command.
You can easily solve the problem by using `set-url` to change the URL, `remove` to delete and re-add, or by adding another remote with a new name, depending on the situation.
