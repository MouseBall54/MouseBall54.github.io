---
typora-root-url: ../
layout: single
title: >
   Python IsADirectoryError: [Errno 21] Is a directory 오류 해결 방법

lang: ko
translation_id: python-isadirectoryerror-errno-21-is-a-directory
header:
   teaser: /images/header_images/overlay_image_python.png
   overlay_image: /images/header_images/overlay_image_python.png
   overlay_filter: 0.5
excerpt: >
   Python에서 디렉터리를 파일처럼 다루려고 할 때 발생하는 IsADirectoryError: [Errno 21] Is a directory 오류를 해결하는 방법을 배우세요. 이 가이드는 경로를 확인하고 올바른 파일 작업을 사용하는 방법을 보여줍니다.
categories:
   - ko_Troubleshooting
tags:
   - Python
   - IsADirectoryError
   - File I/O
   - OSError
   - Troubleshooting
---

## 서론

Python에서 파일 관련 작업을 수행할 때 `IsADirectoryError: [Errno 21] Is a directory` 오류를 만날 수 있습니다. 이 오류는 파일이 아닌 디렉터리를 가리키는 경로에 대해 읽기나 쓰기와 같은 파일 전용 작업을 시도할 때 발생합니다.

이 가이드는 이 오류가 발생하는 이유를 이해하고, 코드가 파일과 디렉터리를 올바르게 구별하도록 하여 문제를 해결하는 방법을 안내합니다.

## `IsADirectoryError`의 원인은 무엇인가요?

이 오류의 근본 원인은 간단합니다. 코드가 디렉터리 경로를 파일 경로인 것처럼 사용하려고 하기 때문입니다.

일반적인 시나리오는 다음과 같습니다.
1.  **디렉터리 열기**: `open()` 함수에 디렉터리 경로를 사용하는 경우.
2.  **디렉터리 읽기**: 디렉터리 경로에 대해 `.read()` 또는 `.write()`를 호출하려고 시도하는 경우.
3.  **잘못된 경로 구성**: 전체 파일 경로를 담아야 할 변수가 부모 디렉터리 경로만 포함하고 있는 경우.

오류를 발생시키는 간단한 예제를 살펴보겠습니다.

```python
# 'my_project'가 디렉터리라고 가정
try:
    with open('my_project', 'r') as f: # 이 줄에서 IsADirectoryError 발생
        content = f.read()
except IsADirectoryError as e:
    print(f"오류: {e}")
# 출력: 오류: [Errno 21] Is a directory: 'my_project'
```

`open()` 함수는 파일과 함께 작동하도록 설계되었으므로, 디렉터리 경로를 받으면 `IsADirectoryError`를 발생시킵니다.

## 오류 해결 방법

이 오류를 해결하려면 파일 작업에 유효한 파일 경로를 제공하고 있는지 확인해야 합니다. 문제를 디버깅하고 해결하는 단계는 다음과 같습니다.

### 1. 경로 확인

첫 번째 단계는 사용 중인 경로가 실제로 파일인지 디렉터리인지 확인하는 것입니다. 이때 `os.path` 모듈이 매우 유용합니다.

-   `os.path.isfile(path)`: 경로가 존재하는 일반 파일이면 `True`를 반환합니다.
-   `os.path.isdir(path)`: 경로가 존재하는 디렉터리면 `True`를 반환합니다.

경로를 열기 전에 코드에 확인 절차를 추가할 수 있습니다.

```python
import os

path = 'my_project' # 이것은 디렉터리입니다

if os.path.isfile(path):
    with open(path, 'r') as f:
        content = f.read()
        print("파일 내용을 성공적으로 읽었습니다.")
elif os.path.isdir(path):
    print(f"오류: '{path}' 경로는 디렉터리입니다. 파일 경로를 제공해주세요.")
else:
    print(f"오류: '{path}' 경로가 존재하지 않거나 일반 파일/디렉터리가 아닙니다.")
```

이 간단한 확인은 오류를 방지하고 무엇이 잘못되었는지에 대한 명확한 메시지를 제공합니다.

### 2. 올바른 파일 경로 구성

종종 이 오류는 파일 이름이 디렉터리 경로에 추가되지 않았기 때문에 발생합니다. 코드가 대상 파일의 전체 경로를 올바르게 구성하는지 확인하세요.

**잘못된 코드:**
```python
import os

dir_path = '/home/user/documents'
# 'documents' 내의 파일을 열려고 했지만 파일 이름이 누락되었습니다.
# with open(dir_path, 'r') as f: # IsADirectoryError 발생
#     ...
```

**올바른 코드:**
```python
import os

dir_path = '/home/user/documents'
file_name = 'report.txt'
full_path = os.path.join(dir_path, file_name)

print(f"열기 시도: {full_path}")

# 열기 전에 파일이 존재하는지 확인하는 것이 좋습니다
if os.path.exists(full_path) and os.path.isfile(full_path):
    with open(full_path, 'r') as f:
        content = f.read()
        print("파일을 성공적으로 읽었습니다.")
else:
    print(f"파일을 찾을 수 없습니다: {full_path}")
```
`os.path.join()`을 사용하는 것은 플랫폼에 독립적인 경로를 만드는 권장 방법입니다.

### 3. 디렉터리 내용 나열하기

만약 목표가 디렉터리 *안의* 파일들과 작업하는 것이라면, 먼저 `os.listdir()`를 사용하여 디렉터리의 내용을 나열한 다음 결과를 반복해야 합니다.

```python
import os

dir_path = 'my_project'

if os.path.isdir(dir_path):
    print(f"'{dir_path}' 내의 파일 및 디렉터리:")
    for item_name in os.listdir(dir_path):
        # 각 항목의 전체 경로 구성
        item_path = os.path.join(dir_path, item_name)
        
        # 파일만 처리
        if os.path.isfile(item_path):
            print(f"  - 파일 처리 중: {item_name}")
            # 여기서 파일을 열고 읽을 수 있습니다
            # with open(item_path, 'r') as f:
            #     ...
        else:
            print(f"  - 디렉터리 건너뛰기: {item_name}")
else:
    print(f"오류: '{dir_path}' 디렉터리를 찾을 수 없습니다.")
```
이 패턴은 실제 파일만 열려고 시도하도록 보장합니다.

## 결론

`IsADirectoryError`는 프로그램이 디렉터리를 파일로 착각하고 있다는 명확한 신호입니다. `os.path.isfile()`, `os.path.isdir()`, `os.path.join()`과 같은 `os.path` 모듈의 함수를 사용하면 파일 및 디렉터리 경로를 올바르게 처리하는 더 강력한 코드를 작성할 수 있습니다. 이 오류를 방지하고 애플리케이션의 안정성을 높이려면 파일 작업을 수행하기 전에 항상 경로를 확인하세요.
