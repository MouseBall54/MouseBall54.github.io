---
typora-root-url: ../
layout: single
title: >
   JavaScript 변수: var, let, const의 차이점

date: 2025-04-15T07:19:00+09:00
lang: ko
translation_id: javascript-variables-var-vs-let-vs-const
header:
   teaser: /images/header_images/overlay_image_js.png
   overlay_image: /images/header_images/overlay_image_js.png
   overlay_filter: 0.5
   image_description: >
     이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: JavaScript 변수: var, let, const의 차이점
excerpt: >
   JavaScript에서 var, let, const의 차이점을 깊이 알아보세요. 스코프, 호이스팅, 재할당 규칙을 이해하여 더 깨끗하고 예측 가능하며 현대적인 JS 코드를 작성하세요.
seo_description: >
   JavaScript에서 var, let, const의 차이점을 깊이 알아보세요. 스코프, 호이스팅, 재할당 규칙을 이해하여 더 깨끗하고 예측 가능하며 현대적인 JS 코드를 작성하세요.
categories:
   - ko_Troubleshooting
tags:
   - JavaScript
   - ES6
   - var
   - let
   - const
---


![이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: JavaScript 변수: var, let, const의 차이점](/images/header_images/overlay_image_js.png)
## 서론

오랫동안 `var`는 JavaScript에서 변수를 선언하는 유일한 방법이었습니다. ES6(ECMAScript 2015)가 도입되면서, 변수 스코프와 동작에 대한 더 많은 제어를 제공하는 `let`과 `const`라는 두 개의 새로운 키워드가 추가되었습니다. 이 세 가지의 차이점을 이해하는 것은 현대적이고 유지 관리하기 쉬우며 버그 없는 JavaScript를 작성하는 데 매우 중요합니다.

이 가이드에서는 스코프, 호이스팅, 재할당 규칙을 기준으로 `var`, `let`, `const`를 비교합니다.

## 1. 스코프 (Scope)

스코프는 코드에서 변수에 접근할 수 있는 위치를 결정합니다.

### `var`: 함수 스코프

`var`로 선언된 변수는 **함수 스코프(function-scoped)**를 가집니다. 이는 선언된 함수 내에서만 접근할 수 있음을 의미합니다. 함수 외부에서 선언되면 전역 스코프를 가집니다.

```javascript
function myFunction() {
    if (true) {
        var myVar = "var로부터의 인사";
    }
    console.log(myVar); // "var로부터의 인사" - 여기서 접근 가능
}
myFunction();
// console.log(myVar); // ReferenceError: myVar is not defined - 여기서 접근 불가
```
`myVar`가 `if` 블록 밖에서도 접근 가능하다는 점에 유의하세요. 이는 `var`가 블록 스코프(`{...}`)를 존중하지 않기 때문이며, 예기치 않은 동작으로 이어질 수 있습니다.

### `let`과 `const`: 블록 스코프

`let`과 `const`로 선언된 변수는 **블록 스코프(block-scoped)**를 가집니다. 이들은 정의된 블록(즉, 중괄호 `{...}` 내부) 내에서만 접근할 수 있습니다.

```javascript
function anotherFunction() {
    if (true) {
        let myLet = "let으로부터의 인사";
        const myConst = "const로부터의 인사";
        console.log(myLet);   // 접근 가능
        console.log(myConst); // 접근 가능
    }
    // console.log(myLet);   // ReferenceError: myLet is not defined
    // console.log(myConst); // ReferenceError: myConst is not defined
}
anotherFunction();
```
이것은 훨씬 더 직관적이며 다른 많은 프로그래밍 언어에서 변수가 작동하는 방식과 유사합니다. 변수의 생명주기를 필요한 블록으로 제한하여 버그를 예방하는 데 도움이 됩니다.

## 2. 호이스팅 (Hoisting)

호이스팅은 코드 실행 전에 선언을 해당 스코프의 맨 위로 옮기는 JavaScript의 동작입니다.

### `var`: 호이스팅되고 초기화됨

`var` 변수는 해당 스코프의 맨 위로 호이스팅되고 `undefined` 값으로 초기화됩니다.

