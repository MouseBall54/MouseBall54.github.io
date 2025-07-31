---
typora-root-url: ../
layout: single
title: "파이썬 'TabError: inconsistent use of tabs and spaces in indentation' 오류 해결 방법"
date: 2025-08-01T14:00:00+09:00
header:
   teaser: /images/header_images/overlay_image_python.png
   overlay_image: /images/header_images/overlay_image_python.png
   overlay_filter: 0.5
excerpt: >
  에디터를 설정하여 들여쓰기에 공백을 사용하고 기존 탭을 공백으로 변환하여 파이썬의 "TabError: inconsistent use of tabs and spaces in indentation" 오류를 해결하는 방법을 알아봅니다.
categories:
  - ko_Troubleshooting
tags:
  - Python
  - TabError
  - Indentation
  - Coding Style
---

파이썬은 코드 블록을 정의하기 위해 들여쓰기를 엄격하게 사용하는 독특한 특징이 있습니다. 이러한 공백 의존성은 입문자들이 가장 흔하게 겪는 `TabError: inconsistent use of tabs and spaces in indentation` 오류로 이어질 수 있습니다.

이 오류는 동일한 코드 블록 내에서 들여쓰기를 위해 탭과 공백을 혼용할 때 발생합니다. 파이썬은 둘 다 사용될 경우 들여쓰기 수준을 안정적으로 결정할 수 없습니다. 이 가이드에서는 이 오류를 해결하고 예방하는 방법을 보여줍니다.

### 탭과 공백을 혼용하는 것이 왜 문제인가요?

많은 텍스트 에디터에서 탭 문자는 4개(또는 2개, 8개)의 공백과 동일하게 보일 수 있지만, 파이썬 인터프리터에게는 완전히 다른 문자입니다.

다음 예제를 보세요:
```python
def my_function():
    print("첫 번째 줄")
# 다음 줄은 탭으로 들여쓰기되었으며, 4개의 공백처럼 보일 수 있습니다
	print("두 번째 줄") 
```

만약 첫 번째 `print` 문이 4개의 공백으로 들여쓰기되고 두 번째 문이 단일 탭 문자로 들여쓰기되었다면, 에디터는 완벽하게 정렬된 것처럼 보일 수 있습니다. 하지만 파이썬은 이를 다른 수준의 들여쓰기로 간주하여 `TabError`를 발생시킵니다.

공식 파이썬 스타일 가이드인 **PEP 8**은 **들여쓰기 수준당 4개의 공백**을 사용할 것을 강력히 권장합니다.

### `TabError` 해결 방법

해결책은 한 가지 스타일(가급적 공백)을 선택하고 그것을 고수하는 것입니다.

#### 1단계: 텍스트 에디터 설정하기

이 오류를 예방하는 가장 좋은 방법은 `Tab` 키를 누를 때마다 **탭 대신 공백을 삽입**하도록 코드 에디터나 IDE를 설정하는 것입니다. 이는 종종 "소프트 탭"이라고 불립니다.

-   **Visual Studio Code**: `설정`(Ctrl+,)으로 이동하여 `Insert Spaces`를 검색하고 `Editor: Insert Spaces` 확인란이 선택되어 있는지 확인합니다. 또한 `Editor: Tab Size`를 4로 설정합니다.
-   **PyCharm**: `Settings/Preferences` > `Editor` > `Code Style` > `Python`으로 이동합니다. "Tabs and Indents" 탭에서 `Use tab character`를 선택하고 `Tab size`, `Indent`, `Continuation indent`를 4로 설정합니다.
-   **Sublime Text**: `Preferences` > `Settings`를 열고 사용자 설정 파일에 `"translate_tabs_to_spaces": true` 줄을 추가합니다.

대부분의 최신 에디터에는 들여쓰기를 시각적으로 표시하는 기능이 있어 탭(종종 `→`로 표시됨)과 공백(종종 `·`으로 표시됨)의 차이를 쉽게 발견할 수 있습니다.

#### 2단계: 기존 탭을 공백으로 변환하기

에디터 설정이 완료되면 기존 파일을 수정해야 합니다. 대부분의 에디터에는 탭을 공백으로 변환하는 내장 기능이 있습니다.

-   **VS Code**: 명령 팔레트(Ctrl+Shift+P)를 열고 `Convert Indentation to Spaces`를 입력합니다.
-   **PyCharm**: `Edit` > `Convert Indents` > `To Spaces`로 이동합니다.
-   **Sublime Text**: 메뉴에서 `View` > `Indentation` > `Convert Indentation to Spaces`로 이동합니다.

이렇게 하면 파일의 모든 탭 문자가 적절한 수의 공백으로 자동 변환되어 `TabError`가 즉시 해결됩니다.

#### 3단계: 린터(Linter) 실행하기

이러한 문제를 사전에 발견하려면 `flake8`나 `pylint`와 같은 파이썬 린터를 사용하세요. 이러한 도구는 혼합된 들여쓰기를 포함한 스타일 위반을 위해 코드를 분석하고, 프로그램을 실행하기 전에 문제를 알려줍니다.

터미널에서 `flake8`을 실행할 수 있습니다:
```bash
pip install flake8
flake8 your_script.py
```
`E101: indentation contains mixed spaces and tabs`와 같은 오류를 보고할 것입니다.

### 결론

`TabError`는 파이썬의 중요한 공백 규칙의 직접적인 결과입니다. 에디터를 설정하여 탭 대신 공백을 사용하고 내장 도구를 사용하여 기존 파일을 정리함으로써 이 오류를 완전히 제거할 수 있습니다. 들여쓰기에 4개의 공백을 사용하는 PEP 8 스타일 가이드를 준수하면 모든 파이썬 개발자가 코드를 더 일관성 있고 읽기 쉽게 만들 수 있습니다.
