---
typora-root-url: ../
layout: single
title: "How to Fix java.lang.ArrayIndexOutOfBoundsException"

date: 2025-01-08T07:12:00+09:00
lang: en
translation_id: java-arrayindexoutofboundsexception
excerpt: "java.lang.ArrayIndexOutOfBoundsException is a common runtime exception that occurs when you try to access an array with an invalid index. This article explains the causes of the error and how to fix it."
seo_description: "java.lang.ArrayIndexOutOfBoundsException is a common runtime exception that occurs when you try to access an array with an invalid index. This article explains the causes of the error and how to fix it."
header:
   teaser: /images/header_images/overlay_image_java.png
   overlay_image: /images/header_images/overlay_image_java.png
   overlay_filter: 0.5
   image_description: >
     A visual summary explaining the main topic of this post: How to Fix java.lang.ArrayIndexOutOfBoundsException
categories:
  - en_Troubleshooting
tags:
  - Java
  - Exception
  - Array
  - Troubleshooting
---


![A visual summary explaining the main topic of this post: How to Fix java.lang.ArrayIndexOutOfBoundsException](/images/header_images/overlay_image_java.png)
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

## Professional Depth Check

For **How to Fix java.lang.ArrayIndexOutOfBoundsException**, the practical standard is not whether the reader can repeat one instruction once. Treat the topic as a reproducible debugging procedure: verify JDK version, build tool configuration, classpath or module path, and runtime stack trace before drawing a conclusion. The result should be written as a small decision record, because future readers need to know which fact was observed, which assumption was used, and which condition would change the answer.

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
