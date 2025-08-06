---
typora-root-url: ../
layout: single
title: >
    JavaScript "WebSocket connection to '...' failed" 해결 방법

lang: ko
translation_id: javascript-websocket-connection-failed
header:
    teaser: /images/header_images/overlay_image_js.png
    overlay_image: /images/header_images/overlay_image_js.png
    overlay_filter: 0.5
excerpt: >
    JavaScript에서 WebSocket 연결 실패는 다양한 원인으로 발생할 수 있습니다. 이 글에서는 "WebSocket connection to '...' failed" 오류의 일반적인 원인과 해결 방법을 알아봅니다.
categories:
    - ko_Troubleshooting
tags:
    - JavaScript
    - WebSocket
    - Network
---

## JavaScript "WebSocket connection to '...' failed"란?

이 오류는 브라우저의 JavaScript 코드가 WebSocket 서버에 연결을 시도했지만 실패했을 때 발생하는 메시지입니다. WebSocket은 클라이언트와 서버 간의 실시간 양방향 통신을 가능하게 하는 프로토콜이며, 연결 실패는 네트워크, 서버 설정, 클라이언트 코드 등 다양한 원인에 의해 발생할 수 있습니다.

## "WebSocket connection failed"의 일반적인 원인

1.  **잘못된 WebSocket URL**: URL 스킴이 `ws://` 또는 `wss://` (보안 연결)가 아니거나, 주소 또는 포트가 잘못된 경우입니다.
2.  **서버가 실행 중이 아님**: 연결하려는 WebSocket 서버가 다운되었거나 실행 중이 아닐 수 있습니다.
3.  **방화벽 또는 프록시 문제**: 로컬 또는 네트워크 방화벽, 프록시 서버가 WebSocket 연결(특정 포트)을 차단하고 있을 수 있습니다.
4.  **CORS (Cross-Origin Resource Sharing) 문제**: 웹 페이지의 출처(origin)와 WebSocket 서버의 출처가 다른 경우, 서버가 해당 출처의 연결을 허용하도록 설정되지 않으면 연결이 거부될 수 있습니다.
5.  **서버 측 오류**: WebSocket 서버 애플리케이션 자체에 버그가 있거나, 핸드셰이크 과정에서 오류가 발생할 수 있습니다.
6.  **혼합 콘텐츠 (Mixed Content) 오류**: HTTPS를 통해 로드된 페이지에서 안전하지 않은 `ws://` 프로토콜로 연결을 시도하면 브라우저가 보안상의 이유로 연결을 차단합니다. HTTPS 페이지에서는 반드시 `wss://`를 사용해야 합니다.

## "WebSocket connection failed" 해결 방법

### 1. WebSocket URL 확인

가장 먼저 클라이언트 코드의 WebSocket URL이 올바른지 확인하세요.

```javascript
// URL 스킴, 호스트, 포트가 정확한지 확인
// 예: const socket = new WebSocket('ws://localhost:8080');
// 보안 연결 예: const socket = new WebSocket('wss://example.com/socket');

const socket = new WebSocket('ws://your-server-address:port');
```

### 2. 서버 상태 확인

WebSocket 서버가 정상적으로 실행 중인지 확인하세요. 서버 로그를 점검하여 오류가 없는지 확인하고, `ping`이나 `netstat` 같은 도구를 사용하여 서버에 접근할 수 있는지 테스트할 수 있습니다.

```bash
# 서버가 해당 포트에서 수신 대기 중인지 확인 (Linux/macOS)
netstat -an | grep LISTEN | grep 8080
```

### 3. 방화벽 및 프록시 설정 확인

사용 중인 포트(예: 8080)가 방화벽에서 허용되어 있는지 확인하세요. 회사나 공용 네트워크를 사용하는 경우, 프록시 서버가 WebSocket 트래픽을 차단할 수 있으므로 네트워크 관리자에게 문의해야 할 수 있습니다.

### 4. 서버 측 CORS 및 출처 확인 설정

웹 페이지와 WebSocket 서버의 출처가 다른 경우, 서버 측에서 특정 출처 또는 모든 출처의 연결을 허용하도록 설정해야 합니다. 이는 서버 프레임워크(예: Node.js의 `ws` 라이브러리, Spring Boot)에 따라 구현 방법이 다릅니다.

**Node.js `ws` 라이브러리 예제:**
```javascript
const WebSocket = require('ws');

const wss = new WebSocket.Server({ 
    server, // http 서버 인스턴스
    verifyClient: (info, done) => {
        // 특정 출처만 허용
        const allowedOrigins = ['http://localhost:3000', 'https://your-frontend.com'];
        if (allowedOrigins.includes(info.origin)) {
            done(true);
        } else {
            done(false, 403, 'Forbidden');
        }
    }
});
```

### 5. `wss://` 사용 확인

웹사이트가 HTTPS를 통해 제공된다면, WebSocket 연결도 반드시 보안 연결인 `wss://`를 사용해야 합니다. 최신 브라우저는 보안 페이지에서 비보안 연결을 차단합니다.

```javascript
// HTTPS 페이지에서는 항상 wss:// 사용
if (window.location.protocol === 'https:/') {
    const socket = new WebSocket('wss://your-secure-server.com/socket');
} else {
    const socket = new WebSocket('ws://your-server-address:port');
}
```

### 6. 브라우저 개발자 도구 활용

브라우저의 개발자 도구(F12)를 열고 **콘솔(Console)** 탭에서 자세한 오류 메시지를 확인하세요. **네트워크(Network)** 탭의 `WS` 필터를 사용하면 WebSocket 핸드셰이크 요청과 응답을 확인할 수 있어 문제 해결에 큰 도움이 됩니다.

## 결론

WebSocket 연결 실패는 다양한 요인이 복합적으로 작용하여 발생할 수 있습니다. 문제 해결을 위해서는 클라이언트 URL부터 시작하여 서버 상태, 네트워크 설정, 서버 측 로직까지 단계적으로 확인하는 체계적인 접근이 필요합니다. 브라우저 개발자 도구는 문제의 원인을 파악하는 데 가장 강력한 도구 중 하나이므로 적극적으로 활용하세요.

