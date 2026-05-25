---
typora-root-url: ../
layout: single
title: >
   How to Fix "SSL: CERTIFICATE_VERIFY_FAILED" Error in Python on Windows
date: 2025-07-21T22:00:00+09:00
excerpt: "Learn to fix the SSL: CERTIFICATE_VERIFY_FAILED error in Python on Windows by installing certifi, setting REQUESTS_CA_BUNDLE or SSL_CERT_FILE, and using a proper CA bundle."
seo_description: "Learn to fix the SSL: CERTIFICATE_VERIFY_FAILED error in Python on Windows by installing certifi, setting REQUESTS_CA_BUNDLE or SSL_CERT_FILE, and using a proper CA bundle."
lang: en
translation_id: python-certificate-verify-failed
header:
   teaser: /images/header_images/overlay_image_python.png
   overlay_image: /images/header_images/overlay_image_python.png
   overlay_filter: 0.5
   image_description: >
     A visual summary explaining the main topic of this post: How to Fix "SSL: CERTIFICATE_VERIFY_FAILED" Error in Python on Windows
categories:
  - en_Troubleshooting
tags:
  - SSL
  - Python
  - Windows
  - Security
---


![A visual summary explaining the main topic of this post: How to Fix "SSL: CERTIFICATE_VERIFY_FAILED" Error in Python on Windows](/images/header_images/overlay_image_python.png)
## Introduction

SSL errors often occur when Python cannot verify a server’s TLS certificate.
Requests to APIs or HTTPS sites fail with an exception.
This post shows common causes and fixes on Windows.

## What Is the Error?

```
SSLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:…)
```

Python raises this in the `ssl` or `requests` library.
It means your client cannot find or trust the CA bundle.

## Common Causes

* Missing or outdated CA certificates.
* Incorrect environment variable settings.
* Corporate proxy intercepting SSL.
* Python not locating the system’s CA store.

## Solution 1: Install and Use Certifi

1. Install the `certifi` package.

   ```bash
   pip install certifi
   ```
2. In your code, point `requests` to certifi’s bundle:

   ```python
   import requests, certifi

   response = requests.get(
       "https://example.com",
       verify=certifi.where()
   )
   print(response.status_code)
   ```

## Solution 2: Set `REQUESTS_CA_BUNDLE`

1. Find the certifi path:

   ```bash
   python -c "import certifi; print(certifi.where())"
   ```
2. In PowerShell, set the env var for current session:

   ```powershell
   setx REQUESTS_CA_BUNDLE "<path-to-cacert.pem>"
   ```
3. Restart PowerShell or your editor.
4. Now `requests` uses that bundle by default.

## Solution 3: Set `SSL_CERT_FILE` on Windows

1. Download a PEM file, e.g., from \[curl.se/docs/caextract.html].
2. In PowerShell, add:

   ```powershell
   setx SSL_CERT_FILE "C:\path\to\cacert.pem"
   ```
3. Restart your terminal or IDE.

## Solution 4: Bypass Verification (Not Recommended)

For quick tests only. Disables security checks.

```python
import requests
response = requests.get("https://example.com", verify=False)
print(response.status_code)
```

> **Warning:** This makes you vulnerable to MITM attacks.

## Solution 5: Use `verify` Parameter Globally

You can configure `verify` for all sessions:

```python
import requests

session = requests.Session()
session.verify = "C:\\path\\to\\cacert.pem"

resp = session.get("https://example.com")
print(resp.ok)
```

## Conclusion

Always prefer a valid CA bundle.
Use certifi or system certificates.
Avoid disabling verification in production.

## Professional Depth Check

For **How to Fix "SSL: CERTIFICATE_VERIFY_FAILED" Error in Python on Windows**, the practical standard is not whether the reader can repeat one instruction once. Treat the topic as a reproducible debugging procedure: verify interpreter path, virtual environment, package version, and input file or data boundary before drawing a conclusion. The result should be written as a small decision record, because future readers need to know which fact was observed, which assumption was used, and which condition would change the answer.

### Evidence That Makes the Guidance Reliable

Use objective evidence before changing a workflow. Good evidence includes `python --version`, `python -m pip show`, the full traceback, and a minimal script. If two pieces of evidence conflict, keep the conflict visible instead of smoothing it over. For example, a successful quick fix is still weak evidence if the same input, account, dependency, or device state has not been tested again. A durable article should help the reader distinguish a confirmed fix from a plausible fix.

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

## Applied Review Scenario

Assume a reader has already tried the first recommendation for **How to Fix "SSL: CERTIFICATE_VERIFY_FAILED" Error in Python on Windows**, but the outcome is still uncertain. The next step is to build a short audit trail instead of trying several fixes at once. Start with one sentence that names the decision, one sentence that names the environment, and one sentence that names the observed result. Then compare interpreter path, virtual environment, package version, and input file or data boundary against the facts already captured. This prevents the article from becoming a list of disconnected tips.

### Audit Trail Template

| Field | Example Standard | Reason |
| --- | --- | --- |
| Observation | What was seen before action | Keeps the baseline objective |
| Evidence | `python --version`, and `python -m pip show` | Anchors the decision in records |
| Assumption | What is believed but not proven | Prevents hidden guesses |
| Action | One change at a time | Makes the result attributable |
| Stop Rule | When to stop and escalate | Reduces repeated trial and error |

### Quality Boundary

The guidance should be treated as strong only when the same result appears after a controlled recheck. If a different account, device, data sample, dependency version, contract term, or official rule is involved, the conclusion should be downgraded to a hypothesis. That distinction is important for search readers because they often arrive with an urgent problem and may skip context. A professional post should slow down the risky part of the decision while still giving a practical next action.

## Related Reading

Continue with these related posts from the same topic area.

- [How to Fix "Permission denied (publickey)" Error with Git on Windows](/en_troubleshooting/git-permission-denied-publickey-windows/)
- [How to Fix "ModuleNotFoundError: No module named '…'" in Python](/en_troubleshooting/python-modulenotfounderror-no-module-named/)
