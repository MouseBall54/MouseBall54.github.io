---
typora-root-url: ../
layout: single
title: "Python 'IndexError: list index out of range' 오류 해결 방법"

lang: ko
translation_id: python-indexerror-list-index-out-of-range
excerpt: "Python의 'IndexError: list index out of range' 오류의 원인과 해결책을 알아봅니다. 리스트 길이 확인, 올바른 반복문 사용 등 오류를 방지하는 방법을 확인하세요."
header:
   teaser: /images/header_images/overlay_image_python.png
   overlay_image: /images/header_images/overlay_image_python.png
   overlay_filter: 0.5
categories:
  - ko_Troubleshooting
tags:
  - Python
  - IndexError
  - List
  - Debugging
---

## `IndexError: list index out of range` 오류 이해하기

`IndexError: list index out of range`는 Python에서 흔히 발생하는 런타임 오류다. 이 오류는 리스트에 존재하지 않는 인덱스에 접근하려고 할 때 발생한다. 리스트는 0부터 시작하는 인덱스를 사용하므로, 첫 번째 요소는 인덱스 0에 있고 마지막 요소는 `n-1` 인덱스에 위치한다 (여기서 `n`은 리스트의 요소 개수다).

### 주요 원인

이 오류는 보통 다음과 같은 간단한 이유로 발생한다.

1.  **존재하지 않는 인덱스 접근**: 리스트 길이와 같거나 더 큰 인덱스를 요청하는 경우.
2.  **잘못된 반복문 범위 사용**: 리스트의 범위를 벗어나는 인덱스로 반복문을 실행하는 경우.
3.  **빈 리스트의 요소에 접근**: 항목이 없는 리스트에서 요소를 가져오려고 시도하는 경우.

### 오류 해결 방법

#### 1. 리스트 길이 확인하기

인덱스에 접근하기 전에 해당 인덱스가 유효한 범위 내에 있는지 확인해야 한다. `len()` 함수를 사용해 리스트의 길이를 확인할 수 있다.

**문제 코드:**
```python
my_list = [10, 20, 30]
print(my_list[3])  # IndexError 발생
```

**해결책:**
```python
my_list = [10, 20, 30]
index_to_access = 3

if index_to_access < len(my_list):
    print(my_list[index_to_access])
else:
    print(f"인덱스 {index_to_access}는 길이 {len(my_list)}의 리스트 범위를 벗어났습니다.")
```

#### 2. 안전한 반복문 습관 사용하기

인덱스를 사용하여 리스트를 순회할 때, 반복문의 범위가 올바른지 확인해야 한다. `range(len(my_list))`는 리스트의 인덱스를 안전하게 생성하는 방법이다.

**문제 코드:**
```python
my_list = [1, 2, 3, 4, 5]
# 이 반복문은 범위를 벗어난 인덱스 5에 접근하려고 시도한다.
for i in range(6):
    print(my_list[i])
```

**해결책:**
더 나은 접근 방식은 항목을 직접 순회하거나 `range(len(my_list))`를 사용하는 것이다.

```python
my_list = [1, 2, 3, 4, 5]

# 방법 1: 직접 순회 (권장)
for item in my_list:
    print(item)

# 방법 2: 인덱스로 순회
for i in range(len(my_list)):
    print(my_list[i])
```

#### 3. 빈 리스트 처리하기

리스트의 요소에 접근하기 전에 항상 리스트가 비어 있는지 확인해야 한다.

**문제 코드:**
```python
data = []
print(data[0])  # IndexError 발생
```

**해결책:**
```python
data = []
if data:  # 빈 리스트는 False로 평가된다.
    print(data[0])
else:
    print("리스트가 비어 있습니다.")
```

이러한 간단한 확인 절차를 따르면 `IndexError`를 예방하고 더 안정적인 Python 코드를 작성할 수 있다.
