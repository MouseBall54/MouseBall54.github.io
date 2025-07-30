---
typora-root-url: ../
layout: single
title: "JavaScript TypeError: Cannot read properties of null 오류 해결하기"
date: 2025-07-30T14:00:00+09:00
excerpt: "JavaScript 개발자라면 누구나 한 번쯤 마주치는 'Cannot read properties of null' 오류. 이 오류의 원인을 명확히 이해하고, DOM 로딩 시점과 조건부 접근을 통해 효과적으로 해결하는 방법을 알아봅니다."
categories:
  - ko_Troubleshooting
tags:
  - JavaScript
  - TypeError
  - DOM
  - Frontend
---

## JavaScript `TypeError: Cannot read properties of null` 오류란?

이 오류는 JavaScript에서 `null` 값을 가진 변수나 객체의 속성(property)에 접근하려고 할 때 발생합니다. `null`은 '값이 없음'을 의도적으로 나타내는 특별한 값입니다. 즉, 존재하지 않는 대상의 무언가를 읽으려고 시도했기 때문에 발생하는 `TypeError` 입니다.

웹 개발, 특히 DOM(Document Object Model)을 조작할 때 매우 흔하게 발생하는 오류입니다.

### 가장 흔한 원인: DOM 요소가 로드되기 전 접근

이 오류의 가장 대표적인 원인은 **HTML 요소가 화면에 그려지기 전에 JavaScript 코드가 해당 요소에 접근하려고 시도**하는 경우입니다.

**오류 발생 코드:**
```html
<!DOCTYPE html>
<html>
<head>
  <title>오류 예제</title>
  <script>
    const myButton = document.getElementById('myBtn');
    // 이 시점에는 아직 <button> 태그가 로드되지 않았습니다.
    // 따라서 document.getElementById('myBtn')는 null을 반환합니다.
    myButton.addEventListener('click', function() { // null의 addEventListener 속성에 접근 -> TypeError 발생
      alert('버튼 클릭!');
    });
  </script>
</head>
<body>
  <button id="myBtn">클릭하세요</button>
</body>
</html>
```
위 코드에서 `<script>` 태그는 `<body>` 태그보다 먼저 실행됩니다. 따라서 스크립트가 `document.getElementById('myBtn')`를 실행하는 시점에는 아직 `myBtn`이라는 ID를 가진 버튼이 DOM에 존재하지 않습니다. 결과적으로 `myButton` 변수에는 `null`이 할당되고, `null.addEventListener(...)`를 실행하려다 `TypeError`가 발생하는 것입니다.

### 해결 방법

#### 1. 스크립트를 `<body>` 태그 끝으로 옮기기

가장 간단하고 직관적인 해결책입니다. 스크립트가 DOM 요소에 접근하기 전에 모든 HTML 요소가 먼저 로드되도록 보장하는 방법입니다.

**해결된 코드:**
```html
<!DOCTYPE html>
<html>
<head>
  <title>해결 예제</title>
</head>
<body>
  <button id="myBtn">클릭하세요</button>

  <script>
    const myButton = document.getElementById('myBtn');
    // 이 시점에는 <button> 태그가 이미 로드되었습니다.
    myButton.addEventListener('click', function() {
      alert('버튼 클릭!');
    });
  </script>
</body>
</html>
```

#### 2. `DOMContentLoaded` 이벤트 리스너 사용하기

스크립트의 위치를 유지하면서도 DOM이 완전히 로드된 후에 코드를 실행하고 싶다면 `DOMContentLoaded` 이벤트를 사용할 수 있습니다. 이 방법은 코드를 논리적으로 구성하는 데 더 도움이 됩니다.

**해결된 코드:**
```html
<script>
  document.addEventListener('DOMContentLoaded', function() {
    // 이 코드는 DOM이 모두 로드된 후에 실행됩니다.
    const myButton = document.getElementById('myBtn');
    myButton.addEventListener('click', function() {
      alert('버튼 클릭!');
    });
  });
</script>
```

### 방어적인 코드 작성: 조건부 접근

오류를 방지하는 또 다른 좋은 습관은 객체가 `null`이 아닌지 확인한 후에 속성에 접근하는 것입니다. 이는 예기치 않은 상황에서 오류로 인해 전체 스크립트가 멈추는 것을 방지해줍니다.

**조건문 사용:**
```javascript
const myElement = document.getElementById('nonExistentElement');

if (myElement) { // myElement가 null이 아닐 경우에만 코드 실행
  myElement.style.color = 'red';
}
```

**Optional Chaining (`?.`) 사용:**

최신 JavaScript(ES2020)에서는 Optional Chaining 연산자 `?.`를 사용하여 코드를 더 간결하게 작성할 수 있습니다. `null`이나 `undefined`일 수 있는 객체의 속성에 안전하게 접근할 수 있게 해줍니다.

```javascript
const myElement = document.getElementById('nonExistentElement');

// myElement가 null이나 undefined가 아니면 style 속성에 접근, 그렇지 않으면 undefined를 반환
const color = myElement?.style?.color;
console.log(color); // undefined (오류 발생 안 함)
```

### 결론

`TypeError: Cannot read properties of null` 오류는 대부분 DOM 로딩 순서 문제로 발생합니다. 이 오류를 해결하려면:

1.  **스크립트 위치를 확인**하고 `<body>` 끝으로 옮기거나,
2.  **`DOMContentLoaded` 이벤트**를 사용하여 DOM이 준비된 후 코드를 실행하세요.
3.  **조건문**이나 **Optional Chaining (`?.`)**을 사용하여 항상 `null` 가능성을 염두에 둔 방어적인 코드를 작성하는 습관을 들이는 것이 좋습니다.
