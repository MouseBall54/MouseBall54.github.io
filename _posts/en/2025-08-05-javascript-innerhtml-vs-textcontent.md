---
typora-root-url: ../
layout: single
title: >
   JavaScript innerHTML vs. textContent: Which Should You Use?
date: 2025-08-05T11:05:00+09:00
header:
   teaser: /images/header_images/overlay_image_js.png
   overlay_image: /images/header_images/overlay_image_js.png
   overlay_filter: 0.5
excerpt: >
   Understand the key differences between innerHTML and textContent in JavaScript. Learn when to use each property for better security, performance, and predictability in your web applications.
categories:
   - en_Troubleshooting
tags:
   - JavaScript
   - DOM
   - innerHTML
   - textContent
   - Security
---

## Introduction

When you need to get or set the content of an HTML element using JavaScript, you'll quickly come across two common properties: `innerHTML` and `textContent`. While they might seem similar, they have crucial differences in how they handle content, which impacts security, performance, and behavior. Choosing the right one is essential for writing robust and secure code.

This guide will compare `innerHTML` and `textContent` to help you decide which one to use in different scenarios.

## What is `innerHTML`?

The `innerHTML` property gets or sets the HTML markup contained within an element. When you set `innerHTML`, the browser parses the string you provide as HTML and rebuilds the DOM tree for that element.

**Example:**
```html
<div id="my-div">This is some <strong>old</strong> text.</div>
```

```javascript
const myDiv = document.getElementById('my-div');

// Getting content
console.log(myDiv.innerHTML);
// Output: This is some <strong>old</strong> text.

// Setting content
myDiv.innerHTML = 'This is some <span>new</span> text.';
// The div now contains the new HTML content, including the span element.
```

### Key Characteristics of `innerHTML`
-   **Parses HTML**: It recognizes and renders HTML tags.
-   **Security Risk**: It is vulnerable to Cross-Site Scripting (XSS) attacks. If you set `innerHTML` with untrusted user input, a malicious user could inject a `<script>` tag or other harmful markup that will be executed by the browser.
-   **Performance**: It is generally slower than `textContent` because it involves the overhead of parsing HTML and rebuilding the DOM.

## What is `textContent`?

The `textContent` property gets or sets the raw text content of an element and all its descendants, without any HTML markup.

**Example:**
```html
<div id="my-div">This is some <strong>old</strong> text.</div>
```

```javascript
const myDiv = document.getElementById('my-div');

// Getting content
console.log(myDiv.textContent);
// Output: This is some old text.

// Setting content
myDiv.textContent = 'This is some <span>new</span> text.';
// The div now contains the literal string "This is some <span>new</span> text."
// The <span> tags are not parsed; they are displayed as plain text.
```

### Key Characteristics of `textContent`
-   **Plain Text Only**: It treats all content as raw text and does not parse HTML tags.
-   **Secure**: It automatically sanitizes the content by rendering HTML tags as literal text, effectively preventing XSS attacks.
-   **Performance**: It is much faster than `innerHTML` because it involves a direct manipulation of text nodes without any HTML parsing.
-   **Aware of CSS**: `textContent` returns the text of all elements, including those hidden by CSS (e.g., `display: none;`). In contrast, the similar `innerText` property would not include hidden text.

## `innerHTML` vs. `textContent`: The Showdown

| Feature          | `innerHTML`                                       | `textContent`                                           |
| ---------------- | ------------------------------------------------- | ------------------------------------------------------- |
| **Content Type** | HTML string                                       | Plain text string                                       |
| **Security**     | **Vulnerable to XSS**. Use only with trusted content. | **Secure by default**. Automatically sanitizes HTML.    |
| **Performance**  | Slower (due to HTML parsing)                      | Faster (direct text manipulation)                       |
| **Usage**        | When you explicitly need to render HTML markup.   | When you only need to work with plain text.             |
| **Output**       | Returns HTML tags, comments, and text.            | Returns only the text content.                          |

## Which One Should You Use?

Here’s a simple rule of thumb:

> **Always default to `textContent` unless you have a specific and safe reason to use `innerHTML`.**

-   **Use `textContent` when:**
    -   You are setting text that comes from user input.
    -   You only need to display or update plain text.
    -   Security and performance are priorities.

-   **Use `innerHTML` only when:**
    -   You are setting content that you have full control over (e.g., a hardcoded template).
    -   You explicitly need to generate and insert HTML elements (like `<strong>`, `<span>`, `<a>`, etc.) into the DOM.

### A Note on `innerText`

There is a third, similar property called `innerText`. It is different from `textContent` in a few ways:
-   `innerText` is CSS-aware and will not return the text of elements hidden with `display: none;`.
-   `innerText` triggers a reflow (a performance-heavy recalculation of the layout), whereas `textContent` does not.
-   It has some inconsistent behavior across older browsers.

For these reasons, **`textContent` is generally the preferred property** for performance and predictability, unless you specifically need the CSS-aware behavior of `innerText`.

## Conclusion

Understanding the difference between `innerHTML` and `textContent` is crucial for writing secure and efficient JavaScript. While `innerHTML` is powerful for creating dynamic HTML, its security risks cannot be ignored. `textContent` provides a safer and faster alternative for all plain-text operations.

By making a conscious choice between the two, you can protect your applications from XSS vulnerabilities and ensure better performance. Remember: **use `textContent` by default, and `innerHTML` with caution.**
