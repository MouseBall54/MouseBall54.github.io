---
typora-root-url: ../
layout: single
title: "JavaScript \"ReferenceError: assignment to undeclared variable\" 오류 해결 방법"

date: 2025-02-14T07:49:00+09:00
lang: ko
translation_id: javascript-referenceerror-undeclared-variable
excerpt: "값을 할당하기 전에 `let`, `const` 또는 `var`로 변수를 올바르게 선언하여 JavaScript의 strict mode에서 발생하는 \"ReferenceError: assignment to undeclared variable\" 오류를 해결하세요."
seo_description: "값을 할당하기 전에 `let`, `const` 또는 `var`로 변수를 올바르게 선언하여 JavaScript의 strict mode에서 발생하는 \"ReferenceError: assignment to undeclared variable\" 오류를 해결하세요."
header:
   teaser: /images/header_images/overlay_image_js.png
   overlay_image: /images/header_images/overlay_image_js.png
   overlay_filter: 0.5
   image_description: >
     이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: JavaScript \"ReferenceError: assignment to undeclared variable\" 오류 해결 방법
categories:
  - ko_Troubleshooting
tags:
  - JavaScript
  - ReferenceError
  - Debugging
  - Strict Mode
---


![이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: JavaScript \"ReferenceError: assignment to undeclared variable\" 오류 해결 방법](/images/header_images/overlay_image_js.png)
## 서론

`ReferenceError: assignment to undeclared variable "..."`는 JavaScript의 **strict mode(엄격 모드)**에서만 발생하는 오류다. 이 오류는 아직 선언되지 않은 변수에 값을 할당하여 실수로 전역 변수를 생성하는 것을 방지하는 안전장치 역할을 한다. 이 가이드에서는 이 오류가 발생하는 이유와 해결 방법을 설명한다.

## Strict Mode란?

Strict mode는 JavaScript의 제한된 변형을 선택하는 방법이다. 일반적인 JavaScript 의미 체계에 몇 가지 변경 사항을 적용한다.
1.  일부 JavaScript의 조용한 오류를 제거하고 대신 오류를 발생시킨다.
2.  JavaScript 엔진이 최적화를 수행하기 어렵게 만드는 실수를 수정한다.
3.  ECMAScript의 향후 버전에 정의될 가능성이 있는 일부 구문을 금지한다.

파일 시작 부분에 `"use strict";`를 추가하여 전체 스크립트에 대해 strict mode를 활성화하거나, 함수 본문 시작 부분에 추가하여 특정 함수에 대해 활성화할 수 있다.

```javascript
// 전체 스크립트에 대해
"use strict";
// ... 당신의 코드 ...

// 특정 함수에 대해
function myStrictFunction() {
  "use strict";
  // ... 당신의 코드 ...
}
```

## 오류의 원인

Strict mode가 아닌 경우, `var`, `let` 또는 `const`로 선언되지 않은 변수에 값을 할당하면 JavaScript는 자동으로 새로운 전역 변수를 생성한다.

**비-Strict Mode 예시:**
```javascript
function createGlobal() {
  message = "Hello, world!"; // 선언 없음
}

createGlobal();
console.log(message); // 출력: "Hello, world!" ('message'라는 전역 변수가 생성됨)
```
이러한 동작은 변수가 실수로 전역 스코프에 생성되어 코드의 다른 부분과 충돌할 수 있으므로 추적하기 어려운 버그로 이어질 수 있다.

**Strict mode**에서는 이것이 허용되지 않는다. 선언되지 않은 변수에 값을 할당하면 `ReferenceError`가 발생한다.

**Strict Mode 예시:**
```javascript
"use strict";

function createGlobal() {
  message = "Hello, world!"; // 선언 없음
}

createGlobal(); 
// ReferenceError: assignment to undeclared variable "message" 오류 발생
```

## 해결 방법

해결책은 간단하며 좋은 코딩 습관을 장려한다: **변수를 사용하기 전에 항상 선언하라**.

JavaScript의 선언 키워드(`let`, `const` 또는 `var`) 중 하나를 사용하여 적절한 스코프 내에서 변수를 선언하면 된다.

### `let`을 사용한 해결책

변수의 값이 변경되어야 하는 경우 `let`을 사용한다.

```javascript
"use strict";

function assignValue() {
  let message; // 변수 선언
  message = "This is a valid assignment.";
  console.log(message);
}

assignValue();
```

### `const`를 사용한 해결책

변수의 값이 재할당되지 않을 경우 `const`를 사용한다. 이는 일반적으로 우발적인 재할당을 방지하는 데 선호된다.

```javascript
"use strict";

function assignConstant() {
  const greeting = "Hello!"; // 선언 및 할당
  console.log(greeting);
  // greeting = "Hi!"; // 이 코드는 TypeError를 발생시킨다
}

assignConstant();
```

### `var`를 사용한 해결책

`var`도 옵션이지만, `let`과 `const`는 함수 스코프가 아닌 블록 스코프(`{...}`)를 가지므로 다른 유형의 버그를 예방하는 데 도움이 되어 일반적으로 사용이 권장된다.

```javascript
"use strict";

function assignWithVar() {
  var count; // 변수 선언
  count = 100;
  console.log(count);
}

assignWithVar();
```

변수를 명시적으로 선언함으로써 코드를 더 명확하고 유지보수하기 쉽게 만들고 `ReferenceError: assignment to undeclared variable` 오류를 방지할 수 있다.

## 전문 보완 체크

**JavaScript \"ReferenceError: assignment to undeclared variable\" 오류 해결 방법**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 브라우저 또는 Node 버전, 번들러 설정, 비동기 경계, DOM 또는 API 상태를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

### 신뢰도를 높이는 증거

작업을 바꾸기 전에는 객관적인 증거를 먼저 확인해야 합니다. 쓸 만한 증거에는 콘솔 stack trace, `node --version`, Network 탭 출력, 최소 재현 예제가 포함됩니다. 증거가 서로 맞지 않으면 억지로 하나의 이야기로 합치지 말고 충돌 자체를 남겨야 합니다. 빠른 해결이 한 번 성공했더라도 같은 입력, 계정, 의존성, 기기 상태에서 다시 확인하지 않았다면 아직 확정된 해결책이라고 보기 어렵습니다.

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

## 적용 검토 시나리오

독자가 **JavaScript \"ReferenceError: assignment to undeclared variable\" 오류 해결 방법**의 첫 번째 권장 조치를 이미 시도했지만 결과가 여전히 불확실하다고 가정해 봅니다. 다음 단계는 여러 해결책을 한꺼번에 시험하는 것이 아니라 짧은 감사 기록을 만드는 것입니다. 먼저 어떤 판단을 하려는지 한 문장으로 쓰고, 환경을 한 문장으로 적고, 관찰된 결과를 한 문장으로 남깁니다. 그다음 브라우저 또는 Node 버전, 번들러 설정, 비동기 경계, DOM 또는 API 상태를 이미 확보한 사실과 대조합니다. 이렇게 해야 글이 서로 끊어진 팁 목록이 아니라 검증 가능한 절차가 됩니다.

### 감사 기록 양식

| 항목 | 예시 기준 | 이유 |
| --- | --- | --- |
| 관찰 | 조치 전 실제로 본 내용 | 기준 상태를 객관화합니다 |
| 증거 | 콘솔 stack trace, `node --version` | 판단을 기록에 연결합니다 |
| 가정 | 믿고 있지만 아직 증명하지 못한 내용 | 숨은 추정을 드러냅니다 |
| 조치 | 한 번에 하나의 변경 | 결과의 원인을 추적하게 합니다 |
| 중단 기준 | 멈추고 도움을 요청할 조건 | 반복적인 시행착오를 줄입니다 |

### 품질 경계

같은 결과가 통제된 재확인 뒤에도 반복될 때만 이 안내를 강한 결론으로 보아야 합니다. 계정, 기기, 데이터 샘플, 의존성 버전, 계약 조건, 공식 규칙이 달라졌다면 결론의 강도를 낮추고 가설로 다루는 편이 안전합니다. 검색 독자는 급한 문제를 안고 들어오는 경우가 많아 맥락을 건너뛰기 쉽습니다. 전문적인 글은 위험한 판단을 천천히 하게 만들면서도 다음 행동은 분명하게 제시해야 합니다.

## 함께 보면 좋은 글

같은 주제 흐름에서 이어서 읽기 좋은 글입니다.

- [SSL: CERTIFICATE_VERIFY_FAILED 오류 해결 방법 (Windows Python)](/ko_troubleshooting/python-certificate-verify-failed/)
- [Permission denied (publickey) 오류 해결 방법 (Windows Git SSH)](/ko_troubleshooting/git-permission-denied-publickey-windows/)
