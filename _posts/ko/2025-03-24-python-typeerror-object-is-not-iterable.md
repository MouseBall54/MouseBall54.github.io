---
typora-root-url: ../
layout: single
title: >
    파이썬 TypeError: '...' object is not iterable 해결 방법

date: 2025-03-24T07:42:00+09:00
lang: ko
translation_id: python-typeerror-object-is-not-iterable
header:
   teaser: /images/header_images/overlay_image_python.png
   overlay_image: /images/header_images/overlay_image_python.png
   overlay_filter: 0.5
   image_description: >
     이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: 파이썬 TypeError: '...' object is not iterable 해결 방법
excerpt: >
    파이썬에서 반복 불가능한(non-iterable) 객체를 순회하려고 할 때 발생하는 `TypeError: '...' object is not iterable` 오류의 원인과 해결 방법을 알아봅니다.
seo_description: >
    파이썬에서 반복 불가능한(non-iterable) 객체를 순회하려고 할 때 발생하는 `TypeError: '...' object is not iterable` 오류의 원인과 해결 방법을 알아봅니다.
categories:
  - ko_Troubleshooting
tags:
  - Python
  - TypeError
  - Iterable
---


![이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: 파이썬 TypeError: '...' object is not iterable 해결 방법](/images/header_images/overlay_image_python.png)
## 문제 상황

파이썬에서 `for` 루프나 `in` 연산자처럼 반복(iteration)을 기대하는 구문에서 반복할 수 없는(non-iterable) 객체를 사용하면 `TypeError: '...' object is not iterable` 오류가 발생합니다. 여기서 `'...'` 부분에는 해당 객체의 타입이 표시됩니다(예: `int`, `NoneType`).

**반복 가능한(Iterable)** 객체란 리스트, 튜플, 딕셔너리, 문자열처럼 여러 항목을 포함하고 있어 하나씩 순회할 수 있는 객체를 의미합니다. 반면, 숫자(정수, 실수)나 `None` 등은 단일 값이므로 반복할 수 없습니다.

## 오류 발생 코드 예시

### 1. 숫자를 순회하려는 경우

가장 흔한 예는 숫자를 직접 `for` 루프에 사용하는 경우입니다.

```python
# TypeError: 'int' object is not iterable
for i in 123:
    print(i)
```

`123`은 정수(`int`) 타입이며, 여러 항목으로 구성된 컬렉션이 아니므로 순회할 수 없습니다.

### 2. 함수가 반복 불가능한 값을 반환하는 경우

함수가 리스트나 튜플 대신 단일 값(예: `None` 또는 숫자)을 반환할 때도 이 오류가 발생할 수 있습니다.

```python
def get_data():
    # 데이터가 없는 경우 None을 반환
    return None

# data는 None이므로 순회할 수 없습니다.
# TypeError: 'NoneType' object is not iterable
data = get_data()
for item in data:
    print(item)
```

## 해결 방법

### 1. 객체가 반복 가능한지 확인하기

코드를 디버깅할 때, 순회하려는 변수가 어떤 값을 가지고 있는지 `print()` 함수나 디버거를 통해 확인하는 것이 중요합니다. 예상했던 리스트나 딕셔너리가 아니라 `None`이나 다른 단일 값일 수 있습니다.

```python
def get_data(condition):
    if condition:
        return ["apple", "banana"]
    # 데이터가 없는 경우 빈 리스트를 반환하도록 수정
    return []

data = get_data(False)
print(f"받아온 데이터: {data}") # 받아온 데이터: []

# 빈 리스트는 순회 가능하므로 오류가 발생하지 않습니다.
for item in data:
    print(item)
```

함수가 값을 반환하지 못하는 경우 `None` 대신 **빈 리스트(`[]`)나 빈 튜플(`()`)**을 반환하도록 수정하면 `TypeError`를 방지할 수 있습니다.

### 2. 단일 값을 리스트나 튜플로 감싸기

만약 순회하려는 값이 단일 객체인 것이 확실하지만 `for` 루프 구조를 유지하고 싶다면, 해당 값을 리스트나 튜플로 감싸서 반복 가능하게 만들 수 있습니다.

```python
my_variable = 123

# my_variable이 리스트가 아닐 경우 리스트로 만듭니다.
if not isinstance(my_variable, list):
    my_variable = [my_variable]

for item in my_variable:
    print(item)
# 출력: 123
```

### 3. `range()` 함수 사용하기

숫자 범위를 순회하고 싶었다면 `range()` 함수를 사용해야 합니다.

```python
# 0부터 4까지 순회
for i in range(5):
    print(i)
# 출력: 0, 1, 2, 3, 4
```

## 결론

`TypeError: '...' object is not iterable` 오류는 반복할 수 없는 객체에 `for` 루프와 같은 반복 구문을 사용했기 때문에 발생합니다. 이 문제를 해결하려면,

1.  순회하려는 변수가 **리스트, 튜플, 딕셔너리, 문자열** 등 반복 가능한 타입인지 확인합니다.
2.  함수가 값을 반환하지 않을 때 `None` 대신 **빈 리스트(`[]`)**를 반환하도록 설계합니다.
3.  의도적으로 단일 객체를 순회해야 한다면 **리스트(`[item]`)**로 감싸서 사용합니다.
4.  숫자 범위를 순회하려면 **`range()`** 함수를 사용합니다.

변수의 타입을 항상 염두에 두고 코드를 작성하는 습관이 중요합니다.

## 전문 보완 체크

**파이썬 TypeError: '...' object is not iterable 해결 방법**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 인터프리터 경로, 가상환경, 패키지 버전, 입력 파일 또는 데이터 경계를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

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

독자가 **파이썬 TypeError: '...' object is not iterable 해결 방법**의 첫 번째 권장 조치를 이미 시도했지만 결과가 여전히 불확실하다고 가정해 봅니다. 다음 단계는 여러 해결책을 한꺼번에 시험하는 것이 아니라 짧은 감사 기록을 만드는 것입니다. 먼저 어떤 판단을 하려는지 한 문장으로 쓰고, 환경을 한 문장으로 적고, 관찰된 결과를 한 문장으로 남깁니다. 그다음 인터프리터 경로, 가상환경, 패키지 버전, 입력 파일 또는 데이터 경계를 이미 확보한 사실과 대조합니다. 이렇게 해야 글이 서로 끊어진 팁 목록이 아니라 검증 가능한 절차가 됩니다.

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
