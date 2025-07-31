---
typora-root-url: ../
layout: single
title: "How to Fix Git Error: The requested URL returned error: 403"
date: 2025-07-31T11:30:00+09:00
excerpt: "Resolve Git's '403 Forbidden' error by updating your credentials, using a personal access token (PAT), or checking your repository permissions. Learn the steps to fix this common authentication issue."
categories:
  - en_Troubleshooting
tags:
  - Git
  - Authentication
  - Error 403
  - Troubleshooting
---

## What is the "The requested URL returned error: 403" Error?

When you try to `git push`, `git pull`, or `git clone` from a remote repository, you might see the error message `fatal: The requested URL returned error: 403`. This is an HTTP status code that means "Forbidden." In the context of Git, it indicates that you do not have the necessary permissions to access the repository with the credentials you provided.

This is purely an authentication or authorization issue. It's not a problem with your local repository's code or history.

## Common Causes and Solutions

Here are the most common reasons for a 403 error and how to resolve them.

### 1. Incorrect or Outdated Credentials

Your saved Git credentials (username and password) might be incorrect or may have expired. This is especially common if you've recently changed your password on your Git hosting service (like GitHub, GitLab, or Bitbucket).

#### Solution: Update Your Credentials

The easiest way to fix this is to update your saved credentials. Most modern Git clients use a credential manager to store this information.

**On Windows:**

1.  Open the **Credential Manager** from the Control Panel.
2.  Go to the **Windows Credentials** tab.
3.  Find the entry for your Git hosting service (e.g., `git:https://github.com`).
4.  Click **Edit** to update your password or **Remove** to delete the entry. If you remove it, Git will prompt you for your username and password the next time you connect.

**On macOS:**

1.  Open the **Keychain Access** application.
2.  Search for your Git hosting service (e.g., "github.com").
3.  Find the "internet password" entry and either update it or delete it. Git will ask for credentials on the next attempt.

**On Linux:**

If you have a credential helper configured, you can force Git to forget the old credentials. The exact command depends on your setup, but you can often clear it by reconfiguring the helper or manually editing the stored credentials file (e.g., `~/.git-credentials`).

A simpler approach is to update the remote URL to include your username, which forces a password prompt:

```bash
git remote set-url origin https://<YOUR_USERNAME>@github.com/<USERNAME>/<REPO>.git
```

When you push or pull next, Git will ask for your password.

### 2. Using a Password Instead of a Personal Access Token (PAT)

Most major Git providers, including GitHub, no longer accept password authentication for Git operations over HTTPS. Instead, you must use a **Personal Access Token (PAT)**.

#### Solution: Create and Use a PAT

1.  **Generate a PAT:**
    *   **GitHub:** Go to **Settings > Developer settings > Personal access tokens > Tokens (classic)** and click **Generate new token**. Give it a descriptive name and select the necessary scopes (e.g., `repo` for full repository access).
    *   **GitLab:** Go to **Preferences > Access Tokens**.
    *   **Bitbucket:** Go to **Personal settings > App passwords**.

2.  **Copy the PAT:** Save the token somewhere safe immediately. You won't be able to see it again.

3.  **Use the PAT:** When Git prompts for your password, enter the PAT instead.

If your credentials are cached, follow the steps in the previous section to clear them first. Then, the next time you perform a Git operation, use your username and the PAT as your password.

### 3. Insufficient Repository Permissions

The 403 error can also mean that your account simply doesn't have permission to perform the action you're attempting. For example, you might be trying to push to a repository where you only have read access.

#### Solution: Check Your Permissions

*   **Collaborator Access:** Verify with the repository owner that you have been added as a collaborator with the correct permissions (e.g., "Write" or "Maintain" access to push changes).
*   **Organization/Team Access:** If the repository belongs to an organization, ensure you are a member of a team with the appropriate access level.
*   **Fork and Pull Request:** If you don't have write access, the standard workflow is to fork the repository, push changes to your fork, and then open a pull request to the original repository.

### 4. Single Sign-On (SSO) Issues

If your organization uses Single Sign-On (SSO) with your Git provider, you may need to authorize your PAT to be used with SSO-protected repositories.

#### Solution: Authorize Your PAT for SSO

When you create a PAT on GitHub, you will see an option to **"Configure SSO"** or **"Authorize"** the token for use with your organization's resources. Make sure you complete this step. If you have an existing PAT, you may need to enable it for SSO from the token settings page.

## Conclusion

A `403 Forbidden` error in Git is almost always tied to authentication or permissions. By systematically checking your credentials, switching to a Personal Access Token, and verifying your repository access rights, you can quickly resolve this error. When in doubt, start by clearing your old credentials and trying again with a fresh PAT.
