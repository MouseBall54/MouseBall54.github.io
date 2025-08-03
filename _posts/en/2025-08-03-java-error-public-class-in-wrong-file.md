---
typora-root-url: ../
layout: single
title: >
    How to Fix "Error: a public class ... must be defined in a file called ... .java" in Java
date: 2025-08-03T14:30:00+09:00
header:
    teaser: /images/header_images/overlay_image_java.png
    overlay_image: /images/header_images/overlay_image_java.png
    overlay_filter: 0.5
excerpt: >
    This compilation error in Java occurs when the name of a public class does not match the name of its source file. This article explains the cause of the error and how to fix it.
categories:
    - en_Troubleshooting
tags:
    - Java
    - Compilation Error
    - Class
---

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

---
*Work History*
- *2025-08-03: Initial draft created*
