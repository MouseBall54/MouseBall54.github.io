---
typora-root-url: ../
layout: single
title: >
    How to Fix Python TypeError: '...' object is not iterable

lang: en
translation_id: python-typeerror-object-is-not-iterable
header:
   teaser: /images/header_images/overlay_image_python.png
   overlay_image: /images/header_images/overlay_image_python.png
   overlay_filter: 0.5
excerpt: >
    Learn how to fix the `TypeError: '...' object is not iterable` in Python, which occurs when you try to loop over a non-iterable object like an integer or None.
categories:
  - en_Troubleshooting
tags:
  - Python
  - TypeError
  - Iterable
---

## The Problem

In Python, you'll encounter the `TypeError: '...' object is not iterable` when you try to use a non-iterable object in a context that requires iteration, such as a `for` loop or an `in` operator. The `'...'` part of the error message will specify the type of the object, like `int`, `float`, or `NoneType`.

An **iterable** is an object that can return its members one at a time. Examples include lists, tuples, dictionaries, and strings. In contrast, single-value objects like numbers (integers, floats) or `None` are not iterable.

## Examples of Error-Prone Code

### 1. Trying to Iterate Over a Number

A common mistake is trying to use a number directly in a `for` loop.

```python
# This will raise TypeError: 'int' object is not iterable
for i in 123:
    print(i)
```

The integer `123` is a single value, not a collection of items, so it cannot be iterated over.

### 2. Function Returns a Non-Iterable Value

This error also occurs if a function returns a single value (like `None` or a number) when an iterable (like a list) is expected.

```python
def get_data():
    # This function returns None if there's no data
    return None

# The 'data' variable is None, which is not iterable
# This will raise TypeError: 'NoneType' object is not iterable
data = get_data()
for item in data:
    print(item)
```

## How to Fix It

### 1. Check if the Object is Iterable

When debugging, it's crucial to check the value of the variable you are trying to iterate over. Use `print()` or a debugger to inspect it. You might find it's `None` or another single value instead of the list or dictionary you were expecting.

A good practice is to design functions to return an **empty iterable** (e.g., `[]` or `()`) instead of `None` when there are no results.

```python
def get_data(condition):
    if condition:
        return ["apple", "banana"]
    # Return an empty list instead of None
    return []

data = get_data(False)
print(f"Data received: {data}") # Data received: []

# Iterating over an empty list is perfectly fine and won't cause an error.
for item in data:
    print(item)
```

### 2. Wrap a Single Object in a List or Tuple

If you know you might be dealing with a single item but want to use a `for` loop, you can wrap it in a list or tuple to make it iterable.

```python
my_variable = 123

# If my_variable is not a list, make it one
if not isinstance(my_variable, list):
    my_variable = [my_variable]

for item in my_variable:
    print(item)
# Output: 123
```

### 3. Use the `range()` Function for Numbers

If your intention was to iterate over a sequence of numbers, you should use the `range()` function.

```python
# Iterate from 0 to 4
for i in range(5):
    print(i)
# Output: 0, 1, 2, 3, 4
```

## Conclusion

The `TypeError: '...' object is not iterable` arises from attempting to loop over an object that doesn't support iteration. To fix this:

1.  Ensure the variable you are iterating over is an iterable type like a **list, tuple, dictionary, or string**.
2.  Design functions to return an **empty list (`[]`)** or tuple instead of `None` for "no result" cases.
3.  If you need to iterate over a single item, wrap it in a **list (`[item]`)**.
4.  To iterate over a sequence of numbers, use the **`range()`** function.

Always being mindful of your variables' types is key to avoiding this common error.
