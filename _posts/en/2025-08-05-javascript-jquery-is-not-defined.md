---
typora-root-url: ../
layout: single
title: >
   How to Fix "jQuery is not defined" Error in JavaScript
date: 2025-08-05T11:00:00+09:00
header:
   teaser: /images/header_images/overlay_image_js.png
   overlay_image: /images/header_images/overlay_image_js.png
   overlay_filter: 0.5
excerpt: >
   Resolve the common "Uncaught ReferenceError: jQuery is not defined" by ensuring the jQuery library is loaded correctly before your script attempts to use it. This guide covers the causes and solutions.
categories:
   - en_Troubleshooting
tags:
   - JavaScript
   - jQuery
   - ReferenceError
   - Web Development
   - Troubleshooting
---

## Introduction

The "Uncaught ReferenceError: jQuery is not defined" or "$ is not defined" is a classic error that nearly every web developer encounters when using jQuery. It means that your code is trying to use the jQuery library before it has been loaded and initialized in the browser.

This guide will walk you through the common reasons for this error and provide simple, effective solutions to ensure your jQuery-dependent scripts run smoothly.

## What Causes "jQuery is not defined"?

This error occurs for a few primary reasons, all related to the loading order of scripts in your HTML document.

1.  **Incorrect Script Order**: Your custom script that uses jQuery (`<script src="my_script.js"></script>`) is placed *before* the script that loads the jQuery library (`<script src=".../jquery.min.js"></script>`). The browser executes scripts in the order they appear in the HTML, so your code tries to use jQuery before it exists.
2.  **Failed jQuery Load**: The link to the jQuery library is broken, pointing to the wrong location, or the CDN (Content Delivery Network) is temporarily down. The browser fails to download the library, so it's never defined.
3.  **Asynchronous Loading Issues**: Using `async` or `defer` attributes on your script tags can alter the execution order, potentially causing your code to run before jQuery is ready.
4.  **jQuery Slim Build**: You might be using a "slim" version of jQuery, which excludes the `ajax` and `effects` modules. If your code tries to use functions from these modules (like `$.ajax()`), it can sometimes lead to related errors, though the primary "not defined" error is about the core library itself.

## How to Fix the Error

Let's go through the solutions, starting with the most common fix.

### 1. Check Your Script Loading Order

This is the most frequent cause. Ensure that you include the jQuery library **before** any other scripts that depend on it. The correct order in your HTML file should be:

```html
<!DOCTYPE html>
<html>
<head>
    <title>My Page</title>
</head>
<body>
    <!-- Your HTML content -->

    <!-- 1. Load jQuery first -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>

    <!-- 2. Then load your custom script that uses jQuery -->
    <script src="js/my_script.js"></script>
</body>
</html>
```

Placing scripts at the end of the `<body>` tag is a common best practice, as it allows the browser to render the page content before pausing to parse and execute JavaScript.

### 2. Verify the jQuery Source Path

Double-check the `src` attribute of your jQuery `<script>` tag.

-   **Is the URL correct?** Check for typos in the path to your local file or the CDN link.
-   **Does the file exist?** Open the URL directly in your browser. You should see the jQuery source code. If you get a 404 Not Found error, the path is wrong.

**Example using a local file:**
```html
<!-- Make sure this path is correct relative to your HTML file -->
<script src="libs/jquery/jquery-3.6.0.min.js"></script>
```

**Example using a CDN:**
```html
<!-- A reliable CDN is often the best choice -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
```

### 3. Wrap Your Code in a Document Ready Block

Even if the script tags are in the right order, it's best practice to wait until the DOM (Document Object Model) is fully loaded before running your jQuery code. This prevents issues where your script tries to manipulate HTML elements that don't exist yet.

jQuery provides the `$(document).ready()` function for this purpose.

```javascript
// In your my_script.js file

$(document).ready(function() {
    // All your jQuery code goes here
    $('#my-button').click(function() {
        alert('Button clicked!');
    });
});

// A shorter, equivalent syntax is also common:
$(function() {
    // All your jQuery code goes here
    $('h1').css('color', 'blue');
});
```

This ensures that the code inside the function only runs after jQuery is loaded and the page structure is ready.

### 4. Check for Network Issues or Ad Blockers

-   **Network Connectivity**: Make sure you are connected to the internet, especially if you are using a CDN.
-   **Ad Blockers**: Some aggressive ad blockers or browser extensions might block requests to certain CDNs. Try disabling them to see if it resolves the issue.

## Conclusion

The "jQuery is not defined" error is almost always a loading issue. By ensuring your `<script>` tags are in the correct order, verifying the path to the jQuery file, and wrapping your code in a `$(document).ready()` block, you can eliminate this error and build reliable, jQuery-powered applications. Always load your dependencies first—it's a fundamental rule of web development.
