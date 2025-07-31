---
typora-root-url: ../
layout: single
title: "Python UnboundLocalError: local variable referenced before assignment 해결 방법"
date: 2025-07-31T14:30:00+09:00
excerpt: "변수 스코프를 이해하여 Python의 UnboundLocalError를 해결합니다. `global` 및 `nonlocal` 키워드를 사용하거나, 변수가 접근되기 전에 항상 함수 스코프 내에서 값이 할당되도록 하는 방법을 배웁니다."
categories:
  - ko_Troubleshooting
tags:
  - Python
  - UnboundLocalError
  - Scope
  - Exception Handling
---

## "UnboundLocalError: local variable '...' referenced before assignment"란?

`UnboundLocalError`는 Python에서 `NameError`의 특정 유형이다. 함수나 메서드 내에서 지역 변수에 값이 할당되기 *전에* 해당 변수에 접근하려고 할 때 발생한다.

이 오류는 같은 이름의 전역 변수가 있을 수 있기 때문에 혼란스러울 수 있다. 하지만 함수 내 어디에서든 변수에 값을 *할당*하면, Python은 해당 변수를 그 함수의 전체 스코프에 대해 지역 변수로 취급한다.

## 주요 원인과 해결 방법

이 오류를 유발하는 시나리오를 살펴보자.

### 1. 함수 내에서 전역 변수 수정

가장 흔한 원인은 Python에게 의도를 명시적으로 알리지 않고 전역 변수를 수정하려고 할 때다.

#### 문제 코드

```python
count = 0

def increment():
    # Python은 이 할당을 보고 'count'를 지역 변수로 간주한다.
    count = count + 1
    print(count)

# UnboundLocalError가 발생함
increment()
```

Python이 `increment` 함수를 컴파일할 때, `count = ...` 할당을 본다. 이는 Python에게 `count`가 지역 변수임을 알린다. 하지만 함수가 실행될 때, 지역 `count`에 값이 할당되기 *전에* 표현식의 오른쪽(`count + 1`)에서 `count`의 값을 읽으려고 시도한다. 전역 `count`는 무시되므로 오류가 발생한다.

#### 해결 방법: `global` 키워드 사용

함수 내에서 전역 변수를 수정하려면, `global` 키워드를 사용하여 의도를 선언해야 한다.

```python
count = 0

def increment():
    global count # Python에게 전역 'count'를 사용한다고 알림
    count = count + 1
    print(count)

increment() # 출력: 1
print(f"전역 count는 이제: {count}") # 출력: 전역 count는 이제: 1
```

### 2. 변수 할당이 조건부인 경우

변수가 조건부 블록(`if`, `for`, `try`) 내에서만 값이 할당되고, 해당 블록에 진입하지 않으면, 나중에 함수에서 해당 변수에 접근하려고 할 때 변수가 존재하지 않게 된다.

#### 문제 코드

```python
def get_status_message(status_code):
    if status_code == 200:
        message = "OK"
    
    # status_code가 200이 아니면 'message'는 할당되지 않음
    return f"상태: {message}"

# UnboundLocalError가 발생함
print(get_status_message(404))
```

`get_status_message(404)`가 호출되면, `if` 조건이 거짓이므로 `message = "OK"` 줄은 건너뛴다. 그런 다음 `return` 문은 지역 스코프에서 값이 할당되지 않은 `message`에 접근하려고 시도한다.

#### 해결 방법: 변수가 항상 할당되도록 보장

변수에 접근하기 전에 모든 가능한 실행 경로에서 값이 할당되도록 해야 한다. 일반적인 관행은 함수 시작 부분에서 기본값으로 초기화하는 것이다.

```python
def get_status_message(status_code):
    message = "알 수 없는 상태" # 기본값으로 초기화
    
    if status_code == 200:
        message = "OK"
    elif status_code == 404:
        message = "찾을 수 없음"
    
    return f"상태: {message}"

print(get_status_message(404)) # 출력: 상태: 찾을 수 없음
print(get_status_message(500)) # 출력: 상태: 알 수 없는 상태
```

### 3. 중첩 함수에서 변수 수정 (클로저)

비슷한 문제가 중첩 함수에서 바깥쪽(하지만 전역은 아닌) 스코프의 변수를 수정하려고 할 때 발생한다.

#### 문제 코드

```python
def outer_function():
    value = 10
    
    def inner_function():
        # Python은 할당 때문에 'value'를 inner_function의 지역 변수로 간주한다.
        value = value + 5
        print(value)
        
    inner_function()

# UnboundLocalError가 발생함
outer_function()
```

#### 해결 방법: `nonlocal` 키워드 사용

`nonlocal` 키워드(Python 3에서 도입)는 인터프리터에게 변수가 전역이 아닌 가장 가까운 바깥쪽 스코프에서 온 것임을 알려준다.

```python
def outer_function():
    value = 10
    
    def inner_function():
        nonlocal value # outer_function의 'value'를 사용
        value = value + 5
        print(f"내부 값: {value}")
        
    inner_function()
    print(f"외부 값: {value}")

outer_function()
# 출력:
# 내부 값: 15
# 외부 값: 15
```

## 결론

`UnboundLocalError`는 항상 스코프 관련 문제의 신호다. 이를 해결하려면 어떤 변수에 접근하려는지 명확히 해야 한다.
*   **전역 변수**를 수정하려는 경우, `global` 키워드를 사용한다.
*   **바깥쪽 함수의 스코프**에 있는 변수를 수정하려는 경우, `nonlocal` 키워드를 사용한다.
*   그렇지 않은 경우, **지역 변수**를 읽기 전에 모든 가능한 코드 경로에서 값이 할당되도록 보장해야 한다.
