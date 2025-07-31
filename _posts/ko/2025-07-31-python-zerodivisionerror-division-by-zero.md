---
typora-root-url: ../
layout: single
title: "Python ZeroDivisionError: division by zero 해결 방법"
date: 2025-07-31T14:15:00+09:00
excerpt: "나누기를 수행하기 전에 제수가 0인지 확인하여 Python의 'ZeroDivisionError: division by zero'를 예방합니다. 견고한 오류 처리를 위해 조건문과 try-except 블록을 사용하는 방법을 배웁니다."
header:
   teaser: /images/header_images/overlay_image_python.png
   overlay_image: /images/header_images/overlay_image_python.png
   overlay_filter: 0.5
categories:
  - ko_Troubleshooting
tags:
  - Python
  - ZeroDivisionError
  - Exception Handling
  - Math
---

## "ZeroDivisionError: division by zero"란?

`ZeroDivisionError`는 Python에서 직관적이고 흔한 런타임 오류다. 숫자를 0으로 나누려고 시도할 때 발생한다. 수학에서 0으로 나누는 것은 정의되지 않으며, 대부분의 프로그래밍 언어와 마찬가지로 Python도 이 불법적인 연산이 발생했음을 알리기 위해 예외를 발생시킨다.

이 오류는 표준 나눗셈 (`/`)과 정수 나눗셈 (`//`) 모두에서 발생할 수 있다.

## 주요 원인과 해결 방법

이 오류의 원인은 단 하나, 제수가 0이라는 것이다. 문제는 보통 그 제수가 *어떻게* 0이 되었는지를 파악하는 것이다.

### 1. 0으로 직접 나누기

가장 명백한 경우로, 숫자 0을 직접 제수로 사용하는 경우다.

#### 문제 코드

```python
numerator = 10
denominator = 0

# ZeroDivisionError가 발생함
result = numerator / denominator
print(result)
```

#### 해결 방법: 나누기 전에 제수 확인

이 오류를 예방하는 근본적인 방법은 나누기를 수행하기 *전에* 분모가 0인지 확인하는 것이다. `if` 문은 이를 위한 완벽한 도구다.

```python
numerator = 10
denominator = 0
result = 0 # 기본값 할당

if denominator != 0:
    result = numerator / denominator
else:
    print("오류: 0으로 나눌 수 없습니다.")
    # 오류를 적절히 처리, 예: 기본값 설정 또는 계산 건너뛰기

print(f"결과: {result}")
```

### 2. 변수가 예기치 않게 0이 되는 경우

더 자주 발생하는 경우는 제수로 사용된 변수가 프로그램 실행 중에 계산이나 외부 입력으로 인해 0이 되는 경우다.

#### 문제 시나리오

평균 점수를 계산하는 함수가 있지만, 점수 목록이 비어 있을 수 있다고 상상해보자.

```python
def calculate_average(scores):
    # scores가 비어 있으면 len(scores)는 0이 됨
    return sum(scores) / len(scores)

# ZeroDivisionError가 발생함
average = calculate_average([])
print(average)
```

여기서 `len(scores)`는 `0`으로 평가되어 나눗셈이 실패한다.

#### 해결 방법: 정상적인 처리를 위한 `try-except` 블록 사용

제수의 값이 불확실할 때, `try-except` 블록은 프로그램을 중단시키지 않고 잠재적인 오류를 처리하는 훌륭한 방법이다. 이는 특히 복잡한 코드에서 여러 `if` 검사를 하는 것보다 종종 더 깔끔하다.

```python
def calculate_average(scores):
    try:
        return sum(scores) / len(scores)
    except ZeroDivisionError:
        print("오류: 점수 목록이 비어 있어 평균을 계산할 수 없습니다.")
        return 0 # 합리적인 기본값 반환

average = calculate_average([])
print(f"평균: {average}") # 출력: 평균: 0
```

이 접근 방식은 오류가 발생할 때만 잡아내어 프로그램이 계속 실행되도록 하므로 견고하다.

### 3. 외부 소스로부터의 데이터

파일, 데이터베이스 또는 사용자 입력에서 데이터를 읽을 때, 예상치 못한 곳에서 0 값을 받을 수 있다.

#### 문제 코드

```python
# 사용자가 '0'을 입력할 수 있음
user_input = input("분배할 사람 수를 입력하세요: ")
items_per_person = 100 / int(user_input)
print(items_per_person)
```

사용자가 `0`을 입력하면 프로그램은 `ZeroDivisionError`와 함께 충돌할 것이다. (숫자가 아닌 텍스트를 입력하면 `ValueError`로도 충돌하므로, 검사를 결합하는 것이 중요하다).

#### 해결 방법: 유효성 검사와 오류 처리 결합

외부 입력의 경우, 데이터를 검증하고 예외를 처리해야 한다.

```python
user_input = input("분배할 사람 수를 입력하세요: ")
items_per_person = None

try:
    num_people = int(user_input)
    if num_people == 0:
        print("오류: 사람 수는 0이 될 수 없습니다.")
    else:
        items_per_person = 100 / num_people
        print(f"각 사람에게 {items_per_person}개의 아이템이 돌아갑니다.")

except ValueError:
    print("오류: 유효한 정수를 입력하세요.")
except ZeroDivisionError: 
    # if 검사가 있다면 중복되지만, 좋은 예비책이 됨
    print("오류: 0으로 나눌 수 없습니다.")
```
`try-except` 블록을 사용한 더 간결한 방법:
```python
try:
    num_people = int(user_input)
    items_per_person = 100 / num_people
    print(f"각 사람에게 {items_per_person}개의 아이템이 돌아갑니다.")
except ValueError:
    print("오류: 유효한 정수를 입력하세요.")
except ZeroDivisionError:
    print("오류: 사람 수는 0이 될 수 없습니다.")
```

## 결론

`ZeroDivisionError`는 이해하기 쉽지만 예방을 위해 방어적인 프로그래밍이 필요하다. 특히 변수, 계산 또는 외부 데이터를 다룰 때는 항상 0인 제수의 가능성을 예상해야 한다. 직접적인 검사를 위해서는 간단한 조건부 `if` 문을 사용하고, 더 견고하고 안전한 오류 처리를 위해서는 `try-except` 블록을 사용하자.
