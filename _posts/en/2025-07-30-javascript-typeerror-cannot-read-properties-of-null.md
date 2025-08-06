---
typora-root-url: ../
layout: single
title: "How to Fix JavaScript's TypeError: Cannot read properties of null"

lang: en
translation_id: javascript-typeerror-cannot-read-properties-of-null
excerpt: "Every JavaScript developer encounters 'Cannot read properties of null'. Clearly understand its cause and learn how to effectively fix it by managing DOM loading times and using conditional access."
header:
   teaser: /images/header_images/overlay_image_js.png
   overlay_image: /images/header_images/overlay_image_js.png
   overlay_filter: 0.5
categories:
  - en_Troubleshooting
tags:
  - JavaScript
  - TypeError
  - DOM
  - Frontend
---

## What is the `TypeError: Cannot read properties of null` Error in JavaScript?

This error occurs when you try to access a property of a variable or object that holds a `null` value. `null` is a special value in JavaScript that intentionally represents "no value." In essence, this `TypeError` means you tried to read something from a target that doesn't exist.

It is an extremely common error in web development, especially when manipulating the DOM (Document Object Model).

### The Most Common Cause: Accessing a DOM Element Before It Loads

The most typical reason for this error is that **your JavaScript code attempts to access an HTML element before it has been rendered on the page**.

**Incorrect Code:**
```html
<!DOCTYPE html>
<html>
<head>
  <title>Error Example</title>
  <script>
    const myButton = document.getElementById('myBtn');
    // At this point, the <button> tag has not been loaded yet.
    // Therefore, document.getElementById('myBtn') returns null.
    myButton.addEventListener('click', function() { // Accessing addEventListener on null -> TypeError
      alert('Button clicked!');
    });
  </script>
</head>
<body>
  <button id="myBtn">Click Me</button>
</body>
</html>
```
In the code above, the `<script>` tag is executed before the `<body>` tag. Consequently, when the script runs `document.getElementById('myBtn')`, the button with the ID `myBtn` does not yet exist in the DOM. The `myButton` variable is assigned `null`, and attempting to execute `null.addEventListener(...)` results in a `TypeError`.

### Solutions

#### 1. Move the Script to the End of the `<body>` Tag

This is the simplest and most direct solution. It ensures that all HTML elements are loaded before the script tries to access them.

**Corrected Code:**
```html
<!DOCTYPE html>
<html>
<head>
  <title>Solution Example</title>
</head>
<body>
  <button id="myBtn">Click Me</button>

  <script>
    const myButton = document.getElementById('myBtn');
    // At this point, the <button> tag has already been loaded.
    myButton.addEventListener('click', function() {
      alert('Button clicked!');
    });
  </script>
</body>
</html>
```

#### 2. Use the `DOMContentLoaded` Event Listener

If you want to keep your script in the `<head>` while ensuring it only runs after the DOM is fully loaded, you can use the `DOMContentLoaded` event. This approach is often better for organizing your code logically.

**Corrected Code:**
```html
<script>
  document.addEventListener('DOMContentLoaded', function() {
    // This code will only run after the entire DOM is loaded.
    const myButton = document.getElementById('myBtn');
    myButton.addEventListener('click', function() {
      alert('Button clicked!');
    });
  });
</script>
```

### Defensive Coding: Conditional Access

Another good practice to prevent this error is to check if an object is not `null` before accessing its properties. This prevents your entire script from halting due to an unexpected error.

**Using a Conditional Statement:**
```javascript
const myElement = document.getElementById('nonExistentElement');

if (myElement) { // Only run the code if myElement is not null
  myElement.style.color = 'red';
}
```

**Using Optional Chaining (`?.`)**

In modern JavaScript (ES2020), you can write this more concisely with the Optional Chaining operator (`?.`). It allows you to safely access properties of an object that might be `null` or `undefined`.

```javascript
const myElement = document.getElementById('nonExistentElement');

// Accesses .style only if myElement is not null or undefined; otherwise, returns undefined.
const color = myElement?.style?.color;
console.log(color); // undefined (no error is thrown)
```

### Conclusion

The `TypeError: Cannot read properties of null` is most often a DOM loading-order issue. To fix it:

1.  **Check your script's location** and consider moving it to the end of the `<body>`.
2.  Use the **`DOMContentLoaded` event** to run your code only after the DOM is ready.
3.  Adopt a defensive coding style by using **conditional statements** or **Optional Chaining (`?.`)** to account for the possibility of `null` values.
