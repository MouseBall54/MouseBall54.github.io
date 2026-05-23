---
typora-root-url: ../
layout: single
title: >
  Python venv가 활성화되지 않을 때 해결 방법
seo_title: >
  Python venv가 활성화되지 않을 때 해결 방법
date: 2026-05-23T11:00:00+09:00
last_modified_at: 2026-05-23T23:59:59+09:00
lang: ko
translation_id: python-venv-not-activating
header:
   teaser: /images/2026-05-23-python-venv-not-activating/python-venv-not-activating-hero.png
   overlay_image: /images/2026-05-23-python-venv-not-activating/python-venv-not-activating-hero.png
   overlay_filter: 0.5
   image_description: >
     Python venv가 활성화되지 않을 때 해결 방법 주제를 한눈에 설명하는 시각 자료입니다.
excerpt: >
  Python venv 활성화 문제를 shell별 명령 확인, PowerShell 실행 정책 수정, 현재 인터프리터 경로 검증으로 해결하는 방법입니다.
seo_description: >
  Python venv 활성화 문제를 shell별 명령 확인, PowerShell 실행 정책 수정, 현재 인터프리터 경로 검증으로 해결하는 방법입니다.
categories:
  - ko_Troubleshooting
tags:
  - Python
  - venv
  - PowerShell
  - VirtualEnvironment
---

## 문제 상황

`python -m venv .venv`로 Python 가상환경을 만들었는데 활성화되지 않는 것처럼 보일 수 있습니다.
터미널 프롬프트가 바뀌지 않거나, `pip install`이 여전히 전역 환경에 설치되거나, VS Code가 다른 Python interpreter를 계속 사용할 수 있습니다.

![Python venv가 활성화되지 않을 때 해결 방법 설명 이미지](/images/2026-05-23-python-venv-not-activating/python-venv-not-activating-hero.png)

헷갈리는 부분은 프롬프트 변화가 단지 시각적인 단서일 뿐이라는 점입니다.
진짜 확인 기준은 `python`과 `pip`가 가상환경 내부를 가리키는지입니다.

## 원인

`venv` 활성화 실패는 보통 아래 원인 중 하나입니다.

- 현재 shell과 맞지 않는 활성화 명령을 사용했습니다.
- PowerShell 실행 정책 때문에 `Activate.ps1`이 차단되었습니다.
- 프로젝트 폴더가 아닌 다른 위치에서 명령을 실행했습니다.
- `.venv` 폴더가 삭제되었거나 다른 위치에 생성되었습니다.
- VS Code가 다른 interpreter를 선택하고 있습니다.
- 같은 터미널에서 `conda`와 `venv`를 섞어 사용하고 있습니다.
- 프롬프트만 바뀌지 않았을 뿐 실제로는 활성화되었습니다.

해결 방법은 현재 shell에 맞는 활성화 스크립트를 사용하고, Python 실행 파일 경로를 확인하는 것입니다.

## 빠른 해결

현재 사용하는 shell에 맞는 명령을 실행합니다.

### Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

### Windows Command Prompt

```cmd
.venv\Scripts\activate.bat
```

### Windows Git Bash

```bash
source .venv/Scripts/activate
```

### macOS와 Linux

```bash
source .venv/bin/activate
```

그다음 확인합니다.

```bash
python -c "import sys; print(sys.executable)"
python -m pip --version
```

경로에 `.venv`가 포함되어 있다면 프롬프트가 바뀌지 않았더라도 가상환경은 활성화된 것입니다.

## 단계별 해결 방법

### 1. venv 폴더가 있는지 확인

프로젝트 루트에서 `.venv`가 있는지 확인합니다.

Windows PowerShell:

```powershell
Get-ChildItem .venv
```

macOS와 Linux:

```bash
ls .venv
```

폴더가 없다면 새로 만듭니다.

```bash
python -m venv .venv
```

여러 Python 버전이 설치되어 있다면 원하는 interpreter로 가상환경을 만들어야 합니다.

Windows:

```powershell
py -3.12 -m venv .venv
```

macOS와 Linux:

```bash
python3.12 -m venv .venv
```

### 2. 올바른 활성화 스크립트 사용

shell마다 활성화 파일이 다릅니다.

| Shell | 활성화 명령 |
| --- | --- |
| PowerShell | `.\.venv\Scripts\Activate.ps1` |
| Command Prompt | `.venv\Scripts\activate.bat` |
| Windows Git Bash | `source .venv/Scripts/activate` |
| macOS/Linux shell | `source .venv/bin/activate` |

macOS/Linux 명령을 PowerShell에 붙여 넣으면 실패합니다.
반대로 PowerShell 명령을 Git Bash에 붙여 넣어도 실패합니다.

