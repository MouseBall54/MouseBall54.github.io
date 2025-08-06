---
typora-root-url: ../
layout: single
title: >
   How to Fix "SSL: CERTIFICATE_VERIFY_FAILED" Error in Python on Windows
date: 2025-07-21T22:00:00+09:00
excerpt: "Learn to fix the SSL: CERTIFICATE_VERIFY_FAILED error in Python on Windows by installing certifi, setting REQUESTS_CA_BUNDLE or SSL_CERT_FILE, and using a proper CA bundle."
lang: en
translation_id: python-certificate-verify-failed
header:
   teaser: /images/header_images/overlay_image_python.png
   overlay_image: /images/header_images/overlay_image_python.png
   overlay_filter: 0.5
categories:
  - en_Troubleshooting
tags:
  - SSL
  - Python
  - Windows
  - Security
---

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

