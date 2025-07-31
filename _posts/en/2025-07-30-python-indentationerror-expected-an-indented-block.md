---
typora-root-url: ../
layout: single
title: "How to Fix Python's IndentationError: expected an indented block"
date: 2025-07-30T11:00:00+09:00
excerpt: "Master Python's core syntax: indentation! Understand the causes of and solutions for IndentationError, fix mixed tabs and spaces, and learn to write clean, error-free code."
header:
   teaser: /images/header_images/overlay_image_python.png
   overlay_image: /images/header_images/overlay_image_python.png
   overlay_filter: 0.5
categories:
  - en_Troubleshooting
tags:
  - Python
  - IndentationError
  - Programming
  - Beginner
---

## What is Python's `IndentationError: expected an indented block`?

Unlike many other programming languages that use braces `{}` to define code structure, Python uses **indentation**. The `IndentationError: expected an indented block` is a very Python-specific error that occurs when these indentation rules are not followed.

This error typically appears when a required indentation is missing from a code block or when the indentation style is inconsistent.

### 1. Missing Indentation in a Code Block

This is the most common cause. Statements that initiate a new code block, such as `if`, `for`, `def`, and `class`, must be followed by indented code.

**Incorrect Code:**
```python
def my_function():
print("This line is not indented.") # Requires indentation inside the def block
```

**Corrected Code:**
```python
def my_function():
    print("This line is now indented.")
```
In Python, the standard is to use **four spaces** for one level of indentation. Indenting the `print` function after the `def` statement resolves the error.

### 2. Unnecessary Indentation

Conversely, adding indentation where it isn't needed can also cause an `IndentationError` (specifically, an `unexpected indent` error).

**Incorrect Code:**
```python
x = 10
    print(x) # Unnecessary indentation
```

**Corrected Code:**
```python
x = 10
print(x)
```
Top-level code should always start at the far left, with no preceding spaces.

### 3. Mixing Tabs and Spaces

This is a tricky cause of `IndentationError` because it's often invisible. Python treats tabs and spaces as different characters. If you indent one line with a tab and another with spaces, the interpreter sees them as different indentation levels and raises an error.

**Potentially Incorrect Code (Visually Indistinguishable):**
```python
if True:
	print("This line is indented with a tab.")
    print("This line is indented with spaces.") # -> Raises IndentationError
```

**Solution:**

The best way to solve this is to configure your code editor to **automatically convert tabs to spaces**.

-   **Visual Studio Code**: In your `settings.json`, add the settings `"editor.insertSpaces": true` and `"editor.tabSize": 4`.
-   **PyCharm**: Go to `Settings > Editor > Code Style > Python`, uncheck `Use tab character`, and set `Indent` to 4.

To fix existing code, use your editor's feature to **"Convert Indentation to Spaces"**.

### Conclusion

`IndentationError` highlights the importance of indentation, which is fundamental to Python's syntax. To avoid this error, it's crucial to remember these rules:

1.  **Be Consistent**: Stick to one indentation style throughout your project (four spaces is the recommended standard).
2.  **Configure Your Editor**: Set up your editor to insert four spaces when you press the Tab key.
3.  **Check Your Blocks**: Always ensure that lines ending with a colon (`:`)—like `if`, `for`, and `def`—are followed by an indented code block.

Adopting proper indentation habits not only prevents `IndentationError` but is also the first step toward writing clean, readable code.
