---
typora-root-url: ../
layout: single
title: "Python FileNotFoundError 해결 방법"

date: 2025-01-16T07:20:00+09:00
lang: ko
translation_id: python-filenotfounderror
excerpt: "Python에서 파일을 다룰 때 흔히 발생하는 FileNotFoundError: [Errno 2] No such file or directory 오류의 원인과 해결책을 상세히 알아봅니다."
seo_description: "Python에서 파일을 다룰 때 흔히 발생하는 FileNotFoundError: [Errno 2] No such file or directory 오류의 원인과 해결책을 상세히 알아봅니다."
header:
   teaser: /images/header_images/overlay_image_python.png
   overlay_image: /images/header_images/overlay_image_python.png
   overlay_filter: 0.5
   image_description: >
     이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Python FileNotFoundError 해결 방법
categories:
  - ko_Troubleshooting
tags:
  - Python
  - FileNotFoundError
  - File I/O
  - Error Handling
---


![이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Python FileNotFoundError 해결 방법](/images/header_images/overlay_image_python.png)
## `FileNotFoundError`란 무엇인가?

`FileNotFoundError`는 지정된 경로에 존재하지 않는 파일에 접근하려고 할 때 발생하는 예외다. 이는 파일을 열거나, 읽거나, 쓰는 등 파일 입출력(I/O) 작업을 할 때 매우 흔하게 발생하는 오류다.

전체 오류 메시지는 보통 다음과 같은 형식이다.
`FileNotFoundError: [Errno 2] No such file or directory: 'non_existent_file.txt'`

이 오류는 오류의 종류(`FileNotFoundError`)와 Python이 찾지 못한 파일(`non_existent_file.txt`) 두 가지 정보를 알려준다.

## `FileNotFoundError`의 일반적인 원인

이 오류가 발생하는 몇 가지 이유는 다음과 같다.

- **잘못된 파일 이름:** 파일 이름에 오타가 있을 수 있다.
- **잘못된 경로:** 파일 경로가 틀렸을 수 있다. 파일이 생각과 다른 디렉터리에 있을 수 있다.
- **작업 디렉터리:** 스크립트의 현재 작업 디렉터리가 예상과 다를 수 있으며, 이는 상대 경로를 사용할 때 문제가 될 수 있다.
- **파일이 존재하지 않음:** 파일이 생성되지 않았거나, 삭제 또는 이동되었을 수 있다.

## `FileNotFoundError` 해결 방법

간단한 확인부터 더 견고한 해결책까지, 이 오류를 해결하는 몇 가지 방법이 있다.

### 1. 파일 경로와 이름 확인

가장 먼저 할 일은 파일 이름과 경로에 오타가 없는지 다시 확인하는 것이다. 또한, 지정한 위치에 파일이 실제로 존재하는지 확인해야 한다.

### 2. 절대 경로와 상대 경로

**상대 경로**는 현재 작업 디렉터리를 기준으로 한 경로다. 예를 들어, `data/my_file.txt`와 같다.
**절대 경로**는 루트 디렉터리부터 시작하는 전체 경로다. 예를 들어, Windows에서는 `C:/Users/YourUser/Documents/data/my_file.txt`, Linux/macOS에서는 `/home/YourUser/Documents/data/my_file.txt`와 같다.

상대 경로에 문제가 있다면, 절대 경로를 사용해 문제가 해결되는지 확인해 보자. 이를 통해 문제가 경로 자체에 있는지, 아니면 작업 디렉터리에 있는지 판단하는 데 도움이 될 수 있다.

`os` 모듈을 사용해 현재 작업 디렉터리를 확인할 수 있다.

```python
import os
print(os.getcwd())
```

### 3. 파일 존재 여부 확인 후 열기

파일을 열기 전에 프로그래밍 방식으로 파일이 존재하는지 확인할 수 있다. `os.path.exists()` 함수가 이 작업에 적합하다.

```python
import os

file_path = 'data/my_file.txt'

if os.path.exists(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
        print(content)
else:
    print(f"{file_path} 경로에 파일이 없습니다.")
```

이 접근 방식은 오류가 발생하는 것을 사전에 방지한다.

### 4. `try...except` 블록 사용

잠재적인 오류를 처리하는 가장 Pythonic한 방법은 `try...except` 블록을 사용하는 것이다. 이를 통해 실패할 수 있는 연산을 "시도(try)"하고, 실패할 경우 예외를 "잡을(catch)" 수 있다.

```python
file_path = 'data/my_file.txt'

try:
    with open(file_path, 'r') as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print(f"오류: {file_path} 경로에서 파일을 찾을 수 없습니다.")
except Exception as e:
    print(f"예상치 못한 오류가 발생했습니다: {e}")
```

이 방법은 Python 프로그래밍에서 흔한 "허락보다 용서를 구하기가 더 쉽다(EAFP)" 원칙을 따르기 때문에 종종 선호된다. 프로그램을 중단시키지 않고 오류를 부드럽게 처리한다.

## 결론

`FileNotFoundError`는 파일을 찾을 수 없음을 나타내는 직관적인 오류다. 파일 경로를 신중하게 확인하고, 절대 경로와 상대 경로의 차이점을 이해하며, `os.path.exists()`나 `try...except` 블록과 같은 도구를 사용함으로써 파일 작업을 더 안정적으로 처리하고 더 견고한 애플리케이션을 만들 수 있다.

## 전문 보완 체크

**Python FileNotFoundError 해결 방법**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 인터프리터 경로, 가상환경, 패키지 버전, 입력 파일 또는 데이터 경계를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

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

독자가 **Python FileNotFoundError 해결 방법**의 첫 번째 권장 조치를 이미 시도했지만 결과가 여전히 불확실하다고 가정해 봅니다. 다음 단계는 여러 해결책을 한꺼번에 시험하는 것이 아니라 짧은 감사 기록을 만드는 것입니다. 먼저 어떤 판단을 하려는지 한 문장으로 쓰고, 환경을 한 문장으로 적고, 관찰된 결과를 한 문장으로 남깁니다. 그다음 인터프리터 경로, 가상환경, 패키지 버전, 입력 파일 또는 데이터 경계를 이미 확보한 사실과 대조합니다. 이렇게 해야 글이 서로 끊어진 팁 목록이 아니라 검증 가능한 절차가 됩니다.

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
