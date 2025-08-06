---
typora-root-url: ../
layout: single
title: >
    자바스크립트 Uncaught (in promise) 오류 해결 방법

lang: ko
translation_id: javascript-uncaught-in-promise
header:
   teaser: /images/header_images/overlay_image_js.png
   overlay_image: /images/header_images/overlay_image_js.png
   overlay_filter: 0.5
excerpt: >
    자바스크립트에서 프로미스(Promise) 체인에서 발생한 예외가 처리되지 않았을 때 나타나는 `Uncaught (in promise)` 오류의 원인과 해결 방법을 알아봅니다.
categories:
  - ko_Troubleshooting
tags:
  - JavaScript
  - Promise
  - async/await
  - Error Handling
---

## 문제 상황

자바스크립트에서 비동기 작업을 처리하기 위해 프로미스(Promise)를 사용할 때, 콘솔에 `Uncaught (in promise)`라는 오류가 나타나는 경우가 있습니다. 이 오류는 프로미스가 `rejected` (거부) 상태가 되었지만, 이를 처리할 `.catch()` 블록이나 `try...catch` 구문이 없다는 것을 의미합니다.

비동기 작업(예: API 요청, 파일 읽기)은 성공할 수도 있지만 실패할 수도 있습니다. 프로미스는 이러한 실패 상황을 `rejected` 상태로 관리하며, 개발자는 이 상태를 반드시 처리해야 합니다. 그렇지 않으면 애플리케이션에서 예기치 않은 동작이 발생할 수 있습니다.

## 오류 발생 코드 예시

다음은 `fetch` API를 사용하여 존재하지 않는 URL에 요청을 보내는 예시입니다. 네트워크 오류 등으로 인해 프로미스가 거부되지만, 이를 처리하는 코드가 없습니다.

```javascript
// 존재하지 않는 API에 요청을 보냅니다.
fetch('https://api.example.com/non-existent-endpoint')
  .then(response => {
    if (!response.ok) {
      // response.ok가 false일 때 직접 에러를 발생시켜야 .catch()에서 잡을 수 있습니다.
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    console.log(data);
  });

// .catch() 블록이 없으므로 위에서 발생한 Error는 처리되지 않습니다.
// 결과: Uncaught (in promise) Error: Network response was not ok
```

## 해결 방법

프로미스에서 발생한 오류를 처리하는 방법은 크게 두 가지입니다.

### 1. `.catch()` 메서드 추가하기

가장 일반적인 방법은 프로미스 체인 마지막에 `.catch()` 메서드를 추가하는 것입니다. 체인 내의 어떤 `.then()` 블록에서든 오류가 발생하면, 실행 흐름은 즉시 가장 가까운 `.catch()` 블록으로 이동합니다.

```javascript
fetch('https://api.example.com/non-existent-endpoint')
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    console.log(data);
  })
  .catch(error => {
    console.error('Fetch 작업에 문제가 발생했습니다:', error);
    // 여기서 사용자에게 오류 메시지를 보여주는 등의 후속 처리를 할 수 있습니다.
  });
```

이렇게 하면 프로미스가 거부되더라도 오류가 `catch` 블록에서 처리되므로 `Uncaught (in promise)` 메시지가 나타나지 않습니다.

### 2. `try...catch`와 `async/await` 사용하기

`async/await` 문법을 사용하면 동기 코드처럼 비동기 코드를 작성할 수 있어 가독성이 향상됩니다. `async` 함수 내에서는 `try...catch` 구문을 사용하여 프로미스 오류를 처리할 수 있습니다.

```javascript
async function fetchData() {
  try {
    const response = await fetch('https://api.example.com/non-existent-endpoint');
    
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error('Fetch 작업에 문제가 발생했습니다:', error);
  }
}

fetchData();
```

`await` 키워드는 프로미스가 완료될 때까지 기다립니다. 만약 프로미스가 거부되면, `try...catch` 구문의 `catch` 블록이 해당 오류를 잡아냅니다.

## 결론

`Uncaught (in promise)` 오류는 처리되지 않은 프로미스 거부가 있음을 알려주는 중요한 신호입니다. 모든 비동기 작업은 실패 가능성을 내포하고 있으므로, 항상 오류 처리 코드를 작성하는 습관을 들여야 합니다.

-   프로미스 체인을 사용할 때는 마지막에 **`.catch()`**를 붙여 오류를 처리하세요.
-   `async/await`를 사용할 때는 **`try...catch`** 구문으로 코드를 감싸서 오류를 처리하세요.

안정적인 애플리케이션을 만들기 위해 비동기 오류 처리는 선택이 아닌 필수입니다.
