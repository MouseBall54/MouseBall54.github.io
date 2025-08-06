---
typora-root-url: ../
layout: single
title: >
    파이썬 RuntimeError: dictionary changed size during iteration 해결 방법

lang: ko
translation_id: python-runtimeerror-dictionary-changed-size-during-iteration
header:
   teaser: /images/header_images/overlay_image_python.png
   overlay_image: /images/header_images/overlay_image_python.png
   overlay_filter: 0.5
excerpt: >
    파이썬에서 딕셔너리를 순회하는 도중 크기를 변경하면 발생하는 `RuntimeError: dictionary changed size during iteration` 오류의 원인과 해결 방법을 알아봅니다.
categories:
  - ko_Troubleshooting
tags:
  - Python
  - RuntimeError
  - Dictionary
  - Iteration
---

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