### 3. PowerShell 실행 정책 수정

PowerShell에서 "running scripts is disabled on this system" 같은 메시지가 보인다면 현재 사용자 범위의 실행 정책을 바꿉니다.

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

터미널을 닫고 새 PowerShell 창을 연 뒤 다시 활성화합니다.

```powershell
.\.venv\Scripts\Activate.ps1
```

의도적으로 시스템 전체 정책을 바꾸려는 것이 아니라면 `LocalMachine`이 아니라 `CurrentUser` 범위를 사용하는 것이 좋습니다.

### 4. 활성화된 Python 확인

프롬프트만 믿지 말고 다음 명령을 실행합니다.

```bash
python -c "import sys; print(sys.executable)"
```

정상적인 예시는 다음과 같습니다.

```text
C:\project\.venv\Scripts\python.exe
/home/user/project/.venv/bin/python
```

그다음 `pip`도 확인합니다.

```bash
python -m pip --version
```

이 출력도 `.venv` 내부 경로를 가리켜야 합니다.

### 5. VS Code interpreter 불일치 해결

터미널에서는 가상환경이 활성화되지만 VS Code가 계속 다른 Python으로 실행한다면 interpreter를 직접 선택해야 합니다.

VS Code에서 다음 순서로 진행합니다.

1. Command Palette를 엽니다.
2. `Python: Select Interpreter`를 실행합니다.
3. `.venv` 내부 interpreter를 선택합니다.

선택된 경로는 보통 다음과 비슷해야 합니다.

```text
.venv\Scripts\python.exe
```

또는:

```text
.venv/bin/python
```

선택 후 VS Code 터미널을 새로 열고 다시 확인합니다.

```bash
python -c "import sys; print(sys.executable)"
```

### 6. conda와 venv 혼용 피하기

프롬프트에 Conda 환경과 `.venv`가 동시에 보인다면 환경 관리자가 섞인 상태일 수 있습니다.
단순한 프로젝트라면 먼저 Conda를 비활성화합니다.

```bash
conda deactivate
```

그다음 `.venv`를 다시 활성화합니다.
특별한 이유가 없다면 한 프로젝트에서는 하나의 환경 관리 방식만 사용하는 것이 좋습니다.

## 해결 확인 방법

정상적인 가상환경은 아래 확인을 통과해야 합니다.

```bash
python -c "import sys; print(sys.executable)"
python -m pip --version
python -c "import site; print(site.getsitepackages())"
```

출력 경로에 `.venv`가 포함되어야 합니다.

작은 패키지를 설치해 실제 설치 위치도 확인합니다.

```bash
python -m pip install requests
python -m pip show requests
```

`pip show` 경로가 `.venv`를 가리킨다면 활성화와 설치가 모두 정상입니다.

## 흔한 실수

- PowerShell에서 `source .venv/bin/activate`를 실행합니다.
- `.venv`가 없는 폴더에서 `Activate.ps1`을 실행합니다.
- 프롬프트가 바뀌지 않았다는 이유만으로 활성화 실패라고 판단합니다.
- 잘못된 Python으로 활성화한 뒤 단독 `pip`로 패키지를 설치합니다.
- VS Code에서 다른 interpreter를 선택한 상태로 실행합니다.
- `sys.executable`을 확인하지 않고 Conda와 `venv`를 섞어 사용합니다.

## 관련 글

- [Python pip install 실패 해결 방법](/ko_Troubleshooting/python-pip-install-failed/)
- [Python No module named pip 오류 해결 방법](/ko_Troubleshooting/python-no-module-named-pip/)
- [Python ModuleNotFoundError 해결 방법](/ko_Troubleshooting/python-modulenotfounderror/)

## 자주 묻는 질문

### 이 글은 언제 먼저 적용하면 좋나요?

오류 메시지, 실행한 명령, 사용 중인 OS와 버전을 먼저 기록한 뒤 이 글의 원인별 순서대로 확인하는 것이 좋습니다.

### 초보자가 가장 먼저 확인할 부분은 무엇인가요?

처음에는 환경 변수, 설치 경로, 권한, 캐시처럼 재현 가능성이 높은 항목부터 확인하세요. 그다음 로그와 설정 파일을 비교하면 원인을 좁히기 쉽습니다.

### 더 찾아볼 때 어떤 키워드를 쓰면 좋나요?

추가 검색할 때는 "Python venv가 활성화되지 않을 때 해결 방법" 같은 핵심 문구와 error message, version, Windows, GitHub Pages, Jekyll 같은 실제 환경 키워드를 붙이면 더 정확한 결과를 얻기 쉽습니다.
