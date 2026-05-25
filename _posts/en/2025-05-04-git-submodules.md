---
typora-root-url: ../
layout: single
title: >
   How to Use Git Submodules to Manage Project Dependencies

date: 2025-05-04T07:38:00+09:00
lang: en
translation_id: git-submodules
header:
   teaser: /images/header_images/overlay_image_git.png
   overlay_image: /images/header_images/overlay_image_git.png
   overlay_filter: 0.5
   image_description: >
     A visual summary explaining the main topic of this post: How to Use Git Submodules to Manage Project Dependencies
excerpt: >
    Learn how to use `git submodule` to include and manage external repositories as subdirectories within your main project.
seo_description: >
    Learn how to use `git submodule` to include and manage external repositories as subdirectories within your main project.
categories:
  - en_Troubleshooting
tags:
  - Git
  - Submodule
  - Dependency
  - Repository
---


![A visual summary explaining the main topic of this post: How to Use Git Submodules to Manage Project Dependencies](/images/header_images/overlay_image_git.png)
## What are Git Submodules?

A Git submodule allows you to keep a Git repository as a subdirectory of another Git repository. This is a great way to include and manage a dependency on an external library or another component that is developed and maintained separately.

The submodule is a separate Git repository, locked to a specific commit. Your main repository, often called the "superproject," stores a reference to that commit.

## Problem Scenario

You are working on a project that uses a third-party library. You want to include the library's source code directly in your project, but you also want to be able to easily update the library to new versions when they are released.

You could just copy the library's code into your repository, but that makes updating it a manual and error-prone process.

## Solution

### 1. Adding a Submodule

To add a new submodule, you use the `git submodule add` command. You need the URL of the repository and the path where you want to place it.

```bash
git submodule add https://github.com/example/library.git external/library
```

This command does two things:
1.  It clones the `library` repository into the `external/library` directory.
2.  It creates a `.gitmodules` file (or updates it) in your root directory. This file maps the submodule path to its URL.
3.  It stages the new submodule directory and the `.gitmodules` file.

Now, commit the changes to your superproject:
```bash
git commit -m "Add the library submodule"
```

### 2. Cloning a Project with Submodules

When someone else clones your project, the submodule directories will be created, but they will be empty.

To initialize and clone the submodule's content, they need to run:
```bash
git submodule init
git submodule update
```

Alternatively, they can do it in one step by cloning the superproject with the `--recurse-submodules` flag:
```bash
git clone --recurse-submodules https://github.com/your/project.git
```

### 3. Updating a Submodule

Over time, the library you are using will be updated. To pull the latest changes into your submodule:

1.  Navigate into the submodule directory:
    ```bash
    cd external/library
    ```
2.  Fetch the latest changes and check out the desired branch (e.g., `main`):
    ```bash
    git fetch
    git checkout main
    git pull
    ```
3.  Go back to the superproject's root directory:
    ```bash
    cd ../..
    ```
4.  You will see that `external/library` has new changes. Stage and commit this update in your superproject.
    ```bash
    git add external/library
    git commit -m "Update library to the latest version"
    ```

This updates the pointer in your superproject to the new commit in the submodule. Other collaborators can get this update by running `git submodule update --remote`.

## Removing a Submodule

Removing a submodule is a multi-step process:
1.  De-initialize the submodule: `git submodule deinit -f external/library`
2.  Remove the submodule's entry from `.gitmodules` and its directory from the index: `git rm -f external/library`
3.  Remove the submodule's directory from the `.git` directory: `rm -rf .git/modules/external/library`
4.  Commit the changes.

## Conclusion

Git submodules are a powerful way to manage dependencies on external Git repositories. They allow you to keep external code separate while integrating it cleanly into your project. While they can sometimes be tricky to work with, they are invaluable for projects that rely on other version-controlled components.

## Professional Depth Check

For **How to Use Git Submodules to Manage Project Dependencies**, the practical standard is not whether the reader can repeat one instruction once. Treat the topic as a reproducible debugging procedure: verify repository root, branch and remote state, index and working tree, and credential or network boundary before drawing a conclusion. The result should be written as a small decision record, because future readers need to know which fact was observed, which assumption was used, and which condition would change the answer.

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

## Related Reading

Continue with these related posts from the same topic area.

- [How to Fix "SSL: CERTIFICATE_VERIFY_FAILED" Error in Python on Windows](/en_troubleshooting/python-certificate-verify-failed/)
- [How to Fix "Permission denied (publickey)" Error with Git on Windows](/en_troubleshooting/git-permission-denied-publickey-windows/)
