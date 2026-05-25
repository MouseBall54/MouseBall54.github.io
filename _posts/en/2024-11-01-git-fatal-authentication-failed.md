---
typora-root-url: ../
layout: single
title: >
  How to Fix Git fatal: Authentication failed for HTTPS Remotes
seo_title: >
  Fix Git fatal Authentication failed
date: 2024-11-01T07:41:00+09:00
last_modified_at: 2026-05-23T23:59:59+09:00
lang: en
translation_id: git-fatal-authentication-failed
header:
   teaser: /images/2026-05-23-git-fatal-authentication-failed/git-authentication-failed-hero.png
   overlay_image: /images/2026-05-23-git-fatal-authentication-failed/git-authentication-failed-hero.png
   overlay_filter: 0.35
   image_description: >
     Visual guide explaining How to Fix Git fatal: Authentication failed for HTTPS Remotes.
excerpt: >
  Fix Git fatal: Authentication failed by checking the remote URL, replacing password authentication with a token or SSH key, clearing stale credentials, and testing push access.
seo_description: >
  Fix Git fatal: Authentication failed by checking the remote URL, using a token or SSH key, clearing stale credentials, and testing push access.
categories:
  - en_Troubleshooting
tags:
  - Git
  - GitHub
  - Authentication
  - SSH
  - Windows
---

## Quick Answer

`fatal: Authentication failed` usually means Git reached the remote server but the credentials were rejected.
For HTTPS remotes, do not use your account password.
Use a supported credential flow such as Git Credential Manager, a personal access token, or switch the remote to SSH.

![Git authentication failure flow with blocked credential gate and successful token path](/images/2026-05-23-git-fatal-authentication-failed/git-authentication-failed-hero.png)

The image shows the typical failure.
Git can find the remote, but the credential gate blocks the request.
The fix is to confirm the remote URL, remove stale credentials, authenticate again, and verify with a small fetch or push.

## Common Symptoms

You may see one of these messages:

```text
fatal: Authentication failed for 'https://github.com/OWNER/REPO.git/'
remote: Invalid username or password.
remote: Support for password authentication was removed.
```

Sometimes the error appears during:

```bash
git clone https://github.com/OWNER/REPO.git
git fetch
git pull
git push
```

The important clue is that the remote URL is reachable.
This is different from a DNS problem, proxy problem, or missing repository.

## 1. Check the Remote URL

Start by checking which remote Git is using.

```bash
git remote -v
```

For HTTPS, it should look like:

```text
origin  https://github.com/OWNER/REPO.git (fetch)
origin  https://github.com/OWNER/REPO.git (push)
```

If the owner or repository name is wrong, fix it:

```bash
git remote set-url origin https://github.com/OWNER/REPO.git
```

If you prefer SSH, use:

```bash
git remote set-url origin git@github.com:OWNER/REPO.git
```

Do not continue until the remote points to the repository you actually have access to.

## 2. Stop Using Account Passwords for HTTPS

Most modern Git hosting providers no longer accept account passwords for Git over HTTPS.
Use a token-based or credential-manager flow instead.

For GitHub, the practical choices are:

- Sign in through Git Credential Manager.
- Use a personal access token with the required repository permissions.
- Switch to SSH and use an SSH key.

If you use a personal access token, treat it like a password.
Do not paste it into code, config files, screenshots, or shell history that will be shared.

## 3. Clear Stale Credentials

This error often continues after you create the correct token because your computer still has an old password cached.

On Windows:

1. Open **Credential Manager**.
2. Go to **Windows Credentials**.
3. Remove old entries for the Git host.
4. Run `git fetch` again and sign in with the new credential flow.

On macOS with Keychain:

1. Open **Keychain Access**.
2. Search for the Git host.
3. Remove stale internet password entries.
4. Run Git again.

With Git Credential Manager, you can also sign out for the host:

```bash
git credential-manager github logout
```

Then retry:

```bash
git fetch origin
```

## 4. Verify Access Before Pushing

Use `git fetch` first.
It is a safer test than `git push` because it does not change the remote.

```bash
git fetch origin
```

If fetch works, check the current branch:

```bash
git branch --show-current
git status
```

Then push only when you know the branch is correct:

```bash
git push origin HEAD
```

If fetch works but push fails, the credentials are valid but may not have write permission.
Check repository permission, organization SSO, branch protection, and token scopes.

## 5. Check Two-Factor Authentication and SSO

If your organization uses SSO or two-factor authentication, a token may still fail until it is authorized for that organization.
This is common in company repositories.

Check:

- Does your account have access to the repository?
- Does the token include the required repository permission?
- Does the organization require SSO authorization?
- Are you pushing to a protected branch?

Authentication and authorization are different.
Authentication proves who you are.
Authorization decides what you may do.

## 6. Consider Switching to SSH

SSH avoids repeated HTTPS credential prompts once the key is configured.

Basic flow:

```bash
ssh-keygen -t ed25519 -C "your-email@example.com"
ssh -T git@github.com
git remote set-url origin git@github.com:OWNER/REPO.git
git fetch origin
```

If `ssh -T` fails, fix SSH first.
Changing the Git remote will not help until the key is loaded and registered with the Git host.

## Common Mistakes

The first mistake is pasting the GitHub website password into Git.
That is not the correct authentication method for HTTPS Git operations.

The second mistake is creating a token but leaving the old password in the credential store.
Git will keep sending the stale credential until you remove it.

The third mistake is using the wrong remote URL.
Authentication can fail if you are accidentally pushing to a private fork or organization repo that your account cannot access.

The fourth mistake is testing with `git push` before checking branch protection.
If `git fetch` works and `git push` fails, the problem may be write permission or branch policy rather than login.

## Professional Depth Check

For **How to Fix Git fatal: Authentication failed for HTTPS Remotes**, the practical standard is not whether the reader can repeat one instruction once. Treat the topic as a reproducible debugging procedure: verify repository root, branch and remote state, index and working tree, and credential or network boundary before drawing a conclusion. The result should be written as a small decision record, because future readers need to know which fact was observed, which assumption was used, and which condition would change the answer.

## Related Reading

- [How to Fix Git Permission denied publickey](/en_troubleshooting/git-permission-denied-publickey/)
- [How to Fix Git fatal: could not read Username Error](/en_troubleshooting/git-fatal-could-not-read-username/)
- [GitHub: Managing personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)
- [GitHub: Caching credentials in Git](https://docs.github.com/en/get-started/git-basics/caching-your-github-credentials-in-git)

## Final Checklist

```text
[ ] `git remote -v` points to the correct repository.
[ ] You are not using an account password for HTTPS Git.
[ ] Old credentials were removed from the credential store.
[ ] `git fetch origin` works.
[ ] Token or account permissions include repository access.
[ ] Organization SSO or branch protection is not blocking the action.
```

Once fetch works with the right account, most authentication failures become permission or branch-policy issues.
Separate those two cases and the fix becomes much faster.

## FAQ

### When should I use this guide?

Use it when you can reproduce the error and need a practical order for checking commands, versions, paths, permissions, and logs.

### What should beginners verify first?

Start with the exact error message, the command you ran, the operating system, and the tool version. These details usually narrow the cause faster than changing many settings at once.

### Which keywords should I search next?

Search for "How to Fix Git fatal: Authentication failed for HTTPS Remotes" together with the exact error text, version, operating system, and tool name used in your environment.
