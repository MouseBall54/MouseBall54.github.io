---
typora-root-url: ../
layout: single
title: >
   Python TypeError: unsupported operand type(s) for + 오류 해결 방법

date: 2025-04-23T07:27:00+09:00
lang: ko
translation_id: python-typeerror-unsupported-operand-types
header:
   teaser: /images/header_images/overlay_image_python.png
   overlay_image: /images/header_images/overlay_image_python.png
   overlay_filter: 0.5
   image_description: >
     이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Python TypeError: unsupported operand type(s) for + 오류 해결 방법
excerpt: >
   Python에서 호환되지 않는 타입으로 연산을 시도할 때 발생하는 TypeError: unsupported operand type(s) for + 오류를 해결하세요. 이 가이드는 숫자, 문자열 및 기타 객체에 대한 타입 변환을 처리하는 방법을 설명합니다.
seo_description: >
   Python에서 호환되지 않는 타입으로 연산을 시도할 때 발생하는 TypeError: unsupported operand type(s) for + 오류를 해결하세요. 이 가이드는 숫자, 문자열 및 기타 객체에 대한 타입 변환을 처리하는 방법을 설명합니다.
categories:
   - ko_Troubleshooting
tags:
   - Python
   - TypeError
   - Data Types
   - Operators
   - Troubleshooting
---


![이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Python TypeError: unsupported operand type(s) for + 오류 해결 방법](/images/header_images/overlay_image_python.png)
## 서론

`TypeError: unsupported operand type(s) for +: '...' and '...'`는 새로운 Python 프로그래머들이 가장 흔하게 접하는 오류 중 하나입니다. 이 오류는 덧셈 연산자(`+`)를 호환되지 않는 타입의 두 객체에 사용하려고 할 때 발생합니다. 예를 들어, 숫자와 문자열 또는 리스트와 딕셔너리를 직접 더할 수 없습니다.

이 가이드에서는 이 `TypeError`가 발생하는 이유를 설명하고, 다양한 데이터 타입을 올바르게 처리하기 위한 명확한 해결책을 제공합니다.

## 이 `TypeError`의 원인은 무엇인가요?

Python은 강력한 타입 언어로, 대부분의 연산에서 데이터 타입을 자동으로 변환하지 않습니다. `+` 연산자는 피연산자의 타입에 따라 다르게 동작합니다.

-   **숫자**(int, float)의 경우: 수학적 덧셈을 수행합니다.
-   **문자열**의 경우: 연결(concatenation)을 수행합니다.
-   **리스트**의 경우: 연결을 수행합니다.
-   **튜플**의 경우: 연결을 수행합니다.

오류는 `+` 연산자에 대해 정의된 동작이 없는 타입을 혼합할 때 발생합니다.

**오류를 발생시키는 일반적인 예:**

1.  **문자열과 정수 더하기:**
    ```python
    age = 25
    message = "My age is " + age # TypeError 발생
    # TypeError: can only concatenate str (not "int") to str
    ```

2.  **리스트와 문자열 더하기:**
    ```python
    my_list = [1, 2, 3]
    my_string = "456"
    result = my_list + my_string # TypeError 발생
    # TypeError: can only concatenate list (not "str") to list
    ```

3.  **딕셔너리와 리스트 더하기:**
    ```python
    my_dict = {'a': 1}
    my_list = ['b', 2]
    result = my_dict + my_list # TypeError 발생
    # TypeError: unsupported operand type(s) for +: 'dict' and 'list'
    ```

## 오류 해결 방법

해결책은 항상 `+` 연산자를 사용하기 전에 피연산자가 호환되는 타입인지 확인하는 것입니다. 이는 보통 명시적인 타입 변환을 포함합니다.

### 1. 문자열 연결을 위한 변환

문자열을 숫자나 다른 객체와 결합하여 표시하려는 경우, `str()`을 사용하여 문자열이 아닌 객체를 문자열로 변환하세요.

**잘못된 코드:**
```python
age = 25
message = "I am " + age + " years old."
```

**올바른 코드:**
```python
age = 25
# 정수 'age'를 문자열로 변환
message = "I am " + str(age) + " years old."
print(message) # 출력: I am 25 years old.
```

문자열을 포맷하는 더 현대적이고 가독성 좋은 방법은 **f-string**(포맷된 문자열 리터럴)을 사용하는 것입니다. 이는 변환을 자동으로 처리합니다.

**모범 사례 (f-string):**
```python
age = 25
message = f"I am {age} years old."
print(message) # 출력: I am 25 years old.
```

### 2. 덧셈을 위한 숫자 변환

사용자 입력이나 파일로부터 숫자 데이터를 문자열로 받은 경우, 산술 연산을 수행하기 전에 숫자 타입(`int` 또는 `float`)으로 변환해야 합니다.

**잘못된 코드:**
```python
num1_str = "10"
num2_int = 20
result = num1_str + num2_int # TypeError 발생
```

**올바른 코드:**
```python
num1_str = "10"
num2_int = 20
# 문자열 'num1_str'을 정수로 변환
result = int(num1_str) + num2_int
print(result) # 출력: 30
```

문자열이 유효한 숫자가 아닐 경우 발생할 수 있는 `ValueError`를 처리해야 합니다.
```python
num_str = "hello"
try:
    num_int = int(num_str)
except ValueError:
    print(f"'{num_str}'는 정수로 변환할 수 없습니다.")
```

