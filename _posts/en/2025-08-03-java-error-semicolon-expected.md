---
typora-root-url: ../
layout: single
title: >
    How to Fix Java Error: ';' expected (A Fundamental Mistake)
date: 2025-08-03T11:40:00+09:00
header:
   teaser: /images/header_images/overlay_image_java.png
   overlay_image: /images/header_images/overlay_image_java.png
   overlay_filter: 0.5
excerpt: >
    Learn how to fix the basic `Error: ';' expected` compile error in Java, which occurs when you forget to terminate a statement with a semicolon (;).
categories:
  - en_Troubleshooting
tags:
  - Java
  - Compilation Error
  - SyntaxError
---

## The Problem

The `Error: ';' expected` is one of the most common compilation errors, especially for those new to Java. The meaning of this error is straightforward: the Java compiler **expected a semicolon (`;`) at a certain point in the code but did not find one.**

In Java, the semicolon is a crucial piece of syntax that marks the end of a statement. Most statements—such as variable declarations, value assignments, method calls, and `return` statements—must be terminated with a semicolon.

## Examples of Error-Prone Code

The most common cause is simply forgetting a semicolon at the end of a line.

### 1. Missing Semicolon in a Variable Declaration

```java
public class Main {
    public static void main(String[] args) {
        String message = "Hello, World!" // Semicolon is missing.
        System.out.println(message);
    }
}
```

The compiler expects a semicolon after the statement `String message = "Hello, World!"`. When it instead encounters `System.out.println(message)` on the next line, it reports an error. The error message will look something like this:

```
Main.java:4: error: ';' expected
        System.out.println(message)
                                   ^
```
Note that the error is often reported at the beginning of the *next* line, as that's where the compiler realized something was wrong.

### 2. Missing Semicolon in a Method Call

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello") // Semicolon is missing.
    }
}
```

## The Solution

This is a purely syntactical error, so there is only one way to fix it.

### Add a Semicolon (`;`)

Check the location indicated by the compiler and add the missing semicolon at the end of the preceding statement.

```java
// Corrected Code
public class Main {
    public static void main(String[] args) {
        String message = "Hello, World!"; // Semicolon added.
        System.out.println(message);
    }
}
```

### When Not to Use a Semicolon

For clarity, it's worth noting that not every line in Java ends with a semicolon. You do not use them in the following cases:

-   **Class or method declarations:** `public class Main { ... }` or `public void myMethod() { ... }`
-   **Control flow statements (the declaration part):** `if (condition) { ... }` or `for (int i=0; i<5; i++) { ... }`
-   **Package and import statements:** These are statements and *do* end with a semicolon, e.g., `package com.example;` and `import java.util.List;`.

A good rule of thumb is that you **do not place a semicolon after a closing curly brace `}`** that defines a code block.

## Conclusion

The `Error: ';' expected` occurs when you break one of the most fundamental syntax rules in Java. When you see this error:

1.  Look at the line the compiler points to, or the line directly above it.
2.  Check if the statement is properly terminated with a semicolon and add one if it's missing.

Most modern Integrated Development Environments (IDEs) will detect and highlight this mistake in real-time, making it much easier to catch before you even compile.
