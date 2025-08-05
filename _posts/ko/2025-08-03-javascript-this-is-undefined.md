---
typora-root-url: ../
layout: single
title: >
    JavaScript에서 "this is undefined" 문제 해결 방법
date: 2025-08-03T14:20:00+09:00
header:
    teaser: /images/header_images/overlay_image_js.png
    overlay_image: /images/header_images/overlay_image_js.png
    overlay_filter: 0.5
excerpt: >
    JavaScript에서 'this'는 호출 컨텍스트에 따라 동적으로 결정됩니다. 이로 인해 콜백 함수나 이벤트 핸들러에서 'this'가 undefined가 되는 문제가 자주 발생합니다. 이 글에서는 원인과 해결 방법을 알아봅니다.
categories:
    - ko_Troubleshooting
tags:
    - JavaScript
    - this
    - Scope
    - undefined
---

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

