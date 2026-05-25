---
typora-root-url: ../
layout: single
title: >
   How to Use `git bisect` to Find the Commit That Introduced a Bug

date: 2025-04-24T07:28:00+09:00
lang: en
translation_id: git-bisect
header:
   teaser: /images/header_images/overlay_image_git.png
   overlay_image: /images/header_images/overlay_image_git.png
   overlay_filter: 0.5
   image_description: >
     A visual summary explaining the main topic of this post: How to Use `git bisect` to Find the Commit That Introduced a Bug
excerpt: >
    A step-by-step guide on using `git bisect` to perform a binary search on your commit history and quickly pinpoint the exact commit that caused a bug.
seo_description: >
    A step-by-step guide on using `git bisect` to perform a binary search on your commit history and quickly pinpoint the exact commit that caused a bug.
categories:
  - en_Troubleshooting
tags:
  - Git
  - Bisect
  - Debugging
  - Bug
  - Commit
---


![A visual summary explaining the main topic of this post: How to Use git bisect to Find the Commit That Introduced a Bug](/images/header_images/overlay_image_git.png)
## What is `git bisect`?

`git bisect` is a powerful debugging tool in Git. It helps you find the specific commit that introduced a bug by performing an automated binary search through your project's commit history. 

Instead of manually checking out and testing each commit one by one, `git bisect` quickly narrows down the search space, making the process much faster and more efficient.

## Problem Scenario

You know that your application was working correctly a week ago, but now a feature is broken. You have hundreds of commits between the last known good state and the current broken state. Finding the exact commit that caused the issue would be very time-consuming.

## Solution: Using `git bisect`

Here’s how to use `git bisect` to find the problematic commit.

### 1. Start the Bisect Process

First, you need to start the bisect session. 

```bash
git bisect start
```

### 2. Mark the Bad and Good Commits

Next, you need to tell Git two things:
-   A "bad" commit where the bug is present.
-   A "good" commit where the bug is not present.

Usually, the current commit (`HEAD`) is the bad one.
```bash
git bisect bad HEAD
```

Then, you provide the hash or tag of a commit that you know was working correctly.
```bash
git bisect good <commit_hash_or_tag>
# Example:
git bisect good v1.0.0
```

### 3. Test and Repeat

Once you've marked the good and bad commits, `git bisect` will check out a commit halfway between them. It will then say something like:

```
Bisecting: 675 revisions left to test after this (roughly 10 steps)
```

Now, you need to test your code at this commit to see if the bug exists.
-   If the bug **is present**, tell Git this commit is "bad":
    ```bash
    git bisect bad
    ```
-   If the bug **is not present**, tell Git this commit is "good":
    ```bash
    git bisect good
    ```

Git will then check out another commit, again halfway between the new good and bad boundaries. You repeat this process of testing and marking commits as `good` or `bad`.

### 4. Identify the First Bad Commit

After a few steps, Git will have narrowed down the possibilities to a single commit. It will print a message like this:

```
c1a2b3d is the first bad commit
commit c1a2b3d
Author: John Doe <john.doe@example.com>
Date:   Mon Aug 5 10:00:00 2025 +0000

    Refactor the login module

... file changes ...
```

This is the commit that introduced the bug. You can now examine its changes to understand what went wrong.

### 5. End the Bisect Session

Once you have found the bad commit, you should end the bisect session to return to your original state (`HEAD`).

```bash
git bisect reset
```

## Automating the Process

You can even automate the testing step if you have a script that can determine whether the code is good or bad (e.g., a test suite).

The `git bisect run` command takes a script as an argument. Git will run the script on each step. 
-   If the script exits with code `0`, the commit is marked `good`.
-   If it exits with any other code (between `1` and `127`, except `125`), it's marked `bad`.

```bash
# Example: using a test script
git bisect run npm test
```

## Conclusion

`git bisect` is an incredibly useful tool for quickly tracking down regressions in your codebase. By automating the search for a bug-introducing commit, it saves you a significant amount of time and effort in the debugging process.

## Professional Depth Check

For **How to Use `git bisect` to Find the Commit That Introduced a Bug**, the practical standard is not whether the reader can repeat one instruction once. Treat the topic as a reproducible debugging procedure: verify repository root, branch and remote state, index and working tree, and credential or network boundary before drawing a conclusion. The result should be written as a small decision record, because future readers need to know which fact was observed, which assumption was used, and which condition would change the answer.

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

## Related Reading

Continue with these related posts from the same topic area.

- [How to Fix "SSL: CERTIFICATE_VERIFY_FAILED" Error in Python on Windows](/en_troubleshooting/python-certificate-verify-failed/)
- [How to Fix "Permission denied (publickey)" Error with Git on Windows](/en_troubleshooting/git-permission-denied-publickey-windows/)
