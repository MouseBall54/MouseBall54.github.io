---
typora-root-url: ../
layout: single
title: >
    How to Fix "Insecure mixed content" Error in JavaScript
date: 2025-08-03T16:05:00+09:00
header:
    teaser: /images/header_images/overlay_image_js.png
    overlay_image: /images/header_images/overlay_image_js.png
    overlay_filter: 0.5
excerpt: >
    "Insecure mixed content" is a browser security warning that occurs when an HTTPS page loads insecure HTTP resources. This article explains the cause and how to fix it.
categories:
    - en_Troubleshooting
tags:
    - JavaScript
    - HTTPS
    - Security
    - Mixed Content
---

## What is "Insecure mixed content"?

The "Mixed Content" error occurs when the initial HTML is loaded securely over HTTPS, but other resources on the page (such as images, videos, scripts, or stylesheets) are loaded over the insecure HTTP protocol. This weakens the security of the entire page, so modern browsers either block this content or display a warning.

HTTPS encrypts the communication between the user and the website, protecting it from man-in-the-middle attacks. However, if any part of the page is transmitted over HTTP, an attacker could intercept or modify this unencrypted content, potentially gaining control over the entire page.

## Two Types of Mixed Content

1.  **Passive Mixed Content**: Content that can change the display of the page but does not interact with other parts of it (e.g., `<img>`, `<audio>`, `<video>`).
    -   **Browser Behavior**: Most browsers still load this content but will notify the user by changing the lock icon in the address bar or showing a warning in the developer console.

2.  **Active Mixed Content**: Content that can access the entire DOM of the page and change its behavior (e.g., `<script>`, `<link>` (stylesheets), `<iframe>`, `fetch` requests, `XMLHttpRequest`).
    -   **Browser Behavior**: Because the security risk is very high, **most browsers block this content by default**. This can cause the website's functionality to break.

## How to Fix "Insecure mixed content"

### 1. Change All HTTP Links to HTTPS

The most fundamental and reliable solution is to change all `http://` resource requests on your website to `https://`.

**Before:**
```html
<script src="http://example.com/script.js"></script>
<img src="http://example.com/image.jpg">
```

**After:**
```html
<script src="https://example.com/script.js"></script>
<img src="https://example.com/image.jpg">
```

If a resource does not support HTTPS, you will need to find another hosting service or download it and serve it from your own server over HTTPS.

### 2. Use Protocol-Relative URLs

If you omit the protocol (http: or https:) from a URL, the browser will request the resource using the same protocol as the current page. This works flexibly in both HTTP and HTTPS environments.

```html
<!-- If the current page is HTTPS, it requests via https://; if HTTP, it requests via http:// -->
<script src="//example.com/script.js"></script>
<img src="//example.com/image.jpg">
```
**Note**: This method is only effective if the target server supports both HTTP and HTTPS. As of 2024, it is more recommended to explicitly specify `https://` for all resources.

### 3. Use the `Content-Security-Policy` (CSP) Header

You can automatically handle mixed content by setting the `Content-Security-Policy` (CSP) in the server's response headers. The `upgrade-insecure-requests` directive instructs the browser to automatically upgrade all HTTP requests to HTTPS.

**HTTP Response Header Example:**
```
Content-Security-Policy: upgrade-insecure-requests
```

You can also use a `<meta>` tag in your HTML:
```html
<meta http-equiv="Content-Security-Policy" content="upgrade-insecure-requests">
```
This method is very useful when you need to handle a large number of HTTP links at once.

### 4. Use a Mixed Content Scanner

If your website is complex and it is difficult to find all the links manually, you can use online tools like Why No Padlock? or Mixed Content Scan to diagnose mixed content issues on your site.

## Conclusion

The "Insecure mixed content" error is an important browser feature for user security. To resolve this issue, you must ensure that all resources loaded on your website (including your own and third-party resources) are served securely over `https://`. The best practice is to explicitly specify `https://` for all URLs and to enhance security with the `Content-Security-Policy` header.

---
*Work History*
- *2025-08-03: Initial draft created*
