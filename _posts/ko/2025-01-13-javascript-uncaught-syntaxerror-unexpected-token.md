---
typora-root-url: ../
layout: single
title: "JavaScript 오류 'Uncaught SyntaxError: Unexpected token' 해결 방법"

date: 2025-01-13T07:17:00+09:00
lang: ko
translation_id: javascript-uncaught-syntaxerror-unexpected-token
excerpt: "'Uncaught SyntaxError: Unexpected token'은 JavaScript 엔진이 문법적으로 예상치 못한 토큰을 만났을 때 발생하는 구문 오류입니다. 이 오류의 일반적인 원인과 해결책을 알아봅니다."
seo_description: "'Uncaught SyntaxError: Unexpected token'은 JavaScript 엔진이 문법적으로 예상치 못한 토큰을 만났을 때 발생하는 구문 오류입니다. 이 오류의 일반적인 원인과 해결책을 알아봅니다."
header:
   teaser: /images/header_images/overlay_image_js.png
   overlay_image: /images/header_images/overlay_image_js.png
   overlay_filter: 0.5
   image_description: >
     이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: JavaScript 오류 'Uncaught SyntaxError: Unexpected token' 해결 방법
categories:
  - ko_Troubleshooting
tags:
  - JavaScript
  - SyntaxError
  - Troubleshooting
  - Debugging
---


![이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: JavaScript 오류 'Uncaught SyntaxError: Unexpected token' 해결 방법](/images/header_images/overlay_image_js.png)
## 'Uncaught SyntaxError: Unexpected token' 오류란?

`Uncaught SyntaxError: Unexpected token`은 JavaScript 코드가 언어의 문법 규칙을 따르지 않을 때 발생하는 가장 일반적인 구문 오류 중 하나다.
JavaScript 엔진이 코드를 파싱(해석)하는 과정에서 문법적으로 올바르지 않은, 예상치 못한 문자나 키워드(토큰)를 만나면 이 오류를 발생시킨다.
오류 메시지는 보통 `Unexpected token 'X'`와 같은 형태로 나타나며, 여기서 `'X'`는 문제가 된 특정 문자나 토큰을 가리킨다.

## 주요 원인

이 오류는 다양한 문법적 실수로 인해 발생할 수 있다.

### 1. 괄호, 중괄호, 대괄호의 불일치

열린 괄호가 제대로 닫히지 않았거나, 짝이 맞지 않는 경우에 발생한다.

```javascript
// 닫는 소괄호 '}'가 아닌 ')'여야 함
if (condition) {
    console.log("Hello, World!";
}
// Uncaught SyntaxError: Unexpected token '}'
```

### 2. 잘못된 연산자 사용

객체 리터럴에서 `=`를 사용하거나, 쉼표가 누락되는 등 잘못된 연산자 사용이 원인이 될 수 있다.

```javascript
let myObject = {
    key1: "value1",
    key2 = "value2" // '='가 아닌 ':'를 사용해야 함
};
// Uncaught SyntaxError: Unexpected token '='
```

### 3. 예약어의 잘못된 사용

`let`, `const`, `class` 같은 예약어를 변수 이름으로 사용하려고 할 때 발생한다.

```javascript
let let = 5; // 'let'은 예약어이므로 변수명으로 사용할 수 없음
// Uncaught SyntaxError: Unexpected token 'let'
```

### 4. JSON 데이터 파싱 오류

`JSON.parse()`를 사용할 때, 전달된 문자열이 유효한 JSON 형식이 아닐 경우 이 오류가 발생할 수 있다.
예를 들어, JSON 문자열 내의 키를 큰따옴표로 감싸지 않았거나, 마지막 속성 뒤에 쉼표가 붙어 있는 경우가 해당된다.

```javascript
// 마지막 속성 뒤에 쉼표(trailing comma)가 있어 오류 발생
let jsonString = '{"name": "John", "age": 30,}';
JSON.parse(jsonString);
// Uncaught SyntaxError: Unexpected token '}' in JSON at position ...
```

## 해결 방법

### 1. 코드 편집기 및 Linter 활용

대부분의 최신 코드 편집기(VS Code, WebStorm 등)는 실시간으로 구문 오류를 감지하고 강조 표시해준다.
또한 ESLint와 같은 Linter 도구를 사용하면 코드를 실행하기 전에 잠재적인 구문 오류를 미리 찾아낼 수 있어 매우 유용하다.

### 2. 괄호 및 따옴표 짝 맞추기

오류가 발생한 줄 주변의 모든 괄호(`()`, `{}`, `[]`)와 따옴표(`'`, `"`, `` ` ``)가 올바르게 짝을 이루고 닫혔는지 확인한다.
코드 편집기의 괄호 짝 맞춤 기능을 활용하면 쉽게 찾을 수 있다.

### 3. 문법 규칙 재확인

오류 메시지에 나타난 `Unexpected token`이 무엇인지 확인하고, 해당 부분의 JavaScript 문법이 올바른지 다시 한번 확인한다.
예를 들어, 객체 속성은 콜론(`:`)으로 정의하고, 배열 요소와 객체 속성은 쉼표(`,`)로 구분하는 등의 기본 규칙을 점검한다.

### 4. JSON 유효성 검사

`JSON.parse()` 관련 오류라면, 파싱하려는 문자열이 유효한 JSON 형식인지 검사해야 한다.
온라인 JSON 검증 도구(JSONLint 등)를 사용하거나, JSON의 규칙(키는 항상 큰따옴표, 마지막 요소 뒤 쉼표 없음 등)을 다시 확인한다.

## 결론

`Uncaught SyntaxError: Unexpected token`은 코드에 문법적 실수가 있음을 알려주는 명확한 신호다.
오류 메시지가 가리키는 위치와 예상치 못한 토큰이 무엇인지 주의 깊게 살펴보는 것이 문제 해결의 첫걸음이다.
코드 편집기의 구문 강조 기능과 Linter를 적극적으로 활용하면 이러한 종류의 오류를 사전에 예방하고 빠르게 수정하는 데 큰 도움이 된다.

## 전문 보완 체크

**JavaScript 오류 'Uncaught SyntaxError: Unexpected token' 해결 방법**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 브라우저 또는 Node 버전, 번들러 설정, 비동기 경계, DOM 또는 API 상태를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

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

독자가 **JavaScript 오류 'Uncaught SyntaxError: Unexpected token' 해결 방법**의 첫 번째 권장 조치를 이미 시도했지만 결과가 여전히 불확실하다고 가정해 봅니다. 다음 단계는 여러 해결책을 한꺼번에 시험하는 것이 아니라 짧은 감사 기록을 만드는 것입니다. 먼저 어떤 판단을 하려는지 한 문장으로 쓰고, 환경을 한 문장으로 적고, 관찰된 결과를 한 문장으로 남깁니다. 그다음 브라우저 또는 Node 버전, 번들러 설정, 비동기 경계, DOM 또는 API 상태를 이미 확보한 사실과 대조합니다. 이렇게 해야 글이 서로 끊어진 팁 목록이 아니라 검증 가능한 절차가 됩니다.

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
