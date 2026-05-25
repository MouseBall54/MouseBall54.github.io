---
typora-root-url: ../
layout: single
title: "How to Fix ModuleNotFoundError in Python"

date: 2025-01-20T07:24:00+09:00
lang: en
translation_id: python-modulenotfounderror
excerpt: "A guide to resolving the ModuleNotFoundError: No module named '...' in Python. Learn how to install and manage modules to avoid this common error."
seo_description: "A guide to resolving the ModuleNotFoundError: No module named '...' in Python. Learn how to install and manage modules to avoid this common error."
header:
   teaser: /images/header_images/overlay_image_python.png
   overlay_image: /images/header_images/overlay_image_python.png
   overlay_filter: 0.5
   image_description: >
     A visual summary explaining the main topic of this post: How to Fix ModuleNotFoundError in Python
categories:
  - en_Troubleshooting
tags:
  - Python
  - ModuleNotFoundError
  - pip
  - Modules
  - Error Handling
---


![A visual summary explaining the main topic of this post: How to Fix ModuleNotFoundError in Python](/images/header_images/overlay_image_python.png)
## What is `ModuleNotFoundError`?

A `ModuleNotFoundError` is an exception that Python raises when it cannot find a module you are trying to import. This error was introduced in Python 3.6; in older versions, it would raise an `ImportError`. It's one of the most common issues for beginners and experienced developers alike, especially when setting up a new project or environment.

The error message is usually very clear:
`ModuleNotFoundError: No module named 'some_module'`

This means Python looked for `some_module` in its list of installed modules and couldn't find it.

## Common Causes of `ModuleNotFoundError`

- **Module Not Installed:** The most frequent cause is that the module is not installed in the Python environment you are using.
- **Typo in Module Name:** You might have misspelled the module's name in your `import` statement.
- **Incorrect Python Environment:** You may have multiple Python installations or virtual environments, and the module is installed in one environment, but you are running your script from another.
- **Circular Dependencies:** In rare cases, two or more modules might be importing each other in a circular fashion, which can sometimes lead to import issues.

## How to Fix `ModuleNotFoundError`

Here’s how you can troubleshoot and fix this error.

### 1. Install the Missing Module with `pip`

If the module is not installed, you can usually install it using `pip`, Python's package installer. Open your terminal or command prompt and run:

```bash
pip install some_module
```

Replace `some_module` with the actual name of the module you need. For example, to install the popular `requests` library, you would run:

```bash
pip install requests
```

**Note:** Sometimes the package name to install with `pip` is different from the module name you import. For example, to use the `cv2` module, you need to install `opencv-python`. A quick search online usually clarifies the correct package name.

### 2. Check for Typos

Carefully check your `import` statement for any spelling mistakes. It's an easy mistake to make.

```python
# Incorrect: typo in 'requests'
import reqeusts 

# Correct
import requests
```

### 3. Verify Your Python Environment

If you have multiple versions of Python installed (e.g., Python 2.7 and Python 3.8) or use virtual environments, you need to make sure you are installing the package in the same environment where you are running your script.

You can check the Python version you are using with:

```bash
python --version
# or
python3 --version
```

To ensure you are using the correct `pip` for your Python environment, you can run `pip` as a module:

```bash
python -m pip install some_module
```

This command guarantees that the package is installed for the `python` executable you are running.

### 4. Understanding Virtual Environments

Virtual environments are a best practice in Python development. They allow you to create isolated environments for each project, with their own set of installed packages.

If you are using a virtual environment (e.g., created with `venv` or `conda`), make sure you have **activated** it before installing packages or running your script.

**To activate a `venv` environment:**

- **Windows:** `my-env\Scripts\activate`
- **macOS/Linux:** `source my-env/bin/activate`

Once activated, your terminal prompt will usually change to show the environment's name. Any `pip install` commands will then apply only to that active environment.

## Conclusion

A `ModuleNotFoundError` is a common roadblock that is usually easy to fix. By ensuring the module is installed with the correct `pip`, checking for typos, and verifying that you are operating in the correct Python environment, you can quickly resolve this error and get back to coding. Using virtual environments from the start of a project is a great way to prevent such issues altogether.

## Professional Depth Check

For **How to Fix ModuleNotFoundError in Python**, the practical standard is not whether the reader can repeat one instruction once. Treat the topic as a reproducible debugging procedure: verify interpreter path, virtual environment, package version, and input file or data boundary before drawing a conclusion. The result should be written as a small decision record, because future readers need to know which fact was observed, which assumption was used, and which condition would change the answer.

### Evidence That Makes the Guidance Reliable

Use objective evidence before changing a workflow. Good evidence includes `python --version`, `python -m pip show`, the full traceback, and a minimal script. If two pieces of evidence conflict, keep the conflict visible instead of smoothing it over. For example, a successful quick fix is still weak evidence if the same input, account, dependency, or device state has not been tested again. A durable article should help the reader distinguish a confirmed fix from a plausible fix.

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

## Related Reading

Continue with these related posts from the same topic area.

- [How to Fix "SSL: CERTIFICATE_VERIFY_FAILED" Error in Python on Windows](/en_troubleshooting/python-certificate-verify-failed/)
- [How to Fix "Permission denied (publickey)" Error with Git on Windows](/en_troubleshooting/git-permission-denied-publickey-windows/)
