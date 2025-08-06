---
typora-root-url: ../
layout: single
title: >
   JavaScript Equality: == vs. === (Loose vs. Strict)

lang: en
translation_id: javascript-equality-double-vs-triple-equals
header:
   teaser: /images/header_images/overlay_image_js.png
   overlay_image: /images/header_images/overlay_image_js.png
   overlay_filter: 0.5
excerpt: >
   Learn the critical difference between loose equality (==) and strict equality (===) in JavaScript. Understand how type coercion works and why you should almost always use === to avoid common bugs.
categories:
   - en_Troubleshooting
tags:
   - JavaScript
   - Equality
   - Type Coercion
   - Operators
   - Best Practices
---

## Introduction

In JavaScript, comparing two values for equality can be done with two different operators: `==` (loose equality) and `===` (strict equality). For beginners, the distinction can be confusing, but understanding it is fundamental to writing predictable and bug-free code. The core difference lies in how they handle data types.

This guide will break down the behavior of `==` and `===`, explain the concept of type coercion, and make a clear recommendation on which operator you should use.

## Strict Equality (`===`)

Let's start with the simpler and more predictable operator: strict equality.

The strict equality operator (`===`) checks if two values are equal **without performing any type conversion**. It returns `true` only if both the values and the data types are the same.

**Examples:**
```javascript
console.log(7 === 7);       // true (same value, same type)
console.log('hello' === 'hello'); // true (same value, same type)

console.log(7 === '7');     // false (different types: number vs. string)
console.log(true === 1);      // false (different types: boolean vs. number)
console.log(null === undefined); // false (different types)
```

Because it doesn't try to convert types, its behavior is straightforward and easy to reason about. What you see is what you get.

## Loose Equality (`==`)

The loose equality operator (`==`) is more complex. It checks if two values are equal after **attempting to convert them to a common type**. This conversion process is called **type coercion**.

Because of type coercion, the results can sometimes be non-intuitive.

**Examples:**
```javascript
console.log(7 == '7');     // true (string '7' is coerced to number 7)
console.log(true == 1);      // true (boolean true is coerced to number 1)
console.log(false == 0);     // true (boolean false is coerced to number 0)
console.log(null == undefined); // true (this is a special case in the language spec)

console.log('' == 0);       // true (empty string is coerced to number 0)
console.log('\t\r\n' == 0); // true (string with only whitespace is coerced to 0)
```

### The Dangers of Type Coercion

While type coercion might seem convenient, it often leads to subtle bugs that are hard to track down. The rules for coercion are complex and can produce unexpected results.

Consider this example:
```javascript
console.log('0' == false); // true
console.log(0 == false);   // true

// But this means...
console.log('0' == 0);   // true
```
This kind of transitive but inconsistent logic can make code difficult to maintain and debug.

Another infamous example:
```javascript
console.log([] == ![]); // true
// Why? 
// ![] (not an empty array) is false.
// The comparison becomes [] == false.
// The empty array [] is coerced to the number 0.
// The boolean false is coerced to the number 0.
// The comparison becomes 0 == 0, which is true.
```
This is a perfect illustration of how loose equality can be confusing.

## `==` vs. `===`: The Comparison

| Operator | Name             | Compares Values | Compares Types | Type Coercion | Predictability |
| :------: | :--------------- | :-------------: | :------------: | :-----------: | :-------------: |
| `==`     | Loose Equality   |       Yes       |       No       |      Yes      |       Low       |
| `===`    | Strict Equality  |       Yes       |      Yes       |      No       |      High       |

## Which One Should You Use? The Golden Rule

The overwhelming consensus among experienced JavaScript developers is:

> **Always use `===` (strict equality) and `!==` (strict inequality) unless you have a specific, deliberate reason to use `==`.**

Using strict equality:
-   **Prevents Bugs**: It eliminates a whole class of bugs caused by unexpected type coercion.
-   **Improves Readability**: Your code becomes easier to understand because there are no hidden conversions happening. The intent is clear.
-   **Encourages Better Code**: It forces you to be explicit about your data types. If you need to compare a number with a string, you should perform the conversion yourself (e.g., `Number('7')`) to make the operation clear.

### The Only Common Exception: Checking for `null` or `undefined`

One of the few widely accepted use cases for `==` is to check if a value is either `null` or `undefined` at the same time, because `null == undefined` is `true`.

```javascript
let myVar;

// Instead of this:
if (myVar === null || myVar === undefined) {
    console.log('Variable is null or undefined');
}

// You can do this:
if (myVar == null) {
    console.log('Variable is null or undefined');
}
```
Even this is a matter of style, and many developers still prefer the explicit `===` checks for clarity.

## Conclusion

While `==` and `===` both check for equality, they are not interchangeable. The loose equality operator (`==`) can introduce subtle and confusing bugs into your code through its automatic type coercion. The strict equality operator (`===`) is predictable, reliable, and leads to clearer, more maintainable code.

By making `===` your default choice, you will write more robust JavaScript and avoid many common pitfalls. Save `==` for the rare cases where you intentionally want to leverage its type-coercing behavior.
