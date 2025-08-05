---
typora-root-url: ../
layout: single
title: >
    How to Fix "RecursionError: maximum recursion depth exceeded" in Python
date: 2025-08-03T14:05:00+09:00
header:
    teaser: /images/header_images/overlay_image_python.png
    overlay_image: /images/header_images/overlay_image_python.png
    overlay_filter: 0.5
excerpt: >
    In Python, a RecursionError occurs when the depth of recursive calls exceeds the maximum limit. This article explains the cause of the error and how to fix it.
categories:
    - en_Troubleshooting
tags:
    - Python
    - RecursionError
    - Recursion
---

## What is "RecursionError: maximum recursion depth exceeded" in Python?

A `RecursionError` is an exception raised when a function calls itself too many times, exceeding the maximum recursion depth set by the Python interpreter. This is a safety measure to prevent a stack overflow, which typically occurs due to infinite recursion or a flawed termination condition in a recursive function.

## Common Causes of "RecursionError"

1.  **No Base Case**: The recursive function lacks a base case—a condition that stops the recursion and returns a value. Without it, the function will call itself indefinitely.
2.  **Incorrect Base Case**: The base case exists but is logically flawed, so it is never met.
3.  **Very Deep Recursion**: The algorithm naturally requires a recursion depth that exceeds Python's default limit.

## How to Fix "RecursionError"

### 1. Check and Correct the Base Case

The first step is to ensure your recursive function has a correct and reachable base case. Every recursive call must eventually lead to the base case.

**Incorrect Example (No Base Case):**
```python
def countdown(n):
    print(n)
    countdown(n - 1) # Causes infinite recursion

# countdown(10) # Raises RecursionError
```

**Correct Example:**
```python
def countdown(n):
    if n < 0:
        return  # Base case
    print(n)
    countdown(n - 1)

countdown(10)
```

### 2. Increase the Recursion Limit

If your algorithm is correct but requires deep recursion, you can increase the limit using the `sys` module. However, use this approach with caution, as it may not be the root solution and could lead to memory issues.

```python
import sys

# Check the current recursion limit
print(sys.getrecursionlimit()) # Default is usually 1000

# Set a new recursion limit
sys.setrecursionlimit(2000)

def deep_recursion(n):
    if n == 0:
        return
    deep_recursion(n - 1)

deep_recursion(1500) # Works correctly
```

### 3. Convert to an Iterative Approach

Most recursive functions can be rewritten using a loop (e.g., `for`, `while`). This approach is often more memory-efficient and fundamentally resolves the `RecursionError`.

**Recursive Example:**
```python
def factorial_recursive(n):
    if n == 1:
        return 1
    return n * factorial_recursive(n - 1)
```

**Iterative Example:**
```python
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
```

## Conclusion

A `RecursionError` is most often caused by a problem with the base case of a recursive function. Always start by debugging the termination condition. Only increase the recursion limit if you are certain the algorithm requires it. The best solution is often to convert the recursive algorithm into an iterative one, freeing it from stack depth limitations.
