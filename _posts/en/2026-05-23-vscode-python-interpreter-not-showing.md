---
typora-root-url: ../
layout: single
title: >
  VS Code Python Interpreter Not Showing: How to Find and Select the Right Environment
seo_title: >
  VS Code Python Interpreter Not Showing
date: 2026-05-23T23:59:59+09:00
last_modified_at: 2026-05-23T23:59:59+09:00
lang: en
translation_id: vscode-python-interpreter-not-showing
header:
   teaser: /images/2026-05-23-vscode-python-interpreter-not-showing/vscode-python-interpreter-hero.png
   overlay_image: /images/2026-05-23-vscode-python-interpreter-not-showing/vscode-python-interpreter-hero.png
   overlay_filter: 0.35
   image_description: >
     Visual guide explaining VS Code Python Interpreter Not Showing: How to Find and Select the Right Environment.
excerpt: >
  Fix VS Code Python interpreter not showing by checking the Python extension, workspace folder, virtual environment location, manual interpreter path, and terminal environment.
seo_description: >
  Fix VS Code Python interpreter not showing by checking the Python extension, workspace folder, virtual environment, manual path, and terminal.
categories:
  - en_Troubleshooting
tags:
  - Python
  - VSCode
  - VirtualEnvironment
  - Interpreter
  - Windows
---

## Quick Answer

If the Python interpreter is not showing in VS Code, first confirm the Python extension is installed and you opened a folder, not just a single file.
Then create or locate the virtual environment, use **Python: Select Interpreter**, and choose the interpreter path manually if auto-detection misses it.

![VS Code Python interpreter picker with missing environment and recovery paths](/images/2026-05-23-vscode-python-interpreter-not-showing/vscode-python-interpreter-hero.png)

The image shows the common situation.
The editor is open, but the expected environment is missing from the picker.
The fix is to verify the extension, workspace, environment path, refresh state, and terminal.

## 1. Confirm the Python Extension

Open Extensions in VS Code and check that the Microsoft Python extension is installed and enabled.
Then reload the window:

```text
Developer: Reload Window
```

If the extension is disabled for the workspace, the interpreter picker may not behave as expected.

## 2. Open the Project Folder

VS Code detects environments better when a workspace folder is open.
Use:

```text
File > Open Folder
```

Do not only open one `.py` file.
Virtual environments are usually discovered relative to the workspace folder.

Good project shape:

```text
my-project/
  .venv/
  src/
  pyproject.toml
```

If `.venv` is outside the workspace, auto-detection may miss it.
Manual selection can still work.

## 3. Create a Virtual Environment

From the project folder:

```bash
python -m venv .venv
```

Windows activation:

```powershell
.\.venv\Scripts\Activate.ps1
```

macOS or Linux:

```bash
source .venv/bin/activate
```

Then reload VS Code and run:

```text
Python: Select Interpreter
```

If `.venv` is inside the workspace, it usually appears in the list.

## 4. Select the Interpreter Manually

If the interpreter still does not appear, choose:

```text
Python: Select Interpreter
Enter interpreter path
```

Common paths:

Windows:

```text
.\.venv\Scripts\python.exe
```

macOS or Linux:

```text
./.venv/bin/python
```

After selection, VS Code stores the interpreter choice for the workspace.

## 5. Check Terminal and VS Code Are Using the Same Python

In the VS Code terminal:

```bash
python --version
python -c "import sys; print(sys.executable)"
```

If the path does not match the selected interpreter, open a new terminal after selecting it.
The old terminal may keep the previous environment.

Also check:

```text
Python: Create Environment
Python: Select Interpreter
Python: Clear Workspace Interpreter Setting
```

These commands help reset a confused workspace.

## 6. Check Windows Execution Policy

On Windows, activation can fail because PowerShell blocks scripts.
If activation fails, VS Code may still select the interpreter manually, but the terminal environment may not activate.

For the current user:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Use the least broad policy that works for your environment.

## Common Mistakes

The first mistake is installing Python but not the VS Code Python extension.

The second mistake is opening a single file instead of the project folder.

The third mistake is creating `.venv` in a different directory than the workspace.

The fourth mistake is selecting an interpreter and then using an old terminal that was opened before the selection.

The fifth mistake is confusing global Python, Conda, and virtual environment Python.
Check `sys.executable` to know what is actually running.

## Related Reading

- [Python venv Not Activating](/en_Troubleshooting/python-venv-not-activating/)
- [Python Command Not Found on Windows](/en_Troubleshooting/python-command-not-found-windows/)
- [VS Code: Python environments](https://code.visualstudio.com/docs/python/environments)
- [VS Code Python tutorial](https://code.visualstudio.com/docs/python/python-tutorial)

## Final Checklist

```text
[ ] Python extension is installed and enabled.
[ ] A project folder is open.
[ ] `.venv` exists inside or near the workspace.
[ ] Interpreter path can be selected manually.
[ ] New terminal uses the selected Python.
[ ] `sys.executable` points to the expected environment.
```

When auto-detection fails, manual interpreter selection is the fastest reliable fix.
After that, verify with `sys.executable`, not only the status bar.

## FAQ

### When should I use this guide?

Use it when you can reproduce the error and need a practical order for checking commands, versions, paths, permissions, and logs.

### What should beginners verify first?

Start with the exact error message, the command you ran, the operating system, and the tool version. These details usually narrow the cause faster than changing many settings at once.

### Which keywords should I search next?

Search for "VS Code Python Interpreter Not Showing: How to Find and Select the Right Environment" together with the exact error text, version, operating system, and tool name used in your environment.
