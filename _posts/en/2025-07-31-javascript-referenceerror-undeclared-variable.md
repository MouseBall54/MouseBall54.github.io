---
typora-root-url: ../
layout: single
title: "How to Fix \"ReferenceError: assignment to undeclared variable\" in JavaScript"
date: 2025-07-31T22:11:00+09:00
excerpt: "Resolve the \"ReferenceError: assignment to undeclared variable\" in JavaScript's strict mode by properly declaring variables with `let`, `const`, or `var` before assigning values."
header:
   teaser: /images/header_images/overlay_image_js.png
   overlay_image: /images/header_images/overlay_image_js.png
   overlay_filter: 0.5
categories:
  - en_Troubleshooting
tags:
  - JavaScript
  - ReferenceError
  - Debugging
  - Strict Mode
---

## Introduction

The `ReferenceError: assignment to undeclared variable "..."` is an error that occurs exclusively in JavaScript's **strict mode**. It acts as a safeguard, preventing you from accidentally creating global variables by assigning a value to a variable that has not been declared yet. This guide explains why this error happens and how to fix it.

## What is Strict Mode?

Strict mode is a way to opt into a restricted variant of JavaScript. It makes several changes to normal JavaScript semantics:
1.  It eliminates some JavaScript silent errors by changing them to throw errors.
2.  It fixes mistakes that make it difficult for JavaScript engines to perform optimizations.
3.  It prohibits some syntax likely to be defined in future versions of ECMAScript.

You can enable strict mode for an entire script by adding `"use strict";` at the beginning of the file, or for a specific function by adding it at the beginning of the function body.

```javascript
// For an entire script
"use strict";
// ... your code ...

// For a function
function myStrictFunction() {
  "use strict";
  // ... your code ...
}
```

## Cause of the Error

In non-strict mode, if you assign a value to a variable that hasn't been declared with `var`, `let`, or `const`, JavaScript creates a new global variable for you.

**Non-Strict Mode Example:**
```javascript
function createGlobal() {
  message = "Hello, world!"; // No declaration
}

createGlobal();
console.log(message); // Outputs: "Hello, world!" (a global variable 'message' was created)
```
This behavior can lead to bugs that are hard to track, as variables can be created accidentally in the global scope, potentially conflicting with other parts of your code.

In **strict mode**, this is not allowed. Assigning a value to an undeclared variable will throw the `ReferenceError`.

**Strict Mode Example:**
```javascript
"use strict";

function createGlobal() {
  message = "Hello, world!"; // No declaration
}

createGlobal(); 
// Throws: ReferenceError: assignment to undeclared variable "message"
```

## How to Fix It

The solution is simple and promotes good coding practices: **always declare your variables before you use them**.

Use one of JavaScript's declaration keywords (`let`, `const`, or `var`) to declare the variable within the appropriate scope.

### Solution using `let`

If the variable's value needs to change, use `let`.

```javascript
"use strict";

function assignValue() {
  let message; // Declare the variable
  message = "This is a valid assignment.";
  console.log(message);
}

assignValue();
```

### Solution using `const`

If the variable's value will not be reassigned, use `const`. This is generally preferred for preventing accidental reassignments.

```javascript
"use strict";

function assignConstant() {
  const greeting = "Hello!"; // Declare and assign
  console.log(greeting);
  // greeting = "Hi!"; // This would throw a TypeError
}

assignConstant();
```

### Solution using `var`

While `var` is also an option, it is generally recommended to use `let` and `const` because they have block scope (`{...}`) instead of function scope, which can help prevent other types of bugs.

```javascript
"use strict";

function assignWithVar() {
  var count; // Declare the variable
  count = 100;
  console.log(count);
}

assignWithVar();
```

By explicitly declaring your variables, you make your code clearer, more maintainable, and free of the `ReferenceError: assignment to undeclared variable` error.

```