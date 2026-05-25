---
typora-root-url: ../
layout: single
title: "Python IndentationError: expected an indented block 오류 해결법"

date: 2025-01-17T07:21:00+09:00
lang: ko
translation_id: python-indentationerror-expected-an-indented-block
excerpt: "Python의 핵심 문법인 들여쓰기! IndentationError의 원인과 해결 방법을 명확히 알아보고, 탭과 공백 혼용 문제를 해결하여 깔끔한 코드를 작성하는 방법을 배워보세요."
seo_description: "Python의 핵심 문법인 들여쓰기! IndentationError의 원인과 해결 방법을 명확히 알아보고, 탭과 공백 혼용 문제를 해결하여 깔끔한 코드를 작성하는 방법을 배워보세요."
header:
   teaser: /images/header_images/overlay_image_python.png
   overlay_image: /images/header_images/overlay_image_python.png
   overlay_filter: 0.5
   image_description: >
     이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Python IndentationError: expected an indented block 오류 해결법
categories:
  - ko_Troubleshooting
tags:
  - Python
  - IndentationError
  - Programming
  - Beginner
---


![이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Python IndentationError: expected an indented block 오류 해결법](/images/header_images/overlay_image_python.png)
## Python `IndentationError: expected an indented block` 오류란?

Python은 다른 프로그래밍 언어와 달리 코드의 구조를 중괄호 `{}` 대신 **들여쓰기(indentation)** 로 구분합니다. `IndentationError: expected an indented block` 오류는 이러한 들여쓰기 규칙이 지켜지지 않았을 때 발생하는, Python의 매우 특징적인 오류입니다.

이 오류는 주로 코드 블록이 필요한 곳에 들여쓰기가 없거나, 들여쓰기 스타일이 일관되지 않을 때 나타납니다.

### 1. 코드 블록에 들여쓰기가 없는 경우

가장 흔한 원인입니다. `if`, `for`, `def`, `class` 등 새로운 코드 블록을 시작하는 구문 다음에는 반드시 들여쓰기가 적용된 코드가 와야 합니다.

**오류 발생 코드:**
```python
def my_function():
print("들여쓰기가 없습니다.") # def 블록 안에 들여쓰기 필요
```

**해결 방법:**
```python
def my_function():
    print("들여쓰기가 적용되었습니다.")
```
Python에서는 일반적으로 **공백 4개**를 사용하여 한 수준의 들여쓰기를 표현합니다. `def` 구문 다음에 오는 `print` 함수를 안쪽으로 들여쓰면 오류가 해결됩니다.

### 2. 불필요한 들여쓰기

반대로, 코드 블록이 필요하지 않은 곳에 불필요하게 들여쓰기를 해도 `IndentationError`가 발생할 수 있습니다. (정확히는 `unexpected indent` 오류가 발생합니다.)

**오류 발생 코드:**
```python
x = 10
    print(x) # 불필요한 들여쓰기
```

**해결 방법:**
```python
x = 10
print(x)
```
최상위 레벨의 코드는 들여쓰기 없이 가장 왼쪽에서 시작해야 합니다.

### 3. 탭(Tab)과 공백(Space)의 혼용

눈으로는 잘 보이지 않지만, `IndentationError`를 유발하는 까다로운 원인 중 하나입니다. Python은 탭과 공백을 다른 문자로 취급합니다. 어떤 줄은 탭으로, 다른 줄은 공백으로 들여쓰기를 하면 인터프리터는 이를 다른 들여쓰기 수준으로 인식하여 오류를 발생시킵니다.

**오류 발생 가능성이 있는 코드 (눈으로는 구별 불가):**
```python
if True:
	print("이 줄은 탭으로 들여쓰기")
    print("이 줄은 공백으로 들여쓰기") # -> IndentationError 발생
```

**해결 방법:**

이 문제를 해결하는 가장 좋은 방법은 코드 편집기에서 **탭을 공백으로 자동 변환**하도록 설정하는 것입니다.

-   **Visual Studio Code**: `settings.json` 파일에 `"editor.insertSpaces": true`, `"editor.tabSize": 4` 설정을 추가합니다.
-   **PyCharm**: `Settings > Editor > Code Style > Python` 메뉴에서 `Use tab character` 체크를 해제하고 `Indent`를 4로 설정합니다.

이미 작성된 코드의 탭과 공백을 정리하려면 편집기의 **"Convert Indentation to Spaces"** 와 같은 기능을 사용하세요.

### 결론

`IndentationError`는 Python의 문법 근간을 이루는 들여쓰기의 중요성을 보여주는 오류입니다. 이 오류를 피하기 위해서는 다음 규칙을 기억하는 것이 중요합니다.

1.  **일관성**: 프로젝트 전체에서 하나의 들여쓰기 스타일(공백 4개 권장)을 유지하세요.
2.  **편집기 설정**: 탭 키를 눌렀을 때 공백 4개가 입력되도록 편집기를 설정하세요.
3.  **블록 확인**: `if`, `for`, `def` 등 콜론(`:`)으로 끝나는 줄 다음에는 반드시 들여쓰기된 코드 블록이 와야 합니다.

올바른 들여쓰기 습관은 `IndentationError`를 예방할 뿐만 아니라, 가독성 높은 코드를 작성하는 첫걸음입니다.

## 전문 보완 체크

**Python IndentationError: expected an indented block 오류 해결법**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 인터프리터 경로, 가상환경, 패키지 버전, 입력 파일 또는 데이터 경계를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

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

독자가 **Python IndentationError: expected an indented block 오류 해결법**의 첫 번째 권장 조치를 이미 시도했지만 결과가 여전히 불확실하다고 가정해 봅니다. 다음 단계는 여러 해결책을 한꺼번에 시험하는 것이 아니라 짧은 감사 기록을 만드는 것입니다. 먼저 어떤 판단을 하려는지 한 문장으로 쓰고, 환경을 한 문장으로 적고, 관찰된 결과를 한 문장으로 남깁니다. 그다음 인터프리터 경로, 가상환경, 패키지 버전, 입력 파일 또는 데이터 경계를 이미 확보한 사실과 대조합니다. 이렇게 해야 글이 서로 끊어진 팁 목록이 아니라 검증 가능한 절차가 됩니다.

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
