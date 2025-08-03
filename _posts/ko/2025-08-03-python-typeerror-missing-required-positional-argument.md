---
typora-root-url: ../
layout: single
title: >
    파이썬 TypeError: missing 1 required positional argument 해결 방법
date: 2025-08-03T11:20:00+09:00
header:
   teaser: /images/header_images/overlay_image_python.png
   overlay_image: /images/header_images/overlay_image_python.png
   overlay_filter: 0.5
excerpt: >
    파이썬에서 함수나 메서드를 호출할 때 필수적인 위치 인자(positional argument)를 전달하지 않아 발생하는 `TypeError: missing 1 required positional argument` 오류의 원인과 해결책을 알아봅니다.
categories:
  - ko_Troubleshooting
tags:
  - Python
  - TypeError
  - Argument
  - Function Call
---

## 문제 상황

파이썬에서 함수나 클래스의 메서드를 호출할 때 `TypeError: missing 1 required positional argument: '...'` 와 같은 오류가 발생하는 경우가 있습니다. 이 오류는 함수(또는 메서드)가 필요로 하는 **필수 위치 인자(positional argument)가 호출 시에 전달되지 않았다**는 것을 의미합니다.

오류 메시지의 마지막 `'...'` 부분에는 누락된 인자의 이름이 표시되어 어떤 값이 빠졌는지 알려줍니다.

## 오류 발생 코드 예시

### 1. 일반 함수 호출 시 인자 누락

`greet` 함수는 `name`이라는 하나의 위치 인자를 필요로 하지만, 아무런 인자 없이 호출했습니다.

```python
def greet(name):
    print(f"Hello, {name}!")

# 함수 호출 시 'name' 인자를 전달하지 않았습니다.
greet() 
# TypeError: greet() missing 1 required positional argument: 'name'
```

### 2. 클래스 메서드 호출 시 인스턴스 문제

클래스의 인스턴스 메서드를 호출할 때 이 오류가 발생한다면, 대부분의 경우 메서드가 인스턴스 자체(`self`)를 첫 번째 인자로 받아야 하는데, 이를 클래스에서 직접 호출하려고 할 때 발생합니다.

```python
class Calculator:
    # 'self'는 인스턴스 자신을 가리키는 필수 위치 인자입니다.
    def add(self, x, y):
        return x + y

# 인스턴스를 생성하지 않고 클래스에서 직접 메서드를 호출합니다.
# 이 경우 'self'에 해당하는 인스턴스가 전달되지 않습니다.
result = Calculator.add(5, 10)
# TypeError: Calculator.add() missing 1 required positional argument: 'self'
```

파이썬에서 `instance.method(arg1, arg2)`는 내부적으로 `ClassName.method(instance, arg1, arg2)`와 같이 동작합니다. 따라서 클래스에서 직접 메서드를 호출하면 첫 번째 인자인 `self`가 누락되는 것입니다.

## 해결 방법

### 1. 함수에 필요한 모든 인자 전달하기

가장 간단한 해결책은 함수를 호출할 때 정의된 모든 필수 인자를 정확하게 전달하는 것입니다.

```python
def greet(name):
    print(f"Hello, {name}!")

# 'name' 인자에 값을 전달합니다.
greet("Alice")
# 출력: Hello, Alice!
```

### 2. 인자에 기본값(Default Value) 설정하기

만약 특정 인자가 항상 필요하지는 않다면, 함수를 정의할 때 기본값을 설정하여 선택적(optional)으로 만들 수 있습니다.

```python
# 'name' 인자에 기본값 "Guest"를 설정합니다.
def greet(name="Guest"):
    print(f"Hello, {name}!")

# 인자 없이 호출해도 기본값이 사용되므로 오류가 발생하지 않습니다.
greet()
# 출력: Hello, Guest!

greet("Bob")
# 출력: Hello, Bob!
```

### 3. 클래스의 인스턴스를 통해 메서드 호출하기

클래스 메서드 관련 오류인 경우, 클래스의 인스턴스를 먼저 생성한 다음, 그 인스턴스를 통해 메서드를 호출해야 합니다.

```python
class Calculator:
    def add(self, x, y):
        return x + y

# 1. Calculator 클래스의 인스턴스를 생성합니다.
calc_instance = Calculator()

# 2. 생성된 인스턴스를 통해 메서드를 호출합니다.
# 이 때 'self'는 자동으로 전달됩니다.
result = calc_instance.add(5, 10)

print(result)
# 출력: 15
```

만약 인스턴스 없이 클래스 자체에서 직접 호출해야 하는 메서드라면, `@staticmethod` 데코레이터를 사용하여 정적 메서드로 만들 수 있습니다. 정적 메서드는 `self` 인자를 필요로 하지 않습니다.

```python
class Calculator:
    @staticmethod
    def add(x, y): # 정적 메서드는 'self'가 없습니다.
        return x + y

# 인스턴스 생성 없이 클래스에서 직접 호출 가능
result = Calculator.add(5, 10)
print(result)
# 출력: 15
```

## 결론

`TypeError: missing 1 required positional argument` 오류는 함수 호출의 기본을 지키지 않았을 때 발생합니다. 이 오류를 해결하려면,

1.  함수 호출 시 **필요한 모든 인자를 전달**했는지 확인합니다.
2.  필요에 따라 함수 정의 시 **인자에 기본값**을 설정합니다.
3.  클래스 메서드의 경우, **인스턴스를 생성한 후 메서드를 호출**하거나, `self`가 필요 없다면 **`@staticmethod`**를 사용합니다.

오류 메시지가 어떤 인자가 누락되었는지 알려주므로, 해당 함수나 메서드의 정의를 확인하는 것이 디버깅의 첫걸음입니다.
