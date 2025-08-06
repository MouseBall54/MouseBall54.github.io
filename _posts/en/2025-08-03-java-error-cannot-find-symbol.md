---
typora-root-url: ../
layout: single
title: >
    How to Fix "Error: cannot find symbol" in Java

lang: en
translation_id: java-error-cannot-find-symbol
header:
    teaser: /images/header_images/overlay_image_java.png
    overlay_image: /images/header_images/overlay_image_java.png
    overlay_filter: 0.5
excerpt: >
    In Java, "cannot find symbol" is a very common compilation error that occurs when the compiler cannot find the identifier (variable, method, class, etc.) used in the code. This article explains its causes and solutions.
categories:
    - en_Troubleshooting
tags:
    - Java
    - Compilation Error
    - Symbol
---

## What is "Error: cannot find symbol" in Java?

The `cannot find symbol` error means that the Java compiler does not recognize the declaration for an identifier (a symbol) in your code. A "symbol" here refers to any name a developer defines and uses, such as a variable name, method name, class name, or interface name. The error is the compiler's way of saying, "I don't know what '...' is or where it is defined."

The error message usually consists of three parts:
- **symbol**: The name of the symbol that cannot be found.
- **location**: The location (class or method) where the error occurred.
- **(optional) variable ... of type ...**: The context in which the symbol was used.

**Error Example:**
```java
public class SymbolTest {
    public static void main(String[] args) {
        Strng message = "Hello, World!"; // Typo: String -> Strng
        System.out.println(mesage); // Typo: message -> mesage
    }
}
```

**Compilation Error:**
```
SymbolTest.java:3: error: cannot find symbol
        Strng message = "Hello, World!";
        ^
  symbol:   class Strng
  location: class SymbolTest
SymbolTest.java:4: error: cannot find symbol
        System.out.println(mesage);
                           ^
  symbol:   variable mesage
  location: class SymbolTest
```

## Common Causes and Solutions for "cannot find symbol"

### 1. Typo

This is the most frequent cause. It happens when the spelling of a variable, method, or class name differs between its declaration and its use. Remember that Java is case-sensitive.

- **Solution**: Correct the name of the symbol to be consistent in both the declaration and usage. In the example above, changing `Strng` to `String` and `mesage` to `message` will fix the error.

### 2. Missing `import` Statement

This occurs when you use a class from another package without importing it. For example, to use `ArrayList`, you must import `java.util.ArrayList`.

- **Solution**: Add an `import` statement for the required class at the top of your source file.
    ```java
    import java.util.ArrayList;

    public class MyClass {
        public static void main(String[] args) {
            ArrayList<String> list = new ArrayList<>();
        }
    }
    ```

### 3. Incorrect Variable Scope

This happens when you try to access a variable outside of the scope (block) in which it was declared. For instance, a variable declared inside a `for` loop cannot be used outside the loop.

- **Solution**: Declare the variable in a wider scope that includes the code block where you intend to use it.
    ```java
    public class ScopeTest {
        public void test() {
            int myVar = 0; // Declared outside the block
            for (int i = 0; i < 5; i++) {
                myVar = i;
            }
            System.out.println(myVar); // Works correctly
        }
    }
    ```

### 4. Incorrect Method Call

This occurs when you try to call a method that does not exist or call a method with a different number or type of parameters.

- **Solution**: Check that the method signature (name and parameters) you are calling matches the one defined in the class.

### 5. Library/Classpath Issues

This happens when you use an external library (.jar file) but do not include it in the classpath during compilation.

- **Solution**: Use the `-cp` or `-classpath` option in the `javac` command to specify the path to the library. If you are using an IDE (like Eclipse or IntelliJ), you need to add the library to the project's build path.
    ```bash
    javac -cp "/path/to/library.jar;." MyProgram.java
    ```

## Conclusion

The `cannot find symbol` error usually stems from a minor mistake. By carefully examining the symbol and location indicated in the error message and checking the following points in order, you can easily resolve it:
1.  Is there a typo in the name?
2.  Have I imported the necessary classes?
3.  Is the variable's scope correct?
4.  Does the method signature match?
5.  Is the external library included in the classpath?

