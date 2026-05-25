---
typora-root-url: ../
layout: single
title: "Python ModuleNotFoundError 해결 방법"

date: 2025-01-20T07:24:00+09:00
lang: ko
translation_id: python-modulenotfounderror
excerpt: "Python에서 발생하는 ModuleNotFoundError: No module named '...' 오류의 원인을 파악하고, 이를 해결하기 위한 다양한 방법을 알아봅니다."
seo_description: "Python에서 발생하는 ModuleNotFoundError: No module named '...' 오류의 원인을 파악하고, 이를 해결하기 위한 다양한 방법을 알아봅니다."
header:
   teaser: /images/header_images/overlay_image_python.png
   overlay_image: /images/header_images/overlay_image_python.png
   overlay_filter: 0.5
   image_description: >
     이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Python ModuleNotFoundError 해결 방법
categories:
  - ko_Troubleshooting
tags:
  - Python
  - ModuleNotFoundError
  - pip
  - Modules
  - Error Handling
---


![이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Python ModuleNotFoundError 해결 방법](/images/header_images/overlay_image_python.png)
## `ModuleNotFoundError`란 무엇인가?

`ModuleNotFoundError`는 가져오려는(import) 모듈을 Python이 찾을 수 없을 때 발생하는 예외다. 이 오류는 Python 3.6부터 도입되었으며, 이전 버전에서는 `ImportError`가 발생했다. 이는 초보자부터 숙련된 개발자까지, 특히 새로운 프로젝트나 환경을 설정할 때 가장 흔하게 겪는 문제 중 하나다.

오류 메시지는 보통 매우 명확하다.
`ModuleNotFoundError: No module named 'some_module'`

이는 Python이 설치된 모듈 목록에서 `some_module`을 찾아봤지만 찾지 못했다는 의미다.

## `ModuleNotFoundError`의 일반적인 원인

- **모듈이 설치되지 않음:** 가장 흔한 원인으로, 사용 중인 Python 환경에 해당 모듈이 설치되어 있지 않은 경우다.
- **모듈 이름의 오타:** `import` 문에서 모듈 이름을 잘못 입력했을 수 있다.
- **잘못된 Python 환경:** 여러 Python 설치 버전이나 가상 환경이 있을 때, 모듈은 한 환경에 설치되어 있는데 스크립트는 다른 환경에서 실행하고 있을 수 있다.
- **순환 종속성:** 드물게, 두 개 이상의 모듈이 서로를 순환적으로 가져오는 경우 가져오기 문제가 발생할 수 있다.

## `ModuleNotFoundError` 해결 방법

이 오류를 해결하고 수정하는 방법은 다음과 같다.

### 1. `pip`로 누락된 모듈 설치

모듈이 설치되어 있지 않다면, 보통 Python의 패키지 설치 프로그램인 `pip`를 사용해 설치할 수 있다. 터미널이나 명령 프롬프트를 열고 다음을 실행하자.

```bash
pip install some_module
```

`some_module`을 필요한 실제 모듈 이름으로 바꾸면 된다. 예를 들어, 인기 있는 `requests` 라이브러리를 설치하려면 다음을 실행한다.

```bash
pip install requests
```

**참고:** 때로는 `pip`로 설치하는 패키지 이름이 가져오는 모듈 이름과 다를 수 있다. 예를 들어, `cv2` 모듈을 사용하려면 `opencv-python`을 설치해야 한다. 보통 인터넷에서 간단히 검색하면 올바른 패키지 이름을 찾을 수 있다.

### 2. 오타 확인

`import` 문에 철자 오류가 있는지 주의 깊게 확인하자. 쉽게 저지를 수 있는 실수다.

```python
# 잘못된 예: 'requests'에 오타
import reqeusts 

# 올바른 예
import requests
```

### 3. Python 환경 확인

여러 버전의 Python(예: Python 2.7과 Python 3.8)이 설치되어 있거나 가상 환경을 사용하는 경우, 스크립트를 실행하는 환경과 동일한 환경에 패키지를 설치하고 있는지 확인해야 한다.

다음 명령으로 사용 중인 Python 버전을 확인할 수 있다.

```bash
python --version
# 또는
python3 --version
```

사용 중인 Python 환경에 맞는 `pip`를 사용하려면, `pip`를 모듈로 실행할 수 있다.

```bash
python -m pip install some_module
```

이 명령은 현재 실행 중인 `python` 실행 파일에 대해 패키지가 설치되도록 보장한다.

### 4. 가상 환경 이해하기

가상 환경은 Python 개발의 모범 사례다. 각 프로젝트마다 고유한 설치된 패키지 집합을 가진 격리된 환경을 만들 수 있게 해준다.

