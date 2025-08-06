---
typora-root-url: ../
layout: single
title: "How to Fix \"TypeError: Assignment to constant variable\" in JavaScript"

lang: en
translation_id: javascript-typeerror-assignment-to-constant
excerpt: "Understand and fix the \"TypeError: Assignment to constant variable\" in JavaScript by learning the properties of `const` and using `let` for variables that need to be reassigned."
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
  - Const
  - ES6
---

## Introduction

The `TypeError: Assignment to constant variable` is a common error in modern JavaScript (ES6 and later). It occurs when you try to reassign a value to a variable that was declared using the `const` keyword. This guide will explain the behavior of `const`, why this error happens, and how to correctly manage your variables to avoid it.

## Understanding `const`

The `const` keyword was introduced in ES6 to allow for the declaration of constants. A constant is a variable whose value cannot be changed through reassignment. When you declare a variable with `const`, you must initialize it with a value, and you cannot assign a new value to it later.

### Key Properties of `const`:
1.  **Cannot be Reassigned**: Once a value is assigned, the variable identifier cannot be pointed to a new value.
2.  **Must be Initialized**: You must provide a value when you declare a `const` variable.
3.  **Block-Scoped**: Like `let`, `const` variables are scoped to the block (`{...}`) in which they are defined.

### Example of the Error

```javascript
const myName = "Alice";

console.log(myName); // Outputs: "Alice"

// Attempting to reassign the constant variable
myName = "Bob"; 
// Throws: TypeError: Assignment to constant variable.
```

This happens because `myName` was declared as a constant, and the JavaScript engine prevents you from changing its assignment.

## How to Fix It

The solution depends on your intention for the variable.

### 1. Use `let` for Variables That Change

If you intended for the variable's value to change over time, you should have declared it with `let` instead of `const`. The `let` keyword declares a block-scoped variable that can be reassigned.

**Solution:**
```javascript
let myName = "Alice"; // Use 'let' instead of 'const'

console.log(myName); // Outputs: "Alice"

// Now, this is a valid reassignment
myName = "Bob"; 
console.log(myName); // Outputs: "Bob"
```
This is the most common fix. You likely used `const` for a variable that you later realized needed to be updated.

### 2. Be Aware of `const` with Objects and Arrays

A common point of confusion is how `const` works with objects and arrays. When you declare an object or array with `const`, it means the **variable itself cannot be reassigned** to a new object or array. However, the **properties of the object or the elements of the array can be changed**.

**Example with an Object:**
```javascript
const person = {
  name: "Alice",
  age: 30
};

// This is ALLOWED: Modifying a property of the constant object
person.age = 31; 
console.log(person.age); // Outputs: 31

// This is NOT ALLOWED: Reassigning the constant variable to a new object
person = { name: "Bob", age: 40 }; 
// Throws: TypeError: Assignment to constant variable.
```

**Example with an Array:**
```javascript
const myNumbers = [1, 2, 3];

// This is ALLOWED: Modifying the contents of the constant array
myNumbers.push(4);
console.log(myNumbers); // Outputs: [1, 2, 3, 4]

// This is NOT ALLOWED: Reassigning the constant variable to a new array
myNumbers = [5, 6, 7];
// Throws: TypeError: Assignment to constant variable.
```

If you need to prevent the properties of an object from being changed, you should use `Object.freeze()`.

```javascript
const person = Object.freeze({
  name: "Alice",
  age: 30
});

person.age = 31; // This will not cause an error, but the change will be ignored in strict mode.
console.log(person.age); // Outputs: 30
```

## Best Practices

- **Default to `const`**: As a general rule, declare all your variables with `const` by default.
- **Switch to `let` only when needed**: If you find that you need to reassign a variable, then go back and change its declaration from `const` to `let`. This practice helps prevent accidental reassignments and makes your code more predictable.

By understanding the difference between `const` and `let`, you can easily avoid the `TypeError: Assignment to constant variable` and write more robust code.

```