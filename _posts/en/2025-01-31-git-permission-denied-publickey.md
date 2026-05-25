---
typora-root-url: ../
layout: single
title: "How to Fix Git Error: Permission Denied (publickey)"

date: 2025-01-31T07:35:00+09:00
lang: en
translation_id: git-permission-denied-publickey
excerpt: "Resolve the 'Permission denied (publickey)' error in Git by correctly generating an SSH key, adding it to the ssh-agent, and registering it with your Git hosting provider."
seo_description: "Resolve the 'Permission denied (publickey)' error in Git by correctly generating an SSH key, adding it to the ssh-agent, and registering it with your Git hosting provider."
header:
   teaser: /images/header_images/overlay_image_git.png
   overlay_image: /images/header_images/overlay_image_git.png
   overlay_filter: 0.5
   image_description: >
     A visual summary explaining the main topic of this post: How to Fix Git Error: Permission Denied (publickey)
categories:
  - en_Troubleshooting
tags:
  - Git
  - SSH
  - Authentication
  - Troubleshooting
---


![A visual summary explaining the main topic of this post: How to Fix Git Error: Permission Denied (publickey)](/images/header_images/overlay_image_git.png)
## What is the "Permission denied (publickey)" Error?

The `Permission denied (publickey)` error is a common issue that occurs when you try to connect to a remote Git repository (like on GitHub, GitLab, or Bitbucket) using the SSH protocol. It means that the remote server rejected your connection because it couldn't authenticate you with the SSH key you provided.

Essentially, your machine failed to prove to the server that you have the correct credentials to access the repository.

## Common Causes

1.  **No SSH Key**: You haven't generated an SSH key on your local machine.
2.  **SSH Key Not Added to Agent**: Your SSH key exists but the `ssh-agent` (a background program that handles SSH keys) doesn't know about it.
3.  **Public Key Not Added to Git Host**: You have an SSH key, but you haven't uploaded the public part of it to your account on the Git hosting service (e.g., GitHub).
4.  **Incorrect Repository URL**: You are using an HTTPS URL instead of an SSH URL for your remote repository. SSH authentication only works with SSH URLs (e.g., `git@github.com:user/repo.git`).
5.  **Permissions Issue**: The permissions on your `.ssh` directory or the key files are too open, causing SSH to ignore them for security reasons.

## How to Fix It

Here is a step-by-step guide to resolving this error.

### Step 1: Check for an Existing SSH Key

First, check if you already have an SSH key. By default, keys are stored in the `~/.ssh` directory (for Linux/macOS) or `C:\Users\YourUsername\.ssh` (for Windows).

```bash
ls -al ~/.ssh
# Look for files named id_rsa.pub, id_ed25519.pub, or similar
```

If you see a `.pub` file, you already have a key. You can skip to Step 3.

### Step 2: Generate a New SSH Key

If you don't have a key, generate a new one. The Ed25519 algorithm is recommended.

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

When prompted to "Enter a file in which to save the key," press Enter to accept the default location. You can optionally enter a passphrase for extra security.

### Step 3: Add Your SSH Key to the ssh-agent

The `ssh-agent` manages your keys. Make sure it's running and add your new key to it.

```bash
# Start the ssh-agent in the background
eval "$(ssh-agent -s)"

# Add your SSH private key to the agent
ssh-add ~/.ssh/id_ed25519
```

### Step 4: Add Your Public Key to Your Git Host

You need to give your public key to the service hosting your repository.

1.  **Copy the public key** to your clipboard.

    ```bash
    # For macOS/Linux
    cat ~/.ssh/id_ed25519.pub | clip

    # For Windows (in Git Bash)
    cat ~/.ssh/id_ed25519.pub | clip
    # If clip command is not available, open the file and copy its content manually
    ```

2.  **Go to your Git host's website**:
    - **GitHub**: Go to `Settings` > `SSH and GPG keys` > `New SSH key`.
    - **GitLab**: Go to `Preferences` > `SSH Keys`.
3.  **Paste your key**: Give it a descriptive title (e.g., "My Work Laptop") and paste the copied public key into the "Key" field.

### Step 5: Test Your SSH Connection

After adding your key, test the connection to your Git host.

```bash
# For GitHub
ssh -T git@github.com

# For GitLab
ssh -T git@gitlab.com
```

You should see a message like: `Hi [YourUsername]! You've successfully authenticated...`. If you see this, your setup is correct.

### Step 6: Ensure You Are Using the SSH URL

Finally, make sure your repository's remote URL is set to the SSH version, not HTTPS.

```bash
# Check your current remote URL
git remote -v

# If it shows an https:// URL, change it
git remote set-url origin git@github.com:YOUR-USERNAME/YOUR-REPOSITORY.git
```

By following these steps, you can resolve the `Permission denied (publickey)` error and securely connect to your remote repositories.

## Professional Depth Check

For **How to Fix Git Error: Permission Denied (publickey)**, the practical standard is not whether the reader can repeat one instruction once. Treat the topic as a reproducible debugging procedure: verify repository root, branch and remote state, index and working tree, and credential or network boundary before drawing a conclusion. The result should be written as a small decision record, because future readers need to know which fact was observed, which assumption was used, and which condition would change the answer.

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
