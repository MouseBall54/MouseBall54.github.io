---
typora-root-url: ../
layout: single
title: >
    How to Fix JavaScript SyntaxError: Unterminated string literal
date: 2025-04-13T07:17:00+09:00
seo_title: >
    How to Fix JavaScript SyntaxError: Unterminated string literal

lang: en
translation_id: javascript-syntaxerror-unterminated-string-literal
header:
   teaser: /images/header_images/overlay_image_js.png
   overlay_image: /images/header_images/overlay_image_js.png
   overlay_filter: 0.5
   image_description: >
     A visual summary explaining the main topic of this post: How to Fix JavaScript SyntaxError: Unterminated string literal
excerpt: >
    In JavaScript, "SyntaxError: Unterminated string literal" is a syntax error that occurs when a string is not closed properly. This error is usually caused by issues with quotes or line breaks. This post explains the causes of the error and how to fix it.
seo_description: >
    In JavaScript, "SyntaxError: Unterminated string literal" is a syntax error that occurs when a string is not closed properly. This error is usually caused by issues with quotes or line breaks. This post explains the causes of the error and how to fix it.
categories:
  - en_Troubleshooting
tags:
  - JavaScript
  - SyntaxError
  - String
  - Error
---


![A visual summary explaining the main topic of this post: How to Fix JavaScript SyntaxError: Unterminated string literal](/images/header_images/overlay_image_js.png)
## The Problem

When writing JavaScript code, you might encounter the `SyntaxError: Unterminated string literal` (or in some browsers, `Uncaught SyntaxError: Invalid or unexpected token`).
This error means that a string literal was not properly terminated.
It usually occurs when there is an opening quote for a string but no closing quote, or when an invalid character is used within the string.

```javascript
// Incorrect Example 1: Missing closing quote
let message = 'Hello, world;

// Incorrect Example 2: Line break inside a string
let htmlString = '<div>
    <p>Hello</p>
</div>';

console.log(message);
console.log(htmlString);
```

Both of the above code snippets will cause a `SyntaxError`.
The first one is missing a closing single quote (`'`).
The second one includes a direct line break within a regular string.

## Cause Analysis

The main causes of this error are:

1.  **Mismatched or Missing Quotes**: The closing quote does not match the opening quote, or the closing quote is missing entirely.
2.  **Raw Line Breaks in a String**: A normal single-quoted or double-quoted string cannot contain a direct line break.
3.  **Copied Smart Quotes**: Text copied from documents or chat tools may include `“` or `’` instead of JavaScript string delimiters.
4.  **Unescaped Quotes Inside Text**: A quote inside the string can terminate it early unless it is escaped or the delimiter is changed.

## Reliable Fixes

Use the fix that matches the shape of the string. Do not just add a quote at the end without checking whether the string should be single-line, multi-line, or generated from data.

### 1. Close the String With the Same Delimiter

```javascript
const message = 'Hello, world';
const title = "Today's report";
```

The opening and closing delimiters must match. If the string contains an apostrophe, double quotes may be clearer. If the string contains double quotes, single quotes or a template literal may be clearer.

### 2. Use a Template Literal for Multi-Line Text

```javascript
const htmlString = `<div>
  <p>Hello</p>
</div>`;
```

Template literals use backticks and can contain line breaks. They are useful for readable snippets of HTML, SQL-like text, or messages that are assembled across multiple lines. They should still be reviewed carefully when user-controlled data is inserted, because template literals do not make unsafe HTML safe by themselves.

### 3. Escape an Internal Quote

```javascript
const sentence = 'It\\'s ready';
const label = "Click the \"Save\" button";
```

Escaping is appropriate when the string is short and the delimiter choice is intentional. If the string becomes hard to read, changing the delimiter or using a template literal is usually more maintainable.

## How to Verify the Fix

Run the smallest file that reproduces the error before returning to the full application. In Node.js, use `node file.js`. In a browser, open DevTools and check the Console line number. If a bundler such as Vite, Webpack, or Next.js is involved, also check whether the reported line points to source code or generated output. Source maps can shift the location, so the useful evidence is the original source line, the delimiter used on that line, and the character immediately before the reported token.

## Prevention Checklist

- Prefer an editor or formatter that highlights unmatched strings.
- Keep long HTML or message templates in template literals rather than broken single-line strings.
- Avoid pasting rich-text quotes into code.
- Add a lint rule or formatter step so quote issues fail before deployment.
- When debugging, reduce the code to the smallest string that still produces the syntax error.

## Professional Depth Check

For **How to Fix JavaScript SyntaxError: Unterminated string literal**, the practical standard is not whether the reader can repeat one instruction once. Treat the topic as a reproducible debugging procedure: verify browser or Node version, bundler setting, async boundary, and DOM or API state before drawing a conclusion. The result should be written as a small decision record, because future readers need to know which fact was observed, which assumption was used, and which condition would change the answer.

### Evidence That Makes the Guidance Reliable

Use objective evidence before changing a workflow. Good evidence includes console stack trace, `node --version`, network tab output, and a minimal reproduction. If two pieces of evidence conflict, keep the conflict visible instead of smoothing it over. For example, a successful quick fix is still weak evidence if the same input, account, dependency, or device state has not been tested again. A durable article should help the reader distinguish a confirmed fix from a plausible fix.

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

Assume a reader has already tried the first recommendation for **How to Fix JavaScript SyntaxError: Unterminated string literal**, but the outcome is still uncertain. The next step is to build a short audit trail instead of trying several fixes at once. Start with one sentence that names the decision, one sentence that names the environment, and one sentence that names the observed result. Then compare browser or Node version, bundler setting, async boundary, and DOM or API state against the facts already captured. This prevents the article from becoming a list of disconnected tips.

### Audit Trail Template

| Field | Example Standard | Reason |
| --- | --- | --- |
| Observation | What was seen before action | Keeps the baseline objective |
| Evidence | console stack trace, and `node --version` | Anchors the decision in records |
| Assumption | What is believed but not proven | Prevents hidden guesses |
| Action | One change at a time | Makes the result attributable |
| Stop Rule | When to stop and escalate | Reduces repeated trial and error |

### Quality Boundary

The guidance should be treated as strong only when the same result appears after a controlled recheck. If a different account, device, data sample, dependency version, contract term, or official rule is involved, the conclusion should be downgraded to a hypothesis. That distinction is important for search readers because they often arrive with an urgent problem and may skip context. A professional post should slow down the risky part of the decision while still giving a practical next action.

## Related Reading

Continue with these related posts from the same topic area.

- [How to Fix "SSL: CERTIFICATE_VERIFY_FAILED" Error in Python on Windows](/en_troubleshooting/python-certificate-verify-failed/)
- [How to Fix "Permission denied (publickey)" Error with Git on Windows](/en_troubleshooting/git-permission-denied-publickey-windows/)
