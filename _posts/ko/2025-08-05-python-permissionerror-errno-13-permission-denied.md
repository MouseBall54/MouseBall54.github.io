---
typora-root-url: ../
layout: single
title: >
   Python PermissionError: [Errno 13] Permission denied 오류 해결 방법
date: 2025-08-05T10:05:00+09:00
header:
   teaser: /images/header_images/overlay_image_python.png
   overlay_image: /images/header_images/overlay_image_python.png
   overlay_filter: 0.5
excerpt: >
   Python에서 파일 권한을 올바르게 관리하여 PermissionError: [Errno 13] Permission denied 오류를 해결하세요. 이 가이드는 원인을 설명하고 Windows, macOS, Linux용 해결책을 제공합니다.
categories:
   - ko_Troubleshooting
tags:
   - Python
   - PermissionError
   - File Permissions
   - OSError
   - Troubleshooting
---

## 서론

`PermissionError: [Errno 13] Permission denied`는 Python에서 스크립트가 필요한 권한 없이 파일이나 디렉터리에 접근하려고 할 때 발생하는 일반적인 오류입니다. 파일을 읽거나, 쓰거나, 실행할 때 발생할 수 있습니다. 근본 원인을 이해하는 것이 효율적인 해결의 핵심입니다.

이 가이드에서는 이 오류가 발생하는 이유를 설명하고 여러 운영 체제에서 문제를 해결하기 위한 명확하고 실행 가능한 단계를 제공합니다.

## `PermissionError: [Errno 13] Permission denied`의 원인은 무엇인가요?

이 오류는 거의 항상 Python 스크립트를 실행하는 사용자의 파일 시스템 권한과 관련이 있습니다. 가장 일반적인 시나리오는 다음과 같습니다.

1.  **보호된 파일 읽기**: 스크립트가 읽기 권한이 없는 파일을 읽으려고 합니다.
2.  **보호된 파일 또는 디렉터리에 쓰기**: 스크립트가 쓰기 권한이 없는 파일에 쓰거나 디렉터리에 새 파일을 만들려고 시도합니다.
3.  **실행 권한 없는 파일 실행**: 스크립트가 실행 파일을 실행하려고 하지만 실행 권한이 없습니다.
4.  **파일 대신 디렉터리 접근**: 때때로 실수로 디렉터리를 파일처럼 읽거나 쓰려고 시도하면 권한 오류가 발생할 수 있습니다.
5.  **파일이 사용 중인 경우**: Windows에서는 다른 프로세스가 파일을 잠근 경우 `PermissionError`가 발생할 수 있습니다.

## 오류 해결 방법

해결책은 스크립트가 무엇을 하려는지와 사용 중인 운영 체제에 따라 다릅니다.

### 1. 파일/디렉터리 권한 확인

먼저 문제가 되는 파일이나 디렉터리를 식별하고 권한을 확인합니다.

-   **Linux 또는 macOS**: 터미널에서 `ls -l` 명령을 사용하여 권한을 확인합니다.

```bash
ls -l /path/to/your/file.txt
# 출력 예시: -rw-r--r-- 1 owner group ... file.txt
```

출력은 소유자, 그룹, 기타 사용자에 대한 권한을 보여줍니다. `r`은 읽기, `w`는 쓰기, `x`는 실행을 의미합니다.

-   **Windows**: 파일이나 디렉터리를 마우스 오른쪽 버튼으로 클릭하고 **속성**으로 이동한 다음 **보안** 탭을 선택합니다. 여기서 여러 사용자 및 그룹에 대한 권한을 볼 수 있습니다.

### 2. 파일/디렉터리 권한 변경

권한이 잘못된 경우 변경해야 합니다. 이를 위해 관리자/루트 권한이 필요할 수 있습니다.

-   **Linux 또는 macOS**: `chmod` 명령을 사용하여 필요한 권한을 부여합니다.

```bash
# 소유자에게 읽기 및 쓰기 권한 부여
chmod u+rw /path/to/your/file.txt

# 실행 권한 부여
chmod +x /path/to/your/script.sh

# 디렉터리와 그 내용의 권한을 재귀적으로 변경
chmod -R u+rw /path/to/your/directory
```

-   **Windows**: 파일 속성의 **보안** 탭에서 **편집...**을 클릭하여 권한을 변경합니다. 스크립트를 실행하는 사용자를 선택하고 필요에 따라 "읽기", "쓰기" 또는 "모든 권한" 확인란을 선택합니다.

### 3. 충분한 권한으로 스크립트 실행

파일 권한을 변경할 수 없는 경우, 필요한 권한을 가진 사용자로 스크립트를 실행해야 할 수 있습니다.

-   **Linux 또는 macOS**: `sudo`를 사용하여 루트 권한으로 스크립트를 실행합니다. **스크립트가 충분히 테스트되지 않았다면 의도하지 않은 결과를 초래할 수 있으므로 주의해서 사용하세요.**

```bash
sudo python your_script.py
```

-   **Windows**: 명령 프롬프트나 IDE를 마우스 오른쪽 버튼으로 클릭하고 **"관리자 권한으로 실행"**을 선택합니다. 이렇게 하면 스크립트에 상승된 권한이 부여됩니다.

### 4. 경로가 올바른지 확인

`open()`과 같은 파일 작업을 수행할 때 스크립트가 디렉터리가 아닌 파일을 대상으로 하는지 확인하세요.

**잘못된 코드:**
```python
# '/path/to/data'가 디렉터리인 경우 오류 발생
with open('/path/to/data', 'w') as f:
    f.write('hello')
```

**올바른 접근 방식:**
```python
import os

file_path = '/path/to/data/file.txt'
dir_path = os.path.dirname(file_path)

# 디렉터리가 존재하는지 확인
if not os.path.exists(dir_path):
    os.makedirs(dir_path)

# 이제 파일을 쓰기 모드로 엽니다
with open(file_path, 'w') as f:
    f.write('hello')
```
`os.path.isdir()` 함수를 사용하여 경로가 디렉터리를 가리키는지 확인할 수 있습니다.

### 5. 파일을 사용하는 다른 프로그램 닫기 (Windows)

Windows에서는 다른 프로그램(예: 텍스트 편집기 또는 스프레드시트 소프트웨어)이 파일을 열고 있으면 파일이 잠겨 Python 스크립트가 접근하지 못할 수 있습니다. 파일을 사용하고 있을 수 있는 다른 모든 응용 프로그램을 닫고 스크립트를 다시 실행해 보세요.

## 결론

`PermissionError: [Errno 13] Permission denied`는 파일 시스템 권한을 관리하여 해결할 수 있는 간단한 문제입니다. 스크립트를 실행하는 사용자와 대상 파일 또는 디렉터리에 대한 권한을 확인하여 문제를 신속하게 진단할 수 있습니다. 항상 스크립트가 의도한 작업을 수행하는 데 필요한 권한을 가지고 있는지 확인하고, 상승된 권한으로 스크립트를 실행할 때는 주의하세요.
