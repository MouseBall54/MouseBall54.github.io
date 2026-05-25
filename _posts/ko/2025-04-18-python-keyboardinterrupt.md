---
typora-root-url: ../
layout: single
title: >
    Python KeyboardInterrupt 예외 처리 방법
date: 2025-04-18T07:22:00+09:00
seo_title: >
    Python KeyboardInterrupt 예외 처리 방법

lang: ko
translation_id: python-keyboardinterrupt
header:
   teaser: /images/header_images/overlay_image_python.png
   overlay_image: /images/header_images/overlay_image_python.png
   overlay_filter: 0.5
   image_description: >
     이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Python KeyboardInterrupt 예외 처리 방법
excerpt: >
    Python에서 KeyboardInterrupt는 사용자가 Ctrl+C를 눌러 프로그램을 강제 종료할 때 발생하는 예외입니다. 이 예외를 올바르게 처리하면 프로그램을 안전하게 종료하고 리소스를 정리할 수 있습니다. 이 글에서는 KeyboardInterrupt를 처리하는 방법을 알아봅니다.
seo_description: >
    Python에서 KeyboardInterrupt는 사용자가 Ctrl+C를 눌러 프로그램을 강제 종료할 때 발생하는 예외입니다. 이 예외를 올바르게 처리하면 프로그램을 안전하게 종료하고 리소스를 정리할 수 있습니다. 이 글에서는 KeyboardInterrupt를 처리하는 방법을 알아봅니다.
categories:
  - ko_Troubleshooting
tags:
  - Python
  - KeyboardInterrupt
  - Exception
  - Signal
---


![이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Python KeyboardInterrupt 예외 처리 방법](/images/header_images/overlay_image_python.png)
## 문제 상황

Python 스크립트가 실행 중일 때, 사용자가 터미널에서 `Ctrl+C`를 누르면 프로그램이 즉시 종료됩니다.
이때 `KeyboardInterrupt`라는 예외가 발생합니다.
만약 이 예외를 처리하지 않으면, 프로그램은 하던 작업을 마무리하지 못하고 비정상적으로 종료될 수 있습니다.
이는 파일 핸들이나 네트워크 연결과 같은 리소스가 제대로 해제되지 않는 문제를 유발할 수 있습니다.

```python
import time

print("프로그램 시작. 종료하려면 Ctrl+C를 누르세요.")
i = 0
while True:
    print(f"작업 중... {i}")
    time.sleep(1)
    i += 1
```

위 코드를 실행하고 `Ctrl+C`를 누르면 다음과 같은 메시지와 함께 프로그램이 종료됩니다.

```
Traceback (most recent call last):
  File "main.py", line 7, in <module>
    time.sleep(1)
KeyboardInterrupt
```

## 원인 분석

`KeyboardInterrupt`는 `BaseException`을 상속하는 예외 클래스입니다.
사용자가 `Ctrl+C` (SIGINT 신호)를 입력하면 Python 인터프리터가 이 예외를 발생시킵니다.
이는 사용자에게 프로그램을 중단할 수 있는 제어권을 주기 위한 정상적인 기능입니다.
문제는 이 중단이 예기치 않은 시점에 발생하여 프로그램의 상태를 불안정하게 만들 수 있다는 점입니다.

## 해결 방법

### 1. `try-except` 블록으로 예외 처리

가장 일반적인 방법은 `try-except` 블록을 사용하여 `KeyboardInterrupt`를 잡는 것입니다.
이를 통해 프로그램이 종료되기 전에 필요한 정리 작업을 수행할 수 있습니다.

```python
import time

print("프로그램 시작. 종료하려면 Ctrl+C를 누르세요.")
try:
    i = 0
    while True:
        print(f"작업 중... {i}")
        time.sleep(1)
        i += 1
except KeyboardInterrupt:
    print("\n프로그램을 종료합니다. 정리 작업을 수행합니다.")
    # 여기에 파일 닫기, 연결 종료 등 정리 코드를 추가
    print("정리 완료. 안녕히 가세요.")
```

이제 `Ctrl+C`를 누르면 `except` 블록의 코드가 실행되어 안전하게 프로그램을 마무리할 수 있습니다.

### 2. `finally` 블록으로 리소스 정리 보장

`KeyboardInterrupt`가 발생하든 안 하든 항상 실행되어야 하는 정리 코드가 있다면 `finally` 블록을 사용하는 것이 좋습니다.
`finally`는 예외 발생 여부와 관계없이 항상 실행되기 때문입니다.

```python
import time

f = None
try:
    f = open("temp_file.txt", "w")
    print("파일을 열었습니다. 작업을 시작합니다.")
    i = 0
    while True:
        f.write(f"로그: {i}\n")
        print(f"작업 중... {i}")
        time.sleep(1)
        i += 1
except KeyboardInterrupt:
    print("\n프로그램을 중단합니다.")
finally:
    if f:
        f.close()
        print("파일을 닫았습니다. 프로그램 종료.")
```

이 구조는 `Ctrl+C`가 눌렸을 때 파일이 안전하게 닫히도록 보장합니다.

### 3. `signal` 모듈 사용 (고급)

더 낮은 수준에서 신호를 직접 처리하고 싶다면 `signal` 모듈을 사용할 수 있습니다.
`signal.signal()` 함수를 사용하여 `SIGINT` 신호에 대한 핸들러를 등록할 수 있습니다.

```python
import signal
import sys
import time

def signal_handler(sig, frame):
    print("\nCtrl+C가 감지되었습니다! 프로그램을 종료합니다.")
    # 필요한 정리 작업 수행
    sys.exit(0)

# SIGINT 신호에 대한 핸들러 등록
signal.signal(signal.SIGINT, signal_handler)

print("프로그램 시작. 종료하려면 Ctrl+C를 누르세요.")
i = 0
while True:
    print(f"작업 중... {i}")
    time.sleep(1)
    i += 1
```

이 방법은 `try-except`보다 복잡하지만, 프로그램의 여러 부분에서 일관된 종료 동작을 적용해야 할 때 유용합니다.

## 결론

`KeyboardInterrupt`는 사용자의 프로그램 중단 요청을 처리하는 중요한 메커니즘입니다.
`try-except` 블록을 사용하여 이 예외를 적절히 처리하면, 프로그램이 비정상적으로 종료되는 것을 막고 리소스를 안전하게 해제할 수 있습니다.
대부분의 경우 `try-except`와 `finally` 조합으로 충분하며, 더 복잡한 신호 처리가 필요할 때 `signal` 모듈을 고려해볼 수 있습니다.

## 전문 보완 체크

**Python KeyboardInterrupt 예외 처리 방법**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 인터프리터 경로, 가상환경, 패키지 버전, 입력 파일 또는 데이터 경계를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

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

독자가 **Python KeyboardInterrupt 예외 처리 방법**의 첫 번째 권장 조치를 이미 시도했지만 결과가 여전히 불확실하다고 가정해 봅니다. 다음 단계는 여러 해결책을 한꺼번에 시험하는 것이 아니라 짧은 감사 기록을 만드는 것입니다. 먼저 어떤 판단을 하려는지 한 문장으로 쓰고, 환경을 한 문장으로 적고, 관찰된 결과를 한 문장으로 남깁니다. 그다음 인터프리터 경로, 가상환경, 패키지 버전, 입력 파일 또는 데이터 경계를 이미 확보한 사실과 대조합니다. 이렇게 해야 글이 서로 끊어진 팁 목록이 아니라 검증 가능한 절차가 됩니다.

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
