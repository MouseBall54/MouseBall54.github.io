---
typora-root-url: ../
layout: single
title: >
    JavaScript "SyntaxError: Invalid or unexpected token" 오류 해결 방법

lang: ko
translation_id: javascript-syntaxerror-invalid-or-unexpected-token
header:
   teaser: /images/header_images/overlay_image_js.png
   overlay_image: /images/header_images/overlay_image_js.png
   overlay_filter: 0.5
excerpt: >
    이 포스트에서는 JavaScript 엔진이 언어의 구문 규칙을 위반하는 코드를 만났을 때 발생하는 "SyntaxError: Invalid or unexpected token" 오류의 해결 방법을 설명합니다.
categories:
  - ko_Troubleshooting
tags:
  - JavaScript
  - SyntaxError
  - Debugging
  - Frontend
---

## "SyntaxError: Invalid or unexpected token" 이란?

"SyntaxError: Invalid or unexpected token"은 JavaScript에서 흔히 발생하는 오류입니다. 이 오류는 JavaScript 엔진의 파서(parser)가 이해할 수 없거나 언어의 구문 규칙을 위반하는 코드를 만났을 때 발생합니다. 여기서 "토큰(token)"은 키워드, 연산자, 변수 이름과 같은 코드의 단일 단위를 의미합니다. 이 오류는 본질적으로 파서가 예상치 못한 곳에서 토큰을 발견하여 코드의 문법 구조가 깨졌음을 의미합니다.

## 주요 원인과 해결 방법

이 오류는 다양한 구문 실수로 인해 발생할 수 있습니다. 가장 흔한 원인과 해결 방법은 다음과 같습니다.

### 1. 괄호, 대괄호, 중괄호의 누락 또는 불일치

가장 흔한 원인 중 하나는 괄호 `()`, 대괄호 `[]`, 또는 중괄호 `{}`가 누락되거나 추가된 경우입니다.

**잘못된 코드:**
```javascript
function calculate(a, b { // 인자를 위한 닫는 괄호 누락
  return a + b;
}

console.log(calculate(5, 10); // 함수 호출을 위한 닫는 괄호 누락
```

**올바른 코드:**
```javascript
function calculate(a, b) { // 괄호 수정
  return a + b;
}

console.log(calculate(5, 10)); // 괄호 수정
```

**해결 방법:**
코드를 주의 깊게 확인하여 모든 여는 `(`, `[`, `{`에 해당하는 닫는 `)`, `]`, `}`가 있는지 확인하세요. 구문 강조 기능이 있는 코드 에디터는 이러한 불일치를 찾는 데 매우 유용합니다.

### 2. 오타 (Typos)

추가 문자나 잘못된 위치의 연산자와 같은 간단한 오타가 이 오류를 유발할 수 있습니다.

**잘못된 코드:**
```javascript
let x = 10;
let y = 20;
let z = x + y+; // 불필요한 '+' 연산자
```

**올바른 코드:**
```javascript
let x = 10;
let y = 20;
let z = x + y; // 불필요한 '+' 제거
```

**해결 방법:**
오류가 발생한 줄을 검토하여 오타나 잘못된 문자가 있는지 확인하세요. 브라우저의 개발자 콘솔은 보통 정확한 줄 번호를 알려줍니다.

### 3. 템플릿 리터럴의 잘못된 사용

템플릿 리터럴(백틱 `` ` ``)을 사용할 때 표현식을 포함하기 위한 `${}`를 잊어버릴 수 있습니다.

**잘못된 코드:**
```javascript
const name = "World";
const greeting = `Hello, "name"!`; // "name"이 문자열 리터럴로 처리됨
```

이 코드는 구문 오류를 발생시키지는 않지만 잘못된 결과를 출력합니다. 내용이 유효하지 않은 경우 구문 오류가 발생할 수 있습니다. 오류의 더 직접적인 원인은 닫히지 않은 리터럴입니다.

**잘못된 코드:**
```javascript
const message = `이것은 닫히지 않은 템플릿 리터럴입니다;
```

**올바른 코드:**
```javascript
const name = "World";
const greeting = `Hello, ${name}!`; // 변수를 올바르게 포함

const message = `이것은 닫힌 템플릿 리터럴입니다`; // 리터럴을 닫음
```

**해결 방법:**
모든 템플릿 리터럴이 백틱으로 제대로 닫혔는지 확인하고, 표현식을 포함할 때는 `${...}` 구문을 사용했는지 확인하세요.

### 4. 유효하지 않은 문자

때로는 JavaScript 코드에 유효하지 않은 문자를 실수로 복사하여 붙여넣을 수 있습니다. 예를 들어, 표준 큰따옴표(`" "`) 대신 스마트 따옴표(`“ ”`)를 사용하는 경우입니다.

**잘못된 코드:**
```javascript
const text = “Hello World”; // 스마트 따옴표 사용
```

**올바른 코드:**
```javascript
const text = "Hello World"; // 표준 큰따옴표 사용
```

**해결 방법:**
코드 에디터가 표준 따옴표를 사용하도록 설정되었는지 확인하고, 특히 웹 페이지나 문서에서 복사한 코드에 비표준 문자가 있는지 확인하세요.

### 5. 예약어를 변수 이름으로 사용

JavaScript 예약어(예: `class`, `const`, `function`)를 변수나 함수 이름으로 사용하면 구문 오류가 발생합니다.

**잘못된 코드:**
```javascript
let const = "이것은 허용되지 않습니다"; // 'const'는 예약어
```

**올바른 코드:**
```javascript
let myConst = "이것은 허용됩니다"; // 변수 이름 변경
```

**해결 방법:**
예약어를 식별자로 사용하지 마세요. 확실하지 않은 경우 온라인에서 JavaScript 예약어 목록을 찾아볼 수 있습니다.

## 결론

"SyntaxError: Invalid or unexpected token" 오류는 거의 항상 코드 구조의 간단한 실수로 인해 발생합니다. 오류 메시지가 가리키는 코드 줄을 주의 깊게 검사하고, 괄호 불일치, 오타 또는 유효하지 않은 문자와 같은 일반적인 문제를 확인하면 이 오류를 신속하게 해결할 수 있습니다. 린팅 및 구문 강조 기능이 있는 좋은 코드 에디터를 사용하면 코드를 실행하기 전에 이러한 오류를 발견하는 데 도움이 될 수 있습니다.
