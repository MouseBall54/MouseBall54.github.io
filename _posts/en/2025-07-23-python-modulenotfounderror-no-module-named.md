---
typora-root-url: ../
layout: single
title: >
  How to Fix "ModuleNotFoundError: No module named '…'" in Python
date: 2025-07-23T22:00:00+09:00
excerpt: >
  "Learn to resolve Python's 'ModuleNotFoundError' by installing the correct package, activating the right environment, and checking your import paths.
lang: en
translation_id: python-modulenotfounderror-no-module-named
header:
   teaser: /images/header_images/overlay_image_python.png
   overlay_image: /images/header_images/overlay_image_python.png
   overlay_filter: 0.5
categories:
  - en_Troubleshooting
tags:
  - Python
  - ModuleNotFoundError
  - ErrorHandling
---

## Introduction

When you run a Python script, you may see:

```bash
ModuleNotFoundError: No module named 'requests'
```

This means Python can’t locate the module you’re trying to import.

## What Is ModuleNotFoundError?

* A built-in exception raised when `import x` fails.
* Indicates that `x` is not in any folder on `sys.path`.

## Common Causes

1. **Package not installed**.
2. **Wrong virtual environment** active.
3. **Multiple Python versions** (pip vs. python mismatch).
4. **Naming conflicts** (your script named `requests.py`).
5. **Incorrect PYTHONPATH** or broken install.

## Solution 1: Install the Module

```bash
# For latest pip
python -m pip install <module_name>

# Or specify version
python -m pip install <module_name>==1.2.3
```

Use `python -m pip` to match the interpreter you run.

## Solution 2: Activate Your Virtual Environment

1. Create env (if none):

   ```bash
   python -m venv env
   ```
2. Activate:

   * **Windows (PowerShell)**:

     ```powershell
     .\env\Scripts\Activate.ps1
     ```
   * **Git Bash**:

     ```bash
     source env/Scripts/activate
     ```
3. Then reinstall your package inside the env.

## Solution 3: Check Python Version and Pip

Ensure you install with the same Python you run:

```bash
which python
which pip
# Or on Windows
where python
where pip
```

If they differ, use `python -m pip install`.

## Solution 4: Avoid Naming Conflicts

* Don’t name your script or folder the same as the module.
* Rename `requests.py` to avoid shadowing the real package.

## Solution 5: Verify PYTHONPATH and Site-Packages

* Inspect `sys.path` in Python:

  ```python
  import sys
  print(sys.path)
  ```
* Ensure the folder containing your module is listed.
* If using editable installs, run:

  ```bash
  pip install -e .
  ```

## Conclusion

`ModuleNotFoundError` is almost always an install or path issue.
Install with the correct interpreter, activate your environment, and avoid naming collisions.

