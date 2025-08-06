typora-root-url: ../
layout: single
title: >
   Java: String vs. StringBuilder vs. StringBuffer

lang: en
translation_id: java-string-vs-stringbuilder-vs-stringbuffer
header:
   teaser: /images/header_images/overlay_image_java.png
   overlay_image: /images/header_images/overlay_image_java.png
   overlay_filter: 0.5
excerpt: >
    Understand the key differences between String, StringBuilder, and StringBuffer in Java to write more efficient and optimized code for string manipulation.
categories:
  - en_Troubleshooting
tags:
  - Java
  - String
  - StringBuilder
  - StringBuffer
  - Performance
---
## String vs. StringBuilder vs. StringBuffer in Java

In Java, strings seem simple, but how you work with them can have a significant impact on performance. Java provides three main classes for handling sequences of characters: `String`, `StringBuilder`, and `StringBuffer`. Understanding their differences is crucial for writing efficient code.

### 1. `String`

The `String` class is the most basic and commonly used. The key characteristic of a `String` object is that it is **immutable**.

- **Immutability:** Once a `String` object is created, its value cannot be changed. Every time you "modify" a string (e.g., by concatenation), you are actually creating a new `String` object in memory.

**Example:**
```java
String s = "Hello";
s = s + " World"; // Creates a new String object "Hello World"
                  // The original "Hello" is now eligible for garbage collection
```

- **When to use `String`:**
  - When the string value will not change.
  - For simple, infrequent concatenations.
  - In multi-threaded environments where thread safety for the value is needed without explicit locking.

- **Performance:** Frequent concatenation with `String` objects is inefficient because it creates many intermediate objects, leading to higher memory consumption and more work for the garbage collector.

### 2. `StringBuilder`

`StringBuilder` was introduced in Java 5 to address the performance issues of `String`. It is a **mutable** sequence of characters.

- **Mutability:** You can append, insert, or delete characters from a `StringBuilder` without creating a new object each time. It modifies the internal character array.
- **Not Thread-Safe:** `StringBuilder` is not synchronized. This means it is not safe for use by multiple threads simultaneously. However, this lack of synchronization makes it faster than `StringBuffer`.

**Example:**
```java
StringBuilder sb = new StringBuilder("Hello");
sb.append(" World"); // Modifies the existing object
System.out.println(sb.toString()); // "Hello World"
```

- **When to use `StringBuilder`:**
  - In a single-threaded environment.
  - When you need to perform many string modifications (e.g., building a long string in a loop). This is the most common choice for a "string builder".

- **Performance:** It offers the best performance for string manipulation in a single-threaded context.

### 3. `StringBuffer`

`StringBuffer` is very similar to `StringBuilder`. It is also a **mutable** sequence of characters. The main difference is its thread safety.

- **Mutability:** Like `StringBuilder`, it can be modified without creating new objects.
- **Thread-Safe:** `StringBuffer` is synchronized. Its methods (like `append`, `insert`) are `synchronized`, meaning they can be safely used by multiple threads without causing data corruption. This synchronization adds a performance overhead.

**Example:**
```java
StringBuffer sbf = new StringBuffer("Hello");
sbf.append(" World"); // This operation is thread-safe
System.out.println(sbf.toString()); // "Hello World"
```

- **When to use `StringBuffer`:**
  - In a multi-threaded environment where multiple threads might modify the same string buffer.
  - In older Java code (before Java 5, it was the only mutable option).

- **Performance:** It is slower than `StringBuilder` due to the overhead of synchronization.

### Summary of Differences

| Feature          | `String`                               | `StringBuilder`                        | `StringBuffer`                         |
| ---------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- |
| **Mutability**   | Immutable                              | Mutable                                | Mutable                                |
| **Thread Safety**| Thread-safe (due to immutability)      | Not thread-safe (unsynchronized)       | Thread-safe (synchronized)             |
| **Performance**  | Slow for frequent modifications        | Fast (best for single-threaded)        | Slow (due to synchronization)          |
| **Introduced**   | Since JDK 1.0                          | Since Java 5 (JDK 1.5)                 | Since JDK 1.0                          |

### Conclusion

- Use **`String`** for fixed string values or simple concatenations.
- Use **`StringBuilder`** for most string building tasks in a single-threaded environment (this is the default choice for mutable strings).
- Use **`StringBuffer`** only when you need a mutable string that is shared across multiple threads.
