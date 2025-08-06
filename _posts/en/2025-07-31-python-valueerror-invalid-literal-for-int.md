---
typora-root-url: ../
layout: single
title: "How to Fix Python's ValueError: invalid literal for int() with base 10"

lang: en
translation_id: python-valueerror-invalid-literal-for-int
excerpt: "Resolve Python's 'ValueError: invalid literal for int()' by ensuring the string you are converting is a valid integer. Learn to use try-except blocks for safe conversion and the str.isdigit() method for validation."
header:
   teaser: /images/header_images/overlay_image_python.png
   overlay_image: /images/header_images/overlay_image_python.png
   overlay_filter: 0.5
categories:
  - en_Troubleshooting
tags:
  - Python
  - ValueError
  - Type Conversion
  - Exception Handling
---

## What is "ValueError: invalid literal for int() with base 10"?

This `ValueError` is one of the most common exceptions in Python, especially for beginners. It occurs when you try to convert a string to an integer using the `int()` function, but the string's content is not a valid number in base 10 (the standard decimal system).

The "literal" in the error message refers to the string value you are trying to convert. Essentially, Python is telling you, "I don't know how to interpret this string as a whole number."

## Common Causes and Solutions

Let's look at why this error happens and how to prevent it.

### 1. The String Contains Non-Numeric Characters

The most direct cause is trying to convert a string that contains letters, symbols, or other non-digit characters.

#### Problematic Code

```python
# This will raise a ValueError
number_string = "123a"
integer_value = int(number_string)
print(integer_value)
```

Python cannot convert `"123a"` because the character `'a'` is not a digit.

#### Solution: Use a `try-except` Block

When you are not sure if a string will always be a valid number (e.g., with user input), the safest approach is to wrap the conversion in a `try-except` block. This allows you to handle the error gracefully instead of crashing your program.

```python
number_string = "123a"
integer_value = 0 # Default value

try:
    integer_value = int(number_string)
    print(f"Successfully converted: {integer_value}")
except ValueError:
    print(f"Conversion failed: '{number_string}' is not a valid integer.")

# The program continues running
print(f"The value is: {integer_value}")
```

### 2. The String Represents a Floating-Point Number

The `int()` function does not automatically handle strings that represent floating-point numbers (numbers with a decimal point).

#### Problematic Code

```python
# This will raise a ValueError
float_string = "123.45"
integer_value = int(float_string)
print(integer_value)
```

The `.` character is not a valid digit for an integer.

#### Solution: Convert to a `float` First

If you need to convert a string representation of a float to an integer, you must first convert it to a `float` and then to an `int`. This two-step process correctly truncates the decimal part.

```python
float_string = "123.45"
integer_value = 0

try:
    integer_value = int(float(float_string))
    print(f"Successfully converted: {integer_value}") # Output: 123
except ValueError:
    print(f"Conversion failed: '{float_string}' is not a valid number.")
```

### 3. The String Contains Leading/Trailing Whitespace

Sometimes, a string might contain hidden whitespace that prevents a successful conversion.

#### Problematic Code

```python
# This will raise a ValueError
number_string_with_space = " 123 "
# The spaces at the beginning and end are the problem
# Note: int() can handle this, but other functions might not.
# Let's assume a more complex case where whitespace is mixed in.
number_string_with_space = "123 45" 
integer_value = int(number_string_with_space)
```
*Correction*: The `int()` function in Python is smart enough to handle leading and trailing whitespace (e.g., `int(" 123 ")` works). However, it cannot handle whitespace *within* the number.

#### Solution: Use `str.strip()`

To be safe, especially before further validation, it's good practice to remove leading and trailing whitespace using the `str.strip()` method.

```python
number_string_with_space = " 123 "
cleaned_string = number_string_with_space.strip()
integer_value = int(cleaned_string) # This works reliably
print(integer_value)
```

### 4. Pre-validating with `str.isdigit()`

Before attempting a conversion, you can check if a string contains only digits. The `str.isdigit()` method is perfect for this, but it has a limitation: it returns `False` for negative numbers because of the `-` sign.

#### Example

```python
def safe_int_convert(text):
    # Remove whitespace first
    cleaned_text = text.strip()
    
    # Handle negative numbers by checking the string without the sign
    if cleaned_text.startswith('-') and cleaned_text[1:].isdigit():
        return int(cleaned_text)
    # Handle positive numbers
    elif cleaned_text.isdigit():
        return int(cleaned_text)
    else:
        print(f"Cannot convert '{text}' to an integer.")
        return None

print(safe_int_convert("123"))    # Output: 123
print(safe_int_convert("-45"))   # Output: -45
print(safe_int_convert("67a"))   # Output: Cannot convert '67a' to an integer. None
```

While this works, a `try-except` block is generally considered more "Pythonic" and is often more readable and efficient for handling such cases.

## Conclusion

The `ValueError: invalid literal for int() with base 10` is a clear signal to validate your input. The most robust and Pythonic way to handle potentially invalid string-to-integer conversions is with a `try-except ValueError` block. This ensures your program can handle unexpected input gracefully without crashing.
