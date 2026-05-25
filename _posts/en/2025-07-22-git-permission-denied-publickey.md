---
typora-root-url: ../
layout: single
title: >
  How to Fix "Permission denied (publickey)" Error with Git on Windows
date: 2025-07-22T22:00:00+09:00
excerpt: >
  Fix Git's "Permission denied (publickey)" error on Windows by creating an SSH key, adding it to the SSH agent, and registering it with your Git host.
seo_description: >
  Fix Git's "Permission denied (publickey)" error on Windows by creating an SSH key, adding it to the SSH agent, and registering it with your Git host.
lang: en
translation_id: git-permission-denied-publickey-windows
permalink: /en_troubleshooting/git-permission-denied-publickey-windows/
header:
   teaser: /images/header_images/overlay_image_git.png
   overlay_image: /images/header_images/overlay_image_git.png
   overlay_filter: 0.5
   image_description: >
     A visual summary explaining the main topic of this post: How to Fix "Permission denied (publickey)" Error with Git on Windows
categories:
  - en_Troubleshooting
tags:
  - Git
  - SSH
  - Windows
  - Authentication
---


![A visual summary explaining the main topic of this post: How to Fix "Permission denied (publickey)" Error with Git on Windows](/images/header_images/overlay_image_git.png)
## Introduction

Git over SSH prevents password leaks.
If your SSH key is missing or unregistered, you see:

```
Permission denied (publickey).
fatal: Could not read from remote repository.
```

This guide covers common causes and fixes on Windows.

## What Is the Error?

* Occurs when the SSH client can’t find a valid key for the host.
* Git cannot authenticate you to GitHub, GitLab, Bitbucket, etc.

## Common Causes

1. No SSH key generated.
2. SSH agent not running or key not added.
3. Public key not uploaded to Git host.
4. Wrong file permissions or config settings.

## Solution 1: Generate a New SSH Key

1. Open **Git Bash**.
2. Run:

   ```bash
   ssh-keygen -t ed25519 -C "you@example.com"
   ```
3. Press **Enter** to accept defaults.
4. (Optionally) set a passphrase.

## Solution 2: Add Your Key to the SSH Agent

### In Git Bash

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

### In PowerShell

1. Start the agent:

   ```powershell
   Start-Service ssh-agent
   ```
2. Add the key (adjust path):

   ```powershell
   ssh-add C:\Users\<YourUser>\.ssh\id_ed25519
   ```

## Solution 3: Upload Your Public Key to Git Host

1. Copy your public key:

   ```bash
   cat ~/.ssh/id_ed25519.pub
   ```
2. Log in to **GitHub/GitLab/Bitbucket**.
3. Go to **Settings → SSH and GPG keys → New SSH key**.
4. Paste the key and save.

## Solution 4: Verify the SSH Connection

Run in **Git Bash** or **PowerShell**:

```bash
ssh -T git@github.com
```

Expected response:

```
Hi <username>! You've successfully authenticated.
```

## Additional Tips

* **Check `~/.ssh/config`:**

  ```text
  Host github.com
    User git
    HostName github.com
    IdentityFile ~/.ssh/id_ed25519
  ```
* **File permissions:** Ensure private key is only readable by you. In Git Bash:

  ```bash
  chmod 600 ~/.ssh/id_ed25519
  ```
* **Multiple keys:** Use `ssh-add -l` to list loaded keys.

## Conclusion

Generating an SSH key, adding it to the agent, and registering it with your Git host resolves "Permission denied (publickey)" errors. Follow each step carefully on Windows.

## Professional Depth Check

For **How to Fix "Permission denied (publickey)" Error with Git on Windows**, the practical standard is not whether the reader can repeat one instruction once. Treat the topic as a reproducible debugging procedure: verify repository root, branch and remote state, index and working tree, and credential or network boundary before drawing a conclusion. The result should be written as a small decision record, because future readers need to know which fact was observed, which assumption was used, and which condition would change the answer.

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

## Additional Professional Check

Before applying **How to Fix "Permission denied (publickey)" Error with Git on Windows** in a real workflow, split the conclusion into three checks. First, confirm that the reader's case is inside the scope of the article. Second, preserve evidence such as `git status`, `git remote -v`, and `git branch --show-current`. Third, define the point where the reader should stop, escalate, or ask for review. Without those boundaries, the same article can lead different readers to take different actions.

If repository root, branch and remote state, and index and working tree changes, downgrade the confidence of the conclusion. In that case, trying more fixes is less useful than separating the conditions again. A one-line record for cause, evidence, action, and result makes future comparison possible. This matters for search-driven content because urgent readers often skip context; the post has to make the careful path visible without hiding the practical next step.

Finally, use the article as a checklist rather than a guarantee. Problems involving money, health, personal data, account security, legal rights, or production systems should prioritize evidence preservation and responsibility boundaries over speed. That added structure increases reading time, but it also increases decision quality, which is the point of expanding a short post.

## Related Reading

Continue with these related posts from the same topic area.

- [How to Fix "SSL: CERTIFICATE_VERIFY_FAILED" Error in Python on Windows](/en_troubleshooting/python-certificate-verify-failed/)
- [How to Fix "ModuleNotFoundError: No module named '…'" in Python](/en_troubleshooting/python-modulenotfounderror-no-module-named/)
