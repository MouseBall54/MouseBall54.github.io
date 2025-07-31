---
typora-root-url: ../
layout: single
title: >
  "JavaScript "TypeError: '...' is not a function" 오류 해결 방법"
date: 2025-07-31T22:00:00+09:00
excerpt: >
  "호출하려는 변수가 실제 함수인지 확인하고, 스코프 문제나 오타를 점검하여 JavaScript의 "TypeError: '...' is not a function" 오류를 해결하세요."
  header:
   teaser: /images/header_images/overlay_image_js.png
   overlay_image: /images/header_images/overlay_image_js.png
   overlay_filter: 0.5
categories:
  - ko_Troubleshooting
tags:
  - JavaScript
  - TypeError
  - Debugging
  - Functions
---

## 서론

`TypeError: '...' is not a function`은 JavaScript에서 매우 흔하게 발생하는 오류다. 이 오류는 함수가 아닌 것을 함수처럼 호출하려고 할 때 발생한다. 함수 이름의 오타, 변수가 함수 이름을 덮어쓰는 경우, 또는 객체에 존재하지 않는 메서드를 호출하는 등 여러 가지 이유로 발생할 수 있다. 이 가이드에서는 일반적인 원인과 해결 방법을 안내한다.

## 1. 원인: 함수 이름의 오타

가장 직접적인 원인은 단순한 철자 실수다. 함수 이름을 잘못 입력하면 JavaScript는 해당 함수를 찾지 못하고 변수를 `undefined`로 취급하며, 이는 함수가 아니다.

### 예시

```javascript
function greetUser() {
  console.log("Hello, user!");
}

// 오타: 'greetUser'를 'greetUsers'로 잘못 입력
greetUsers(); 
// TypeError: greetUsers is not a function 오류 발생
```

### 해결책

- **철자 확인**: 함수 이름에 오타가 없는지 다시 확인하고, 정의된 이름과 일치하는지 확인한다.
- **IDE 또는 린터 사용**: VS Code의 IntelliSense나 ESLint와 같은 린터 도구는 코드를 실행하기 전에 이러한 오류를 잡아낼 수 있다.

## 2. 원인: 변수가 함수를 덮어쓰는 경우

함수와 동일한 이름으로 변수를 선언하면 변수의 값이 함수 정의를 덮어쓴다. 나중에 함수를 호출하려고 하면 실제로는 변수의 값을 호출하게 된다.

### 예시

```javascript
function myFunction() {
  console.log("This is a function.");
}

// 'myFunction' 변수가 함수 정의를 덮어씀
const myFunction = "This is a string.";

myFunction(); 
// TypeError: myFunction is not a function 오류 발생
```

### 해결책

- **이름 충돌 방지**: 변수와 함수에 고유하고 서술적인 이름을 사용한다. 같은 스코프 내에서 이름을 재사용하지 않는다.
- **함수에 `const` 사용**: `const`와 화살표 함수 표현식을 사용하여 함수를 선언하면 우발적인 재할당을 방지할 수 있다.
  ```javascript
  const myFunction = () => {
    console.log("This is a function.");
  };
  ```

## 3. 원인: 객체에 메서드가 존재하지 않는 경우

이 오류는 객체에 존재하지 않는 메서드를 호출하려고 할 때 자주 발생한다. 이는 DOM 요소나 API 데이터를 다룰 때 흔히 발생한다.

### 예시

```javascript
const myObject = {
  name: "Test Object",
  // 'sayHello' 메서드가 정의되지 않음
};

myObject.sayHello(); 
// TypeError: myObject.sayHello is not a function 오류 발생
```

또 다른 일반적인 시나리오는 문자열이다. 예를 들어, `toUpperCase()` 대신 `toUppercase()`를 사용하는 경우다.

```javascript
const myString = "hello world";
console.log(myString.toUppercase()); // 'c'가 소문자인 점에 유의
// TypeError: myString.toUppercase is not a function 오류 발생
```

### 해결책

- **객체 속성 확인**: 메서드를 호출하기 전에 객체에 해당 메서드가 존재하는지 확인한다. `console.log(myObject)`를 사용하여 객체의 속성과 메서드를 검사할 수 있다.
- **문서 참조**: 내장 메서드(문자열이나 배열 등)나 라이브러리의 메서드를 사용할 때는 항상 공식 문서를 참조하여 올바른 이름과 사용법을 확인한다.

## 4. 원인: 잘못된 Import/Export

모듈을 사용할 때, 함수가 아닌 것을 임포트하거나 잘못된 임포트 구문(예: `import myFunction` 대신 `import { myFunction }`)을 사용하면 이 오류가 발생할 수 있다.

### 예시

**`my-module.js`**:
```javascript
const myData = { value: 42 };
export default myData;
```

**`main.js`**:
```javascript
import myData from './my-module.js';

// myData는 함수가 아닌 객체다
myData(); 
// TypeError: myData is not a function 오류 발생
```

### 해결책

- **Export 확인**: 모듈에서 무엇이 export되는지 확인한다.
- **올바른 Import 구문 사용**: default 또는 named export에 맞는 올바른 구문을 사용하고 있는지 확인한다.
  - Named exports: `export const myFunction = ...` -> `import { myFunction } from ...`
  - Default exports: `export default myFunction` -> `import myFunction from ...`

이러한 사항들을 주의 깊게 확인하면 `TypeError: '...' is not a function`의 원인을 신속하게 파악하고 해결할 수 있다.
