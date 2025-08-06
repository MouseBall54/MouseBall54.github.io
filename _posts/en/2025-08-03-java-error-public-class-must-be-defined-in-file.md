---
typora-root-url: ../
layout: single
title: >
    How to Fix Java Error: a public class ... must be defined in a file called ... .java

lang: en
translation_id: java-error-public-class-must-be-defined-in-file
header:
   teaser: /images/header_images/overlay_image_java.png
   overlay_image: /images/header_images/overlay_image_java.png
   overlay_filter: 0.5
excerpt: >
    Understand and resolve the Java compile error that occurs when the name of a `public` class does not match the name of its `.java` file.
categories:
  - en_Troubleshooting
tags:
  - Java
  - Compilation Error
  - public class
---

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
