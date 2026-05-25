---
typora-root-url: ../
layout: single
title: >
    JavaScript에서 "this is undefined" 문제 해결 방법

date: 2025-03-15T07:33:00+09:00
lang: ko
translation_id: javascript-this-is-undefined
header:
    teaser: /images/header_images/overlay_image_js.png
    overlay_image: /images/header_images/overlay_image_js.png
    overlay_filter: 0.5
    image_description: >
      이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: JavaScript에서 "this is undefined" 문제 해결 방법
excerpt: >
    JavaScript에서 'this'는 호출 컨텍스트에 따라 동적으로 결정됩니다. 이로 인해 콜백 함수나 이벤트 핸들러에서 'this'가 undefined가 되는 문제가 자주 발생합니다. 이 글에서는 원인과 해결 방법을 알아봅니다.
seo_description: >
    JavaScript에서 'this'는 호출 컨텍스트에 따라 동적으로 결정됩니다. 이로 인해 콜백 함수나 이벤트 핸들러에서 'this'가 undefined가 되는 문제가 자주 발생합니다. 이 글에서는 원인과 해결 방법을 알아봅니다.
categories:
    - ko_Troubleshooting
tags:
    - JavaScript
    - this
    - Scope
    - undefined
---


![이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: JavaScript에서 "this is undefined" 문제 해결 방법](/images/header_images/overlay_image_js.png)
## JavaScript에서 "this"란 무엇인가?

JavaScript에서 `this` 키워드는 함수가 호출될 때의 컨텍스트(context)를 참조하는 특별한 식별자입니다. `this`가 가리키는 값은 함수를 어떻게 호출했느냐에 따라 달라지며, 이 동작 방식은 종종 개발자들에게 혼란을 줍니다. 특히 객체의 메서드, 콜백 함수, 이벤트 핸들러 내에서 `this`를 사용할 때 문제가 발생하기 쉽습니다.

## "this is undefined"는 왜 발생할까?

1.  **Strict Mode (엄격 모드)**: 엄격 모드에서 일반 함수 호출 시 `this`는 `undefined`로 설정됩니다. 엄격 모드가 아닐 경우 `this`는 전역 객체(`window` 또는 `global`)를 가리킵니다.

2.  **콜백 함수**: 콜백 함수는 다른 함수에 인자로 전달되어 나중에 호출됩니다. 이때 콜백 함수는 원래의 컨텍스트를 잃어버리고, 호출하는 함수의 컨텍스트에 따라 `this`가 결정됩니다. 예를 들어, `setTimeout`의 콜백 함수 내에서 `this`는 전역 객체 또는 `undefined`(엄격 모드)가 됩니다.

3.  **이벤트 핸들러**: DOM 요소의 이벤트 핸들러가 일반 함수로 정의된 경우, `this`는 이벤트를 발생시킨 DOM 요소를 가리킵니다. 하지만 클래스 메서드를 이벤트 핸들러로 직접 전달하면, 해당 메서드는 컨텍스트를 잃고 `this`는 `undefined`가 됩니다.

**예제 코드:**
```javascript
class MyClass {
  constructor() {
    this.value = 42;
  }

  printValue() {
    console.log(this.value); 
  }

  start() {
    // setTimeout의 콜백으로 printValue를 전달
    // 이때 printValue는 MyClass의 컨텍스트를 잃어버림
    setTimeout(this.printValue, 1000); // 1초 후 TypeError: Cannot read properties of undefined (reading 'value')
  }
}

const instance = new MyClass();
instance.start();
```

## "this is undefined" 해결 방법

### 1. 화살표 함수 (Arrow Functions) 사용

화살표 함수는 자신만의 `this` 컨텍스트를 가지지 않습니다. 대신, 자신을 감싸고 있는 **상위 스코프(lexical scope)의 `this`를 그대로 상속받아 사용**합니다. 이는 `this` 문제를 해결하는 가장 현대적이고 간결한 방법입니다.

**해결 예제 (화살표 함수):**
```javascript
class MyClass {
  constructor() {
    this.value = 42;
  }

  start() {
    // 화살표 함수를 사용하면 상위 스코프의 'this'를 유지
    setTimeout(() => {
      console.log(this.value); // 42
    }, 1000);
  }
}

const instance = new MyClass();
instance.start();
```

### 2. `Function.prototype.bind()` 사용

`bind()` 메서드는 함수의 `this` 값을 특정 객체에 영구적으로 바인딩(고정)한 새로운 함수를 반환합니다. 생성자(constructor)에서 메서드를 미리 바인딩해두는 것은 일반적인 패턴입니다.

