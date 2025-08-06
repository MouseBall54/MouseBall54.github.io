typora-root-url: ../
layout: single
title: >
   Java "error: unreachable statement" 해결 방법

lang: ko
translation_id: java-error-unreachable-statement
header:
   teaser: /images/header_images/overlay_image_java.png
   overlay_image: /images/header_images/overlay_image_java.png
   overlay_filter: 0.5
excerpt: >
    절대 실행될 수 없는 코드가 있을 때 발생하는 Java의 "unreachable statement" 컴파일 시간 오류의 원인을 이해하고 해결하는 방법을 알아보세요.
categories:
  - ko_Troubleshooting
tags:
  - Java
  - Compilation Error
  - Unreachable Code
  - Troubleshooting
---
## "unreachable statement" 오류 이해하기

"error: unreachable statement"는 Java의 컴파일 시간 오류로, 코드에 절대 실행될 수 없는 문장이 있음을 나타냅니다. Java 언어 명세는 모든 문장이 도달 가능해야 한다고 요구합니다. 만약 도달할 수 없는 코드가 있다면, 이는 종종 잘못된 로직을 가리키는 프로그래밍 오류로 간주됩니다.

이 오류는 개발자가 죽은 코드(dead code)를 찾아 제거하여 프로그램을 더 깨끗하고 이해하기 쉽게 만드는 데 도움을 줍니다.

### 일반적인 시나리오와 해결책

이 오류를 유발하는 일반적인 상황들을 살펴보겠습니다.

#### 1. `return` 문 뒤에 오는 코드

`return` 문은 메서드에서 즉시 빠져나가게 하므로, 같은 블록 내에서 `return` 문 뒤에 있는 모든 코드는 도달할 수 없습니다.

**잘못된 코드:**
```java
public int getValue() {
    return 10;
    System.out.println("This will never be printed."); // 도달할 수 없는 코드
}
```

**해결책:**
도달할 수 없는 코드를 제거하거나, 실행되어야 하는 코드라면 `return` 문 앞으로 옮깁니다.

```java
public int getValue() {
    System.out.println("This will be printed.");
    return 10;
}
```

#### 2. `throw` 또는 `break` 뒤에 오는 코드

`return`과 유사하게, 제어를 무조건적으로 이전하는 문장들은 같은 블록 내의 후속 코드를 도달할 수 없게 만듭니다.

**`throw` 다음:**
```java
public void checkValue(int value) {
    if (value < 0) {
        throw new IllegalArgumentException("Value cannot be negative.");
        System.out.println("Error logged."); // 도달할 수 없는 코드
    }
}
```

**반복문 안의 `break` 다음:**
```java
public void findFirstItem() {
    while (true) {
        System.out.println("Found item.");
        break;
        System.out.println("This is unreachable."); // 도달할 수 없는 코드
    }
}
```

**해결책:**
의도된 코드 경로만 존재하도록 코드를 재구성해야 합니다. 실행되어야 하는 로직은 제어 이전 문장 앞에 위치해야 합니다.

```java
public void checkValue(int value) {
    if (value < 0) {
        System.out.println("Error logged."); // throw 앞으로 옮깁니다.
        throw new IllegalArgumentException("Value cannot be negative.");
    }
}
```

#### 3. 무한 루프

컴파일러가 루프가 무한하다고 판단할 수 있는 경우, 해당 루프 바로 다음에 오는 모든 코드는 도달할 수 없는 것으로 표시됩니다.

**잘못된 코드:**
```java
public void runForever() {
    while (true) {
        // 이 루프는 절대 끝나지 않습니다.
    }
    System.out.println("This is unreachable."); // 도달할 수 없는 코드
}
```
`for` 루프 또한 무한 루프가 될 수 있습니다.
```java
public void anotherInfiniteLoop() {
    for (;;) {
        // 무한 루프
    }
    System.out.println("Also unreachable."); // 도달할 수 없는 코드
}
```

**해결책:**
만약 무한 루프가 의도된 것(예: 지속적으로 연결을 수신 대기하는 서버 애플리케이션)이라면, 그 뒤에 오는 코드는 실수일 가능성이 높으므로 제거해야 합니다. 루프가 무한이 아니어야 한다면, 루프를 종료할 수 있는 `break` 문이나 조건을 추가해야 합니다.

```java
public void runWithCondition(int limit) {
    int i = 0;
    while (true) {
        i++;
        if (i > limit) {
            break; // 이 구문이 루프를 종료시킵니다.
        }
    }
    System.out.println("This is now reachable."); // 이제 도달 가능합니다.
}
```

### 핵심 요약

"unreachable statement" 오류는 컴파일러가 코드의 일부 로직에 결함이 있음을 알려주는 신호입니다. 절대 실행될 수 없는 문장을 검토하고 제거하라는 의미입니다. 항상 제어 흐름 문장(`return`, `throw`, `break`, `continue`)이 올바르게 배치되었는지, 그리고 루프에 명확한 종료 조건이 있는지 확인하세요.
