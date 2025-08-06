---
typora-root-url: ../
layout: single
title: "JavaScript 오류 'Uncaught ReferenceError: is not defined' 해결 방법"

lang: ko
translation_id: javascript-uncaught-referenceerror-is-not-defined
excerpt: "'Uncaught ReferenceError: ... is not defined'는 JavaScript에서 변수나 함수가 선언되지 않았거나 접근할 수 없는 스코프에 있을 때 발생하는 흔한 오류입니다. 원인과 해결 방법을 알아봅니다."
header:
   teaser: /images/header_images/overlay_image_js.png
   overlay_image: /images/header_images/overlay_image_js.png
   overlay_filter: 0.5
categories:
  - ko_Troubleshooting
tags:
  - JavaScript
  - ReferenceError
  - Troubleshooting
  - Scope
---

## 'Uncaught ReferenceError: ... is not defined' 오류란?

`Uncaught ReferenceError: ... is not defined`는 JavaScript 코드를 실행할 때 특정 변수나 함수를 찾을 수 없을 때 발생하는 오류다.
이것은 해당 식별자가 현재 스코프(scope) 또는 전역 스코프(global scope) 내에서 선언되지 않았음을 의미한다.
개발 과정에서 매우 흔하게 접하는 오류 중 하나다.

## 주요 원인

### 1. 변수 또는 함수 이름의 오타

가장 단순하고 흔한 원인이다. 변수나 함수를 선언할 때 사용한 이름과 호출할 때 사용한 이름이 다르면 이 오류가 발생한다.

```javascript
let myVariable = "Hello, World!";

// 'myvariable'이 아닌 'myVariable'로 호출해야 함
console.log(myvariable); 
// Uncaught ReferenceError: myvariable is not defined
```

JavaScript는 대소문자를 구분하므로 `myVariable`과 `myvariable`은 다른 식별자로 취급된다.

### 2. 변수 선언 전 사용

변수가 선언되기 전에 해당 변수에 접근하려고 하면 `ReferenceError`가 발생한다.
`var`로 선언된 변수는 호이스팅(hoisting)으로 인해 `undefined`를 반환하지만, `let`과 `const`는 임시 사각지대(Temporal Dead Zone, TDZ)에 놓여 이 오류를 발생시킨다.

```javascript
console.log(x); // Uncaught ReferenceError: Cannot access 'x' before initialization
let x = 10;
```

### 3. 스코프(Scope) 문제

변수나 함수가 특정 스코프 내에서만 유효한데, 그 스코프 밖에서 접근하려고 할 때 오류가 발생한다.

```javascript
function myFunction() {
    let localVariable = "I am local";
    console.log(localVariable); // 정상 작동
}

myFunction();

console.log(localVariable); // Uncaught ReferenceError: localVariable is not defined
```

`localVariable`은 `myFunction` 함수 내부에서만 접근할 수 있는 지역 변수이므로, 함수 밖에서는 찾을 수 없다.

### 4. 외부 라이브러리 로드 실패

jQuery나 Lodash 같은 외부 라이브러리를 사용하지만, HTML 파일에서 해당 라이브러리를 제대로 로드하지 않았을 때도 이 오류가 발생할 수 있다.

```html
<!-- jQuery 라이브러리를 로드하지 않은 상태 -->
<script>
    // '$'는 jQuery의 식별자이지만, 라이브러리가 없으므로 정의되지 않음
    $("#myElement").hide(); 
    // Uncaught ReferenceError: $ is not defined
</script>
```

## 해결 방법

### 1. 이름 확인 및 오타 수정

가장 먼저 변수나 함수의 이름을 선언부와 호출부에서 정확히 일치하는지 확인한다. 대소문자까지 꼼꼼히 살펴야 한다.

### 2. 선언 순서 확인

변수는 항상 사용하기 전에 선언해야 한다. 코드의 논리적 흐름에 맞게 변수와 함수 선언을 코드 상단이나 사용 지점 이전에 배치한다.

### 3. 스코프 이해 및 조정

변수나 함수가 필요한 모든 곳에서 접근 가능한지 스코프를 확인해야 한다.
여러 함수에서 공통으로 사용해야 하는 변수라면, 해당 함수들을 포함하는 더 넓은 스코프에 변수를 선언해야 한다.

```javascript
let sharedVariable = "I am shared";

function functionOne() {
    console.log(sharedVariable);
}

function functionTwo() {
    console.log(sharedVariable);
}

functionOne(); // "I am shared"
functionTwo(); // "I am shared"
```

### 4. 외부 스크립트 로드 확인

외부 라이브러리를 사용한다면, HTML 파일의 `<head>` 태그나 `<body>` 태그가 닫히기 직전에 `<script>` 태그를 통해 라이브러리가 올바르게 로드되었는지 확인한다.
스크립트 URL이 정확한지, 네트워크 문제로 로드에 실패하지 않았는지 개발자 도구의 네트워크 탭에서 확인하는 것이 좋다.

```html
<head>
    <!-- jQuery 라이브러리를 먼저 로드 -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>
    <!-- 이제 '$'를 정상적으로 사용할 수 있음 -->
    <script>
        $("#myElement").hide();
    </script>
</body>
```

## 결론

`Uncaught ReferenceError`는 대부분 기본적인 실수에서 비롯된다.
오타, 잘못된 선언 순서, 스코프에 대한 오해 등이 주된 원인이다.
오류 메시지에 나타난 변수나 함수 이름을 중심으로 코드를 차근차근 살펴보면 대부분의 경우 쉽게 문제를 해결할 수 있다.