**해결 예제 (`bind`):**
```javascript
class MyClass {
  constructor() {
    this.value = 42;
    // printValue 메서드의 'this'를 현재 인스턴스에 바인딩
    this.printValue = this.printValue.bind(this);
  }

  printValue() {
    console.log(this.value);
  }

  start() {
    setTimeout(this.printValue, 1000); // 42
  }
}

const instance = new MyClass();
instance.start();
```

### 3. `that` 또는 `self` 변수 사용 (구식 방법)

`this`를 다른 변수(예: `that`, `self`)에 할당하여 클로저(closure)를 통해 내부 함수에서 접근하는 방법입니다. 화살표 함수가 등장하기 전에 널리 사용되었지만, 현재는 화살표 함수를 사용하는 것이 더 권장됩니다.

**해결 예제 (`that`):**
```javascript
class MyClass {
  constructor() {
    this.value = 42;
  }

  start() {
    const that = this; // 'this'를 변수에 저장
    setTimeout(function() {
      console.log(that.value); // 42
    }, 1000);
  }
}
```

## 결론

JavaScript에서 `this`의 동작 방식을 이해하는 것은 매우 중요합니다. 콜백 함수나 이벤트 핸들러에서 `this`가 `undefined`가 되는 문제는 대부분 컨텍스트 상실 때문에 발생합니다. **화살표 함수**는 이러한 문제를 해결하는 가장 직관적이고 효과적인 방법이며, `bind`는 특정 컨텍스트를 명시적으로 고정해야 할 때 유용합니다. 코드의 일관성과 가독성을 위해 `this`를 다루는 일관된 전략을 사용하는 것이 좋습니다.

## 전문 보완 체크

**JavaScript에서 "this is undefined" 문제 해결 방법**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 실행 환경, 정확한 오류 경계, 최소 재현 예제, 되돌릴 수 있는 경로를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

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

## 적용 검토 시나리오

독자가 **JavaScript에서 "this is undefined" 문제 해결 방법**의 첫 번째 권장 조치를 이미 시도했지만 결과가 여전히 불확실하다고 가정해 봅니다. 다음 단계는 여러 해결책을 한꺼번에 시험하는 것이 아니라 짧은 감사 기록을 만드는 것입니다. 먼저 어떤 판단을 하려는지 한 문장으로 쓰고, 환경을 한 문장으로 적고, 관찰된 결과를 한 문장으로 남깁니다. 그다음 실행 환경, 정확한 오류 경계, 최소 재현 예제, 되돌릴 수 있는 경로를 이미 확보한 사실과 대조합니다. 이렇게 해야 글이 서로 끊어진 팁 목록이 아니라 검증 가능한 절차가 됩니다.

### 감사 기록 양식

| 항목 | 예시 기준 | 이유 |
| --- | --- | --- |
| 관찰 | 조치 전 실제로 본 내용 | 기준 상태를 객관화합니다 |
| 증거 | 전체 명령 출력, 버전 번호 | 판단을 기록에 연결합니다 |
| 가정 | 믿고 있지만 아직 증명하지 못한 내용 | 숨은 추정을 드러냅니다 |
| 조치 | 한 번에 하나의 변경 | 결과의 원인을 추적하게 합니다 |
| 중단 기준 | 멈추고 도움을 요청할 조건 | 반복적인 시행착오를 줄입니다 |

### 품질 경계

같은 결과가 통제된 재확인 뒤에도 반복될 때만 이 안내를 강한 결론으로 보아야 합니다. 계정, 기기, 데이터 샘플, 의존성 버전, 계약 조건, 공식 규칙이 달라졌다면 결론의 강도를 낮추고 가설로 다루는 편이 안전합니다. 검색 독자는 급한 문제를 안고 들어오는 경우가 많아 맥락을 건너뛰기 쉽습니다. 전문적인 글은 위험한 판단을 천천히 하게 만들면서도 다음 행동은 분명하게 제시해야 합니다.

## 함께 보면 좋은 글

같은 주제 흐름에서 이어서 읽기 좋은 글입니다.

- [SSL: CERTIFICATE_VERIFY_FAILED 오류 해결 방법 (Windows Python)](/ko_troubleshooting/python-certificate-verify-failed/)
- [Permission denied (publickey) 오류 해결 방법 (Windows Git SSH)](/ko_troubleshooting/git-permission-denied-publickey-windows/)
