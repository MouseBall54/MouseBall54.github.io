---
typora-root-url: ../
layout: single
title: >
    java.lang.NumberFormatException 해결 방법

lang: ko
translation_id: java-numberformatexception
header:
   teaser: /images/header_images/overlay_image_java.png
   overlay_image: /images/header_images/overlay_image_java.png
   overlay_filter: 0.5
excerpt: >
    부적절한 형식의 문자열을 숫자 값으로 변환하려고 할 때 발생하는 java.lang.NumberFormatException을 해결하는 방법을 알아보세요.
categories:
  - ko_Troubleshooting
tags:
  - Java
  - Exception
  - NumberFormatException
  - Debugging
---

## NumberFormatException 이란?

`java.lang.NumberFormatException`은 애플리케이션이 문자열을 숫자 타입(예: `int`, `float`, `double` 등)으로 변환하려고 할 때, 해당 문자열이 변환 가능한 형식이 아닐 경우 발생하는 `unchecked exception`입니다. 이 예외는 주로 `Integer.parseInt()`, `Double.parseDouble()`, `Float.parseFloat()`와 같은 메서드를 사용할 때 발생합니다.

예를 들어, 문자열 `"123"`을 정수로 변환하면 완벽하게 작동합니다. 하지만 `"abc"`나 `"12.3"`과 같은 문자열을 정수로 변환하려고 하면 `NumberFormatException`이 발생합니다.

## 주요 원인과 해결 방법

이 예외를 유발하는 일반적인 시나리오와 이를 예방하거나 처리하는 방법을 살펴보겠습니다.

### 1. 문자열에 숫자가 아닌 문자가 포함된 경우

가장 흔한 원인은 글자, 기호 또는 숫자가 아닌 다른 문자가 포함된 문자열을 파싱하려고 할 때입니다.

**문제 코드:**
```java
public class Main {
    public static void main(String[] args) {
        String notANumber = "hello123";
        int number = Integer.parseInt(notANumber); // NumberFormatException 발생
        System.out.println(number);
    }
}
```

**해결 방법:**
문자열을 파싱하기 전에 유효성을 검사해야 합니다. `try-catch` 블록은 이 예외를 정상적으로 처리하는 표준적인 방법입니다.

**수정된 코드:**
```java
public class Main {
    public static void main(String[] args) {
        String notANumber = "hello123";
        try {
            int number = Integer.parseInt(notANumber);
            System.out.println(number);
        } catch (NumberFormatException e) {
            System.err.println("문자열이 유효한 정수가 아닙니다: " + notANumber);
            // e.printStackTrace(); // 디버깅용
        }
    }
}
```
이 코드는 예외를 잡아 프로그램이 충돌하는 대신 사용자 친화적인 오류 메시지를 출력합니다.

### 2. 문자열에 공백이 포함된 경우

문자열의 앞이나 뒤에 있는 공백도 `NumberFormatException`을 유발할 수 있습니다.

**문제 코드:**
```java
String withWhitespace = "  123  ";
int number = Integer.parseInt(withWhitespace); // NumberFormatException 발생
```
*참고: `Integer.parseInt()`는 Java 1.4부터 실제로 공백을 처리할 수 있지만, 다른 파서나 이전 버전에서는 그렇지 않을 수 있습니다. 문자열을 `trim()`하는 것은 여전히 좋은 습관입니다.*

**해결 방법:**
파싱하기 전에 `String` 클래스의 `trim()` 메서드를 사용하여 앞뒤 공백을 제거합니다.

**수정된 코드:**
```java
String withWhitespace = "  123  ";
try {
    int number = Integer.parseInt(withWhitespace.trim());
    System.out.println(number); // 출력: 123
} catch (NumberFormatException e) {
    System.err.println("공백이 포함된 문자열 파싱 오류.");
}
```

### 3. 부동 소수점 숫자를 정수로 파싱하는 경우

부동 소수점 숫자를 나타내는 문자열(예: `"19.99"`)을 `Integer.parseInt()`를 사용하여 파싱하려고 하면, 마침표(`.`)가 정수에 유효한 문자가 아니기 때문에 실패합니다.

**문제 코드:**
```java
String floatString = "19.99";
int number = Integer.parseInt(floatString); // NumberFormatException 발생
```

**해결 방법:**
먼저 문자열을 `Double`이나 `Float`으로 파싱한 다음, 필요한 경우 `int`로 형변환합니다.

**수정된 코드:**
```java
String floatString = "19.99";
try {
    double doubleValue = Double.parseDouble(floatString);
    int number = (int) doubleValue; // int로 형변환
    System.out.println(number); // 출력: 19
} catch (NumberFormatException e) {
    System.err.println("문자열이 유효한 숫자가 아닙니다: " + floatString);
}
```

### 4. 특수 문자 또는 기호

통화 기호, 쉼표 또는 기타 특수 문자가 포함된 문자열은 직접 파싱할 수 없습니다.

**문제 코드:**
```java
String currencyValue = "$1,000";
int number = Integer.parseInt(currencyValue); // NumberFormatException 발생
```

**해결 방법:**
파싱하기 전에 이러한 특수 문자를 제거하도록 문자열을 전처리해야 합니다.

**수정된 코드:**
```java
String currencyValue = "$1,000";
try {
    String cleanString = currencyValue.replace("$", "").replace(",", "");
    int number = Integer.parseInt(cleanString);
    System.out.println(number); // 출력: 1000
} catch (NumberFormatException e) {
    System.err.println("통화 문자열 파싱 오류.");
}
```

## 예방을 위한 모범 사례

- **항상 `try-catch` 블록 사용:** 문자열이 항상 올바른 형식일 것이라고 가정하지 마세요. 파싱 로직을 `try-catch` 블록으로 감싸는 것이 애플리케이션 충돌을 방지하는 가장 안전한 방법입니다.
- **입력 유효성 검사:** 파싱을 시도하기 전에 사용자 입력을 검증하세요. 정규 표현식을 사용하여 문자열에 숫자만 포함되어 있는지 확인할 수 있습니다.
- **문자열 전처리:** `trim()` 및 `replace()`와 같은 메서드를 사용하여 파싱 전에 문자열을 정리하세요.

이러한 지침을 따르면 `NumberFormatException`을 효과적으로 처리하고 Java 애플리케이션을 더 견고하고 사용자 친화적으로 만들 수 있습니다.
