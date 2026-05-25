---
typora-root-url: ../
layout: single
title: "How to Fix Python's IndentationError: expected an indented block"

date: 2025-01-17T07:21:00+09:00
lang: en
translation_id: python-indentationerror-expected-an-indented-block
excerpt: "Master Python's core syntax: indentation! Understand the causes of and solutions for IndentationError, fix mixed tabs and spaces, and learn to write clean, error-free code."
seo_description: "Master Python's core syntax: indentation! Understand the causes of and solutions for IndentationError, fix mixed tabs and spaces, and learn to write clean, error-free code."
header:
   teaser: /images/header_images/overlay_image_python.png
   overlay_image: /images/header_images/overlay_image_python.png
   overlay_filter: 0.5
   image_description: >
     A visual summary explaining the main topic of this post: How to Fix Python's IndentationError: expected an indented block
categories:
  - en_Troubleshooting
tags:
  - Python
  - IndentationError
  - Programming
  - Beginner
---


![A visual summary explaining the main topic of this post: How to Fix Python's IndentationError: expected an indented block](/images/header_images/overlay_image_python.png)
## What is Python's `IndentationError: expected an indented block`?

Unlike many other programming languages that use braces `{}` to define code structure, Python uses **indentation**. The `IndentationError: expected an indented block` is a very Python-specific error that occurs when these indentation rules are not followed.

This error typically appears when a required indentation is missing from a code block or when the indentation style is inconsistent.

### 1. Missing Indentation in a Code Block

This is the most common cause. Statements that initiate a new code block, such as `if`, `for`, `def`, and `class`, must be followed by indented code.

**Incorrect Code:**
```python
def my_function():
print("This line is not indented.") # Requires indentation inside the def block
```

**Corrected Code:**
```python
def my_function():
    print("This line is now indented.")
```
In Python, the standard is to use **four spaces** for one level of indentation. Indenting the `print` function after the `def` statement resolves the error.

### 2. Unnecessary Indentation

Conversely, adding indentation where it isn't needed can also cause an `IndentationError` (specifically, an `unexpected indent` error).

**Incorrect Code:**
```python
x = 10
    print(x) # Unnecessary indentation
```

**Corrected Code:**
```python
x = 10
print(x)
```
Top-level code should always start at the far left, with no preceding spaces.

### 3. Mixing Tabs and Spaces

This is a tricky cause of `IndentationError` because it's often invisible. Python treats tabs and spaces as different characters. If you indent one line with a tab and another with spaces, the interpreter sees them as different indentation levels and raises an error.

**Potentially Incorrect Code (Visually Indistinguishable):**
```python
if True:
	print("This line is indented with a tab.")
    print("This line is indented with spaces.") # -> Raises IndentationError
```

**Solution:**

The best way to solve this is to configure your code editor to **automatically convert tabs to spaces**.

-   **Visual Studio Code**: In your `settings.json`, add the settings `"editor.insertSpaces": true` and `"editor.tabSize": 4`.
-   **PyCharm**: Go to `Settings > Editor > Code Style > Python`, uncheck `Use tab character`, and set `Indent` to 4.

To fix existing code, use your editor's feature to **"Convert Indentation to Spaces"**.

### Conclusion

`IndentationError` highlights the importance of indentation, which is fundamental to Python's syntax. To avoid this error, it's crucial to remember these rules:

1.  **Be Consistent**: Stick to one indentation style throughout your project (four spaces is the recommended standard).
2.  **Configure Your Editor**: Set up your editor to insert four spaces when you press the Tab key.
3.  **Check Your Blocks**: Always ensure that lines ending with a colon (`:`)—like `if`, `for`, and `def`—are followed by an indented code block.

Adopting proper indentation habits not only prevents `IndentationError` but is also the first step toward writing clean, readable code.

## Professional Depth Check

For **How to Fix Python's IndentationError: expected an indented block**, the practical standard is not whether the reader can repeat one instruction once. Treat the topic as a reproducible debugging procedure: verify interpreter path, virtual environment, package version, and input file or data boundary before drawing a conclusion. The result should be written as a small decision record, because future readers need to know which fact was observed, which assumption was used, and which condition would change the answer.

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

### Maintenance Standard

Recheck this guidance after dependency, operating-system, or build-tool changes. A useful update does not need to rewrite the entire post; it should confirm whether the examples, links, commands, screenshots, and decision criteria still match current behavior. If the old conclusion remains valid, record the check date. If it changes, explain what changed and why the previous advice is no longer enough.

### Practical Questions Before Acting

- What is the smallest observable signal that proves the problem or decision is real?
- Which source is official, and which part is local judgment?
- What should be captured before making changes?
- What result would show that the guidance did not apply?
- Who needs the record if the same issue appears again?

## Related Reading

Continue with these related posts from the same topic area.

- [How to Fix "SSL: CERTIFICATE_VERIFY_FAILED" Error in Python on Windows](/en_troubleshooting/python-certificate-verify-failed/)
- [How to Fix "Permission denied (publickey)" Error with Git on Windows](/en_troubleshooting/git-permission-denied-publickey-windows/)
