---
typora-root-url: ../
layout: single
title: >
  "Python "ImportError: cannot import name '...' from '...'" 오류 해결 방법"
date: 2025-07-31T22:00:00+09:00
excerpt: >
  "순환 참조, 오타, 잘못된 모듈 경로를 확인하여 Python의 "ImportError: cannot import name '...' from '...'" 오류를 해결하세요."
categories:
  - ko_Troubleshooting
tags:
  - Python
  - ImportError
  - Debugging
  - Circular Import
---

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

```