---
typora-root-url: ../
layout: single
title: >
    Python "OSError: [Errno 28] No space left on device" 해결 방법
date: 2025-08-03T14:10:00+09:00
header:
    teaser: /images/header_images/overlay_image_python.png
    overlay_image: /images/header_images/overlay_image_python.png
    overlay_filter: 0.5
excerpt: >
    Python에서 "OSError: [Errno 28] No space left on device"는 디스크 공간이 부족할 때 발생합니다. 이 글에서는 오류의 원인과 해결 방법을 알아봅니다.
categories:
    - ko_Troubleshooting
tags:
    - Python
    - OSError
    - Disk Space
---

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

