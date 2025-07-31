---
typora-root-url: ../
layout: single
title: "How to Fix Python's UnboundLocalError: local variable referenced before assignment"
date: 2025-07-31T14:30:00+09:00
excerpt: "Resolve Python's UnboundLocalError by understanding variable scope. Learn to use the `global` and `nonlocal` keywords or ensure a variable is always assigned a value within a function's scope before it is accessed."
header:
   teaser: /images/header_images/overlay_image_python.png
   overlay_image: /images/header_images/overlay_image_python.png
   overlay_filter: 0.3
categories:
  - en_Troubleshooting
tags:
  - Python
  - UnboundLocalError
  - Scope
  - Exception Handling
---

## What is "UnboundLocalError: local variable '...' referenced before assignment"?

`UnboundLocalError` is a specific type of `NameError` in Python. It occurs when you try to access a local variable within a function or method before a value has been assigned to it *within that same function or method*.

This error can be confusing because you might have a global variable with the same name. However, if you *assign* a value to a variable anywhere inside a function, Python treats that variable as local to that function for its entire scope.

## Common Causes and Solutions

Let's explore the scenarios that lead to this error.

### 1. Modifying a Global Variable Inside a Function

The most common cause is trying to modify a global variable without explicitly telling Python that you intend to do so.

#### Problematic Code

```python
count = 0

def increment():
    # Python sees this assignment and assumes 'count' is a local variable.
    count = count + 1
    print(count)

# This will raise an UnboundLocalError
increment()
```

When Python compiles the `increment` function, it sees the assignment `count = ...`. This tells Python that `count` is a local variable. However, when the function executes, it tries to read the value of `count` from the right side of the expression (`count + 1`) *before* a value has been assigned to the local `count`. The global `count` is ignored, leading to the error.

#### Solution: Use the `global` Keyword

To modify a global variable from within a function, you must use the `global` keyword to declare your intent.

```python
count = 0

def increment():
    global count # Tell Python we are using the global 'count'
    count = count + 1
    print(count)

increment() # Output: 1
print(f"Global count is now: {count}") # Output: Global count is now: 1
```

### 2. Variable Assignment is Conditional

If a variable is only assigned a value inside a conditional block (`if`, `for`, `try`), and that block is never entered, the variable will not exist when you try to access it later in the function.

#### Problematic Code

```python
def get_status_message(status_code):
    if status_code == 200:
        message = "OK"
    
    # If status_code is not 200, 'message' is never assigned.
    return f"Status: {message}"

# This will raise an UnboundLocalError
print(get_status_message(404))
```

When `get_status_message(404)` is called, the `if` condition is false, so the line `message = "OK"` is skipped. The `return` statement then tries to access `message`, which has not been assigned a value in the local scope.

#### Solution: Ensure the Variable is Always Assigned

Make sure the variable is assigned a value in all possible execution paths before it is accessed. A common practice is to initialize it with a default value at the beginning of the function.

```python
def get_status_message(status_code):
    message = "Unknown Status" # Initialize with a default value
    
    if status_code == 200:
        message = "OK"
    elif status_code == 404:
        message = "Not Found"
    
    return f"Status: {message}"

print(get_status_message(404)) # Output: Status: Not Found
print(get_status_message(500)) # Output: Status: Unknown Status
```

### 3. Modifying a Variable in a Nested Function (Closures)

A similar issue arises with nested functions when you try to modify a variable from an enclosing (but not global) scope.

#### Problematic Code

```python
def outer_function():
    value = 10
    
    def inner_function():
        # Python assumes 'value' is local to inner_function due to the assignment.
        value = value + 5
        print(value)
        
    inner_function()

# This will raise an UnboundLocalError
outer_function()
```

#### Solution: Use the `nonlocal` Keyword

The `nonlocal` keyword (introduced in Python 3) tells the interpreter that a variable is from the nearest enclosing scope that is not global.

```python
def outer_function():
    value = 10
    
    def inner_function():
        nonlocal value # Use the 'value' from outer_function
        value = value + 5
        print(f"Inner value: {value}")
        
    inner_function()
    print(f"Outer value: {value}")

outer_function()
# Output:
# Inner value: 15
# Outer value: 15
```

## Conclusion

`UnboundLocalError` is always a sign of a scope-related issue. To fix it, you need to be clear about which variable you are trying to access:
*   If you mean to modify a **global variable**, use the `global` keyword.
*   If you mean to modify a variable in an **enclosing function's scope**, use the `nonlocal` keyword.
*   Otherwise, ensure your **local variable** is assigned a value in all possible code paths before you try to read from it.
