typora-root-url: ../
layout: single
title: >
   Java에서 IllegalArgumentException 처리하는 방법
date: 2025-08-05T10:30:00+09:00
header:
   teaser: /images/header_images/overlay_image_java.png
   overlay_image: /images/header_images/overlay_image_java.png
   overlay_filter: 0.5
excerpt: >
    IllegalArgumentException이 무엇인지, 왜 발생하는지, 그리고 메서드 인자를 검증하고 코드의 견고성을 향상시키기 위해 효과적으로 사용하는 방법을 알아보세요.
categories:
  - ko_Troubleshooting
tags:
  - Java
  - Exceptions
  - IllegalArgumentException
  - Best Practices
---
## `IllegalArgumentException`이란 무엇인가?

`IllegalArgumentException`은 메서드에 부적절하거나 잘못된 인수가 전달되었음을 나타내기 위해 발생하는 Java의 **unchecked exception**입니다. 이것은 `RuntimeException`의 하위 클래스로, 컴파일러가 `try-catch` 블록이나 `throws` 절로 처리하도록 강제하지 않는다는 의미입니다.

이 예외는 메서드와 호출자 사이의 규약을 강제하는 중요한 도구입니다. 호출자가 메서드 사용의 전제 조건을 위반했음을 알리는 신호입니다.

### 언제 그리고 왜 발생하는가?

호출자가 메서드의 정의에 따라 유효하지 않은 인수를 전달했을 때 수동으로 `IllegalArgumentException`을 발생시켜야 합니다. 이는 메서드 시작 부분에서 **인수 검증**을 수행하는 방법입니다.

일반적인 시나리오는 다음과 같습니다:
- 값이 예상 범위를 벗어날 때 (예: 나이에 음수 값).
- 객체가 유효하지 않은 상태일 때.
- 문자열이 필수 형식과 일치하지 않을 때.
- 인수가 `null`이 아니어야 할 때 `null`일 경우 (이 경우에는 `NullPointerException`이 더 구체적일 때가 많습니다).

이 예외를 조기에 발생시킴으로써, 유효하지 않은 데이터로 메서드가 계속 진행되는 것을 막을 수 있으며, 이는 나중에 더 모호한 오류나 잘못된 동작으로 이어질 수 있습니다.

### `IllegalArgumentException`을 발생시키는 방법

사용자의 나이를 설정하는 메서드 예제를 살펴보겠습니다. 나이는 음수가 아닌 정수여야 합니다.

```java
public class User {
    private String name;
    private int age;

    public void setAge(int age) {
        if (age < 0) {
            // 나이가 유효하지 않으면 예외를 발생시킵니다.
            throw new IllegalArgumentException("Age cannot be negative. Received: " + age);
        }
        this.age = age;
    }
    // 다른 메서드들...
}
```

이 예제에서:
1.  `setAge` 메서드는 먼저 `age` 매개변수를 검증합니다.
2.  `age`가 0보다 작으면, 설명적인 메시지와 함께 새로운 `IllegalArgumentException`을 생성합니다.
3.  `throw` 키워드는 즉시 메서드 실행을 중단하고 예외를 호출 스택 위로 전달합니다.

오류 메시지는 중요합니다. 메서드를 사용하는 개발자가 문제를 쉽게 디버깅할 수 있도록 인수에 무엇이 잘못되었는지 명확하게 설명해야 합니다.

### `IllegalArgumentException`을 처리하는 방법

`IllegalArgumentException`은 unchecked exception이므로, 이를 잡을 의무는 없습니다. 이것은 일반적으로 호출자 측의 **프로그래밍 오류**를 나타냅니다. 이를 "처리"하는 가장 좋은 방법은 호출 코드를 수정하여 유효하지 않은 인수를 절대 전달하지 않도록 하는 것입니다.

예를 들어, `setAge`를 호출하는 코드는 다음과 같이 수정되어야 합니다.

**잘못된 호출 코드 (버그):**
```java
User user = new User();
int ageFromUserInput = -5; // 이것은 검증되었어야 합니다.
user.setAge(ageFromUserInput); // IllegalArgumentException 발생
```

**수정된 호출 코드:**
```java
User user = new User();
int ageFromUserInput = -5;

// 메서드를 호출하기 전에 입력을 검증합니다.
if (ageFromUserInput >= 0) {
    user.setAge(ageFromUserInput);
} else {
    System.err.println("Invalid age entered. Please provide a valid age.");
}
```

드물게, 완전히 제어할 수 없는 외부 입력으로 인해 유효하지 않은 인수가 들어오는 경우와 같이 이를 잡고 싶을 때도 있습니다.

```java
try {
    int age = Integer.parseInt(userInput);
    user.setAge(age);
} catch (IllegalArgumentException e) {
    // 오류를 기록하고 사용자에게 알립니다.
    System.err.println("Error: " + e.getMessage());
    // 다시 입력을 요청합니다.
}
```

### `IllegalArgumentException` vs. `IllegalStateException`

`IllegalArgumentException`을 `IllegalStateException`과 혼동하지 않는 것이 중요합니다.

- **`IllegalArgumentException`**: 문제는 호출자에 의해 메서드*로* 전달된 인수에 있습니다.
- **`IllegalStateException`**: 문제는 메서드가 호출된 *객체의 상태*에 있습니다. 인수는 유효할 수 있지만, 객체가 해당 작업을 수행하기에 적절한 상태가 아닌 경우입니다.

**`IllegalStateException`의 예시:**
```java
public class Connection {
    private boolean isOpen = false;

    public void sendData(String data) {
        if (!isOpen) {
            throw new IllegalStateException("Connection is not open. Cannot send data.");
        }
        // ... 데이터 전송
    }
    // ... 열기/닫기 위한 다른 메서드들
}
```

### 핵심 요약

`IllegalArgumentException`을 사용하여 메서드를 견고하고 자체적으로 문서화되도록 만드세요. 메서드 시작 시 인수를 검증하고 이 예외를 발생시킴으로써, 잘못된 사용에 대한 즉각적이고 명확한 피드백을 제공하여 버그를 예방하고 코드를 더 쉽게 유지보수할 수 있도록 돕습니다.
