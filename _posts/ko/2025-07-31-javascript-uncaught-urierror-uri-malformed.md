---
typora-root-url: ../
layout: single
title: "JavaScript에서 Uncaught URIError: URI malformed 오류 해결 방법"

lang: ko
translation_id: javascript-uncaught-urierror-uri-malformed
excerpt: "URI 디코딩 함수를 사용하기 전에 문자열이 올바르게 형식화되었는지 확인하여 JavaScript의 'Uncaught URIError: URI malformed' 오류를 이해하고 해결합니다."
header:
   teaser: /images/header_images/overlay_image_js.png
   overlay_image: /images/header_images/overlay_image_js.png
   overlay_filter: 0.5
categories:
  - ko_Troubleshooting
tags:
  - JavaScript
  - URIError
  - URI
  - Decoding
  - Troubleshooting
---

## `Uncaught URIError: URI malformed`란 무엇인가?

`Uncaught URIError: URI malformed` 오류는 JavaScript에서 `decodeURI()` 또는 `decodeURIComponent()`와 같은 URI(Uniform Resource Identifier) 처리 함수를 유효하지 않은 URI 구성 요소인 문자열과 함께 사용할 때 발생한다.

이 함수들은 특정 형식을 기대하며, URI 사양을 따르지 않는 문자 시퀀스(예: 두 개의 16진수가 뒤따르지 않는 단독 '%' 기호)를 만나면 이 오류를 발생시킨다.

## 일반적인 원인

주된 원인은 부적절하게 인코딩되었거나 손상된 URI 문자열을 디코딩 함수에 전달하는 것이다.

1.  **잘못된 퍼센트 인코딩**: 흔한 실수는 문자열에 유효한 퍼센트 인코딩 시퀀스(예: 공백의 경우 `%20`)의 일부가 아닌 '%' 문자가 포함된 경우다. 예를 들어, `"https://example.com/path?query=100%"`와 같은 문자열은 후행 `%`가 유효한 이스케이프 시퀀스가 아니기 때문에 실패한다.

2.  **이미 디코딩된 문자열 디코딩**: 이미 디코딩된 문자열을 디코딩하려고 시도하면 문자열에 잘못된 URI 시퀀스처럼 보이는 문자가 자연스럽게 포함된 경우 이 오류가 발생할 수 있다.

3.  **수동 문자열 조작**: URI 문자열을 수동으로 잘못 구성하면 쉽게 오류가 발생할 수 있다.

## 해결 방법

핵심은 디코딩하는 문자열이 유효하고 인코딩된 URI 구성 요소인지 확인하는 것이다.

### 1. 입력 유효성 검사 및 삭제

URI를 디코딩하기 전에, 특히 외부 소스나 사용자 입력에서 온 경우 유효성을 검사해야 한다. 이 오류를 방지하는 가장 좋은 방법은 URI 구성 요소를 전송하거나 사용하기 전에 올바르게 인코딩하는 것이다.

전체 URI를 만들기 전에 문자열의 특수 문자를 인코딩하려면 `encodeURIComponent()`를 사용한다.

```javascript
// 잘못된 방법: 특수 문자로 쿼리 문자열을 수동으로 생성
const query = "search=this&that%"; // '%'가 오류를 유발함
const url = `https://example.com/search?${query}`;

// 올바른 방법: 구성 요소를 먼저 인코딩
const searchTerm = "this&that%";
const encodedSearchTerm = encodeURIComponent(searchTerm); // "this%26that%25"
const correctUrl = `https://example.com/search?query=${encodedSearchTerm}`;

console.log(correctUrl);
// "https://example.com/search?query=this%26that%25"
```

### 2. 정상적인 오류 처리를 위한 `try...catch` 사용

URI 문자열이 항상 유효하다고 보장할 수 없는 경우, 디코딩 함수를 `try...catch` 블록으로 감싼다. 이렇게 하면 애플리케이션이 충돌하지 않고 오류를 정상적으로 처리할 수 있다.

```javascript
function safelyDecodeURI(encodedString) {
  try {
    return decodeURIComponent(encodedString);
  } catch (e) {
    if (e instanceof URIError) {
      console.error("URI 구성 요소 디코딩 실패:", encodedString);
      // 대체 값 또는 원본 문자열 반환
      return encodedString;
    } else {
      // 다른 오류는 다시 던지기
      throw e;
    }
  }
}

// 사용 예시
const malformedURI = "https://example.com/data?value=100%";
const decoded = safelyDecodeURI(malformedURI);

console.log(decoded); // 오류를 기록하고 원본 문자열을 반환함
```

### 3. 일반적인 실수 확인

- **공백**: 공백이 `%20` 또는 `+`로 올바르게 인코딩되었는지 확인한다.
- **퍼센트 기호**: URI의 리터럴 퍼센트 기호(`%`)는 `%25`로 인코딩해야 한다.

잘못된 형식의 URI를 수정하는 방법의 예는 다음과 같다.

```javascript
// 잘못된 '%'가 있는 잘못된 형식의 URI
let uri = "https://api.example.com/items?category=electronics%";

// 디코딩을 시도하면 오류가 발생함
try {
  decodeURIComponent(uri);
} catch (e) {
  console.error(e); // URIError: URI malformed
}

// 해결 방법:
// 1. '%'가 오타였다면 제거한다.
let correctedUri = uri.slice(0, -1); // "https://api.example.com/items?category=electronics"
console.log(decodeURIComponent(correctedUri));

// 2. '%'가 의도적인 것이었다면 %25로 인코딩되었어야 한다.
let properlyEncodedUri = "https://api.example.com/items?category=electronics%25";
console.log(decodeURIComponent(properlyEncodedUri)); // "https://api.example.com/items?category=electronics%"
```

문자열이 디코딩 함수에 전달되기 전에 올바르게 인코딩되었는지 확인하고 안전을 위해 `try...catch` 블록을 사용하면 `URIError: URI malformed` 오류를 효과적으로 방지하고 관리할 수 있다.