### 3. 다른 데이터 타입 처리

리스트나 딕셔너리와 같은 다른 데이터 타입으로 작업할 때, "덧셈"이 컨텍스트에서 무엇을 의미하는지 생각해야 합니다.

-   **리스트에 항목 추가**: `append()` 메서드나 다른 리스트와의 리스트 연결을 사용합니다.

    ```python
    my_list = [1, 2, 3]
    item_to_add = 4
    
    # 단일 항목 추가
    my_list.append(item_to_add)
    print(my_list) # 출력: [1, 2, 3, 4]
    
    # 다른 리스트와 연결
    another_list = [5, 6]
    combined_list = my_list + another_list
    print(combined_list) # 출력: [1, 2, 3, 4, 5, 6]
    ```

-   **딕셔너리에 "추가"**: 이는 보통 새로운 키-값 쌍으로 업데이트하는 것을 의미합니다. `update()` 메서드나 직접 할당을 사용합니다.

    ```python
    my_dict = {'a': 1}
    
    # 새로운 키-값 쌍 추가
    my_dict['b'] = 2
    
    # 다른 딕셔너리로 업데이트
    another_dict = {'c': 3, 'd': 4}
    my_dict.update(another_dict)
    
    print(my_dict) # 출력: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    ```

## 결론

`TypeError: unsupported operand type(s) for +`는 데이터 타입의 중요성을 강조하는 Python의 근본적인 오류입니다. 이를 해결하려면 명시적인 타입 변환을 수행하여 `+` 연산자를 호환되는 타입에만 사용하도록 해야 합니다. 문자열 연결에는 `str()`, 수학적 덧셈에는 `int()` 또는 `float()`, 다른 자료 구조에는 `append()`나 `update()`와 같은 적절한 메서드를 사용하세요. 문자열 포맷팅에 f-string을 채택하면 더 깨끗하고 오류 없는 코드를 작성하는 데 도움이 될 것입니다.

## 전문 보완 체크

**Python TypeError: unsupported operand type(s) for + 오류 해결 방법**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 실행 환경, 정확한 오류 경계, 최소 재현 예제, 되돌릴 수 있는 경로를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

### 신뢰도를 높이는 증거

작업을 바꾸기 전에는 객관적인 증거를 먼저 확인해야 합니다. 쓸 만한 증거에는 전체 명령 출력, 버전 번호, 변경된 파일, 기대 동작과 실제 동작가 포함됩니다. 증거가 서로 맞지 않으면 억지로 하나의 이야기로 합치지 말고 충돌 자체를 남겨야 합니다. 빠른 해결이 한 번 성공했더라도 같은 입력, 계정, 의존성, 기기 상태에서 다시 확인하지 않았다면 아직 확정된 해결책이라고 보기 어렵습니다.

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

독자가 **Python TypeError: unsupported operand type(s) for + 오류 해결 방법**의 첫 번째 권장 조치를 이미 시도했지만 결과가 여전히 불확실하다고 가정해 봅니다. 다음 단계는 여러 해결책을 한꺼번에 시험하는 것이 아니라 짧은 감사 기록을 만드는 것입니다. 먼저 어떤 판단을 하려는지 한 문장으로 쓰고, 환경을 한 문장으로 적고, 관찰된 결과를 한 문장으로 남깁니다. 그다음 실행 환경, 정확한 오류 경계, 최소 재현 예제, 되돌릴 수 있는 경로를 이미 확보한 사실과 대조합니다. 이렇게 해야 글이 서로 끊어진 팁 목록이 아니라 검증 가능한 절차가 됩니다.

### 감사 기록 양식

| 항목 | 예시 기준 | 이유 |
| --- | --- | --- |
| 관찰 | 조치 전 실제로 본 내용 | 기준 상태를 객관화합니다 |
| 증거 | 전체 명령 출력, 버전 번호 | 판단을 기록에 연결합니다 |
| 가정 | 믿고 있지만 아직 증명하지 못한 내용 | 숨은 추정을 드러냅니다 |
| 조치 | 한 번에 하나의 변경 | 결과의 원인을 추적하게 합니다 |
| 중단 기준 | 멈추고 도움을 요청할 조건 | 반복적인 시행착오를 줄입니다 |

### 품질 경계

같은 결과가 통제된 재확인 뒤에도 반복될 때만 이 안내를 강한 결론으로 보아야 합니다. 계정, 기기, 데이터 샘플, 의존성 버전, 계약 조건, 공식 규칙이 달라졌다면 결론의 강도를 낮추고 가설로 다루는 편이 안전합니다. 검색 독자는 급한 문제를 안고 들어오는 경우가 많아 맥락을 건너뛰기 쉽습니다. 전문적인 글은 위험한 판단을 천천히 하게 만들면서도 다음 행동은 분명하게 제시해야 합니다.

## 함께 보면 좋은 글

같은 주제 흐름에서 이어서 읽기 좋은 글입니다.

- [SSL: CERTIFICATE_VERIFY_FAILED 오류 해결 방법 (Windows Python)](/ko_troubleshooting/python-certificate-verify-failed/)
- [Permission denied (publickey) 오류 해결 방법 (Windows Git SSH)](/ko_troubleshooting/git-permission-denied-publickey-windows/)
