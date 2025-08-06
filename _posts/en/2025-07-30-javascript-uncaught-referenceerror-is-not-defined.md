---
typora-root-url: ../
layout: single
title: "How to Fix 'Uncaught ReferenceError: is not defined' in JavaScript"

lang: en
translation_id: javascript-uncaught-referenceerror-is-not-defined
excerpt: "'Uncaught ReferenceError: ... is not defined' is a common error in JavaScript that occurs when a variable or function is not declared or is outside the accessible scope. Let's explore its causes and solutions."
header:
   teaser: /images/header_images/overlay_image_js.png
   overlay_image: /images/header_images/overlay_image_js.png
   overlay_filter: 0.5
categories:
  - en_Troubleshooting
tags:
  - JavaScript
  - ReferenceError
  - Troubleshooting
  - Scope
---

## What is 'Uncaught ReferenceError: ... is not defined'?

`Uncaught ReferenceError: ... is not defined` is an error that occurs when the JavaScript engine cannot find a specific variable or function during code execution.
This means the identifier has not been declared within the current scope or the global scope.
It is one of the most common errors encountered during development.

## Main Causes

### 1. Typo in Variable or Function Name

This is the simplest and most common cause. The error occurs if the name used to declare a variable or function differs from the name used to call it.

```javascript
let myVariable = "Hello, World!";

// Should be called as 'myVariable', not 'myvariable'
console.log(myvariable); 
// Uncaught ReferenceError: myvariable is not defined
```

JavaScript is case-sensitive, so `myVariable` and `myvariable` are treated as different identifiers.

### 2. Using a Variable Before Declaration

A `ReferenceError` occurs if you try to access a variable before it is declared.
Variables declared with `var` are hoisted and return `undefined`, but `let` and `const` are placed in the Temporal Dead Zone (TDZ), which causes this error.

```javascript
console.log(x); // Uncaught ReferenceError: Cannot access 'x' before initialization
let x = 10;
```

### 3. Scope Issues

The error occurs when you try to access a variable or function outside of the scope in which it is valid.

```javascript
function myFunction() {
    let localVariable = "I am local";
    console.log(localVariable); // Works fine
}

myFunction();

console.log(localVariable); // Uncaught ReferenceError: localVariable is not defined
```

`localVariable` is a local variable accessible only within the `myFunction` function, so it cannot be found outside the function.

### 4. Failure to Load External Libraries

This error can also occur if you use an external library like jQuery or Lodash but fail to load it properly in your HTML file.

```html
<!-- jQuery library is not loaded -->
<script>
    // '$' is jQuery's identifier, but it is not defined without the library
    $("#myElement").hide(); 
    // Uncaught ReferenceError: $ is not defined
</script>
```

## How to Fix It

### 1. Check Names and Fix Typos

First, ensure that the names of variables and functions match exactly between their declaration and usage. Pay close attention to case sensitivity.

### 2. Check Declaration Order

Variables must always be declared before they are used. Place variable and function declarations at the top of your code or before the point of use, following the logical flow.

### 3. Understand and Adjust Scope

You need to check the scope to ensure that variables and functions are accessible where they are needed.
If a variable needs to be used in multiple functions, declare it in a broader scope that includes those functions.

```javascript
let sharedVariable = "I am shared";

function functionOne() {
    console.log(sharedVariable);
}

function functionTwo() {
    console.log(sharedVariable);
}

functionOne(); // "I am shared"
functionTwo(); // "I am shared"
```

### 4. Verify External Script Loading

If you are using an external library, make sure it is loaded correctly via a `<script>` tag in your HTML file, either in the `<head>` or just before the closing `</body>` tag.
It is a good practice to check the developer tools' Network tab to ensure the script URL is correct and that it did not fail to load due to network issues.

```html
<head>
    <!-- Load the jQuery library first -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>
    <!-- Now '$' can be used normally -->
    <script>
        $("#myElement").hide();
    </script>
</body>
```

## Conclusion

`Uncaught ReferenceError` usually stems from basic mistakes.
The main causes are typos, incorrect declaration order, and misunderstandings of scope.
By carefully examining the code around the variable or function name mentioned in the error message, you can usually solve the problem easily.
