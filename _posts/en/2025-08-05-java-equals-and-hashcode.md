typora-root-url: ../
layout: single
title: >
   Understanding equals() and hashCode() in Java
date: 2025-08-05T10:20:00+09:00
header:
   teaser: /images/header_images/overlay_image_java.png
   overlay_image: /images/header_images/overlay_image_java.png
   overlay_filter: 0.5
excerpt: >
    Learn why you must always override hashCode() if you override equals() in Java. Understand the contract between these two methods and how they work with hash-based collections.
categories:
  - en_Troubleshooting
tags:
  - Java
  - equals
  - hashCode
  - Collections
  - Best Practices
---
## The Contract Between `equals()` and `hashCode()`

In Java, the `equals()` and `hashCode()` methods, both defined in the `Object` class, are fundamental for determining object equality. When you create custom classes, you often need to override `equals()` to define logical equality (based on object state) rather than reference equality (based on memory address).

However, there's a critical rule you must follow: **If you override `equals()`, you MUST override `hashCode()`.**

This is because of the contract between them, which is essential for the correct functioning of hash-based collections like `HashMap`, `HashSet`, and `Hashtable`.

The contract states:
1.  If two objects are equal according to the `equals(Object)` method, then calling the `hashCode()` method on each of the two objects must produce the same integer result.
2.  It is *not* required that if two objects are unequal according to the `equals(Object)` method, then calling the `hashCode()` method on each of the two objects must produce distinct integer results. However, producing distinct results for unequal objects may improve the performance of hash tables.

### Why is this Contract Important?

Hash-based collections use the `hashCode()` method to determine where to store an object in memory (which "bucket" to put it in). When you try to retrieve an object (e.g., with `map.get(key)` or `set.contains(object)`), the collection does the following:

1.  It calculates the hash code of the object you're looking for.
2.  It uses this hash code to quickly find the bucket where the object *should* be.
3.  It then iterates through the (usually small) number of objects in that bucket, using the `equals()` method to find the exact match.

### What Happens if You Break the Contract?

Let's say you have a `User` class and you override `equals()` but not `hashCode()`.

```java
class User {
    private int id;
    private String email;

    // Constructor, getters...

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        User user = (User) o;
        return id == user.id && email.equals(user.email);
    }

    // Missing hashCode() override!
}
```

Now, let's use this class in a `HashSet`:

```java
User user1 = new User(1, "test@example.com");
User user2 = new User(1, "test@example.com");

System.out.println("user1.equals(user2): " + user1.equals(user2)); // true

Set<User> userSet = new HashSet<>();
userSet.add(user1);

System.out.println("userSet.contains(user2): " + userSet.contains(user2)); // false!
```

**Why does `contains()` return `false`?**

1.  When `userSet.add(user1)` is called, `HashSet` calculates `user1.hashCode()` (using the default implementation from `Object`, which is based on memory address) and stores `user1` in a bucket corresponding to that hash code.
2.  When `userSet.contains(user2)` is called, `HashSet` calculates `user2.hashCode()`. Since `user1` and `user2` are different objects in memory, their default hash codes are different.
3.  `HashSet` looks in the bucket for `user2`'s hash code, which is a different bucket from where `user1` is stored. It doesn't find anything, so it immediately returns `false` without ever calling `equals()`.

The collection fails to find an object that is logically equal because the broken contract led it to look in the wrong place.

### How to Correctly Override `hashCode()`

To fix this, you must implement `hashCode()` so that it produces the same hash for objects that are considered equal. A good `hashCode()` implementation should use the same fields that are used in the `equals()` method.

**Correct Implementation:**

```java
import java.util.Objects;

class User {
    private int id;
    private String email;

    // Constructor, getters...

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        User user = (User) o;
        return id == user.id && Objects.equals(email, user.email);
    }

    @Override
    public int hashCode() {
        // Use Objects.hash() to easily generate a hash code from the fields.
        return Objects.hash(id, email);
    }
}
```

With this corrected `hashCode()`, `user1.hashCode()` and `user2.hashCode()` will be the same. The `HashSet` will now correctly find the bucket and then use `equals()` to confirm the match, returning `true` for `contains()`.

### Key Takeaway

Always override `hashCode()` when you override `equals()`. The easiest and safest way to do this is by using the `java.util.Objects.hash()` utility method, passing it the same fields you used in your `equals()` implementation.
