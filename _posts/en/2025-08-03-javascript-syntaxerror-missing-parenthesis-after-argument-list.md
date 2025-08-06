---
typora-root-url: ../
layout: single
title: >
    How to Fix JavaScript SyntaxError: missing ) after argument list

lang: en
translation_id: javascript-syntaxerror-missing-parenthesis-after-argument-list
header:
   teaser: /images/header_images/overlay_image_js.png
   overlay_image: /images/header_images/overlay_image_js.png
   overlay_filter: 0.5
excerpt: >
    Learn how to fix the `SyntaxError: missing ) after argument list` in JavaScript, a common error caused by forgetting to add a closing parenthesis `)` after a function's argument list.
categories:
  - en_Troubleshooting
tags:
  - JavaScript
  - SyntaxError
  - Function Call
---

## The Problem

The `SyntaxError: missing ) after argument list` is a very common syntax error in JavaScript. As its name suggests, it means that the JavaScript parser expected a **closing parenthesis `)` after a function's argument list, but did not find one.**

When the JavaScript engine parses your code, it recognizes a function call when it sees an opening parenthesis `(` after a function name. It then reads the list of arguments until it finds a matching closing parenthesis `)`. If the closing parenthesis is missing from its expected position, the engine determines that the syntax is incomplete and throws this error.

## Examples of Error-Prone Code

The most typical example is simply forgetting the closing parenthesis in a function call.

```javascript
console.log("Hello, World!";
// SyntaxError: missing ) after argument list
```

In the code above, the `console.log` function receives the argument `"Hello, World!"`, but it is immediately followed by a semicolon `;` instead of a closing parenthesis `)`.

This error can be harder to spot when function calls are nested or the code is more complex.

```javascript
// The closing parenthesis for the alert function is missing.
alert(parseInt("123" ); 
// SyntaxError: missing ) after argument list
```

## How to Fix It

Since this is a syntax issue, the solution is very straightforward.

### 1. Add the Missing Closing Parenthesis `)`

Check the line where the error occurred and add the missing closing parenthesis `)` at the end of the function's argument list.

```javascript
// Corrected code
console.log("Hello, World!");

alert(parseInt("123"));
```

### 2. Use Your Code Editor's Help

To reduce these kinds of mistakes, it's highly recommended to leverage the features of your code editor (e.g., VS Code).

-   **Bracket Matching:** Most editors automatically add a closing parenthesis when you type an opening one. They also highlight matching pairs, making it easy to spot a missing one.
-   **Use a Linter:** A tool like ESLint can detect syntax errors in real-time as you write code, often underlining the problematic area. This allows you to fix the issue before you even run the code.
-   **Use a Code Formatter:** A tool like Prettier automatically formats your code into a consistent style whenever you save. As the code is aligned, its structure becomes clearer, making a missing parenthesis more visually apparent.

## Conclusion

The `SyntaxError: missing ) after argument list` is a syntax error caused by simple carelessness. If you encounter this error, don't panic. Just check the following:

-   Look at the **function call** on the line where the error occurred.
-   Ensure that a **closing parenthesis `)` is correctly placed** after the argument list.

In most cases, the problem is solved by adding a single missing parenthesis. Using your editor's built-in features can greatly help in preventing these errors from happening in the first place.
