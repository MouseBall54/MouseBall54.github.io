---
typora-root-url: ../
layout: single
title: >
  "Python "ImportError: cannot import name '...' from '...'" 오류 해결 방법"

date: 2025-02-19T07:54:00+09:00
lang: ko
translation_id: python-importerror-cannot-import-name
excerpt: >
  "순환 참조, 오타, 잘못된 모듈 경로를 확인하여 Python의 "ImportError: cannot import name '...' from '...'" 오류를 해결하세요."
seo_description: >
  "순환 참조, 오타, 잘못된 모듈 경로를 확인하여 Python의 "ImportError: cannot import name '...' from '...'" 오류를 해결하세요."
header:
   teaser: /images/header_images/overlay_image_python.png
   overlay_image: /images/header_images/overlay_image_python.png
   overlay_filter: 0.5
   image_description: >
     이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Python "ImportError: cannot import name '...' from '...'" 오류 해결 방법
categories:
  - ko_Troubleshooting
tags:
  - Python
  - ImportError
  - Debugging
  - Circular Import
---


![이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Python "ImportError: cannot import name '...' from '...'" 오류 해결 방법](/images/header_images/overlay_image_python.png)
## 서론

`ImportError: cannot import name '...' from '...'`는 Python에서 import 구문이 실패할 때 발생하는 흔한 오류다. 이 오류는 주로 세 가지 원인, 즉 순환 참조, 임포트하려는 함수나 클래스 이름의 오타, 또는 잘못된 모듈 경로 때문에 발생한다. 이 가이드에서는 각 원인을 설명하고 해결책을 제공한다.

## 1. 원인: 순환 참조 (Circular Imports)

순환 참조는 둘 이상의 모듈이 서로를 의존할 때 발생한다. 예를 들어, `module_a.py`가 `module_b.py`의 무언가를 임포트하려고 하고, 동시에 `module_b.py`도 `module_a.py`의 무언가를 임포트하려고 할 때다. 이는 Python이 해결할 수 없는 의존성 루프를 만든다.

### 예시

**`module_a.py`**:
```python
from module_b import b_func

def a_func():
    print("This is a_func")
    b_func()

a_func()
```

**`module_b.py`**:
```python
from module_a import a_func

def b_func():
    print("This is b_func")

# module_b가 a_func를 임포트하려 할 때, module_a가 아직 완전히 정의되지 않았으므로
# ImportError가 발생한다.
```

### 해결책

순환 참조를 해결하려면 의존성 고리를 끊도록 코드를 리팩토링해야 한다.

- **임포트 문 이동**: 때로는 임포트 문을 필요한 함수 내부로 옮기는 것(지역 임포트)으로 문제를 해결할 수 있다.
- **코드 재구성**: 공유되는 기능을 제3의 모듈로 옮겨 `module_a`와 `module_b`가 순환 의존성 없이 임포트할 수 있도록 한다.
- **인터페이스 또는 의존성 주입 사용**: 더 복잡한 애플리케이션의 경우, 모듈 간의 결합도를 낮추는 디자인 패턴을 사용하는 것을 고려한다.

## 2. 원인: 오타 또는 존재하지 않는 이름

지정된 모듈에 존재하지 않는 이름(함수, 클래스, 변수)을 임포트하려고 할 때도 이 오류가 발생할 수 있다. 이는 종종 단순한 오타 때문이다.

### 예시

**`my_module.py`**:
```python
def calculate_sum(a, b):
    return a + b
```

**`main.py`**:
```python
# 오타: 'calculate_sum'을 'calculate_total'로 잘못 입력
from my_module import calculate_total 

# ImportError: cannot import name 'calculate_total' from 'my_module' 오류 발생
```

### 해결책

- **오타 확인**: 임포트하려는 이름의 철자를 주의 깊게 확인하고 소스 모듈의 정의와 일치하는지 확인한다.
- **이름 존재 여부 확인**: 해당 함수, 클래스 또는 변수가 임포트하려는 모듈에 실제로 정의되어 있는지 확인한다.

## 3. 원인: 잘못된 모듈 경로 또는 이름

모듈 자체를 찾을 수 없거나 이름 충돌(예: 스크립트 이름이 표준 라이브러리 모듈과 동일한 경우)이 있을 때 이 오류가 발생할 수 있다.

### 예시

프로젝트에 `math.py`라는 파일이 있고 표준 `math` 라이브러리의 함수를 임포트하려고 하면, 로컬 파일에서 임포트를 시도할 수 있다.

### 해결책

- **`sys.path` 확인**: 모듈이 포함된 디렉터리가 Python의 검색 경로에 있는지 확인한다. `sys.path`를 검사하여 Python이 모듈을 찾는 위치를 볼 수 있다.
- **이름 충돌 방지**: 스크립트 이름을 표준 Python 라이브러리와 동일하게 짓지 않는다 (예: `math.py`, `os.py`, `sys.py`).
- **`__init__.py` 존재 확인**: 패키지(모듈 디렉터리)에서 임포트하는 경우, `__init__.py` 파일이 포함되어 있는지 확인한다 (Python 3.3+의 네임스페이스 패키지에서는 덜 엄격함).

이러한 일반적인 원인들을 체계적으로 점검함으로써 `ImportError: cannot import name '...' from '...'` 오류를 효과적으로 해결할 수 있다.

## 전문 보완 체크

**"Python "ImportError: cannot import name '...' from '...'" 오류 해결 방법"**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 인터프리터 경로, 가상환경, 패키지 버전, 입력 파일 또는 데이터 경계를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

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

독자가 **"Python "ImportError: cannot import name '...' from '...'" 오류 해결 방법"**의 첫 번째 권장 조치를 이미 시도했지만 결과가 여전히 불확실하다고 가정해 봅니다. 다음 단계는 여러 해결책을 한꺼번에 시험하는 것이 아니라 짧은 감사 기록을 만드는 것입니다. 먼저 어떤 판단을 하려는지 한 문장으로 쓰고, 환경을 한 문장으로 적고, 관찰된 결과를 한 문장으로 남깁니다. 그다음 인터프리터 경로, 가상환경, 패키지 버전, 입력 파일 또는 데이터 경계를 이미 확보한 사실과 대조합니다. 이렇게 해야 글이 서로 끊어진 팁 목록이 아니라 검증 가능한 절차가 됩니다.

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
