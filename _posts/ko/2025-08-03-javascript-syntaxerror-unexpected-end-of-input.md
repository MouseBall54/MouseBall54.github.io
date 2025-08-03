---
typora-root-url: ../
layout: single
title: >
    자바스크립트 SyntaxError: Unexpected end of input 해결 방법
date: 2025-08-03T10:30:00+09:00
header:
   teaser: /images/header_images/overlay_image_js.png
   overlay_image: /images/header_images/overlay_image_js.png
   overlay_filter: 0.5
excerpt: >
    자바스크립트 코드를 파싱하는 동안 엔진이 코드 블록의 끝을 예상치 못하게 만났을 때 발생하는 `SyntaxError: Unexpected end of input` 오류의 일반적인 원인과 해결책을 알아봅니다.
categories:
  - ko_Troubleshooting
tags:
  - JavaScript
  - SyntaxError
  - JSON
  - Debugging
---

## 문제 상황

`SyntaxError: Unexpected end of input`는 자바스크립트 엔진이 코드를 해석(parsing)하던 중, 코드 블록이나 구문이 끝나기를 예상하지 않은 시점에서 파일의 끝(end of file)이나 입력의 끝(end of input)에 도달했을 때 발생하는 구문 오류입니다.

이 오류의 가장 흔한 원인은 **괄호, 중괄호, 대괄호의 짝이 맞지 않는 것**입니다. 예를 들어, 함수나 `if` 문의 여는 중괄호(`{`)는 있지만 닫는 중괄호(`}`)가 없는 경우입니다.

## 오류 발생 코드 예시

### 1. 함수나 제어문의 중괄호 누락

함수, `if` 문, `for` 루프 등의 코드 블록에서 닫는 중괄호(`}`)를 빠뜨린 경우입니다.

```javascript
function calculate(a, b) {
  const result = a + b;
  return result;
// 닫는 중괄호 '}'가 없습니다.
// SyntaxError: Unexpected end of input
```

### 2. 객체 리터럴의 중괄호 누락

객체를 정의할 때 닫는 중괄호(`}`)가 없는 경우에도 동일한 오류가 발생합니다.

```javascript
const person = {
  name: 'Alice',
  age: 30
// 닫는 중괄호 '}'가 없습니다.
// SyntaxError: Unexpected end of input
```

### 3. 불완전한 JSON 데이터 파싱

`JSON.parse()`를 사용할 때 전달된 문자열이 완전한 JSON 형식이 아닐 경우에도 이 오류가 발생할 수 있습니다. 예를 들어, 네트워크 통신이 중간에 끊겨 데이터가 잘린 경우입니다.

```javascript
// 중괄호가 닫히지 않은 불완전한 JSON 문자열
const jsonString = '{"name": "Bob", "city": "New York"'; 

try {
  const data = JSON.parse(jsonString);
} catch (e) {
  console.error(e); // SyntaxError: Unexpected end of JSON input
}
```

`JSON.parse`의 경우 조금 더 구체적인 오류 메시지(`Unexpected end of JSON input`)를 보여줍니다.

## 해결 방법

이 오류는 대부분 간단한 실수로 인해 발생하므로, 해결 방법도 명확합니다.

### 1. 괄호, 중괄호, 대괄호의 짝 맞추기

오류가 발생한 코드 주변을 살펴보고, 모든 여는 기호(`(`, `{`, `[`)에 해당하는 닫는 기호가 있는지 꼼꼼히 확인하세요.

```javascript
// 수정된 코드
function calculate(a, b) {
  const result = a + b;
  return result;
} // 닫는 중괄호 추가

const person = {
  name: 'Alice',
  age: 30
}; // 닫는 중괄호 추가
```

### 2. 코드 편집기 기능 활용하기

최신 코드 편집기(예: VS Code, WebStorm)는 다음과 같은 기능을 제공하여 이런 실수를 방지하는 데 도움을 줍니다.

-   **괄호 짝 하이라이팅**: 커서를 특정 괄호에 놓으면 그 짝이 되는 괄호를 시각적으로 표시해줍니다.
-   **코드 포매팅(Code Formatting)**: `Prettier`와 같은 코드 포매터를 사용하면 코드를 저장할 때 자동으로 들여쓰기와 구조를 정리해주므로, 괄호가 빠진 부분을 쉽게 찾을 수 있습니다.
-   **린팅(Linting)**: `ESLint`와 같은 린팅 도구는 코드를 분석하여 구문 오류를 실시간으로 알려줍니다.

## 결론

`SyntaxError: Unexpected end of input` 오류는 대부분 코드 블록을 제대로 닫지 않아서 발생합니다. 오류가 발생하면 당황하지 말고 다음을 확인하세요.

-   함수, 제어문, 객체 리터럴 등에서 **여는 기호와 닫는 기호의 짝**이 모두 맞는지 검토합니다.
-   코드 편집기의 **괄호 매칭 기능**이나 **린터**를 적극적으로 활용하여 실수를 예방합니다.

차분히 코드를 살펴보면 보통 빠뜨린 중괄호 하나를 찾는 것으로 문제가 해결될 것입니다.
