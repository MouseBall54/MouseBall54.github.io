---
typora-root-url: ../
layout: single
title: "How to Fix Uncaught URIError: URI malformed in JavaScript"
date: 2025-07-31T12:00:00+09:00
excerpt: "Understand and resolve the JavaScript 'Uncaught URIError: URI malformed' by ensuring strings are correctly formatted before using URI decoding functions."
categories:
  - en_Troubleshooting
tags:
  - JavaScript
  - URIError
  - URI
  - Decoding
  - Troubleshooting
---

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
