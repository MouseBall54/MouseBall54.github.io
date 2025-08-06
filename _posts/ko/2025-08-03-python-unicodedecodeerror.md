---
typora-root-url: ../
layout: single
title: >
    파이썬 "UnicodeDecodeError: 'utf-8' codec can't decode byte" 오류 해결 방법

lang: ko
translation_id: python-unicodedecodeerror
header:
   teaser: /images/header_images/overlay_image_python.png
   overlay_image: /images/header_images/overlay_image_python.png
   overlay_filter: 0.5
excerpt: >
    파이썬의 "UnicodeDecodeError"를 해결합니다. 이 오류는 기본 'utf-8' 코덱과 일치하지 않는 인코딩으로 파일을 읽을 때 발생합니다.
categories:
  - ko_Troubleshooting
tags:
  - Python
  - UnicodeDecodeError
  - Encoding
  - File I/O
---

## UnicodeDecodeError란?

`UnicodeDecodeError`는 파이썬에서 발생합니다.
파일을 읽으려고 할 때 일어납니다.
파일의 인코딩이 예상과 다를 때입니다.
파이썬 3는 기본으로 'utf-8' 인코딩을 사용합니다.
파일이 다른 인코딩으로 저장되면 이 오류가 나타납니다.
"'utf-8' codec can't decode byte..." 메시지가 표시됩니다.
파일의 특정 바이트가 'utf-8' 형식이 아니라는 뜻입니다.

## 주요 원인과 해결 방법

이 오류의 주된 원인은 하나입니다. 파일 인코딩이 잘못된 것입니다.

### 1. 다른 인코딩으로 파일 읽기

파일은 'cp949', 'euc-kr', 'latin-1' 등으로 저장될 수 있습니다.
파이썬이 이 파일을 'utf-8'로 읽으려 하면 오류가 발생합니다.

**문제 코드:**
```python
# 이 코드는 'my_data.csv' 파일이 utf-8로 인코딩되었다고 가정합니다.
# 그렇지 않으면 UnicodeDecodeError가 발생합니다.
with open('my_data.csv', 'r') as f:
    content = f.read()
print(content)
```

**해결 방법:**
정확한 인코딩을 지정해야 합니다.
`open()` 함수에서 `encoding` 파라미터를 사용하세요.

먼저 파일의 실제 인코딩을 찾아야 합니다.
Notepad++나 VS Code 같은 텍스트 에디터로 확인할 수 있습니다.
또는 파이썬의 `chardet` 라이브러리를 사용할 수도 있습니다.

```bash
pip install chardet
```

인코딩을 알았다면 적용합니다.
파일 인코딩이 'cp949'라고 가정해 봅시다.

**수정된 코드:**
```python
# 'cp949'와 같이 정확한 인코딩을 지정합니다.
try:
    with open('my_data.csv', 'r', encoding='cp949') as f:
        content = f.read()
    print(content)
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
except UnicodeDecodeError:
    print("파일이 cp949로 인코딩되지 않았습니다.")
```

### 2. 잠재적인 인코딩 오류 처리

때로는 인코딩을 확신할 수 없습니다.
또는 파일에 몇 개의 잘못된 문자가 포함될 수 있습니다.
이 경우 `errors` 파라미터를 사용할 수 있습니다.

**오류 처리 코드:**
```python
# 'errors' 파라미터는 파이썬에게 인코딩 오류 처리 방법을 알려줍니다.
# 'ignore': 문제가 되는 문자를 건너뜁니다.
# 'replace': 문제가 되는 문자를 대체 문자(예: '?')로 바꿉니다.

with open('my_data.csv', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()
print(content)
```
이 방법은 프로그램 충돌을 막습니다.
하지만 데이터 손실이나 손상을 유발할 수 있습니다.
완벽한 데이터 무결성이 중요하지 않을 때만 사용하세요.

## 모범 사례

- **항상 인코딩을 지정하세요.** 기본값에 의존하지 마세요. `open('file.txt', 'r', encoding='utf-8')`가 가장 좋은 방법입니다.
- **파일을 'utf-8'로 저장하세요.** 파일을 쓸 때 'utf-8'을 사용하세요. 가장 널리 지원되는 표준입니다.
- **데이터를 파악하세요.** 파일의 출처와 예상되는 인코딩을 이해하세요.

파일 인코딩을 명시적으로 관리하면 `UnicodeDecodeError`를 예방할 수 있습니다. 코드가 더 안정적이고 신뢰성 있게 됩니다.
