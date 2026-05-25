---
typora-root-url: ../
layout: single
title: "How to Fix Uncaught URIError: URI malformed in JavaScript"

date: 2025-02-18T07:53:00+09:00
lang: en
translation_id: javascript-uncaught-urierror-uri-malformed
excerpt: "Understand and resolve the JavaScript 'Uncaught URIError: URI malformed' by ensuring strings are correctly formatted before using URI decoding functions."
seo_description: "Understand and resolve the JavaScript 'Uncaught URIError: URI malformed' by ensuring strings are correctly formatted before using URI decoding functions."
header:
   teaser: /images/header_images/overlay_image_js.png
   overlay_image: /images/header_images/overlay_image_js.png
   overlay_filter: 0.5
   image_description: >
     A visual summary explaining the main topic of this post: How to Fix Uncaught URIError: URI malformed in JavaScript
categories:
  - en_Troubleshooting
tags:
  - JavaScript
  - URIError
  - URI
  - Decoding
  - Troubleshooting
---


![A visual summary explaining the main topic of this post: How to Fix Uncaught URIError: URI malformed in JavaScript](/images/header_images/overlay_image_js.png)
## What is `Uncaught URIError: URI malformed`?

The `Uncaught URIError: URI malformed` error occurs in JavaScript when you use a URI (Uniform Resource Identifier) handling function like `decodeURI()` or `decodeURIComponent()` with a string that is not a valid URI component.

These functions expect a specific format, and if they encounter character sequences that don't conform to the URI specification (e.g., a lone '%' sign not followed by two hex digits), they throw this error.

## Common Causes

The primary cause is passing an improperly encoded or corrupted URI string to a decoding function.

1.  **Invalid Percent-Encoding**: A common mistake is having a '%' character in the string that is not part of a valid percent-encoded sequence (e.g., `%20` for a space). For instance, a string like `"https://example.com/path?query=100%"` will fail because the trailing `%` is not a valid escape sequence.

2.  **Decoding an Already Decoded String**: Attempting to decode a string that has already been decoded can sometimes lead to this error if the string naturally contains characters that look like invalid URI sequences.

3.  **Manual String Manipulation**: Incorrectly constructing a URI string manually can easily introduce errors.

## How to Fix It

The key is to ensure the string you are decoding is a valid, encoded URI component.

### 1. Validate and Sanitize Input

Before attempting to decode a URI, especially if it comes from an external source or user input, you should validate it. The best way to prevent this error is to properly encode the URI components before they are transmitted or used.

Use `encodeURIComponent()` to encode special characters in a string before creating a full URI.

```javascript
// Incorrect: Manually creating a query string with special characters
const query = "search=this&that%"; // The '%' will cause an error
const url = `https://example.com/search?${query}`;

// Correct: Encoding the components first
const searchTerm = "this&that%";
const encodedSearchTerm = encodeURIComponent(searchTerm); // "this%26that%25"
const correctUrl = `https://example.com/search?query=${encodedSearchTerm}`;

console.log(correctUrl);
// "https://example.com/search?query=this%26that%25"
```

### 2. Use `try...catch` for Graceful Error Handling

If you cannot guarantee that a URI string will always be valid, wrap the decoding function in a `try...catch` block. This allows you to handle the error gracefully without crashing your application.

```javascript
function safelyDecodeURI(encodedString) {
  try {
    return decodeURIComponent(encodedString);
  } catch (e) {
    if (e instanceof URIError) {
      console.error("Failed to decode URI component:", encodedString);
      // Return a fallback value or the original string
      return encodedString;
    } else {
      // Re-throw other errors
      throw e;
    }
  }
}

// Example usage
const malformedURI = "https://example.com/data?value=100%";
const decoded = safelyDecodeURI(malformedURI);

console.log(decoded); // Logs the error and returns the original string
```

### 3. Check for Common Mistakes

- **Spaces**: Ensure spaces are properly encoded as `%20` or `+`.
- **Percent Signs**: A literal percent sign (`%`) in a URI must be encoded as `%25`.

Here is an example of how a malformed URI can be fixed:

```javascript
// Malformed URI with a stray '%'
let uri = "https://api.example.com/items?category=electronics%";

// Attempting to decode will throw an error
try {
  decodeURIComponent(uri);
} catch (e) {
  console.error(e); // URIError: URI malformed
}

// How to fix it:
// 1. If the '%' was a typo, remove it.
let correctedUri = uri.slice(0, -1); // "https://api.example.com/items?category=electronics"
console.log(decodeURIComponent(correctedUri));

// 2. If the '%' was intentional, it should have been encoded as %25.
let properlyEncodedUri = "https://api.example.com/items?category=electronics%25";
console.log(decodeURIComponent(properlyEncodedUri)); // "https://api.example.com/items?category=electronics%"
```

By ensuring that strings are correctly encoded before being passed to decoding functions and by using `try...catch` blocks for safety, you can effectively prevent and manage the `URIError: URI malformed` error.

## Professional Depth Check

For **How to Fix Uncaught URIError: URI malformed in JavaScript**, the practical standard is not whether the reader can repeat one instruction once. Treat the topic as a reproducible debugging procedure: verify browser or Node version, bundler setting, async boundary, and DOM or API state before drawing a conclusion. The result should be written as a small decision record, because future readers need to know which fact was observed, which assumption was used, and which condition would change the answer.

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

## Related Reading

Continue with these related posts from the same topic area.

- [How to Fix "SSL: CERTIFICATE_VERIFY_FAILED" Error in Python on Windows](/en_troubleshooting/python-certificate-verify-failed/)
- [How to Fix "Permission denied (publickey)" Error with Git on Windows](/en_troubleshooting/git-permission-denied-publickey-windows/)
