---
typora-root-url: ../
layout: single
title: >
   Python NotADirectoryError: [Errno 20] Not a directory 오류 해결 방법

date: 2025-04-19T07:23:00+09:00
lang: ko
translation_id: python-notadirectoryerror-errno-20-not-a-directory
header:
   teaser: /images/header_images/overlay_image_python.png
   overlay_image: /images/header_images/overlay_image_python.png
   overlay_filter: 0.5
   image_description: >
     이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Python NotADirectoryError: [Errno 20] Not a directory 오류 해결 방법
excerpt: >
   Python에서 디렉터리 경로가 필요한 곳에 파일 경로를 사용하여 발생하는 NotADirectoryError: [Errno 20] Not a directory 오류를 이해하고 해결하세요. 경로를 검증하여 이 흔한 문제를 피하는 방법을 배웁니다.
seo_description: >
   Python에서 디렉터리 경로가 필요한 곳에 파일 경로를 사용하여 발생하는 NotADirectoryError: [Errno 20] Not a directory 오류를 이해하고 해결하세요. 경로를 검증하여 이 흔한 문제를 피하는 방법을 배웁니다.
categories:
   - ko_Troubleshooting
tags:
   - Python
   - NotADirectoryError
   - File System
   - OSError
   - Troubleshooting
---


![이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Python NotADirectoryError: Errno 20 Not a directory 오류 해결 방법](/images/header_images/overlay_image_python.png)
## 서론

`NotADirectoryError: [Errno 20] Not a directory`는 `OSError`의 하위 클래스로, 디렉터리 경로가 필요한 컨텍스트에서 파일 경로를 사용하려고 할 때 발생합니다. 이것은 `IsADirectoryError`와 논리적으로 반대되는 오류입니다. 예를 들어, 파일의 내용을 디렉터리인 것처럼 나열하려고 하면 이 오류가 발생합니다.

이 가이드에서는 `NotADirectoryError`의 일반적인 원인을 설명하고 파일 및 디렉터리 경로를 올바르게 처리하여 해결하는 방법을 보여줍니다.

## `NotADirectoryError`의 원인은 무엇인가요?

이 오류는 디렉터리 경로가 필요한 함수가 대신 파일 경로를 받을 때 발생합니다. 이를 유발할 수 있는 가장 일반적인 함수는 다음과 같습니다.

1.  **`os.listdir(path)`**: 이 함수는 주어진 `path` 내부의 파일과 디렉터리를 나열합니다. 만약 `path`가 파일을 가리키면 `NotADirectoryError`를 발생시킵니다.
2.  **`os.path.join(path, ...)`**: 마지막 부분을 제외한 `path`의 구성 요소 중 하나가 파일인 경우 이 오류가 발생할 수 있습니다.
3.  **`os.makedirs(path)`**: 부모 경로 구성 요소 중 하나가 파일인 곳에 디렉터리를 만들려고 할 때 발생합니다.

간단한 예제는 다음과 같습니다.

```python
import os

# 'my_file.txt'가 디렉터리가 아닌 일반 파일이라고 가정
file_path = 'my_file.txt'

try:
    # listdir()는 디렉터리를 예상하므로 NotADirectoryError가 발생합니다
    contents = os.listdir(file_path) 
except NotADirectoryError as e:
    print(f"오류: {e}")

# 출력: 오류: [Errno 20] Not a directory: 'my_file.txt'
```

## 오류 해결 방법

이 오류를 해결하려면 디렉터리 수준 함수에 전달되는 모든 경로가 실제로 디렉터리인지 확인해야 합니다.

### 1. 사용 전 경로 유효성 검사

`os.listdir()`와 같은 함수를 호출하기 전에 경로가 디렉터리인지 확인해야 합니다. `os.path.isdir()` 함수가 이 작업에 완벽합니다.

```python
import os

path_to_check = 'my_file.txt' # 이것은 파일입니다

if os.path.isdir(path_to_check):
    print(f

## 전문 보완 체크

**Python NotADirectoryError: [Errno 20] Not a directory 오류 해결 방법**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 실행 환경, 정확한 오류 경계, 최소 재현 예제, 되돌릴 수 있는 경로를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

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

## 적용 검토 시나리오

독자가 **Python NotADirectoryError: [Errno 20] Not a directory 오류 해결 방법**의 첫 번째 권장 조치를 이미 시도했지만 결과가 여전히 불확실하다고 가정해 봅니다. 다음 단계는 여러 해결책을 한꺼번에 시험하는 것이 아니라 짧은 감사 기록을 만드는 것입니다. 먼저 어떤 판단을 하려는지 한 문장으로 쓰고, 환경을 한 문장으로 적고, 관찰된 결과를 한 문장으로 남깁니다. 그다음 실행 환경, 정확한 오류 경계, 최소 재현 예제, 되돌릴 수 있는 경로를 이미 확보한 사실과 대조합니다. 이렇게 해야 글이 서로 끊어진 팁 목록이 아니라 검증 가능한 절차가 됩니다.

### 감사 기록 양식

| 항목 | 예시 기준 | 이유 |
| --- | --- | --- |
| 관찰 | 조치 전 실제로 본 내용 | 기준 상태를 객관화합니다 |
| 증거 | 전체 명령 출력, 버전 번호 | 판단을 기록에 연결합니다 |
| 가정 | 믿고 있지만 아직 증명하지 못한 내용 | 숨은 추정을 드러냅니다 |
| 조치 | 한 번에 하나의 변경 | 결과의 원인을 추적하게 합니다 |
| 중단 기준 | 멈추고 도움을 요청할 조건 | 반복적인 시행착오를 줄입니다 |

### 품질 경계

같은 결과가 통제된 재확인 뒤에도 반복될 때만 이 안내를 강한 결론으로 보아야 합니다. 계정, 기기, 데이터 샘플, 의존성 버전, 계약 조건, 공식 규칙이 달라졌다면 결론의 강도를 낮추고 가설로 다루는 편이 안전합니다. 검색 독자는 급한 문제를 안고 들어오는 경우가 많아 맥락을 건너뛰기 쉽습니다. 전문적인 글은 위험한 판단을 천천히 하게 만들면서도 다음 행동은 분명하게 제시해야 합니다.

## 함께 보면 좋은 글

같은 주제 흐름에서 이어서 읽기 좋은 글입니다.

- [SSL: CERTIFICATE_VERIFY_FAILED 오류 해결 방법 (Windows Python)](/ko_troubleshooting/python-certificate-verify-failed/)
- [Permission denied (publickey) 오류 해결 방법 (Windows Git SSH)](/ko_troubleshooting/git-permission-denied-publickey-windows/)
