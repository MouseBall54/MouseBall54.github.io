---
typora-root-url: ../
layout: single
title: >
    How to Fix Java Error: a public class ... must be defined in a file called ... .java

date: 2025-03-06T07:24:00+09:00
lang: en
translation_id: java-error-public-class-must-be-defined-in-file
header:
   teaser: /images/header_images/overlay_image_java.png
   overlay_image: /images/header_images/overlay_image_java.png
   overlay_filter: 0.5
   image_description: >
     A visual summary explaining the main topic of this post: How to Fix Java Error: a public class ... must be defined in a file called ... .java
excerpt: >
    Understand and resolve the Java compile error that occurs when the name of a `public` class does not match the name of its `.java` file.
seo_description: >
    Understand and resolve the Java compile error that occurs when the name of a `public` class does not match the name of its `.java` file.
categories:
  - en_Troubleshooting
tags:
  - Java
  - Compilation Error
  - public class
---


![A visual summary explaining the main topic of this post: How to Fix Java Error: a public class ... must be defined in a file called ... .java](/images/header_images/overlay_image_java.png)
## The Problem

When you compile a Java source file, you might encounter the following error message:

```
Error: a public class <ClassName> must be defined in a file called <ClassName>.java
```

This error occurs when you violate one of the fundamental rules of Java: **a single source file (`.java`) can contain at most one `public` class, and the name of that `public` class must exactly match the source file's name (including case).**

This rule helps the Java compiler and runtime environment locate and load classes efficiently from the file system.

## Example of Error-Prone Code

Let's say you have a file named `MyProgram.java` with the following content:

**File Name: `MyProgram.java`**

```java
// The file is named MyProgram.java, but the public class is named HelloWorld.
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

When you try to compile this code, the compiler expects the `public` class `HelloWorld` to be in a file named `HelloWorld.java`. Since it's in `MyProgram.java`, it will produce an error like this:

```
MyProgram.java:2: error: class HelloWorld is public, should be declared in a file named HelloWorld.java
public class HelloWorld {
       ^
1 error
```

## How to Fix It

This problem is very simple to fix.

### 1. Rename the File to Match the Class Name

The most common solution is to rename the `.java` file to match the name of the `public` class.

-   In the example above, you would rename the file `MyProgram.java` to `HelloWorld.java`.

This is the preferred method when you want to keep the class name as it is.

### 2. Rename the Class to Match the File Name

Alternatively, if you want to keep the file name, you can change the name of the `public` class to match it.

-   You would modify the content of `MyProgram.java` as follows:

**File Name: `MyProgram.java`**

```java
// Change the class name to match the file name, MyProgram.
public class MyProgram {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

### 3. Remove the `public` Keyword from the Class (Not Recommended)

If the class does not need to be accessed from other packages, you can remove the `public` access modifier. A non-public (package-private) class does not have the restriction of matching the file name.

**File Name: `MyProgram.java`**

```java
// Removing the public keyword allows the class and file names to be different.
class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

However, this changes the accessibility of your class and should be done with caution. In most cases, keeping the class `public` and ensuring the names match is the best practice.

## Conclusion

The `Error: a public class ... must be defined in a file called ... .java` is caused by a mismatch between the `public` class name and the file name. To resolve it, choose one of the following:

1.  Change the **file name** to match the `public` class name.
2.  Change the **`public` class name** to match the file name.

Adhering to this naming convention is a standard practice in Java that improves code organization and readability. It's best to always follow this rule.

## Professional Depth Check

For **How to Fix Java Error: a public class ... must be defined in a file called ... .java**, the practical standard is not whether the reader can repeat one instruction once. Treat the topic as a reproducible debugging procedure: verify JDK version, build tool configuration, classpath or module path, and runtime stack trace before drawing a conclusion. The result should be written as a small decision record, because future readers need to know which fact was observed, which assumption was used, and which condition would change the answer.

### Evidence That Makes the Guidance Reliable

Use objective evidence before changing a workflow. Good evidence includes `java -version`, `javac -version`, Maven or Gradle output, and the smallest failing class. If two pieces of evidence conflict, keep the conflict visible instead of smoothing it over. For example, a successful quick fix is still weak evidence if the same input, account, dependency, or device state has not been tested again. A durable article should help the reader distinguish a confirmed fix from a plausible fix.

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
