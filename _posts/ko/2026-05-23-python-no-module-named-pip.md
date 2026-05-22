---
typora-root-url: ../
layout: single
title: >
  Python No module named pip 오류 해결 방법
seo_title: >
  Python No module named pip 오류 해결 방법
date: 2026-05-23T10:00:00+09:00
lang: ko
translation_id: python-no-module-named-pip
header:
   teaser: /images/2026-05-23-python-no-module-named-pip/python-no-module-named-pip-hero.png
   overlay_image: /images/2026-05-23-python-no-module-named-pip/python-no-module-named-pip-hero.png
   overlay_filter: 0.5
excerpt: >
  Python의 No module named pip 오류를 ensurepip 실행, 현재 인터프리터 확인, 가상환경 복구로 해결하는 방법입니다.
seo_description: >
  Python의 No module named pip 오류를 ensurepip 실행, 현재 인터프리터 확인, 가상환경 복구로 해결하는 방법입니다.
categories:
  - ko_Troubleshooting
tags:
  - Python
  - pip
  - ensurepip
  - Environment
---

## 문제 상황

`pip`를 실행하려고 했는데 Python이 `pip` 모듈을 찾지 못하는 경우가 있습니다.

![Python No module named pip 오류 해결 방법 설명 이미지](/images/2026-05-23-python-no-module-named-pip/python-no-module-named-pip-hero.png)

오류는 보통 다음처럼 나타납니다.

```text
No module named pip
```

다음 명령을 실행할 때도 같은 오류가 날 수 있습니다.

```bash
python -m pip --version
```

이 오류는 일반적인 패키지 설치 실패와 다릅니다.
이 경우 Python 자체는 실행되지만, 현재 사용 중인 Python 환경 안에 `pip` 설치 도구가 없는 상태입니다.

단독 `pip` 명령은 다른 Python 설치를 가리킬 수 있어 혼란을 줄 수 있습니다.
따라서 문제를 진단할 때는 `python -m pip`를 사용하고, Windows에서는 `py -m pip`도 함께 확인하는 것이 좋습니다.

## 원인

`No module named pip`는 보통 아래 원인 중 하나로 발생합니다.

- Python을 설치할 때 `pip`가 함께 설치되지 않았습니다.
- Python 설치가 불완전하거나 손상되었습니다.
- 가상환경이 `pip` 없이 생성되었습니다.
- 현재 터미널이 예상과 다른 Python을 가리키고 있습니다.
- system-managed Python 패키지가 기본적으로 `pip`를 포함하지 않습니다.
- 환경에서 `pip` 패키지가 삭제되었습니다.

가장 안전한 해결 방법은 실제로 사용할 Python 인터프리터에 대해 `pip`를 복구하는 것입니다.

## 빠른 해결

먼저 `ensurepip`를 시도합니다.
`ensurepip`는 많은 표준 Python 설치에 포함된 `pip` bootstrap 도구입니다.

### Windows

```powershell
py -m ensurepip --upgrade
py -m pip install --upgrade pip
py -m pip --version
```

### macOS와 Linux

```bash
python3 -m ensurepip --upgrade
python3 -m pip install --upgrade pip
python3 -m pip --version
```

프로젝트에서 `python3`가 아닌 다른 명령을 사용한다면, 해당 인터프리터 명령으로 바꿔 실행합니다.
예를 들면 다음과 같습니다.

```bash
python -m ensurepip --upgrade
python -m pip --version
```

## 단계별 해결 방법

### 1. 어떤 Python을 사용하는지 확인

무언가를 다시 설치하기 전에 현재 Python 경로를 확인합니다.

```bash
python -c "import sys; print(sys.executable)"
python -c "import sys; print(sys.version)"
```

Windows에서는 설치된 Python 목록을 다음 명령으로 확인할 수 있습니다.

```powershell
py -0p
```

경로가 예상한 Python 설치가 아니라면 그 문제를 먼저 해결해야 합니다.
그렇지 않으면 한 Python 설치에 `pip`를 복구해 놓고, 실제 프로젝트는 다른 Python으로 실행하는 상황이 생깁니다.

