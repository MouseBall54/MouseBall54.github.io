---
typora-root-url: ../
layout: single
title: "Python UnboundLocalError: local variable referenced before assignment 해결 방법"

date: 2025-02-20T07:10:00+09:00
lang: ko
translation_id: python-unboundlocalerror-local-variable-referenced-before-assignment
excerpt: "변수 스코프를 이해하여 Python의 UnboundLocalError를 해결합니다. `global` 및 `nonlocal` 키워드를 사용하거나, 변수가 접근되기 전에 항상 함수 스코프 내에서 값이 할당되도록 하는 방법을 배웁니다."
seo_description: "변수 스코프를 이해하여 Python의 UnboundLocalError를 해결합니다. `global` 및 `nonlocal` 키워드를 사용하거나, 변수가 접근되기 전에 항상 함수 스코프 내에서 값이 할당되도록 하는 방법을 배웁니다."
header:
   teaser: /images/header_images/overlay_image_python.png
   overlay_image: /images/header_images/overlay_image_python.png
   overlay_filter: 0.5
   image_description: >
     이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Python UnboundLocalError: local variable referenced before assignment 해결 방법
categories:
  - ko_Troubleshooting
tags:
  - Python
  - UnboundLocalError
  - Scope
  - Exception Handling
---


![이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Python UnboundLocalError: local variable referenced before assignment 해결 방법](/images/header_images/overlay_image_python.png)
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

## 전문 보완 체크

**Python UnboundLocalError: local variable referenced before assignment 해결 방법**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 인터프리터 경로, 가상환경, 패키지 버전, 입력 파일 또는 데이터 경계를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

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

독자가 **Python UnboundLocalError: local variable referenced before assignment 해결 방법**의 첫 번째 권장 조치를 이미 시도했지만 결과가 여전히 불확실하다고 가정해 봅니다. 다음 단계는 여러 해결책을 한꺼번에 시험하는 것이 아니라 짧은 감사 기록을 만드는 것입니다. 먼저 어떤 판단을 하려는지 한 문장으로 쓰고, 환경을 한 문장으로 적고, 관찰된 결과를 한 문장으로 남깁니다. 그다음 인터프리터 경로, 가상환경, 패키지 버전, 입력 파일 또는 데이터 경계를 이미 확보한 사실과 대조합니다. 이렇게 해야 글이 서로 끊어진 팁 목록이 아니라 검증 가능한 절차가 됩니다.

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
