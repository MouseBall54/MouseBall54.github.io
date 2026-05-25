---
typora-root-url: ../
layout: single
title: "How to Handle java.lang.UnsupportedOperationException"

date: 2025-08-01T00:00:00+09:00
lang: en
translation_id: java-unsupportedoperationexception
header:
   teaser: /images/header_images/overlay_image_java.png
   overlay_image: /images/header_images/overlay_image_java.png
   overlay_filter: 0.5
   image_description: >
     A visual summary explaining the main topic of this post: How to Handle java.lang.UnsupportedOperationException
excerpt: >
  Understand and resolve `UnsupportedOperationException` in Java, which typically occurs when trying to modify unmodifiable collections like those from `Arrays.asList()`.
seo_description: >
  Understand and resolve `UnsupportedOperationException` in Java, which typically occurs when trying to modify unmodifiable collections like those from `Arrays.asList()`.
categories:
  - en_Troubleshooting
tags:
  - Java
  - Exception
  - Collections
  - UnsupportedOperationException
---


![A visual summary explaining the main topic of this post: How to Handle java.lang.UnsupportedOperationException](/images/header_images/overlay_image_java.png)
`java.lang.UnsupportedOperationException` is a common runtime exception in Java that signals a requested operation is not supported. While it can be thrown by any method, it most frequently appears when working with the Java Collections Framework, particularly when trying to modify an unmodifiable collection.

This article explores the common causes of this exception and provides clear solutions.

### Why Does `UnsupportedOperationException` Occur?

This exception is thrown to indicate that an object does not support a particular method, even though its class or interface declares it. The most classic example involves trying to add or remove elements from a fixed-size or unmodifiable collection.

#### Common Cause: Modifying a List from `Arrays.asList()`

The most frequent source of this exception is the `List` returned by `java.util.Arrays.asList()`.

```java
import java.util.Arrays;
import java.util.List;

public class ExceptionExample {
    public static void main(String[] args) {
        String[] array = {"one", "two"};
        List<String> list = Arrays.asList(array);

        // This line will throw UnsupportedOperationException
        list.add("three"); 
    }
}
```

**Why does this happen?**
The `Arrays.asList()` method does not create a standard `java.util.ArrayList`. Instead, it returns a private inner class (`java.util.Arrays$ArrayList`) that is a wrapper around the original array. This list is **fixed-size**. You can change existing elements (e.g., `list.set(0, "new_one")`), but you cannot change its size by adding or removing elements. The `add()` and `remove()` methods are not implemented and thus throw `UnsupportedOperationException`.

### How to Fix the Exception

The solution is to create a new, modifiable collection from the unmodifiable one.

#### Solution: Create a Modifiable `ArrayList`

To fix the issue, wrap the list from `Arrays.asList()` in a new `java.util.ArrayList` instance. This creates a true, modifiable copy.

```java
import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;

public class SolutionExample {
    public static void main(String[] args) {
        String[] array = {"one", "two"};
        List<String> fixedList = Arrays.asList(array);

        // Create a new, modifiable ArrayList from the fixed-size list
        List<String> modifiableList = new ArrayList<>(fixedList);

        // Now, this works perfectly
        modifiableList.add("three"); 

        System.out.println(modifiableList); // Output: [one, two, three]
    }
}
```

By passing the fixed-size list to the `ArrayList` constructor, you create a new list that supports all collection operations, including adding and removing elements.

#### Other Causes

While `Arrays.asList()` is the most common trigger, other scenarios can also cause this exception:

1.  **Unmodifiable Collections**: Using methods like `Collections.unmodifiableList()`, `Collections.unmodifiableSet()`, or `Collections.unmodifiableMap()`. These are explicitly designed to prevent modification.
    ```java
    List<String> list = new ArrayList<>();
    list.add("a");
    List<String> unmodifiable = Collections.unmodifiableList(list);
    unmodifiable.add("b"); // Throws UnsupportedOperationException
    ```

2.  **Immutable Collections (Java 9+)**: Using `List.of()`, `Set.of()`, or `Map.of()`. These factory methods create truly immutable collections.
    ```java
    List<String> immutableList = List.of("a", "b");
    immutableList.add("c"); // Throws UnsupportedOperationException
    ```

3.  **Keys of a Map**: The `keySet()` method of a `Map` returns a `Set` view of the keys. You cannot add elements to this set, though you can remove them (which also removes the entry from the map).

### Conclusion

`UnsupportedOperationException` is a clear signal that you are trying to perform an action that an object was not designed for. When you encounter it with collections, it usually means you are trying to change the size of a fixed-size or unmodifiable collection. The standard solution is to create a new, modifiable collection instance (like an `ArrayList` or `HashSet`) from the existing one.

## Professional Depth Check

For **How to Handle java.lang.UnsupportedOperationException**, the practical standard is not whether the reader can repeat one instruction once. Treat the topic as a reproducible debugging procedure: verify JDK version, build tool configuration, classpath or module path, and runtime stack trace before drawing a conclusion. The result should be written as a small decision record, because future readers need to know which fact was observed, which assumption was used, and which condition would change the answer.

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
