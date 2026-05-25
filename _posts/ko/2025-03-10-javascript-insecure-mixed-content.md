---
typora-root-url: ../
layout: single
title: >
    JavaScript "Insecure mixed content" 오류 해결 방법

date: 2025-03-10T07:28:00+09:00
lang: ko
translation_id: javascript-insecure-mixed-content
header:
    teaser: /images/header_images/overlay_image_js.png
    overlay_image: /images/header_images/overlay_image_js.png
    overlay_filter: 0.5
    image_description: >
      이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: JavaScript "Insecure mixed content" 오류 해결 방법
excerpt: >
    "Insecure mixed content"는 HTTPS 페이지에서 안전하지 않은 HTTP 리소스를 로드할 때 발생하는 브라우저 보안 경고입니다. 이 글에서는 원인과 해결 방법을 알아봅니다.
seo_description: >
    "Insecure mixed content"는 HTTPS 페이지에서 안전하지 않은 HTTP 리소스를 로드할 때 발생하는 브라우저 보안 경고입니다. 이 글에서는 원인과 해결 방법을 알아봅니다.
categories:
    - ko_Troubleshooting
tags:
    - JavaScript
    - HTTPS
    - Security
    - Mixed Content
---


![이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: JavaScript "Insecure mixed content" 오류 해결 방법](/images/header_images/overlay_image_js.png)
## "Insecure mixed content"란 무엇인가?

"혼합 콘텐츠(Mixed Content)" 오류는 초기 HTML이 HTTPS를 통해 안전하게 로드되었지만, 페이지의 다른 리소스(예: 이미지, 비디오, 스크립트, 스타일시트)가 안전하지 않은 HTTP 프로토콜을 통해 로드될 때 발생합니다. 이는 전체 페이지의 보안을 약화시키기 때문에 최신 브라우저는 이를 차단하거나 경고를 표시합니다.

HTTPS는 사용자와 웹사이트 간의 통신을 암호화하여 중간자 공격(man-in-the-middle attack)으로부터 보호합니다. 하지만 페이지의 일부라도 HTTP를 통해 전송되면, 공격자가 이 비암호화된 콘텐츠를 가로채거나 변조하여 전체 페이지를 제어할 수 있는 위험이 생깁니다.

## 혼합 콘텐츠의 두 가지 유형

1.  **수동적 혼합 콘텐츠 (Passive Mixed Content)**: 페이지의 표시를 변경할 수는 있지만 다른 부분과 상호작용하지 않는 콘텐츠입니다. (예: `<img>`, `<audio>`, `<video>`)
    -   **브라우저 동작**: 대부분의 브라우저는 여전히 이 콘텐츠를 로드하지만, 주소창의 자물쇠 아이콘을 변경하거나 개발자 도구에 경고를 표시하여 사용자에게 알립니다.

2.  **능동적 혼합 콘텐츠 (Active Mixed Content)**: 페이지의 DOM 전체에 접근하여 동작을 변경할 수 있는 콘텐츠입니다. (예: `<script>`, `<link>`(스타일시트), `<iframe>`, `fetch` 요청, `XMLHttpRequest`)
    -   **브라우저 동작**: 보안 위험이 매우 크기 때문에 **대부분의 브라우저는 이 콘텐츠를 기본적으로 차단**합니다. 이로 인해 웹사이트의 기능이 제대로 동작하지 않을 수 있습니다.

## "Insecure mixed content" 해결 방법

### 1. 모든 HTTP 링크를 HTTPS로 변경

가장 근본적이고 확실한 해결책은 웹사이트의 모든 `http://` 리소스 요청을 `https://`로 바꾸는 것입니다.

**수정 전:**
```html
<script src="http://example.com/script.js"></script>
<img src="http://example.com/image.jpg">
```

**수정 후:**
```html
<script src="https://example.com/script.js"></script>
<img src="https://example.com/image.jpg">
```

만약 해당 리소스가 HTTPS를 지원하지 않는다면, 다른 호스팅 서비스를 찾거나 직접 다운로드하여 자신의 서버에서 HTTPS로 제공해야 합니다.

### 2. 프로토콜 상대 경로 사용

URL에서 프로토콜(http: 또는 https:) 부분을 생략하면, 브라우저는 현재 페이지의 프로토콜을 따라 리소스를 요청합니다. 이는 HTTP와 HTTPS 환경 모두에서 유연하게 작동합니다.

```html
<!-- 현재 페이지가 HTTPS이면 https://로, HTTP이면 http://로 요청 -->
<script src="//example.com/script.js"></script>
<img src="//example.com/image.jpg">
```
**주의**: 이 방법은 대상 서버가 HTTP와 HTTPS를 모두 지원할 때만 유효합니다. 2024년 현재는 모든 리소스를 명시적으로 `https://`로 지정하는 것이 더 권장됩니다.

### 3. `Content-Security-Policy` (CSP) 헤더 사용

서버의 응답 헤더에 `Content-Security-Policy` (CSP)를 설정하여 혼합 콘텐츠를 자동으로 처리할 수 있습니다. `upgrade-insecure-requests` 지시어는 브라우저가 모든 HTTP 요청을 HTTPS로 자동 업그레이드하도록 지시합니다.

**HTTP 응답 헤더 예시:**
```
Content-Security-Policy: upgrade-insecure-requests
```

또는 HTML의 `<meta>` 태그를 사용할 수도 있습니다.
```html
<meta http-equiv="Content-Security-Policy" content="upgrade-insecure-requests">
```
이 방법은 많은 수의 HTTP 링크를 한 번에 처리해야 할 때 매우 유용합니다.

### 4. 혼합 콘텐츠 스캐너 사용

웹사이트가 복잡하여 수동으로 모든 링크를 찾기 어렵다면, Why No Padlock?이나 Mixed Content Scan 같은 온라인 도구를 사용하여 사이트의 혼합 콘텐츠 문제를 진단할 수 있습니다.

## 결론

"Insecure mixed content" 오류는 사용자 보안을 위한 브라우저의 중요한 기능입니다. 이 문제를 해결하려면 웹사이트에서 로드하는 모든 리소스(자체 서버 및 외부 서드파티 리소스 포함)가 `https://`를 통해 안전하게 제공되는지 확인해야 합니다. 가장 좋은 방법은 모든 URL을 `https://`로 명시적으로 지정하고, `Content-Security-Policy` 헤더를 사용하여 보안을 강화하는 것입니다.

## 전문 보완 체크

**JavaScript "Insecure mixed content" 오류 해결 방법**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 실행 환경, 정확한 오류 경계, 최소 재현 예제, 되돌릴 수 있는 경로를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

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
