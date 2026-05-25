---
typora-root-url: ../
layout: single
title: >
   JavaScript async/await 오류 처리 마스터하기

date: 2025-04-08T07:12:00+09:00
lang: ko
translation_id: javascript-async-await-error-handling
header:
   teaser: /images/header_images/overlay_image_js.png
   overlay_image: /images/header_images/overlay_image_js.png
   overlay_filter: 0.5
   image_description: >
     이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: JavaScript async/await 오류 처리 마스터하기
excerpt: >
   JavaScript에서 try...catch 블록을 사용하여 async/await 함수의 오류를 올바르게 처리하는 방법을 배우세요. 처리되지 않은 프로미스 거부를 피하고, 견고하고 신뢰할 수 있는 비동기 코드를 작성하세요.
seo_description: >
   JavaScript에서 try...catch 블록을 사용하여 async/await 함수의 오류를 올바르게 처리하는 방법을 배우세요. 처리되지 않은 프로미스 거부를 피하고, 견고하고 신뢰할 수 있는 비동기 코드를 작성하세요.
categories:
   - ko_Troubleshooting
tags:
   - JavaScript
   - async/await
   - Promises
   - Error Handling
   - try...catch
---


![이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: JavaScript async/await 오류 처리 마스터하기](/images/header_images/overlay_image_js.png)
## 서론

ES2017에 도입된 `async/await`는 JavaScript에서 프로미스를 다루는 훨씬 깨끗하고 가독성 좋은 구문을 제공합니다. 이를 통해 동기식 코드처럼 보이고 동작하는 비동기 코드를 작성할 수 있습니다. 하지만 개발자들이 어려움을 겪을 수 있는 한 가지 영역은 오류 처리입니다. 프로미스 체인에서 `.catch()`를 잊어버리면 조용한 실패나 처리되지 않은 프로미스 거부로 이어질 수 있습니다.

이 가이드에서는 `async/await` 함수에서 오류를 처리하는 표준적이고 가장 효과적인 방법인 `try...catch` 블록을 보여줍니다.

## `async/await`에서 오류 처리가 중요한 이유

프로미스를 `await`할 때 다음 두 가지 중 하나가 발생할 수 있습니다.
1.  프로미스가 **이행(fulfill)**되고, `await` 표현식은 이행된 값을 반환합니다.
2.  프로미스가 **거부(reject)**되고, `await` 표현식은 오류를 발생시킵니다. 이것이 핵심 부분입니다.

프로미스 거부가 잡히지 않으면 "처리되지 않은 프로미스 거부(unhandled promise rejection)"가 되어 Node.js 애플리케이션을 중단시키거나 브라우저에서 조용하고 디버깅하기 어려운 실패로 이어질 수 있습니다.

**잘못된 코드 (오류 처리 없음):**
```javascript
async function fetchUserData() {
    // 이 fetch가 실패하면 오류가 처리되지 않습니다!
    const response = await fetch('https://api.example.com/non-existent-user');
    const data = await response.json();
    console.log(data);
}

fetchUserData(); // "Uncaught (in promise) TypeError"를 유발할 수 있습니다
```
위 코드에서 `fetch` 프로미스가 거부되면(예: 404 오류 또는 네트워크 실패로 인해) 전체 프로그램이 잡히지 않은 오류로 중단될 수 있습니다.

## `try...catch` 해결책

`try...catch` 문은 동기식 JavaScript에서 오류 처리의 초석이며, `async/await`와 완벽하게 작동합니다.

"위험한" 비동기 코드(`await` 호출)를 `try` 블록으로 감쌉니다. 대기 중인 프로미스 중 하나라도 거부되면 코드 실행은 즉시 `catch` 블록으로 이동하여 오류를 정상적으로 처리할 수 있습니다.

