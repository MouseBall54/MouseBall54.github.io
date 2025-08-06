---
typora-root-url: ../
layout: single
title: "How to Fix Python TypeError: can only concatenate str (not 'int') to str"

lang: en
translation_id: python-typeerror-can-only-concatenate-str-not-int-to-str
excerpt: "The 'TypeError: can only concatenate str (not 'int') to str' in Python occurs when you try to concatenate a string with a non-string type, like an integer. This article explains the cause and how to fix it."
header:
   teaser: /images/header_images/overlay_image_python.png
   overlay_image: /images/header_images/overlay_image_python.png
   overlay_filter: 0.5
categories:
  - en_Troubleshooting
tags:
  - Python
  - TypeError
  - Troubleshooting
  - String
---

## What is the 'TypeError: can only concatenate str (not "int") to str' Error?

This `TypeError` is a very common error in Python that occurs when you try to concatenate a string with a non-string data type (e.g., an integer, a list) using the `+` operator.
Python performs strong type checking, so it does not allow implicit concatenation of different types.
The error message clearly states, "You can only concatenate a string with another string (not an 'integer' type)."

## Main Cause

The cause of this error is singular: attempting to directly append a variable or value of a different type to a string using the `+` operator.

```python
name = "User"
age = 25

# Error: Directly concatenating a string (str) and an integer (int)
message = "Hello, " + name + ". Your age is " + age + "."
# TypeError: can only concatenate str (not "int") to str
```

In the code above, the `age` variable is an integer (`int`) type.
Python cannot directly add the integer `25` to the string `"Hello, User. Your age is "`, so it raises a `TypeError`.

## How to Fix It

There are several simple and effective ways to solve this problem.

### 1. Explicit Type Conversion with `str()`

The most basic solution is to explicitly convert the non-string data to a string using the `str()` function.

```python
name = "User"
age = 25

# Convert the integer age to a string using str()
message = "Hello, " + name + ". Your age is " + str(age) + "."
print(message)
# Output: Hello, User. Your age is 25.
```

`str(age)` converts the integer `25` to the string `"25"`, so all elements become strings and can be concatenated correctly.

### 2. Using f-strings (Formatted String Literals)

If you are using Python 3.6 or higher, f-strings are the most modern and recommended method.
By prefixing the string with an `f` and placing variables directly inside curly braces `{}`, they are automatically converted to strings, which is very convenient.

```python
name = "User"
age = 25

# Conc cisely format the string using an f-string
message = f"Hello, {name}. Your age is {age}."
print(message)
# Output: Hello, {name}. Your age is {age}.
```

The code becomes much more concise and readable.

### 3. Using the `str.format()` Method

Before the introduction of f-strings, the `str.format()` method was commonly used.
This method involves placing `{}` placeholders in the string and passing the variables as arguments to the `.format()` method.

```python
name = "User"
age = 25

# Using the str.format() method
message = "Hello, {}. Your age is {}.".format(name, age)
print(message)
# Output: Hello, User. Your age is 25.
```

### 4. Using a Comma in the `print` Function

If the goal is simply to print multiple values to the console, you can pass them separated by commas in the `print` function.
The `print` function automatically separates each argument with a space and prints them.

```python
name = "User"
age = 25

# Using a comma in the print function automatically converts each type to a string for output
print("Hello,", name, ". Your age is", age, ".")
# Output: Hello, User . Your age is 25 .
```

However, this method is useful only for printing multiple values, not for creating a single string that includes the variables.

## Conclusion

`TypeError: can only concatenate str (not "int") to str` occurs when you try to concatenate non-string data without converting it to a string.
To solve this problem, it is best to either directly convert the type with the `str()` function or use string formatting features like f-strings or `str.format()`.
F-strings, in particular, are the most concise and efficient method in modern Python, so it is highly recommended to use them actively.

```