---
typora-root-url: ../
layout: single
title: "How to Fix Python's NameError: name '...' is not defined"
date: 2025-07-30T22:00:00+09:00
excerpt: "Understand and fix the Python NameError, which occurs when a variable or function is used before it's defined. Learn common causes like typos and scope issues."
header:
   teaser: /images/header_images/overlay_image_python.png
   overlay_image: /images/header_images/overlay_image_python.png
   overlay_filter: 0.3
categories:
  - en_Troubleshooting
tags:
  - Python
  - NameError
  - Programming
  - Error Handling
---

## What is `NameError: name '...' is not defined`?

This error occurs when the Python interpreter encounters a name (variable, function, class) that it doesn't recognize.
Essentially, you are trying to use something that hasn't been created or assigned a value yet.
It is one of the most common errors for beginners.

## Common Causes and Solutions

Let's look at the typical reasons why you might see a `NameError` and how to resolve them.

### 1. Misspelling a Variable or Function Name

A simple typo is the most frequent cause. Python is case-sensitive, so `myVariable` is different from `myvariable`.

**Error Example:**
```python
message = "Hello, World!"
print(mesage)
```

**Output:**
```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'mesage' is not defined
```

**Solution:**
Correct the typo. Ensure the name used matches the name at declaration.

```python
message = "Hello, World!"
print(message) # Corrected from 'mesage'
```

### 2. Using a Variable Before Assignment

You must assign a value to a variable before you can use it.

**Error Example:**
```python
if some_condition:
    user_name = "Alice"

print(user_name) # NameError if some_condition is False
```

**Solution:**
Initialize the variable with a default value before the conditional block.

```python
user_name = "Guest" # Initialize with a default value
if some_condition:
    user_name = "Alice"

print(user_name)
```

### 3. Variable Scope Issues

A variable defined inside a function (a local variable) cannot be accessed from outside that function.

**Error Example:**
```python
def greet():
    greeting = "Hello from inside the function!"
    print(greeting)

greet()
print(greeting) # This will cause a NameError
```

**Output:**
```
Hello from inside the function!
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'greeting' is not defined
```

**Solution:**
If you need to use the value outside, `return` it from the function and assign it to a new variable.

```python
def greet():
    greeting = "Hello from inside the function!"
    return greeting

returned_greeting = greet()
print(returned_greeting)
```

### 4. Forgetting to Import a Module or Name

When using modules from the standard library or third-party packages, you must import them first.

**Error Example:**
```python
# Forgetting to import the 'math' module
print(math.sqrt(25))
```

**Output:**
```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'math' is not defined
```

**Solution:**
Add the required `import` statement at the top of your script.

```python
import math

print(math.sqrt(25))
```

By checking for these common mistakes, you can quickly identify and fix most `NameError` exceptions in your Python code.
