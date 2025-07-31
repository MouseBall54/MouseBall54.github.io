---
typora-root-url: ../
layout: single
title: "How to Fix Cross-Origin Read Blocking (CORB) Errors"
date: 2025-07-31T22:00:00+09:00
header:
   overlay_image: /images/header_images/overlay_image_js.png
   overlay_filter: 0.5
excerpt: >
  Resolve Cross-Origin Read Blocking (CORB) warnings in your browser by ensuring the server sends the correct Content-Type and CORS headers for your API requests.
categories:
  - en_Troubleshooting
tags:
  - JavaScript
  - CORB
  - CORS
  - Web Security
  - Fetch
---

You may have encountered a warning message in your browser's developer console like "Cross-Origin Read Blocking (CORB) blocked cross-origin response..." This is not a traditional error that breaks your code, but a security warning indicating the browser has blocked a response for safety.

This post will explain what CORB is, why it occurs, and how to fix it.

### What is Cross-Origin Read Blocking (CORB)?

CORB is a web security feature designed to prevent certain cross-origin network responses from being delivered to a web page. Its primary goal is to mitigate side-channel attacks like Spectre, where sensitive data could be leaked from the memory of other applications.

It works by inspecting the `Content-Type` of a response. If the response is for a resource that shouldn't be embedded in a script or style sheet (like HTML, XML, or JSON) but is requested from a context that expects one (e.g., `<script>`, `<img>`), CORB may block it.

### Common Causes of CORB Warnings

The most common cause is a mismatch between the `Content-Type` header sent by the server and the type of content the browser expects.

1.  **Incorrect `Content-Type` Header**: The server is sending a resource with a generic or incorrect `Content-Type`. For example, an API endpoint that should return `application/json` is instead sending `text/html`.
2.  **`X-Content-Type-Options: nosniff` Header**: This security header tells the browser not to guess (or "sniff") the MIME type. If the `Content-Type` is incorrect and `nosniff` is active, the browser will trust the incorrect header and may trigger CORB.

### How to Fix CORB Issues

The solution almost always involves fixing the server-side configuration.

#### Step 1: Check the Response Headers

First, use your browser's developer tools to inspect the network request that triggered the warning.

1.  Open Developer Tools (F12 or Ctrl+Shift+I).
2.  Go to the "Network" tab.
3.  Find the problematic request.
4.  Look at the "Response Headers" section and check the value of `Content-Type`.

You will likely find that an API call is returning `text/html` or `text/plain` instead of `application/json`.

#### Step 2: Correct the `Content-Type` on the Server

The primary fix is to ensure your server sends the correct `Content-Type` header.

For example, if you have a Node.js Express server, your API endpoint should explicitly set the header.

```javascript
// Before (Incorrect)
app.get('/api/data', (req, res) => {
  // The server might default to text/html
  res.send({ message: 'This is JSON data' });
});

// After (Correct)
app.get('/api/data', (req, res) => {
  res.setHeader('Content-Type', 'application/json');
  res.json({ message: 'This is JSON data' });
});
```
Using `res.json()` in Express automatically sets the `Content-Type` to `application/json`.

#### Step 3: Ensure Proper CORS Configuration

While CORB is different from CORS (Cross-Origin Resource Sharing), they are related. A misconfigured CORS policy can lead to issues. Make sure your server includes the `Access-Control-Allow-Origin` header in its response.

```javascript
// Example in Node.js/Express
app.use((req, res, next) => {
  res.setHeader('Access-Control-Allow-Origin', 'https://your-frontend-domain.com');
  // ... other CORS headers
  next();
});
```

#### Step 4: Use a Proxy Server (If You Can't Change the Server)

If you are consuming a third-party API and cannot change its server-side headers, the only viable workaround is to set up a proxy server.

Your frontend application would make a request to your proxy, which then requests the data from the third-party API. The proxy can then forward the response back to your application with the correct `Content-Type` and CORS headers.

### Conclusion

A CORB warning is a sign that your browser is protecting you from potential security vulnerabilities. It is almost always caused by a server sending an incorrect `Content-Type` header for a requested resource. The best solution is to fix the server's response headers to accurately describe the content being sent.
