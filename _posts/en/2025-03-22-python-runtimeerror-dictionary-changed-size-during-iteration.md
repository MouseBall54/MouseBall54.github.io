---
typora-root-url: ../
layout: single
title: >
    How to Fix Python RuntimeError: dictionary changed size during iteration

date: 2025-03-22T07:40:00+09:00
lang: en
translation_id: python-runtimeerror-dictionary-changed-size-during-iteration
header:
   teaser: /images/header_images/overlay_image_python.png
   overlay_image: /images/header_images/overlay_image_python.png
   overlay_filter: 0.5
   image_description: >
     A visual summary explaining the main topic of this post: How to Fix Python RuntimeError: dictionary changed size during iteration
excerpt: >
    Learn how to fix the `RuntimeError: dictionary changed size during iteration` in Python, which occurs when you modify a dictionary while looping over it.
seo_description: >
    Learn how to fix the `RuntimeError: dictionary changed size during iteration` in Python, which occurs when you modify a dictionary while looping over it.
categories:
  - en_Troubleshooting
tags:
  - Python
  - RuntimeError
  - Dictionary
  - Iteration
---


![A visual summary explaining the main topic of this post: How to Fix Python RuntimeError: dictionary changed size during iteration](/images/header_images/overlay_image_python.png)
## The Problem

When you try to add or remove items from a dictionary while iterating over it using a `for` loop in Python, you might encounter the following `RuntimeError`:

```
RuntimeError: dictionary changed size during iteration
```

This error occurs because Python does not allow the size of a dictionary to be modified during iteration. This restriction ensures the consistency of the loop operation.

## Example of Error-Prone Code

Here is an example that tries to remove items with even values from a dictionary, which will trigger the error.

```python
numbers = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# This code will raise a RuntimeError
for key, value in numbers.items():
    if value % 2 == 0:
        del numbers[key]

print(numbers)
```

When you run this code, the `del numbers[key]` statement changes the size of the `numbers` dictionary inside the `for` loop, causing the `RuntimeError`.

## How to Fix It

There are several ways to solve this issue. The key is to iterate over a copy of the dictionary instead of modifying the original one directly.

### 1. Use a Copy of the Dictionary

The simplest solution is to iterate over a shallow copy of the dictionary, which you can create using the `.copy()` method. This allows you to safely modify the original dictionary.

```python
numbers = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Iterate over a copy of the dictionary
for key, value in numbers.copy().items():
    if value % 2 == 0:
        del numbers[key] # Delete the item from the original dictionary

print(numbers)
# Output: {'a': 1, 'c': 3}
```

### 2. Iterate Over a List of Keys

Another approach is to create a list of the dictionary's keys before the loop starts. You can then iterate over this static list to modify the dictionary.

```python
numbers = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Create a list of keys to iterate over
for key in list(numbers.keys()):
    if numbers[key] % 2 == 0:
        del numbers[key]

print(numbers)
# Output: {'a': 1, 'c': 3}
```

### 3. Create a New Dictionary (Dictionary Comprehension)

Instead of modifying the existing dictionary, a cleaner and often safer approach is to create a new dictionary containing only the items you want to keep. **Dictionary comprehension** is a concise way to achieve this.

```python
numbers = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Create a new dictionary with only the desired items
filtered_numbers = {key: value for key, value in numbers.items() if value % 2 != 0}

print(filtered_numbers)
# Output: {'a': 1, 'c': 3}
```

This method is highly readable and avoids mutating the data you are iterating over, which is generally a good practice.

## Conclusion

The `RuntimeError: dictionary changed size during iteration` is triggered when you modify a dictionary while looping through it. To resolve this, remember these three techniques:

1.  Iterate over a copy using `.copy()`.
2.  Iterate over a list of keys using `list(dictionary.keys())`.
3.  Create a new dictionary with the desired items instead of modifying the original.

In most cases, using a **dictionary comprehension** is the recommended approach because it is both concise and safe.

## Professional Depth Check

For **How to Fix Python RuntimeError: dictionary changed size during iteration**, the practical standard is not whether the reader can repeat one instruction once. Treat the topic as a reproducible debugging procedure: verify interpreter path, virtual environment, package version, and input file or data boundary before drawing a conclusion. The result should be written as a small decision record, because future readers need to know which fact was observed, which assumption was used, and which condition would change the answer.

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
