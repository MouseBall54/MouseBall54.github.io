---
typora-root-url: ../
layout: single
title: "Python ZeroDivisionError: division by zero 해결 방법"

date: 2025-02-22T07:12:00+09:00
lang: ko
translation_id: python-zerodivisionerror-division-by-zero
excerpt: "나누기를 수행하기 전에 제수가 0인지 확인하여 Python의 'ZeroDivisionError: division by zero'를 예방합니다. 견고한 오류 처리를 위해 조건문과 try-except 블록을 사용하는 방법을 배웁니다."
seo_description: "나누기를 수행하기 전에 제수가 0인지 확인하여 Python의 'ZeroDivisionError: division by zero'를 예방합니다. 견고한 오류 처리를 위해 조건문과 try-except 블록을 사용하는 방법을 배웁니다."
header:
   teaser: /images/header_images/overlay_image_python.png
   overlay_image: /images/header_images/overlay_image_python.png
   overlay_filter: 0.5
   image_description: >
     이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Python ZeroDivisionError: division by zero 해결 방법
categories:
  - ko_Troubleshooting
tags:
  - Python
  - ZeroDivisionError
  - Exception Handling
  - Math
---


![이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Python ZeroDivisionError: division by zero 해결 방법](/images/header_images/overlay_image_python.png)
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

## 전문 보완 체크

**Python ZeroDivisionError: division by zero 해결 방법**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 인터프리터 경로, 가상환경, 패키지 버전, 입력 파일 또는 데이터 경계를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

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

독자가 **Python ZeroDivisionError: division by zero 해결 방법**의 첫 번째 권장 조치를 이미 시도했지만 결과가 여전히 불확실하다고 가정해 봅니다. 다음 단계는 여러 해결책을 한꺼번에 시험하는 것이 아니라 짧은 감사 기록을 만드는 것입니다. 먼저 어떤 판단을 하려는지 한 문장으로 쓰고, 환경을 한 문장으로 적고, 관찰된 결과를 한 문장으로 남깁니다. 그다음 인터프리터 경로, 가상환경, 패키지 버전, 입력 파일 또는 데이터 경계를 이미 확보한 사실과 대조합니다. 이렇게 해야 글이 서로 끊어진 팁 목록이 아니라 검증 가능한 절차가 됩니다.

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
