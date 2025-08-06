---
typora-root-url: ../
layout: single
title: >
    파이썬 TypeError: '...' object is not iterable 해결 방법

lang: ko
translation_id: python-typeerror-object-is-not-iterable
header:
   teaser: /images/header_images/overlay_image_python.png
   overlay_image: /images/header_images/overlay_image_python.png
   overlay_filter: 0.5
excerpt: >
    파이썬에서 반복 불가능한(non-iterable) 객체를 순회하려고 할 때 발생하는 `TypeError: '...' object is not iterable` 오류의 원인과 해결 방법을 알아봅니다.
categories:
  - ko_Troubleshooting
tags:
  - Python
  - TypeError
  - Iterable
---

## 문제 상황

파이썬에서 `for` 루프나 `in` 연산자처럼 반복(iteration)을 기대하는 구문에서 반복할 수 없는(non-iterable) 객체를 사용하면 `TypeError: '...' object is not iterable` 오류가 발생합니다. 여기서 `'...'` 부분에는 해당 객체의 타입이 표시됩니다(예: `int`, `NoneType`).

**반복 가능한(Iterable)** 객체란 리스트, 튜플, 딕셔너리, 문자열처럼 여러 항목을 포함하고 있어 하나씩 순회할 수 있는 객체를 의미합니다. 반면, 숫자(정수, 실수)나 `None` 등은 단일 값이므로 반복할 수 없습니다.

## 오류 발생 코드 예시

### 1. 숫자를 순회하려는 경우

가장 흔한 예는 숫자를 직접 `for` 루프에 사용하는 경우입니다.

```python
# TypeError: 'int' object is not iterable
for i in 123:
    print(i)
```

`123`은 정수(`int`) 타입이며, 여러 항목으로 구성된 컬렉션이 아니므로 순회할 수 없습니다.

### 2. 함수가 반복 불가능한 값을 반환하는 경우

함수가 리스트나 튜플 대신 단일 값(예: `None` 또는 숫자)을 반환할 때도 이 오류가 발생할 수 있습니다.

```python
def get_data():
    # 데이터가 없는 경우 None을 반환
    return None

# data는 None이므로 순회할 수 없습니다.
# TypeError: 'NoneType' object is not iterable
data = get_data()
for item in data:
    print(item)
```

## 해결 방법

### 1. 객체가 반복 가능한지 확인하기

코드를 디버깅할 때, 순회하려는 변수가 어떤 값을 가지고 있는지 `print()` 함수나 디버거를 통해 확인하는 것이 중요합니다. 예상했던 리스트나 딕셔너리가 아니라 `None`이나 다른 단일 값일 수 있습니다.

```python
def get_data(condition):
    if condition:
        return ["apple", "banana"]
    # 데이터가 없는 경우 빈 리스트를 반환하도록 수정
    return []

data = get_data(False)
print(f"받아온 데이터: {data}") # 받아온 데이터: []

# 빈 리스트는 순회 가능하므로 오류가 발생하지 않습니다.
for item in data:
    print(item)
```

함수가 값을 반환하지 못하는 경우 `None` 대신 **빈 리스트(`[]`)나 빈 튜플(`()`)**을 반환하도록 수정하면 `TypeError`를 방지할 수 있습니다.

### 2. 단일 값을 리스트나 튜플로 감싸기

만약 순회하려는 값이 단일 객체인 것이 확실하지만 `for` 루프 구조를 유지하고 싶다면, 해당 값을 리스트나 튜플로 감싸서 반복 가능하게 만들 수 있습니다.

```python
my_variable = 123

# my_variable이 리스트가 아닐 경우 리스트로 만듭니다.
if not isinstance(my_variable, list):
    my_variable = [my_variable]

for item in my_variable:
    print(item)
# 출력: 123
```

### 3. `range()` 함수 사용하기

숫자 범위를 순회하고 싶었다면 `range()` 함수를 사용해야 합니다.

```python
# 0부터 4까지 순회
for i in range(5):
    print(i)
# 출력: 0, 1, 2, 3, 4
```

## 결론

`TypeError: '...' object is not iterable` 오류는 반복할 수 없는 객체에 `for` 루프와 같은 반복 구문을 사용했기 때문에 발생합니다. 이 문제를 해결하려면,

1.  순회하려는 변수가 **리스트, 튜플, 딕셔너리, 문자열** 등 반복 가능한 타입인지 확인합니다.
2.  함수가 값을 반환하지 않을 때 `None` 대신 **빈 리스트(`[]`)**를 반환하도록 설계합니다.
3.  의도적으로 단일 객체를 순회해야 한다면 **리스트(`[item]`)**로 감싸서 사용합니다.
4.  숫자 범위를 순회하려면 **`range()`** 함수를 사용합니다.

변수의 타입을 항상 염두에 두고 코드를 작성하는 습관이 중요합니다.
