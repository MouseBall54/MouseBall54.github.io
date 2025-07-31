---
typora-root-url: ../
layout: single
title: "JavaScript 오류 'Uncaught SyntaxError: Unexpected token' 해결 방법"
date: 2025-07-30T14:10:00+09:00
excerpt: "'Uncaught SyntaxError: Unexpected token'은 JavaScript 엔진이 문법적으로 예상치 못한 토큰을 만났을 때 발생하는 구문 오류입니다. 이 오류의 일반적인 원인과 해결책을 알아봅니다."
header:
   teaser: /images/header_images/overlay_image_js.png
   overlay_image: /images/header_images/overlay_image_js.png
   overlay_filter: 0.5
categories:
  - ko_Troubleshooting
tags:
  - JavaScript
  - SyntaxError
  - Troubleshooting
  - Debugging
---

## 'Uncaught SyntaxError: Unexpected token' 오류란?

`Uncaught SyntaxError: Unexpected token`은 JavaScript 코드가 언어의 문법 규칙을 따르지 않을 때 발생하는 가장 일반적인 구문 오류 중 하나다.
JavaScript 엔진이 코드를 파싱(해석)하는 과정에서 문법적으로 올바르지 않은, 예상치 못한 문자나 키워드(토큰)를 만나면 이 오류를 발생시킨다.
오류 메시지는 보통 `Unexpected token 'X'`와 같은 형태로 나타나며, 여기서 `'X'`는 문제가 된 특정 문자나 토큰을 가리킨다.

## 주요 원인

이 오류는 다양한 문법적 실수로 인해 발생할 수 있다.

### 1. 괄호, 중괄호, 대괄호의 불일치

열린 괄호가 제대로 닫히지 않았거나, 짝이 맞지 않는 경우에 발생한다.

```javascript
// 닫는 소괄호 '}'가 아닌 ')'여야 함
if (condition) {
    console.log("Hello, World!";
}
// Uncaught SyntaxError: Unexpected token '}'
```

### 2. 잘못된 연산자 사용

객체 리터럴에서 `=`를 사용하거나, 쉼표가 누락되는 등 잘못된 연산자 사용이 원인이 될 수 있다.

```javascript
let myObject = {
    key1: "value1",
    key2 = "value2" // '='가 아닌 ':'를 사용해야 함
};
// Uncaught SyntaxError: Unexpected token '='
```

### 3. 예약어의 잘못된 사용

`let`, `const`, `class` 같은 예약어를 변수 이름으로 사용하려고 할 때 발생한다.

```javascript
let let = 5; // 'let'은 예약어이므로 변수명으로 사용할 수 없음
// Uncaught SyntaxError: Unexpected token 'let'
```

### 4. JSON 데이터 파싱 오류

`JSON.parse()`를 사용할 때, 전달된 문자열이 유효한 JSON 형식이 아닐 경우 이 오류가 발생할 수 있다.
예를 들어, JSON 문자열 내의 키를 큰따옴표로 감싸지 않았거나, 마지막 속성 뒤에 쉼표가 붙어 있는 경우가 해당된다.

```javascript
// 마지막 속성 뒤에 쉼표(trailing comma)가 있어 오류 발생
let jsonString = '{"name": "John", "age": 30,}';
JSON.parse(jsonString);
// Uncaught SyntaxError: Unexpected token '}' in JSON at position ...
```

## 해결 방법

### 1. 코드 편집기 및 Linter 활용

대부분의 최신 코드 편집기(VS Code, WebStorm 등)는 실시간으로 구문 오류를 감지하고 강조 표시해준다.
또한 ESLint와 같은 Linter 도구를 사용하면 코드를 실행하기 전에 잠재적인 구문 오류를 미리 찾아낼 수 있어 매우 유용하다.

### 2. 괄호 및 따옴표 짝 맞추기

오류가 발생한 줄 주변의 모든 괄호(`()`, `{}`, `[]`)와 따옴표(`'`, `"`, `` ` ``)가 올바르게 짝을 이루고 닫혔는지 확인한다.
코드 편집기의 괄호 짝 맞춤 기능을 활용하면 쉽게 찾을 수 있다.

### 3. 문법 규칙 재확인

오류 메시지에 나타난 `Unexpected token`이 무엇인지 확인하고, 해당 부분의 JavaScript 문법이 올바른지 다시 한번 확인한다.
예를 들어, 객체 속성은 콜론(`:`)으로 정의하고, 배열 요소와 객체 속성은 쉼표(`,`)로 구분하는 등의 기본 규칙을 점검한다.

### 4. JSON 유효성 검사

`JSON.parse()` 관련 오류라면, 파싱하려는 문자열이 유효한 JSON 형식인지 검사해야 한다.
온라인 JSON 검증 도구(JSONLint 등)를 사용하거나, JSON의 규칙(키는 항상 큰따옴표, 마지막 요소 뒤 쉼표 없음 등)을 다시 확인한다.

## 결론

`Uncaught SyntaxError: Unexpected token`은 코드에 문법적 실수가 있음을 알려주는 명확한 신호다.
오류 메시지가 가리키는 위치와 예상치 못한 토큰이 무엇인지 주의 깊게 살펴보는 것이 문제 해결의 첫걸음이다.
코드 편집기의 구문 강조 기능과 Linter를 적극적으로 활용하면 이러한 종류의 오류를 사전에 예방하고 빠르게 수정하는 데 큰 도움이 된다.
