---
typora-root-url: ../
layout: single
title: >
  Python Command Not Found on Windows: How to Fix It
seo_title: >
  Python Command Not Found on Windows: How to Fix It
date: 2026-05-23T12:00:00+09:00
last_modified_at: 2026-05-23T23:59:59+09:00
lang: en
translation_id: python-command-not-found-windows
header:
   teaser: /images/2026-05-23-python-command-not-found-windows/python-command-not-found-windows-hero.png
   overlay_image: /images/2026-05-23-python-command-not-found-windows/python-command-not-found-windows-hero.png
   overlay_filter: 0.5
   image_description: >
     Visual guide explaining Python Command Not Found on Windows: How to Fix It.
excerpt: >
  Fix python command not found on Windows by checking the py launcher, PATH, App Execution Aliases, and the active Python installation.
seo_description: >
  Fix python command not found on Windows by checking the py launcher, PATH, App Execution Aliases, and the active Python installation.
categories:
  - en_Troubleshooting
tags:
  - Python
  - Windows
  - PATH
  - py
---

## Problem

You open PowerShell or Command Prompt on Windows and run:

![Python Command Not Found on Windows: How to Fix It explanatory image](/images/2026-05-23-python-command-not-found-windows/python-command-not-found-windows-hero.png)

```powershell
python --version
```

But Windows returns an error such as:

```text
python is not recognized as an internal or external command
```

or:

```text
Python was not found; run without arguments to install from the Microsoft Store
```

This usually means Windows cannot find the `python.exe` command through `PATH`, or the Microsoft Store App Execution Alias is intercepting the command.

## Cause

`python command not found windows` problems usually come from one of these causes.

- Python is not installed.
- Python is installed, but its install folder is not in `PATH`.
- The Microsoft Store App Execution Alias is taking over `python`.
- The terminal was not restarted after installing Python.
- Multiple Python versions are installed and Windows finds the wrong one first.
- You installed Python, but only the `py` launcher works.
- `pip` is being used before confirming which Python is active.

The fastest path is to check whether the `py` launcher can find Python.

## Quick Fix

Run these commands in PowerShell:

```powershell
py --version
py -0p
where python
where py
```

If `py --version` works, Python is installed and the Python launcher can find it.
You can use:

```powershell
py script.py
py -m pip --version
py -m pip install package-name
```

If `py` works but `python` does not, the issue is usually `PATH` or the App Execution Alias.

## Step-by-Step Fix

### 1. Check Whether Python Is Installed

Run:

```powershell
py --version
```

If this prints a Python version, Python is available through the launcher.

Then list all Python versions that the launcher can see:

```powershell
py -0p
```

Example output:

```text
 -V:3.12 *        C:\Users\you\AppData\Local\Programs\Python\Python312\python.exe
 -V:3.11          C:\Users\you\AppData\Local\Programs\Python\Python311\python.exe
```

If `py` is also not found, install Python from the official Python website or your package manager, then open a new terminal.

### 2. Check Which python Command Windows Finds

Run:

```powershell
where python
```

You may see a real Python path, such as:

```text
C:\Users\you\AppData\Local\Programs\Python\Python312\python.exe
```

Or you may see the WindowsApps alias:

```text
C:\Users\you\AppData\Local\Microsoft\WindowsApps\python.exe
```

If the command points to `WindowsApps`, Windows may be using the Microsoft Store alias instead of your real Python installation.

### 3. Turn Off the Microsoft Store App Execution Alias

If Windows opens the Microsoft Store or shows "Python was not found", turn off the aliases.

Steps:

1. Open Windows Settings.
2. Go to `Apps`.
3. Open `Advanced app settings`.
4. Open `App execution aliases`.
5. Turn off `python.exe`.
6. Turn off `python3.exe`.
7. Close and reopen PowerShell or Command Prompt.

Then run:

```powershell
python --version
where python
```

If `python` still does not work, add Python to `PATH`.

### 4. Add Python to PATH

Find your Python install path with:

```powershell
py -0p
```

For a per-user Python install, the paths often look like:

```text
C:\Users\you\AppData\Local\Programs\Python\Python312\
C:\Users\you\AppData\Local\Programs\Python\Python312\Scripts\
```

Add both paths to the user `PATH`.

Steps:

1. Open Windows Search.
2. Search for `Environment Variables`.
3. Open `Edit environment variables for your account`.
4. Select `Path`.
5. Click `Edit`.
6. Add the Python folder.
7. Add the `Scripts` folder.
8. Save the changes.
9. Open a new terminal.

Do not test in the old terminal window.
Environment variable changes apply to new terminal sessions.

### 5. Prefer py When Multiple Python Versions Are Installed

If you have more than one Python version, the `py` launcher can be clearer than `python`.

Examples:

```powershell
py -3.12 --version
py -3.12 -m pip --version
py -3.12 script.py
```

This avoids guessing which `python.exe` appears first in `PATH`.

### 6. Check pip After Python Works

After `python` or `py` works, check `pip`.

```powershell
py -m pip --version
python -m pip --version
```

If `py -m pip` works but `python -m pip` does not, keep using `py -m pip` or fix the `python` command path.

Do not start with plain `pip`.
First confirm which Python interpreter you are using.

## How to Verify

Run:

```powershell
py --version
py -0p
where python
python --version
py -m pip --version
```

A healthy setup should show:

- `py` can list at least one Python version.
- `where python` points to a real Python install, not only `WindowsApps`.
- `python --version` prints the expected version.
- `py -m pip --version` works.

Then test a simple command:

```powershell
py -c "import sys; print(sys.executable)"
```

The output should point to the Python installation you intend to use.

## Common Mistakes

- Editing `PATH` and testing in the same old terminal.
- Leaving the Microsoft Store `python.exe` alias enabled.
- Installing Python but not checking the "Add python.exe to PATH" option.
- Using `pip` before confirming `py -m pip --version`.
- Having multiple Python versions and assuming `python` points to the newest one.
- Adding only the Python folder to `PATH` but not the `Scripts` folder.

## Related Posts

- [How to Fix pip install Failed in Python](/en_troubleshooting/python-pip-install-failed/)
- [How to Fix No module named pip in Python](/en_troubleshooting/python-no-module-named-pip/)
- [Python venv Not Activating: How to Fix It](/en_troubleshooting/python-venv-not-activating/)

## FAQ

### When should I use this guide?

Use it when you can reproduce the error and need a practical order for checking commands, versions, paths, permissions, and logs.

### What should beginners verify first?

Start with the exact error message, the command you ran, the operating system, and the tool version. These details usually narrow the cause faster than changing many settings at once.

### Which keywords should I search next?

Search for "Python Command Not Found on Windows: How to Fix It" together with the exact error text, version, operating system, and tool name used in your environment.
