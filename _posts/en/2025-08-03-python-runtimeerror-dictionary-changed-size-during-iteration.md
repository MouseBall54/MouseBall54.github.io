---
typora-root-url: ../
layout: single
title: >
    How to Fix Python RuntimeError: dictionary changed size during iteration
date: 2025-08-03T10:00:00+09:00
header:
   teaser: /images/header_images/overlay_image_python.png
   overlay_image: /images/header_images/overlay_image_python.png
   overlay_filter: 0.5
excerpt: >
    Learn how to fix the `RuntimeError: dictionary changed size during iteration` in Python, which occurs when you modify a dictionary while looping over it.
categories:
  - en_Troubleshooting
tags:
  - Python
  - RuntimeError
  - Dictionary
  - Iteration
---

## The Problem

When you try to add or remove items from a dictionary while iterating over it using a `for` loop in Python, you might encounter the following `RuntimeError`:

```
RuntimeError: dictionary changed size during iteration
```

This error occurs because Python does not allow the size of a dictionary to be modified during iteration. This restriction ensures the consistency of the loop operation.

## Example of Error-Prone Code

Here is an example that tries to remove items with even values from a dictionary, which will trigger the error.

```python
numbers = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# This code will raise a RuntimeError
for key, value in numbers.items():
    if value % 2 == 0:
        del numbers[key]

print(numbers)
```

When you run this code, the `del numbers[key]` statement changes the size of the `numbers` dictionary inside the `for` loop, causing the `RuntimeError`.

## How to Fix It

There are several ways to solve this issue. The key is to iterate over a copy of the dictionary instead of modifying the original one directly.

### 1. Use a Copy of the Dictionary

The simplest solution is to iterate over a shallow copy of the dictionary, which you can create using the `.copy()` method. This allows you to safely modify the original dictionary.

```python
numbers = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Iterate over a copy of the dictionary
for key, value in numbers.copy().items():
    if value % 2 == 0:
        del numbers[key] # Delete the item from the original dictionary

print(numbers)
# Output: {'a': 1, 'c': 3}
```

### 2. Iterate Over a List of Keys

Another approach is to create a list of the dictionary's keys before the loop starts. You can then iterate over this static list to modify the dictionary.

```python
numbers = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Create a list of keys to iterate over
for key in list(numbers.keys()):
    if numbers[key] % 2 == 0:
        del numbers[key]

print(numbers)
# Output: {'a': 1, 'c': 3}
```

### 3. Create a New Dictionary (Dictionary Comprehension)

Instead of modifying the existing dictionary, a cleaner and often safer approach is to create a new dictionary containing only the items you want to keep. **Dictionary comprehension** is a concise way to achieve this.

```python
numbers = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Create a new dictionary with only the desired items
filtered_numbers = {key: value for key, value in numbers.items() if value % 2 != 0}

print(filtered_numbers)
# Output: {'a': 1, 'c': 3}
```

This method is highly readable and avoids mutating the data you are iterating over, which is generally a good practice.

## Conclusion

The `RuntimeError: dictionary changed size during iteration` is triggered when you modify a dictionary while looping through it. To resolve this, remember these three techniques:

1.  Iterate over a copy using `.copy()`.
2.  Iterate over a list of keys using `list(dictionary.keys())`.
3.  Create a new dictionary with the desired items instead of modifying the original.

In most cases, using a **dictionary comprehension** is the recommended approach because it is both concise and safe.
