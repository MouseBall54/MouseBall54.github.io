---
typora-root-url: ../
layout: single
title: >
   JavaScript Variables: The Difference Between var, let, and const

lang: en
translation_id: javascript-variables-var-vs-let-vs-const
header:
   teaser: /images/header_images/overlay_image_js.png
   overlay_image: /images/header_images/overlay_image_js.png
   overlay_filter: 0.5
excerpt: >
   Dive into the differences between var, let, and const in JavaScript. Understand scope, hoisting, and reassignment rules to write cleaner, more predictable, and modern JS code.
categories:
   - en_Troubleshooting
tags:
   - JavaScript
   - ES6
   - var
   - let
   - const
---

## Introduction

For many years, `var` was the only way to declare a variable in JavaScript. With the introduction of ES6 (ECMAScript 2015), two new keywords, `let` and `const`, were added, providing more control over variable scope and behavior. Understanding the differences between these three is crucial for writing modern, maintainable, and bug-free JavaScript.

This guide will compare `var`, `let`, and `const` based on their scope, hoisting, and reassignment rules.

## 1. Scope

Scope determines where a variable is accessible in your code.

### `var`: Function Scope

Variables declared with `var` are **function-scoped**. This means they are only accessible within the function they are declared in. If declared outside any function, they have a global scope.

```javascript
function myFunction() {
    if (true) {
        var myVar = "Hello from var";
    }
    console.log(myVar); // "Hello from var" - Accessible here
}
myFunction();
// console.log(myVar); // ReferenceError: myVar is not defined - Not accessible here
```
Notice that `myVar` is accessible outside the `if` block. This is because `var` does not respect block scope (`{...}`), which can lead to unexpected behavior.

### `let` and `const`: Block Scope

Variables declared with `let` and `const` are **block-scoped**. They are only accessible within the block (i.e., inside the curly braces `{...}`) in which they are defined.

```javascript
function anotherFunction() {
    if (true) {
        let myLet = "Hello from let";
        const myConst = "Hello from const";
        console.log(myLet);   // Accessible
        console.log(myConst); // Accessible
    }
    // console.log(myLet);   // ReferenceError: myLet is not defined
    // console.log(myConst); // ReferenceError: myConst is not defined
}
anotherFunction();
```
This is much more intuitive and similar to how variables work in many other programming languages. It helps prevent bugs by limiting the variable's lifecycle to the block where it's needed.

## 2. Hoisting

Hoisting is JavaScript's behavior of moving declarations to the top of their scope before code execution.

### `var`: Hoisted and Initialized

`var` variables are hoisted to the top of their scope and are initialized with a value of `undefined`.

```javascript
console.log(hoistedVar); // undefined (No error)
var hoistedVar = "I am hoisted";
console.log(hoistedVar); // "I am hoisted"
```
This means you can access a `var` variable before it's declared without getting an error, though its value will be `undefined`.

### `let` and `const`: Hoisted but Not Initialized

`let` and `const` variables are also hoisted, but they are **not** initialized. Accessing them before the declaration results in a `ReferenceError`. The period from the start of the block to the declaration is called the **Temporal Dead Zone (TDZ)**.

```javascript
// console.log(hoistedLet); // ReferenceError: Cannot access 'hoistedLet' before initialization
let hoistedLet = "I am hoisted too";

// console.log(hoistedConst); // ReferenceError: Cannot access 'hoistedConst' before initialization
const hoistedConst = "So am I";
```
This behavior prevents you from accidentally using a variable before its value is assigned, making the code more robust.

## 3. Reassignment

This is the primary difference between `let` and `const`.

### `var` and `let`: Can be Reassigned

Variables declared with `var` or `let` can be updated or reassigned.

```javascript
var myVarVariable = "First value";
myVarVariable = "New value"; // Allowed

let myLetVariable = "First value";
myLetVariable = "New value"; // Allowed
```

### `const`: Cannot be Reassigned

Variables declared with `const` (short for constant) must be initialized at the time of declaration and **cannot be reassigned** a new value.

```javascript
const myConstVariable = "This value is constant";
// myConstVariable = "Trying to change"; // TypeError: Assignment to constant variable.
```

**Important Note for Objects and Arrays:**
When you declare an object or array with `const`, it means the **reference** to that object/array is constant, not its content. You can still modify the properties of the object or the elements of the array.

```javascript
const myObj = { name: "Alice" };
myObj.name = "Bob"; // This is allowed!
console.log(myObj.name); // "Bob"

const myArray = [1, 2, 3];
myArray.push(4); // This is also allowed!
console.log(myArray); // [1, 2, 3, 4]

// But you cannot reassign the variable itself
// myObj = { name: "Charlie" }; // TypeError
// myArray = [5, 6]; // TypeError
```

## Summary and Best Practices

| Keyword | Scope         | Hoisting                               | Reassignment | Redeclaration (in same scope) |
| :-----: | :------------ | :------------------------------------- | :----------: | :---------------------------: |
| `var`   | Function      | Hoisted and initialized to `undefined` |      Yes     |              Yes              |
| `let`   | Block         | Hoisted, but not initialized (TDZ)     |      Yes     |               No              |
| `const` | Block         | Hoisted, but not initialized (TDZ)     |      No      |               No              |

Here are the modern JavaScript best practices for variable declaration:

1.  **Use `const` by default**: This makes your code more predictable by preventing accidental reassignments. It signals that the variable's identifier will not be reassigned.
2.  **Use `let` only when you know you need to reassign the variable**: This is typically for loop counters or variables that need to be updated within a block.
3.  **Avoid using `var`**: There is generally no reason to use `var` in modern JavaScript (ES6+). Its function-scoping and hoisting behavior can lead to bugs that `let` and `const` were designed to prevent.

By following these rules, you will write clearer, more reliable, and easier-to-debug JavaScript code.
