---
typora-root-url: ../
layout: single
title: >
   Mastering async/await Error Handling in JavaScript

lang: en
translation_id: javascript-async-await-error-handling
header:
   teaser: /images/header_images/overlay_image_js.png
   overlay_image: /images/header_images/overlay_image_js.png
   overlay_filter: 0.5
excerpt: >
   Learn how to properly handle errors in async/await functions using try...catch blocks in JavaScript. Avoid unhandled promise rejections and write robust, reliable asynchronous code.
categories:
   - en_Troubleshooting
tags:
   - JavaScript
   - async/await
   - Promises
   - Error Handling
   - try...catch
---

## Introduction

`async/await`, introduced in ES2017, provides a much cleaner and more readable syntax for working with Promises in JavaScript. It allows you to write asynchronous code that looks and behaves like synchronous code. However, one area that can trip up developers is error handling. A forgotten `.catch()` on a promise chain can lead to silent failures or unhandled promise rejections.

This guide will show you the standard and most effective way to handle errors in `async/await` functions: the `try...catch` block.

## Why Error Handling is Crucial for `async/await`

When you `await` a promise, one of two things can happen:
1.  The promise **fulfills**, and the `await` expression returns the fulfilled value.
2.  The promise **rejects**, and the `await` expression throws an error. This is the key part.

If a promise rejection is not caught, it becomes an "unhandled promise rejection," which can crash a Node.js application or lead to silent, hard-to-debug failures in the browser.

**Incorrect Code (No Error Handling):**
```javascript
async function fetchUserData() {
    // If this fetch fails, the error will be unhandled!
    const response = await fetch('https://api.example.com/non-existent-user');
    const data = await response.json();
    console.log(data);
}

fetchUserData(); // This might cause an "Uncaught (in promise) TypeError"
```
In the code above, if the `fetch` promise rejects (e.g., due to a 404 error or network failure), the entire program might halt with an uncaught error.

## The `try...catch` Solution

The `try...catch` statement is the cornerstone of error handling in synchronous JavaScript, and it works perfectly with `async/await`.

You wrap the "risky" asynchronous code (the `await` calls) in a `try` block. If any of the awaited promises reject, the code execution immediately jumps to the `catch` block, where you can handle the error gracefully.

**Correct Code (with `try...catch`):**
```javascript
async function fetchUserData() {
    try {
        console.log("Fetching user data...");
        const response = await fetch('https://api.example.com/non-existent-user');

        // Check for HTTP errors like 404 or 500
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();
        console.log("Data received:", data);
        return data;
    } catch (error) {
        console.error("Failed to fetch user data:", error.message);
        // You can show a message to the user, log the error, etc.
        return null; // Return a fallback value
    }
}

fetchUserData();
```

### How it Works:
1.  The code inside the `try` block is executed.
2.  If `fetch()` rejects, or if we `throw` a new error manually (like for a bad HTTP status), the control is passed to the `catch (error)` block.
3.  The `error` object contains information about what went wrong.
4.  The `catch` block handles the failure, preventing the application from crashing.

## Handling Multiple `await` Calls

A single `try...catch` block can handle failures from multiple `await` expressions. The first one that rejects will cause execution to jump to the `catch` block, and subsequent lines in the `try` block will not be executed.

```javascript
async function fetchUserAndPosts(userId) {
    try {
        const userResponse = await fetch(`https://api.example.com/users/${userId}`);
        if (!userResponse.ok) throw new Error("Failed to fetch user");
        const userData = await userResponse.json();

        // If the first fetch fails, this line is never reached
        const postsResponse = await fetch(`https://api.example.com/posts?userId=${userId}`);
        if (!postsResponse.ok) throw new Error("Failed to fetch posts");
        const postsData = await postsResponse.json();

        return { user: userData, posts: postsData };
    } catch (error) {
        console.error("An error occurred:", error.message);
        return null;
    }
}
```

## An Alternative: Using `.catch()`

While `try...catch` is the most common pattern, you can also handle errors by chaining a `.catch()` to the `async` function call. This is useful if you want the calling code to be responsible for handling the error.

First, the `async` function is written to let errors propagate (by not using `try...catch` inside it).

```javascript
async function getUser(userId) {
    // No try...catch here. Errors will be thrown.
    const response = await fetch(`https://api.example.com/users/${userId}`);
    if (!response.ok) {
        throw new Error(`User not found: ${response.status}`);
    }
    return response.json();
}
```

Then, the caller handles the error:

```javascript
console.log("Attempting to get user...");

getUser('invalid-user-id')
    .then(user => {
        console.log("User found:", user);
    })
    .catch(error => {
        console.error("Error in caller:", error.message);
        // Handle the error here
    });

console.log("Request initiated.");
```

This approach is useful for creating reusable async functions where the error handling logic might change depending on where the function is called.

## Conclusion

Proper error handling is non-negotiable for building robust applications. With `async/await`, the `try...catch` block is your primary tool. It provides a clean, synchronous-looking way to manage promise rejections and other exceptions.

**Key Takeaways:**
-   Always wrap your `await` calls in a `try...catch` block to handle potential promise rejections.
-   A rejected promise in an `async` function will throw an error that can be caught.
-   Check `response.ok` for `fetch` calls to handle HTTP errors (like 404) that don't cause a promise rejection by default.
-   Alternatively, use `.catch()` on the `async` function call itself to delegate error handling to the caller.

By mastering `try...catch` with `async/await`, you can write asynchronous code that is not only clean and readable but also resilient and reliable.
