typora-root-url: ../
layout: single
title: >
   Java "error: missing return statement" 해결 방법
date: 2025-08-05T10:00:00+09:00
header:
   teaser: /images/header_images/overlay_image_java.png
   overlay_image: /images/header_images/overlay_image_java.png
   overlay_filter: 0.5
excerpt: >
    Java에서 "error: missing return statement" 오류는 반환 타입이 명시된 메서드의 모든 코드 경로가 값을 반환하도록 보장하지 않을 때 발생합니다. 이 문제를 해결하는 방법을 알아보세요.
categories:
  - ko_Troubleshooting
tags:
  - Java
  - Compilation Error
  - Return Statement
  - Troubleshooting
---
## "missing return statement" 오류 이해하기

"error: missing return statement"는 Java에서 흔히 발생하는 컴파일 시간 오류입니다. 이 오류는 메서드가 특정 타입의 값(`int`, `String`, `Object` 등)을 반환하도록 선언되었지만, 컴파일러가 분석했을 때 값을 반환하지 않고 메서드가 종료될 수 있는 경로가 하나 이상 존재할 때 발생합니다.

### 문제의 원인

Java 컴파일러는 `void`가 아닌 반환 타입을 가진 모든 메서드가 어떤 경우에도 반드시 값을 반환하도록 강제합니다. 만약 `if-else`와 같은 조건문 로직이 있다면, 각 분기점이 값을 반환하거나 모든 조건문 블록 다음에 최종 `return` 문이 존재해야 합니다.

### 일반적인 시나리오와 해결책

이 오류가 발생하는 대표적인 예시와 해결 방법을 살펴보겠습니다.

#### 1. 조건문 블록에 `return` 누락

가장 흔한 원인입니다.

**잘못된 코드:**
```java
public int getNumberSign(int number) {
    if (number > 0) {
        return 1;
    } else if (number < 0) {
        return -1;
    }
    // number가 0일 때 반환하는 구문이 없습니다.
}
```

이 예제에서 `number`가 `0`이면 `if` 또는 `else if` 조건이 모두 충족되지 않아, 메서드는 값을 반환하지 않고 종료됩니다.

**해결책:**
모든 경로가 값을 반환하도록 보장해야 합니다. 마지막에 `else` 블록을 추가하거나 기본 `return` 문을 추가할 수 있습니다.

```java
public int getNumberSign(int number) {
    if (number > 0) {
        return 1;
    } else if (number < 0) {
        return -1;
    } else {
        return 0; // number가 0인 경우를 처리합니다.
    }
}
```
또는 메서드 마지막에 기본 반환 값을 둘 수도 있습니다.
```java
public int getNumberSign(int number) {
    if (number > 0) {
        return 1;
    }
    if (number < 0) {
        return -1;
    }
    return 0; // 나머지 경우에 대한 기본 반환 값입니다.
}
```

#### 2. 반복문 내부에만 `return` 존재

컴파일러는 반복문이 최소 한 번 이상 실행될 것이라고 보장할 수 없습니다. 따라서 반복문 내부에만 `return` 문이 있는 것은 충분하지 않습니다.

**잘못된 코드:**
```java
public boolean findValue(int[] array, int value) {
    for (int item : array) {
        if (item == value) {
            return true; // 값을 찾았을 때만 반환합니다.
        }
    }
    // 반복문이 종료된 후 값을 찾지 못했을 때 어떻게 될까요?
}
```

**해결책:**
반복문이 끝난 후 값을 반환하는 `return` 문을 추가하여, 반복문에서 값을 찾지 못하고 종료되는 경우를 처리해야 합니다.

```java
public boolean findValue(int[] array, int value) {
    for (int item : array) {
        if (item == value) {
            return true;
        }
    }
    return false; // 모든 항목을 확인한 후에도 값을 찾지 못하면 false를 반환합니다.
}
```

#### 3. 복잡한 조건부 로직

로직이 복잡해지면 누락된 경로를 찾기 더 어려울 수 있습니다.

**잘못된 코드:**
```java
public String getCategory(int score) {
    if (score >= 90) {
        return "A";
    }
    if (score >= 80 && score < 90) {
        return "B";
    }
    // 80점 미만일 때 반환 값이 없습니다.
}
```

**해결책:**
`if-else if-else` 구조를 사용하여 모든 가능성을 처리하거나, 기본 반환 값을 제공해야 합니다.

```java
public String getCategory(int score) {
    if (score >= 90) {
        return "A";
    } else if (score >= 80) { // 여기서 && score < 90 조건은 불필요합니다.
        return "B";
    } else {
        return "C"; // 다른 모든 경우를 처리합니다.
    }
}
```

### 핵심 요약

"missing return statement" 오류를 피하려면 반환 타입이 있는 메서드를 작성할 때 항상 주의를 기울여야 합니다. 실행 경로가 어떻게 되든 항상 `return` 문에 도달하도록 보장해야 합니다. 이를 위한 간단한 방법은 메서드 본문 마지막에 조건 없는 최종 `return` 문을 두는 것입니다.
