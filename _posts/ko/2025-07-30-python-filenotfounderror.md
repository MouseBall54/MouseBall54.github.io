---
typora-root-url: ../
layout: single
title: "Python FileNotFoundError 해결 방법"

lang: ko
translation_id: python-filenotfounderror
excerpt: "Python에서 파일을 다룰 때 흔히 발생하는 FileNotFoundError: [Errno 2] No such file or directory 오류의 원인과 해결책을 상세히 알아봅니다."
header:
   teaser: /images/header_images/overlay_image_python.png
   overlay_image: /images/header_images/overlay_image_python.png
   overlay_filter: 0.5
categories:
  - ko_Troubleshooting
tags:
  - Python
  - FileNotFoundError
  - File I/O
  - Error Handling
---

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
