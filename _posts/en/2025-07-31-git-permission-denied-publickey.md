---
typora-root-url: ../
layout: single
title: "How to Fix Git Error: Permission Denied (publickey)"

lang: en
translation_id: git-permission-denied-publickey
excerpt: "Resolve the 'Permission denied (publickey)' error in Git by correctly generating an SSH key, adding it to the ssh-agent, and registering it with your Git hosting provider."
header:
   teaser: /images/header_images/overlay_image_git.png
   overlay_image: /images/header_images/overlay_image_git.png
   overlay_filter: 0.5
categories:
  - en_Troubleshooting
tags:
  - Git
  - SSH
  - Authentication
  - Troubleshooting
---

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