가상 환경(`venv`나 `conda`로 생성)을 사용하는 경우, 패키지를 설치하거나 스크립트를 실행하기 전에 해당 환경을 **활성화**했는지 확인해야 한다.

**`venv` 환경을 활성화하려면:**

- **Windows:** `my-env\Scripts\activate`
- **macOS/Linux:** `source my-env/bin/activate`

활성화되면 터미널 프롬프트가 보통 환경 이름을 표시하도록 변경된다. 그 후 `pip install` 명령은 활성화된 환경에만 적용된다.

## 결론

`ModuleNotFoundError`는 보통 쉽게 해결할 수 있는 흔한 장애물이다. 올바른 `pip`로 모듈을 설치하고, 오타를 확인하며, 올바른 Python 환경에서 작업하고 있는지 확인함으로써 이 오류를 신속하게 해결하고 코딩으로 돌아갈 수 있다. 프로젝트 시작부터 가상 환경을 사용하는 것은 이러한 문제를 전반적으로 예방하는 좋은 방법이다.

## 전문 보완 체크

**Python ModuleNotFoundError 해결 방법**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 인터프리터 경로, 가상환경, 패키지 버전, 입력 파일 또는 데이터 경계를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

### 신뢰도를 높이는 증거

작업을 바꾸기 전에는 객관적인 증거를 먼저 확인해야 합니다. 쓸 만한 증거에는 `python --version`, `python -m pip show`, 전체 traceback, 최소 재현 스크립트가 포함됩니다. 증거가 서로 맞지 않으면 억지로 하나의 이야기로 합치지 말고 충돌 자체를 남겨야 합니다. 빠른 해결이 한 번 성공했더라도 같은 입력, 계정, 의존성, 기기 상태에서 다시 확인하지 않았다면 아직 확정된 해결책이라고 보기 어렵습니다.

### 검토 표

| 검토 항목 | 확인할 내용 | 중요한 이유 |
| --- | --- | --- |
| 범위 | 이 글이 다루는 정확한 사례 | 조언을 과도하게 적용하지 않게 합니다 |
| 기준 상태 | 변경 전 상태 | 되돌리기와 비교를 가능하게 합니다 |
| 변경 | 실제로 수행한 가장 작은 조치 | 숨은 부작용을 줄입니다 |
| 결과 | 변경 뒤 관찰한 출력 또는 반응 | 기대와 증거를 구분합니다 |
| 재확인 | 결론을 다시 볼 시점 | 글의 정확도를 유지합니다 |

### 예외 상황과 실패 모드

주요 위험은 증상만 고치고 원인을 남기는 상황, 서로 무관한 변경을 같은 테스트에 섞는 상황입니다. 생산 데이터, 개인정보, 돈, 건강, 법적 권리, 보안 복구가 관련되어 있다면 넓은 해결책을 바로 적용하기보다 먼저 증거를 모으는 보수적인 접근이 낫습니다. 같은 제목의 문제라도 환경이 다르면 원인이 달라질 수 있으므로, 독자는 명령이나 결정을 복사하기 전에 자신의 조건이 글의 가정과 맞는지 비교해야 합니다.

### 유지보수 기준

이 안내는 의존성, 운영체제, 빌드 도구가 바뀐 뒤 다시 확인해야 합니다. 좋은 업데이트는 글 전체를 다시 쓰는 것이 아니라 예시, 링크, 명령, 화면, 판단 기준이 현재 동작과 여전히 맞는지 확인하는 일입니다. 기존 결론이 유효하면 확인 날짜를 남기고, 바뀌었다면 무엇이 바뀌었고 왜 이전 조언만으로 부족한지 설명해야 합니다.

### 실행 전 질문

- 문제나 판단이 실제임을 보여 주는 가장 작은 관찰 신호는 무엇인가?
- 공식 출처는 무엇이고, 내부 판단은 어느 부분인가?
- 변경 전에 반드시 캡처해야 할 기록은 무엇인가?
- 어떤 결과가 나오면 이 글의 조언이 맞지 않는다고 볼 것인가?
- 같은 문제가 반복될 때 누가 이 기록을 다시 봐야 하는가?

## 함께 보면 좋은 글

같은 주제 흐름에서 이어서 읽기 좋은 글입니다.

- [SSL: CERTIFICATE_VERIFY_FAILED 오류 해결 방법 (Windows Python)](/ko_troubleshooting/python-certificate-verify-failed/)
- [Permission denied (publickey) 오류 해결 방법 (Windows Git SSH)](/ko_troubleshooting/git-permission-denied-publickey-windows/)
