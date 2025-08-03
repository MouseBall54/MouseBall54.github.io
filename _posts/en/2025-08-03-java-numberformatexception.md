---
typora-root-url: ../
layout: single
title: >
    How to Handle java.lang.NumberFormatException
date: 2025-08-03T10:05:00+09:00
header:
   teaser: /images/header_images/overlay_image_java.png
   overlay_image: /images/header_images/overlay_image_java.png
   overlay_filter: 0.5
excerpt: >
    Learn how to fix the java.lang.NumberFormatException, which occurs when you try to convert a string with an improper format into a numeric value.
categories:
  - en_Troubleshooting
tags:
  - Java
  - Exception
  - NumberFormatException
  - Debugging
---

## What is NumberFormatException?

`java.lang.NumberFormatException` is an unchecked exception thrown in Java when an application tries to convert a string into a numeric type (like `int`, `float`, `double`, etc.), but the string is not in a convertible format. This typically happens when using methods like `Integer.parseInt()`, `Double.parseDouble()`, or `Float.parseFloat()`.

For example, if you try to parse the string `"123"` into an integer, it will work perfectly. However, if you try to parse `"abc"` or `"12.3"` into an integer, a `NumberFormatException` will be thrown.

## Common Causes and Solutions

Let's look at the common scenarios that lead to this exception and how to prevent or handle them.

### 1. String Contains Non-Numeric Characters

The most frequent cause is trying to parse a string that contains letters, symbols, or other characters that are not digits.

**Problematic Code:**
```java
public class Main {
    public static void main(String[] args) {
        String notANumber = "hello123";
        int number = Integer.parseInt(notANumber); // Throws NumberFormatException
        System.out.println(number);
    }
}
```

**Solution:**
You should validate the string before parsing it. A `try-catch` block is the standard way to handle this exception gracefully.

**Corrected Code:**
```java
public class Main {
    public static void main(String[] args) {
        String notANumber = "hello123";
        try {
            int number = Integer.parseInt(notANumber);
            System.out.println(number);
        } catch (NumberFormatException e) {
            System.err.println("The string is not a valid integer: " + notANumber);
            // e.printStackTrace(); // For debugging
        }
    }
}
```
This code will catch the exception and print a user-friendly error message instead of crashing the program.

### 2. String Contains Whitespace

Leading or trailing whitespace in the string can also cause a `NumberFormatException`.

**Problematic Code:**
```java
String withWhitespace = "  123  ";
int number = Integer.parseInt(withWhitespace); // Throws NumberFormatException
```
*Note: `Integer.parseInt()` can actually handle whitespace since Java 1.4, but other parsers or older versions might not. It's still good practice to trim the string.*

**Solution:**
Use the `trim()` method of the `String` class to remove any leading or trailing whitespace before parsing.

**Corrected Code:**
```java
String withWhitespace = "  123  ";
try {
    int number = Integer.parseInt(withWhitespace.trim());
    System.out.println(number); // Output: 123
} catch (NumberFormatException e) {
    System.err.println("Error parsing string with whitespace.");
}
```

### 3. Parsing a Floating-Point Number as an Integer

If you try to parse a string representing a floating-point number (e.g., `"19.99"`) using `Integer.parseInt()`, it will fail because the period (`.`) is not a valid character for an integer.

**Problematic Code:**
```java
String floatString = "19.99";
int number = Integer.parseInt(floatString); // Throws NumberFormatException
```

**Solution:**
First, parse the string into a `Double` or `Float`, and then, if necessary, cast it to an `int`.

**Corrected Code:**
```java
String floatString = "19.99";
try {
    double doubleValue = Double.parseDouble(floatString);
    int number = (int) doubleValue; // Casting to int
    System.out.println(number); // Output: 19
} catch (NumberFormatException e) {
    System.err.println("The string is not a valid number: " + floatString);
}
```

### 4. Special Characters or Symbols

Strings containing currency symbols, commas, or other special characters cannot be parsed directly.

**Problematic Code:**
```java
String currencyValue = "$1,000";
int number = Integer.parseInt(currencyValue); // Throws NumberFormatException
```

**Solution:**
You need to preprocess the string to remove these special characters before parsing.

**Corrected Code:**
```java
String currencyValue = "$1,000";
try {
    String cleanString = currencyValue.replace("$", "").replace(",", "");
    int number = Integer.parseInt(cleanString);
    System.out.println(number); // Output: 1000
} catch (NumberFormatException e) {
    System.err.println("Error parsing currency string.");
}
```

## Best Practices for Prevention

- **Always use a `try-catch` block:** Never assume a string will be in the correct format. Wrapping parsing logic in a `try-catch` block is the safest way to prevent your application from crashing.
- **Validate input:** Before attempting to parse, validate the user input. You can use regular expressions to check if a string contains only numeric characters.
- **Preprocess strings:** Use methods like `trim()` and `replace()` to clean up strings before parsing them.

By following these guidelines, you can effectively handle `NumberFormatException` and make your Java applications more robust and user-friendly.
