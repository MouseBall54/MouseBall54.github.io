---
typora-root-url: ../
layout: single
title: "Python TypeError: can only concatenate str (not 'int') to str 해결 방법"

date: 2025-01-23T07:27:00+09:00
lang: ko
translation_id: python-typeerror-can-only-concatenate-str-not-int-to-str
excerpt: "Python에서 'TypeError: can only concatenate str (not 'int') to str'는 문자열에 정수와 같은 다른 타입의 데이터를 직접 연결하려 할 때 발생합니다. 이 오류의 원인과 해결 방법을 알아봅니다."
seo_description: "Python에서 'TypeError: can only concatenate str (not 'int') to str'는 문자열에 정수와 같은 다른 타입의 데이터를 직접 연결하려 할 때 발생합니다. 이 오류의 원인과 해결 방법을 알아봅니다."
header:
   teaser: /images/header_images/overlay_image_python.png
   overlay_image: /images/header_images/overlay_image_python.png
   overlay_filter: 0.5
   image_description: >
     이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Python TypeError: can only concatenate str (not 'int') to str 해결 방법
categories:
  - ko_Troubleshooting
tags:
  - Python
  - TypeError
  - Troubleshooting
  - String
---


![이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Python TypeError: can only concatenate str (not 'int') to str 해결 방법](/images/header_images/overlay_image_python.png)
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

## 전문 보완 체크

**Python TypeError: can only concatenate str (not 'int') to str 해결 방법**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 인터프리터 경로, 가상환경, 패키지 버전, 입력 파일 또는 데이터 경계를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

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

독자가 **Python TypeError: can only concatenate str (not 'int') to str 해결 방법**의 첫 번째 권장 조치를 이미 시도했지만 결과가 여전히 불확실하다고 가정해 봅니다. 다음 단계는 여러 해결책을 한꺼번에 시험하는 것이 아니라 짧은 감사 기록을 만드는 것입니다. 먼저 어떤 판단을 하려는지 한 문장으로 쓰고, 환경을 한 문장으로 적고, 관찰된 결과를 한 문장으로 남깁니다. 그다음 인터프리터 경로, 가상환경, 패키지 버전, 입력 파일 또는 데이터 경계를 이미 확보한 사실과 대조합니다. 이렇게 해야 글이 서로 끊어진 팁 목록이 아니라 검증 가능한 절차가 됩니다.

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
