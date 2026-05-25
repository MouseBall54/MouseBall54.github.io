---
typora-root-url: ../
layout: single
title: >
  Windows에서 python 명령어가 안 될 때 해결 방법
seo_title: >
  Windows에서 python 명령어가 안 될 때 해결 방법
date: 2024-11-10T07:50:00+09:00
last_modified_at: 2026-05-23T23:59:59+09:00
lang: ko
translation_id: python-command-not-found-windows
header:
   teaser: /images/2026-05-23-python-command-not-found-windows/python-command-not-found-windows-hero.png
   overlay_image: /images/2026-05-23-python-command-not-found-windows/python-command-not-found-windows-hero.png
   overlay_filter: 0.5
   image_description: >
     Windows에서 python 명령어가 안 될 때 해결 방법 주제를 한눈에 설명하는 시각 자료입니다.
excerpt: >
  Windows에서 python 명령어가 안 될 때 py launcher, PATH, App Execution Alias, 현재 Python 설치 경로를 확인해 해결하는 방법입니다.
seo_description: >
  Windows에서 python 명령어가 안 될 때 py launcher, PATH, App Execution Alias, 현재 Python 설치 경로를 확인해 해결하는 방법입니다.
categories:
  - ko_Troubleshooting
tags:
  - Python
  - Windows
  - PATH
  - py
---

## 문제 상황

Windows PowerShell이나 Command Prompt에서 다음 명령을 실행합니다.

![Windows에서 python 명령어가 안 될 때 해결 방법 설명 이미지](/images/2026-05-23-python-command-not-found-windows/python-command-not-found-windows-hero.png)

```powershell
python --version
```

그런데 아래와 같은 오류가 나올 수 있습니다.

```text
python is not recognized as an internal or external command
```

또는 다음 메시지가 표시될 수 있습니다.

```text
Python was not found; run without arguments to install from the Microsoft Store
```

이 문제는 보통 Windows가 `PATH`에서 `python.exe`를 찾지 못하거나, Microsoft Store App Execution Alias가 `python` 명령을 가로챌 때 발생합니다.

## 원인

Windows에서 `python command not found` 문제가 발생하는 원인은 보통 다음 중 하나입니다.

- Python이 설치되어 있지 않습니다.
- Python은 설치되어 있지만 설치 폴더가 `PATH`에 없습니다.
- Microsoft Store App Execution Alias가 `python` 명령을 가로채고 있습니다.
- Python 설치 후 터미널을 새로 열지 않았습니다.
- 여러 Python 버전이 설치되어 있고 Windows가 잘못된 버전을 먼저 찾습니다.
- Python은 설치되어 있지만 `py` launcher만 동작합니다.
- 활성 Python을 확인하기 전에 `pip`부터 사용하고 있습니다.

가장 빠른 확인 방법은 `py` launcher가 Python을 찾을 수 있는지 보는 것입니다.

## 빠른 해결

PowerShell에서 다음 명령을 실행합니다.

```powershell
py --version
py -0p
where python
where py
```

`py --version`이 동작한다면 Python은 설치되어 있고 Python launcher가 이를 찾을 수 있다는 뜻입니다.
이 경우 다음처럼 사용할 수 있습니다.

```powershell
py script.py
py -m pip --version
py -m pip install package-name
```

`py`는 동작하지만 `python`은 동작하지 않는다면 보통 `PATH` 또는 App Execution Alias 문제입니다.

## 단계별 해결 방법

### 1. Python 설치 여부 확인

먼저 다음 명령을 실행합니다.

```powershell
py --version
```

Python 버전이 출력되면 launcher를 통해 Python을 사용할 수 있습니다.

launcher가 인식하는 Python 버전 목록도 확인합니다.

```powershell
py -0p
```

출력 예시는 다음과 같습니다.

```text
 -V:3.12 *        C:\Users\you\AppData\Local\Programs\Python\Python312\python.exe
 -V:3.11          C:\Users\you\AppData\Local\Programs\Python\Python311\python.exe
```

`py`도 찾을 수 없다면 공식 Python 웹사이트 또는 사용하는 package manager로 Python을 설치한 뒤, 터미널을 새로 열어야 합니다.

### 2. Windows가 찾는 python 명령 확인

다음 명령을 실행합니다.

```powershell
where python
```

정상적인 Python 경로가 나올 수 있습니다.

```text
C:\Users\you\AppData\Local\Programs\Python\Python312\python.exe
```

또는 WindowsApps alias가 나올 수 있습니다.

```text
C:\Users\you\AppData\Local\Microsoft\WindowsApps\python.exe
```

`WindowsApps`를 가리킨다면 Windows가 실제 Python 설치 대신 Microsoft Store alias를 사용하고 있을 수 있습니다.

### 3. Microsoft Store App Execution Alias 끄기

Windows가 Microsoft Store를 열거나 "Python was not found" 메시지를 보여준다면 alias를 끕니다.

순서:

