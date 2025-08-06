---
typora-root-url: ../
layout: single
title: >
    How to Fix "ReferenceError: assignment to undeclared variable" in JavaScript

lang: en
translation_id: javascript-referenceerror-assignment-to-undeclared-variable
header:
   teaser: /images/header_images/overlay_image_js.png
   overlay_image: /images/header_images/overlay_image_js.png
   overlay_filter: 0.5
excerpt: >
    This post explains how to fix the "ReferenceError: assignment to undeclared variable" in JavaScript, which occurs in strict mode when you assign a value to a variable that has not been declared.
categories:
  - en_Troubleshooting
tags:
  - JavaScript
  - ReferenceError
  - Strict Mode
  - Debugging
---

## What is "ReferenceError: assignment to undeclared variable"?

This JavaScript error is specific.
It only occurs in **strict mode**.
You see it when you assign a value to a variable.
But the variable has not been declared yet.
Declaration uses keywords like `let`, `const`, or `var`.
In non-strict mode, this action creates a global variable.
Strict mode prevents this behavior to avoid potential bugs.
It helps write cleaner and more reliable code.

## Common Cause and Solution

The cause is straightforward. A variable is used without declaration.

### Assigning to an Undeclared Variable

You might forget to declare a variable before using it.
This is often a simple typo or oversight.

**Problematic Code (in strict mode):**
```javascript
'use strict';

function calculateTotal(price) {
  // Typo: 'totl' instead of 'total'
  totl = price * 1.1; // ReferenceError
  return totl;
}

// Or simply forgetting to declare
x = 10; // ReferenceError
console.log(x);
```

In the example, `totl` and `x` were never declared.
Strict mode catches this and throws a `ReferenceError`.

**Solution:**
The solution is simple.
Declare all variables before assigning values to them.
Use `let`, `const`, or `var`.

**Corrected Code:**
```javascript
'use strict';

function calculateTotal(price) {
  // Declare 'total' with let
  let total = price * 1.1;
  return total;
}

// Declare 'x' with let
let x = 10;
console.log(x);
```
By adding `let`, the variables are properly declared.
The code now runs without errors.

## Why Strict Mode is Important

This error highlights a key benefit of strict mode.
It prevents accidental creation of global variables.
Accidental globals can cause many problems.
They can conflict with other variables in your application.
This leads to unpredictable behavior and bugs.
Bugs from global variables are often hard to track down.
Strict mode turns these silent errors into noticeable `ReferenceError`s.
It forces better coding habits.

## How to Enable Strict Mode

You can enable strict mode in two ways.

1.  **For an entire script:**
    Place `'use strict';` at the very beginning of your JavaScript file.

    ```javascript
    'use strict';

    // All code in this script will be in strict mode
    let a = 1;
    b = 2; // ReferenceError
    ```

2.  **For a specific function:**
    Place `'use strict';` at the beginning of the function body.

    ```javascript
    function myStrictFunction() {
      'use strict';
      // Code inside this function is in strict mode
      let c = 3;
      d = 4; // ReferenceError
    }
    ```

## Conclusion

The "ReferenceError: assignment to undeclared variable" is a helpful error.
It is a feature of JavaScript's strict mode.
It signals that you are trying to use a variable without declaring it first.
To fix it, always declare your variables with `let`, `const`, or `var`.
Adopting strict mode is a best practice.
It helps you write more robust and maintainable JavaScript code.
