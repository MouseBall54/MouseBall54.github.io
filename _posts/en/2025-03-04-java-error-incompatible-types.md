---
typora-root-url: ../
layout: single
title: >
    How to Fix "Error: incompatible types" in Java

date: 2025-03-04T07:22:00+09:00
lang: en
translation_id: java-error-incompatible-types
header:
    teaser: /images/header_images/overlay_image_java.png
    overlay_image: /images/header_images/overlay_image_java.png
    overlay_filter: 0.5
    image_description: >
      A visual summary explaining the main topic of this post: How to Fix "Error: incompatible types" in Java
excerpt: >
    In Java, the "incompatible types" error is a compilation error that occurs when you try to assign a value of an incompatible type to a variable or pass it to a method. This article explains its causes and solutions.
seo_description: >
    In Java, the "incompatible types" error is a compilation error that occurs when you try to assign a value of an incompatible type to a variable or pass it to a method. This article explains its causes and solutions.
categories:
    - en_Troubleshooting
tags:
    - Java
    - Compilation Error
    - Type System
---


![A visual summary explaining the main topic of this post: How to Fix "Error: incompatible types" in Java](/images/header_images/overlay_image_java.png)
## What is "Error: incompatible types" in Java?

`Error: incompatible types` is a compile-time error that occurs when Java's static type system determines that the type of a value you are trying to assign to a variable is not compatible with the variable's declared type. Java places a strong emphasis on type safety, so the compiler strictly checks for type mismatch issues before the code is executed.

The error message usually tells you clearly what type was required and what type was found.

**Error Message Format:**
`incompatible types: <found_type> cannot be converted to <required_type>`

**Error Example:**
```java
public class TypeTest {
    public static void main(String[] args) {
        // Trying to assign a String to an int variable
        int number = "123"; 
    }
}
```

**Compilation Error:**
```
TypeTest.java:4: error: incompatible types: String cannot be converted to int
        int number = "123";
                     ^
```

## Common Causes and Solutions for "incompatible types"

### 1. Assigning a Value of the Wrong Type to a Variable

This is the most basic cause. It occurs when you try to directly assign a value of a different type to a variable.

-   **Solution**: Assign a value of the correct type to the variable, or change the variable's type to match the value. If a type conversion is needed, use an appropriate conversion method.
    ```java
    // Solution 1: Assign a value of the correct type
    int number = 123;

    // Solution 2: Convert the string to an integer
    String text = "123";
    int numberFromString = Integer.parseInt(text);
    ```

### 2. Mismatch between Method Return Type and Variable Type

This occurs when the type of the value returned by a method is not compatible with the type of the variable intended to receive that value.

-   **Solution**: Use a variable that matches the method's return type, or verify that the method is returning the correct type as intended.
    ```java
    public class MethodTest {
        public String getName() {
            return "Java";
        }

        public static void main(String[] args) {
            MethodTest mt = new MethodTest();
            // int nameLength = mt.getName(); // Error: Cannot assign String to int
            String name = mt.getName(); // Correct type
            int nameLength = name.length(); // Get the length of the String
        }
    }
    ```

### 3. Incorrect Type Assignment in Inheritance (Downcasting)

This happens when you try to assign an object of a parent class type to a variable of a child class type without an explicit cast. This is because while every `Dog` is an `Animal`, not every `Animal` is a `Dog`.

-   **Solution**: Check if the downcast is safe using the `instanceof` operator, and then perform an explicit cast.
    ```java
    class Animal {}
    class Dog extends Animal {}

    public class CastingTest {
        public static void main(String[] args) {
            Animal myAnimal = new Dog();
            // Dog myDog = myAnimal; // Error: Cannot assign Animal to Dog

            if (myAnimal instanceof Dog) {
                Dog myDog = (Dog) myAnimal; // Explicit cast
            }
        }
    }
    ```

### 4. Generic Type Mismatch

This occurs when the type parameters do not match in collections that use generics.

-   **Solution**: Use objects of a type that matches the declared generic type.
    ```java
    import java.util.ArrayList;
    import java.util.List;

    public class GenericTest {
        public static void main(String[] args) {
            List<String> names = new ArrayList<>();
            // names.add(123); // Error: Cannot add int to List<String>
            names.add("Java"); // Correct
        }
    }
    ```

## Conclusion

`Error: incompatible types` is a helpful error that allows you to catch potential bugs at compile time, thanks to Java's strong type system. When you encounter this error, carefully examine the "required" and "found" types provided by the compiler and modify your code to make the two types compatible. You can resolve the issue by changing the value's type, changing the variable's type, or performing an explicit cast.

## Professional Depth Check

For **How to Fix "Error: incompatible types" in Java**, the practical standard is not whether the reader can repeat one instruction once. Treat the topic as a reproducible debugging procedure: verify runtime environment, exact error boundary, minimal reproduction, and rollback path before drawing a conclusion. The result should be written as a small decision record, because future readers need to know which fact was observed, which assumption was used, and which condition would change the answer.

### Evidence That Makes the Guidance Reliable

Use objective evidence before changing a workflow. Good evidence includes full command output, version numbers, changed files, and expected versus actual behavior. If two pieces of evidence conflict, keep the conflict visible instead of smoothing it over. For example, a successful quick fix is still weak evidence if the same input, account, dependency, or device state has not been tested again. A durable article should help the reader distinguish a confirmed fix from a plausible fix.

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
