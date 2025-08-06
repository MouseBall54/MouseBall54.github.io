---
typora-root-url: ../
layout: single
title: >
    Python "RecursionError: maximum recursion depth exceeded" 해결 방법

lang: ko
translation_id: python-recursion-error
header:
    teaser: /images/header_images/overlay_image_python.png
    overlay_image: /images/header_images/overlay_image_python.png
    overlay_filter: 0.5
excerpt: >
    Python에서 RecursionError는 재귀 호출의 깊이가 최대 한도를 초과할 때 발생합니다. 이 글에서는 오류의 원인과 해결 방법을 알아봅니다.
categories:
    - ko_Troubleshooting
tags:
    - Python
    - RecursionError
    - Recursion
---

## Python "RecursionError: maximum recursion depth exceeded"란?

`RecursionError`는 Python 인터프리터가 설정한 최대 재귀 깊이 한도를 초과하여 함수가 계속해서 자신을 호출할 때 발생하는 예외입니다. 이는 무한 재귀에 빠지거나, 재귀의 종료 조건이 잘못 설정되었을 때 주로 발생하며, 시스템의 스택 오버플로를 방지하기 위한 안전장치입니다.

## "RecursionError"의 일반적인 원인

1.  **종료 조건 부재**: 재귀 함수에 더 이상 자신을 호출하지 않고 값을 반환하는 기본 사례(base case)가 없는 경우, 함수는 무한정 자신을 호출하게 됩니다.
2.  **잘못된 종료 조건**: 종료 조건이 있지만, 논리적 오류로 인해 해당 조건이 절대 충족되지 않는 경우입니다.
3.  **매우 깊은 재귀**: 알고리즘 자체가 매우 깊은 재귀를 요구하는 경우, Python의 기본 재귀 한도를 초과할 수 있습니다.

## "RecursionError" 해결 방법

### 1. 종료 조건 확인 및 수정

가장 먼저 재귀 함수의 종료 조건이 올바르게 설정되어 있는지 확인해야 합니다. 모든 재귀 호출이 결국에는 종료 조건에 도달해야 합니다.

**잘못된 예 (종료 조건 없음):**
```python
def countdown(n):
    print(n)
    countdown(n - 1) # 종료 조건이 없어 무한 재귀 발생

# countdown(10) # RecursionError 발생
```

**올바른 예:**
```python
def countdown(n):
    if n < 0:
        return  # 종료 조건
    print(n)
    countdown(n - 1)

countdown(10)
```

### 2. 재귀 깊이 한도 늘리기

알고리즘이 정상적이지만 깊은 재귀가 꼭 필요한 경우, `sys` 모듈을 사용하여 재귀 한도를 늘릴 수 있습니다. 하지만 이 방법은 근본적인 해결책이 아닐 수 있으며, 메모리 문제를 유발할 수 있으므로 신중하게 사용해야 합니다.

```python
import sys

# 현재 재귀 한도 확인
print(sys.getrecursionlimit()) # 기본값은 보통 1000

# 재귀 한도 설정
sys.setrecursionlimit(2000)

def deep_recursion(n):
    if n == 0:
        return
    deep_recursion(n - 1)

deep_recursion(1500) # 정상 작동
```

### 3. 반복문으로 변경 (Iteration)

대부분의 재귀 함수는 반복문(for, while)을 사용하여 비재귀적인 형태로 변경할 수 있습니다. 이 방법이 메모리 사용 측면에서 더 효율적이고 `RecursionError`를 근본적으로 해결할 수 있습니다.

**재귀 예:**
```python
def factorial_recursive(n):
    if n == 1:
        return 1
    return n * factorial_recursive(n - 1)
```

**반복문 예:**
```python
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
```

## 결론

`RecursionError`는 대부분 재귀 함수의 종료 조건에 문제가 있을 때 발생합니다. 코드를 디버깅하여 종료 조건을 먼저 확인하고, 필요한 경우에만 재귀 깊이 한도를 조정하세요. 가장 좋은 해결책은 재귀적인 알고리즘을 반복적인 형태로 바꾸어 스택 깊이의 제약에서 벗어나는 것입니다.

