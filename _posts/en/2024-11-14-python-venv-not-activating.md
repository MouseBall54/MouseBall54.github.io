---
typora-root-url: ../
layout: single
title: >
  Python venv Not Activating: How to Fix It
seo_title: >
  Python venv Not Activating: How to Fix It
date: 2024-11-14T07:54:00+09:00
last_modified_at: 2026-05-23T23:59:59+09:00
lang: en
translation_id: python-venv-not-activating
header:
   teaser: /images/2026-05-23-python-venv-not-activating/python-venv-not-activating-hero.png
   overlay_image: /images/2026-05-23-python-venv-not-activating/python-venv-not-activating-hero.png
   overlay_filter: 0.5
   image_description: >
     Visual guide explaining Python venv Not Activating: How to Fix It.
excerpt: >
  Fix Python venv activation problems by using the right shell command, checking PowerShell policy, and verifying the active interpreter path.
seo_description: >
  Fix Python venv activation problems by using the right shell command, checking PowerShell policy, and verifying the active interpreter path.
categories:
  - en_Troubleshooting
tags:
  - Python
  - venv
  - PowerShell
  - VirtualEnvironment
---

## Problem

You created a Python virtual environment with `python -m venv .venv`, but it does not seem to activate.
The terminal prompt may not change, `pip install` may still install globally, or VS Code may keep using a different Python interpreter.

![Python venv Not Activating: How to Fix It explanatory image](/images/2026-05-23-python-venv-not-activating/python-venv-not-activating-hero.png)

The confusing part is that prompt changes are only a visual clue.
The real test is whether `python` and `pip` now point inside the virtual environment.

## Cause

`venv` activation usually fails for one of these reasons.

- You used the activation command for the wrong shell.
- PowerShell blocks `Activate.ps1` because of the execution policy.
- You are running the command from the wrong project directory.
- The `.venv` folder was deleted or created somewhere else.
- VS Code is using a different selected interpreter.
- You are mixing `conda` and `venv` in the same terminal.
- The prompt did not change, but the environment actually activated.

The fix is to use the correct activation script for your shell, then verify the Python executable path.

## Quick Fix

Use the command that matches your shell.

### Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

### Windows Command Prompt

```cmd
.venv\Scripts\activate.bat
```

### Git Bash on Windows

```bash
source .venv/Scripts/activate
```

### macOS and Linux

```bash
source .venv/bin/activate
```

Then verify:

```bash
python -c "import sys; print(sys.executable)"
python -m pip --version
```

If the path includes `.venv`, the environment is active even if your prompt did not change.

## Step-by-Step Fix

### 1. Confirm the venv Folder Exists

From the project root, check that `.venv` exists.

Windows PowerShell:

```powershell
Get-ChildItem .venv
```

macOS and Linux:

```bash
ls .venv
```

If the folder does not exist, create it:

```bash
python -m venv .venv
```

If your machine has multiple Python versions, create the environment with the exact interpreter you want.

Windows:

```powershell
py -3.12 -m venv .venv
```

macOS and Linux:

```bash
python3.12 -m venv .venv
```

### 2. Use the Correct Activation Script

Each shell has a different activation file.

| Shell | Activation command |
| --- | --- |
| PowerShell | `.\.venv\Scripts\Activate.ps1` |
| Command Prompt | `.venv\Scripts\activate.bat` |
| Git Bash on Windows | `source .venv/Scripts/activate` |
| macOS/Linux shell | `source .venv/bin/activate` |

If you copy the macOS/Linux command into PowerShell, it will fail.
If you copy the PowerShell command into Git Bash, it will also fail.

### 3. Fix PowerShell Execution Policy

If PowerShell shows a message like "running scripts is disabled on this system", change the policy for the current user.

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Close the terminal, open a new PowerShell window, and activate again:

```powershell
.\.venv\Scripts\Activate.ps1
```

Use `CurrentUser`, not `LocalMachine`, unless you intentionally want a system-wide policy change.

### 4. Verify the Active Python

Do not rely only on the prompt.
Run:

```bash
python -c "import sys; print(sys.executable)"
```

Expected examples:

```text
C:\project\.venv\Scripts\python.exe
/home/user/project/.venv/bin/python
```

Then check `pip`:

```bash
python -m pip --version
```

The output should also point inside `.venv`.

### 5. Fix VS Code Interpreter Mismatch

If the terminal activates correctly but VS Code still runs another Python, select the interpreter manually.

In VS Code:

1. Open the Command Palette.
2. Run `Python: Select Interpreter`.
3. Choose the interpreter inside `.venv`.

The selected path should look like:

```text
.venv\Scripts\python.exe
```

or:

```text
.venv/bin/python
```

After selecting it, open a new terminal in VS Code and verify again:

```bash
python -c "import sys; print(sys.executable)"
```

### 6. Avoid Mixing conda and venv

If your prompt shows both a Conda environment and `.venv`, you may be mixing environment managers.
For a simple project, deactivate Conda first:

```bash
conda deactivate
```

Then activate `.venv` again.
Use one environment manager per project unless you have a specific reason to combine them.

## How to Verify

A working virtual environment should pass these checks.

```bash
python -c "import sys; print(sys.executable)"
python -m pip --version
python -c "import site; print(site.getsitepackages())"
```

The output should reference `.venv`.

Then install a small package and confirm it is installed inside the environment:

```bash
python -m pip install requests
python -m pip show requests
```

If `pip show` points to `.venv`, activation and installation are working.

## Common Mistakes

- Using `source .venv/bin/activate` in PowerShell.
- Running `Activate.ps1` from a directory that does not contain `.venv`.
- Assuming activation failed only because the prompt did not change.
- Installing packages with plain `pip` after activating with the wrong Python.
- Selecting the wrong interpreter in VS Code.
- Mixing Conda and `venv` without checking `sys.executable`.

## Professional Depth Check

For **Python venv Not Activating: How to Fix It**, the practical standard is not whether the reader can repeat one instruction once. Treat the topic as a reproducible debugging procedure: verify interpreter path, virtual environment, package version, and input file or data boundary before drawing a conclusion. The result should be written as a small decision record, because future readers need to know which fact was observed, which assumption was used, and which condition would change the answer.

### Evidence That Makes the Guidance Reliable

Use objective evidence before changing a workflow. Good evidence includes `python --version`, `python -m pip show`, the full traceback, and a minimal script. If two pieces of evidence conflict, keep the conflict visible instead of smoothing it over. For example, a successful quick fix is still weak evidence if the same input, account, dependency, or device state has not been tested again. A durable article should help the reader distinguish a confirmed fix from a plausible fix.

## Related Posts

- [How to Fix pip install Failed in Python](/en_troubleshooting/python-pip-install-failed/)
- [How to Fix No module named pip in Python](/en_troubleshooting/python-no-module-named-pip/)
- [How to Fix ModuleNotFoundError in Python](/en_troubleshooting/python-modulenotfounderror/)

## FAQ

### When should I use this guide?

Use it when you can reproduce the error and need a practical order for checking commands, versions, paths, permissions, and logs.

### What should beginners verify first?

Start with the exact error message, the command you ran, the operating system, and the tool version. These details usually narrow the cause faster than changing many settings at once.

### Which keywords should I search next?

Search for "Python venv Not Activating: How to Fix It" together with the exact error text, version, operating system, and tool name used in your environment.
