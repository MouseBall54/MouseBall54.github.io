---
typora-root-url: ../
layout: single
title: "JavaScript \"ReferenceError: assignment to undeclared variable\" 오류 해결 방법"
date: 2025-07-31T22:11:00+09:00
excerpt: "값을 할당하기 전에 `let`, `const` 또는 `var`로 변수를 올바르게 선언하여 JavaScript의 strict mode에서 발생하는 \"ReferenceError: assignment to undeclared variable\" 오류를 해결하세요."
header:
   teaser: /images/header_images/overlay_image_js.png
   overlay_image: /images/header_images/overlay_image_js.png
   overlay_filter: 0.5
categories:
  - ko_Troubleshooting
tags:
  - JavaScript
  - ReferenceError
  - Debugging
  - Strict Mode
---

## 서론

`ReferenceError: assignment to undeclared variable "..."`는 JavaScript의 **strict mode(엄격 모드)**에서만 발생하는 오류다. 이 오류는 아직 선언되지 않은 변수에 값을 할당하여 실수로 전역 변수를 생성하는 것을 방지하는 안전장치 역할을 한다. 이 가이드에서는 이 오류가 발생하는 이유와 해결 방법을 설명한다.

## Strict Mode란?

Strict mode는 JavaScript의 제한된 변형을 선택하는 방법이다. 일반적인 JavaScript 의미 체계에 몇 가지 변경 사항을 적용한다.
1.  일부 JavaScript의 조용한 오류를 제거하고 대신 오류를 발생시킨다.
2.  JavaScript 엔진이 최적화를 수행하기 어렵게 만드는 실수를 수정한다.
3.  ECMAScript의 향후 버전에 정의될 가능성이 있는 일부 구문을 금지한다.

파일 시작 부분에 `"use strict";`를 추가하여 전체 스크립트에 대해 strict mode를 활성화하거나, 함수 본문 시작 부분에 추가하여 특정 함수에 대해 활성화할 수 있다.

```javascript
// 전체 스크립트에 대해
"use strict";
// ... 당신의 코드 ...

// 특정 함수에 대해
function myStrictFunction() {
  "use strict";
  // ... 당신의 코드 ...
}
```

## 오류의 원인

Strict mode가 아닌 경우, `var`, `let` 또는 `const`로 선언되지 않은 변수에 값을 할당하면 JavaScript는 자동으로 새로운 전역 변수를 생성한다.

**비-Strict Mode 예시:**
```javascript
function createGlobal() {
  message = "Hello, world!"; // 선언 없음
}

createGlobal();
console.log(message); // 출력: "Hello, world!" ('message'라는 전역 변수가 생성됨)
```
이러한 동작은 변수가 실수로 전역 스코프에 생성되어 코드의 다른 부분과 충돌할 수 있으므로 추적하기 어려운 버그로 이어질 수 있다.

**Strict mode**에서는 이것이 허용되지 않는다. 선언되지 않은 변수에 값을 할당하면 `ReferenceError`가 발생한다.

**Strict Mode 예시:**
```javascript
"use strict";

function createGlobal() {
  message = "Hello, world!"; // 선언 없음
}

createGlobal(); 
// ReferenceError: assignment to undeclared variable "message" 오류 발생
```

## 해결 방법

해결책은 간단하며 좋은 코딩 습관을 장려한다: **변수를 사용하기 전에 항상 선언하라**.

JavaScript의 선언 키워드(`let`, `const` 또는 `var`) 중 하나를 사용하여 적절한 스코프 내에서 변수를 선언하면 된다.

### `let`을 사용한 해결책

변수의 값이 변경되어야 하는 경우 `let`을 사용한다.

```javascript
"use strict";

function assignValue() {
  let message; // 변수 선언
  message = "This is a valid assignment.";
  console.log(message);
}

assignValue();
```

### `const`를 사용한 해결책

변수의 값이 재할당되지 않을 경우 `const`를 사용한다. 이는 일반적으로 우발적인 재할당을 방지하는 데 선호된다.

```javascript
"use strict";

function assignConstant() {
  const greeting = "Hello!"; // 선언 및 할당
  console.log(greeting);
  // greeting = "Hi!"; // 이 코드는 TypeError를 발생시킨다
}

assignConstant();
```

### `var`를 사용한 해결책

`var`도 옵션이지만, `let`과 `const`는 함수 스코프가 아닌 블록 스코프(`{...}`)를 가지므로 다른 유형의 버그를 예방하는 데 도움이 되어 일반적으로 사용이 권장된다.

```javascript
"use strict";

function assignWithVar() {
  var count; // 변수 선언
  count = 100;
  console.log(count);
}

assignWithVar();
```

변수를 명시적으로 선언함으로써 코드를 더 명확하고 유지보수하기 쉽게 만들고 `ReferenceError: assignment to undeclared variable` 오류를 방지할 수 있다.
