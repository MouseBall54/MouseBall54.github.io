---
typora-root-url: ../
layout: single
title: "Python AttributeError: 'NoneType' object has no attribute '...' 해결 방법"
date: 2025-07-30T22:00:00+09:00
excerpt: "Python에서 자주 발생하는 오류인 AttributeError: 'NoneType' object has no attribute '...'의 원인을 파악하고 이를 방지하는 방법을 상세히 알아봅니다."
header:
   teaser: /images/header_images/overlay_image_python.png
   overlay_image: /images/header_images/overlay_image_python.png
   overlay_filter: 0.3
categories:
  - ko_Troubleshooting
tags:
  - Python
  - AttributeError
  - NoneType
  - Debugging
---

## `AttributeError: 'NoneType' object has no attribute '...'`란 무엇인가?

이 오류는 Python 개발자들이 가장 흔하게 마주하는 예외 중 하나다. 객체일 것으로 예상한 변수가 실제로는 `None`일 때, 그 변수의 메서드를 호출하거나 속성에 접근하려고 시도하면 발생한다.

`None`은 Python에서 값의 부재 또는 null 값을 나타내는 특별한 상수다. `None`은 그 자체로 `NoneType`이라는 타입을 가진 객체다. `NoneType` 객체에는 사용할 수 있는 속성이나 메서드가 전혀 없으므로, 여기에 `.append()`나 `.strip()` 같은 작업을 시도하면 `AttributeError`가 발생한다.

## 오류의 일반적인 원인

이 오류는 거의 항상 함수나 메서드가 예상된 값을 반환하지 못했음을 의미한다. 몇 가지 흔한 시나리오는 다음과 같다.

- **값을 명시적으로 반환하지 않는 함수:** 함수가 `return` 문 없이 종료되면, 암묵적으로 `None`을 반환한다.
- **특정 조건에서 `None`을 반환하는 함수:** 함수가 성공 시에는 유효한 객체를 반환하지만, 실패 시(예: 항목을 찾지 못한 경우)에는 `None`을 반환할 수 있다.
- **제자리(in-place) 연산:** 일부 메서드는 객체를 직접 수정하고 `None`을 반환한다. 대표적인 예가 `list.sort()`다.
- **딕셔너리의 `.get()` 메서드:** `my_dict.get(key)`를 기본값 없이 사용할 때, 키를 찾지 못하면 `None`을 반환한다.

오류를 발생시키는 예제는 다음과 같다.

```python
def get_user(user_id):
    # 이 사용자가 데이터베이스에 없다고 가정
    if user_id != 1:
        return None
    return {'name': 'Admin'}

user = get_user(2) # 이 함수 호출은 None을 반환

# 다음 줄에서 AttributeError가 발생
print(user['name']) 
```

이 코드는 `get_user(2)`가 `None`을 반환하고, 그 `None` 객체에서 `name` 키를 찾으려고 시도하기 때문에 오류가 발생한다.

## `AttributeError` 해결 방법

이 오류를 해결하는 핵심은 `None` 객체를 다루고 있지 않은지 확인하는 것이다.

### 1. 속성에 접근하기 전 `None` 확인

이 오류를 방지하는 가장 직접적인 방법은 변수를 사용하기 전에 `None`인지 확인하는 것이다.

```python
user = get_user(2)

if user is not None:
    print(user['name'])
else:
    print("사용자를 찾을 수 없습니다.")
```

이 간단한 조건문은 객체가 존재할 때만 속성에 접근하도록 보장한다.

### 2. 함수가 `None`을 반환하는 이유 파악

`None` 값의 출처를 조사해야 한다. 변수를 반환한 함수나 메서드를 살펴보자.

- 모든 가능한 경로에 `return` 문이 있는가?
- `None`을 반환하도록 설계된 조건이 있는가?
- `list.sort()`처럼 제자리에서 작동하는 메서드를 사용하고 그 반환값을 사용하려 하는가?

예를 들어, `list.sort()`는 리스트를 제자리에서 정렬하고 `None`을 반환한다.

```python
my_list = [3, 1, 2]

# 잘못된 방법: sorted_list는 None이 됨
sorted_list = my_list.sort() 

# 올바른 방법
my_list.sort()
sorted_list = my_list # 이제 sorted_list는 정렬된 리스트를 가리킴
```

원본 리스트를 수정하지 않고 새로운 정렬된 리스트를 얻으려면 `sorted()` 함수를 사용해야 한다.

```python
my_list = [3, 1, 2]
sorted_list = sorted(my_list) # 이 코드는 새로운 리스트를 반환하며 잘 작동함
```

### 3. 기본값 사용 또는 `try...except` 블록

변수가 `None`일 때 기본값으로 계속 진행해도 괜찮다면, 조건부 할당을 사용할 수 있다.

```python
user = get_user(2)
username = user['name'] if user is not None else 'Guest'
print(username)
```

또는 `try...except` 블록을 사용해 오류를 부드럽게 처리할 수도 있다. `AttributeError`에 대해 흔한 방법은 아니지만, `None` 값을 예외적인 경우로 간주한다면 유용할 수 있다.

```python
user = get_user(2)

try:
    print(user['name'])
except AttributeError:
    print("사용자 객체가 None이어서 사용자 이름을 가져올 수 없습니다.")
```

## 결론

`AttributeError: 'NoneType' object has no attribute '...'`는 코드의 논리적 결함을 알리는 런타임 오류다. 이 오류는 객체라고 생각했던 변수가 실제로는 `None`임을 알려준다. `None`을 확인하는 코드를 추가하고, 함수의 반환값을 이해하며, `None`인 경우를 명시적으로 처리함으로써 코드를 더 견고하게 만들고 이 흔한 오류가 프로그램을 중단시키는 것을 방지할 수 있다.
