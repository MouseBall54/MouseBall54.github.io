typora-root-url: ../
layout: single
title: >
    JavaScript SyntaxError: Unterminated string literal 해결 방법
seo_title: >
    JavaScript SyntaxError: Unterminated string literal 해결 방법

lang: ko
translation_id: javascript-syntaxerror-unterminated-string-literal
header:
   teaser: /images/header_images/overlay_image_js.png
   overlay_image: /images/header_images/overlay_image_js.png
   overlay_filter: 0.5
excerpt: >
    JavaScript에서 "SyntaxError: Unterminated string literal"은 문자열이 제대로 닫히지 않았을 때 발생하는 구문 오류입니다. 이 오류는 주로 따옴표나 줄 바꿈 문제로 인해 발생합니다. 이 글에서는 오류의 원인과 해결 방법을 알아봅니다.
seo_description: >
    JavaScript에서 "SyntaxError: Unterminated string literal"은 문자열이 제대로 닫히지 않았을 때 발생하는 구문 오류입니다. 이 오류는 주로 따옴표나 줄 바꿈 문제로 인해 발생합니다. 이 글에서는 오류의 원인과 해결 방법을 알아봅니다.
categories:
  - ko_Troubleshooting
tags:
  - JavaScript
  - SyntaxError
  - String
  - Error
---

## 문제 상황

JavaScript 코드를 작성할 때 `SyntaxError: Unterminated string literal` (또는 일부 브라우저에서는 `Uncaught SyntaxError: Invalid or unexpected token`) 오류가 발생할 수 있습니다.
이 오류는 문자열 리터럴이 올바르게 종료되지 않았음을 의미합니다.
주로 문자열을 여는 따옴표는 있지만 닫는 따옴표가 없거나, 문자열 내에서 잘못된 문자가 사용될 때 발생합니다.

```javascript
// 잘못된 예시 1: 닫는 따옴표 누락
let message = 'Hello, world;

// 잘못된 예시 2: 문자열 내부에 줄 바꿈 포함
let htmlString = '<div>
    <p>Hello</p>
</div>';

console.log(message);
console.log(htmlString);
```

위 코드들은 모두 `SyntaxError`를 발생시킵니다.
첫 번째는 닫는 작은따옴표(`'`)가 없습니다.
두 번째는 일반 문자열 안에 직접 줄 바꿈을 포함하고 있습니다.

## 원인 분석

이 오류의 주요 원인은 다음과 같습니다.

1.  **따옴표 불일치 또는 누락**: 문자열을 시작하는 따옴표(작은따옴표 `'` 또는 큰따옴표 `