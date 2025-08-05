typora-root-url: ../
layout: single
title: >
    How to Handle KeyboardInterrupt in Python
seo_title: >
    How to Handle KeyboardInterrupt in Python
date: 2025-08-05T21:10:00+09:00
header:
   teaser: /images/header_images/overlay_image_python.png
   overlay_image: /images/header_images/overlay_image_python.png
   overlay_filter: 0.5
excerpt: >
    In Python, KeyboardInterrupt is an exception raised when the user presses Ctrl+C to forcefully terminate a program. Handling this exception correctly allows you to shut down your program gracefully and clean up resources. This post explains how to handle KeyboardInterrupt.
seo_description: >
    In Python, KeyboardInterrupt is an exception raised when the user presses Ctrl+C to forcefully terminate a program. Handling this exception correctly allows you to shut down your program gracefully and clean up resources. This post explains how to handle KeyboardInterrupt.
categories:
  - en_Troubleshooting
tags:
  - Python
  - KeyboardInterrupt
  - Exception
  - Signal
---

## The Problem

When a Python script is running, pressing `Ctrl+C` in the terminal will immediately terminate the program.
This raises an exception called `KeyboardInterrupt`.
If this exception is not handled, the program may terminate abnormally without finishing its tasks.
This can lead to issues like unreleased resources, such as file handles or network connections.

```python
import time

print("Program started. Press Ctrl+C to exit.")
i = 0
while True:
    print(f"Working... {i}")
    time.sleep(1)
    i += 1
```

Running the code above and pressing `Ctrl+C` will terminate the program with a message like this:

```
Traceback (most recent call last):
  File "main.py", line 7, in <module>
    time.sleep(1)
KeyboardInterrupt
```

## Cause Analysis

`KeyboardInterrupt` is an exception class that inherits from `BaseException`.
The Python interpreter raises this exception when the user inputs `Ctrl+C` (a SIGINT signal).
This is a normal feature designed to give users control over program termination.
The problem is that this interruption can occur at an unexpected time, potentially leaving the program in an unstable state.

## Solution

### 1. Handle the Exception with a `try-except` Block

The most common way to handle `KeyboardInterrupt` is by using a `try-except` block.
This allows you to perform necessary cleanup tasks before the program exits.

```python
import time

print("Program started. Press Ctrl+C to exit.")
try:
    i = 0
    while True:
        print(f"Working... {i}")
        time.sleep(1)
        i += 1
except KeyboardInterrupt:
    print("\nProgram exiting. Performing cleanup.")
    # Add cleanup code here, like closing files or connections
    print("Cleanup complete. Goodbye.")
```

Now, when you press `Ctrl+C`, the code in the `except` block will be executed, allowing for a graceful shutdown.

### 2. Ensure Resource Cleanup with a `finally` Block

If you have cleanup code that must run regardless of whether a `KeyboardInterrupt` occurred, it is best to use a `finally` block.
The `finally` block is always executed, regardless of whether an exception was raised.

```python
import time

f = None
try:
    f = open("temp_file.txt", "w")
    print("File opened. Starting work.")
    i = 0
    while True:
        f.write(f"Log: {i}\n")
        print(f"Working... {i}")
        time.sleep(1)
        i += 1
except KeyboardInterrupt:
    print("\nProgram interrupted.")
finally:
    if f:
        f.close()
        print("File closed. Program terminated.")
```

This structure ensures that the file is safely closed when `Ctrl+C` is pressed.

### 3. Use the `signal` Module (Advanced)

If you want to handle signals at a lower level, you can use the `signal` module.
The `signal.signal()` function allows you to register a handler for the `SIGINT` signal.

```python
import signal
import sys
import time

def signal_handler(sig, frame):
    print("\nCtrl+C detected! Exiting gracefully.")
    # Perform necessary cleanup
    sys.exit(0)

# Register the handler for the SIGINT signal
signal.signal(signal.SIGINT, signal_handler)

print("Program started. Press Ctrl+C to exit.")
i = 0
while True:
    print(f"Working... {i}")
    time.sleep(1)
    i += 1
```

This method is more complex than `try-except` but is useful when you need to apply a consistent exit behavior across different parts of your program.

## Conclusion

`KeyboardInterrupt` is an important mechanism for handling user requests to terminate a program.
By properly handling this exception with a `try-except` block, you can prevent abnormal termination and ensure that resources are released safely.
In most cases, a combination of `try-except` and `finally` is sufficient. The `signal` module can be considered for more complex signal handling needs.

