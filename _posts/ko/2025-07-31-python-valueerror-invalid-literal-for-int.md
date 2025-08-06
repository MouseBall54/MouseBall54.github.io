---
typora-root-url: ../
layout: single
title: "Python ValueError: invalid literal for int() with base 10 해결 방법"

lang: ko
translation_id: python-valueerror-invalid-literal-for-int
excerpt: "변환하려는 문자열이 유효한 정수인지 확인하여 Python의 'ValueError: invalid literal for int()'를 해결합니다. 안전한 변환을 위해 try-except 블록을 사용하고, str.isdigit() 메서드로 유효성을 검사하는 법을 배웁니다."
header:
   teaser: /images/header_images/overlay_image_python.png
   overlay_image: /images/header_images/overlay_image_python.png
   overlay_filter: 0.5
categories:
  - ko_Troubleshooting
tags:
  - Python
  - ValueError
  - Type Conversion
  - Exception Handling
---

## "ValueError: invalid literal for int() with base 10"란?

이 `ValueError`는 특히 초보자에게 Python에서 가장 흔한 예외 중 하나다. `int()` 함수를 사용하여 문자열을 정수로 변환하려고 할 때, 해당 문자열의 내용이 10진수(표준 십진법)에서 유효한 숫자가 아닐 때 발생한다.

오류 메시지의 "literal"은 변환하려는 문자열 값을 의미한다. 본질적으로 Python은 "이 문자열을 정수로 어떻게 해석해야 할지 모르겠습니다"라고 말하는 것이다.

## 주요 원인과 해결 방법

이 오류가 발생하는 이유와 예방 방법을 살펴보자.

### 1. 문자열에 숫자가 아닌 문자가 포함된 경우

가장 직접적인 원인은 글자, 기호 또는 기타 숫자가 아닌 문자가 포함된 문자열을 변환하려고 할 때다.

#### 문제 코드

```python
# ValueError가 발생함
number_string = "123a"
integer_value = int(number_string)
print(integer_value)
```

Python은 `'a'` 문자가 숫자가 아니기 때문에 `"123a"`를 변환할 수 없다.

#### 해결 방법: `try-except` 블록 사용

문자열이 항상 유효한 숫자인지 확신할 수 없는 경우(예: 사용자 입력), 가장 안전한 접근 방식은 변환을 `try-except` 블록으로 감싸는 것이다. 이렇게 하면 프로그램이 충돌하는 대신 오류를 정상적으로 처리할 수 있다.

```python
number_string = "123a"
integer_value = 0 # 기본값

try:
    integer_value = int(number_string)
    print(f"성공적으로 변환됨: {integer_value}")
except ValueError:
    print(f"변환 실패: '{number_string}'는 유효한 정수가 아닙니다.")

# 프로그램은 계속 실행됨
print(f"현재 값: {integer_value}")
```

### 2. 문자열이 부동 소수점 숫자를 나타내는 경우

`int()` 함수는 부동 소수점 숫자(소수점이 있는 숫자)를 나타내는 문자열을 자동으로 처리하지 않는다.

#### 문제 코드

```python
# ValueError가 발생함
float_string = "123.45"
integer_value = int(float_string)
print(integer_value)
```

`.` 문자는 정수에 유효한 숫자가 아니다.

#### 해결 방법: 먼저 `float`으로 변환

부동 소수점의 문자열 표현을 정수로 변환해야 하는 경우, 먼저 `float`으로 변환한 다음 `int`로 변환해야 한다. 이 2단계 과정은 소수 부분을 올바르게 잘라낸다.

```python
float_string = "123.45"
integer_value = 0

try:
    integer_value = int(float(float_string))
    print(f"성공적으로 변환됨: {integer_value}") # 출력: 123
except ValueError:
    print(f"변환 실패: '{float_string}'는 유효한 숫자가 아닙니다.")
```

### 3. 문자열에 앞뒤 공백이 포함된 경우

때로는 문자열에 숨겨진 공백이 있어 성공적인 변환을 방해할 수 있다.

#### 문제 코드

```python
# ValueError가 발생함
number_string_with_space = " 123 "
# 시작과 끝의 공백이 문제임
# 참고: int()는 이를 처리할 수 있지만, 다른 함수는 그렇지 않을 수 있음
# 공백이 중간에 섞인 더 복잡한 경우를 가정
number_string_with_space = "123 45" 
integer_value = int(number_string_with_space)
```
*수정*: Python의 `int()` 함수는 앞뒤 공백을 처리할 만큼 똑똑하다(예: `int(" 123 ")`는 작동함). 하지만 숫자 *내부*의 공백은 처리할 수 없다.

#### 해결 방법: `str.strip()` 사용

특히 추가 유효성 검사 전에 안전을 기하기 위해 `str.strip()` 메서드를 사용하여 앞뒤 공백을 제거하는 것이 좋은 습관이다.

```python
number_string_with_space = " 123 "
cleaned_string = number_string_with_space.strip()
integer_value = int(cleaned_string) # 안정적으로 작동함
print(integer_value)
```

### 4. `str.isdigit()`로 사전 유효성 검사

변환을 시도하기 전에 문자열이 숫자로만 구성되어 있는지 확인할 수 있다. `str.isdigit()` 메서드는 이를 위해 완벽하지만, 음수 부호 `-` 때문에 음수에는 `False`를 반환하는 한계가 있다.

#### 예시

```python
def safe_int_convert(text):
    # 먼저 공백 제거
    cleaned_text = text.strip()
    
    # 부호를 제외한 문자열을 확인하여 음수 처리
    if cleaned_text.startswith('-') and cleaned_text[1:].isdigit():
        return int(cleaned_text)
    # 양수 처리
    elif cleaned_text.isdigit():
        return int(cleaned_text)
    else:
        print(f"'{text}'를 정수로 변환할 수 없습니다.")
        return None

print(safe_int_convert("123"))    # 출력: 123
print(safe_int_convert("-45"))   # 출력: -45
print(safe_int_convert("67a"))   # 출력: '67a'를 정수로 변환할 수 없습니다. None
```

이 방법도 작동하지만, `try-except` 블록이 일반적으로 더 "Pythonic"하다고 여겨지며, 이러한 경우를 처리하는 데 더 읽기 쉽고 효율적이다.

## 결론

`ValueError: invalid literal for int() with base 10`는 입력을 검증하라는 명확한 신호다. 잠재적으로 유효하지 않은 문자열-정수 변환을 처리하는 가장 견고하고 Pythonic한 방법은 `try-except ValueError` 블록을 사용하는 것이다. 이는 프로그램이 예기치 않은 입력을 충돌 없이 정상적으로 처리하도록 보장한다.
