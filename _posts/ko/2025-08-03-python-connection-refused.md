---
typora-root-url: ../
layout: single
title: >
    Python "ConnectionError: [Errno 111] Connection refused" 해결 방법
date: 2025-08-03T16:00:00+09:00
header:
    teaser: /images/header_images/overlay_image_python.png
    overlay_image: /images/header_images/overlay_image_python.png
    overlay_filter: 0.5
excerpt: >
    Python에서 "Connection refused" 오류는 네트워크 연결 시 대상 서버가 연결을 거부할 때 발생합니다. 이 글에서는 오류의 원인과 해결 방법을 알아봅니다.
categories:
    - ko_Troubleshooting
tags:
    - Python
    - ConnectionError
    - Network
    - Socket
---

## Python "ConnectionError: [Errno 111] Connection refused"란?

`ConnectionError: [Errno 111] Connection refused`는 Python의 `socket`이나 `requests` 같은 네트워킹 라이브러리를 사용하여 원격 서버에 연결을 시도할 때, 대상 서버가 연결 요청을 거부했음을 나타내는 오류입니다. 숫자 `111`은 Linux 시스템에서 "Connection refused"를 의미하는 에러 코드입니다. (Windows나 다른 OS에서는 다른 에러 코드가 표시될 수 있습니다.)

이 오류는 클라이언트 측 코드의 문제라기보다는, **서버가 클라이언트의 연결을 받아들일 준비가 되어 있지 않다**는 신호입니다.

## "Connection refused"의 일반적인 원인

1.  **서버가 실행 중이 아님**: 가장 흔한 원인입니다. 연결하려는 IP 주소와 포트에서 아무런 애플리케이션도 실행되고 있지 않을 수 있습니다.
2.  **잘못된 IP 주소 또는 포트**: 서버는 실행 중이지만, 클라이언트가 잘못된 IP 주소나 포트 번호로 연결을 시도하고 있을 수 있습니다.
3.  **방화벽**: 서버 또는 클라이언트, 혹은 그 사이의 네트워크 장비(라우터 등)에 있는 방화벽이 특정 포트로의 연결을 차단하고 있을 수 있습니다.
4.  **서버의 리스닝(Listening) 주소 설정 오류**: 서버 애플리케이션이 `localhost` 또는 `127.0.0.1`로만 바인딩되어 있을 수 있습니다. 이 경우, 서버가 실행 중인 컴퓨터 내부에서는 접속이 가능하지만 다른 컴퓨터에서는 접속할 수 없습니다. 외부에서의 접속을 허용하려면 `0.0.0.0`으로 바인딩해야 합니다.
5.  **서버의 연결 대기 큐(Backlog) 초과**: 서버가 동시에 처리할 수 있는 연결 요청의 한계를 초과하여 새로운 연결을 거부하는 경우입니다. 이는 서버 부하가 매우 높을 때 발생할 수 있습니다.

## "Connection refused" 해결 방법

### 1. 서버 상태 확인

가장 먼저 연결하려는 서버가 정상적으로 실행 중인지 확인해야 합니다.

-   서버에 직접 접근할 수 있다면, 해당 애플리케이션의 프로세스가 실행 중인지 확인합니다.
-   서버 로그를 확인하여 시작 시 오류가 발생하지 않았는지 점검합니다.

### 2. IP 주소 및 포트 확인

클라이언트 코드에 하드코딩된 IP 주소와 포트가 서버가 리스닝하고 있는 주소 및 포트와 일치하는지 다시 한번 확인하세요.

서버 측에서 `netstat` 명령어를 사용하면 어떤 포트에서 리스닝 중인지 확인할 수 있습니다.

```bash
# Linux/macOS
netstat -an | grep LISTEN

# Windows
netstat -an | findstr "LISTENING"
```

### 3. 방화벽 설정 확인

서버의 방화벽이 클라이언트의 연결을 허용하도록 설정되어 있는지 확인합니다. 예를 들어, Linux의 `ufw`나 `firewalld`, Windows의 방화벽 설정에서 해당 포트(예: 8080)가 인바운드 규칙에 허용되어 있는지 확인해야 합니다.

클라이언트 측에서도 아웃바운드 연결이 차단되지 않았는지 확인이 필요할 수 있습니다.

### 4. 서버 리스닝 주소 확인

서버 애플리케이션이 모든 네트워크 인터페이스로부터의 연결을 허용하는지 확인하세요. 일반적으로 웹 서버나 API 서버를 설정할 때 호스트 주소를 `127.0.0.1`이 아닌 `0.0.0.0`으로 설정해야 외부에서 접속할 수 있습니다.

**Flask 예제:**
```python
# 127.0.0.1 (localhost)에서만 접속 가능
# app.run(host='127.0.0.1', port=5000)

# 모든 IP 주소에서 접속 가능
app.run(host='0.0.0.0', port=5000)
```

### 5. 간단한 연결 테스트

`telnet`이나 `nc` (netcat) 같은 간단한 도구를 사용하여 클라이언트 컴퓨터에서 서버로의 기본적인 TCP 연결이 가능한지 테스트할 수 있습니다.

```bash
telnet <server_ip> <port>
# 예: telnet 192.168.1.100 8080
```
만약 여기서도 "Connection refused"가 발생한다면, Python 코드의 문제가 아니라 네트워크 또는 서버 설정의 문제임이 확실합니다.

## 결론

`ConnectionError: [Errno 111] Connection refused`는 네트워크 프로그래밍에서 흔히 마주치는 문제이며, 대부분의 경우 클라이언트 코드보다는 서버 측의 상태나 네트워크 구성에 원인이 있습니다. 문제를 해결하기 위해서는 서버가 정상적으로 실행 중인지, 올바른 주소와 포트로 리스닝하고 있는지, 그리고 방화벽이 연결을 막고 있지는 않은지 체계적으로 확인하는 접근 방식이 필요합니다.

