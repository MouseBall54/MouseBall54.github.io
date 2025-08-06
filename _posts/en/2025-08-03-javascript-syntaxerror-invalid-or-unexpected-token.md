---
typora-root-url: ../
layout: single
title: >
    How to Fix "SyntaxError: Invalid or unexpected token" in JavaScript

lang: en
translation_id: javascript-syntaxerror-invalid-or-unexpected-token
header:
   teaser: /images/header_images/overlay_image_js.png
   overlay_image: /images/header_images/overlay_image_js.png
   overlay_filter: 0.5
excerpt: >
    This post explains how to resolve the "SyntaxError: Invalid or unexpected token" in JavaScript, which occurs when the JavaScript engine encounters code that violates the language's syntax rules.
categories:
  - en_Troubleshooting
tags:
  - JavaScript
  - SyntaxError
  - Debugging
  - Frontend
---

## What is "SyntaxError: Invalid or unexpected token"?

The "SyntaxError: Invalid or unexpected token" is a common error in JavaScript. It occurs when the JavaScript engine's parser encounters a piece of code that it doesn't understand or that violates the language's syntax rules. The "token" refers to a single unit of code, like a keyword, an operator, or a variable name. This error essentially means the parser found a token where it didn't expect one, breaking the grammatical structure of the code.

## Common Causes and Solutions

This error can be triggered by a wide range of syntax mistakes. Here are some of the most frequent causes and how to fix them.

### 1. Missing or Mismatched Parentheses, Brackets, or Braces

One of the most common culprits is a missing or extra parenthesis `()`, bracket `[]`, or brace `{}`.

**Incorrect Code:**
```javascript
function calculate(a, b { // Missing closing parenthesis for arguments
  return a + b;
}

console.log(calculate(5, 10); // Missing closing parenthesis for function call
```

**Correct Code:**
```javascript
function calculate(a, b) { // Corrected parenthesis
  return a + b;
}

console.log(calculate(5, 10)); // Corrected parenthesis
```

**How to Fix:**
Carefully check your code to ensure every opening `(`, `[`, or `{` has a corresponding closing `)`, `]`, or `}`. Code editors with syntax highlighting can be very helpful in spotting these mismatches.

### 2. Typographical Errors (Typos)

A simple typo, like an extra character or a misplaced operator, can cause this error.

**Incorrect Code:**
```javascript
let x = 10;
let y = 20;
let z = x + y+; // Extra '+' operator
```

**Correct Code:**
```javascript
let x = 10;
let y = 20;
let z = x + y; // Removed the extra '+'
```

**How to Fix:**
Review the line where the error occurs for any typos or misplaced characters. The browser's developer console usually points to the exact line number.

### 3. Incorrect Use of Template Literals

When using template literals (backticks `` ` ``), you might forget to use `${}` to embed expressions.

**Incorrect Code:**
```javascript
const name = "World";
const greeting = `Hello, "name"!`; // "name" is treated as a literal string
```

This doesn't throw a syntax error but leads to incorrect output. A syntax error might occur if the content inside is invalid. A more direct cause of the error is an unclosed literal:

**Incorrect Code:**
```javascript
const message = `This is an unclosed template literal;
```

**Correct Code:**
```javascript
const name = "World";
const greeting = `Hello, ${name}!`; // Correctly embeds the variable

const message = `This is a closed template literal`; // Closed the literal
```

**How to Fix:**
Ensure all template literals are properly closed with a backtick and that you use the `${...}` syntax for embedding expressions.

### 4. Illegal Characters

Sometimes, you might accidentally copy and paste characters that are not valid in JavaScript code, such as smart quotes (`“ ”`) instead of standard double quotes (`" "`).

**Incorrect Code:**
```javascript
const text = “Hello World”; // Using smart quotes
```

**Correct Code:**
```javascript
const text = "Hello World"; // Using standard double quotes
```

**How to Fix:**
Make sure your code editor is configured to use standard quotes and check for any non-standard characters, especially in code copied from web pages or documents.

### 5. Reserved Keywords as Variable Names

Using a reserved JavaScript keyword (e.g., `class`, `const`, `function`) as a variable or function name will cause a syntax error.

**Incorrect Code:**
```javascript
let const = "This is not allowed"; // 'const' is a reserved keyword
```

**Correct Code:**
```javascript
let myConst = "This is allowed"; // Changed the variable name
```

**How to Fix:**
Avoid using reserved keywords as identifiers. If you are unsure, you can find a list of JavaScript reserved words online.

## Conclusion

The "SyntaxError: Invalid or unexpected token" is almost always a result of a simple mistake in your code's structure. By carefully examining the line of code indicated by the error message and checking for common issues like mismatched brackets, typos, or illegal characters, you can usually resolve this error quickly. Using a good code editor with linting and syntax highlighting features can also help you catch these errors before you even run the code.
