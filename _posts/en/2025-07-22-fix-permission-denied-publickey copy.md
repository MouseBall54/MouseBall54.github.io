---
typora-root-url: ../
layout: single
title: "How to Fix “Permission denied (publickey)” Error with Git on Windows"
date: 2025-07-22T22:00:00+09:00
excerpt: "Fix Git’s “Permission denied (publickey)” error on Windows by creating an SSH key, adding it to the SSH agent, and registering it with your Git host."
header:
   teaser: /images/header_images/overlay_image_python.png
   overlay_image: /images/header_images/overlay_image_python.png
   overlay_filter: 0.5
categories:
  - en_Troubleshooting
tags:
  - Git
  - SSH
  - Windows
  - Authentication
---

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

Generating an SSH key, adding it to the agent, and registering it with your Git host resolves “Permission denied (publickey)” errors. Follow each step carefully on Windows.

