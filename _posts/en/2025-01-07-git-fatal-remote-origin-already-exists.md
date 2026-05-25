---
typora-root-url: ../
layout: single
title: "How to Fix 'fatal: remote origin already exists' in Git"

date: 2025-01-07T07:11:00+09:00
lang: en
translation_id: git-fatal-remote-origin-already-exists
excerpt: "The 'fatal: remote origin already exists' error occurs when you try to add a remote named 'origin' that is already in use. This article explains the cause and how to resolve it."
seo_description: "The 'fatal: remote origin already exists' error occurs when you try to add a remote named 'origin' that is already in use. This article explains the cause and how to resolve it."
header:
   teaser: /images/header_images/overlay_image_git.png
   overlay_image: /images/header_images/overlay_image_git.png
   overlay_filter: 0.5
   image_description: >
     A visual summary explaining the main topic of this post: How to Fix 'fatal: remote origin already exists' in Git
categories:
  - en_Troubleshooting
tags:
  - Git
  - Troubleshooting
  - Version Control
  - Remote
---


![A visual summary explaining the main topic of this post: How to Fix 'fatal: remote origin already exists' in Git](/images/header_images/overlay_image_git.png)
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

## Professional Depth Check

For **How to Fix 'fatal: remote origin already exists' in Git**, the practical standard is not whether the reader can repeat one instruction once. Treat the topic as a reproducible debugging procedure: verify repository root, branch and remote state, index and working tree, and credential or network boundary before drawing a conclusion. The result should be written as a small decision record, because future readers need to know which fact was observed, which assumption was used, and which condition would change the answer.

### Evidence That Makes the Guidance Reliable

Use objective evidence before changing a workflow. Good evidence includes `git status`, `git remote -v`, `git branch --show-current`, and the exact command that failed. If two pieces of evidence conflict, keep the conflict visible instead of smoothing it over. For example, a successful quick fix is still weak evidence if the same input, account, dependency, or device state has not been tested again. A durable article should help the reader distinguish a confirmed fix from a plausible fix.

### Review Table

| Review Item | What To Confirm | Why It Matters |
| --- | --- | --- |
| Scope | The exact case covered by this article | Prevents over-applying the advice |
| Baseline | The state before any change | Makes rollback and comparison possible |
| Change | The smallest action taken | Reduces hidden side effects |
| Result | The observed output after the change | Separates evidence from expectation |
| Recheck | When to revisit the conclusion | Keeps the post accurate over time |

### Edge Cases and Failure Modes

The main risks are fixing the symptom while leaving the root cause, and mixing unrelated changes into the same test. When the situation involves production data, personal information, money, health, legal rights, or security recovery, the conservative path is to stop and collect evidence before applying a broad fix. The same title can describe very different cases, so the reader should compare their environment with the assumptions in the post before copying commands or decisions.

### Maintenance Standard

Recheck this guidance after dependency, operating-system, or build-tool changes. A useful update does not need to rewrite the entire post; it should confirm whether the examples, links, commands, screenshots, and decision criteria still match current behavior. If the old conclusion remains valid, record the check date. If it changes, explain what changed and why the previous advice is no longer enough.

### Practical Questions Before Acting

- What is the smallest observable signal that proves the problem or decision is real?
- Which source is official, and which part is local judgment?
- What should be captured before making changes?
- What result would show that the guidance did not apply?
- Who needs the record if the same issue appears again?

## Related Reading

Continue with these related posts from the same topic area.

- [How to Fix "SSL: CERTIFICATE_VERIFY_FAILED" Error in Python on Windows](/en_troubleshooting/python-certificate-verify-failed/)
- [How to Fix "Permission denied (publickey)" Error with Git on Windows](/en_troubleshooting/git-permission-denied-publickey-windows/)
