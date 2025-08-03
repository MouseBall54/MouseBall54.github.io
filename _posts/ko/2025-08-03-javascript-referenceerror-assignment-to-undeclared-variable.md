---
typora-root-url: ../
layout: single
title: >
    JavaScript "ReferenceError: assignment to undeclared variable" 오류 해결 방법
date: 2025-08-03T11:05:00+09:00
header:
   teaser: /images/header_images/overlay_image_js.png
   overlay_image: /images/header_images/overlay_image_js.png
   overlay_filter: 0.5
excerpt: >
    이 포스트는 JavaScript의 엄격 모드(strict mode)에서 선언되지 않은 변수에 값을 할당할 때 발생하는 "ReferenceError: assignment to undeclared variable" 오류를 해결하는 방법을 설명합니다.
categories:
  - ko_Troubleshooting
tags:
  - JavaScript
  - ReferenceError
  - Strict Mode
  - Debugging
---

## "ReferenceError: assignment to undeclared variable"란?

이 JavaScript 오류는 특별합니다.
**엄격 모드(strict mode)**에서만 발생합니다.
변수에 값을 할당할 때 나타납니다.
하지만 그 변수는 아직 선언되지 않았습니다.
선언에는 `let`, `const`, `var` 같은 키워드를 사용합니다.
비-엄격 모드에서는 이 코드가 전역 변수를 생성합니다.
엄격 모드는 잠재적 버그를 피하기 위해 이 동작을 막습니다.
더 깨끗하고 신뢰성 있는 코드 작성에 도움이 됩니다.

## 주요 원인과 해결 방법

원인은 간단합니다. 변수가 선언 없이 사용된 것입니다.

### 선언되지 않은 변수에 값 할당

변수를 사용하기 전에 선언하는 것을 잊을 수 있습니다.
이는 종종 간단한 오타나 실수입니다.

**문제 코드 (엄격 모드):**
```javascript
'use strict';

function calculateTotal(price) {
  // 'total' 대신 'totl'로 오타 발생
  totl = price * 1.1; // ReferenceError
  return totl;
}

// 또는 단순히 선언을 잊은 경우
x = 10; // ReferenceError
console.log(x);
```

위 예제에서 `totl`과 `x`는 선언된 적이 없습니다.
엄격 모드는 이를 감지하고 `ReferenceError`를 발생시킵니다.

**해결 방법:**
해결책은 간단합니다.
모든 변수는 값을 할당하기 전에 선언하세요.
`let`, `const`, 또는 `var`를 사용하세요.

**수정된 코드:**
```javascript
'use strict';

function calculateTotal(price) {
  // 'let'으로 'total'을 선언
  let total = price * 1.1;
  return total;
}

// 'let'으로 'x'를 선언
let x = 10;
console.log(x);
```
`let`을 추가하여 변수를 적절하게 선언했습니다.
이제 코드는 오류 없이 실행됩니다.

## 엄격 모드의 중요성

이 오류는 엄격 모드의 핵심 장점을 보여줍니다.
실수로 전역 변수를 생성하는 것을 방지합니다.
우발적인 전역 변수는 많은 문제를 일으킬 수 있습니다.
애플리케이션의 다른 변수와 충돌할 수 있습니다.
이는 예측 불가능한 동작과 버그로 이어집니다.
전역 변수로 인한 버그는 추적하기 어려운 경우가 많습니다.
엄격 모드는 이런 조용한 오류를 눈에 띄는 `ReferenceError`로 바꿉니다.
더 나은 코딩 습관을 강제합니다.

## 엄격 모드 활성화 방법

엄격 모드는 두 가지 방법으로 활성화할 수 있습니다.

1.  **스크립트 전체에 적용:**
    JavaScript 파일의 가장 처음에 `'use strict';`를 배치합니다.

    ```javascript
    'use strict';

    // 이 스크립트의 모든 코드는 엄격 모드로 실행됩니다.
    let a = 1;
    b = 2; // ReferenceError
    ```

2.  **특정 함수에 적용:**
    함수 본문의 시작 부분에 `'use strict';`를 배치합니다.

    ```javascript
    function myStrictFunction() {
      'use strict';
      // 이 함수 내부의 코드는 엄격 모드입니다.
      let c = 3;
      d = 4; // ReferenceError
    }
    ```

## 결론

"ReferenceError: assignment to undeclared variable"는 유용한 오류입니다.
JavaScript 엄격 모드의 한 기능입니다.
변수를 먼저 선언하지 않고 사용하려 한다는 신호입니다.
해결하려면 항상 `let`, `const`, 또는 `var`로 변수를 선언하세요.
엄격 모드를 채택하는 것은 모범 사례입니다.
더 견고하고 유지보수하기 좋은 JavaScript 코드를 작성하는 데 도움이 됩니다.
