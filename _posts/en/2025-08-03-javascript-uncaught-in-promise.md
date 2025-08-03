---
typora-root-url: ../
layout: single
title: >
    How to Fix JavaScript Uncaught (in promise) Error
date: 2025-08-03T10:20:00+09:00
header:
   teaser: /images/header_images/overlay_image_js.png
   overlay_image: /images/header_images/overlay_image_js.png
   overlay_filter: 0.5
excerpt: >
    Learn how to resolve the `Uncaught (in promise)` error in JavaScript, which appears when a Promise rejection is not handled by a `.catch()` block or a try...catch statement.
categories:
  - en_Troubleshooting
tags:
  - JavaScript
  - Promise
  - async/await
  - Error Handling
---

## The Problem

When working with Promises for asynchronous operations in JavaScript, you may see an `Uncaught (in promise)` error in your console. This error means that a Promise was rejected, but there was no error handler (`.catch()` block or a `try...catch` statement) to deal with the rejection.

Asynchronous operations, like API requests or file I/O, can either succeed or fail. A Promise represents this eventual completion or failure. When it fails, it enters a `rejected` state. It is crucial for developers to handle this state to prevent unexpected behavior in the application.

## Example of Error-Prone Code

The following example uses the `fetch` API to make a request to a non-existent URL. The Promise will be rejected due to a network error, but there is no code to handle this rejection.

```javascript
// Requesting a non-existent API endpoint
fetch('https://api.example.com/non-existent-endpoint')
  .then(response => {
    if (!response.ok) {
      // You must throw an error here for the .catch() block to catch it
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    console.log(data);
  });

// Since there is no .catch() block, the error thrown above is not handled.
// Result: Uncaught (in promise) Error: Network response was not ok
```

## How to Fix It

There are two primary ways to handle errors in Promises.

### 1. Add a `.catch()` Method

The most common way is to append a `.catch()` method to the end of your Promise chain. If an error is thrown in any of the `.then()` blocks, the execution flow will immediately jump to the nearest `.catch()` block down the chain.

```javascript
fetch('https://api.example.com/non-existent-endpoint')
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    console.log(data);
  })
  .catch(error => {
    console.error('There has been a problem with your fetch operation:', error);
    // You can perform follow-up actions here, like showing an error message to the user.
  });
```

By adding `.catch()`, the rejection is properly handled, and the `Uncaught (in promise)` error will no longer appear.

### 2. Use `try...catch` with `async/await`

The `async/await` syntax allows you to write asynchronous code that looks and behaves more like synchronous code, which can improve readability. Within an `async` function, you can use a standard `try...catch` block to handle Promise rejections.

```javascript
async function fetchData() {
  try {
    const response = await fetch('https://api.example.com/non-existent-endpoint');
    
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error('There has been a problem with your fetch operation:', error);
  }
}

fetchData();
```

The `await` keyword pauses the function execution until the Promise is settled (either resolved or rejected). If the Promise is rejected, the `catch` block of the `try...catch` statement will handle the error.

## Conclusion

The `Uncaught (in promise)` error is a critical warning that you have an unhandled Promise rejection. Since any asynchronous operation can potentially fail, you should always implement error handling.

-   When using Promise chains, append a **`.catch()`** method at the end.
-   When using `async/await`, wrap your code in a **`try...catch`** block.

Properly handling asynchronous errors is essential for building robust and reliable applications.
