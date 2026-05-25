---
typora-root-url: ../
layout: single
title: >
    How to Fix "Error: ';' expected" in Java

date: 2025-03-07T07:25:00+09:00
lang: en
translation_id: java-error-semicolon-expected
header:
    teaser: /images/header_images/overlay_image_java.png
    overlay_image: /images/header_images/overlay_image_java.png
    overlay_filter: 0.5
    image_description: >
      A visual summary explaining the main topic of this post: How to Fix "Error: ';' expected" in Java
excerpt: >
    In Java, "';' expected" is a basic compilation error that occurs when a semicolon is missing at the end of a statement. This article explains the cause of the error and how to fix it.
seo_description: >
    In Java, "';' expected" is a basic compilation error that occurs when a semicolon is missing at the end of a statement. This article explains the cause of the error and how to fix it.
categories:
    - en_Troubleshooting
tags:
    - Java
    - Compilation Error
    - Syntax
---


![A visual summary explaining the main topic of this post: How to Fix "Error: ';' expected" in Java](/images/header_images/overlay_image_java.png)
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

## Professional Depth Check

For **How to Fix "Error: ';' expected" in Java**, the practical standard is not whether the reader can repeat one instruction once. Treat the topic as a reproducible debugging procedure: verify runtime environment, exact error boundary, minimal reproduction, and rollback path before drawing a conclusion. The result should be written as a small decision record, because future readers need to know which fact was observed, which assumption was used, and which condition would change the answer.

### Evidence That Makes the Guidance Reliable

Use objective evidence before changing a workflow. Good evidence includes full command output, version numbers, changed files, and expected versus actual behavior. If two pieces of evidence conflict, keep the conflict visible instead of smoothing it over. For example, a successful quick fix is still weak evidence if the same input, account, dependency, or device state has not been tested again. A durable article should help the reader distinguish a confirmed fix from a plausible fix.

### Review Table

| Review Item | What To Confirm | Why It Matters |
| --- | --- | --- |
| Scope | The exact case covered by this article | Prevents over-applying the advice |
| Baseline | The state before any change | Makes rollback and comparison possible |
| Change | The smallest action taken | Reduces hidden side effects |
| Result | The observed output after the change | Separates evidence from expectation |
| Recheck | When to revisit the conclusion | Keeps the post accurate over time |

### Edge Cases and Failure Modes

The main risks are fixing the symptom while leaving the root cause, and mixing unrelated changes into the same test. When the situation involves production data, personal information, money, health, legal rights, or security recovery, the conservative path is to stop and collect evidence before applying a broad fix. The same title can describe very different cases, so the reader should compare their environment with the assumptions in the post before copying commands or decisions.

### Maintenance Standard

Recheck this guidance after dependency, operating-system, or build-tool changes. A useful update does not need to rewrite the entire post; it should confirm whether the examples, links, commands, screenshots, and decision criteria still match current behavior. If the old conclusion remains valid, record the check date. If it changes, explain what changed and why the previous advice is no longer enough.

## Related Reading

Continue with these related posts from the same topic area.

- [How to Fix "SSL: CERTIFICATE_VERIFY_FAILED" Error in Python on Windows](/en_troubleshooting/python-certificate-verify-failed/)
- [How to Fix "Permission denied (publickey)" Error with Git on Windows](/en_troubleshooting/git-permission-denied-publickey-windows/)
