---
typora-root-url: ../
layout: single
title: "TypeError: undefined is not a function 오류 해결 방법 (JavaScript)"
date: 2025-07-24T22:00:00+09:00
excerpt: "TypeError: undefined is not a function 오류 원인과 해결책을 다룬다."
categories:
  - ko_Troubleshooting
tags:
  - JavaScript
  - TypeError
  - Debugging
  - WebDev
---

## 소개

JavaScript에서 함수가 아닌 값을 호출할 때 발생한다.
코드 실행이 중단된다.
주요 원인과 해결 방법을 정리한다.

## 오류 내용

```
TypeError: undefined is not a function
    at myFunction (app.js:10)
    at HTMLButtonElement.onclick (index.html:5)
```

호출 대상이 undefined다. 함수가 아니다.

## 주요 원인

* 함수 이름 오타
* 스크립트 로드 순서 오류
* 모듈의 잘못된 import/export
* 전역 변수나 빌트인 메서드 덮어쓰기
* this 바인딩 문제

## 해결 방법 1: 이름 확인

오타를 점검한다.

```js
// 잘못된 예
element.addEventListerner('click', handleClick);

// 올바른 예
element.addEventListener('click', handleClick);
```

## 해결 방법 2: 로드 순서 검증

라이브러리 다음에 코드 실행.

```html
<script src="jquery.js"></script>
<script src="app.js"></script>
```

DOMContentLoaded 사용.

```js
document.addEventListener('DOMContentLoaded', () => {
  initApp();
});
```

## 해결 방법 3: import/export 확인

ES 모듈:

```js
// utils.js
export function doThing() { … }

// app.js
import { doThing } from './utils.js';
doThing();
```

CommonJS:

```js
// utils.js
module.exports = { doThing };

// app.js
const { doThing } = require('./utils');
doThing();
```

## 해결 방법 4: 전역 덮어쓰기 방지

표준 API 이름 재사용 금지.

```js
// 잘못된 예
const fetch = null;
fetch('/api'); // TypeError

// 올바른 예
// 이름 충돌이 없도록 변수명 변경
const customFetch = null;
```

## 해결 방법 5: this 바인딩 수정

bind 또는 화살표 함수 사용.

```js
class MyClass {
  constructor() {
    this.method = this.method.bind(this);
  }
  method() { … }
}
```

혹은:

```js
button.addEventListener('click', () => this.method());
```

## 결론

오타, 로드 순서, 모듈 설정, 전역 변수, this 바인딩을 점검하면 해결할 수 있다.
위 방법을 적용해 오류를 예방하자.
