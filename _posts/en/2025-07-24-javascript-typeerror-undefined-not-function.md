---
typora-root-url: ../
layout: single
title: >
  How to Fix "TypeError: undefined is not a function" in JavaScript
date: 2025-07-24T22:00:00+09:00
excerpt: >
  "TypeError: undefined is not a function" occurs when code attempts to call a value that isn't a function. Learn to identify the root cause—such as typos, load order issues, or incorrect imports—and apply targeted fixes.
lang: en
translation_id: javascript-typeerror-undefined-not-function
header:
   teaser: /images/header_images/overlay_image_js.png
   overlay_image: /images/header_images/overlay_image_js.png
   overlay_filter: 0.5
categories:
  - en_Troubleshooting
tags:
  - JavaScript
  - TypeError
  - Debugging
  - WebDev
---
## Introduction

JavaScript throws a `TypeError: undefined is not a function` when you invoke something that isn’t callable. This error often appears in browser console or Node.js logs and blocks your code execution. Understanding common patterns makes it easy to resolve.

## What Is the Error?

```text
TypeError: undefined is not a function
    at myFunction (app.js:10)
    at HTMLButtonElement.onclick (index.html:5)
```

It means the identifier you’re calling evaluates to `undefined`, not to a function reference.

## Common Causes

1. **Typo in function or method name.**
2. **Script or module load order**: code runs before definition.
3. **Incorrect export/import** in ES modules or CommonJS.
4. **Overwriting built-in methods** or globals.
5. **`this` binding issues** when using callbacks.

## Solution 1: Check for Typos

Ensure the function name matches exactly:

```js
// Wrong
element.addEventListerner('click', handleClick);
// Right
element.addEventListener('click', handleClick);
```

## Solution 2: Verify Load Order

Load scripts in correct sequence:

```html
<!-- library defines $.ajax -->
<script src="jquery.js"></script>
<script src="app.js"></script>
```

Or wrap calls in `DOMContentLoaded`:

```js
document.addEventListener('DOMContentLoaded', () => {
  initApp();
});
```

## Solution 3: Validate Imports and Exports

ES Modules:

```js
// utils.js
export function doThing() { … }

// app.js
import { doThing } from './utils.js';
doThing();
```

CommonJS:

```js
// utils.js
module.exports = { doThing };

// app.js
const { doThing } = require('./utils');
doThing();
```

## Solution 4: Avoid Overwriting Globals

Don’t reuse names of standard APIs:

```js
// BAD: overwrites window.fetch
const fetch = null;
fetch('/api'); // TypeError
```

## Solution 5: Fix `this` Binding

Use `.bind()` or arrow functions to preserve context:

```js
class MyClass {
  constructor() {
    this.method = this.method.bind(this);
  }
  method() { … }
}
```

Or:

```js
button.addEventListener('click', () => this.method());
```

## Conclusion

"TypeError: undefined is not a function" is usually a simple fix—correct names, load scripts in order, use proper imports, and ensure correct context. Following these guidelines prevents the error and keeps your JavaScript running smoothly.

