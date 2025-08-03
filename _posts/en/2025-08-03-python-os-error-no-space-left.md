---
typora-root-url: ../
layout: single
title: >
    How to Fix "OSError: [Errno 28] No space left on device" in Python
date: 2025-08-03T14:10:00+09:00
header:
    teaser: /images/header_images/overlay_image_python.png
    overlay_image: /images/header_images/overlay_image_python.png
    overlay_filter: 0.5
excerpt: >
    In Python, "OSError: [Errno 28] No space left on device" occurs when there is insufficient disk space. This article explains the causes of the error and how to fix it.
categories:
    - en_Troubleshooting
tags:
    - Python
    - OSError
    - Disk Space
---

## What is "OSError: [Errno 28] No space left on device" in Python?

`OSError: [Errno 28] No space left on device` is an operating system-level error that occurs when your Python program tries to write to a file but cannot because the disk is full. This error is not limited to file-writing operations; it can also be triggered by libraries or processes that create temporary files.

## Common Causes of "No space left on device"

1.  **Insufficient Disk Space**: The most obvious cause is that the hard drive or partition has run out of storage.
2.  **Inode Exhaustion**: (Linux/macOS) Even if there is disk space available, this error can occur if the file system has run out of inodes, which are metadata structures for files and directories. This is common when there are a very large number of small files.
3.  **Excessive Temporary Files**: If a program does not terminate correctly or lacks proper error handling, temporary files may not be deleted and can accumulate over time.
4.  **Large Log Files**: Improperly configured logging can generate massive log files that consume all available disk space.

## How to Fix "No space left on device"

### 1. Check and Free Up Disk Space

The first step is to check your system's disk usage.

*   **Linux/macOS**:
    ```bash
    df -h
    ```
    This command shows the usage, available space, and use percentage for each partition. If a partition is full, you need to free up space by deleting unnecessary files. The `du` command can help you find which directories are taking up the most space.
    ```bash
    du -sh /path/to/directory
    ```

*   **Windows**: Check the properties of each drive in File Explorer to inspect disk space and use the Disk Cleanup utility to remove unnecessary files.

### 2. Check Inode Usage (Linux/macOS)

If you have enough disk space but still get the error, you might be out of inodes.

```bash
df -i
```
If `IUse%` is near 100%, you have exhausted your inodes. In this case, you need to find and delete a large number of small files (e.g., session files, cache files).

### 3. Clean Up Temporary Files and Caches

Ensure that temporary files and caches created by your program are properly managed. When using the `tempfile` module, a `with` statement ensures that the file is automatically cleaned up when the block is exited.

```python
import tempfile

with tempfile.NamedTemporaryFile(mode='w+', delete=True) as temp_file:
    # With delete=True (default), the file is automatically deleted when closed.
    temp_file.write('Hello, world!')
    temp_file.seek(0)
    # File processing logic
```

### 4. Manage Log Files

When using the `logging` module, prevent log files from growing indefinitely. Use `RotatingFileHandler` or `TimedRotatingFileHandler` to split logs into multiple files based on size or time and automatically delete old logs.

```python
import logging
from logging.handlers import RotatingFileHandler

log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

# Keep up to 5 log files, each 10MB in size
handler = RotatingFileHandler('app.log', maxBytes=10*1024*1024, backupCount=5)
handler.setFormatter(log_formatter)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(handler)

logger.info('This is a test log message.')
```

## Conclusion

`OSError: [Errno 28] No space left on device` is typically an environment issue rather than a code problem. It is important to periodically monitor disk space and inode usage and to ensure your program cleans up after itself. Managing log files and temporary files is especially critical for long-running applications.

---
*Work History*
- *2025-08-03: Initial draft created*
