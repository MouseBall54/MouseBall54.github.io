typora-root-url: ../
layout: single
title: >
   Java: String vs. StringBuilder vs. StringBuffer 비교

lang: ko
translation_id: java-string-vs-stringbuilder-vs-stringbuffer
header:
   teaser: /images/header_images/overlay_image_java.png
   overlay_image: /images/header_images/overlay_image_java.png
   overlay_filter: 0.5
excerpt: >
    Java에서 문자열을 다루는 세 가지 주요 클래스인 String, StringBuilder, StringBuffer의 핵심 차이점을 이해하여 더 효율적이고 최적화된 코드를 작성하는 방법을 알아보세요.
categories:
  - ko_Troubleshooting
tags:
  - Java
  - String
  - StringBuilder
  - StringBuffer
  - Performance
---
## Java의 String vs. StringBuilder vs. StringBuffer

Java에서 문자열은 단순해 보이지만, 어떻게 다루느냐에 따라 성능에 상당한 영향을 미칠 수 있습니다. Java는 문자열을 처리하기 위한 세 가지 주요 클래스인 `String`, `StringBuilder`, `StringBuffer`를 제공합니다. 이들의 차이점을 이해하는 것은 효율적인 코드를 작성하는 데 매우 중요합니다.

### 1. `String`

`String` 클래스는 가장 기본적이고 일반적으로 사용됩니다. `String` 객체의 핵심 특징은 **불변(immutable)**이라는 점입니다.

- **불변성:** `String` 객체는 한번 생성되면 그 값을 변경할 수 없습니다. 문자열을 "수정"할 때마다(예: 연결 연산), 실제로는 메모리에 새로운 `String` 객체가 생성됩니다.

**예시:**
```java
String s = "Hello";
s = s + " World"; // "Hello World"라는 새로운 String 객체를 생성합니다.
                  // 기존의 "Hello"는 가비지 컬렉션 대상이 됩니다.
```

- **`String` 사용 시점:**
  - 문자열 값이 변경되지 않을 때.
  - 간단하고 빈번하지 않은 연결 연산을 할 때.
  - 명시적인 잠금 없이 값의 스레드 안전성이 필요한 다중 스레드 환경에서.

- **성능:** `String` 객체를 사용한 빈번한 연결은 비효율적입니다. 많은 중간 객체를 생성하여 메모리 소비를 늘리고 가비지 컬렉터의 부담을 가중시키기 때문입니다.

### 2. `StringBuilder`

`StringBuilder`는 `String`의 성능 문제를 해결하기 위해 Java 5에서 도입되었습니다. 이것은 **가변(mutable)**적인 문자열 시퀀스입니다.

- **가변성:** 매번 새로운 객체를 생성하지 않고도 `StringBuilder`에 문자를 추가, 삽입 또는 삭제할 수 있습니다. 내부 문자 배열을 직접 수정합니다.
- **스레드 안전성 없음:** `StringBuilder`는 동기화되지 않습니다. 즉, 여러 스레드가 동시에 사용하는 것은 안전하지 않습니다. 그러나 이러한 비동기화 덕분에 `StringBuffer`보다 빠릅니다.

**예시:**
```java
StringBuilder sb = new StringBuilder("Hello");
sb.append(" World"); // 기존 객체를 수정합니다.
System.out.println(sb.toString()); // "Hello World"
```

- **`StringBuilder` 사용 시점:**
  - 단일 스레드 환경에서.
  - 많은 문자열 수정이 필요할 때(예: 반복문 안에서 긴 문자열을 만들 때). 이것이 "문자열 빌더"의 가장 일반적인 선택입니다.

- **성능:** 단일 스레드 환경에서 문자열 조작에 가장 좋은 성능을 제공합니다.

### 3. `StringBuffer`

`StringBuffer`는 `StringBuilder`와 매우 유사합니다. 이 또한 **가변(mutable)**적인 문자열 시퀀스입니다. 주된 차이점은 스레드 안전성입니다.

- **가변성:** `StringBuilder`처럼 새로운 객체를 생성하지 않고 수정할 수 있습니다.
- **스레드 안전성:** `StringBuffer`는 동기화됩니다. `append`, `insert`와 같은 메서드들이 `synchronized`로 선언되어 있어, 데이터 손상 없이 여러 스레드에서 안전하게 사용할 수 있습니다. 이 동기화는 성능 오버헤드를 유발합니다.

**예시:**
```java
StringBuffer sbf = new StringBuffer("Hello");
sbf.append(" World"); // 이 연산은 스레드에 안전합니다.
System.out.println(sbf.toString()); // "Hello World"
```

- **`StringBuffer` 사용 시점:**
  - 여러 스레드가 동일한 문자열 버퍼를 수정할 수 있는 다중 스레드 환경에서.
  - 오래된 Java 코드에서 (Java 5 이전에는 유일한 가변 옵션이었습니다).

- **성능:** 동기화 오버헤드로 인해 `StringBuilder`보다 느립니다.

### 차이점 요약

| 기능          | `String`                               | `StringBuilder`                        | `StringBuffer`                         |
| ---------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- |
| **가변성**   | 불변 (Immutable)                              | 가변 (Mutable)                                | 가변 (Mutable)                                |
| **스레드 안전성**| 안전 (불변성 때문)      | 안전하지 않음 (비동기화)       | 안전 (동기화)             |
| **성능**  | 빈번한 수정 시 느림        | 빠름 (단일 스레드에 최적)        | 느림 (동기화 오버헤드)          |
| **도입 시기**   | JDK 1.0 부터                          | Java 5 (JDK 1.5) 부터                 | JDK 1.0 부터                          |

### 결론

- 고정된 문자열 값이나 간단한 연결에는 **`String`**을 사용하세요.
- 단일 스레드 환경에서 대부분의 문자열 구성 작업에는 **`StringBuilder`**를 사용하세요 (이것이 가변 문자열의 기본 선택입니다).
- 여러 스레드 간에 공유되는 가변 문자열이 필요할 때만 **`StringBuffer`**를 사용하세요.
