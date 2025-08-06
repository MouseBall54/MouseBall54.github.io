---
typora-root-url: ../
layout: single
title: >
   Python TimeoutError: [WinError 10060] 연결 시도 실패 오류 해결 방법

lang: ko
translation_id: python-timeouterror-winerror-10060
header:
   teaser: /images/header_images/overlay_image_python.png
   overlay_image: /images/header_images/overlay_image_python.png
   overlay_filter: 0.5
excerpt: >
   네트워크 연결 시간 초과 시 발생하는 Python TimeoutError: [WinError 10060] 오류를 해결하는 방법을 알아보세요. 이 가이드는 방화벽, 잘못된 주소, 서버 문제 등 원인을 다루고 명확한 해결책을 제공합니다.
categories:
   - ko_Troubleshooting
tags:
   - Python
   - TimeoutError
   - WinError 10060
   - Networking
   - Troubleshooting
---

## 서론

Python으로 네트워크 프로그래밍을 할 때 `TimeoutError: [WinError 10060]` 오류를 마주칠 수 있습니다. 이 오류는 연결된 상대방이 일정 시간 동안 제대로 응답하지 않았거나, 연결된 호스트가 응답하지 않아 설정된 연결이 실패했음을 의미합니다. 웹 클라이언트, API, 데이터베이스 커넥터와 같이 네트워크 소켓에 의존하는 애플리케이션에서 흔히 발생하는 문제입니다.

이 가이드에서는 이 오류의 일반적인 원인을 살펴보고 단계별 해결 방법을 안내합니다.

## `TimeoutError: [WinError 10060]`의 원인은 무엇인가요?

이 오류는 일반적으로 다음 중 한 가지 이유로 발생합니다.

1.  **잘못된 IP 주소 또는 포트**: 연결하려는 서버가 지정된 IP 주소에 존재하지 않거나 지정된 포트에서 수신 대기하고 있지 않습니다.
2.  **방화벽 제한**: 로컬 컴퓨터, 네트워크 또는 원격 서버의 방화벽이 연결을 차단하고 있습니다.
3.  **서버 미실행 또는 과부하**: 서버 애플리케이션이 실행 중이 아니거나, 충돌했거나, 너무 바빠서 새 연결을 수락할 수 없습니다.
4.  **네트워크 문제**: 패킷 손실이나 높은 지연 시간과 같은 일반적인 네트워크 문제로 인해 시기적절한 응답을 받지 못할 수 있습니다.
5.  **짧은 타임아웃 값**: Python 스크립트에 설정된 타임아웃이 너무 짧아 서버가 응답하기에 부족합니다. 특히 오래 실행되는 작업의 경우 그렇습니다.

## 오류 해결 방법

위에서 언급한 각 원인에 대한 해결책을 살펴보겠습니다.

### 1. IP 주소 및 포트 확인

가장 먼저 할 일은 연결하려는 IP 주소와 포트가 올바른지 확인하는 것입니다.

-   **오타 확인**: 코드에 있는 IP 주소와 포트 번호를 다시 확인하세요.
-   **서버 정보 확인**: 서버 관리자에게 올바른 연결 정보를 가지고 있는지 확인하세요.
-   **네트워크 도구 사용**: `ping`이나 `telnet`과 같은 도구를 사용하여 연결을 테스트할 수 있습니다.

```bash
# 서버에 ping을 보내 도달 가능한지 확인
ping example.com

# 특정 포트로 telnet하여 열려 있는지 확인
telnet example.com 8080
```

`ping`이 실패하거나 `telnet`으로 연결할 수 없다면, 주소나 네트워크 접근성 문제일 가능성이 높습니다.

### 2. 방화벽 설정 확인

방화벽은 흔한 원인입니다. 클라이언트 컴퓨터와 원격 서버 양쪽의 방화벽 설정을 확인하세요.

