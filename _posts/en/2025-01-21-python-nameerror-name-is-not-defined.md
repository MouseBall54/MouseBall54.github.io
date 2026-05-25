---
typora-root-url: ../
layout: single
title: "How to Fix Python's NameError: name '...' is not defined"

date: 2025-01-21T07:25:00+09:00
lang: en
translation_id: python-nameerror-name-is-not-defined
excerpt: "Understand and fix the Python NameError, which occurs when a variable or function is used before it's defined. Learn common causes like typos and scope issues."
seo_description: "Understand and fix the Python NameError, which occurs when a variable or function is used before it's defined. Learn common causes like typos and scope issues."
header:
   teaser: /images/header_images/overlay_image_python.png
   overlay_image: /images/header_images/overlay_image_python.png
   overlay_filter: 0.5
   image_description: >
     A visual summary explaining the main topic of this post: How to Fix Python's NameError: name '...' is not defined
categories:
  - en_Troubleshooting
tags:
  - Python
  - NameError
  - Programming
  - Error Handling
---


![A visual summary explaining the main topic of this post: How to Fix Python's NameError: name '...' is not defined](/images/header_images/overlay_image_python.png)
## What is `NameError: name '...' is not defined`?

This error occurs when the Python interpreter encounters a name (variable, function, class) that it doesn't recognize.
Essentially, you are trying to use something that hasn't been created or assigned a value yet.
It is one of the most common errors for beginners.

## Common Causes and Solutions

Let's look at the typical reasons why you might see a `NameError` and how to resolve them.

### 1. Misspelling a Variable or Function Name

A simple typo is the most frequent cause. Python is case-sensitive, so `myVariable` is different from `myvariable`.

**Error Example:**
```python
message = "Hello, World!"
print(mesage)
```

**Output:**
```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'mesage' is not defined
```

**Solution:**
Correct the typo. Ensure the name used matches the name at declaration.

```python
message = "Hello, World!"
print(message) # Corrected from 'mesage'
```

### 2. Using a Variable Before Assignment

You must assign a value to a variable before you can use it.

**Error Example:**
```python
if some_condition:
    user_name = "Alice"

print(user_name) # NameError if some_condition is False
```

**Solution:**
Initialize the variable with a default value before the conditional block.

```python
user_name = "Guest" # Initialize with a default value
if some_condition:
    user_name = "Alice"

print(user_name)
```

### 3. Variable Scope Issues

A variable defined inside a function (a local variable) cannot be accessed from outside that function.

**Error Example:**
```python
def greet():
    greeting = "Hello from inside the function!"
    print(greeting)

greet()
print(greeting) # This will cause a NameError
```

**Output:**
```
Hello from inside the function!
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'greeting' is not defined
```

**Solution:**
If you need to use the value outside, `return` it from the function and assign it to a new variable.

```python
def greet():
    greeting = "Hello from inside the function!"
    return greeting

returned_greeting = greet()
print(returned_greeting)
```

### 4. Forgetting to Import a Module or Name

When using modules from the standard library or third-party packages, you must import them first.

**Error Example:**
```python
# Forgetting to import the 'math' module
print(math.sqrt(25))
```

**Output:**
```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'math' is not defined
```

**Solution:**
Add the required `import` statement at the top of your script.

```python
import math

print(math.sqrt(25))
```

By checking for these common mistakes, you can quickly identify and fix most `NameError` exceptions in your Python code.

## Professional Depth Check

For **How to Fix Python's NameError: name '...' is not defined**, the practical standard is not whether the reader can repeat one instruction once. Treat the topic as a reproducible debugging procedure: verify interpreter path, virtual environment, package version, and input file or data boundary before drawing a conclusion. The result should be written as a small decision record, because future readers need to know which fact was observed, which assumption was used, and which condition would change the answer.

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

## Applied Review Scenario

Assume a reader has already tried the first recommendation for **How to Fix Python's NameError: name '...' is not defined**, but the outcome is still uncertain. The next step is to build a short audit trail instead of trying several fixes at once. Start with one sentence that names the decision, one sentence that names the environment, and one sentence that names the observed result. Then compare interpreter path, virtual environment, package version, and input file or data boundary against the facts already captured. This prevents the article from becoming a list of disconnected tips.

### Audit Trail Template

| Field | Example Standard | Reason |
| --- | --- | --- |
| Observation | What was seen before action | Keeps the baseline objective |
| Evidence | `python --version`, and `python -m pip show` | Anchors the decision in records |
| Assumption | What is believed but not proven | Prevents hidden guesses |
| Action | One change at a time | Makes the result attributable |
| Stop Rule | When to stop and escalate | Reduces repeated trial and error |

### Quality Boundary

The guidance should be treated as strong only when the same result appears after a controlled recheck. If a different account, device, data sample, dependency version, contract term, or official rule is involved, the conclusion should be downgraded to a hypothesis. That distinction is important for search readers because they often arrive with an urgent problem and may skip context. A professional post should slow down the risky part of the decision while still giving a practical next action.

## Related Reading

Continue with these related posts from the same topic area.

- [How to Fix "SSL: CERTIFICATE_VERIFY_FAILED" Error in Python on Windows](/en_troubleshooting/python-certificate-verify-failed/)
- [How to Fix "Permission denied (publickey)" Error with Git on Windows](/en_troubleshooting/git-permission-denied-publickey-windows/)
