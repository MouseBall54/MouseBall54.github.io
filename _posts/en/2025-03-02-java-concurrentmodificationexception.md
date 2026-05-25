---
typora-root-url: ../
layout: single
title: >
    How to Handle ConcurrentModificationException in Java

date: 2025-03-02T07:20:00+09:00
lang: en
translation_id: java-concurrentmodificationexception
header:
   teaser: /images/header_images/overlay_image_java.png
   overlay_image: /images/header_images/overlay_image_java.png
   overlay_filter: 0.5
   image_description: >
     A visual summary explaining the main topic of this post: How to Handle ConcurrentModificationException in Java
excerpt: >
    Learn how to fix ConcurrentModificationException in Java. This exception occurs when a collection is modified while it is being iterated over.
seo_description: >
    Learn how to fix ConcurrentModificationException in Java. This exception occurs when a collection is modified while it is being iterated over.
categories:
  - en_Troubleshooting
tags:
  - Java
  - Exception
  - ConcurrentModificationException
  - Collections
---


![A visual summary explaining the main topic of this post: How to Handle ConcurrentModificationException in Java](/images/header_images/overlay_image_java.png)
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

## Professional Depth Check

For **How to Handle ConcurrentModificationException in Java**, the practical standard is not whether the reader can repeat one instruction once. Treat the topic as a reproducible debugging procedure: verify JDK version, build tool configuration, classpath or module path, and runtime stack trace before drawing a conclusion. The result should be written as a small decision record, because future readers need to know which fact was observed, which assumption was used, and which condition would change the answer.

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
