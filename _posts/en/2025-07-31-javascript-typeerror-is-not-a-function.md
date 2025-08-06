---
typora-root-url: ../
layout: single
title: "How to Fix \"TypeError: '...' is not a function\" in JavaScript"

lang: en
translation_id: javascript-typeerror-is-not-a-function
excerpt: "Fix the \"TypeError: '...' is not a function\" in JavaScript by ensuring the variable you are calling is actually a function and checking for scope issues or typos."
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
  - Functions
---

## Introduction

The `TypeError: '...' is not a function` is a very common error in JavaScript. It occurs when you try to call something that is not a function. This can happen for several reasons, such as a typo in the function name, a variable having the same name as a function, or a method being called on an object that doesn't have it. This guide will walk you through the common causes and how to fix them.

## 1. Cause: Typo in Function Name

The most straightforward cause is a simple spelling mistake. If you misspell the function's name, JavaScript won't be able to find it and will treat the variable as `undefined`, which is not a function.

### Example

```javascript
function greetUser() {
  console.log("Hello, user!");
}

// Typo: 'greetUser' is misspelled as 'greetUsers'
greetUsers(); 
// Throws: TypeError: greetUsers is not a function
```

### Solution

- **Check spelling**: Double-check the function name for any typos. Ensure it matches the name used in its definition.
- **Use an IDE or linter**: Tools like VS Code with IntelliSense or linters like ESLint can catch these errors before you even run the code.

## 2. Cause: Variable Overwriting a Function

If you declare a variable with the same name as a function, the variable's value will overwrite the function definition. When you later try to call the function, you are actually trying to invoke the variable's value.

### Example

```javascript
function myFunction() {
  console.log("This is a function.");
}

// The variable 'myFunction' overwrites the function definition
const myFunction = "This is a string.";

myFunction(); 
// Throws: TypeError: myFunction is not a function
```

### Solution

- **Avoid name collisions**: Use unique and descriptive names for your variables and functions. Avoid reusing names within the same scope.
- **Use `const` for functions**: Declaring functions using `const` and an arrow function expression can prevent accidental reassignment.
  ```javascript
  const myFunction = () => {
    console.log("This is a function.");
  };
  ```

## 3. Cause: Method Does Not Exist on an Object

This error often occurs when you try to call a method on an object that does not have that method. This is common when working with DOM elements or data from an API.

### Example

```javascript
const myObject = {
  name: "Test Object",
  // No 'sayHello' method defined
};

myObject.sayHello(); 
// Throws: TypeError: myObject.sayHello is not a function
```

Another common scenario is with strings. For example, `toUppercase()` instead of `toUpperCase()`.

```javascript
const myString = "hello world";
console.log(myString.toUppercase()); // Note the lowercase 'c'
// Throws: TypeError: myString.toUppercase is not a function
```

### Solution

- **Check object properties**: Before calling a method, ensure it exists on the object. You can use `console.log(myObject)` to inspect the object's properties and methods.
- **Consult documentation**: When using built-in methods (like for strings or arrays) or methods from a library, always refer to the official documentation to confirm the correct name and usage.

## 4. Cause: Incorrect Import/Export

When working with modules, if you import something that is not a function or use the wrong import syntax (e.g., `import { myFunction }` vs. `import myFunction`), you can get this error.

### Example

**`my-module.js`**:
```javascript
const myData = { value: 42 };
export default myData;
```

**`main.js`**:
```javascript
import myData from './my-module.js';

// myData is an object, not a function
myData(); 
// Throws: TypeError: myData is not a function
```

### Solution

- **Verify exports**: Check what is being exported from the module.
- **Use correct import syntax**: Ensure you are using the correct syntax for default or named exports.
  - For named exports: `export const myFunction = ...` -> `import { myFunction } from ...`
  - For default exports: `export default myFunction` -> `import myFunction from ...`

By carefully checking these points, you can quickly identify the source of the `TypeError: '...' is not a function` and resolve it.

