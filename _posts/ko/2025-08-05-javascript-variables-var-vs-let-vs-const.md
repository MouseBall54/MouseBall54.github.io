---
typora-root-url: ../
layout: single
title: >
   JavaScript 변수: var, let, const의 차이점

lang: ko
translation_id: javascript-variables-var-vs-let-vs-const
header:
   teaser: /images/header_images/overlay_image_js.png
   overlay_image: /images/header_images/overlay_image_js.png
   overlay_filter: 0.5
excerpt: >
   JavaScript에서 var, let, const의 차이점을 깊이 알아보세요. 스코프, 호이스팅, 재할당 규칙을 이해하여 더 깨끗하고 예측 가능하며 현대적인 JS 코드를 작성하세요.
categories:
   - ko_Troubleshooting
tags:
   - JavaScript
   - ES6
   - var
   - let
   - const
---

## 서론

오랫동안 `var`는 JavaScript에서 변수를 선언하는 유일한 방법이었습니다. ES6(ECMAScript 2015)가 도입되면서, 변수 스코프와 동작에 대한 더 많은 제어를 제공하는 `let`과 `const`라는 두 개의 새로운 키워드가 추가되었습니다. 이 세 가지의 차이점을 이해하는 것은 현대적이고 유지 관리하기 쉬우며 버그 없는 JavaScript를 작성하는 데 매우 중요합니다.

이 가이드에서는 스코프, 호이스팅, 재할당 규칙을 기준으로 `var`, `let`, `const`를 비교합니다.

## 1. 스코프 (Scope)

스코프는 코드에서 변수에 접근할 수 있는 위치를 결정합니다.

### `var`: 함수 스코프

`var`로 선언된 변수는 **함수 스코프(function-scoped)**를 가집니다. 이는 선언된 함수 내에서만 접근할 수 있음을 의미합니다. 함수 외부에서 선언되면 전역 스코프를 가집니다.

```javascript
function myFunction() {
    if (true) {
        var myVar = "var로부터의 인사";
    }
    console.log(myVar); // "var로부터의 인사" - 여기서 접근 가능
}
myFunction();
// console.log(myVar); // ReferenceError: myVar is not defined - 여기서 접근 불가
```
`myVar`가 `if` 블록 밖에서도 접근 가능하다는 점에 유의하세요. 이는 `var`가 블록 스코프(`{...}`)를 존중하지 않기 때문이며, 예기치 않은 동작으로 이어질 수 있습니다.

### `let`과 `const`: 블록 스코프

`let`과 `const`로 선언된 변수는 **블록 스코프(block-scoped)**를 가집니다. 이들은 정의된 블록(즉, 중괄호 `{...}` 내부) 내에서만 접근할 수 있습니다.

```javascript
function anotherFunction() {
    if (true) {
        let myLet = "let으로부터의 인사";
        const myConst = "const로부터의 인사";
        console.log(myLet);   // 접근 가능
        console.log(myConst); // 접근 가능
    }
    // console.log(myLet);   // ReferenceError: myLet is not defined
    // console.log(myConst); // ReferenceError: myConst is not defined
}
anotherFunction();
```
이것은 훨씬 더 직관적이며 다른 많은 프로그래밍 언어에서 변수가 작동하는 방식과 유사합니다. 변수의 생명주기를 필요한 블록으로 제한하여 버그를 예방하는 데 도움이 됩니다.

## 2. 호이스팅 (Hoisting)

호이스팅은 코드 실행 전에 선언을 해당 스코프의 맨 위로 옮기는 JavaScript의 동작입니다.

### `var`: 호이스팅되고 초기화됨

`var` 변수는 해당 스코프의 맨 위로 호이스팅되고 `undefined` 값으로 초기화됩니다.

```javascript
console.log(hoistedVar); // undefined (오류 없음)
var hoistedVar = "나는 호이스팅되었어";
console.log(hoistedVar); // "나는 호이스팅되었어"
```
이는 `var` 변수가 선언되기 전에 접근해도 오류가 발생하지 않지만, 그 값은 `undefined`가 됨을 의미합니다.

