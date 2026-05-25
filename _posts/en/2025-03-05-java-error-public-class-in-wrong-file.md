---
typora-root-url: ../
layout: single
title: >
    How to Fix "Error: a public class ... must be defined in a file called ... .java" in Java

date: 2025-03-05T07:23:00+09:00
lang: en
translation_id: java-error-public-class-in-wrong-file
header:
    teaser: /images/header_images/overlay_image_java.png
    overlay_image: /images/header_images/overlay_image_java.png
    overlay_filter: 0.5
    image_description: >
      A visual summary explaining the main topic of this post: How to Fix "Error: a public class ... must be defined in a file called ... .java" in Java
excerpt: >
    This compilation error in Java occurs when the name of a public class does not match the name of its source file. This article explains the cause of the error and how to fix it.
seo_description: >
    This compilation error in Java occurs when the name of a public class does not match the name of its source file. This article explains the cause of the error and how to fix it.
categories:
    - en_Troubleshooting
tags:
    - Java
    - Compilation Error
    - Class
---


![A visual summary explaining the main topic of this post: How to Fix "Error: a public class ... must be defined in a file called ... .java" in Java](/images/header_images/overlay_image_java.png)
## What is "Error: a public class ... must be defined in a file called ... .java" in Java?

This error message is one of the most basic errors encountered when compiling Java source code with the Java compiler (javac). According to the Java Language Specification, a single source file (.java) can contain **at most one `public` class**. If a `public` class exists, the **name of the source file must exactly match the name of the `public` class, including case**.

## Common Causes of the Error

1.  **Mismatch between File Name and Class Name**: This is the most common cause. For example, this error will occur if a `public` class named `MyClass` is saved in a file named `MyProgram.java`.
2.  **Case Mismatch**: While your file system might be case-insensitive, the Java compiler is strictly case-sensitive. If the class `MyClass` is saved in a file named `myclass.java`, it will cause an error.
3.  **Multiple `public` Classes in One File**: Attempting to declare more than one `public` class within a single `.java` file will trigger this error.

**Error Example:**

In file `AnotherClass.java`:
```java
// The file is named AnotherClass.java, but the public class is named MyClass.
public class MyClass {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}

class AnotherClass {
    // ...
}
```

Compiling this code will produce the following error:
```
AnotherClass.java:2: error: class MyClass is public, should be declared in a file named MyClass.java
public class MyClass {
       ^
```

## How to Fix the Error

### 1. Match the File Name to the `public` Class Name

The simplest solution is to rename the `.java` file to match the name of the `public` class.

In the example above, renaming the file `AnotherClass.java` to `MyClass.java` will resolve the issue.

### 2. Match the Class Name to the File Name

If you cannot change the file name, modify the `public` class name to match the file name.

In file `AnotherClass.java`:
```java
// Match the class name to the file name, AnotherClass.
public class AnotherClass {
    public static void main(String[] args) {
        System.out.println("Hello from AnotherClass!");
    }
}

class MyClass {
    // ...
}
```

### 3. Remove the `public` Access Modifier from the Class

If the class does not need to be `public`, you can remove the `public` keyword to make it a package-private class. Non-`public` classes are not required to have names that match the file name. However, this means the class will not be accessible from other packages.

In file `AnotherClass.java`:
```java
// Remove public from MyClass to resolve the error.
class MyClass {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}

public class AnotherClass {
    // This class is public, so its name must match the file name.
}
```

## Conclusion

The "public class ... must be defined in a file called ... .java" error in Java occurs when you violate a fundamental rule of the language. This rule exists to help organize code and make it easier for the compiler and JVM to locate classes. To resolve the issue, it is important to get into the habit of ensuring that the file name and the `public` class name always match, including case.

## Professional Depth Check

For **How to Fix "Error: a public class ... must be defined in a file called ... .java" in Java**, the practical standard is not whether the reader can repeat one instruction once. Treat the topic as a reproducible debugging procedure: verify runtime environment, exact error boundary, minimal reproduction, and rollback path before drawing a conclusion. The result should be written as a small decision record, because future readers need to know which fact was observed, which assumption was used, and which condition would change the answer.

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

### Practical Questions Before Acting

- What is the smallest observable signal that proves the problem or decision is real?
- Which source is official, and which part is local judgment?
- What should be captured before making changes?
- What result would show that the guidance did not apply?
- Who needs the record if the same issue appears again?

## Related Reading

Continue with these related posts from the same topic area.

- [How to Fix "SSL: CERTIFICATE_VERIFY_FAILED" Error in Python on Windows](/en_troubleshooting/python-certificate-verify-failed/)
- [How to Fix "Permission denied (publickey)" Error with Git on Windows](/en_troubleshooting/git-permission-denied-publickey-windows/)
