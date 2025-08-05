---
typora-root-url: ../
layout: single
title: >
   How to Fix Python TypeError: unsupported operand type(s) for +
date: 2025-08-05T10:20:00+09:00
header:
   teaser: /images/header_images/overlay_image_python.png
   overlay_image: /images/header_images/overlay_image_python.png
   overlay_filter: 0.5
excerpt: >
   Fix the TypeError: unsupported operand type(s) for + in Python by ensuring you are using compatible types in your operations. This guide explains how to handle type conversions for numbers, strings, and other objects.
categories:
   - en_Troubleshooting
tags:
   - Python
   - TypeError
   - Data Types
   - Operators
   - Troubleshooting
---

## Introduction

The `TypeError: unsupported operand type(s) for +: '...' and '...'` is one of the most common errors new Python programmers encounter. It occurs when you try to use the addition operator (`+`) on two objects of incompatible types. For example, you cannot directly add a number to a string or a list to a dictionary.

This guide will explain why this `TypeError` happens and provide clear solutions for handling different data types correctly.

## What Causes This `TypeError`?

Python is a strongly typed language, which means it doesn't automatically convert data types in most operations. The `+` operator behaves differently depending on the types of its operands:

-   For **numbers** (int, float), it performs mathematical addition.
-   For **strings**, it performs concatenation.
-   For **lists**, it performs concatenation.
-   For **tuples**, it performs concatenation.

The error arises when you mix types that don't have a defined behavior for the `+` operator.

**Common examples that raise the error:**

1.  **Adding a string and an integer:**
    ```python
    age = 25
    message = "My age is " + age # Raises TypeError
    # TypeError: can only concatenate str (not "int") to str
    ```

2.  **Adding a list and a string:**
    ```python
    my_list = [1, 2, 3]
    my_string = "456"
    result = my_list + my_string # Raises TypeError
    # TypeError: can only concatenate list (not "str") to list
    ```

3.  **Adding a dictionary and a list:**
    ```python
    my_dict = {'a': 1}
    my_list = ['b', 2]
    result = my_dict + my_list # Raises TypeError
    # TypeError: unsupported operand type(s) for +: 'dict' and 'list'
    ```

## How to Fix the Error

The solution is always to ensure that the operands are of a compatible type before using the `+` operator. This usually involves explicit type conversion.

### 1. Converting to String for Concatenation

When you want to combine a string with a number or another object for display purposes, convert the non-string object to a string using `str()`.

**Incorrect:**
```python
age = 25
message = "I am " + age + " years old."
```

**Correct:**
```python
age = 25
# Convert the integer 'age' to a string
message = "I am " + str(age) + " years old."
print(message) # Output: I am 25 years old.
```

A more modern and readable way to format strings is using **f-strings** (formatted string literals), which automatically handle the conversion.

**Best Practice (f-strings):**
```python
age = 25
message = f"I am {age} years old."
print(message) # Output: I am 25 years old.
```

### 2. Converting to Numbers for Addition

If you receive numeric data as strings (e.g., from user input or a file), you must convert them to a numeric type (`int` or `float`) before performing arithmetic.

**Incorrect:**
```python
num1_str = "10"
num2_int = 20
result = num1_str + num2_int # Raises TypeError
```

**Correct:**
```python
num1_str = "10"
num2_int = 20
# Convert the string 'num1_str' to an integer
result = int(num1_str) + num2_int
print(result) # Output: 30
```

Be sure to handle potential `ValueError` if the string is not a valid number.
```python
num_str = "hello"
try:
    num_int = int(num_str)
except ValueError:
    print(f"'{num_str}' cannot be converted to an integer.")
```

### 3. Handling Other Data Types

When working with other data types like lists or dictionaries, you need to think about what "addition" means in your context.

-   **Adding an item to a list**: Use the `append()` method or list concatenation with another list.

    ```python
    my_list = [1, 2, 3]
    item_to_add = 4
    
    # To add a single item
    my_list.append(item_to_add)
    print(my_list) # Output: [1, 2, 3, 4]
    
    # To concatenate with another list
    another_list = [5, 6]
    combined_list = my_list + another_list
    print(combined_list) # Output: [1, 2, 3, 4, 5, 6]
    ```

-   **"Adding" to a dictionary**: This usually means updating it with new key-value pairs. Use the `update()` method or direct assignment.

    ```python
    my_dict = {'a': 1}
    
    # Add a new key-value pair
    my_dict['b'] = 2
    
    # Update with another dictionary
    another_dict = {'c': 3, 'd': 4}
    my_dict.update(another_dict)
    
    print(my_dict) # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    ```

## Conclusion

The `TypeError: unsupported operand type(s) for +` is a fundamental error in Python that highlights the importance of data types. To fix it, you must perform explicit type conversion to ensure that you are only using the `+` operator on compatible types. Use `str()` for string concatenation, `int()` or `float()` for mathematical addition, and appropriate methods like `append()` or `update()` for other data structures. Adopting f-strings for string formatting will also help you write cleaner and more error-free code.
