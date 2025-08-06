---
typora-root-url: ../
layout: single
title: "How to Fix java.lang.ArrayIndexOutOfBoundsException"

lang: en
translation_id: java-arrayindexoutofboundsexception
excerpt: "java.lang.ArrayIndexOutOfBoundsException is a common runtime exception that occurs when you try to access an array with an invalid index. This article explains the causes of the error and how to fix it."
header:
   teaser: /images/header_images/overlay_image_java.png
   overlay_image: /images/header_images/overlay_image_java.png
   overlay_filter: 0.5
categories:
  - en_Troubleshooting
tags:
  - Java
  - Exception
  - Array
  - Troubleshooting
---

## What is java.lang.ArrayIndexOutOfBoundsException?

`java.lang.ArrayIndexOutOfBoundsException` is a very common runtime exception when working with arrays in Java.
This error occurs when you try to access an index that does not exist in the array.
In Java, an array's index starts at `0` and goes up to `array length - 1`.
If you use an index outside of this range, the JVM (Java Virtual Machine) will throw this exception.

## Main Causes

The cause of this error is clear: accessing an index without checking the array's boundaries.

### 1. Using an Incorrect Index Value

This is the most common case, where an index is used without considering the length of the array.

```java
public class Example {
    public static void main(String[] args) {
        String[] fruits = {"Apple", "Banana", "Cherry"};
        // The length of the array is 3, so valid indices are 0, 1, 2
        
        // Error occurs: index 3 does not exist
        System.out.println(fruits[3]); 
    }
}
```

In the code above, the length of the `fruits` array is 3, so the valid indices are 0, 1, and 2.
However, the code attempts to access index 3, which causes an `ArrayIndexOutOfBoundsException`.

### 2. Incorrect Loop Condition

When using a loop, this error can occur if the loop condition is set to go beyond the array's boundaries.

```java
public class LoopExample {
    public static void main(String[] args) {
        int[] numbers = new int[5]; // Indices are from 0 to 4
        
        // Error occurs: tries to access numbers[5] when i becomes 5
        for (int i = 0; i <= numbers.length; i++) {
            numbers[i] = i;
        }
    }
}
```

The condition of the `for` loop is set to `i <= numbers.length`.
Since `numbers.length` is 5, `i` will iterate from 0 to 5.
In the last iteration when `i` is 5, it tries to access `numbers[5]`, causing the exception.
The loop condition should be `i < numbers.length` to be correct.

### 3. Accessing an Empty Array

The error can also occur if you try to access a specific index of an empty or `null` array.
Of course, accessing a `null` array will first result in a `NullPointerException`.

## How to Fix It

### 1. Check the Index Range

The most basic solution is to always check if the index is within the valid range before accessing the array.

```java
public class SafeAccessExample {
    public static void main(String[] args) {
        String[] fruits = {"Apple", "Banana", '"Cherry"'};
        int index = 3;

        if (index >= 0 && index < fruits.length) {
            System.out.println(fruits[index]);
        } else {
            System.out.println("Invalid index: " + index);
        }
    }
}
```

By using an `if` statement to check if the index is greater than or equal to `0` and less than the `array length`, you can prevent the error.

### 2. Use an Enhanced for-loop (for-each)

When accessing all elements of an array sequentially, it is safer and more concise to use an enhanced `for` loop that does not handle indices directly.

```java
public class ForEachExample {
    public static void main(String[] args) {
        String[] fruits = {"Apple", "Banana", "Cherry"};
        
        for (String fruit : fruits) {
            System.out.println(fruit);
        }
    }
}
```

The enhanced `for` loop internally manages the array's boundaries, so there is no room for an `ArrayIndexOutOfBoundsException` to occur.

## Conclusion

`ArrayIndexOutOfBoundsException` is a simple but critical error caused by not checking the array's boundaries.
It is a good habit to always check the valid range before accessing an array index, and if possible, use the enhanced `for` loop that does not handle indices directly.
Following these basic principles will greatly help in writing stable code.
