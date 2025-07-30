---
typora-root-url: ../
layout: single
title: "Python NameError: name '...' is not defined 오류 해결 방법"
date: 2025-07-30T22:00:00+09:00
excerpt: "변수나 함수가 정의되기 전에 사용될 때 발생하는 Python NameError의 원인과 해결 방법을 알아봅니다. 오타, 변수 범위 등 흔한 원인을 확인하세요."
categories:
  - ko_Troubleshooting
tags:
  - Python
  - NameError
  - 프로그래밍
  - 오류 처리
---

## `NameError: name '...' is not defined`란?

이 오류는 Python 인터프리터가 인식할 수 없는 이름(변수, 함수, 클래스 등)을 만났을 때 발생한다.
기본적으로, 아직 생성되거나 값이 할당되지 않은 것을 사용하려고 시도할 때 나타난다.
초보자들이 가장 흔하게 겪는 오류 중 하나이다.

## 흔한 원인과 해결 방법

`NameError`가 발생하는 일반적인 원인과 해결 방법을 살펴보자.

### 1. 변수 또는 함수 이름 오타

가장 빈번한 원인은 단순한 오타다. Python은 대소문자를 구분하므로 `myVariable`과 `myvariable`은 다르다.

**오류 예시:**
```python
message = "Hello, World!"
print(mesage)
```

**출력:**
```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'mesage' is not defined
```

**해결책:**
오타를 수정한다. 사용된 이름이 선언된 이름과 일치하는지 확인한다.

```python
message = "Hello, World!"
print(message) # 'mesage'를 'message'로 수정
```

### 2. 변수를 할당 전에 사용

변수는 사용하기 전에 반드시 값을 할당해야 한다.

**오류 예시:**
```python
if some_condition:
    user_name = "Alice"

print(user_name) # some_condition이 False이면 NameError 발생
```

**해결책:**
조건문 블록 앞에 변수를 기본값으로 초기화한다.

```python
user_name = "Guest" # 기본값으로 초기화
if some_condition:
    user_name = "Alice"

print(user_name)
```

### 3. 변수 범위(Scope) 문제

함수 내부에 정의된 변수(지역 변수)는 함수 밖에서 접근할 수 없다.

**오류 예시:**
```python
def greet():
    greeting = "함수 내부의 인사말!"
    print(greeting)

greet()
print(greeting) # 여기서 NameError 발생
```

**출력:**
```
함수 내부의 인사말!
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'greeting' is not defined
```

**해결책:**
함수 밖에서 값이 필요하다면, 함수에서 `return`하여 새로운 변수에 할당한다.

```python
def greet():
    greeting = "함수 내부의 인사말!"
    return greeting

returned_greeting = greet()
print(returned_greeting)
```

### 4. 모듈 또는 이름을 임포트하지 않음

표준 라이브러리나 서드파티 패키지의 모듈을 사용할 때는 먼저 임포트해야 한다.

**오류 예시:**
```python
# 'math' 모듈 임포트를 잊음
print(math.sqrt(25))
```

**출력:**
```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'math' is not defined
```

**해결책:**
스크립트 상단에 필요한 `import` 구문을 추가한다.

```python
import math

print(math.sqrt(25))
```

이러한 흔한 실수들을 확인하면 대부분의 `NameError` 예외를 빠르게 찾아 수정할 수 있다.
