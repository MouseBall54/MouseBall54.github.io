---
typora-root-url: ../
layout: single
title: "Java IllegalArgumentException 예외 처리 방법"
date: 2025-07-31T22:14:00+09:00
excerpt: "메서드 시작 시 명시적 검사를 수행하여 인수가 유효한지 확인하고, Java의 IllegalArgumentException을 효과적으로 사용하고 처리하는 방법을 배웁니다."
categories:
  - ko_Troubleshooting
tags:
  - Java
  - IllegalArgumentException
  - Exception Handling
  - Best Practices
---

## 서론

`java.lang.IllegalArgumentException`은 메서드에 불법적이거나 부적절한 인수가 전달되었음을 나타내기 위해 발생하는 Java의 unchecked exception이다. 이는 메서드가 제공된 입력이 메서드의 사전 조건을 충족하지 않음을 호출자에게 알리는 방법이다. 외부 문제(네트워크나 파일 문제 등)를 알리는 다른 많은 예외와 달리, 이 예외는 거의 항상 프로그래머의 오류를 나타낸다—즉, 호출 코드가 호출하는 메서드의 계약을 존중하지 않고 있다는 것이다.

## IllegalArgumentException은 언제 발생시켜야 하는가?

메서드의 매개변수를 검증하기 위해 메서드 시작 부분에서 `IllegalArgumentException`을 발생시켜야 한다. 이는 메서드가 유효한 데이터에 대해서만 작동하도록 보장하여, 불안정한 상태에 들어가거나 부정확한 결과를 생성하는 것을 방지하는 방어적 프로그래밍의 한 형태다.

일반적인 유효성 검사 항목은 다음과 같다:
- **Null이 아닌 인수**: 객체 참조가 `null`이 아님을 보장한다.
- **범위 검사**: 숫자 값이 예상 범위 내에 있는지 확인한다 (예: 나이는 음수일 수 없다).
- **형식 검사**: 문자열이 특정 형식과 일치하는지 확인한다 (예: 유효한 이메일 주소여야 한다).
- **상태 검사**: 인수 객체가 적절한 상태에 있는지 확인한다.

### `IllegalArgumentException` 발생 예시

`Person` 객체의 나이를 설정하는 메서드를 생각해보자. 나이는 음수일 수 없다.

```java
public class Person {
    private int age;
    private String name;

    public Person(String name, int age) {
        if (name == null || name.trim().isEmpty()) {
            throw new IllegalArgumentException("이름은 null이거나 비어 있을 수 없습니다.");
        }
        if (age < 0) {
            throw new IllegalArgumentException("나이는 음수일 수 없습니다. 입력값: " + age);
        }
        this.name = name;
        this.age = age;
    }

    public void setAge(int age) {
        if (age < 0) {
            throw new IllegalArgumentException("나이는 음수일 수 없습니다. 입력값: " + age);
        }
        this.age = age;
    }
}
```

이 예제에서 생성자와 `setAge` 메서드는 `age` 매개변수에 대해 즉시 검사를 수행한다. 검사가 실패하면, 명확하고 설명적인 메시지와 함께 예외를 발생시킨다. 이러한 "fail-fast" 접근 방식은 오류가 발생한 근원에서 잡히기 때문에 디버깅을 훨씬 쉽게 만든다.

## IllegalArgumentException 처리 방법

`IllegalArgumentException`은 unchecked exception이므로 컴파일러가 이를 잡도록 강제하지 않는다. 대부분의 경우, **이 예외를 잡아서는 안 된다**.

왜냐하면 이것은 코드의 버그를 의미하기 때문이다. 호출하는 메서드가 유효하지 않은 데이터를 전달했다. 올바른 조치는 예외를 잡고 복구하려는 시도가 아니라 **호출 코드를 수정하는 것**이다.

### 잘못된 방법: 예외 잡기

```java
// 이렇게 하지 마세요
Person person;
try {
    person = new Person("John", -5); // 유효하지 않은 인수 전달
} catch (IllegalArgumentException e) {
    // 예외를 잡아 "문제"를 해결하려는 시도
    System.err.println("예외 발생, 나이를 0으로 설정합니다.");
    person = new Person("John", 0); // 이것은 원래의 버그를 숨긴다
}
```
여기서 예외를 잡는 것은 진짜 문제, 즉 음수 나이로 `Person`을 생성하려던 코드를 숨긴다. 버그는 여전히 존재하지만 이제 찾기가 더 어려워졌다.

### 올바른 방법: 호출 코드 수정하기

개발자는 테스트 중에 예외를 보고 실수를 깨닫고, 유효하지 않은 인수를 전달하는 코드를 수정해야 한다.

**올바른 호출 코드 예시:**
```java
public void processPerson(int ageInput) {
    // 호출 코드는 유효한 데이터를 제공할 책임이 있다.
    // 예를 들어, 사용자 입력을 검증함으로써.
    if (ageInput >= 0) {
        Person person = new Person("Jane", ageInput);
        System.out.println("Person이 성공적으로 생성되었습니다.");
    } else {
        System.err.println("유효하지 않은 나이가 제공되었습니다. Person을 생성할 수 없습니다.");
        // 유효하지 않은 입력을 우아하게 처리, 예: 사용자에게 오류 표시
    }
}
```

## 모범 사례

1.  **Fail-Fast**: 메서드 시작 부분에서 인수 유효성 검사를 수행하라. 이는 객체가 일관성 없는 상태에 빠지는 것을 방지한다.
2.  **명확한 메시지 제공**: `IllegalArgumentException`을 발생시킬 때, 인수에 무엇이 잘못되었고 예상되는 값은 무엇이었는지 설명하는 상세한 메시지를 포함하라. 이는 디버깅에 매우 중요하다.
3.  **메서드의 계약 문서화**: Javadoc 주석을 사용하여 메서드 매개변수의 사전 조건을 명확하게 문서화하라. 각 인수의 유효한 범위, 형식 또는 상태를 명시하라.
    ```java
    /**
     * 사람의 나이를 설정합니다.
     *
     * @param age 새로운 나이
     * @throws IllegalArgumentException 나이가 음수인 경우
     */
    public void setAge(int age) {
        // ... 구현 ...
    }
    ```
4.  **잡지 말 것 (보통의 경우)**: `IllegalArgumentException`을 호출 코드의 버그를 수정하라는 신호로 취급하라. 입력을 완전히 제어할 수 없는 제3자 라이브러리와 상호 작용하는 경우와 같이 매우 드문 경우에만 사용자 친화적인 오류 메시지를 제공하기 위해 잡는 것을 고려할 수 있다.

`IllegalArgumentException`을 올바르게 사용함으로써 더 견고하고 예측 가능하며 자체 문서화되는 API를 만들 수 있다.
