---
typora-root-url: ../
layout: single
title: >
   Python PermissionError: [Errno 13] Permission denied 오류 해결 방법

date: 2025-04-20T07:24:00+09:00
lang: ko
translation_id: python-permissionerror-errno-13-permission-denied
header:
   teaser: /images/header_images/overlay_image_python.png
   overlay_image: /images/header_images/overlay_image_python.png
   overlay_filter: 0.5
   image_description: >
     이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Python PermissionError: [Errno 13] Permission denied 오류 해결 방법
excerpt: >
   Python에서 파일 권한을 올바르게 관리하여 PermissionError: [Errno 13] Permission denied 오류를 해결하세요. 이 가이드는 원인을 설명하고 Windows, macOS, Linux용 해결책을 제공합니다.
seo_description: >
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


![이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Python PermissionError: Errno 13 Permission denied 오류 해결 방법](/images/header_images/overlay_image_python.png)
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

## 전문 보완 체크

**Python PermissionError: [Errno 13] Permission denied 오류 해결 방법**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 실행 환경, 정확한 오류 경계, 최소 재현 예제, 되돌릴 수 있는 경로를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

### 신뢰도를 높이는 증거

작업을 바꾸기 전에는 객관적인 증거를 먼저 확인해야 합니다. 쓸 만한 증거에는 전체 명령 출력, 버전 번호, 변경된 파일, 기대 동작과 실제 동작가 포함됩니다. 증거가 서로 맞지 않으면 억지로 하나의 이야기로 합치지 말고 충돌 자체를 남겨야 합니다. 빠른 해결이 한 번 성공했더라도 같은 입력, 계정, 의존성, 기기 상태에서 다시 확인하지 않았다면 아직 확정된 해결책이라고 보기 어렵습니다.

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
