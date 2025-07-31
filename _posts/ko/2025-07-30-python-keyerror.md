---
typora-root-url: ../
layout: single
title: "Python KeyError 해결 방법: 딕셔너리 키 오류"
date: 2025-07-30T22:00:00+09:00
excerpt: "Python에서 존재하지 않는 딕셔너리 키에 접근할 때 발생하는 KeyError의 원인을 이해하고, 이를 해결하는 효과적인 방법들을 알아봅니다."
header:
   teaser: /images/header_images/overlay_image_python.png
   overlay_image: /images/header_images/overlay_image_python.png
   overlay_filter: 0.5
categories:
  - ko_Troubleshooting
tags:
  - Python
  - KeyError
  - Dictionary
  - Error Handling
---

## Python `KeyError`란 무엇인가?

`KeyError`는 딕셔너리(dictionary)에 존재하지 않는 키(key)로 값(value)에 접근하려고 할 때 발생하는 예외다. 딕셔너리는 데이터를 키-값 쌍으로 저장하며, 각 키는 고유해야 한다. 만약 딕셔너리에 없는 키를 사용해 값을 요청하면, Python은 `KeyError`를 발생시켜 찾으려는 키가 없음을 알린다.

이 오류는 딕셔너리나 다른 매핑(mapping) 타입의 객체에서만 발생한다. 흔히 겪는 문제지만, 다행히 쉽게 예방할 수 있다.

## `KeyError`의 일반적인 원인

`KeyError`가 발생하는 주된 원인은 다음과 같다.

- **단순한 오타:** 키 이름을 잘못 입력했을 수 있다.
- **잘못된 데이터 가정:** 외부 API나 JSON 파일 같은 데이터를 다룰 때, 특정 키가 항상 존재할 것이라고 가정하는 경우다.
- **대소문자 구분:** 딕셔너리 키는 대소문자를 구분한다. 예를 들어, `'name'`과 `'Name'`은 서로 다른 키로 취급된다.
- **의도치 않은 삭제:** 코드의 다른 부분에서 해당 키가 이미 삭제되었을 수 있다.

다음은 `KeyError`를 유발하는 간단한 예시다.

```python
my_dict = {'name': 'Alice', 'age': 30}

# 존재하지 않는 키에 접근 시도
print(my_dict['city'])
```

이 코드를 실행하면 다음과 같은 결과가 나온다.

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'city'
```

## `KeyError` 해결 방법

`KeyError`를 처리하거나 예방하는 몇 가지 방법이 있다.

### 1. `in` 키워드로 키 존재 여부 확인

키에 접근하기 전에 `in` 키워드를 사용해 해당 키가 딕셔너리에 존재하는지 확인할 수 있다. 이는 가장 직관적이고 가독성이 좋은 방법이다.

```python
my_dict = {'name': 'Alice', 'age': 30}
key_to_check = 'city'

if key_to_check in my_dict:
    print(my_dict[key_to_check])
else:
    print(f"'{key_to_check}' 키가 존재하지 않습니다.")
```

이 코드는 키 존재 여부를 안전하게 확인하여 오류를 피하고, 대신 유용한 메시지를 출력한다.

### 2. `.get()` 메서드 사용

딕셔너리의 `.get()` 메서드는 이 문제를 해결하는 가장 Pythonic한 방법 중 하나다. 이 메서드는 키를 사용해 값을 가져오려고 시도하며, 만약 키가 없으면 `KeyError`를 발생시키는 대신 기본값으로 `None`을 반환한다.

또한, 키가 없을 때 반환할 기본값을 직접 지정할 수도 있다.

```python
my_dict = {'name': 'Alice', 'age': 30}

# 'city' 키가 없으므로 None을 반환
city = my_dict.get('city')
print(city)  # 출력: None

# 키가 없을 경우 지정한 기본값을 반환
country = my_dict.get('country', 'Unknown')
print(country)  # 출력: Unknown
```

`.get()`을 사용하면 코드가 더 간결하고 안정적으로 변한다.

### 3. `try...except` 블록 사용

만약 키가 없는 상황이 예외적인 경우에만 발생할 것으로 예상된다면, `try...except` 블록을 사용해 `KeyError`를 잡을 수 있다. 이는 키의 부재가 특별한 처리가 필요한 오류 상황을 의미할 때 유용하다.

```python
my_dict = {'name': 'Alice', 'age': 30}

try:
    city = my_dict['city']
    print(city)
except KeyError:
    print("'city' 키를 딕셔너리에서 찾을 수 없습니다.")
    # 여기에 다른 오류 처리 로직을 추가할 수 있다
```

이 접근 방식은 주된 로직을 깔끔하게 유지하면서 오류를 처리할 명확한 경로를 제공한다.

## 결론

Python의 `KeyError`는 존재하지 않는 딕셔너리 키에 접근하려 할 때 발생하는 신호다. `in` 키워드를 사용한 간단한 확인, 유연한 `.get()` 메서드, 또는 `try...except`를 이용한 구조적인 오류 처리를 통해 더 안정적이고 오류 없는 코드를 작성할 수 있다. 어떤 방법을 선택할지는 특정 요구사항과 프로그램에서 키가 없는 상황이 예상된 시나리오인지, 아니면 예외적인 이벤트인지에 따라 달라진다.
