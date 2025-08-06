---
typora-root-url: ../
layout: single
title: >
   JavaScript 프로미스: Promise.all vs. Promise.race

lang: ko
translation_id: javascript-promise-all-vs-promise-race
header:
   teaser: /images/header_images/overlay_image_js.png
   overlay_image: /images/header_images/overlay_image_js.png
   overlay_filter: 0.5
excerpt: >
   여러 비동기 작업을 처리하기 위한 JavaScript의 Promise.all과 Promise.race의 차이점을 알아보세요. 모든 프로미스가 완료될 때까지 기다려야 하는 경우와 가장 먼저 완료된 프로미스에 따라 행동해야 하는 경우를 이해하세요.
categories:
   - ko_Troubleshooting
tags:
   - JavaScript
   - Promises
   - async
   - Promise.all
   - Promise.race
---

## 서론

JavaScript 프로미스는 비동기 작업을 관리하는 데 필수적입니다. 종종 단일 프로미스로 작업하지만, 한 번에 여러 프로미스를 처리해야 하는 시나리오도 많습니다. `Promise` 객체는 이를 위해 `Promise.all()`과 `Promise.race()`라는 두 가지 주요 정적 메서드를 제공합니다.

이 둘의 차이점을 이해하는 것은 복잡한 비동기 워크플로우를 효율적으로 조율하는 데 매우 중요합니다. 이 가이드에서는 `Promise.all`과 `Promise.race`를 명확한 예제와 함께 비교하여 각각 언제 사용해야 하는지 보여줍니다.

## `Promise.all()` - "전부 아니면 전무" 방식

`Promise.all(iterable)`은 프로미스의 이터러블(배열 등)을 인자로 받아 단일 `Promise`를 반환합니다. 이 새로운 프로미스는 다음과 같이 동작합니다.

-   입력된 프로미스가 **모두** 이행(fulfill)될 때 **이행**됩니다. 이행 값은 입력 배열의 프로미스 순서와 동일한 순서로 모든 프로미스의 이행 값을 담은 배열입니다.
-   입력된 프로미스 중 **어느 하나라도** 거부(reject)되면 즉시 **거부**됩니다. 거부 이유는 가장 먼저 거부된 프로미스의 이유입니다.

그룹 과제라고 생각해보세요. 모든 구성원이 자신의 과제를 완료해야만 전체 그룹이 성공합니다. 한 명이라도 실패하면 전체 그룹 과제는 즉시 실패합니다.

### `Promise.all()` 사용 시점

서로 독립적인 여러 비동기 작업이 있고, 다음 단계로 진행하기 전에 모든 작업이 완료될 때까지 기다려야 할 때 `Promise.all()`을 사용합니다.

**일반적인 사용 사례:**
-   여러 API 엔드포인트에서 동시에 데이터 가져오기.
-   여러 파일 업로드하고 모든 업로드가 끝날 때까지 기다리기.
-   여러 데이터베이스 쿼리를 수행하고 결과 집계하기.

### 예제

프로필 페이지를 렌더링하기 전에 두 개의 다른 API에서 사용자 데이터와 게시물을 가져와야 한다고 상상해보세요.

```javascript
const promise1 = fetch('https://api.example.com/users/1').then(res => res.json());
const promise2 = fetch('https://api.example.com/posts/1').then(res => res.json());
const promise3 = new Promise(resolve => setTimeout(() => resolve("추가 정보"), 100));

Promise.all([promise1, promise2, promise3])
    .then(results => {
        const userData = results[0];
        const postData = results[1];
        const extraInfo = results[2];

        console.log("모든 프로미스가 이행되었습니다!");
        console.log("사용자:", userData);
        console.log("게시물:", postData);
        console.log("추가:", extraInfo);
        // 이제 페이지를 렌더링할 수 있습니다
    })
    .catch(error => {
        console.error("프로미스 중 하나가 거부되었습니다:", error);
        // 오류 처리 (예: 오류 메시지 표시)
    });
```

만약 `fetch` 호출 중 하나라도 실패하면 `.catch()` 블록이 즉시 실행됩니다.

## `Promise.race()` - "가장 먼저 끝나는" 방식

`Promise.race(iterable)`도 프로미스의 이터러블을 인자로 받아 단일 `Promise`를 반환합니다. 하지만 이 새로운 프로미스는 입력된 프로미스 중 **가장 먼저** 완료(settle, 즉 이행 또는 거부)되는 즉시 완료됩니다.

-   가장 먼저 완료된 프로미스가 이행되면 **이행**됩니다. 이행 값은 그 첫 번째로 이행된 프로미스의 값입니다.
-   가장 먼저 완료된 프로미스가 거부되면 **거부**됩니다. 거부 이유는 그 첫 번째로 거부된 프로미스의 이유입니다.

경주라고 생각해보세요. 오직 승자에게만 관심이 있습니다. 한 주자가 결승선을 통과하는 즉시 경주는 끝나고 결과를 얻게 됩니다.

### `Promise.race()` 사용 시점

동일한 정보에 대한 여러 소스가 있거나 타임아웃을 구현하고 싶을 때 `Promise.race()`를 사용합니다.

**일반적인 사용 사례:**
-   여러 중복 서버에 리소스를 요청하고 가장 빠른 응답을 사용하기.
-   비동기 작업에 대한 타임아웃 설정하기.

### 예제

네트워크 요청에 대한 타임아웃을 구현해 보겠습니다. `fetch` 작업을 위한 프로미스 하나와 특정 시간 후에 거부되는 또 다른 프로미스를 만듭니다. 그런 다음 이 둘을 경쟁시킵니다.

```javascript
function fetchWithTimeout(url, timeout) {
    const fetchPromise = fetch(url);

    const timeoutPromise = new Promise((_, reject) => {
        setTimeout(() => {
            reject(new Error(`${timeout}ms 후 요청 시간 초과`));
        }, timeout);
    });

    return Promise.race([fetchPromise, timeoutPromise]);
}

fetchWithTimeout('https://api.example.com/slow-resource', 5000)
    .then(response => response.json())
    .then(data => {
        console.log("데이터 수신:", data);
    })
    .catch(error => {
        console.error("오류:", error.message);
        // fetch가 너무 오래 걸리면 "5000ms 후 요청 시간 초과"가 기록됩니다
    });
```
만약 `fetch` 호출이 5초 이상 걸리면 `timeoutPromise`가 먼저 거부되어 `Promise.race`가 거부됩니다.

## 요약 표

| 기능 | `Promise.all()` | `Promise.race()` |
| --- | --- | --- |
| **이행 시점** | **모든** 프로미스가 이행될 때. | **첫 번째** 프로미스가 이행될 때. |
| **거부 시점** | **어느 하나라도** 프로미스가 거부될 때. | **첫 번째** 프로미스가 거부될 때. |
| **이행 값** | 모든 이행 값의 배열. | 첫 번째로 이행된 프로미스의 이행 값. |
| **사용 사례** | 여러 프로미스의 결과 집계. | 가장 빠른 프로미스의 결과 얻기 또는 타임아웃. |

## 결론

`Promise.all()`과 `Promise.race()`는 여러 비동기 작업을 관리하는 강력한 도구이지만, 매우 다른 목적을 가집니다.

-   **`Promise.all()`**은 계속 진행하기 전에 모든 것이 성공해야 할 때 사용합니다.
-   **`Promise.race()`**는 가장 먼저 완료된 프로미스의 결과만 필요할 때 사용합니다.

시나리오에 맞는 올바른 메서드를 선택함으로써 더 깨끗하고 선언적이며 효율적인 비동기 JavaScript 코드를 작성할 수 있습니다.
