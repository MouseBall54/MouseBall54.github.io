---
typora-root-url: ../
layout: single
title: "How to Fix \"SyntaxError: Invalid or unexpected token\" in JavaScript"

lang: en
translation_id: javascript-syntaxerror-invalid-token
excerpt: "Resolve the \"SyntaxError: Invalid or unexpected token\" in JavaScript by checking for typos, missing characters like commas or parentheses, and incorrect syntax."
header:
   teaser: /images/header_images/overlay_image_js.png
   overlay_image: /images/header_images/overlay_image_js.png
   overlay_filter: 0.5
categories:
  - en_Troubleshooting
tags:
  - JavaScript
  - SyntaxError
  - Debugging
  - Token
---

## Introduction

The `SyntaxError: Invalid or unexpected token` is a common error in JavaScript that occurs when the JavaScript engine encounters a piece of code that it cannot parse. This error is very general and can be caused by a wide variety of syntax mistakes, from simple typos to more complex structural problems. This guide will cover the most frequent causes and how to identify and fix them.

## 1. Cause: Typos and Misplaced Characters

The most common reason for this error is a simple typographical mistake. This could be an extra character, a misplaced comma, or an invalid character in your code.

### Example

```javascript
// An extra comma in an object literal
const myObject = {
  name: "John",
  age: 30,, // Extra comma
};

// A stray character in the code
const x = 10; & // Invalid character '&'

// Missing comma between array elements
const myArray = [1 2, 3]; // Missing comma between 1 and 2
```

### Solution

- **Review the code carefully**: Look closely at the line number indicated in the error message. Often, the error is on that line or the line immediately preceding it.
- **Use a linter**: Tools like ESLint can automatically detect and flag these kinds-of syntax errors as you type, saving you debugging time.

## 2. Cause: Missing Parentheses, Brackets, or Braces

Unbalanced parentheses `()`, square brackets `[]`, or curly braces `{}` are a frequent source of this error. If you open one but forget to close it, the JavaScript parser gets confused.

### Example

```javascript
function myFunction(a, b { // Missing closing parenthesis ')'
  return a + b;
}

const myArray = [1, 2, 3; // Missing closing bracket ']'

if (condition) {
  // Missing closing brace '}'
```

### Solution

- **Check for matching pairs**: Ensure every opening `(`, `[`, or `{` has a corresponding closing `)`, `]`, or `}`.
- **Use a code editor with bracket matching**: Most modern code editors (like VS Code, Sublime Text, Atom) highlight matching brackets, making it easy to spot when one is missing.

## 3. Cause: Incorrect Use of Reserved Keywords

Using a reserved JavaScript keyword (like `class`, `const`, `function`, `let`) as a variable or function name will cause a syntax error.

### Example

```javascript
const let = "This is not allowed"; // 'let' is a reserved keyword

function class() { // 'class' is a reserved keyword
  console.log("This is also not allowed");
}
```

### Solution

- **Avoid using reserved words**: Familiarize yourself with the list of JavaScript reserved keywords and choose different names for your variables and functions. You can find a complete list on MDN Web Docs.

## 4. Cause: Copy-Pasting Code with Invalid Characters

Sometimes, when you copy code from a web page, a PDF, or a word processor, it can include "smart quotes" (`“...”` or `‘...’`) instead of standard straight quotes (`"..."` or `'...'`). JavaScript does not recognize smart quotes as valid string delimiters.

### Example

```javascript
// Using smart quotes instead of straight quotes
const greeting = “Hello, World!”; 
// Throws: SyntaxError: Invalid or unexpected token
```

### Solution

- **Replace smart quotes**: Manually replace any smart quotes with standard single or double quotes.
- **Configure your editor**: Some code editors can be configured to automatically convert smart quotes to straight quotes when you paste code.

By systematically checking for these common mistakes, you can quickly diagnose and fix the `SyntaxError: Invalid or unexpected token`.
