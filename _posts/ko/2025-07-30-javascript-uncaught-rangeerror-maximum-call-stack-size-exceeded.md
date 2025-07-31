---
typora-root-url: ../
layout: single
title: "JavaScript 'Maximum call stack size exceeded' 오류 해결 방법"
date: 2025-07-30T11:00:00+09:00
excerpt: "JavaScript에서 'Uncaught RangeError: Maximum call stack size exceeded' 오류가 발생하는 원인인 무한 재귀를 파악하고, 함수에 올바른 종료 조건을 구현하여 문제를 해결하는 방법을 알아봅니다."
header:
   teaser: /images/header_images/overlay_image_js.png
   overlay_image: /images/header_images/overlay_image_js.png
   overlay_filter: 0.5
categories:
  - ko_Troubleshooting
tags:
  - JavaScript
  - RangeError
  - 콜 스택
  - 재귀
---

## "Uncaught RangeError: Maximum call stack size exceeded" 오류 이해하기

이 오류는 JavaScript에서 함수가 자기 자신을 너무 많이 호출하여 스택 오버플로가 발생할 때 나타난다. 콜 스택(Call Stack)은 인터프리터가 여러 함수를 호출하는 스크립트에서 현재 위치를 추적하는 메커니즘이다. 스택의 크기에는 제한이 있으며, 이 한도를 초과하면 오류가 발생한다.

### 주요 원인: 무한 재귀

가장 흔한 원인은 **무한 재귀(infinite recursion)**다. 이는 함수가 적절한 종료 조건 없이 자기 자신을 계속 호출하는 경우에 발생한다.

**문제 코드:**
```javascript
function infiniteLoop() {
  infiniteLoop(); // 함수가 멈추는 조건 없이 자신을 호출한다.
}

// 이 함수를 호출하면 오류가 발생한다.
// infiniteLoop(); 
```

또 다른 일반적인 시나리오는 기본 케이스(base case)는 있지만, 재귀 호출이 입력을 기본 케이스로 유도하지 못하는 경우다.

```javascript
function countdown(n) {
  if (n === 0) {
    console.log("Blast off!");
    return;
  }
  console.log(n);
  countdown(n + 1); // 실수! 0이라는 기본 케이스에서 멀어지게 숫자를 증가시킨다.
}

// countdown(10);
```

### 오류 해결 방법

#### 1. 기본 케이스(종료 조건) 추가하기

재귀 함수는 반드시 재귀를 멈추는 조건인 **기본 케이스(base case)**를 가져야 한다.

**잘못된 코드 (기본 케이스 없음):**
```javascript
function goOnForever() {
    goOnForever();
}
```

**해결책:**
조건이 충족되면 함수가 자신을 다시 호출하지 않도록 하는 조건을 만들어야 한다.

```javascript
function countdown(n) {
  if (n <= 0) { // 기본 케이스
    console.log("Done!");
    return;
  }
  console.log(n);
  countdown(n - 1); // 기본 케이스를 향해 가는 재귀 호출
}

countdown(5); // 5, 4, 3, 2, 1, Done!
```

#### 2. 반복적 접근 방식으로 변환하기

재귀적 해결책이 무한이 아니더라도 너무 깊으면 스택 크기를 초과할 수 있다. 이런 경우 함수를 루프(반복적 접근 방식)를 사용하도록 변환하면 문제를 해결할 수 있다.

**재귀 함수:**
```javascript
function sumRecursive(n, total = 0) {
  if (n <= 0) {
    return total;
  }
  return sumRecursive(n - 1, total + n);
}
```

**반복적 해결책:**
```javascript
function sumIterative(n) {
  let total = 0;
  for (let i = 1; i <= n; i++) {
    total += i;
  }
  return total;
}

// 이 함수는 스택 오버플로 없이 매우 큰 숫자도 처리할 수 있다.
console.log(sumIterative(100000)); 
```

재귀를 신중하게 관리하고 모든 재귀 함수에 도달 가능한 기본 케이스가 있도록 보장함으로써 "Maximum call stack size exceeded" 오류를 피하고 더 안정적인 코드를 작성할 수 있다.
