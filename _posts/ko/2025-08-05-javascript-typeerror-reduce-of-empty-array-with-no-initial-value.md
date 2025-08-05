typora-root-url: ../
layout: single
title: >
    JavaScript TypeError: Reduce of empty array with no initial value 해결 방법
seo_title: >
    JavaScript TypeError: Reduce of empty array with no initial value 해결 방법
date: 2025-08-05T21:30:00+09:00
header:
   teaser: /images/header_images/overlay_image_js.png
   overlay_image: /images/header_images/overlay_image_js.png
   overlay_filter: 0.5
excerpt: >
    JavaScript에서 "TypeError: Reduce of empty array with no initial value"는 초기값 없이 빈 배열에 대해 reduce() 메서드를 호출할 때 발생하는 오류입니다. 이 글에서는 이 오류의 원인을 분석하고 해결 방법을 알아봅니다.
seo_description: >
    JavaScript에서 "TypeError: Reduce of empty array with no initial value"는 초기값 없이 빈 배열에 대해 reduce() 메서드를 호출할 때 발생하는 오류입니다. 이 글에서는 이 오류의 원인을 분석하고 해결 방법을 알아봅니다.
categories:
  - ko_Troubleshooting
tags:
  - JavaScript
  - TypeError
  - reduce
  - Array
---

## 문제 상황

JavaScript에서 배열의 `reduce()` 메서드를 사용할 때 `TypeError: Reduce of empty array with no initial value` 오류가 발생할 수 있습니다.
이 오류는 이름 그대로, 초기값(initial value)이 제공되지 않은 상태에서 빈 배열에 `reduce()`를 호출하려고 할 때 발생합니다.

```javascript
const numbers = [];

// 초기값 없이 빈 배열에 reduce()를 호출하여 TypeError 발생
const sum = numbers.reduce((accumulator, currentValue) => accumulator + currentValue);

console.log(sum);
```

위 코드는 빈 배열 `numbers`에 `reduce()`를 적용하고 있습니다.
`reduce()` 메서드는 두 번째 인자로 초기값을 받을 수 있는데, 이 예제에서는 초기값이 생략되었습니다.
이 경우 `reduce()`는 배열의 첫 번째 요소를 초기값으로 사용하려고 하지만, 배열이 비어있어 첫 번째 요소가 없으므로 `TypeError`가 발생합니다.

## 원인 분석

`Array.prototype.reduce()` 메서드의 동작 방식 때문에 이 오류가 발생합니다.

`reduce()` 메서드의 구문은 다음과 같습니다.

```javascript
arr.reduce(callback(accumulator, currentValue[, index[, array]])[, initialValue])
```

-   `callback`: 각 요소에 대해 실행할 함수.
-   `initialValue` (선택 사항): `callback` 함수 최초 호출 시 `accumulator`에 할당될 값.

동작 흐름은 `initialValue`의 제공 여부에 따라 달라집니다.

1.  **`initialValue`가 제공된 경우**:
    -   `accumulator`는 `initialValue`로 초기화됩니다.
    -   `currentValue`는 배열의 첫 번째 요소부터 시작합니다.
    -   빈 배열에 호출해도 `initialValue`가 그대로 반환되므로 오류가 발생하지 않습니다.

2.  **`initialValue`가 제공되지 않은 경우**:
    -   `accumulator`는 배열의 **첫 번째 요소**로 초기화됩니다.
    -   `currentValue`는 배열의 **두 번째 요소**부터 시작합니다.
    -   만약 배열이 비어 있다면, `accumulator`로 사용할 첫 번째 요소가 없으므로 `TypeError`가 발생합니다.

결국, 오류의 근본 원인은 **초기값 없이 빈 배열에 대해 축소(reduction) 연산을 시도**했기 때문입니다.

## 해결 방법

### 1. `reduce()`에 초기값 제공

가장 간단하고 안전한 해결책은 `reduce()` 메서드에 항상 초기값을 제공하는 것입니다.
초기값은 연산의 종류에 따라 적절하게 선택해야 합니다.

-   숫자의 합을 구하는 경우: `0`
-   숫자의 곱을 구하는 경우: `1`
-   문자열을 연결하는 경우: `''` (빈 문자열)
-   객체를 만드는 경우: `{}` (빈 객체)

```javascript
const numbers = [];

// 초기값으로 0을 제공
const sum = numbers.reduce((accumulator, currentValue) => accumulator + currentValue, 0);

console.log(sum); // 0
```

이제 코드는 빈 배열에 대해서도 오류 없이 `0`을 올바르게 반환합니다.

### 2. 배열이 비어있는지 확인 후 `reduce()` 호출

상황에 따라 빈 배열을 다르게 처리해야 할 수도 있습니다.
이 경우, `reduce()`를 호출하기 전에 배열의 길이를 확인하여 분기 처리를 할 수 있습니다.

```javascript
const numbers = [];
let sum;

if (numbers.length > 0) {
    sum = numbers.reduce((accumulator, currentValue) => accumulator + currentValue);
} else {
    // 빈 배열일 때의 기본값 설정
    sum = 0; 
}

console.log(sum); // 0
```

이 방법은 코드가 조금 더 길어지지만, 로직을 명확하게 표현할 수 있습니다.

### 3. 기본값과 함께 단축 평가 사용 (ES6+)

조금 더 간결한 코드를 원한다면, `reduce`의 결과가 `undefined`나 `null`이 될 수 있는 경우 기본값을 설정하는 방식을 사용할 수 있습니다.
하지만 이 방법은 `reduce`가 오류를 던지는 근본적인 문제를 해결하지는 않으므로, 초기값을 제공하는 첫 번째 방법을 사용하는 것이 더 좋습니다.

```javascript
// 이 코드는 여전히 오류를 발생시키므로 좋은 예가 아님
// const sum = (numbers.length > 0 ? numbers.reduce(...) : 0);

// 항상 초기값을 제공하는 것이 가장 좋은 습관입니다.
const sumWithInitialValue = numbers.reduce((acc, val) => acc + val, 0);
```

## 결론

`TypeError: Reduce of empty array with no initial value`는 `reduce()` 메서드의 동작 방식을 이해하면 쉽게 해결할 수 있는 문제입니다.
가장 좋은 해결책이자 예방책은 **`reduce()`를 사용할 때 항상 적절한 초기값을 제공하는 것**입니다.
이는 코드를 더 예측 가능하고 안정적으로 만들어주며, 빈 배열과 같은 엣지 케이스를 자연스럽게 처리해줍니다.
