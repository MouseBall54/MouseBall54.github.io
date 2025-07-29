---
typora-root-url: ../
layout: single
title: "How to Fix “NullPointerException” Error in Java"
date: 2025-07-24T22:00:00+09:00
excerpt: "NullPointerException happens when code accesses a null reference. Prevent it with null checks, proper initialization, Optional, and nullability annotations."
categories:
  - en_Troubleshooting
tags:
  - Java
  - NullPointerException
---

## Introduction

NullPointerException is one of the most common runtime errors in Java.
It occurs when you call a method or access a field on a null reference.
This guide shows typical causes and solutions.

## What Is NullPointerException?

Thrown by the JVM when you dereference a null pointer.
Example:

```java
String text = null;
int len = text.length(); // throws NullPointerException
```

## Common Causes

1. Calling methods on uninitialized objects.
2. Automatic unboxing of null wrapper types (e.g., `Integer`).
3. Methods returning null unexpectedly.
4. Missing checks after collection lookups or map gets.

## Solution 1: Add Null Checks

```java
if (text != null) {
  int len = text.length();
}
```

## Solution 2: Use Optional

```java
Optional<String> opt = Optional.ofNullable(text);
opt.ifPresent(s -> System.out.println(s.length()));
```

## Solution 3: Proper Initialization

Always initialize objects before use:

```java
List<String> list = new ArrayList<>();
// instead of List<String> list;
```

## Solution 4: Apply Nullability Annotations

Use `@NonNull` and `@Nullable` to document intent:

```java
public void process(@NonNull String input) { … }
```

IDEs and static analysis tools can warn you at compile time.

## Solution 5: Avoid Autounboxing Null

Check wrapper types before unboxing:

```java
Integer count = getCount();
if (count != null) {
  int c = count; // safe unboxing
}
```

## Conclusion

NullPointerException is avoidable.
Use null checks and initialize fields.
Leverage Optional and nullability annotations.
Adopt these practices for safer code.