### 2. ensurepip로 pip 복구

다음 명령을 실행합니다.

```bash
python -m ensurepip --upgrade
```

이후 `pip`를 최신 버전으로 올립니다.

```bash
python -m pip install --upgrade pip
```

마지막으로 확인합니다.

```bash
python -m pip --version
```

출력에는 `pip` 버전과 함께 현재 Python 설치 또는 가상환경 내부 경로가 보여야 합니다.

### 3. pip가 없는 가상환경 복구

가상환경 안에서 오류가 발생한다면, 해당 환경이 `pip` 없이 생성되었을 수 있습니다.

먼저 가상환경을 활성화합니다.

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

macOS와 Linux:

```bash
source .venv/bin/activate
```

그다음 실행합니다.

```bash
python -m ensurepip --upgrade
python -m pip install --upgrade pip
python -m pip --version
```

환경이 작고 다시 만들기 쉽다면, 새로 만드는 것이 가장 깔끔할 때도 있습니다.

```bash
python -m venv .venv
```

완전히 다시 만들 필요가 있다면 기존 가상환경 폴더를 삭제한 뒤, 같은 Python 버전으로 새 환경을 생성합니다.

### 4. ensurepip가 없는 경우 확인

일부 Linux 배포판은 `pip`를 별도 패키지로 제공합니다.
이 경우 `ensurepip`가 비활성화되어 있거나 없을 수 있습니다.

그럴 때는 system package manager로 `pip`를 설치하거나, `ensurepip`가 포함된 Python 설치로 프로젝트 가상환경을 만드는 방식을 사용합니다.

예시:

```bash
sudo apt install python3-pip
```

또는:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip --version
```

package manager는 system Python을 위한 용도로만 사용하는 것이 좋습니다.
프로젝트 의존성 설치는 가상환경 안에서 처리하는 것이 안전합니다.

### 5. pip와 Python 혼동 방지

`pip`를 복구한 뒤에도, 해당 명령이 올바른 인터프리터를 가리키는지 확인하기 전까지는 단독 `pip` 사용을 피하는 것이 좋습니다.

다음처럼 실행합니다.

```bash
python -m pip install package-name
```

대신 아래 명령은 신중하게 사용합니다.

```bash
pip install package-name
```

이렇게 하면 `pip`는 한 Python 버전에 설치하고, 스크립트는 다른 Python으로 실행하는 흔한 불일치를 줄일 수 있습니다.

## 해결 확인 방법

다음 명령을 실행합니다.

```bash
python -m pip --version
python -m pip list
python -c "import sys; print(sys.executable)"
```

`pip --version`의 경로가 `sys.executable`로 확인한 환경과 일치해야 합니다.

실제 설치도 테스트합니다.

```bash
python -m pip install requests
python -c "import requests; print(requests.__version__)"
```

이 명령이 성공하면 `pip`가 정상적으로 복구된 것입니다.

## 흔한 실수

- 한 Python 버전에 `pip`를 설치하고 프로젝트는 다른 Python으로 실행합니다.
- `python -m pip --version`을 확인하기 전에 단독 `pip`를 사용합니다.
- 가상환경을 다시 만들고 활성화하는 것을 잊습니다.
- 가상환경으로 해결할 수 있는데 관리자 권한 설치를 먼저 시도합니다.
- `No module named pip`를 `No module named requests`와 같은 문제로 처리합니다. 전자는 `pip` 자체가 없는 것이고, 후자는 프로젝트 패키지가 없는 것입니다.

## 관련 글

- [Python pip install 실패 해결 방법](/ko_Troubleshooting/python-pip-install-failed/)
- [Python ModuleNotFoundError 해결 방법](/ko_Troubleshooting/python-modulenotfounderror/)
- [Python PermissionError: [Errno 13] Permission denied 해결 방법](/ko_Troubleshooting/python-permissionerror-errno-13-permission-denied/)

