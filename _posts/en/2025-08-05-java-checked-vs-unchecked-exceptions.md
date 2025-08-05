typora-root-url: ../
layout: single
title: >
   Java Exceptions: Checked vs. Unchecked
date: 2025-08-05T10:25:00+09:00
header:
   teaser: /images/header_images/overlay_image_java.png
   overlay_image: /images/header_images/overlay_image_java.png
   overlay_filter: 0.5
excerpt: >
    Learn the difference between checked and unchecked exceptions in Java, when to use them, and how they impact your code's design and robustness.
categories:
  - en_Troubleshooting
tags:
  - Java
  - Exceptions
  - Checked Exception
  - Unchecked Exception
  - Best Practices
---
## Understanding Java's Exception Hierarchy

In Java, all exception and error types are subclasses of the `Throwable` class. This class has two main direct subclasses: `Error` and `Exception`.

- **`Error`**: Represents critical problems that a reasonable application should not try to catch, such as `OutOfMemoryError` or `StackOverflowError`. These are almost always unrecoverable.
- **`Exception`**: Represents conditions that a reasonable application might want to catch. This is the class we focus on for exception handling.

The `Exception` class itself is the parent for two categories of exceptions: **checked exceptions** and **unchecked exceptions**.

![Java Exception Hierarchy](https://i.imgur.com/s5l4VjD.png)
*(A simplified diagram of the exception hierarchy)*

### Checked Exceptions

A **checked exception** is an exception that the Java compiler *checks* at compile-time. They are subclasses of `Exception` but do not extend `RuntimeException`.

- **Rule:** If a method can throw a checked exception, it must either handle it using a `try-catch` block or declare it in its signature using the `throws` keyword.
- **Purpose:** They are used for predictable but unpreventable problems that arise from external conditions. The caller of the method is forced to consider how to handle these failure scenarios.
- **Examples:**
  - `IOException`: An error occurred during an I/O operation (e.g., reading a file that doesn't exist).
  - `SQLException`: An error occurred while interacting with a database.
  - `ClassNotFoundException`: A class needed at runtime could not be found.

**Example:**
```java
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

public void readFile(String fileName) throws IOException { // Declaring the exception
    File file = new File(fileName);
    FileReader reader = new FileReader(file);
    // ... read the file
}

public void processFile() {
    try {
        readFile("my-file.txt"); // Handling the exception
    } catch (IOException e) {
        System.err.println("Failed to read file: " + e.getMessage());
    }
}
```

### Unchecked Exceptions

An **unchecked exception** is an exception that the compiler does *not* check at compile-time. In Java, these are all subclasses of `RuntimeException`.

- **Rule:** You are not required to handle or declare unchecked exceptions.
- **Purpose:** They typically represent programming errors or logic flaws, such as bugs in your code. These are problems that should ideally be fixed rather than handled at runtime.
- **Examples:**
  - `NullPointerException`: Trying to access a member of a `null` object reference.
  - `ArrayIndexOutOfBoundsException`: Using an illegal index to access an array.
  - `IllegalArgumentException`: Passing an invalid argument to a method.
  - `NumberFormatException`: Trying to convert a non-numeric string to a number.

**Example:**
```java
public void printLength(String text) {
    // No need to declare NullPointerException
    // The caller is expected to pass a valid, non-null string
    System.out.println(text.length()); 
}

public void run() {
    // Calling code is not forced to use try-catch
    printLength(null); // This will throw a NullPointerException at runtime
}
```

### Key Differences Summarized

| Feature             | Checked Exception                               | Unchecked Exception (RuntimeException)          |
| ------------------- | ----------------------------------------------- | ----------------------------------------------- |
| **Compiler Check**  | Yes (checked at compile-time)                   | No (not checked at compile-time)                |
| **Handling**        | Must be handled (`try-catch`) or declared (`throws`) | Optional to handle or declare                 |
| **Parent Class**    | `Exception` (but not `RuntimeException`)        | `RuntimeException`                              |
| **Represents**      | Recoverable external conditions (e.g., I/O)     | Programming errors/bugs (e.g., null pointer)    |
| **Example**         | `IOException`, `SQLException`                   | `NullPointerException`, `IndexOutOfBoundsException` |

### When to Use Which?

- **Use checked exceptions** for conditions from which the caller can realistically be expected to recover. If a client can take some useful recovery action, a checked exception is a good choice. For example, if a file isn't found, the user could be prompted to enter a different file name.
- **Use unchecked exceptions** to indicate programming errors. A `NullPointerException` suggests a bug that should be fixed in the code (e.g., by adding a null check) rather than caught and handled by the caller.

By understanding the distinction, you can design more robust and maintainable APIs and applications in Java.
