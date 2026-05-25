---
typora-root-url: ../
layout: single
title: >
    How to Fix Python TypeError: missing 1 required positional argument

date: 2025-03-23T07:41:00+09:00
lang: en
translation_id: python-typeerror-missing-required-positional-argument
header:
   teaser: /images/header_images/overlay_image_python.png
   overlay_image: /images/header_images/overlay_image_python.png
   overlay_filter: 0.5
   image_description: >
     A visual summary explaining the main topic of this post: How to Fix Python TypeError: missing 1 required positional argument
excerpt: >
    Learn how to fix the `TypeError: missing 1 required positional argument` in Python, which occurs when you call a function or method without providing a mandatory positional argument.
seo_description: >
    Learn how to fix the `TypeError: missing 1 required positional argument` in Python, which occurs when you call a function or method without providing a mandatory positional argument.
categories:
  - en_Troubleshooting
tags:
  - Python
  - TypeError
  - Argument
  - Function Call
---


![A visual summary explaining the main topic of this post: How to Fix Python TypeError: missing 1 required positional argument](/images/header_images/overlay_image_python.png)
## The Problem

When calling a function or a class method in Python, you might encounter an error like `TypeError: missing 1 required positional argument: '...'`. This error means that the function (or method) was expecting a **required positional argument**, but it was not provided when the function was called.

The last part of the error message, `'...'`, helpfully tells you the name of the missing argument.

## Examples of Error-Prone Code

### 1. Missing Argument in a Simple Function Call

The `greet` function requires one positional argument, `name`, but it was called without any arguments.

```python
def greet(name):
    print(f"Hello, {name}!")

# The 'name' argument was not provided in the function call.
greet() 
# TypeError: greet() missing 1 required positional argument: 'name'
```

### 2. Instance Method Called on the Class

This error is common when dealing with class methods. It usually happens when you try to call an instance method directly on the class, forgetting that the method's first argument must be the instance itself (`self`).

```python
class Calculator:
    # 'self' is a required positional argument referring to the instance.
    def add(self, x, y):
        return x + y

# Calling the method directly on the class, not an instance.
# In this case, no instance is passed as the 'self' argument.
result = Calculator.add(5, 10)
# TypeError: Calculator.add() missing 1 required positional argument: 'self'
```

In Python, `instance.method(arg1, arg2)` is syntactic sugar for `ClassName.method(instance, arg1, arg2)`. When you call the method on the class, the first argument, `self`, is missing.

## How to Fix It

### 1. Provide All Required Arguments

The most straightforward solution is to provide a value for every required argument when you call the function.

```python
def greet(name):
    print(f"Hello, {name}!")

# Pass a value for the 'name' argument.
greet("Alice")
# Output: Hello, Alice!
```

### 2. Set a Default Value for the Argument

If an argument is not always required, you can make it optional by providing a default value in the function definition.

```python
# Set a default value "Guest" for the 'name' argument.
def greet(name="Guest"):
    print(f"Hello, {name}!")

# Calling without an argument now works, as it uses the default value.
greet()
# Output: Hello, Guest!

greet("Bob")
# Output: Hello, Bob!
```

### 3. Call the Method on an Instance of the Class

For errors related to class methods, you must first create an instance of the class and then call the method on that instance.

```python
class Calculator:
    def add(self, x, y):
        return x + y

# 1. Create an instance of the Calculator class.
calc_instance = Calculator()

# 2. Call the method on the instance.
# Python automatically passes 'calc_instance' as the 'self' argument.
result = calc_instance.add(5, 10)

print(result)
# Output: 15
```

If you need a method that can be called directly on the class without an instance, you should define it as a static method using the `@staticmethod` decorator. A static method does not require a `self` argument.

```python
class Calculator:
    @staticmethod
    def add(x, y): # A static method does not have 'self'.
        return x + y

# It can be called directly on the class without creating an instance.
result = Calculator.add(5, 10)
print(result)
# Output: 15
```

## Conclusion

The `TypeError: missing 1 required positional argument` occurs when the basic rules of function calls are not met. To fix it:

1.  Ensure you **pass all required arguments** when calling a function.
2.  If appropriate, **set a default value** for an argument in the function definition to make it optional.
3.  For class methods, **call the method on an instance** of the class, or use **`@staticmethod`** if `self` is not needed.

The error message tells you exactly which argument is missing, so checking the function or method definition should be your first step in debugging.

## Professional Depth Check

For **How to Fix Python TypeError: missing 1 required positional argument**, the practical standard is not whether the reader can repeat one instruction once. Treat the topic as a reproducible debugging procedure: verify interpreter path, virtual environment, package version, and input file or data boundary before drawing a conclusion. The result should be written as a small decision record, because future readers need to know which fact was observed, which assumption was used, and which condition would change the answer.

### Evidence That Makes the Guidance Reliable

Use objective evidence before changing a workflow. Good evidence includes `python --version`, `python -m pip show`, the full traceback, and a minimal script. If two pieces of evidence conflict, keep the conflict visible instead of smoothing it over. For example, a successful quick fix is still weak evidence if the same input, account, dependency, or device state has not been tested again. A durable article should help the reader distinguish a confirmed fix from a plausible fix.

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
