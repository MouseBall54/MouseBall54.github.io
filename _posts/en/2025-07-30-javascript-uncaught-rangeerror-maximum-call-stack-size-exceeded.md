---
typora-root-url: ../
layout: single
title: "How to Fix 'Maximum call stack size exceeded' in JavaScript"

lang: en
translation_id: javascript-uncaught-rangeerror-maximum-call-stack-size-exceeded
excerpt: "Resolve the 'Uncaught RangeError: Maximum call stack size exceeded' in JavaScript by identifying infinite recursion and implementing proper base cases in your functions."
header:
   teaser: /images/header_images/overlay_image_js.png
   overlay_image: /images/header_images/overlay_image_js.png
   overlay_filter: 0.5
categories:
  - en_Troubleshooting
tags:
  - JavaScript
  - RangeError
  - Call Stack
  - Recursion
---

## Understanding "Uncaught RangeError: Maximum call stack size exceeded"

This error occurs in JavaScript when a function calls itself too many times, leading to a stack overflow. The call stack is a mechanism for an interpreter to keep track of its place in a script that calls multiple functions. There's a limit to the size of the stack, and when that limit is exceeded, this error is thrown.

### Common Cause: Infinite Recursion

The most frequent cause is **infinite recursion**, where a function calls itself without a proper exit condition.

**Problematic Code:**
```javascript
function infiniteLoop() {
  infiniteLoop(); // The function calls itself with no way to stop.
}

// Calling this function will cause the error.
// infiniteLoop(); 
```

Another common scenario is a recursive function that has a base case, but the recursive call doesn't move the input toward that base case.

```javascript
function countdown(n) {
  if (n === 0) {
    console.log("Blast off!");
    return;
  }
  console.log(n);
  countdown(n + 1); // Oops! This counts up, away from the base case of 0.
}

// countdown(10);
```

### How to Fix the Error

#### 1. Add a Base Case (Termination Condition)

A recursive function must have a **base case**—a condition that stops the recursion.

**Incorrect Code (No Base Case):**
```javascript
function goOnForever() {
    goOnForever();
}
```

**Solution:**
Ensure there's a condition that, when met, prevents the function from calling itself again.

```javascript
function countdown(n) {
  if (n <= 0) { // Base case
    console.log("Done!");
    return;
  }
  console.log(n);
  countdown(n - 1); // Recursive call that moves toward the base case
}

countdown(5); // 5, 4, 3, 2, 1, Done!
```

#### 2. Convert to an Iterative Approach

If a recursive solution is too deep, even if it's not infinite, it can still exceed the stack size. In such cases, converting the function to use a loop (an iterative approach) can solve the problem.

**Recursive Function:**
```javascript
function sumRecursive(n, total = 0) {
  if (n <= 0) {
    return total;
  }
  return sumRecursive(n - 1, total + n);
}
```

**Iterative Solution:**
```javascript
function sumIterative(n) {
  let total = 0;
  for (let i = 1; i <= n; i++) {
    total += i;
  }
  return total;
}

// This can handle very large numbers without a stack overflow.
console.log(sumIterative(100000)); 
```

By carefully managing recursion and ensuring every recursive function has a reachable base case, you can avoid the "Maximum call stack size exceeded" error and write more stable code.
