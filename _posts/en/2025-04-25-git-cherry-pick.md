---
typora-root-url: ../
layout: single
title: >
   How to Cherry-Pick a Commit from Another Branch in Git

date: 2025-04-25T07:29:00+09:00
lang: en
translation_id: git-cherry-pick
header:
   teaser: /images/header_images/overlay_image_git.png
   overlay_image: /images/header_images/overlay_image_git.png
   overlay_filter: 0.5
   image_description: >
     A visual summary explaining the main topic of this post: How to Cherry-Pick a Commit from Another Branch in Git
excerpt: >
    Learn how to use `git cherry-pick` to apply a specific commit from one branch to another without merging the entire branch.
seo_description: >
    Learn how to use `git cherry-pick` to apply a specific commit from one branch to another without merging the entire branch.
categories:
  - en_Troubleshooting
tags:
  - Git
  - Cherry-pick
  - Commit
  - Branch
---


![A visual summary explaining the main topic of this post: How to Cherry-Pick a Commit from Another Branch in Git](/images/header_images/overlay_image_git.png)
## What is Git Cherry-Pick?

`git cherry-pick` is a command that allows you to pick a commit from one branch and apply it onto another. This is useful when you need a specific change from another branch, but you don't want to merge the entire branch. It avoids introducing unrelated changes.

## Problem Scenario

Suppose you have two branches: `main` and `feature`. A critical bug was fixed in the `feature` branch. You need to apply this fix to the `main` branch immediately, without merging the whole `feature` branch, which is still under development.

**`feature` branch log:**
```bash
git log --oneline feature
a1b2c3d (feature) Add new experimental feature
d4e5f6g Fix critical bug #123
cba1a2d Start developing feature
```

**`main` branch log:**
```bash
git log --oneline main
f30abf4 (HEAD -> main) Release version 1.0
```

We need to get the commit `d4e5f6g` into the `main` branch.

## Solution

### 1. Switch to the Target Branch

First, ensure you are on the branch where you want to apply the commit. In this case, it's the `main` branch.

```bash
git switch main
```

### 2. Find the Commit Hash

You need the hash of the commit you want to cherry-pick. You can get this from the log of the other branch.

```bash
git log --oneline feature
```

From the output, the commit hash for the bug fix is `d4e5f6g`.

### 3. Run `git cherry-pick`

Now, use the `cherry-pick` command with the commit hash.

```bash
git cherry-pick d4e5f6g
```

Git will take the changes from that commit and apply them as a new commit on your current branch (`main`). The new commit will have a different hash but will contain the same changes and a similar commit message.

### 4. Verify the Result

Check the log of the `main` branch to see the new commit.

```bash
git log --oneline main
e9f8d7c (HEAD -> main) Fix critical bug #123
f30abf4 Release version 1.0
```

The fix is now on the `main` branch.

## Handling Conflicts

Sometimes, a cherry-pick can result in a merge conflict. This happens if the changes in the commit you are picking conflict with the current state of your branch.

If a conflict occurs, Git will stop and let you resolve it.
1.  Open the conflicting files.
2.  Manually edit the files to resolve the conflict. Look for the `<<<<<<<`, `=======`, and `>>>>>>>` markers.
3.  After resolving, stage the changes using `git add <file_name>`.
4.  Continue the cherry-pick process by running:
    ```bash
    git cherry-pick --continue
    ```

If you want to abort the cherry-pick, you can use:
```bash
git cherry-pick --abort
```

## Conclusion

`git cherry-pick` is a precise tool for applying specific commits from one branch to another. It's perfect for situations like hotfixes or selectively sharing features between branches. Use it carefully to avoid creating duplicate changes where a merge would be more appropriate.

## Professional Depth Check

For **How to Cherry-Pick a Commit from Another Branch in Git**, the practical standard is not whether the reader can repeat one instruction once. Treat the topic as a reproducible debugging procedure: verify repository root, branch and remote state, index and working tree, and credential or network boundary before drawing a conclusion. The result should be written as a small decision record, because future readers need to know which fact was observed, which assumption was used, and which condition would change the answer.

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
