typora-root-url: ../
layout: single
title: >
    How to Fix JavaScript SyntaxError: Unterminated string literal
seo_title: >
    How to Fix JavaScript SyntaxError: Unterminated string literal
date: 2025-08-05T21:20:00+09:00
header:
   teaser: /images/header_images/overlay_image_js.png
   overlay_image: /images/header_images/overlay_image_js.png
   overlay_filter: 0.5
excerpt: >
    In JavaScript, "SyntaxError: Unterminated string literal" is a syntax error that occurs when a string is not closed properly. This error is usually caused by issues with quotes or line breaks. This post explains the causes of the error and how to fix it.
seo_description: >
    In JavaScript, "SyntaxError: Unterminated string literal" is a syntax error that occurs when a string is not closed properly. This error is usually caused by issues with quotes or line breaks. This post explains the causes of the error and how to fix it.
categories:
  - en_Troubleshooting
tags:
  - JavaScript
  - SyntaxError
  - String
  - Error
---

## The Problem

When writing JavaScript code, you might encounter the `SyntaxError: Unterminated string literal` (or in some browsers, `Uncaught SyntaxError: Invalid or unexpected token`).
This error means that a string literal was not properly terminated.
It usually occurs when there is an opening quote for a string but no closing quote, or when an invalid character is used within the string.

```javascript
// Incorrect Example 1: Missing closing quote
let message = 'Hello, world;

// Incorrect Example 2: Line break inside a string
let htmlString = '<div>
    <p>Hello</p>
</div>';

console.log(message);
console.log(htmlString);
```

Both of the above code snippets will cause a `SyntaxError`.
The first one is missing a closing single quote (`'`).
The second one includes a direct line break within a regular string.

## Cause Analysis

The main causes of this error are:

1.  **Mismatched or Missing Quotes**: The closing quote does not match the opening quote (single `'` vs. double `