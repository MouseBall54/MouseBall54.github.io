---
typora-root-url: ../
layout: single
title: >
  VS Code Python Interpreter가 보이지 않을 때 해결 방법
seo_title: >
  VS Code Python Interpreter Not Showing 해결
date: 2026-05-23T23:59:59+09:00
lang: ko
translation_id: vscode-python-interpreter-not-showing
header:
   teaser: /images/2026-05-23-vscode-python-interpreter-not-showing/vscode-python-interpreter-hero.png
   overlay_image: /images/2026-05-23-vscode-python-interpreter-not-showing/vscode-python-interpreter-hero.png
   overlay_filter: 0.35
excerpt: >
  VS Code에서 Python interpreter가 보이지 않을 때 Python extension, workspace folder, virtual environment 위치, manual path 선택, terminal 환경을 확인합니다.
seo_description: >
  VS Code에서 Python interpreter가 보이지 않을 때 Python extension, workspace folder, virtual environment 위치, manual path 선택, terminal 환경을 확인합니다.
categories:
  - ko_Troubleshooting
tags:
  - Python
  - VSCode
  - VirtualEnvironment
  - Interpreter
  - Windows
---

## 핵심 요약

VS Code에서 Python interpreter가 보이지 않는다면 먼저 Python extension이 설치되어 있고, 단일 파일이 아니라 project folder를 열었는지 확인합니다.
그 다음 virtual environment를 만들거나 위치를 찾고, **Python: Select Interpreter**에서 직접 path를 선택합니다.

![VS Code Python interpreter picker에서 환경이 보이지 않는 상황과 복구 경로를 보여주는 이미지](/images/2026-05-23-vscode-python-interpreter-not-showing/vscode-python-interpreter-hero.png)

이미지는 흔한 상황을 보여줍니다.
editor는 열려 있지만 기대한 environment가 picker에 없습니다.
extension, workspace, environment path, reload, terminal 상태를 차례로 확인하면 됩니다.

## 1. Python Extension 확인

VS Code Extensions에서 Microsoft Python extension이 설치되고 enabled 상태인지 확인합니다.
그 다음 window를 reload합니다.

```text
Developer: Reload Window
```

extension이 workspace에서 disabled 상태라면 interpreter picker가 정상적으로 동작하지 않을 수 있습니다.

## 2. Project Folder 열기

VS Code는 workspace folder가 열려 있을 때 environment를 더 잘 찾습니다.

```text
File > Open Folder
```

단일 `.py` 파일만 열지 마세요.
virtual environment는 보통 workspace folder 기준으로 탐지됩니다.

좋은 프로젝트 구조:

```text
my-project/
  .venv/
  src/
  pyproject.toml
```

`.venv`가 workspace 밖에 있으면 자동 탐지가 실패할 수 있습니다.
그래도 manual selection은 가능합니다.

## 3. Virtual Environment 만들기

project folder에서 실행합니다.

```bash
python -m venv .venv
```

Windows activation:

```powershell
.\.venv\Scripts\Activate.ps1
```

macOS 또는 Linux:

```bash
source .venv/bin/activate
```

그 다음 VS Code를 reload하고 실행합니다.

```text
Python: Select Interpreter
```

`.venv`가 workspace 안에 있다면 보통 목록에 나타납니다.

## 4. Interpreter Path 직접 선택

그래도 보이지 않으면 아래를 선택합니다.

```text
Python: Select Interpreter
Enter interpreter path
```

자주 쓰는 path:

Windows:

```text
.\.venv\Scripts\python.exe
```

macOS 또는 Linux:

```text
./.venv/bin/python
```

선택 후 VS Code는 workspace에 interpreter 선택을 저장합니다.

## 5. Terminal과 VS Code가 같은 Python을 쓰는지 확인

VS Code terminal에서 실행합니다.

```bash
python --version
python -c "import sys; print(sys.executable)"
```

path가 선택한 interpreter와 다르면 새 terminal을 엽니다.
기존 terminal은 이전 environment를 유지할 수 있습니다.

다음 command도 도움이 됩니다.

```text
Python: Create Environment
Python: Select Interpreter
Python: Clear Workspace Interpreter Setting
```

workspace 설정이 꼬였을 때 reset할 수 있습니다.

## 6. Windows Execution Policy 확인

Windows에서는 PowerShell이 script 실행을 막아 activation이 실패할 수 있습니다.
activation이 실패해도 manual interpreter selection은 가능하지만, terminal environment가 활성화되지 않을 수 있습니다.

현재 user 기준:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

환경에 맞는 가장 좁은 정책을 사용하세요.

## 흔한 실수

첫 번째 실수는 Python은 설치했지만 VS Code Python extension을 설치하지 않은 것입니다.

두 번째 실수는 project folder가 아니라 단일 파일만 여는 것입니다.

세 번째 실수는 `.venv`를 workspace와 다른 directory에 만드는 것입니다.

네 번째 실수는 interpreter를 선택한 뒤 이전 terminal을 계속 사용하는 것입니다.

다섯 번째 실수는 global Python, Conda, virtual environment Python을 혼동하는 것입니다.
실제로 무엇이 실행되는지는 `sys.executable`로 확인해야 합니다.

## 함께 보면 좋은 글

- [Python venv가 활성화되지 않을 때](/ko_Troubleshooting/python-venv-not-activating/)
- [Windows에서 python 명령어가 안 될 때](/ko_Troubleshooting/python-command-not-found-windows/)
- [VS Code: Python environments](https://code.visualstudio.com/docs/python/environments)
- [VS Code Python tutorial](https://code.visualstudio.com/docs/python/python-tutorial)

## 최종 체크리스트

```text
[ ] Python extension이 설치되어 있고 enabled 상태다.
[ ] project folder를 열었다.
[ ] `.venv`가 workspace 안이나 가까운 위치에 있다.
[ ] interpreter path를 수동으로 선택할 수 있다.
[ ] 새 terminal이 선택한 Python을 사용한다.
[ ] `sys.executable`이 기대 environment를 가리킨다.
```

자동 탐지가 실패하면 manual interpreter selection이 가장 빠른 해결책입니다.
그 다음 status bar만 보지 말고 `sys.executable`로 실제 실행 경로를 확인하세요.
