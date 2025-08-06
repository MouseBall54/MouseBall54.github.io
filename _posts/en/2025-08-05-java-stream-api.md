typora-root-url: ../
layout: single
title: >
   Processing Data with Java Stream API

lang: en
translation_id: java-stream-api
header:
   teaser: /images/header_images/overlay_image_java.png
   overlay_image: /images/header_images/overlay_image_java.png
   overlay_filter: 0.5
excerpt: >
    Discover the power of the Java Stream API for processing collections of data. Learn how to use streams to write declarative, efficient, and readable code for complex data manipulations.
categories:
  - en_Troubleshooting
tags:
  - Java
  - Stream API
  - Functional Programming
  - Collections
---
## What is the Stream API?

Introduced in Java 8, the **Stream API** is a powerful tool for processing sequences of elements, such as collections. A stream is not a data structure itself; instead, it takes input from collections, arrays, or I/O channels and allows you to perform complex data processing operations on that data in a functional, declarative style.

### Key Characteristics of Streams

- **Declarative:** You describe *what* you want to do, not *how* to do it. This leads to more readable code compared to traditional loops.
- **Pipelining:** Many stream operations return a stream themselves, allowing you to chain operations together in a pipeline.
- **Internal Iteration:** Unlike collections where you iterate externally (e.g., with a `for-each` loop), streams handle iteration internally.
- **Consumable:** A stream can only be traversed once. After a terminal operation is performed, the stream is consumed and cannot be reused.

### From Imperative to Declarative Style

Let's consider a simple task: given a list of `Person` objects, find the names of all people older than 18, sorted alphabetically.

**Imperative Style (Traditional Loop):**
```java
List<Person> people = ...;
List<String> result = new ArrayList<>();

for (Person p : people) {
    if (p.getAge() > 18) {
        result.add(p.getName());
    }
}

Collections.sort(result);
```
This code is verbose. It involves creating an intermediate list and explicitly managing the iteration and sorting.

**Declarative Style (Stream API):**
```java
List<Person> people = ...;
List<String> result = people.stream() // 1. Get a stream from the list
    .filter(p -> p.getAge() > 18)      // 2. Filter people older than 18
    .map(Person::getName)              // 3. Map Person objects to their names
    .sorted()                          // 4. Sort the names
    .collect(Collectors.toList());     // 5. Collect the results into a new list
```
This stream pipeline is much more concise and expressive. It clearly states the sequence of operations.

### Common Stream Operations

Stream operations are divided into two categories:

#### 1. Intermediate Operations

These operations transform a stream into another stream. They are always **lazy**, meaning they don't execute until a terminal operation is invoked.

- **`filter(Predicate<T>)`**: Returns a stream consisting of the elements that match the given predicate.
- **`map(Function<T, R>)`**: Returns a stream consisting of the results of applying the given function to the elements.
- **`sorted()`**: Returns a sorted stream.
- **`distinct()`**: Returns a stream with duplicate elements removed.
- **`limit(long n)`**: Truncates the stream to be no longer than `n` in length.

#### 2. Terminal Operations

These operations produce a result or a side-effect. After the terminal operation is performed, the stream pipeline is considered consumed and can't be used again.

- **`collect(Collector<T, A, R>)`**: Performs a mutable reduction operation, such as collecting elements into a `List`, `Set`, or `Map`.
- **`forEach(Consumer<T>)`**: Performs an action for each element of the stream.
- **`count()`**: Returns the count of elements in the stream.
- **`findFirst()`**: Returns an `Optional` describing the first element.
- **`anyMatch(Predicate<T>)`**: Returns whether any elements match the given predicate.
- **`reduce(...)`**: Performs a reduction on the elements of the stream (e.g., summing numbers).

### Example: A More Complex Pipeline

Let's find the total salary of all unique, active employees who are older than 30.

```java
class Employee {
    // getters for name, age, salary, isActive...
}

List<Employee> employees = ...;

double totalSalary = employees.stream()
    .filter(e -> e.getAge() > 30)       // Keep employees older than 30
    .filter(Employee::isActive)         // Keep active employees
    .distinct()                         // Ensure each employee is counted once
    .mapToDouble(Employee::getSalary)   // Get their salaries as a DoubleStream
    .sum();                             // Sum the salaries
```

### Parallel Streams

The Stream API also makes it easy to parallelize operations. By simply calling `parallelStream()` instead of `stream()`, the API will attempt to process the data in parallel across multiple threads, potentially speeding up execution on multi-core processors.

```java
long count = people.parallelStream()
    .filter(p -> p.getAge() > 18)
    .count();
```

**Caution:** Parallel streams are not always faster. They have overhead and are best suited for large datasets and operations that are computationally expensive and can be easily parallelized.

### Key Takeaway

The Stream API is an essential part of modern Java development. It allows you to write highly readable, declarative code for complex data processing tasks. By chaining intermediate and terminal operations, you can create powerful and efficient data pipelines that are easier to reason about than traditional imperative code.
