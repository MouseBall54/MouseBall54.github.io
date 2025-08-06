---
typora-root-url: ../
layout: single
title: "How to Fix \"The requested URL returned error: 403\" in Git"

lang: en
translation_id: git-error-403-forbidden
excerpt: "Resolve the Git 403 Forbidden error by updating your credentials, using a personal access token (PAT), or switching to SSH authentication for more secure access."
header:
   teaser: /images/header_images/overlay_image_git.png
   overlay_image: /images/header_images/overlay_image_git.png
   overlay_filter: 0.5
categories:
  - en_Troubleshooting
tags:
  - Git
  - Authentication
  - 403 Forbidden
  - HTTPS
  - SSH
---

## Introduction

The `fatal: unable to access '...': The requested URL returned error: 403` is a common error in Git that indicates an authentication or permission problem. The "403 Forbidden" status code means that the server understood your request but is refusing to authorize it. Essentially, you are trying to do something (like `push`, `pull`, or `clone`) that you don't have permission for. This guide will cover the main reasons for this error and how to fix them.

## Cause 1: Incorrect or Outdated Credentials

The most common reason for a 403 error is that the credentials (username and password) Git is using are incorrect, have expired, or have been revoked. This is especially common since many Git hosting providers like GitHub, GitLab, and Bitbucket have deprecated password-based authentication in favor of more secure methods.

### Solution: Use a Personal Access Token (PAT)

Instead of your account password, you should use a Personal Access Token (PAT). A PAT is a randomly generated string that you can use in place of a password for authenticating to Git over HTTPS. You can create a PAT in your Git provider's settings and give it specific permissions (scopes).

**Steps to use a PAT:**
1.  **Generate a PAT**:
    -   **GitHub**: Go to `Settings` > `Developer settings` > `Personal access tokens` > `Generate new token`.
    -   **GitLab**: Go to `User Settings` > `Access Tokens`.
    -   **Bitbucket**: Go to `Personal settings` > `App passwords`.
    Make sure to grant the token the necessary scopes (e.g., `repo` for full repository access). Copy the token immediately—you won't be able to see it again.
2.  **Update Your Credentials**: When Git prompts you for a password, paste the PAT instead.
    ```bash
    git pull
    Username for 'https://github.com': your-username
    Password for 'https://your-username@github.com': [PASTE YOUR TOKEN HERE]
    ```
3.  **Update Your Credential Helper (Optional)**: Your operating system might have cached your old password. You may need to update it in your system's credential manager.
    -   **Windows**: Go to `Credential Manager` in the Control Panel and find the entry for your Git provider (e.g., `git:https://github.com`). Edit it and replace the old password with your PAT.
    -   **macOS**: Open `Keychain Access`, search for your Git provider, and update the password.
    -   **Linux**: You might need to configure a credential helper like `libsecret` or `gnome-keyring`.

## Cause 2: Insufficient Repository Permissions

You might be authenticated correctly, but the account you are using simply doesn't have the required permissions for the repository you are trying to access.

-   You might be trying to push to a repository for which you only have read access.
-   The repository might be private, and you haven't been granted access.
-   If you are in an organization, your access might have been restricted by an administrator.

### Solution: Check Your Permissions

-   **Verify your role**: On the repository's page on GitHub, GitLab, or Bitbucket, check your access level (e.g., Read, Write, Maintain, Admin).
-   **Contact the owner**: If you believe you should have access, contact the repository owner or an organization administrator to grant you the correct permissions.

## Cause 3: Using the Wrong Authentication Method (HTTPS vs. SSH)

Sometimes, the repository might be configured to prefer or only allow SSH connections. If you are trying to use an HTTPS URL, you might be denied access.

### Solution: Switch to SSH

Using SSH for Git authentication is often more secure and convenient than HTTPS. It uses a key pair to authenticate you instead of a username and password/token.

**Steps to switch to SSH:**
1.  **Check for an existing SSH key**:
    ```bash
    ls -al ~/.ssh
    ```
    Look for files named `id_rsa.pub` or `id_ed25519.pub`.
2.  **Generate a new SSH key** if you don't have one:
    ```bash
    ssh-keygen -t ed25519 -C "your_email@example.com"
    ```
    Follow the prompts to save the key.
3.  **Add your SSH key to your Git provider**:
    -   Copy the contents of your public key file (`id_ed25519.pub`).
        ```bash
        cat ~/.ssh/id_ed25519.pub
        ```
    -   Go to the SSH key settings in your Git provider's user profile and paste the key.
4.  **Update your repository's remote URL**: Change the remote URL from HTTPS to SSH format.
    ```bash
    # View current remote URL
    git remote -v
    # It will look like: https://github.com/user/repo.git

    # Update the URL
    git remote set-url origin git@github.com:user/repo.git
    ```
    Now, when you `push` or `pull`, Git will use your SSH key for authentication, which should resolve the 403 error.

By checking your credentials, permissions, and authentication method, you can effectively troubleshoot and fix the Git 403 Forbidden error.
