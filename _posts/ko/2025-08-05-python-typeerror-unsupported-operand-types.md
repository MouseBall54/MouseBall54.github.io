---
typora-root-url: ../
layout: single
title: >
   Python TypeError: unsupported operand type(s) for + 오류 해결 방법
date: 2025-08-05T10:20:00+09:00
header:
   teaser: /images/header_images/overlay_image_python.png
   overlay_image: /images/header_images/overlay_image_python.png
   overlay_filter: 0.5
excerpt: >
   Python에서 호환되지 않는 타입으로 연산을 시도할 때 발생하는 TypeError: unsupported operand type(s) for + 오류를 해결하세요. 이 가이드는 숫자, 문자열 및 기타 객체에 대한 타입 변환을 처리하는 방법을 설명합니다.
categories:
   - ko_Troubleshooting
tags:
   - Python
   - TypeError
   - Data Types
   - Operators
   - Troubleshooting
---

## 서론

`TypeError: unsupported operand type(s) for +: '...' and '...'`는 새로운 Python 프로그래머들이 가장 흔하게 접하는 오류 중 하나입니다. 이 오류는 덧셈 연산자(`+`)를 호환되지 않는 타입의 두 객체에 사용하려고 할 때 발생합니다. 예를 들어, 숫자와 문자열 또는 리스트와 딕셔너리를 직접 더할 수 없습니다.

이 가이드에서는 이 `TypeError`가 발생하는 이유를 설명하고, 다양한 데이터 타입을 올바르게 처리하기 위한 명확한 해결책을 제공합니다.

## 이 `TypeError`의 원인은 무엇인가요?

Python은 강력한 타입 언어로, 대부분의 연산에서 데이터 타입을 자동으로 변환하지 않습니다. `+` 연산자는 피연산자의 타입에 따라 다르게 동작합니다.

-   **숫자**(int, float)의 경우: 수학적 덧셈을 수행합니다.
-   **문자열**의 경우: 연결(concatenation)을 수행합니다.
-   **리스트**의 경우: 연결을 수행합니다.
-   **튜플**의 경우: 연결을 수행합니다.

오류는 `+` 연산자에 대해 정의된 동작이 없는 타입을 혼합할 때 발생합니다.

**오류를 발생시키는 일반적인 예:**

1.  **문자열과 정수 더하기:**
    ```python
    age = 25
    message = "My age is " + age # TypeError 발생
    # TypeError: can only concatenate str (not "int") to str
    ```

2.  **리스트와 문자열 더하기:**
    ```python
    my_list = [1, 2, 3]
    my_string = "456"
    result = my_list + my_string # TypeError 발생
    # TypeError: can only concatenate list (not "str") to list
    ```

3.  **딕셔너리와 리스트 더하기:**
    ```python
    my_dict = {'a': 1}
    my_list = ['b', 2]
    result = my_dict + my_list # TypeError 발생
    # TypeError: unsupported operand type(s) for +: 'dict' and 'list'
    ```

## 오류 해결 방법

해결책은 항상 `+` 연산자를 사용하기 전에 피연산자가 호환되는 타입인지 확인하는 것입니다. 이는 보통 명시적인 타입 변환을 포함합니다.

### 1. 문자열 연결을 위한 변환

문자열을 숫자나 다른 객체와 결합하여 표시하려는 경우, `str()`을 사용하여 문자열이 아닌 객체를 문자열로 변환하세요.

**잘못된 코드:**
```python
age = 25
message = "I am " + age + " years old."
```

**올바른 코드:**
```python
age = 25
# 정수 'age'를 문자열로 변환
message = "I am " + str(age) + " years old."
print(message) # 출력: I am 25 years old.
```

문자열을 포맷하는 더 현대적이고 가독성 좋은 방법은 **f-string**(포맷된 문자열 리터럴)을 사용하는 것입니다. 이는 변환을 자동으로 처리합니다.

**모범 사례 (f-string):**
```python
age = 25
message = f"I am {age} years old."
print(message) # 출력: I am 25 years old.
```

### 2. 덧셈을 위한 숫자 변환

사용자 입력이나 파일로부터 숫자 데이터를 문자열로 받은 경우, 산술 연산을 수행하기 전에 숫자 타입(`int` 또는 `float`)으로 변환해야 합니다.

**잘못된 코드:**
```python
num1_str = "10"
num2_int = 20
result = num1_str + num2_int # TypeError 발생
```

**올바른 코드:**
```python
num1_str = "10"
num2_int = 20
# 문자열 'num1_str'을 정수로 변환
result = int(num1_str) + num2_int
print(result) # 출력: 30
```

문자열이 유효한 숫자가 아닐 경우 발생할 수 있는 `ValueError`를 처리해야 합니다.
```python
num_str = "hello"
try:
    num_int = int(num_str)
except ValueError:
    print(f"'{num_str}'는 정수로 변환할 수 없습니다.")
```

### 3. 다른 데이터 타입 처리

리스트나 딕셔너리와 같은 다른 데이터 타입으로 작업할 때, "덧셈"이 컨텍스트에서 무엇을 의미하는지 생각해야 합니다.

-   **리스트에 항목 추가**: `append()` 메서드나 다른 리스트와의 리스트 연결을 사용합니다.

    ```python
    my_list = [1, 2, 3]
    item_to_add = 4
    
    # 단일 항목 추가
    my_list.append(item_to_add)
    print(my_list) # 출력: [1, 2, 3, 4]
    
    # 다른 리스트와 연결
    another_list = [5, 6]
    combined_list = my_list + another_list
    print(combined_list) # 출력: [1, 2, 3, 4, 5, 6]
    ```

-   **딕셔너리에 "추가"**: 이는 보통 새로운 키-값 쌍으로 업데이트하는 것을 의미합니다. `update()` 메서드나 직접 할당을 사용합니다.

    ```python
    my_dict = {'a': 1}
    
    # 새로운 키-값 쌍 추가
    my_dict['b'] = 2
    
    # 다른 딕셔너리로 업데이트
    another_dict = {'c': 3, 'd': 4}
    my_dict.update(another_dict)
    
    print(my_dict) # 출력: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    ```

## 결론

`TypeError: unsupported operand type(s) for +`는 데이터 타입의 중요성을 강조하는 Python의 근본적인 오류입니다. 이를 해결하려면 명시적인 타입 변환을 수행하여 `+` 연산자를 호환되는 타입에만 사용하도록 해야 합니다. 문자열 연결에는 `str()`, 수학적 덧셈에는 `int()` 또는 `float()`, 다른 자료 구조에는 `append()`나 `update()`와 같은 적절한 메서드를 사용하세요. 문자열 포맷팅에 f-string을 채택하면 더 깨끗하고 오류 없는 코드를 작성하는 데 도움이 될 것입니다.
