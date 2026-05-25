---
typora-root-url: ../
layout: single
title: >
    Python "OSError: [Errno 28] No space left on device" 해결 방법

date: 2025-03-20T07:38:00+09:00
lang: ko
translation_id: python-os-error-no-space-left
header:
    teaser: /images/header_images/overlay_image_python.png
    overlay_image: /images/header_images/overlay_image_python.png
    overlay_filter: 0.5
    image_description: >
      이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Python "OSError: [Errno 28] No space left on device" 해결 방법
excerpt: >
    Python에서 "OSError: [Errno 28] No space left on device"는 디스크 공간이 부족할 때 발생합니다. 이 글에서는 오류의 원인과 해결 방법을 알아봅니다.
seo_description: >
    Python에서 "OSError: [Errno 28] No space left on device"는 디스크 공간이 부족할 때 발생합니다. 이 글에서는 오류의 원인과 해결 방법을 알아봅니다.
categories:
    - ko_Troubleshooting
tags:
    - Python
    - OSError
    - Disk Space
---


![이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Python "OSError: Errno 28 No space left on device" 해결 방법](/images/header_images/overlay_image_python.png)
## Python "OSError: [Errno 28] No space left on device"란?

`OSError: [Errno 28] No space left on device`는 Python 프로그램이 파일을 쓰려고 할 때 디스크의 저장 공간이 부족하여 더 이상 데이터를 기록할 수 없을 때 발생하는 운영 체제 수준의 오류입니다. 이 오류는 단순히 파일 쓰기 작업뿐만 아니라, 임시 파일을 생성하는 라이브러리나 프로세스에서도 발생할 수 있습니다.

## "No space left on device"의 일반적인 원인

1.  **디스크 공간 부족**: 가장 명백한 원인으로, 하드 드라이브나 파티션의 공간이 가득 찼을 때 발생합니다.
2.  **Inode 부족**: (Linux/macOS) 디스크 공간은 남아있지만, 파일 시스템이 할당할 수 있는 Inode(파일과 디렉터리에 대한 메타데이터)의 개수 한도에 도달했을 때 발생할 수 있습니다. 이는 특히 작은 파일이 매우 많을 때 문제가 됩니다.
3.  **임시 파일 과다 생성**: 프로그램이 정상적으로 종료되지 않거나 오류 처리 미흡으로 인해 임시 파일이 삭제되지 않고 계속 쌓이는 경우 발생할 수 있습니다.
4.  **대용량 로그 파일**: 로깅 설정이 잘못되어 매우 큰 로그 파일이 생성되면서 디스크 공간을 모두 차지하는 경우입니다.

## "No space left on device" 해결 방법

### 1. 디스크 공간 확인 및 확보

가장 먼저 시스템의 디스크 사용량을 확인해야 합니다.

*   **Linux/macOS**:
    ```bash
    df -h
    ```
    이 명령은 각 파티션의 사용량, 가용 공간, 사용률을 보여줍니다. 공간이 부족한 파티션을 찾았다면, 불필요한 파일을 삭제하여 공간을 확보해야 합니다. `du` 명령을 사용하면 특정 디렉터리의 크기를 확인할 수 있습니다.
    ```bash
    du -sh /path/to/directory
    ```

*   **Windows**: 파일 탐색기에서 각 드라이브의 속성을 확인하여 디스크 공간을 점검하고, 디스크 정리 유틸리티를 사용하여 불필요한 파일을 제거합니다.

### 2. Inode 사용량 확인 (Linux/macOS)

디스크 공간은 충분한데 오류가 발생한다면 Inode 부족을 의심해볼 수 있습니다.

```bash
df -i
```
`IUse%`가 100%에 가깝다면 Inode가 고갈된 것입니다. 이 경우, 수많은 작은 파일(예: 세션 파일, 캐시 파일)을 찾아 삭제해야 합니다.

### 3. 임시 파일 및 캐시 정리

프로그램이 생성하는 임시 파일이나 캐시가 제대로 관리되고 있는지 확인하세요. `tempfile` 모듈을 사용할 때 `with` 문을 활용하면 블록이 종료될 때 파일이 자동으로 정리됩니다.

```python
import tempfile

with tempfile.NamedTemporaryFile(mode='w+', delete=True) as temp_file:
    # delete=True (기본값)로 설정하면 파일이 닫힐 때 자동으로 삭제됩니다.
    temp_file.write('Hello, world!')
    temp_file.seek(0)
    # 파일 처리 로직
```

### 4. 로그 파일 관리

`logging` 모듈을 사용할 때 로그 파일이 무한정 커지지 않도록 `RotatingFileHandler`나 `TimedRotatingFileHandler`를 사용하여 로그 파일을 일정 크기나 시간 간격으로 분할하고 오래된 로그를 자동으로 삭제하도록 설정하세요.

```python
import logging
from logging.handlers import RotatingFileHandler

log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

# 10MB 크기의 로그 파일을 최대 5개까지 유지
handler = RotatingFileHandler('app.log', maxBytes=10*1024*1024, backupCount=5)
handler.setFormatter(log_formatter)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(handler)

logger.info('This is a test log message.')
```

## 결론

`OSError: [Errno 28] No space left on device`는 코드 자체의 문제라기보다는 시스템 환경의 문제입니다. 디스크 공간이나 Inode 사용량을 주기적으로 확인하고, 프로그램이 불필요한 파일을 남기지 않도록 관리하는 것이 중요합니다. 특히 로그 파일과 임시 파일 관리는 장시간 실행되는 애플리케이션에서 필수적입니다.

## 전문 보완 체크

**Python "OSError: [Errno 28] No space left on device" 해결 방법**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 실행 환경, 정확한 오류 경계, 최소 재현 예제, 되돌릴 수 있는 경로를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

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

독자가 **Python "OSError: [Errno 28] No space left on device" 해결 방법**의 첫 번째 권장 조치를 이미 시도했지만 결과가 여전히 불확실하다고 가정해 봅니다. 다음 단계는 여러 해결책을 한꺼번에 시험하는 것이 아니라 짧은 감사 기록을 만드는 것입니다. 먼저 어떤 판단을 하려는지 한 문장으로 쓰고, 환경을 한 문장으로 적고, 관찰된 결과를 한 문장으로 남깁니다. 그다음 실행 환경, 정확한 오류 경계, 최소 재현 예제, 되돌릴 수 있는 경로를 이미 확보한 사실과 대조합니다. 이렇게 해야 글이 서로 끊어진 팁 목록이 아니라 검증 가능한 절차가 됩니다.

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