**올바른 코드 (`try...catch` 사용):**
```javascript
async function fetchUserData() {
    try {
        console.log("사용자 데이터 가져오는 중...");
        const response = await fetch('https://api.example.com/non-existent-user');

        // 404 또는 500과 같은 HTTP 오류 확인
        if (!response.ok) {
            throw new Error(`HTTP 오류! 상태: ${response.status}`);
        }

        const data = await response.json();
        console.log("데이터 수신:", data);
        return data;
    } catch (error) {
        console.error("사용자 데이터를 가져오는 데 실패했습니다:", error.message);
        // 사용자에게 메시지를 표시하거나 오류를 기록하는 등의 작업을 수행할 수 있습니다.
        return null; // 대체 값 반환
    }
}

fetchUserData();
```

### 작동 방식:
1.  `try` 블록 안의 코드가 실행됩니다.
2.  `fetch()`가 거부되거나, 수동으로 새 오류를 `throw`하면(예: 잘못된 HTTP 상태), 제어가 `catch (error)` 블록으로 전달됩니다.
3.  `error` 객체에는 무엇이 잘못되었는지에 대한 정보가 포함됩니다.
4.  `catch` 블록은 실패를 처리하여 애플리케이션이 중단되는 것을 방지합니다.

## 여러 `await` 호출 처리

단일 `try...catch` 블록은 여러 `await` 표현식의 실패를 처리할 수 있습니다. 거부되는 첫 번째 표현식은 실행을 `catch` 블록으로 이동시키고, `try` 블록의 후속 라인은 실행되지 않습니다.

```javascript
async function fetchUserAndPosts(userId) {
    try {
        const userResponse = await fetch(`https://api.example.com/users/${userId}`);
        if (!userResponse.ok) throw new Error("사용자 정보를 가져오는 데 실패했습니다");
        const userData = await userResponse.json();

        // 첫 번째 fetch가 실패하면 이 줄은 절대 도달하지 않습니다
        const postsResponse = await fetch(`https://api.example.com/posts?userId=${userId}`);
        if (!postsResponse.ok) throw new Error("게시물을 가져오는 데 실패했습니다");
        const postsData = await postsResponse.json();

        return { user: userData, posts: postsData };
    } catch (error) {
        console.error("오류가 발생했습니다:", error.message);
        return null;
    }
}
```

## 대안: `.catch()` 사용

`try...catch`가 가장 일반적인 패턴이지만, `async` 함수 호출에 `.catch()`를 연결하여 오류를 처리할 수도 있습니다. 이는 호출하는 코드가 오류 처리를 책임지게 하려는 경우에 유용합니다.

먼저, `async` 함수는 내부에서 `try...catch`를 사용하지 않음으로써 오류가 전파되도록 작성됩니다.

```javascript
async function getUser(userId) {
    // 여기에는 try...catch가 없습니다. 오류가 발생합니다.
    const response = await fetch(`https://api.example.com/users/${userId}`);
    if (!response.ok) {
        throw new Error(`사용자를 찾을 수 없음: ${response.status}`);
    }
    return response.json();
}
```

그런 다음 호출자가 오류를 처리합니다.

```javascript
console.log("사용자 정보를 가져오는 중...");

getUser('invalid-user-id')
    .then(user => {
        console.log("사용자 찾음:", user);
    })
    .catch(error => {
        console.error("호출자에서 오류 발생:", error.message);
        // 여기서 오류 처리
    });

