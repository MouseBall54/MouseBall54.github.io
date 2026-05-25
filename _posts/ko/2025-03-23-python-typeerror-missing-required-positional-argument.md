---
typora-root-url: ../
layout: single
title: >
    파이썬 TypeError: missing 1 required positional argument 해결 방법

date: 2025-03-23T07:41:00+09:00
lang: ko
translation_id: python-typeerror-missing-required-positional-argument
header:
   teaser: /images/header_images/overlay_image_python.png
   overlay_image: /images/header_images/overlay_image_python.png
   overlay_filter: 0.5
   image_description: >
     이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: 파이썬 TypeError: missing 1 required positional argument 해결 방법
excerpt: >
    파이썬에서 함수나 메서드를 호출할 때 필수적인 위치 인자(positional argument)를 전달하지 않아 발생하는 `TypeError: missing 1 required positional argument` 오류의 원인과 해결책을 알아봅니다.
seo_description: >
    파이썬에서 함수나 메서드를 호출할 때 필수적인 위치 인자(positional argument)를 전달하지 않아 발생하는 `TypeError: missing 1 required positional argument` 오류의 원인과 해결책을 알아봅니다.
categories:
  - ko_Troubleshooting
tags:
  - Python
  - TypeError
  - Argument
  - Function Call
---


![이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: 파이썬 TypeError: missing 1 required positional argument 해결 방법](/images/header_images/overlay_image_python.png)
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

## 전문 보완 체크

**파이썬 TypeError: missing 1 required positional argument 해결 방법**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 인터프리터 경로, 가상환경, 패키지 버전, 입력 파일 또는 데이터 경계를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

### 신뢰도를 높이는 증거

작업을 바꾸기 전에는 객관적인 증거를 먼저 확인해야 합니다. 쓸 만한 증거에는 `python --version`, `python -m pip show`, 전체 traceback, 최소 재현 스크립트가 포함됩니다. 증거가 서로 맞지 않으면 억지로 하나의 이야기로 합치지 말고 충돌 자체를 남겨야 합니다. 빠른 해결이 한 번 성공했더라도 같은 입력, 계정, 의존성, 기기 상태에서 다시 확인하지 않았다면 아직 확정된 해결책이라고 보기 어렵습니다.

### 검토 표

| 검토 항목 | 확인할 내용 | 중요한 이유 |
| --- | --- | --- |
| 범위 | 이 글이 다루는 정확한 사례 | 조언을 과도하게 적용하지 않게 합니다 |
| 기준 상태 | 변경 전 상태 | 되돌리기와 비교를 가능하게 합니다 |
| 변경 | 실제로 수행한 가장 작은 조치 | 숨은 부작용을 줄입니다 |
| 결과 | 변경 뒤 관찰한 출력 또는 반응 | 기대와 증거를 구분합니다 |
| 재확인 | 결론을 다시 볼 시점 | 글의 정확도를 유지합니다 |

### 예외 상황과 실패 모드

주요 위험은 증상만 고치고 원인을 남기는 상황, 서로 무관한 변경을 같은 테스트에 섞는 상황입니다. 생산 데이터, 개인정보, 돈, 건강, 법적 권리, 보안 복구가 관련되어 있다면 넓은 해결책을 바로 적용하기보다 먼저 증거를 모으는 보수적인 접근이 낫습니다. 같은 제목의 문제라도 환경이 다르면 원인이 달라질 수 있으므로, 독자는 명령이나 결정을 복사하기 전에 자신의 조건이 글의 가정과 맞는지 비교해야 합니다.

### 유지보수 기준

이 안내는 의존성, 운영체제, 빌드 도구가 바뀐 뒤 다시 확인해야 합니다. 좋은 업데이트는 글 전체를 다시 쓰는 것이 아니라 예시, 링크, 명령, 화면, 판단 기준이 현재 동작과 여전히 맞는지 확인하는 일입니다. 기존 결론이 유효하면 확인 날짜를 남기고, 바뀌었다면 무엇이 바뀌었고 왜 이전 조언만으로 부족한지 설명해야 합니다.

### 실행 전 질문

- 문제나 판단이 실제임을 보여 주는 가장 작은 관찰 신호는 무엇인가?
- 공식 출처는 무엇이고, 내부 판단은 어느 부분인가?
- 변경 전에 반드시 캡처해야 할 기록은 무엇인가?
- 어떤 결과가 나오면 이 글의 조언이 맞지 않는다고 볼 것인가?
- 같은 문제가 반복될 때 누가 이 기록을 다시 봐야 하는가?

## 적용 검토 시나리오

독자가 **파이썬 TypeError: missing 1 required positional argument 해결 방법**의 첫 번째 권장 조치를 이미 시도했지만 결과가 여전히 불확실하다고 가정해 봅니다. 다음 단계는 여러 해결책을 한꺼번에 시험하는 것이 아니라 짧은 감사 기록을 만드는 것입니다. 먼저 어떤 판단을 하려는지 한 문장으로 쓰고, 환경을 한 문장으로 적고, 관찰된 결과를 한 문장으로 남깁니다. 그다음 인터프리터 경로, 가상환경, 패키지 버전, 입력 파일 또는 데이터 경계를 이미 확보한 사실과 대조합니다. 이렇게 해야 글이 서로 끊어진 팁 목록이 아니라 검증 가능한 절차가 됩니다.

### 감사 기록 양식

| 항목 | 예시 기준 | 이유 |
| --- | --- | --- |
| 관찰 | 조치 전 실제로 본 내용 | 기준 상태를 객관화합니다 |
| 증거 | `python --version`, `python -m pip show` | 판단을 기록에 연결합니다 |
| 가정 | 믿고 있지만 아직 증명하지 못한 내용 | 숨은 추정을 드러냅니다 |
| 조치 | 한 번에 하나의 변경 | 결과의 원인을 추적하게 합니다 |
| 중단 기준 | 멈추고 도움을 요청할 조건 | 반복적인 시행착오를 줄입니다 |

### 품질 경계

같은 결과가 통제된 재확인 뒤에도 반복될 때만 이 안내를 강한 결론으로 보아야 합니다. 계정, 기기, 데이터 샘플, 의존성 버전, 계약 조건, 공식 규칙이 달라졌다면 결론의 강도를 낮추고 가설로 다루는 편이 안전합니다. 검색 독자는 급한 문제를 안고 들어오는 경우가 많아 맥락을 건너뛰기 쉽습니다. 전문적인 글은 위험한 판단을 천천히 하게 만들면서도 다음 행동은 분명하게 제시해야 합니다.

## 함께 보면 좋은 글

같은 주제 흐름에서 이어서 읽기 좋은 글입니다.

- [SSL: CERTIFICATE_VERIFY_FAILED 오류 해결 방법 (Windows Python)](/ko_troubleshooting/python-certificate-verify-failed/)
- [Permission denied (publickey) 오류 해결 방법 (Windows Git SSH)](/ko_troubleshooting/git-permission-denied-publickey-windows/)
