---
typora-root-url: ../
layout: single
title: >
    자바스크립트 SyntaxError: missing ) after argument list 해결 방법
date: 2025-08-03T11:30:00+09:00
header:
   teaser: /images/header_images/overlay_image_js.png
   overlay_image: /images/header_images/overlay_image_js.png
   overlay_filter: 0.5
excerpt: >
    자바스크립트에서 함수를 호출할 때 인자 목록 뒤에 닫는 괄호 `)`를 빠뜨려 발생하는 `SyntaxError: missing ) after argument list` 오류의 원인과 해결책을 알아봅니다.
categories:
  - ko_Troubleshooting
tags:
  - JavaScript
  - SyntaxError
  - Function Call
---

## 문제 상황

`SyntaxError: missing ) after argument list`는 자바스크립트에서 함수를 호출할 때 발생하는 매우 흔한 구문 오류입니다. 이 오류의 의미는 이름 그대로, **함수 호출 시 인자(argument) 목록 뒤에 닫는 괄호 `)`가 빠졌다**는 뜻입니다.

자바스크립트 엔진이 코드를 파싱(해석)할 때, 함수 이름 뒤에 오는 여는 괄호 `(`를 만나면 함수 호출 구문으로 인식하고, 그에 맞는 닫는 괄호 `)`가 나올 때까지 인자 목록을 읽습니다. 만약 닫는 괄호가 제 위치에 없으면, 엔진은 구문이 올바르게 완성되지 않았다고 판단하여 이 오류를 발생시킵니다.

## 오류 발생 코드 예시

가장 대표적인 예시는 함수 호출 시 닫는 괄호를 잊어버리는 경우입니다.

```javascript
console.log("Hello, World!";
// SyntaxError: missing ) after argument list
```

위 코드에서 `console.log` 함수는 `"Hello, World!"`라는 인자를 받았지만, 닫는 괄호 `)` 없이 세미콜론 `;`이 바로 뒤따라왔기 때문에 오류가 발생합니다.

이 오류는 여러 함수 호출이 중첩되거나 코드가 복잡할 때 더 발견하기 어려울 수 있습니다.

```javascript
// alert 함수의 닫는 괄호가 없습니다.
alert(parseInt("123" ); 
// SyntaxError: missing ) after argument list
```

## 해결 방법

이 오류는 구문상의 문제이므로 해결 방법은 매우 간단합니다.

### 1. 닫는 괄호 `)` 추가하기

오류가 발생한 줄을 확인하고, 함수 호출 구문의 인자 목록 끝에 빠진 닫는 괄호 `)`를 추가해주는 것입니다.

```javascript
// 수정된 코드
console.log("Hello, World!");

alert(parseInt("123"));
```

### 2. 코드 편집기의 도움 받기

실수를 줄이기 위해 코드 편집기(예: VS Code)의 기능을 적극적으로 활용하는 것이 좋습니다.

-   **괄호 짝 맞추기(Bracket Matching):** 대부분의 편집기는 여는 괄호를 입력하면 자동으로 닫는 괄호를 추가해주거나, 커서가 있는 괄호의 짝을 시각적으로 강조 표시해줍니다. 이 기능을 통해 빠진 괄호를 쉽게 찾을 수 있습니다.
-   **린터(Linter) 사용:** ESLint와 같은 린팅 도구는 코드를 작성하는 동안 실시간으로 구문 오류를 감지하여 밑줄 등으로 표시해줍니다. 이를 통해 코드를 실행하기 전에 문제를 발견하고 수정할 수 있습니다.
-   **코드 포매터(Code Formatter):** Prettier와 같은 도구는 코드를 저장할 때마다 일관된 스타일로 자동 정렬해줍니다. 코드가 정렬되면서 구조가 명확해지므로, 괄호가 빠진 부분을 시각적으로 더 쉽게 인지할 수 있습니다.

## 결론

`SyntaxError: missing ) after argument list`는 간단한 부주의로 인해 발생하는 구문 오류입니다. 이 오류를 만나면 당황하지 말고 다음을 확인하세요.

-   오류가 발생한 코드 줄의 **함수 호출 구문**을 살펴봅니다.
-   **인자 목록 뒤에 닫는 괄호 `)`가 제대로 위치**하고 있는지 확인합니다.

대부분의 경우, 빠진 괄호 하나를 추가하는 것만으로 문제가 해결됩니다. 코드 편집기의 보조 기능을 활용하면 이러한 실수를 사전에 방지하는 데 큰 도움이 됩니다.
