---
typora-root-url: ../
layout: single
title: >
   JavaScript Promises: Promise.all vs. Promise.race

lang: en
translation_id: javascript-promise-all-vs-promise-race
header:
   teaser: /images/header_images/overlay_image_js.png
   overlay_image: /images/header_images/overlay_image_js.png
   overlay_filter: 0.5
excerpt: >
   Learn the difference between Promise.all and Promise.race in JavaScript for handling multiple asynchronous operations. Understand when to wait for all promises to complete and when to act on the first one that settles.
categories:
   - en_Troubleshooting
tags:
   - JavaScript
   - Promises
   - async
   - Promise.all
   - Promise.race
---

## Introduction

JavaScript Promises are essential for managing asynchronous operations. While you often work with a single promise, there are many scenarios where you need to handle multiple promises at once. The `Promise` object provides two key static methods for this: `Promise.all()` and `Promise.race()`.

Understanding the difference between them is crucial for orchestrating complex asynchronous workflows efficiently. This guide will compare `Promise.all` and `Promise.race` with clear examples to show you when to use each.

## `Promise.all()` - The "All or Nothing" Method

`Promise.all(iterable)` takes an iterable (like an array) of promises and returns a single `Promise`. This new promise behaves as follows:

-   It **fulfills** when **all** of the input promises have fulfilled. The fulfillment value is an array containing the fulfillment values of all the promises, in the same order as they appeared in the input array.
-   It **rejects** as soon as **any one** of the input promises rejects. The rejection reason is the reason of the first promise that rejected.

Think of it as a group task: the entire group succeeds only if every member completes their task. If any single member fails, the entire group task fails immediately.

### When to Use `Promise.all()`

Use `Promise.all()` when you have multiple asynchronous tasks that are independent of each other, and you need to wait for all of them to complete before proceeding.

**Common Use Cases:**
-   Fetching data from multiple API endpoints simultaneously.
-   Uploading multiple files and waiting for all uploads to finish.
-   Performing several database queries and aggregating the results.

### Example

Imagine you need to fetch user data and their posts from two different APIs before rendering a profile page.

```javascript
const promise1 = fetch('https://api.example.com/users/1').then(res => res.json());
const promise2 = fetch('https://api.example.com/posts/1').then(res => res.json());
const promise3 = new Promise(resolve => setTimeout(() => resolve("Extra info"), 100));

Promise.all([promise1, promise2, promise3])
    .then(results => {
        const userData = results[0];
        const postData = results[1];
        const extraInfo = results[2];

        console.log("All promises fulfilled!");
        console.log("User:", userData);
        console.log("Posts:", postData);
        console.log("Extra:", extraInfo);
        // Now you can render the page
    })
    .catch(error => {
        console.error("One of the promises rejected:", error);
        // Handle the error, e.g., show an error message
    });
```

If any of the `fetch` calls fail, the `.catch()` block will be executed immediately.

## `Promise.race()` - The "First to Finish" Method

`Promise.race(iterable)` also takes an iterable of promises and returns a single `Promise`. However, this new promise settles (either fulfills or rejects) as soon as the **first** of the input promises settles.

-   It **fulfills** if the first promise to settle fulfills. The fulfillment value is the value of that first fulfilled promise.
-   It **rejects** if the first promise to settle rejects. The rejection reason is the reason of that first rejected promise.

Think of it as a race: you only care about the winner. As soon as one runner crosses the finish line, the race is over, and you have your result.

### When to Use `Promise.race()`

Use `Promise.race()` when you have multiple sources for the same information or when you want to implement a timeout.

**Common Use Cases:**
-   Requesting a resource from multiple redundant servers and taking the response from whichever is fastest.
-   Setting a timeout for an asynchronous operation.

### Example

Let's implement a timeout for a network request. We'll create one promise for the `fetch` operation and another that rejects after a certain time. We then race them against each other.

```javascript
function fetchWithTimeout(url, timeout) {
    const fetchPromise = fetch(url);

    const timeoutPromise = new Promise((_, reject) => {
        setTimeout(() => {
            reject(new Error(`Request timed out after ${timeout} ms`));
        }, timeout);
    });

    return Promise.race([fetchPromise, timeoutPromise]);
}

fetchWithTimeout('https://api.example.com/slow-resource', 5000)
    .then(response => response.json())
    .then(data => {
        console.log("Data received:", data);
    })
    .catch(error => {
        console.error("Error:", error.message);
        // This will log "Request timed out after 5000 ms" if the fetch takes too long
    });
```
If the `fetch` call takes longer than 5 seconds, the `timeoutPromise` will reject first, causing the `Promise.race` to reject.

## Summary Table

| Feature            | `Promise.all()`                               | `Promise.race()`                                    |
| ------------------ | --------------------------------------------- | --------------------------------------------------- |
| **When it Fulfills** | When **all** promises fulfill.                | When the **first** promise fulfills.                |
| **When it Rejects**  | When **any** promise rejects.                 | When the **first** promise rejects.                 |
| **Fulfillment Value** | An array of all fulfillment values.           | The fulfillment value of the first fulfilled promise. |
| **Use Case**       | Aggregate results from multiple promises.     | Get the result from the fastest promise or timeout. |

## Conclusion

`Promise.all()` and `Promise.race()` are powerful tools for managing multiple asynchronous operations, but they serve very different purposes.

-   Use **`Promise.all()`** when you need everything to succeed before you can proceed.
-   Use **`Promise.race()`** when you only need the result of the very first promise to settle.

By choosing the right method for your scenario, you can write cleaner, more declarative, and more efficient asynchronous JavaScript code.
