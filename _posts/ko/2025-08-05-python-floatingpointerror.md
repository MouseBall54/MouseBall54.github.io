typora-root-url: ../
layout: single
title: >
    Python FloatingPointError 해결 방법
seo_title: >
    Python FloatingPointError 해결 방법
date: 2025-08-05T21:00:00+09:00
header:
   teaser: /images/header_images/overlay_image_python.png
   overlay_image: /images/header_images/overlay_image_python.png
   overlay_filter: 0.5
excerpt: >
    Python에서 FloatingPointError는 부동 소수점 연산이 실패할 때 발생합니다. 이 오류는 일반적으로 잘 발생하지 않지만, 특정 수학적 계산에서 나타날 수 있습니다. 이 글에서는 FloatingPointError의 원인과 해결 방법을 알아봅니다.
seo_description: >
    Python에서 FloatingPointError는 부동 소수점 연산이 실패할 때 발생합니다. 이 오류는 일반적으로 잘 발생하지 않지만, 특정 수학적 계산에서 나타날 수 있습니다. 이 글에서는 FloatingPointError의 원인과 해결 방법을 알아봅니다.
categories:
  - ko_Troubleshooting
tags:
  - Python
  - FloatingPointError
  - Error
  - Exception
---

## 문제 상황

Python에서 부동 소수점 계산을 수행할 때 `FloatingPointError`가 발생할 수 있습니다.
이 오류는 흔하지 않습니다.
하지만 특정 조건에서 부동 소수점 연산이 정의되지 않은 결과를 낼 때 나타납니다.

예를 들어, 매우 큰 수를 다루거나 특정 라이브러리에서 부동 소수점 예외를 명시적으로 활성화한 경우 발생할 수 있습니다.

```python
import numpy as np

# 부동 소수점 오류를 활성화 (일반적인 경우는 아님)
np.seterr(all='raise')

a = np.float32(1e38)
b = np.float32(1e38)

try:
    # 오버플로로 인해 FloatingPointError 발생
    result = a * b
except FloatingPointError as e:
    print(f"오류 발생: {e}")
```

위 코드는 `numpy` 라이브러리를 사용하여 의도적으로 부동 소수점 오류를 발생시키는 예시입니다.
일반 Python 환경에서는 이 오류가 잘 나타나지 않습니다.
대신 `OverflowError`나 `Infinity`(`inf`) 같은 특별한 값을 반환합니다.

## 원인 분석

`FloatingPointError`의 주요 원인은 다음과 같습니다.

1.  **오버플로 (Overflow)**: 계산 결과가 부동 소수점 타입이 표현할 수 있는 최댓값을 초과할 때 발생합니다.
2.  **언더플로 (Underflow)**: 계산 결과가 0에 너무 가까워져 부동 소수점 타입이 표현할 수 있는 최소 정밀도보다 작아질 때 발생합니다.
3.  **유효하지 않은 연산 (Invalid Operation)**: `0/0`이나 무한대에 대한 잘못된 연산 등 수학적으로 정의되지 않은 계산을 수행할 때 발생합니다.

이 오류는 표준 Python에서는 잘 발생하지 않습니다.
`numpy`와 같은 수치 계산 라이브러리에서 `seterr` 함수를 통해 예외 발생을 강제했을 때 주로 나타납니다.

## 해결 방법

### 1. `try-except` 블록으로 예외 처리

가장 직접적인 방법은 `try-except` 블록을 사용하여 `FloatingPointError`를 처리하는 것입니다.
오류가 발생할 가능성이 있는 코드를 `try` 안에 넣고, `except` 블록에서 오류를 잡아냅니다.

```python
import numpy as np

np.seterr(all='raise')

a = np.float32(1e38)
b = np.float32(1e38)

try:
    result = a * b
    print("계산 성공")
except FloatingPointError:
    print("부동 소수점 오류가 발생했지만 처리했습니다.")
    # 오류 발생 시 대체 값(예: 0 또는 최댓값)을 사용
    result = np.inf
    print(f"대체 결과: {result}")
```

### 2. `decimal` 모듈 사용

더 높은 정밀도가 필요하거나 부동 소수점 오류를 피하고 싶을 때 `decimal` 모듈을 사용할 수 있습니다.
`decimal` 모듈은 고정 소수점 및 부동 소수점 산술을 위한 정확한 계산을 지원합니다.

```python
from decimal import Decimal, getcontext

# 정밀도 설정
getcontext().prec = 50

a = Decimal('1e38')
b = Decimal('1e38')

result = a * b
print(result)  # 1.0000000000000000000000000000000000000E+76
```

`decimal` 모듈은 일반적인 부동 소수점보다 속도는 느립니다.
하지만 금융 계산과 같이 정확성이 매우 중요한 경우에 유용합니다.

### 3. 입력 값 확인 및 제한

계산에 사용되는 입력 값이 너무 크거나 작지 않은지 확인하는 것도 좋은 방법입니다.
연산을 수행하기 전에 입력 값의 범위를 검사하여 잠재적인 오류를 미리 방지할 수 있습니다.

```python
import sys

def safe_multiply(a, b):
    # float의 최대값보다 큰 결과가 예상되면 처리하지 않음
    if a > sys.float_info.max / b:
        print("오버플로가 예상되어 계산을 중단합니다.")
        return None
    return a * b

result = safe_multiply(1e200, 1e200)
if result is not None:
    print(f"계산 결과: {result}")
```

## 결론

`FloatingPointError`는 표준 Python에서는 드물지만, `numpy`와 같은 라이브러리에서 정밀한 제어가 필요할 때 마주칠 수 있습니다.
`try-except`를 사용한 예외 처리, `decimal` 모듈을 통한 정밀 계산, 입력 값 검증 등의 방법을 통해 이 문제를 효과적으로 해결할 수 있습니다.
자신의 코드 환경과 요구사항에 맞는 해결책을 선택하는 것이 중요합니다.
