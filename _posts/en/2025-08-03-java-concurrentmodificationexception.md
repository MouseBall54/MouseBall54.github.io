---
typora-root-url: ../
layout: single
title: >
    How to Handle ConcurrentModificationException in Java

lang: en
translation_id: java-concurrentmodificationexception
header:
   teaser: /images/header_images/overlay_image_java.png
   overlay_image: /images/header_images/overlay_image_java.png
   overlay_filter: 0.5
excerpt: >
    Learn how to fix ConcurrentModificationException in Java. This exception occurs when a collection is modified while it is being iterated over.
categories:
  - en_Troubleshooting
tags:
  - Java
  - Exception
  - ConcurrentModificationException
  - Collections
---

## What is ConcurrentModificationException?

This exception occurs in Java.
It is related to collections like `ArrayList` or `HashMap`.
The error happens during iteration.
You iterate over a collection.
Simultaneously, you try to modify it.
Modification can be adding, removing, or updating elements.
This action is not allowed for most standard collections.
The iterator detects the change.
It then throws `ConcurrentModificationException`.
This is a "fail-fast" behavior.
It prevents unpredictable outcomes from concurrent modification.

## Common Cause and Solution

The main cause is modifying a collection while iterating it.

### Modifying a List During Iteration

A common mistake is removing an element inside a for-each loop.

**Problematic Code:**
```java
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<String> fruits = new ArrayList<>();
        fruits.add("Apple");
        fruits.add("Banana");
        fruits.add("Cherry");

        // This loop will throw ConcurrentModificationException
        for (String fruit : fruits) {
            if (fruit.equals("Banana")) {
                fruits.remove("Banana"); 
            }
        }
    }
}
```
The for-each loop uses an iterator internally.
Calling `fruits.remove()` changes the list's structure.
The iterator detects this and fails.

**Solution 1: Use an Iterator Explicitly**

You can use the iterator's `remove()` method.
This is the safe way to modify a collection during iteration.

**Corrected Code:**
```java
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<String> fruits = new ArrayList<>();
        fruits.add("Apple");
        fruits.add("Banana");
        fruits.add("Cherry");

        Iterator<String> iterator = fruits.iterator();
        while (iterator.hasNext()) {
            String fruit = iterator.next();
            if (fruit.equals("Banana")) {
                iterator.remove(); // Safe removal
            }
        }
        System.out.println(fruits); // Output: [Apple, Cherry]
    }
}
```

**Solution 2: Use `removeIf()` (Java 8+)**

For simple conditional removal, Java 8 introduced `removeIf()`.
It is more concise and less error-prone.

**Corrected Code (Java 8+):**
```java
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<String> fruits = new ArrayList<>();
        fruits.add("Apple");
        fruits.add("Banana");
        fruits.add("Cherry");

        fruits.removeIf(fruit -> fruit.equals("Banana")); // Clean and safe

        System.out.println(fruits); // Output: [Apple, Cherry]
    }
}
```

**Solution 3: Create a Copy for Iteration**

You can iterate over a copy of the collection.
Then, you can safely modify the original collection.
This is useful for more complex logic than just removal.

**Corrected Code:**
```java
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<String> fruits = new ArrayList<>();
        fruits.add("Apple");
        fruits.add("Banana");
        fruits.add("Cherry");

        List<String> toRemove = new ArrayList<>();
        for (String fruit : fruits) {
            if (fruit.equals("Banana")) {
                toRemove.add(fruit);
            }
        }
        fruits.removeAll(toRemove);

        System.out.println(fruits); // Output: [Apple, Cherry]
    }
}
```

## Conclusion

`ConcurrentModificationException` is a common issue.
It protects you from bugs in multi-threaded and single-threaded code.
Never modify a collection directly inside a for-each loop.
Instead, use an `Iterator`, the `removeIf()` method, or a temporary collection.
Choosing the right method depends on your specific needs.
These practices will help you write safer and cleaner Java code.