-   **로컬 방화벽**: 로컬 방화벽(예: Windows Defender 방화벽)을 일시적으로 비활성화하여 연결이 성공하는지 확인합니다. 성공한다면, Python 스크립트가 연결을 만들 수 있도록 아웃바운드 규칙을 생성하세요.
-   **네트워크 방화벽**: 회사나 제한된 네트워크에 있다면, 네트워크 관리자에게 연락하여 연결이 차단되고 있지 않은지 확인하세요.
-   **서버 방화벽**: 서버의 방화벽이 필요한 포트의 들어오는 연결을 차단하고 있을 수 있습니다. 해당 포트가 인바운드 트래픽에 대해 열려 있는지 확인하세요.

### 3. 서버 실행 및 응답 확인

연결하려는 서버 애플리케이션이 실행 중이고 새 연결을 처리할 수 있는지 확인하세요.

-   **서버 상태 확인**: 서버에 로그인하여 서비스나 애플리케이션이 활성 상태인지 확인하세요.
-   **서버 로그 검토**: 서버 로그는 응답하지 않는 이유(예: 오류 또는 리소스 제한)에 대한 귀중한 정보를 제공할 수 있습니다.
-   **다른 클라이언트로 테스트**: 다른 클라이언트나 도구에서 연결을 시도하여 클라이언트 측 문제가 아님을 확인하세요.

### 4. 타임아웃 값 늘리기

서버는 실행 중이지만 요청을 처리하는 데 시간이 오래 걸리는 경우, 클라이언트의 기본 타임아웃이 너무 짧을 수 있습니다. Python 코드에서 타임아웃 값을 늘릴 수 있습니다.

예를 들어, 인기 있는 `requests` 라이브러리를 사용할 때:

```python
import requests

try:
    # 더 긴 타임아웃 설정 (예: 30초)
    response = requests.get('http://example.com', timeout=30)
    print("연결 성공!")
except requests.exceptions.Timeout:
    print("요청 시간 초과.")
except requests.exceptions.RequestException as e:
    print(f"오류 발생: {e}")
```

로우 소켓(raw socket)으로 작업하는 경우 `socket.settimeout()`을 사용할 수 있습니다.

```python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(30)  # 30초 타임아웃 설정

try:
    s.connect(('example.com', 8080))
    print("연결 성공!")
except socket.timeout:
    print("연결 시간 초과.")
except socket.error as e:
    print(f"오류 발생: {e}")
finally:
    s.close()
```

### 5. 재시도 로직 구현

네트워크 연결은 불안정할 수 있습니다. 지수적 백오프(exponential backoff) 전략을 사용한 재시도 메커니즘을 구현하면 일시적인 네트워크 문제에 대해 애플리케이션을 더 탄력적으로 만들 수 있습니다.

다음은 간단한 재시도 로직을 구현하는 예제입니다.

```python
import requests
import time

def connect_with_retry(url, retries=3, delay=5):
    for i in range(retries):
        try:
            response = requests.get(url, timeout=10)
            return response
        except requests.exceptions.Timeout:
            print(f"{i+1}번째 시도에서 타임아웃 발생. {delay}초 후 재시도...")
            time.sleep(delay)
    raise ConnectionError(f"{retries}번의 시도 후 {url}에 연결 실패.")

try:
    response = connect_with_retry('http://example.com')
    print("연결 성공!")
except ConnectionError as e:
    print(e)
```

## 결론

`TimeoutError: [WinError 10060]`는 Windows 환경의 Python에서 흔히 발생하는 네트워크 관련 오류입니다. 서버 주소, 방화벽 규칙, 서버 상태, 연결 타임아웃을 체계적으로 점검함으로써 문제를 효과적으로 진단하고 해결할 수 있습니다. 타임아웃을 늘리고 재시도 로직을 추가하는 등 강력한 오류 처리 방법을 구현하면 네트워크 애플리케이션의 안정성을 더욱 높일 수 있습니다.
