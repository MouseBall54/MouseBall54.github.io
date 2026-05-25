---
typora-root-url: ../
layout: single
title: >
    How to Fix "OSError: [Errno 28] No space left on device" in Python

date: 2025-03-20T07:38:00+09:00
lang: en
translation_id: python-os-error-no-space-left
header:
    teaser: /images/header_images/overlay_image_python.png
    overlay_image: /images/header_images/overlay_image_python.png
    overlay_filter: 0.5
    image_description: >
      A visual summary explaining the main topic of this post: How to Fix "OSError: [Errno 28] No space left on device" in Python
excerpt: >
    In Python, "OSError: [Errno 28] No space left on device" occurs when there is insufficient disk space. This article explains the causes of the error and how to fix it.
seo_description: >
    In Python, "OSError: [Errno 28] No space left on device" occurs when there is insufficient disk space. This article explains the causes of the error and how to fix it.
categories:
    - en_Troubleshooting
tags:
    - Python
    - OSError
    - Disk Space
---


![A visual summary explaining the main topic of this post: How to Fix "OSError: Errno 28 No space left on device" in Python](/images/header_images/overlay_image_python.png)
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

## Professional Depth Check

For **How to Fix "OSError: [Errno 28] No space left on device" in Python**, the practical standard is not whether the reader can repeat one instruction once. Treat the topic as a reproducible debugging procedure: verify runtime environment, exact error boundary, minimal reproduction, and rollback path before drawing a conclusion. The result should be written as a small decision record, because future readers need to know which fact was observed, which assumption was used, and which condition would change the answer.

### Evidence That Makes the Guidance Reliable

Use objective evidence before changing a workflow. Good evidence includes full command output, version numbers, changed files, and expected versus actual behavior. If two pieces of evidence conflict, keep the conflict visible instead of smoothing it over. For example, a successful quick fix is still weak evidence if the same input, account, dependency, or device state has not been tested again. A durable article should help the reader distinguish a confirmed fix from a plausible fix.

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

## Related Reading

Continue with these related posts from the same topic area.

- [How to Fix "SSL: CERTIFICATE_VERIFY_FAILED" Error in Python on Windows](/en_troubleshooting/python-certificate-verify-failed/)
- [How to Fix "Permission denied (publickey)" Error with Git on Windows](/en_troubleshooting/git-permission-denied-publickey-windows/)
