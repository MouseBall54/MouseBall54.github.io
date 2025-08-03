---
typora-root-url: ../
layout: single
title: >
    How to Fix Python's "UnicodeDecodeError: 'utf-8' codec can't decode byte"
date: 2025-08-03T11:00:00+09:00
header:
   teaser: /images/header_images/overlay_image_python.png
   overlay_image: /images/header_images/overlay_image_python.png
   overlay_filter: 0.5
excerpt: >
    Resolve the "UnicodeDecodeError" in Python. This error occurs when reading a file with an encoding that doesn't match the default 'utf-8' codec.
categories:
  - en_Troubleshooting
tags:
  - Python
  - UnicodeDecodeError
  - Encoding
  - File I/O
---

## What is UnicodeDecodeError?

A `UnicodeDecodeError` happens in Python.
It occurs when you try to read a file.
The file's encoding does not match the expected format.
Python 3 defaults to 'utf-8' for decoding text.
If a file is saved with a different encoding, this error appears.
The message "'utf-8' codec can't decode byte..." is shown.
It means a specific byte in the file is not valid 'utf-8'.

## Common Causes and Solutions

This error usually has one primary cause. The file encoding is wrong.

### 1. Reading a File with a Different Encoding

A file might be saved in an encoding like 'cp949', 'euc-kr', or 'latin-1'.
When Python tries to read it as 'utf-8', the error occurs.

**Problematic Code:**
```python
# This code assumes the file 'my_data.csv' is utf-8 encoded.
# If it's not, it will raise a UnicodeDecodeError.
with open('my_data.csv', 'r') as f:
    content = f.read()
print(content)
```

**Solution:**
You must specify the correct encoding.
Use the `encoding` parameter in the `open()` function.

First, you need to find the file's actual encoding.
You can use a text editor like Notepad++ or VS Code to check it.
Alternatively, you can use Python's `chardet` library.

```bash
pip install chardet
```

Once you know the encoding, apply it.
Let's assume the file encoding is 'cp949'.

**Corrected Code:**
```python
# Specify the correct encoding, for example 'cp949'.
try:
    with open('my_data.csv', 'r', encoding='cp949') as f:
        content = f.read()
    print(content)
except FileNotFoundError:
    print("File not found.")
except UnicodeDecodeError:
    print("The file is not encoded in cp949.")
```

### 2. Handling Potential Encoding Errors

Sometimes, you cannot be sure of the encoding.
Or, a file might contain a few invalid characters.
In these cases, you can use the `errors` parameter.

**Code with Error Handling:**
```python
# The 'errors' parameter tells Python how to handle encoding errors.
# 'ignore': skips the problematic characters.
# 'replace': replaces problematic characters with a placeholder (e.g., '?').

with open('my_data.csv', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()
print(content)
```
This approach prevents the program from crashing.
However, it might cause some data loss or corruption.
Use it only when perfect data integrity is not critical.

## Best Practices

- **Always specify encoding.** Never rely on the default. `open('file.txt', 'r', encoding='utf-8')` is best practice.
- **Save files as 'utf-8'.** When writing files, use 'utf-8'. It is the most widely supported standard.
- **Know your data.** Understand the source of your files and their likely encoding.

By explicitly managing file encodings, you can prevent `UnicodeDecodeError`. This makes your code more robust and reliable.