1. Windows Settings를 엽니다.
2. `Apps`로 이동합니다.
3. `Advanced app settings`를 엽니다.
4. `App execution aliases`를 엽니다.
5. `python.exe`를 끕니다.
6. `python3.exe`를 끕니다.
7. PowerShell 또는 Command Prompt를 닫고 새로 엽니다.

그다음 다시 확인합니다.

```powershell
python --version
where python
```

그래도 `python`이 동작하지 않으면 Python을 `PATH`에 추가해야 합니다.

### 4. Python을 PATH에 추가

Python 설치 경로를 확인합니다.

```powershell
py -0p
```

사용자별 설치라면 보통 다음과 비슷한 경로입니다.

```text
C:\Users\you\AppData\Local\Programs\Python\Python312\
C:\Users\you\AppData\Local\Programs\Python\Python312\Scripts\
```

두 경로를 사용자 `PATH`에 추가합니다.

순서:

1. Windows Search를 엽니다.
2. `Environment Variables`를 검색합니다.
3. `Edit environment variables for your account`를 엽니다.
4. `Path`를 선택합니다.
5. `Edit`을 클릭합니다.
6. Python 폴더를 추가합니다.
7. `Scripts` 폴더를 추가합니다.
8. 저장합니다.
9. 터미널을 새로 엽니다.

기존 터미널에서 바로 테스트하지 마세요.
환경 변수 변경은 새 터미널 세션부터 적용됩니다.

### 5. Python 버전이 여러 개라면 py 사용

Python 버전이 여러 개라면 `python`보다 `py` launcher가 더 명확할 수 있습니다.

예시:

```powershell
py -3.12 --version
py -3.12 -m pip --version
py -3.12 script.py
```

이렇게 하면 `PATH`에서 어떤 `python.exe`가 먼저 잡히는지 추측하지 않아도 됩니다.

### 6. Python이 동작한 뒤 pip 확인

`python` 또는 `py`가 동작한 뒤 `pip`를 확인합니다.

```powershell
py -m pip --version
python -m pip --version
```

`py -m pip`는 동작하지만 `python -m pip`가 동작하지 않는다면, 계속 `py -m pip`를 사용하거나 `python` 명령 경로를 수정해야 합니다.

처음부터 단독 `pip` 명령을 사용하지 않는 것이 좋습니다.
먼저 어떤 Python interpreter를 사용하는지 확인해야 합니다.

## 해결 확인 방법

다음 명령을 실행합니다.

```powershell
py --version
py -0p
where python
python --version
py -m pip --version
```

정상적인 상태라면 다음을 확인할 수 있어야 합니다.

- `py`가 하나 이상의 Python 버전을 찾습니다.
- `where python`이 `WindowsApps`만 가리키지 않고 실제 Python 설치를 가리킵니다.
- `python --version`이 예상한 버전을 출력합니다.
- `py -m pip --version`이 동작합니다.

간단한 Python 명령도 테스트합니다.

```powershell
py -c "import sys; print(sys.executable)"
```

출력은 사용하려는 Python 설치 경로를 가리켜야 합니다.

## 흔한 실수

- `PATH`를 수정하고 기존 터미널에서 바로 테스트합니다.
- Microsoft Store `python.exe` alias를 켜 둔 상태로 둡니다.
- Python 설치 중 "Add python.exe to PATH" 옵션을 확인하지 않습니다.
- `py -m pip --version`을 확인하기 전에 `pip`부터 사용합니다.
- Python 버전이 여러 개인데 `python`이 최신 버전을 가리킨다고 가정합니다.
- Python 폴더만 `PATH`에 추가하고 `Scripts` 폴더는 추가하지 않습니다.

## 전문 보완 체크

**Windows에서 python 명령어가 안 될 때 해결 방법**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 인터프리터 경로, 가상환경, 패키지 버전, 입력 파일 또는 데이터 경계를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

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

## 관련 글

- [Python pip install 실패 해결 방법](/ko_troubleshooting/python-pip-install-failed/)
- [Python No module named pip 오류 해결 방법](/ko_troubleshooting/python-no-module-named-pip/)
- [Python venv가 활성화되지 않을 때 해결 방법](/ko_troubleshooting/python-venv-not-activating/)

## 자주 묻는 질문

### 이 글은 언제 먼저 적용하면 좋나요?

오류 메시지, 실행한 명령, 사용 중인 OS와 버전을 먼저 기록한 뒤 이 글의 원인별 순서대로 확인하는 것이 좋습니다.

### 초보자가 가장 먼저 확인할 부분은 무엇인가요?

처음에는 환경 변수, 설치 경로, 권한, 캐시처럼 재현 가능성이 높은 항목부터 확인하세요. 그다음 로그와 설정 파일을 비교하면 원인을 좁히기 쉽습니다.

### 더 찾아볼 때 어떤 키워드를 쓰면 좋나요?

추가 검색할 때는 "Windows에서 python 명령어가 안 될 때 해결 방법" 같은 핵심 문구와 error message, version, Windows, GitHub Pages, Jekyll 같은 실제 환경 키워드를 붙이면 더 정확한 결과를 얻기 쉽습니다.
