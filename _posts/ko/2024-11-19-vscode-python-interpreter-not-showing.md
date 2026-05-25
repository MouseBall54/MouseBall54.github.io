---
typora-root-url: ../
layout: single
title: >
  VS Code Python Interpreter가 보이지 않을 때 해결 방법
seo_title: >
  VS Code Python Interpreter Not Showing 해결
date: 2024-11-19T07:14:00+09:00
last_modified_at: 2026-05-23T23:59:59+09:00
lang: ko
translation_id: vscode-python-interpreter-not-showing
header:
   teaser: /images/2026-05-23-vscode-python-interpreter-not-showing/vscode-python-interpreter-hero.png
   overlay_image: /images/2026-05-23-vscode-python-interpreter-not-showing/vscode-python-interpreter-hero.png
   overlay_filter: 0.35
   image_description: >
     VS Code Python Interpreter가 보이지 않을 때 해결 방법 주제를 한눈에 설명하는 시각 자료입니다.
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

## 전문 보완 체크

**VS Code Python Interpreter가 보이지 않을 때 해결 방법**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 인터프리터 경로, 가상환경, 패키지 버전, 입력 파일 또는 데이터 경계를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

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

- [Python venv가 활성화되지 않을 때](/ko_troubleshooting/python-venv-not-activating/)
- [Windows에서 python 명령어가 안 될 때](/ko_troubleshooting/python-command-not-found-windows/)
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

## 자주 묻는 질문

### 이 글은 언제 먼저 적용하면 좋나요?

오류 메시지, 실행한 명령, 사용 중인 OS와 버전을 먼저 기록한 뒤 이 글의 원인별 순서대로 확인하는 것이 좋습니다.

### 초보자가 가장 먼저 확인할 부분은 무엇인가요?

처음에는 환경 변수, 설치 경로, 권한, 캐시처럼 재현 가능성이 높은 항목부터 확인하세요. 그다음 로그와 설정 파일을 비교하면 원인을 좁히기 쉽습니다.

### 더 찾아볼 때 어떤 키워드를 쓰면 좋나요?

추가 검색할 때는 "VS Code Python Interpreter가 보이지 않을 때 해결 방법" 같은 핵심 문구와 error message, version, Windows, GitHub Pages, Jekyll 같은 실제 환경 키워드를 붙이면 더 정확한 결과를 얻기 쉽습니다.
