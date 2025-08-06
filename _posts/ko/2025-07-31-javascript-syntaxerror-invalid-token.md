---
typora-root-url: ../
layout: single
title: "JavaScript \"SyntaxError: Invalid or unexpected token\" 오류 해결 방법"

lang: ko
translation_id: javascript-syntaxerror-invalid-token
excerpt: "오타, 쉼표나 괄호와 같은 문자 누락, 잘못된 구문을 확인하여 JavaScript의 \"SyntaxError: Invalid or unexpected token\" 오류를 해결하세요."
header:
   teaser: /images/header_images/overlay_image_js.png
   overlay_image: /images/header_images/overlay_image_js.png
   overlay_filter: 0.5
categories:
  - ko_Troubleshooting
tags:
  - JavaScript
  - SyntaxError
  - Debugging
  - Token
---

## 서론

`SyntaxError: Invalid or unexpected token`은 JavaScript 엔진이 구문 분석할 수 없는 코드를 만났을 때 발생하는 일반적인 오류다. 이 오류는 매우 포괄적이며, 단순한 오타부터 더 복잡한 구조적 문제에 이르기까지 다양한 구문 실수로 인해 발생할 수 있다. 이 가이드에서는 가장 빈번한 원인과 이를 식별하고 수정하는 방법을 다룬다.

## 1. 원인: 오타 및 잘못된 문자

이 오류의 가장 흔한 원인은 단순한 오타다. 코드에 추가적인 문자, 잘못된 위치의 쉼표 또는 유효하지 않은 문자가 포함될 수 있다.

### 예시

```javascript
// 객체 리터럴에 추가 쉼표
const myObject = {
  name: "John",
  age: 30,, // 추가 쉼표
};

// 코드에 잘못된 문자
const x = 10; & // 유효하지 않은 문자 '&'

// 배열 요소 사이에 쉼표 누락
const myArray = [1 2, 3]; // 1과 2 사이에 쉼표 누락
```

### 해결책

- **코드 신중하게 검토**: 오류 메시지에 표시된 줄 번호를 자세히 살펴본다. 종종 오류는 해당 줄이나 바로 앞 줄에 있다.
- **린터 사용**: ESLint와 같은 도구는 입력하는 동안 이러한 종류의 구문 오류를 자동으로 감지하고 표시하여 디버깅 시간을 절약해 준다.

## 2. 원인: 괄호, 대괄호 또는 중괄호 누락

짝이 맞지 않는 괄호 `()`, 대괄호 `[]` 또는 중괄호 `{}`는 이 오류의 빈번한 원인이다. 하나를 열고 닫는 것을 잊으면 JavaScript 파서가 혼란에 빠진다.

### 예시

```javascript
function myFunction(a, b { // 닫는 괄호 ')' 누락
  return a + b;
}

const myArray = [1, 2, 3; // 닫는 대괄호 ']' 누락

if (condition) {
  // 닫는 중괄호 '}' 누락
```

### 해결책

- **짝이 맞는지 확인**: 모든 여는 `(`, `[`, `{`에 해당하는 닫는 `)`, `]`, `}`가 있는지 확인한다.
- **괄호 매칭 기능이 있는 코드 에디터 사용**: VS Code, Sublime Text, Atom과 같은 대부분의 최신 코드 에디터는 일치하는 괄호를 강조 표시하여 누락된 부분을 쉽게 찾을 수 있도록 도와준다.

## 3. 원인: 예약된 키워드의 잘못된 사용

JavaScript 예약어(`class`, `const`, `function`, `let` 등)를 변수나 함수 이름으로 사용하면 구문 오류가 발생한다.

### 예시

```javascript
const let = "This is not allowed"; // 'let'은 예약어다

function class() { // 'class'는 예약어다
  console.log("This is also not allowed");
}
```

### 해결책

- **예약어 사용 피하기**: JavaScript 예약어 목록에 익숙해지고 변수와 함수에 다른 이름을 선택한다. 전체 목록은 MDN Web Docs에서 찾을 수 있다.

## 4. 원인: 유효하지 않은 문자가 포함된 코드 복사-붙여넣기

웹 페이지, PDF 또는 워드 프로세서에서 코드를 복사할 때 표준 직선 따옴표(`"..."` 또는 `'...'`) 대신 "스마트 따옴표"(`“...”` 또는 `‘...’`)가 포함될 수 있다. JavaScript는 스마트 따옴표를 유효한 문자열 구분 기호로 인식하지 못한다.

### 예시

```javascript
// 직선 따옴표 대신 스마트 따옴표 사용
const greeting = “Hello, World!”; 
// SyntaxError: Invalid or unexpected token 오류 발생
```

### 해결책

- **스마트 따옴표 교체**: 모든 스마트 따옴표를 표준 작은따옴표나 큰따옴표로 수동으로 교체한다.
- **에디터 설정**: 일부 코드 에디터는 코드를 붙여넣을 때 스마트 따옴표를 직선 따옴표로 자동 변환하도록 설정할 수 있다.

이러한 일반적인 실수를 체계적으로 확인하면 `SyntaxError: Invalid or unexpected token`을 신속하게 진단하고 수정할 수 있다.
