---
typora-root-url: ../
layout: single
title: >
   How to Fix Python NotADirectoryError: [Errno 20] Not a directory
date: 2025-08-05T10:15:00+09:00
header:
   teaser: /images/header_images/overlay_image_python.png
   overlay_image: /images/header_images/overlay_image_python.png
   overlay_filter: 0.5
excerpt: >
   Understand and fix the NotADirectoryError: [Errno 20] Not a directory in Python. This error appears when a file path is used where a directory path is expected. Learn to validate paths and avoid this common issue.
categories:
   - en_Troubleshooting
tags:
   - Python
   - NotADirectoryError
   - File System
   - OSError
   - Troubleshooting
---

## Introduction

The `NotADirectoryError: [Errno 20] Not a directory` is an `OSError` subclass that occurs when you try to use a file path in a context where a directory path is expected. This is the logical opposite of the `IsADirectoryError`. For example, trying to list the contents of a file as if it were a directory will trigger this error.

This guide will explain the common causes of `NotADirectoryError` and show you how to fix it by properly handling file and directory paths.

## What Causes `NotADirectoryError`?

The error is raised when a function that requires a directory path receives a file path instead. The most common functions that can cause this are:

1.  **`os.listdir(path)`**: This function lists the files and directories inside the given `path`. If `path` points to a file, it raises `NotADirectoryError`.
2.  **`os.path.join(path, ...)`**: If a component of the `path` before the last part is a file, it can lead to this error.
3.  **`os.makedirs(path)`**: If you try to create a directory where one of the parent path components is a file.

Here is a simple example:

```python
import os

# Assume 'my_file.txt' is a regular file, not a directory
file_path = 'my_file.txt'

try:
    # This will raise NotADirectoryError because listdir() expects a directory
    contents = os.listdir(file_path) 
except NotADirectoryError as e:
    print(f"Error: {e}")

# Output: Error: [Errno 20] Not a directory: 'my_file.txt'
```

## How to Fix the Error

Resolving this error involves ensuring that any path passed to a directory-level function is, in fact, a directory.

### 1. Validate the Path Before Use

Before calling a function like `os.listdir()`, you should verify that the path is a directory. The `os.path.isdir()` function is perfect for this.

```python
import os

path_to_check = 'my_file.txt' # This is a file

if os.path.isdir(path_to_check):
    print(f"Listing contents of '{path_to_check}':")
    contents = os.listdir(path_to_check)
    print(contents)
elif os.path.isfile(path_to_check):
    print(f"Error: '{path_to_check}' is a file, not a directory. Cannot list contents.")
else:
    print(f"Error: Path '{path_to_check}' does not exist.")
```
This preventative check helps you avoid the error and handle the situation gracefully.

### 2. Use `os.path.dirname()` to Get the Directory Path

If you have a file path and need to work with its containing directory, use `os.path.dirname()` to extract the directory portion of the path.

**Incorrect Code:**
```python
import os

file_path = '/home/user/project/main.py'

# This is wrong, as you are trying to list the contents of a file
# contents = os.listdir(file_path) 
```

**Correct Code:**
```python
import os

file_path = '/home/user/project/main.py'
dir_path = os.path.dirname(file_path) # Extracts '/home/user/project'

print(f"The directory is: {dir_path}")

if os.path.isdir(dir_path):
    print(f"Contents of the directory:")
    contents = os.listdir(dir_path)
    print(contents)
```
This is a common pattern when you need to find other files in the same directory as a given script or file.

### 3. Check Path Components in `os.path.join()`

When constructing paths with `os.path.join()`, make sure that the base path you are joining with is a directory.

```python
import os

# This is incorrect because the base is a file
base_path = 'config.ini' 
new_path = os.path.join(base_path, 'new_folder') 

# An operation on new_path might fail, e.g., os.makedirs(new_path)
try:
    os.makedirs(new_path)
except NotADirectoryError as e:
    print(f"Error creating directory: {e}")
    # Output: Error creating directory: [Errno 20] Not a directory: 'config.ini\new_folder'
```
Always ensure that the initial parts of a path you are building or accessing are directories.

## Practical Example: Safely Listing Directory Contents

Here is a robust function that safely lists the contents of a path, handling potential errors.

```python
import os

def safe_list_dir(path):
    """
    Safely lists the contents of a directory.
    Returns a list of contents or None if an error occurs.
    """
    if not os.path.exists(path):
        print(f"Error: Path '{path}' does not exist.")
        return None
    
    if not os.path.isdir(path):
        print(f"Error: Path '{path}' is not a directory.")
        return None
        
try:
        return os.listdir(path)
    except OSError as e:
        print(f"An OS error occurred: {e}")
        return None

# --- Usage ---
# 1. With a valid directory
dir_contents = safe_list_dir('.')
if dir_contents is not None:
    print("Directory contents:", dir_contents)

print("-" * 20)

# 2. With a file path
file_contents = safe_list_dir('my_file.txt') # Assuming my_file.txt exists
if file_contents is None:
    print("Function handled the file path correctly.")
```

## Conclusion

The `NotADirectoryError` is a clear indication of a logical error in path handling. It serves as a reminder to be deliberate about whether you are working with a file or a directory. By using validation functions like `os.path.isdir()` and path manipulation tools like `os.path.dirname()`, you can prevent this error and create more reliable and predictable file system interactions in your Python scripts.