### `let`과 `const`: 호이스팅되지만 초기화되지 않음

`let`과 `const` 변수도 호이스팅되지만, **초기화되지는 않습니다**. 선언 전에 접근하면 `ReferenceError`가 발생합니다. 블록의 시작부터 선언까지의 기간을 **일시적 사각지대(Temporal Dead Zone, TDZ)**라고 합니다.

```javascript
// console.log(hoistedLet); // ReferenceError: Cannot access 'hoistedLet' before initialization
let hoistedLet = "나도 호이스팅되었어";

// console.log(hoistedConst); // ReferenceError: Cannot access 'hoistedConst' before initialization
const hoistedConst = "나도 그래";
```
이 동작은 값이 할당되기 전에 변수를 실수로 사용하는 것을 방지하여 코드를 더 견고하게 만듭니다.

## 3. 재할당 (Reassignment)

이것이 `let`과 `const`의 주된 차이점입니다.

### `var`와 `let`: 재할당 가능

`var` 또는 `let`으로 선언된 변수는 업데이트하거나 재할당할 수 있습니다.

```javascript
var myVarVariable = "첫 번째 값";
myVarVariable = "새로운 값"; // 허용됨

let myLetVariable = "첫 번째 값";
myLetVariable = "새로운 값"; // 허용됨
```

### `const`: 재할당 불가

`const`(상수를 의미)로 선언된 변수는 선언 시에 초기화되어야 하며 새로운 값을 **재할당할 수 없습니다**.

```javascript
const myConstVariable = "이 값은 상수입니다";
// myConstVariable = "변경 시도"; // TypeError: Assignment to constant variable.
```

**객체 및 배열에 대한 중요 참고 사항:**
`const`로 객체나 배열을 선언하면, 그 내용이 아니라 해당 객체/배열에 대한 **참조**가 상수임을 의미합니다. 객체의 속성이나 배열의 요소는 여전히 수정할 수 있습니다.

```javascript
const myObj = { name: "Alice" };
myObj.name = "Bob"; // 이것은 허용됩니다!
console.log(myObj.name); // "Bob"

const myArray = [1, 2, 3];
myArray.push(4); // 이것도 허용됩니다!
console.log(myArray); // [1, 2, 3, 4]

// 하지만 변수 자체를 재할당할 수는 없습니다
// myObj = { name: "Charlie" }; // TypeError
// myArray = [5, 6]; // TypeError
```

## 요약 및 모범 사례

| 키워드 | 스코프 | 호이스팅 | 재할당 | 재선언(같은 스코프 내) |
| :---: | :--- | :--- | :---: | :---: |
| `var` | 함수 | 호이스팅되고 `undefined`로 초기화 | 예 | 예 |
| `let` | 블록 | 호이스팅되지만 초기화되지 않음(TDZ) | 예 | 아니요 |
| `const` | 블록 | 호이스팅되지만 초기화되지 않음(TDZ) | 아니요 | 아니요 |

현대 JavaScript 변수 선언의 모범 사례는 다음과 같습니다.

1.  **기본적으로 `const` 사용**: 우발적인 재할당을 방지하여 코드를 더 예측 가능하게 만듭니다. 변수의 식별자가 재할당되지 않을 것임을 나타냅니다.
2.  **변수를 재할당해야 할 때만 `let` 사용**: 이는 일반적으로 루프 카운터나 블록 내에서 업데이트해야 하는 변수에 해당합니다.
3.  **`var` 사용 피하기**: 현대 JavaScript(ES6+)에서는 `var`를 사용할 이유가 거의 없습니다. `var`의 함수 스코프 및 호이스팅 동작은 `let`과 `const`가 방지하도록 설계된 버그를 유발할 수 있습니다.

이러한 규칙을 따르면 더 명확하고 신뢰할 수 있으며 디버깅하기 쉬운 JavaScript 코드를 작성할 수 있습니다.
