---
typora-root-url: ../
layout: single
title: >
    Amending the Latest Commit in Git: A Complete Guide to git commit --amend
date: 2025-08-03T16:15:00+09:00
header:
    teaser: /images/header_images/overlay_image_git.png
    overlay_image: /images/header_images/overlay_image_git.png
    overlay_filter: 0.5
excerpt: >
    git commit --amend is a useful command for modifying the most recent commit. It is used to fix the last commit, such as changing the commit message or adding forgotten files.
categories:
    - en_Troubleshooting
tags:
    - Git
    - Commit
    - Amend
---

## What is `git commit --amend`?

`git commit --amend` is a command used to amend (modify) the most recent commit. Instead of creating a new commit, this command **replaces the previous commit with a new one**. This allows you to maintain a clean history by fixing minor mistakes in the latest commit (e.g., a typo in the commit message, adding a forgotten file, or including an unnecessary file) without leaving a separate correction commit.

## Common Use Cases for `git commit --amend`

### 1. Modifying the Latest Commit Message

This is the most common use case. It is used when you notice a typo in the commit message or want to add more details after committing.

1.  **Run the Command**:
    With no changes in the working directory, run the following command.
    ```bash
    git commit --amend
    ```

2.  **Edit the Commit Message**:
    This command will open your default text editor (e.g., Vim, Nano) with the previous commit message. After modifying the message, save it and close the editor to amend the commit.

**Tip**: For a simple message change, you can do it in one line:
```bash
git commit --amend -m "New commit message"
```

### 2. Adding Files to the Latest Commit (Staging Forgotten Files)

This is used when you realize you forgot to include an important file in the commit.

1.  **Stage the Forgotten File**:
    Stage the file you want to add using the `git add` command.
    ```bash
    git add forgotten_file.txt
    ```

2.  **Commit with the `--amend` Option**:
    Using the `--no-edit` option will apply the changes from the staging area to the latest commit without changing the commit message.
    ```bash
    git commit --amend --no-edit
    ```
    If you omit the `--no-edit` option, the commit message editor will open, allowing you to modify the message as well.

### 3. Removing Files from the Latest Commit

This can also be used if you accidentally included a file that should not have been in the commit.

1.  **Remove the File**:
    Use `git rm --cached` to remove the file from the staging area and Git tracking (the file in the working directory will remain).
    ```bash
    git rm --cached unwanted_file.txt
    ```

2.  **Commit with the `--amend` Option**:
    ```bash
    git commit --amend --no-edit
    ```

## How `git commit --amend` Works and Important Precautions

Although `--amend` seems to "modify" the existing commit, internally it works by creating a completely **new commit** and replacing the old one. This means that even if the commit content is similar, the commit ID (hash) will be completely different.

Because of this behavior, there is a very important precaution:

**Never `amend` a commit that has already been pushed to a remote repository.**

If you amend a commit that has been pushed to a shared branch (e.g., `main`, `develop`), your local history will diverge from the remote history. To push in this state, you would have to use the `--force` option, which is a dangerous action that forcibly overwrites the remote history and can cause serious conflicts with your teammates' work.

Therefore, it is safe to use `git commit --amend` **only on commits that are still local**, meaning they have not yet been pushed to a remote repository.

If you need to modify a commit that has already been pushed, the correct way is to use `git revert`, which creates a new commit that undoes the changes.

## Conclusion

`git commit --amend` is a very useful tool for keeping your local repository's commit history clean. It is effective for fixing minor mistakes in the latest commit, such as refining the message or adding forgotten files. However, you must remember that this command changes the commit history and should be used with caution, only on local commits that have not yet been pushed.

