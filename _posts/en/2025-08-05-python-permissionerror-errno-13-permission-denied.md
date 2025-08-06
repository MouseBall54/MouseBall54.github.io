---
typora-root-url: ../
layout: single
title: >
   How to Fix Python PermissionError: [Errno 13] Permission denied

lang: en
translation_id: python-permissionerror-errno-13-permission-denied
header:
   teaser: /images/header_images/overlay_image_python.png
   overlay_image: /images/header_images/overlay_image_python.png
   overlay_filter: 0.5
excerpt: >
   Resolve the PermissionError: [Errno 13] Permission denied in Python by learning how to manage file permissions correctly. This guide explains the causes and provides solutions for Windows, macOS, and Linux.
categories:
   - en_Troubleshooting
tags:
   - Python
   - PermissionError
   - File Permissions
   - OSError
   - Troubleshooting
---

## Introduction

The `PermissionError: [Errno 13] Permission denied` is a common error in Python that occurs when your script tries to access a file or directory without the necessary permissions. This can happen when reading, writing, or executing a file. Understanding the root cause is key to resolving it efficiently.

This guide will explain why this error occurs and provide clear, actionable steps to fix it on different operating systems.

## What Causes `PermissionError: [Errno 13] Permission denied`?

This error is almost always related to the file system permissions of the user running the Python script. Here are the most common scenarios:

1.  **Reading a Protected File**: Your script is trying to read a file that it does not have read permissions for.
2.  **Writing to a Protected File or Directory**: Your script is attempting to write to a file or create a new file in a directory where it lacks write permissions.
3.  **Executing a File Without Execute Permissions**: Your script is trying to run an executable file but does not have execute permissions.
4.  **Accessing a Directory Instead of a File**: Sometimes, you might accidentally try to open a directory for reading or writing as if it were a file, which can also lead to a permission error.
5.  **File is in Use**: On Windows, if another process has locked the file, you may get a `PermissionError`.

## How to Fix the Error

The solution depends on what your script is trying to do and the operating system you are using.

### 1. Check File/Directory Permissions

First, identify the file or directory causing the issue and check its permissions.

-   **On Linux or macOS**: Use the `ls -l` command in the terminal to view permissions.

```bash
ls -l /path/to/your/file.txt
# Output might look like: -rw-r--r-- 1 owner group ... file.txt
```

The output shows permissions for the owner, group, and others. `r` stands for read, `w` for write, and `x` for execute.

-   **On Windows**: Right-click the file or directory, go to **Properties**, and then select the **Security** tab. Here you can see the permissions for different users and groups.

### 2. Change File/Directory Permissions

If the permissions are incorrect, you need to change them. You might need administrator/root privileges to do this.

-   **On Linux or macOS**: Use the `chmod` command to grant the necessary permissions.

```bash
# Grant read and write permissions to the owner
chmod u+rw /path/to/your/file.txt

# Grant execute permission
chmod +x /path/to/your/script.sh

# To change permissions for a directory and its contents recursively
chmod -R u+rw /path/to/your/directory
```

-   **On Windows**: In the **Security** tab of the file's properties, click **Edit...** to change permissions. Select the user running the script and check the boxes for "Read", "Write", or "Full control" as needed.

### 3. Run the Script with Sufficient Privileges

If you cannot change the file permissions, you might need to run your script as a user who has the required permissions.

-   **On Linux or macOS**: Use `sudo` to run the script with root privileges. **Use this with caution**, as it can have unintended consequences if the script is not well-tested.

```bash
sudo python your_script.py
```

-   **On Windows**: Right-click your command prompt or IDE and select **"Run as administrator"**. This will give your script elevated permissions.

### 4. Ensure the Path is Correct

Make sure your script is targeting a file and not a directory when performing file operations like `open()`.

**Incorrect Code:**
```python
# This will raise an error if '/path/to/data' is a directory
with open('/path/to/data', 'w') as f:
    f.write('hello')
```

**Correct Approach:**
```python
import os

file_path = '/path/to/data/file.txt'
dir_path = os.path.dirname(file_path)

# Ensure the directory exists
if not os.path.exists(dir_path):
    os.makedirs(dir_path)

# Now, open the file for writing
with open(file_path, 'w') as f:
    f.write('hello')
```
The `os.path.isdir()` function can be used to check if a path points to a directory.

### 5. Close Other Programs Using the File (Windows)

On Windows, if a file is opened by another program (like a text editor or spreadsheet software), it may be locked, preventing your Python script from accessing it. Close any other applications that might be using the file and try running your script again.

## Conclusion

The `PermissionError: [Errno 13] Permission denied` is a straightforward issue that can be resolved by managing file system permissions. By checking who is running the script and what permissions they have for the target file or directory, you can quickly diagnose the problem. Always ensure your script has the necessary rights to perform the intended operations, and be cautious when running scripts with elevated privileges.
