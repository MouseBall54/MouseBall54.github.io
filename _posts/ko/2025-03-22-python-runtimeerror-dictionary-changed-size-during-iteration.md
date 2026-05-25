---
typora-root-url: ../
layout: single
title: >
    파이썬 RuntimeError: dictionary changed size during iteration 해결 방법

date: 2025-03-22T07:40:00+09:00
lang: ko
translation_id: python-runtimeerror-dictionary-changed-size-during-iteration
header:
   teaser: /images/header_images/overlay_image_python.png
   overlay_image: /images/header_images/overlay_image_python.png
   overlay_filter: 0.5
   image_description: >
     이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: 파이썬 RuntimeError: dictionary changed size during iteration 해결 방법
excerpt: >
    파이썬에서 딕셔너리를 순회하는 도중 크기를 변경하면 발생하는 `RuntimeError: dictionary changed size during iteration` 오류의 원인과 해결 방법을 알아봅니다.
seo_description: >
    파이썬에서 딕셔너리를 순회하는 도중 크기를 변경하면 발생하는 `RuntimeError: dictionary changed size during iteration` 오류의 원인과 해결 방법을 알아봅니다.
categories:
  - ko_Troubleshooting
tags:
  - Python
  - RuntimeError
  - Dictionary
  - Iteration
---


![이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: 파이썬 RuntimeError: dictionary changed size during iteration 해결 방법](/images/header_images/overlay_image_python.png)
## 문제 상황

파이썬에서 `for` 루프를 사용해 딕셔너리를 순회하면서 특정 조건에 맞는 항목을 삭제하거나 추가하려고 할 때 다음과 같은 `RuntimeError`가 발생할 수 있습니다.

```
RuntimeError: dictionary changed size during iteration
```

이 오류는 딕셔너리를 반복하는 동안 딕셔너리의 크기(항목 수)가 변경되었기 때문에 발생합니다. 파이썬은 순회 작업의 일관성을 보장하기 위해 이러한 동작을 허용하지 않습니다.

## 오류 발생 코드 예시

다음은 딕셔너리에서 값이 짝수인 항목을 제거하려 할 때 오류가 발생하는 코드입니다.

```python
numbers = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# 아래 코드는 RuntimeError를 발생시킵니다.
for key, value in numbers.items():
    if value % 2 == 0:
        del numbers[key]

print(numbers)
```

이 코드를 실행하면, `for` 루프가 `numbers` 딕셔너리를 순회하는 동안 `del numbers[key]` 구문이 딕셔너리의 크기를 변경하여 `RuntimeError`가 발생합니다.

## 해결 방법

이 문제를 해결하는 몇 가지 방법이 있습니다. 핵심은 원본 딕셔너리를 직접 수정하는 대신, 순회용 복사본을 만드는 것입니다.

### 1. 딕셔너리의 복사본 사용하기

가장 간단한 방법은 `.copy()` 메서드를 사용하여 딕셔너리의 얕은 복사본(shallow copy)을 만들어 순회하는 것입니다. 이렇게 하면 원본 딕셔너리를 안전하게 수정할 수 있습니다.

```python
numbers = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# 딕셔너리의 복사본을 순회합니다.
for key, value in numbers.copy().items():
    if value % 2 == 0:
        del numbers[key] # 원본 딕셔너리에서 항목 삭제

print(numbers)
# 출력: {'a': 1, 'c': 3}
```

### 2. 키(key) 목록을 만들어 순회하기

`list()` 함수를 사용하여 딕셔너리의 키 목록을 미리 만들어두고, 이 목록을 순회하는 방법도 있습니다.

```python
numbers = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# 키 목록을 리스트로 만들어 순회합니다.
for key in list(numbers.keys()):
    if numbers[key] % 2 == 0:
        del numbers[key]

print(numbers)
# 출력: {'a': 1, 'c': 3}
```

### 3. 새로운 딕셔너리 생성하기 (Dictionary Comprehension)

기존 딕셔너리를 수정하는 대신, 원하는 항목만 포함하는 새로운 딕셔너리를 만드는 것도 좋은 방법입니다. 특히 **딕셔너리 컴프리헨션(Dictionary Comprehension)**을 사용하면 코드를 더 간결하게 작성할 수 있습니다.

```python
numbers = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# 조건에 맞는 항목만 포함하는 새로운 딕셔너리를 생성합니다.
filtered_numbers = {key: value for key, value in numbers.items() if value % 2 != 0}

print(filtered_numbers)
# 출력: {'a': 1, 'c': 3}
```

이 방법은 가독성이 높고, 기존 데이터를 변경하지 않아 더 안전합니다.

## 결론

`RuntimeError: dictionary changed size during iteration` 오류는 순회 중인 딕셔너리를 직접 수정하려고 할 때 발생합니다. 이 문제를 해결하려면 다음 세 가지 방법을 기억하세요.

1.  `.copy()`로 복사본을 만들어 순회하기
2.  `list(dictionary.keys())`로 키 목록을 만들어 순회하기
3.  수정하는 대신, 필요한 항목만 담은 새로운 딕셔너리 만들기

대부분의 경우, 코드가 간결하고 안전한 **딕셔너리 컴프리헨션**을 사용하는 것을 권장합니다.

## 전문 보완 체크

**파이썬 RuntimeError: dictionary changed size during iteration 해결 방법**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 인터프리터 경로, 가상환경, 패키지 버전, 입력 파일 또는 데이터 경계를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

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

독자가 **파이썬 RuntimeError: dictionary changed size during iteration 해결 방법**의 첫 번째 권장 조치를 이미 시도했지만 결과가 여전히 불확실하다고 가정해 봅니다. 다음 단계는 여러 해결책을 한꺼번에 시험하는 것이 아니라 짧은 감사 기록을 만드는 것입니다. 먼저 어떤 판단을 하려는지 한 문장으로 쓰고, 환경을 한 문장으로 적고, 관찰된 결과를 한 문장으로 남깁니다. 그다음 인터프리터 경로, 가상환경, 패키지 버전, 입력 파일 또는 데이터 경계를 이미 확보한 사실과 대조합니다. 이렇게 해야 글이 서로 끊어진 팁 목록이 아니라 검증 가능한 절차가 됩니다.

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
