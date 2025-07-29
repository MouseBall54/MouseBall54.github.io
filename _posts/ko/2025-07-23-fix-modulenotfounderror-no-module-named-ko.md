---
typora-root-url: ../
layout: single
title: " ModuleNotFoundError: No module named ‘…’ 오류 해결 방법"
date: 2025-07-23T22:00:00+09:00
excerpt: "Python에서 모듈을 찾지 못해 발생하는 `ModuleNotFoundError`의 주요 원인과 해결책을 정리. 패키지 설치, 가상환경 활성화, 경로 설정, 이름 충돌 방지 방법 안내."
categories:
  - ko_Troubleshooting
tags:
  - Python
  - ModuleNotFoundError
  - ErrorHandling
---

## 소개

파이썬 스크립트 실행 시 import 실패 에러.
많은 개발자가 겪는 대표 오류.
이 글에서 단계별 해결 방법을 다룸.

## 오류 내용

```
ModuleNotFoundError: No module named 'requests'
```

import 대상 모듈이 `sys.path`에 없음을 의미.

## 주요 원인

* 패키지 미설치.
* 가상환경이 활성화되지 않음.
* Python 인터프리터와 pip 불일치.
* 스크립트나 폴더 이름이 모듈명과 충돌.
* PYTHONPATH 또는 site-packages 경로 누락.

## 해결 방법 1: 모듈 설치

```bash
python -m pip install <module_name>
```

* `python -m pip` 사용해 인터프리터 일치 보장.
* 특정 버전 필요 시 `==` 옵션 추가.

## 해결 방법 2: 가상환경 활성화

1. 가상환경 생성:

   ```bash
   python -m venv env
   ```
2. 활성화:

   * PowerShell:

     ```powershell
     .\env\Scripts\Activate.ps1
     ```
   * Git Bash:

     ```bash
     source env/Scripts/activate
     ```
3. 가상환경 내에서 필요한 패키지 재설치.

## 해결 방법 3: Python 버전과 pip 확인

```bash
where python
where pip
```

* 실행에 쓰는 Python과 pip가 같은 경로인지 확인.
* 불일치 시 `python -m pip install` 사용.

## 해결 방법 4: 이름 충돌 방지

* 프로젝트 폴더나 스크립트 이름을 모듈명(`requests.py` 등)과 겹치지 않게 설정.
* 충돌 파일이 있을 경우 이름 변경.

## 해결 방법 5: 경로 확인

```python
import sys
print(sys.path)
```

* 모듈이 설치된 경로가 포함됐는지 확인.
* 개발 중인 패키지는

  ```bash
  pip install -e .
  ```

  로 editable 설치.

## 결론

`ModuleNotFoundError`는 대부분 설치 또는 경로 문제.
올바른 인터프리터 사용, 가상환경 활성화, 이름 충돌 방지로 쉽게 해결 가능.
