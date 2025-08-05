---
typora-root-url: ../
layout: single
title: >
   Python NotADirectoryError: [Errno 20] Not a directory 오류 해결 방법
date: 2025-08-05T10:15:00+09:00
header:
   teaser: /images/header_images/overlay_image_python.png
   overlay_image: /images/header_images/overlay_image_python.png
   overlay_filter: 0.5
excerpt: >
   Python에서 디렉터리 경로가 필요한 곳에 파일 경로를 사용하여 발생하는 NotADirectoryError: [Errno 20] Not a directory 오류를 이해하고 해결하세요. 경로를 검증하여 이 흔한 문제를 피하는 방법을 배웁니다.
categories:
   - ko_Troubleshooting
tags:
   - Python
   - NotADirectoryError
   - File System
   - OSError
   - Troubleshooting
---

## 서론

`NotADirectoryError: [Errno 20] Not a directory`는 `OSError`의 하위 클래스로, 디렉터리 경로가 필요한 컨텍스트에서 파일 경로를 사용하려고 할 때 발생합니다. 이것은 `IsADirectoryError`와 논리적으로 반대되는 오류입니다. 예를 들어, 파일의 내용을 디렉터리인 것처럼 나열하려고 하면 이 오류가 발생합니다.

이 가이드에서는 `NotADirectoryError`의 일반적인 원인을 설명하고 파일 및 디렉터리 경로를 올바르게 처리하여 해결하는 방법을 보여줍니다.

## `NotADirectoryError`의 원인은 무엇인가요?

이 오류는 디렉터리 경로가 필요한 함수가 대신 파일 경로를 받을 때 발생합니다. 이를 유발할 수 있는 가장 일반적인 함수는 다음과 같습니다.

1.  **`os.listdir(path)`**: 이 함수는 주어진 `path` 내부의 파일과 디렉터리를 나열합니다. 만약 `path`가 파일을 가리키면 `NotADirectoryError`를 발생시킵니다.
2.  **`os.path.join(path, ...)`**: 마지막 부분을 제외한 `path`의 구성 요소 중 하나가 파일인 경우 이 오류가 발생할 수 있습니다.
3.  **`os.makedirs(path)`**: 부모 경로 구성 요소 중 하나가 파일인 곳에 디렉터리를 만들려고 할 때 발생합니다.

간단한 예제는 다음과 같습니다.

```python
import os

# 'my_file.txt'가 디렉터리가 아닌 일반 파일이라고 가정
file_path = 'my_file.txt'

try:
    # listdir()는 디렉터리를 예상하므로 NotADirectoryError가 발생합니다
    contents = os.listdir(file_path) 
except NotADirectoryError as e:
    print(f"오류: {e}")

# 출력: 오류: [Errno 20] Not a directory: 'my_file.txt'
```

## 오류 해결 방법

이 오류를 해결하려면 디렉터리 수준 함수에 전달되는 모든 경로가 실제로 디렉터리인지 확인해야 합니다.

### 1. 사용 전 경로 유효성 검사

`os.listdir()`와 같은 함수를 호출하기 전에 경로가 디렉터리인지 확인해야 합니다. `os.path.isdir()` 함수가 이 작업에 완벽합니다.

```python
import os

path_to_check = 'my_file.txt' # 이것은 파일입니다

if os.path.isdir(path_to_check):
    print(f