---
typora-root-url: ../
layout: single
title: "Python IndentationError: expected an indented block 오류 해결법"

lang: ko
translation_id: python-indentationerror-expected-an-indented-block
excerpt: "Python의 핵심 문법인 들여쓰기! IndentationError의 원인과 해결 방법을 명확히 알아보고, 탭과 공백 혼용 문제를 해결하여 깔끔한 코드를 작성하는 방법을 배워보세요."
header:
   teaser: /images/header_images/overlay_image_python.png
   overlay_image: /images/header_images/overlay_image_python.png
   overlay_filter: 0.5
categories:
  - ko_Troubleshooting
tags:
  - Python
  - IndentationError
  - Programming
  - Beginner
---

## Python `IndentationError: expected an indented block` 오류란?

Python은 다른 프로그래밍 언어와 달리 코드의 구조를 중괄호 `{}` 대신 **들여쓰기(indentation)** 로 구분합니다. `IndentationError: expected an indented block` 오류는 이러한 들여쓰기 규칙이 지켜지지 않았을 때 발생하는, Python의 매우 특징적인 오류입니다.

이 오류는 주로 코드 블록이 필요한 곳에 들여쓰기가 없거나, 들여쓰기 스타일이 일관되지 않을 때 나타납니다.

### 1. 코드 블록에 들여쓰기가 없는 경우

가장 흔한 원인입니다. `if`, `for`, `def`, `class` 등 새로운 코드 블록을 시작하는 구문 다음에는 반드시 들여쓰기가 적용된 코드가 와야 합니다.

**오류 발생 코드:**
```python
def my_function():
print("들여쓰기가 없습니다.") # def 블록 안에 들여쓰기 필요
```

**해결 방법:**
```python
def my_function():
    print("들여쓰기가 적용되었습니다.")
```
Python에서는 일반적으로 **공백 4개**를 사용하여 한 수준의 들여쓰기를 표현합니다. `def` 구문 다음에 오는 `print` 함수를 안쪽으로 들여쓰면 오류가 해결됩니다.

### 2. 불필요한 들여쓰기

반대로, 코드 블록이 필요하지 않은 곳에 불필요하게 들여쓰기를 해도 `IndentationError`가 발생할 수 있습니다. (정확히는 `unexpected indent` 오류가 발생합니다.)

**오류 발생 코드:**
```python
x = 10
    print(x) # 불필요한 들여쓰기
```

**해결 방법:**
```python
x = 10
print(x)
```
최상위 레벨의 코드는 들여쓰기 없이 가장 왼쪽에서 시작해야 합니다.

### 3. 탭(Tab)과 공백(Space)의 혼용

눈으로는 잘 보이지 않지만, `IndentationError`를 유발하는 까다로운 원인 중 하나입니다. Python은 탭과 공백을 다른 문자로 취급합니다. 어떤 줄은 탭으로, 다른 줄은 공백으로 들여쓰기를 하면 인터프리터는 이를 다른 들여쓰기 수준으로 인식하여 오류를 발생시킵니다.

**오류 발생 가능성이 있는 코드 (눈으로는 구별 불가):**
```python
if True:
	print("이 줄은 탭으로 들여쓰기")
    print("이 줄은 공백으로 들여쓰기") # -> IndentationError 발생
```

**해결 방법:**

이 문제를 해결하는 가장 좋은 방법은 코드 편집기에서 **탭을 공백으로 자동 변환**하도록 설정하는 것입니다.

-   **Visual Studio Code**: `settings.json` 파일에 `"editor.insertSpaces": true`, `"editor.tabSize": 4` 설정을 추가합니다.
-   **PyCharm**: `Settings > Editor > Code Style > Python` 메뉴에서 `Use tab character` 체크를 해제하고 `Indent`를 4로 설정합니다.

이미 작성된 코드의 탭과 공백을 정리하려면 편집기의 **"Convert Indentation to Spaces"** 와 같은 기능을 사용하세요.

### 결론

`IndentationError`는 Python의 문법 근간을 이루는 들여쓰기의 중요성을 보여주는 오류입니다. 이 오류를 피하기 위해서는 다음 규칙을 기억하는 것이 중요합니다.

1.  **일관성**: 프로젝트 전체에서 하나의 들여쓰기 스타일(공백 4개 권장)을 유지하세요.
2.  **편집기 설정**: 탭 키를 눌렀을 때 공백 4개가 입력되도록 편집기를 설정하세요.
3.  **블록 확인**: `if`, `for`, `def` 등 콜론(`:`)으로 끝나는 줄 다음에는 반드시 들여쓰기된 코드 블록이 와야 합니다.

올바른 들여쓰기 습관은 `IndentationError`를 예방할 뿐만 아니라, 가독성 높은 코드를 작성하는 첫걸음입니다.
