---
typora-root-url: ../
layout: single
title: >
    JavaScript TypeError: Reduce of empty array with no initial value 해결 방법
date: 2025-04-14T07:18:00+09:00
seo_title: >
    JavaScript TypeError: Reduce of empty array with no initial value 해결 방법

lang: ko
translation_id: javascript-typeerror-reduce-of-empty-array-with-no-initial-value
header:
   teaser: /images/header_images/overlay_image_js.png
   overlay_image: /images/header_images/overlay_image_js.png
   overlay_filter: 0.5
   image_description: >
     이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: JavaScript TypeError: Reduce of empty array with no initial value 해결 방법
excerpt: >
    JavaScript에서 "TypeError: Reduce of empty array with no initial value"는 초기값 없이 빈 배열에 대해 reduce() 메서드를 호출할 때 발생하는 오류입니다. 이 글에서는 이 오류의 원인을 분석하고 해결 방법을 알아봅니다.
seo_description: >
    JavaScript에서 "TypeError: Reduce of empty array with no initial value"는 초기값 없이 빈 배열에 대해 reduce() 메서드를 호출할 때 발생하는 오류입니다. 이 글에서는 이 오류의 원인을 분석하고 해결 방법을 알아봅니다.
categories:
  - ko_Troubleshooting
tags:
  - JavaScript
  - TypeError
  - reduce
  - Array
---


![이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: JavaScript TypeError: Reduce of empty array with no initial value 해결 방법](/images/header_images/overlay_image_js.png)
## 문제 상황

JavaScript에서 배열의 `reduce()` 메서드를 사용할 때 `TypeError: Reduce of empty array with no initial value` 오류가 발생할 수 있습니다.
이 오류는 이름 그대로, 초기값(initial value)이 제공되지 않은 상태에서 빈 배열에 `reduce()`를 호출하려고 할 때 발생합니다.

```javascript
const numbers = [];

// 초기값 없이 빈 배열에 reduce()를 호출하여 TypeError 발생
const sum = numbers.reduce((accumulator, currentValue) => accumulator + currentValue);

console.log(sum);
```

위 코드는 빈 배열 `numbers`에 `reduce()`를 적용하고 있습니다.
`reduce()` 메서드는 두 번째 인자로 초기값을 받을 수 있는데, 이 예제에서는 초기값이 생략되었습니다.
이 경우 `reduce()`는 배열의 첫 번째 요소를 초기값으로 사용하려고 하지만, 배열이 비어있어 첫 번째 요소가 없으므로 `TypeError`가 발생합니다.

## 원인 분석

`Array.prototype.reduce()` 메서드의 동작 방식 때문에 이 오류가 발생합니다.

`reduce()` 메서드의 구문은 다음과 같습니다.

```javascript
arr.reduce(callback(accumulator, currentValue[, index[, array]])[, initialValue])
```

-   `callback`: 각 요소에 대해 실행할 함수.
-   `initialValue` (선택 사항): `callback` 함수 최초 호출 시 `accumulator`에 할당될 값.

동작 흐름은 `initialValue`의 제공 여부에 따라 달라집니다.

1.  **`initialValue`가 제공된 경우**:
    -   `accumulator`는 `initialValue`로 초기화됩니다.
    -   `currentValue`는 배열의 첫 번째 요소부터 시작합니다.
    -   빈 배열에 호출해도 `initialValue`가 그대로 반환되므로 오류가 발생하지 않습니다.

2.  **`initialValue`가 제공되지 않은 경우**:
    -   `accumulator`는 배열의 **첫 번째 요소**로 초기화됩니다.
    -   `currentValue`는 배열의 **두 번째 요소**부터 시작합니다.
    -   만약 배열이 비어 있다면, `accumulator`로 사용할 첫 번째 요소가 없으므로 `TypeError`가 발생합니다.

결국, 오류의 근본 원인은 **초기값 없이 빈 배열에 대해 축소(reduction) 연산을 시도**했기 때문입니다.

## 해결 방법

### 1. `reduce()`에 초기값 제공

가장 간단하고 안전한 해결책은 `reduce()` 메서드에 항상 초기값을 제공하는 것입니다.
초기값은 연산의 종류에 따라 적절하게 선택해야 합니다.

-   숫자의 합을 구하는 경우: `0`
-   숫자의 곱을 구하는 경우: `1`
-   문자열을 연결하는 경우: `''` (빈 문자열)
-   객체를 만드는 경우: `{}` (빈 객체)

```javascript
const numbers = [];

// 초기값으로 0을 제공
const sum = numbers.reduce((accumulator, currentValue) => accumulator + currentValue, 0);

console.log(sum); // 0
```

이제 코드는 빈 배열에 대해서도 오류 없이 `0`을 올바르게 반환합니다.

### 2. 배열이 비어있는지 확인 후 `reduce()` 호출

상황에 따라 빈 배열을 다르게 처리해야 할 수도 있습니다.
이 경우, `reduce()`를 호출하기 전에 배열의 길이를 확인하여 분기 처리를 할 수 있습니다.

```javascript
const numbers = [];
let sum;

if (numbers.length > 0) {
    sum = numbers.reduce((accumulator, currentValue) => accumulator + currentValue);
} else {
    // 빈 배열일 때의 기본값 설정
    sum = 0; 
}

console.log(sum); // 0
```

이 방법은 코드가 조금 더 길어지지만, 로직을 명확하게 표현할 수 있습니다.

### 3. 기본값과 함께 단축 평가 사용 (ES6+)

조금 더 간결한 코드를 원한다면, `reduce`의 결과가 `undefined`나 `null`이 될 수 있는 경우 기본값을 설정하는 방식을 사용할 수 있습니다.
하지만 이 방법은 `reduce`가 오류를 던지는 근본적인 문제를 해결하지는 않으므로, 초기값을 제공하는 첫 번째 방법을 사용하는 것이 더 좋습니다.

```javascript
// 이 코드는 여전히 오류를 발생시키므로 좋은 예가 아님
// const sum = (numbers.length > 0 ? numbers.reduce(...) : 0);

// 항상 초기값을 제공하는 것이 가장 좋은 습관입니다.
const sumWithInitialValue = numbers.reduce((acc, val) => acc + val, 0);
```

## 결론

`TypeError: Reduce of empty array with no initial value`는 `reduce()` 메서드의 동작 방식을 이해하면 쉽게 해결할 수 있는 문제입니다.
가장 좋은 해결책이자 예방책은 **`reduce()`를 사용할 때 항상 적절한 초기값을 제공하는 것**입니다.
이는 코드를 더 예측 가능하고 안정적으로 만들어주며, 빈 배열과 같은 엣지 케이스를 자연스럽게 처리해줍니다.

## 전문 보완 체크

**JavaScript TypeError: Reduce of empty array with no initial value 해결 방법**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 브라우저 또는 Node 버전, 번들러 설정, 비동기 경계, DOM 또는 API 상태를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

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

## 함께 보면 좋은 글

같은 주제 흐름에서 이어서 읽기 좋은 글입니다.

- [SSL: CERTIFICATE_VERIFY_FAILED 오류 해결 방법 (Windows Python)](/ko_troubleshooting/python-certificate-verify-failed/)
- [Permission denied (publickey) 오류 해결 방법 (Windows Git SSH)](/ko_troubleshooting/git-permission-denied-publickey-windows/)
