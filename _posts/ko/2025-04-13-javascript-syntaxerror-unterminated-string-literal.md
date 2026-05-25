---
typora-root-url: ../
layout: single
title: >
    JavaScript SyntaxError: Unterminated string literal 해결 방법
date: 2025-04-13T07:17:00+09:00
seo_title: >
    JavaScript SyntaxError: Unterminated string literal 해결 방법

lang: ko
translation_id: javascript-syntaxerror-unterminated-string-literal
header:
   teaser: /images/header_images/overlay_image_js.png
   overlay_image: /images/header_images/overlay_image_js.png
   overlay_filter: 0.5
   image_description: >
     이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: JavaScript SyntaxError: Unterminated string literal 해결 방법
excerpt: >
    JavaScript에서 "SyntaxError: Unterminated string literal"은 문자열이 제대로 닫히지 않았을 때 발생하는 구문 오류입니다. 이 오류는 주로 따옴표나 줄 바꿈 문제로 인해 발생합니다. 이 글에서는 오류의 원인과 해결 방법을 알아봅니다.
seo_description: >
    JavaScript에서 "SyntaxError: Unterminated string literal"은 문자열이 제대로 닫히지 않았을 때 발생하는 구문 오류입니다. 이 오류는 주로 따옴표나 줄 바꿈 문제로 인해 발생합니다. 이 글에서는 오류의 원인과 해결 방법을 알아봅니다.
categories:
  - ko_Troubleshooting
tags:
  - JavaScript
  - SyntaxError
  - String
  - Error
---


![이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: JavaScript SyntaxError: Unterminated string literal 해결 방법](/images/header_images/overlay_image_js.png)
## 문제 상황

JavaScript 코드를 작성할 때 `SyntaxError: Unterminated string literal` (또는 일부 브라우저에서는 `Uncaught SyntaxError: Invalid or unexpected token`) 오류가 발생할 수 있습니다.
이 오류는 문자열 리터럴이 올바르게 종료되지 않았음을 의미합니다.
주로 문자열을 여는 따옴표는 있지만 닫는 따옴표가 없거나, 문자열 내에서 잘못된 문자가 사용될 때 발생합니다.

```javascript
// 잘못된 예시 1: 닫는 따옴표 누락
let message = 'Hello, world;

// 잘못된 예시 2: 문자열 내부에 줄 바꿈 포함
let htmlString = '<div>
    <p>Hello</p>
</div>';

console.log(message);
console.log(htmlString);
```

위 코드들은 모두 `SyntaxError`를 발생시킵니다.
첫 번째는 닫는 작은따옴표(`'`)가 없습니다.
두 번째는 일반 문자열 안에 직접 줄 바꿈을 포함하고 있습니다.

## 원인 분석

이 오류의 주요 원인은 다음과 같습니다.

1.  **따옴표 불일치 또는 누락**: 문자열을 시작한 따옴표와 닫는 따옴표가 맞지 않거나, 닫는 따옴표가 완전히 빠진 경우입니다.
2.  **일반 문자열 안의 직접 줄 바꿈**: 작은따옴표나 큰따옴표로 만든 일반 문자열은 줄 바꿈을 그대로 포함할 수 없습니다.
3.  **복사된 스마트 따옴표**: 문서나 채팅 도구에서 복사한 텍스트에 `“`, `’` 같은 문자가 섞이면 JavaScript 구분자로 동작하지 않습니다.
4.  **문자열 내부 따옴표 미이스케이프**: 문자열 안의 따옴표가 구분자로 해석되면 문자열이 중간에서 끝난 것으로 처리됩니다.

## 신뢰할 수 있는 해결 방법

문자열의 형태에 맞는 해결책을 선택해야 합니다. 끝에 따옴표 하나를 무조건 붙이는 방식은 위험합니다. 해당 문자열이 한 줄인지, 여러 줄인지, 데이터에서 생성되는 값인지 먼저 확인해야 합니다.

### 1. 같은 구분자로 문자열 닫기

```javascript
const message = 'Hello, world';
const title = "Today's report";
```

문자열을 여는 구분자와 닫는 구분자는 일치해야 합니다. 문자열 안에 작은따옴표가 들어간다면 큰따옴표가 더 읽기 쉬울 수 있습니다. 반대로 큰따옴표가 들어간다면 작은따옴표나 template literal을 검토할 수 있습니다.

### 2. 여러 줄 텍스트에는 Template Literal 사용

```javascript
const htmlString = `<div>
  <p>Hello</p>
</div>`;
```

Template literal은 backtick을 사용하며 줄 바꿈을 포함할 수 있습니다. HTML 조각, 여러 줄 메시지, 읽기 쉬운 텍스트 템플릿을 만들 때 유용합니다. 다만 사용자 입력을 끼워 넣는 경우에는 별도의 이스케이프나 sanitizing이 필요합니다. Template literal 자체가 안전한 HTML을 보장하지는 않습니다.

### 3. 문자열 내부 따옴표 이스케이프

```javascript
const sentence = 'It\\'s ready';
const label = "Click the \"Save\" button";
```

이스케이프는 문자열이 짧고 구분자 선택이 명확할 때 적합합니다. 이스케이프가 많아져 읽기 어렵다면 구분자를 바꾸거나 template literal을 사용하는 편이 유지보수에 좋습니다.

## 수정 확인 방법

전체 애플리케이션으로 돌아가기 전에 오류를 재현하는 가장 작은 파일을 먼저 실행합니다. Node.js에서는 `node file.js`로 확인할 수 있습니다. 브라우저에서는 DevTools의 Console에서 줄 번호를 확인합니다. Vite, Webpack, Next.js 같은 번들러가 있다면 보고된 줄이 원본 코드인지 생성된 출력인지도 확인해야 합니다. Source map 때문에 위치가 달라질 수 있으므로, 실제로 중요한 증거는 원본 코드의 해당 줄, 그 줄에서 사용한 구분자, 보고된 토큰 바로 앞 문자입니다.

## 예방 체크리스트

- 문자열이 닫히지 않았을 때 표시해 주는 편집기나 formatter를 사용합니다.
- 긴 HTML이나 메시지는 억지로 한 줄 문자열로 만들지 말고 template literal을 검토합니다.
- 문서 편집기에서 복사한 스마트 따옴표가 코드에 들어가지 않았는지 확인합니다.
- quote 문제를 배포 전에 잡을 수 있도록 lint 또는 formatter 단계를 둡니다.
- 디버깅할 때는 오류를 유지하는 가장 작은 문자열까지 코드를 줄입니다.

## 전문 보완 체크

**JavaScript SyntaxError: Unterminated string literal 해결 방법**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 브라우저 또는 Node 버전, 번들러 설정, 비동기 경계, DOM 또는 API 상태를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

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

독자가 **JavaScript SyntaxError: Unterminated string literal 해결 방법**의 첫 번째 권장 조치를 이미 시도했지만 결과가 여전히 불확실하다고 가정해 봅니다. 다음 단계는 여러 해결책을 한꺼번에 시험하는 것이 아니라 짧은 감사 기록을 만드는 것입니다. 먼저 어떤 판단을 하려는지 한 문장으로 쓰고, 환경을 한 문장으로 적고, 관찰된 결과를 한 문장으로 남깁니다. 그다음 브라우저 또는 Node 버전, 번들러 설정, 비동기 경계, DOM 또는 API 상태를 이미 확보한 사실과 대조합니다. 이렇게 해야 글이 서로 끊어진 팁 목록이 아니라 검증 가능한 절차가 됩니다.

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
