---
typora-root-url: ../
layout: single
title: "Python TypeError: can only concatenate str (not 'int') to str 해결 방법"

lang: ko
translation_id: python-typeerror-can-only-concatenate-str-not-int-to-str
excerpt: "Python에서 'TypeError: can only concatenate str (not 'int') to str'는 문자열에 정수와 같은 다른 타입의 데이터를 직접 연결하려 할 때 발생합니다. 이 오류의 원인과 해결 방법을 알아봅니다."
header:
   teaser: /images/header_images/overlay_image_python.png
   overlay_image: /images/header_images/overlay_image_python.png
   overlay_filter: 0.5
categories:
  - ko_Troubleshooting
tags:
  - Python
  - TypeError
  - Troubleshooting
  - String
---

## 'TypeError: can only concatenate str (not "int") to str' 오류란?

이 `TypeError`는 Python에서 문자열(string)과 문자열이 아닌 다른 데이터 타입(예: 정수, 리스트)을 `+` 연산자로 연결하려고 할 때 발생하는 매우 흔한 오류다.
Python은 강력한 타입 검사를 수행하므로, 서로 다른 타입의 객체를 암시적으로 연결하는 것을 허용하지 않는다.
오류 메시지는 "문자열은 문자열하고만 연결할 수 있습니다 ('정수' 타입은 안 됩니다)"라는 의미를 명확히 전달한다.

## 주요 원인

이 오류의 원인은 단 하나다. `+` 연산자를 사용하여 문자열에 다른 타입의 변수나 값을 직접 붙이려고 시도하는 것이다.

```python
name = "사용자"
age = 25

# 오류 발생: 문자열(str)과 정수(int)를 직접 연결
message = "안녕하세요, " + name + "님. 나이는 " + age + "세입니다."
# TypeError: can only concatenate str (not "int") to str
```

위 코드에서 `age` 변수는 정수(`int`) 타입이다.
Python은 `"안녕하세요, 사용자님. 나이는 "`이라는 문자열에 정수 `25`를 직접 더할 수 없으므로 `TypeError`를 발생시킨다.

## 해결 방법

이 문제를 해결하기 위한 몇 가지 간단하고 효과적인 방법이 있다.

### 1. `str()` 함수로 명시적 형 변환

가장 기본적인 해결책은 다른 타입의 데이터를 `str()` 함수를 사용해 문자열로 명시적으로 변환하는 것이다.

```python
name = "사용자"
age = 25

# 정수 age를 str()을 사용해 문자열로 변환
message = "안녕하세요, " + name + "님. 나이는 " + str(age) + "세입니다."
print(message)
# 출력: 안녕하세요, 사용자님. 나이는 25세입니다.
```

`str(age)`는 정수 `25`를 문자열 `"25"`로 변환하므로, 모든 요소가 문자열이 되어 정상적으로 연결된다.

### 2. f-string (Formatted String Literals) 사용

Python 3.6 이상을 사용한다면 f-string이 가장 현대적이고 권장되는 방법이다.
문자열 앞에 `f`를 붙이고, 변수를 중괄호 `{}` 안에 직접 넣어주면 자동으로 문자열로 변환되어 편리하다.

```python
name = "사용자"
age = 25

# f-string을 사용하여 간결하게 문자열 포매팅
message = f"안녕하세요, {name}님. 나이는 {age}세입니다."
print(message)
# 출력: 안녕하세요, 사용자님. 나이는 25세입니다.
```

코드가 훨씬 간결하고 가독성이 높아진다.

### 3. `str.format()` 메서드 사용

f-string이 도입되기 전에는 `str.format()` 메서드가 주로 사용되었다.
문자열에 `{}` 플레이스홀더를 두고, `.format()` 메서드의 인자로 변수를 전달하는 방식이다.

```python
name = "사용자"
age = 25

# str.format() 메서드 사용
message = "안녕하세요, {}님. 나이는 {}세입니다.".format(name, age)
print(message)
# 출력: 안녕하세요, 사용자님. 나이는 25세입니다.
```

### 4. 쉼표(,)를 사용한 `print` 함수 출력

단순히 여러 값을 콘솔에 출력하는 것이 목적이라면, `print` 함수에서 쉼표로 구분하여 전달할 수 있다.
`print` 함수는 각 인자를 공백으로 구분하여 자동으로 출력해준다.

```python
name = "사용자"
age = 25

# print 함수에서 쉼표를 사용하면 각 타입이 자동으로 문자열로 변환되어 출력됨
print("안녕하세요,", name, "님. 나이는", age, "세입니다.")
# 출력: 안녕하세요, 사용자 님. 나이는 25 세입니다.
```
단, 이 방법은 변수들을 포함하는 단일 문자열을 만드는 것이 아니라, 단순히 여러 값을 출력만 할 때 유용하다.

## 결론

`TypeError: can only concatenate str (not "int") to str`는 다른 타입의 데이터를 문자열로 변환하지 않고 연결하려 할 때 발생한다.
이 문제를 해결하기 위해 `str()` 함수로 직접 형 변환하거나, f-string 또는 `str.format()` 같은 문자열 포매팅 기능을 사용하는 것이 좋다.
특히 f-string은 현대 파이썬에서 가장 간결하고 효율적인 방법이므로 적극적으로 활용하는 것을 권장한다.

```