---
typora-root-url: ../
layout: single
title: >
    How to Fix "RecursionError: maximum recursion depth exceeded" in Python

date: 2025-03-21T07:39:00+09:00
lang: en
translation_id: python-recursion-error
header:
    teaser: /images/header_images/overlay_image_python.png
    overlay_image: /images/header_images/overlay_image_python.png
    overlay_filter: 0.5
    image_description: >
      A visual summary explaining the main topic of this post: How to Fix "RecursionError: maximum recursion depth exceeded" in Python
excerpt: >
    In Python, a RecursionError occurs when the depth of recursive calls exceeds the maximum limit. This article explains the cause of the error and how to fix it.
seo_description: >
    In Python, a RecursionError occurs when the depth of recursive calls exceeds the maximum limit. This article explains the cause of the error and how to fix it.
categories:
    - en_Troubleshooting
tags:
    - Python
    - RecursionError
    - Recursion
---


![A visual summary explaining the main topic of this post: How to Fix "RecursionError: maximum recursion depth exceeded" in Python](/images/header_images/overlay_image_python.png)
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

## Professional Depth Check

For **How to Fix "RecursionError: maximum recursion depth exceeded" in Python**, the practical standard is not whether the reader can repeat one instruction once. Treat the topic as a reproducible debugging procedure: verify runtime environment, exact error boundary, minimal reproduction, and rollback path before drawing a conclusion. The result should be written as a small decision record, because future readers need to know which fact was observed, which assumption was used, and which condition would change the answer.

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
