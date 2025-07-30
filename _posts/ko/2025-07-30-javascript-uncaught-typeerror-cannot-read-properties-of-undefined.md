---
typora-root-url: ../
layout: single
title: "JavaScript 'undefined'의 속성을 읽을 수 없음(Uncaught TypeError) 오류 해결 방법"
date: 2025-07-30T22:00:00+09:00
excerpt: "JavaScript에서 'Uncaught TypeError: Cannot read properties of undefined' 오류가 발생하는 원인을 파악하고, 효과적인 해결 방법을 알아봅니다."
categories:
  - ko_Troubleshooting
tags:
  - JavaScript
  - TypeError
  - undefined
  - Debugging
---

## 서론

"Uncaught TypeError: Cannot read properties of undefined" 오류는 JavaScript에서 가장 흔하게 발생하는 문제 중 하나다. 이 오류는 `undefined` 값을 가진 변수의 속성이나 메서드에 접근하려고 할 때 발생한다. 이 가이드는 주요 원인과 해결 방법을 설명한다.

## 오류 발생 원인

이 오류는 사용하려는 변수에 값이 할당되지 않았거나, 접근하려는 객체 속성이 존재하지 않기 때문에 발생한다. JavaScript 엔진은 `undefined`에서 속성을 읽을 수 없다.

### 주요 발생 시나리오

1.  **초기화되지 않은 변수의 속성에 접근하는 경우.**
2.  **함수가 값을 반환하지 않는 경우.**
3.  **존재하지 않는 객체 속성에 접근하는 경우.**
4.  **DOM 요소를 찾지 못한 경우.**

---

## 오류 해결 방법

### 1. 변수 초기화 확인

모든 변수는 사용하기 전에 값을 가지고 있는지 확인해야 한다.

**문제 코드:**
```javascript
let user;
console.log(user.name); // user가 undefined이므로 TypeError 발생
```

**해결책:**
변수를 기본값으로 초기화한다.

```javascript
let user = {};
console.log(user.name); // undefined를 출력하지만, 오류는 발생하지 않음
```

### 2. 함수 반환 값 확인

명시적으로 값을 `return`하지 않는 함수는 기본적으로 `undefined`를 반환한다.

**문제 코드:**
```javascript
function getUser(id) {
  // 사용자를 찾지 못해 반환문이 실행되지 않음
}

const user = getUser(1);
console.log(user.name); // TypeError 발생
```

**해결책:**
함수가 항상 유효한 객체나 `null`을 반환하도록 하고, `null`인 경우를 처리한다.

```javascript
function getUser(id) {
  if (id === 1) {
    return { name: '홍길동' };
  }
  return null; // 사용자를 찾지 못하면 null 반환
}

const user = getUser(1);
if (user) {
  console.log(user.name); // "홍길동" 출력
} else {
  console.log('사용자를 찾을 수 없습니다.');
}
```

### 3. 옵셔널 체이닝(`?.`) 사용

중첩된 객체를 다룰 때, 어떤 단계에서든 속성이 누락될 수 있다. 옵셔널 체이닝은 중첩 속성에 안전하게 접근하는 방법을 제공한다.

**문제 코드:**
```javascript
const user = {
  profile: {
    // address 속성이 없음
  }
};
console.log(user.profile.address.street); // TypeError 발생
```

**해결책:**
옵셔널 체이닝 연산자(`?.`)를 사용하여 존재하지 않을 수 있는 속성에 안전하게 접근한다.

```javascript
const user = {
  profile: {}
};
console.log(user.profile.address?.street); // undefined 출력, 오류 없음
```

### 4. DOM 요소 존재 여부 확인

DOM 작업을 할 때, HTML이 완전히 로드되기 전에 JavaScript 코드가 실행되면 이 오류가 자주 발생한다.

**문제 코드:**
```html
<script>
  const button = document.getElementById('myButton');
  button.addEventListener('click', () => console.log('클릭됨!')); // TypeError 발생
</script>
<button id="myButton">클릭하세요</button>
```

**해결책:**
스크립트를 `<body>` 태그의 끝에 배치하거나 `DOMContentLoaded`와 같은 이벤트 리스너를 사용한다.

```html
<body>
  <button id="myButton">클릭하세요</button>
  <script>
    const button = document.getElementById('myButton');
    if (button) {
      button.addEventListener('click', () => console.log('클릭됨!'));
    }
  </script>
</body>
```

또는 `DOMContentLoaded` 사용:
```javascript
document.addEventListener('DOMContentLoaded', () => {
  const button = document.getElementById('myButton');
  if (button) {
    button.addEventListener('click', () => console.log('클릭됨!'));
  }
});
```

## 결론

"Cannot read properties of undefined" 오류를 해결하려면, 변수와 객체를 사용하기 전에 적절하게 초기화해야 한다. `null` 또는 `undefined`를 확인하고 옵셔널 체이닝을 사용하는 등 방어적인 코딩 기법은 이 오류를 예방하고 코드를 더 견고하게 만든다.
