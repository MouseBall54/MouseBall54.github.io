---
typora-root-url: ../
layout: single
title: >
    How to Fix "Error: ';' expected" in Java
date: 2025-08-03T14:40:00+09:00
header:
    teaser: /images/header_images/overlay_image_java.png
    overlay_image: /images/header_images/overlay_image_java.png
    overlay_filter: 0.5
excerpt: >
    In Java, "';' expected" is a basic compilation error that occurs when a semicolon is missing at the end of a statement. This article explains the cause of the error and how to fix it.
categories:
    - en_Troubleshooting
tags:
    - Java
    - Compilation Error
    - Syntax
---

## What is "Error: ';' expected" in Java?

`Error: ';' expected` is a syntax error that occurs when the Java compiler does not find a semicolon (`;`) where it syntactically expects a statement to end. In Java, the semicolon is a crucial piece of syntax that signals the end of each command or declaration.

This error usually means that a semicolon is missing on the line where the error occurred or on the line immediately preceding it.

**Error Example:**
```java
public class SemicolonTest {
    public static void main(String[] args) {
        int number = 10 // Missing semicolon
        System.out.println("The number is: " + number)
    }
}
```

**Compilation Error:**
```
SemicolonTest.java:4: error: ';' expected
        int number = 10
                       ^
SemicolonTest.java:5: error: ';' expected
        System.out.println("The number is: " + number)
                                                     ^
```
The compiler detects that a semicolon is missing on the `int number = 10` line and reports an error. As a result of this error, it becomes syntactically confused on the next line, `System.out.println(...)`, and may report additional errors.

## Common Causes and Solutions for "';' expected"

### 1. Missing Semicolon at the End of a Statement

This is the most common cause. Every statement, including variable declarations, method calls, and value assignments, must end with a semicolon.

- **Solution**: Add a semicolon at the end of the statement.
    ```java
    // Before
    int x = 5

    // After
    int x = 5;
    ```

### 2. Syntax Error in a `for` Loop

This can happen if you use a comma (`,`) instead of a semicolon or omit a semicolon when separating the initialization, condition, and increment parts of a `for` loop.

- **Solution**: Each part of the `for` loop must be separated by a semicolon.
    ```java
    // Incorrect
    // for (int i = 0, i < 10, i++) {}

    // Correct
    for (int i = 0; i < 10; i++) {}
    ```

### 3. Error in Method Declaration

If you accidentally add a semicolon after a method signature, the compiler will assume the method declaration ends there and treat the method body (`{}`) as a syntax error, which can lead to this error.

- **Solution**: Do not put a semicolon after the method signature (name and parameter list). The exceptions are abstract methods or methods in an interface.
    ```java
    // Incorrect
    // public void myMethod(); {
    //     System.out.println("Hello");
    // }

    // Correct
    public void myMethod() {
        System.out.println("Hello");
    }
    ```

### 4. Error in Array Initialization Syntax

This occurs when you forget the semicolon after the closing brace (`}`) of an array initializer.

- **Solution**: Add a semicolon at the end of the array initialization statement.
    ```java
    // Before
    // int[] numbers = {1, 2, 3}

    // After
    int[] numbers = {1, 2, 3};
    ```

## Tips for Reading the Error Message

When you encounter a `';' expected` error, pay close attention to the location pointed to by the compiler (`^` symbol). In most cases, a semicolon is needed at or just before the reported location. Sometimes, a single missing semicolon can cause a cascade of multiple `';' expected` or other syntax errors, so it is always best to start by fixing the first error message.

## Conclusion

`Error: ';' expected` occurs when you violate one of the most basic syntax rules in Java. When you face this error, don't panic. It is important to get into the habit of carefully checking that every statement ends with a semicolon, focusing on the location the compiler provides.
