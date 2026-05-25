---
typora-root-url: ../
layout: single
title: >
   JavaScript "jQuery is not defined" 오류 해결 방법

date: 2025-04-11T07:15:00+09:00
lang: ko
translation_id: javascript-jquery-is-not-defined
header:
   teaser: /images/header_images/overlay_image_js.png
   overlay_image: /images/header_images/overlay_image_js.png
   overlay_filter: 0.5
   image_description: >
     이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: JavaScript "jQuery is not defined" 오류 해결 방법
excerpt: >
   흔한 "Uncaught ReferenceError: jQuery is not defined" 오류는 스크립트가 jQuery를 사용하기 전에 라이브러리가 올바르게 로드되었는지 확인하여 해결할 수 있습니다. 이 가이드는 원인과 해결책을 다룹니다.
seo_description: >
   흔한 "Uncaught ReferenceError: jQuery is not defined" 오류는 스크립트가 jQuery를 사용하기 전에 라이브러리가 올바르게 로드되었는지 확인하여 해결할 수 있습니다. 이 가이드는 원인과 해결책을 다룹니다.
categories:
   - ko_Troubleshooting
tags:
   - JavaScript
   - jQuery
   - ReferenceError
   - Web Development
   - Troubleshooting
---


![이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: JavaScript "jQuery is not defined" 오류 해결 방법](/images/header_images/overlay_image_js.png)
## 서론

"Uncaught ReferenceError: jQuery is not defined" 또는 "$ is not defined"는 거의 모든 웹 개발자가 jQuery를 사용할 때 마주치는 고전적인 오류입니다. 이는 코드가 브라우저에서 jQuery 라이브러리가 로드되고 초기화되기 전에 사용하려고 시도했음을 의미합니다.

이 가이드에서는 이 오류의 일반적인 원인을 살펴보고, jQuery에 의존하는 스크립트가 원활하게 실행되도록 간단하고 효과적인 해결책을 제공합니다.

## "jQuery is not defined"의 원인은 무엇인가요?

이 오류는 HTML 문서의 스크립트 로딩 순서와 관련된 몇 가지 주된 이유로 발생합니다.

1.  **잘못된 스크립트 순서**: jQuery를 사용하는 사용자 정의 스크립트 (`<script src="my_script.js"></script>`)가 jQuery 라이브러리를 로드하는 스크립트 (`<script src=".../jquery.min.js"></script>`) *앞에* 배치된 경우입니다. 브라우저는 HTML에 나타나는 순서대로 스크립트를 실행하므로, 코드가 존재하기 전에 jQuery를 사용하려고 시도합니다.
2.  **jQuery 로드 실패**: jQuery 라이브러리 링크가 깨졌거나, 잘못된 위치를 가리키거나, CDN(콘텐츠 전송 네트워크)이 일시적으로 다운된 경우입니다. 브라우저가 라이브러리를 다운로드하지 못해 정의되지 않습니다.
3.  **비동기 로딩 문제**: 스크립트 태그에 `async` 또는 `defer` 속성을 사용하면 실행 순서가 변경되어 코드가 jQuery가 준비되기 전에 실행될 수 있습니다.
4.  **jQuery 슬림 빌드**: `ajax` 및 `effects` 모듈이 제외된 jQuery의 "슬림" 버전을 사용하고 있을 수 있습니다. 코드가 이러한 모듈의 함수(예: `$.ajax()`)를 사용하려고 하면 관련 오류가 발생할 수 있지만, 주된 "not defined" 오류는 핵심 라이브러리 자체에 관한 것입니다.

## 오류 해결 방법

가장 일반적인 수정 사항부터 시작하여 해결책을 살펴보겠습니다.

### 1. 스크립트 로딩 순서 확인

이것이 가장 빈번한 원인입니다. jQuery 라이브러리를 의존하는 다른 스크립트 **전에** 포함했는지 확인하세요. HTML 파일의 올바른 순서는 다음과 같아야 합니다.

```html
<!DOCTYPE html>
<html>
<head>
    <title>My Page</title>
</head>
<body>
    <!-- HTML 콘텐츠 -->

    <!-- 1. jQuery 먼저 로드 -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>

    <!-- 2. 그런 다음 jQuery를 사용하는 사용자 정의 스크립트 로드 -->
    <script src="js/my_script.js"></script>
</body>
</html>
```

스크립트를 `<body>` 태그 끝에 배치하는 것은 일반적인 모범 사례입니다. 이렇게 하면 브라우저가 JavaScript를 파싱하고 실행하기 위해 멈추기 전에 페이지 콘텐츠를 렌더링할 수 있습니다.

### 2. jQuery 소스 경로 확인

jQuery `<script>` 태그의 `src` 속성을 다시 확인하세요.

-   **URL이 올바른가요?** 로컬 파일 경로 또는 CDN 링크에 오타가 있는지 확인하세요.
-   **파일이 존재하나요?** 브라우저에서 URL을 직접 열어보세요. jQuery 소스 코드가 보여야 합니다. 404 Not Found 오류가 발생하면 경로가 잘못된 것입니다.

**로컬 파일 사용 예:**
```html
<!-- 이 경로가 HTML 파일을 기준으로 올바른지 확인하세요 -->
<script src="libs/jquery/jquery-3.6.0.min.js"></script>
```

**CDN 사용 예:**
```html
<!-- 신뢰할 수 있는 CDN이 종종 최선의 선택입니다 -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
```

### 3. 코드를 Document Ready 블록으로 감싸기

스크립트 태그가 올바른 순서에 있더라도, jQuery 코드를 실행하기 전에 DOM(문서 객체 모델)이 완전히 로드될 때까지 기다리는 것이 가장 좋습니다. 이렇게 하면 스크립트가 아직 존재하지 않는 HTML 요소를 조작하려고 시도하는 문제를 방지할 수 있습니다.

jQuery는 이를 위해 `$(document).ready()` 함수를 제공합니다.

```javascript
// my_script.js 파일에서

$(document).ready(function() {
    // 모든 jQuery 코드는 여기에 작성합니다
    $('#my-button').click(function() {
        alert('버튼이 클릭되었습니다!');
    });
});

// 더 짧고 동일한 구문도 일반적입니다:
$(function() {
    // 모든 jQuery 코드는 여기에 작성합니다
    $('h1').css('color', 'blue');
});
```

이렇게 하면 함수 내부의 코드는 jQuery가 로드되고 페이지 구조가 준비된 후에만 실행됩니다.

### 4. 네트워크 문제 또는 광고 차단기 확인

-   **네트워크 연결**: 특히 CDN을 사용하는 경우 인터넷에 연결되어 있는지 확인하세요.
-   **광고 차단기**: 일부 공격적인 광고 차단기나 브라우저 확장 프로그램이 특정 CDN으로의 요청을 차단할 수 있습니다. 이를 비활성화하여 문제가 해결되는지 확인해 보세요.

## 결론

"jQuery is not defined" 오류는 거의 항상 로딩 문제입니다. `<script>` 태그가 올바른 순서에 있는지 확인하고, jQuery 파일 경로를 확인하고, 코드를 `$(document).ready()` 블록으로 감싸면 이 오류를 제거하고 신뢰할 수 있는 jQuery 기반 애플리케이션을 구축할 수 있습니다. 항상 의존성을 먼저 로드하는 것은 웹 개발의 기본 규칙입니다.

## 전문 보완 체크

**JavaScript "jQuery is not defined" 오류 해결 방법**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 실행 환경, 정확한 오류 경계, 최소 재현 예제, 되돌릴 수 있는 경로를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

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
