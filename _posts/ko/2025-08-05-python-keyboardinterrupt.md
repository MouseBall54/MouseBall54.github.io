typora-root-url: ../
layout: single
title: >
    Python KeyboardInterrupt 예외 처리 방법
seo_title: >
    Python KeyboardInterrupt 예외 처리 방법
date: 2025-08-05T21:10:00+09:00
header:
   teaser: /images/header_images/overlay_image_python.png
   overlay_image: /images/header_images/overlay_image_python.png
   overlay_filter: 0.5
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

