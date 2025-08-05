typora-root-url: ../
layout: single
title: >
   Prevent Memory Leaks with try-with-resources in Java
date: 2025-08-05T11:00:00+09:00
header:
   teaser: /images/header_images/overlay_image_java.png
   overlay_image: /images/header_images/overlay_image_java.png
   overlay_filter: 0.5
excerpt: >
    Learn how to use the try-with-resources statement in Java to automatically close resources like streams and connections, preventing common memory leaks and making your code cleaner.
categories:
  - en_Troubleshooting
tags:
  - Java
  - try-with-resources
  - Memory Management
  - Best Practices
---
## The Problem: Resource Leaks

In Java, when you work with external resources like file streams, database connections, or network sockets, you must explicitly close them when you are finished. If you fail to do so, the resource may remain open, consuming system memory or database connections. This is known as a **resource leak**, and it can eventually lead to your application crashing with an `OutOfMemoryError` or other critical failures.

### The Old Way: `finally` Block

Before Java 7, the standard way to ensure a resource was closed was to use a `finally` block. This pattern is verbose and error-prone.

**Classic `finally` block:**
```java
FileReader reader = null;
try {
    reader = new FileReader("file.txt");
    // ... work with the reader
} catch (IOException e) {
    // handle exception
} finally {
    if (reader != null) {
        try {
            reader.close(); // This can also throw an IOException
        } catch (IOException e) {
            // handle close exception
        }
    }
}
```

This code is clumsy. The `close()` call is nested inside another `try-catch` block because `close()` itself can throw an `IOException`. This makes the code hard to read and maintain.

## The Solution: `try-with-resources`

Java 7 introduced the `try-with-resources` statement to simplify this process. It automatically closes any resource that implements the `java.lang.AutoCloseable` or `java.io.Closeable` interface.

### How it Works

You declare the resource within parentheses after the `try` keyword. The Java runtime guarantees that the `close()` method of the resource will be called at the end of the block, whether the `try` block completes normally or an exception is thrown.

**`try-with-resources` example:**
```java
import java.io.FileReader;
import java.io.IOException;

public void readFile() {
    try (FileReader reader = new FileReader("file.txt")) {
        // ... work with the reader
        // The reader is automatically closed here!
    } catch (IOException e) {
        // Handle exception from FileReader constructor or reading
    }
}
```

This code is much cleaner and safer:
- **Concise:** No need for a `finally` block or a null check.
- **Safe:** The resource is guaranteed to be closed.
- **Suppressed Exceptions:** If an exception is thrown inside the `try` block and another is thrown by the `close()` method, the exception from the `close()` method is *suppressed*. The primary exception is the one that gets propagated, which is usually what you want.

### Using Multiple Resources

You can declare multiple resources in a `try-with-resources` statement by separating them with a semicolon. They will be closed in the reverse order of their creation.

```java
import java.io.FileInputStream;
import java.io.BufferedInputStream;
import java.io.IOException;

public void readMultipleFiles() {
    try (FileInputStream fis = new FileInputStream("file1.txt");
         BufferedInputStream bis = new BufferedInputStream(fis)) {
        // Work with bis
        // bis will be closed first, then fis
    } catch (IOException e) {
        // Handle exceptions
    }
}
```

### Who Can Be Used with `try-with-resources`?

Any object that implements `java.lang.AutoCloseable` can be used. This interface has a single method, `void close() throws Exception`. Most standard Java resources that need closing, such as `InputStream`, `OutputStream`, `Reader`, `Writer`, `java.sql.Connection`, `Statement`, and `ResultSet`, implement this interface.

You can also implement `AutoCloseable` in your own custom classes to enable them to be used in a `try-with-resources` statement.

```java
class MyResource implements AutoCloseable {
    public MyResource() {
        System.out.println("Resource created.");
    }

    public void doWork() {
        System.out.println("Doing work.");
    }

    @Override
    public void close() {
        System.out.println("Resource closed.");
    }
}

// Usage
public void useCustomResource() {
    try (MyResource res = new MyResource()) {
        res.doWork();
    }
    // "Resource created.", "Doing work.", "Resource closed." will be printed.
}
```

### Key Takeaway

Always use the `try-with-resources` statement when working with resources that need to be closed. It is the modern, safe, and preferred way to manage resources in Java, effectively preventing resource leaks and simplifying your code.
