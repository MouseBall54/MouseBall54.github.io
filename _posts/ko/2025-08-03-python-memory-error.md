---
typora-root-url: ../
layout: single
title: >
    Python "MemoryError" 해결 방법

lang: ko
translation_id: python-memory-error
header:
    teaser: /images/header_images/overlay_image_python.png
    overlay_image: /images/header_images/overlay_image_python.png
    overlay_filter: 0.5
excerpt: >
    Python에서 MemoryError는 프로그램이 시스템의 가용 메모리를 모두 소진했을 때 발생합니다. 이 글에서는 MemoryError의 원인과 해결 방법을 알아봅니다.
categories:
    - ko_Troubleshooting
tags:
    - Python
    - MemoryError
    - Optimization
---

## Python "MemoryError"란 무엇인가?

`MemoryError`는 Python 프로그램이 실행 중에 시스템의 메모리(RAM)를 모두 소진하여 더 이상 객체를 할당할 수 없을 때 발생하는 예외입니다. 이 오류는 주로 대용량 데이터를 처리하거나, 메모리 누수가 있거나, 비효율적인 알고리즘을 사용할 때 나타납니다.

## "MemoryError"의 일반적인 원인

1.  **대용량 데이터 처리**: 매우 큰 파일(예: 이미지, 동영상, 대규모 데이터셋)을 한 번에 메모리에 로드하려고 할 때 발생할 수 있습니다.
2.  **메모리 누수**: 객체에 대한 참조가 해제되지 않아 가비지 컬렉터가 메모리를 회수하지 못하는 경우 발생합니다.
3.  **비효율적인 자료 구조**: 리스트에 수백만 개의 항목을 추가하는 등 메모리 사용량이 많은 자료 구조를 비효율적으로 사용할 때 발생합니다.
4.  **무한 반복 또는 재귀**: 종료 조건이 없는 반복문이나 재귀 함수는 계속해서 메모리를 소비하여 결국 `MemoryError`를 유발할 수 있습니다.

## "MemoryError" 해결 방법

### 1. 데이터 처리 방식 변경

대용량 파일을 처리할 때는 전체를 한 번에 읽는 대신 **스트리밍(Streaming)** 또는 **점진적(Incremental) 처리** 방식을 사용하세요.

**나쁜 예:**
```python
def process_large_file(file_path):
    with open(file_path, 'r') as f:
        data = f.readlines()  # 파일 전체를 메모리에 로드
    for line in data:
        # 데이터 처리
        pass
```

**좋은 예 (스트리밍):**
```python
def process_large_file_stream(file_path):
    with open(file_path, 'r') as f:
        for line in f:  # 파일을 한 줄씩 읽어 처리
            # 데이터 처리
            pass
```

### 2. 제너레이터(Generator) 사용

제너레이터는 데이터를 한 번에 하나씩 생성하므로 메모리 사용량을 크게 줄일 수 있습니다.

**나쁜 예 (리스트 사용):**
```python
def get_numbers(n):
    nums = []
    for i in range(n):
        nums.append(i)
    return nums

# 1억 개의 숫자를 담은 리스트 생성 (메모리 문제 발생 가능)
# large_list = get_numbers(100000000)
```

**좋은 예 (제너레이터 사용):**
```python
def get_numbers_generator(n):
    for i in range(n):
        yield i

# 제너레이터는 필요할 때마다 값을 생성하므로 메모리 효율적
large_generator = get_numbers_generator(100000000)
for num in large_generator:
    # 숫자 처리
    pass
```

### 3. 메모리 프로파일링 도구 사용

`memory-profiler`와 같은 도구를 사용하여 코드의 어느 부분에서 메모리를 많이 사용하는지 분석할 수 있습니다.

```bash
pip install memory-profiler
```

**사용 예:**
```python
from memory_profiler import profile

@profile
def my_function():
    # 메모리 사용량을 분석하고 싶은 코드
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b
    return a

if __name__ == '__main__':
    my_function()
```

### 4. 64비트 Python 사용

32비트 Python은 프로세스당 메모리 사용량이 약 2GB로 제한됩니다. 대용량 데이터를 다루려면 64비트 Python을 사용하는 것이 좋습니다.

### 5. 메모리 누수 확인

객체에 대한 불필요한 참조가 남아있지 않은지 확인하세요. 예를 들어, 전역 변수나 클래스 멤버에 대용량 객체를 저장하고 해제하지 않으면 메모리 누수가 발생할 수 있습니다.

## 결론

`MemoryError`는 주로 데이터 처리 방식과 관련이 있습니다. 대용량 데이터를 다룰 때는 스트리밍, 제너레이터 등 메모리 효율적인 방법을 사용하고, 프로파일링 도구를 활용하여 메모리 병목 현상을 찾아 해결하는 것이 중요합니다.

