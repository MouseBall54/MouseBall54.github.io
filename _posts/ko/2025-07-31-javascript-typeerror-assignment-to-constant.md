---
typora-root-url: ../
layout: single
title: "JavaScript \"TypeError: Assignment to constant variable\" 오류 해결 방법"
date: 2025-07-31T22:12:00+09:00
excerpt: "`const`의 속성을 배우고, 재할당이 필요한 변수에는 `let`을 사용하여 JavaScript의 \"TypeError: Assignment to constant variable\" 오류를 이해하고 해결하세요."
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
  - Const
  - ES6
---

## 서론

`TypeError: Assignment to constant variable`는 최신 JavaScript(ES6 이상)에서 흔히 발생하는 오류다. 이 오류는 `const` 키워드를 사용하여 선언된 변수에 값을 재할당하려고 할 때 발생한다. 이 가이드에서는 `const`의 동작 방식, 이 오류가 발생하는 이유, 그리고 이를 방지하기 위해 변수를 올바르게 관리하는 방법을 설명한다.

## `const` 이해하기

`const` 키워드는 상수를 선언하기 위해 ES6에서 도입되었다. 상수는 재할당을 통해 값을 변경할 수 없는 변수다. `const`로 변수를 선언할 때는 반드시 값으로 초기화해야 하며, 나중에 새로운 값을 할당할 수 없다.

### `const`의 주요 속성:
1.  **재할당 불가**: 일단 값이 할당되면 변수 식별자는 새로운 값을 가리킬 수 없다.
2.  **반드시 초기화 필요**: `const` 변수를 선언할 때는 값을 제공해야 한다.
3.  **블록 스코프**: `let`과 마찬가지로 `const` 변수는 정의된 블록(`{...}`)에 스코프가 한정된다.

### 오류 예시

```javascript
const myName = "Alice";

console.log(myName); // 출력: "Alice"

// 상수 변수에 재할당 시도
myName = "Bob"; 
// TypeError: Assignment to constant variable. 오류 발생
```

이는 `myName`이 상수로 선언되었기 때문에 JavaScript 엔진이 할당 변경을 막기 때문에 발생한다.

## 해결 방법

해결책은 변수에 대한 의도에 따라 달라진다.

### 1. 변경이 필요한 변수에는 `let` 사용하기

변수의 값이 시간이 지남에 따라 변경되도록 의도했다면 `const` 대신 `let`으로 선언해야 했다. `let` 키워드는 재할당할 수 있는 블록 스코프 변수를 선언한다.

**해결책:**
```javascript
let myName = "Alice"; // 'const' 대신 'let' 사용

console.log(myName); // 출력: "Alice"

// 이제 이것은 유효한 재할당이다
myName = "Bob"; 
console.log(myName); // 출력: "Bob"
```
이것이 가장 일반적인 해결책이다. 나중에 업데이트가 필요하다는 것을 깨달은 변수에 `const`를 사용했을 가능성이 높다.

### 2. 객체 및 배열과 함께 `const` 사용 시 주의사항

흔히 혼동하는 부분은 `const`가 객체 및 배열과 어떻게 작동하는지다. `const`로 객체나 배열을 선언하면 **변수 자체를 새로운 객체나 배열로 재할당할 수 없음**을 의미한다. 그러나 **객체의 속성이나 배열의 요소는 변경할 수 있다**.

**객체 예시:**
```javascript
const person = {
  name: "Alice",
  age: 30
};

// 이것은 허용됨: 상수 객체의 속성 수정
person.age = 31; 
console.log(person.age); // 출력: 31

// 이것은 허용되지 않음: 상수 변수를 새로운 객체로 재할당
person = { name: "Bob", age: 40 }; 
// TypeError: Assignment to constant variable. 오류 발생
```

**배열 예시:**
```javascript
const myNumbers = [1, 2, 3];

// 이것은 허용됨: 상수 배열의 내용 수정
myNumbers.push(4);
console.log(myNumbers); // 출력: [1, 2, 3, 4]

// 이것은 허용되지 않음: 상수 변수를 새로운 배열로 재할당
myNumbers = [5, 6, 7];
// TypeError: Assignment to constant variable. 오류 발생
```

객체의 속성이 변경되는 것을 막으려면 `Object.freeze()`를 사용해야 한다.

```javascript
const person = Object.freeze({
  name: "Alice",
  age: 30
});

person.age = 31; // 오류는 발생하지 않지만, strict mode에서는 변경이 무시된다.
console.log(person.age); // 출력: 30
```

## 모범 사례

- **기본적으로 `const` 사용**: 일반적인 규칙으로, 모든 변수를 기본적으로 `const`로 선언한다.
- **필요할 때만 `let`으로 전환**: 변수를 재할당해야 할 필요가 생기면, 그때 가서 선언을 `const`에서 `let`으로 변경한다. 이 습관은 우발적인 재할당을 방지하고 코드를 더 예측 가능하게 만든다.

`const`와 `let`의 차이점을 이해하면 `TypeError: Assignment to constant variable`를 쉽게 피하고 더 견고한 코드를 작성할 수 있다.