```javascript
console.log(hoistedVar); // undefined (오류 없음)
var hoistedVar = "나는 호이스팅되었어";
console.log(hoistedVar); // "나는 호이스팅되었어"
```
이는 `var` 변수가 선언되기 전에 접근해도 오류가 발생하지 않지만, 그 값은 `undefined`가 됨을 의미합니다.

### `let`과 `const`: 호이스팅되지만 초기화되지 않음

`let`과 `const` 변수도 호이스팅되지만, **초기화되지는 않습니다**. 선언 전에 접근하면 `ReferenceError`가 발생합니다. 블록의 시작부터 선언까지의 기간을 **일시적 사각지대(Temporal Dead Zone, TDZ)**라고 합니다.

```javascript
// console.log(hoistedLet); // ReferenceError: Cannot access 'hoistedLet' before initialization
let hoistedLet = "나도 호이스팅되었어";

// console.log(hoistedConst); // ReferenceError: Cannot access 'hoistedConst' before initialization
const hoistedConst = "나도 그래";
```
이 동작은 값이 할당되기 전에 변수를 실수로 사용하는 것을 방지하여 코드를 더 견고하게 만듭니다.

## 3. 재할당 (Reassignment)

이것이 `let`과 `const`의 주된 차이점입니다.

### `var`와 `let`: 재할당 가능

`var` 또는 `let`으로 선언된 변수는 업데이트하거나 재할당할 수 있습니다.

```javascript
var myVarVariable = "첫 번째 값";
myVarVariable = "새로운 값"; // 허용됨

let myLetVariable = "첫 번째 값";
myLetVariable = "새로운 값"; // 허용됨
```

### `const`: 재할당 불가

`const`(상수를 의미)로 선언된 변수는 선언 시에 초기화되어야 하며 새로운 값을 **재할당할 수 없습니다**.

```javascript
const myConstVariable = "이 값은 상수입니다";
// myConstVariable = "변경 시도"; // TypeError: Assignment to constant variable.
```

**객체 및 배열에 대한 중요 참고 사항:**
`const`로 객체나 배열을 선언하면, 그 내용이 아니라 해당 객체/배열에 대한 **참조**가 상수임을 의미합니다. 객체의 속성이나 배열의 요소는 여전히 수정할 수 있습니다.

```javascript
const myObj = { name: "Alice" };
myObj.name = "Bob"; // 이것은 허용됩니다!
console.log(myObj.name); // "Bob"

const myArray = [1, 2, 3];
myArray.push(4); // 이것도 허용됩니다!
console.log(myArray); // [1, 2, 3, 4]

// 하지만 변수 자체를 재할당할 수는 없습니다
// myObj = { name: "Charlie" }; // TypeError
// myArray = [5, 6]; // TypeError
```

## 요약 및 모범 사례

| 키워드 | 스코프 | 호이스팅 | 재할당 | 재선언(같은 스코프 내) |
| :---: | :--- | :--- | :---: | :---: |
| `var` | 함수 | 호이스팅되고 `undefined`로 초기화 | 예 | 예 |
| `let` | 블록 | 호이스팅되지만 초기화되지 않음(TDZ) | 예 | 아니요 |
| `const` | 블록 | 호이스팅되지만 초기화되지 않음(TDZ) | 아니요 | 아니요 |

현대 JavaScript 변수 선언의 모범 사례는 다음과 같습니다.

1.  **기본적으로 `const` 사용**: 우발적인 재할당을 방지하여 코드를 더 예측 가능하게 만듭니다. 변수의 식별자가 재할당되지 않을 것임을 나타냅니다.
2.  **변수를 재할당해야 할 때만 `let` 사용**: 이는 일반적으로 루프 카운터나 블록 내에서 업데이트해야 하는 변수에 해당합니다.
3.  **`var` 사용 피하기**: 현대 JavaScript(ES6+)에서는 `var`를 사용할 이유가 거의 없습니다. `var`의 함수 스코프 및 호이스팅 동작은 `let`과 `const`가 방지하도록 설계된 버그를 유발할 수 있습니다.

이러한 규칙을 따르면 더 명확하고 신뢰할 수 있으며 디버깅하기 쉬운 JavaScript 코드를 작성할 수 있습니다.

## 전문 보완 체크

**JavaScript 변수: var, let, const의 차이점**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 실행 환경, 정확한 오류 경계, 최소 재현 예제, 되돌릴 수 있는 경로를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

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