console.log("요청이 시작되었습니다.");
```

이 접근 방식은 오류 처리 로직이 함수가 호출되는 위치에 따라 변경될 수 있는 재사용 가능한 비동기 함수를 만드는 데 유용합니다.

## 결론

견고한 애플리케이션을 구축하려면 적절한 오류 처리는 타협할 수 없는 부분입니다. `async/await`를 사용하면 `try...catch` 블록이 주요 도구입니다. 이는 프로미스 거부 및 기타 예외를 관리하는 깨끗하고 동기식처럼 보이는 방법을 제공합니다.

**핵심 요약:**
-   잠재적인 프로미스 거부를 처리하려면 항상 `await` 호출을 `try...catch` 블록으로 감싸세요.
-   `async` 함수에서 거부된 프로미스는 잡을 수 있는 오류를 발생시킵니다.
-   기본적으로 프로미스 거부를 유발하지 않는 HTTP 오류(예: 404)를 처리하려면 `fetch` 호출에 대해 `response.ok`를 확인하세요.
-   또는 `async` 함수 호출 자체에 `.catch()`를 사용하여 오류 처리를 호출자에게 위임하세요.

`async/await`와 함께 `try...catch`를 마스터하면 깨끗하고 가독성 좋을 뿐만 아니라 탄력 있고 신뢰할 수 있는 비동기 코드를 작성할 수 있습니다.

## 전문 보완 체크

**JavaScript async/await 오류 처리 마스터하기**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 실행 환경, 정확한 오류 경계, 최소 재현 예제, 되돌릴 수 있는 경로를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

### 신뢰도를 높이는 증거

작업을 바꾸기 전에는 객관적인 증거를 먼저 확인해야 합니다. 쓸 만한 증거에는 전체 명령 출력, 버전 번호, 변경된 파일, 기대 동작과 실제 동작가 포함됩니다. 증거가 서로 맞지 않으면 억지로 하나의 이야기로 합치지 말고 충돌 자체를 남겨야 합니다. 빠른 해결이 한 번 성공했더라도 같은 입력, 계정, 의존성, 기기 상태에서 다시 확인하지 않았다면 아직 확정된 해결책이라고 보기 어렵습니다.

### 검토 표

| 검토 항목 | 확인할 내용 | 중요한 이유 |
| --- | --- | --- |
| 범위 | 이 글이 다루는 정확한 사례 | 조언을 과도하게 적용하지 않게 합니다 |
| 기준 상태 | 변경 전 상태 | 되돌리기와 비교를 가능하게 합니다 |
| 변경 | 실제로 수행한 가장 작은 조치 | 숨은 부작용을 줄입니다 |
| 결과 | 변경 뒤 관찰한 출력 또는 반응 | 기대와 증거를 구분합니다 |
| 재확인 | 결론을 다시 볼 시점 | 글의 정확도를 유지합니다 |

### 예외 상황과 실패 모드

주요 위험은 증상만 고치고 원인을 남기는 상황, 서로 무관한 변경을 같은 테스트에 섞는 상황입니다. 생산 데이터, 개인정보, 돈, 건강, 법적 권리, 보안 복구가 관련되어 있다면 넓은 해결책을 바로 적용하기보다 먼저 증거를 모으는 보수적인 접근이 낫습니다. 같은 제목의 문제라도 환경이 다르면 원인이 달라질 수 있으므로, 독자는 명령이나 결정을 복사하기 전에 자신의 조건이 글의 가정과 맞는지 비교해야 합니다.

### 유지보수 기준

이 안내는 의존성, 운영체제, 빌드 도구가 바뀐 뒤 다시 확인해야 합니다. 좋은 업데이트는 글 전체를 다시 쓰는 것이 아니라 예시, 링크, 명령, 화면, 판단 기준이 현재 동작과 여전히 맞는지 확인하는 일입니다. 기존 결론이 유효하면 확인 날짜를 남기고, 바뀌었다면 무엇이 바뀌었고 왜 이전 조언만으로 부족한지 설명해야 합니다.

### 실행 전 질문

- 문제나 판단이 실제임을 보여 주는 가장 작은 관찰 신호는 무엇인가?
- 공식 출처는 무엇이고, 내부 판단은 어느 부분인가?
- 변경 전에 반드시 캡처해야 할 기록은 무엇인가?
- 어떤 결과가 나오면 이 글의 조언이 맞지 않는다고 볼 것인가?
- 같은 문제가 반복될 때 누가 이 기록을 다시 봐야 하는가?

## 함께 보면 좋은 글

같은 주제 흐름에서 이어서 읽기 좋은 글입니다.

- [SSL: CERTIFICATE_VERIFY_FAILED 오류 해결 방법 (Windows Python)](/ko_troubleshooting/python-certificate-verify-failed/)
- [Permission denied (publickey) 오류 해결 방법 (Windows Git SSH)](/ko_troubleshooting/git-permission-denied-publickey-windows/)
