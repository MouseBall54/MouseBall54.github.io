---
typora-root-url: ../
layout: single
title: "Cross-Origin Read Blocking (CORB) 오류 해결 방법"
date: 2025-07-31T22:00:00+09:00
header:
   teaser: /images/header_images/overlay_image_js.png
   overlay_image: /images/header_images/overlay_image_js.png
   overlay_filter: 0.5
excerpt: >
  서버가 올바른 Content-Type 및 CORS 헤더를 전송하도록 하여 브라우저의 Cross-Origin Read Blocking (CORB) 경고를 해결하는 방법을 알아봅니다.
categories:
  - ko_Troubleshooting
tags:
  - JavaScript
  - CORB
  - CORS
  - Web Security
  - Fetch
---

브라우저 개발자 콘솔에서 "Cross-Origin Read Blocking (CORB) blocked cross-origin response..."와 같은 경고 메시지를 본 적이 있을 것입니다. 이는 코드를 중단시키는 일반적인 오류가 아니라, 브라우저가 보안을 위해 응답을 차단했음을 알리는 보안 경고입니다.

이 포스트에서는 CORB가 무엇인지, 왜 발생하는지, 그리고 어떻게 해결하는지 설명합니다.

### Cross-Origin Read Blocking (CORB)이란?

CORB는 특정 교차 출처(cross-origin) 네트워크 응답이 웹 페이지에 전달되는 것을 방지하는 웹 보안 기능입니다. 주요 목표는 Spectre와 같은 사이드 채널 공격을 완화하는 것입니다. 이러한 공격은 다른 애플리케이션의 메모리에서 민감한 데이터가 유출될 수 있습니다.

CORB는 응답의 `Content-Type`을 검사하여 작동합니다. 만약 응답이 스크립트나 스타일시트에 포함되어서는 안 되는 리소스(예: HTML, XML, JSON)인데 스크립트 컨텍스트(예: `<script>`, `<img>`)에서 요청된 경우, CORB는 응답을 차단할 수 있습니다.

### CORB 경고의 일반적인 원인

가장 흔한 원인은 서버가 보낸 `Content-Type` 헤더와 브라우저가 예상하는 콘텐츠 유형이 일치하지 않는 경우입니다.

1.  **잘못된 `Content-Type` 헤더**: 서버가 일반적이거나 잘못된 `Content-Type`으로 리소스를 보내고 있습니다. 예를 들어, `application/json`을 반환해야 하는 API 엔드포인트가 대신 `text/html`을 보내는 경우입니다.
2.  **`X-Content-Type-Options: nosniff` 헤더**: 이 보안 헤더는 브라우저에게 MIME 유형을 추측하지 말라고 지시합니다. 만약 `Content-Type`이 잘못되었고 `nosniff`가 활성화되어 있다면, 브라우저는 잘못된 헤더를 신뢰하고 CORB를 트리거할 수 있습니다.

### CORB 문제 해결 방법

해결책은 거의 항상 서버 측 설정을 수정하는 것입니다.

#### 1단계: 응답 헤더 확인하기

먼저, 브라우저의 개발자 도구를 사용하여 경고를 유발한 네트워크 요청을 검사합니다.

1.  개발자 도구를 엽니다 (F12 또는 Ctrl+Shift+I).
2.  "Network" 탭으로 이동합니다.
3.  문제가 되는 요청을 찾습니다.
4.  "Response Headers" 섹션에서 `Content-Type`의 값을 확인합니다.

API 호출이 `application/json` 대신 `text/html`이나 `text/plain`을 반환하고 있는 것을 발견할 가능성이 높습니다.

#### 2단계: 서버에서 `Content-Type` 수정하기

주요 해결책은 서버가 올바른 `Content-Type` 헤더를 보내도록 하는 것입니다.

예를 들어, Node.js Express 서버가 있다면 API 엔드포인트에서 헤더를 명시적으로 설정해야 합니다.

```javascript
// 수정 전 (잘못된 경우)
app.get('/api/data', (req, res) => {
  // 서버가 기본적으로 text/html로 응답할 수 있음
  res.send({ message: 'This is JSON data' });
});

// 수정 후 (올바른 경우)
app.get('/api/data', (req, res) => {
  res.setHeader('Content-Type', 'application/json');
  res.json({ message: 'This is JSON data' });
});
```
Express에서 `res.json()`을 사용하면 `Content-Type`이 자동으로 `application/json`으로 설정됩니다.

#### 3단계: 올바른 CORS 설정 확인하기

CORB는 CORS(Cross-Origin Resource Sharing)와는 다르지만 관련이 있습니다. 잘못 구성된 CORS 정책은 문제를 일으킬 수 있습니다. 서버가 응답에 `Access-Control-Allow-Origin` 헤더를 포함하는지 확인하세요.

```javascript
// Node.js/Express 예시
app.use((req, res, next) => {
  res.setHeader('Access-Control-Allow-Origin', 'https://your-frontend-domain.com');
  // ... 다른 CORS 헤더들
  next();
});
```

#### 4단계: 프록시 서버 사용하기 (서버를 변경할 수 없는 경우)

타사 API를 사용하고 있어 서버 측 헤더를 변경할 수 없는 경우, 유일한 해결 방법은 프록시 서버를 설정하는 것입니다.

프론트엔드 애플리케이션이 프록시에 요청을 보내면, 프록시가 타사 API에서 데이터를 요청합니다. 그런 다음 프록시는 올바른 `Content-Type` 및 CORS 헤더와 함께 응답을 애플리케이션에 다시 전달할 수 있습니다.

### 결론

CORB 경고는 브라우저가 잠재적인 보안 취약점으로부터 사용자를 보호하고 있다는 신호입니다. 이는 거의 항상 서버가 요청된 리소스에 대해 잘못된 `Content-Type` 헤더를 보내기 때문에 발생합니다. 가장 좋은 해결책은 전송되는 콘텐츠를 정확하게 설명하도록 서버의 응답 헤더를 수정하는 것입니다.
