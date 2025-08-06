typora-root-url: ../
layout: single
title: >
   Java 람다 표현식(Lambda Expressions)으로 간결한 코드 작성하기

lang: ko
translation_id: java-lambda-expressions
header:
   teaser: /images/header_images/overlay_image_java.png
   overlay_image: /images/header_images/overlay_image_java.png
   overlay_filter: 0.5
excerpt: >
    Java 람다 표현식이 무엇인지, 함수형 인터페이스의 사용을 어떻게 단순화하는지, 그리고 더 깔끔하고 표현력 있는 코드를 작성하기 위해 사용하는 방법을 알아보세요.
categories:
  - ko_Troubleshooting
tags:
  - Java
  - Lambda Expressions
  - Functional Programming
  - Best Practices
---
## 람다 표현식(Lambda Expressions)이란?

Java 8에서 도입된 **람다 표현식**은 매개변수를 받아 값을 반환하는 짧은 코드 블록입니다. 람다 표현식은 메서드와 유사하지만, 이름이 필요 없으며 다른 메서드의 본문 안에서 바로 구현될 수 있습니다.

이는 Java에서 함수형 프로그래밍의 초석이며, **함수형 인터페이스**(단일 추상 메서드를 가진 인터페이스)의 인스턴스를 명확하고 간결하게 표현하는 방법을 제공합니다.

### 람다 이전의 문제점

Java 8 이전에는 기능의 일부를 메서드의 인자로 전달하려면 **익명 내부 클래스(anonymous inner class)**를 사용해야 했습니다. 이 구문은 장황하고 다루기 불편했습니다.

**익명 내부 클래스 예시 (Java 8 이전):**
문자열 리스트를 길이순으로 정렬하고 싶다고 가정해 봅시다.
```java
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.Arrays;

List<String> names = Arrays.asList("Peter", "Anna", "Mike");

Collections.sort(names, new Comparator<String>() {
    @Override
    public int compare(String a, String b) {
        return a.length() - b.length();
    }
});

System.out.println(names); // [Mike, Anna, Peter]
```
이 간단한 비교 로직을 위해 많은 상용구 코드가 필요합니다.

## 해결책: 람다 표현식

람다 표현식은 함수형 인터페이스의 인스턴스를 더 간결하게 표현할 수 있게 해줍니다.

**람다 표현식 예시 (Java 8 이상):**
```java
import java.util.Collections;
import java.util.List;
import java.util.Arrays;

List<String> names = Arrays.asList("Peter", "Anna", "Mike");

// 람다 표현식 (a, b) -> a.length() - b.length()는 Comparator 인터페이스의 구현체입니다.
Collections.sort(names, (String a, String b) -> {
    return a.length() - b.length();
});

System.out.println(names); // [Mike, Anna, Peter]
```

이 코드는 정확히 동일한 작업을 수행하지만, 읽고 쓰기가 훨씬 쉽습니다.

### 람다 표현식의 구문

람다 표현식은 세 부분으로 구성됩니다:

1.  **매개변수 목록:** 괄호 `()`로 묶인 쉼표로 구분된 매개변수 목록. 컴파일러가 종종 매개변수 타입을 추론할 수 있으므로 생략할 수 있습니다.
2.  **화살표 토큰:** `->` 토큰은 매개변수와 본문을 구분합니다.
3.  **본문:** 단일 표현식 또는 중괄호 `{}`로 묶인 코드 블록.

**추가적인 단순화:**
이전 예제는 훨씬 더 간결하게 만들 수 있습니다.
```java
// 매개변수 a와 b에 대한 타입 추론
// 단일 표현식 본문에는 중괄호나 return 문이 필요 없음
Collections.sort(names, (a, b) -> a.length() - b.length());
```

### 어디서 람다 표현식을 사용할 수 있는가?

람다 표현식은 **함수형 인터페이스**가 예상되는 모든 곳에서 사용할 수 있습니다. 함수형 인터페이스는 정확히 하나의 추상 메서드를 포함하는 모든 인터페이스입니다. `java.util.function` 패키지는 다음과 같은 많은 내장 함수형 인터페이스를 제공합니다:

- **`Predicate<T>`**: 하나의 인자에 대한 술어(boolean 값을 반환하는 함수)를 나타냅니다. 메서드: `boolean test(T t)`.
- **`Function<T, R>`**: 하나의 인자를 받아 결과를 생성하는 함수를 나타냅니다. 메서드: `R apply(T t)`.
- **`Consumer<T>`**: 단일 입력 인자를 받고 결과를 반환하지 않는 연산을 나타냅니다. 메서드: `void accept(T t)`.
- **`Supplier<T>`**: 결과의 공급자를 나타냅니다. 메서드: `T get()`.
- **`Comparator<T>`**: 두 객체를 비교하는 데 사용됩니다. 메서드: `int compare(T o1, T o2)`.

**`forEach`와 `Consumer` 예시:**
```java
List<String> names = Arrays.asList("Peter", "Anna", "Mike");

// 람다 표현식 s -> System.out.println(s)는 Consumer 인터페이스의 구현체입니다.
names.forEach(s -> System.out.println(s));
```

### 메서드 참조 (Method References)

메서드 참조는 기존 메서드를 이름으로 참조할 수 있게 해주는 특별하고 훨씬 더 간결한 유형의 람다 표현식입니다.

- **구문:** `클래스이름::메서드이름`

**예시:**
`forEach` 예제는 메서드 참조로 다시 작성할 수 있습니다.
```java
// System.out::println은 System.out 객체의 println 메서드에 대한 참조입니다.
names.forEach(System.out::println);
```
람다 표현식이 단지 기존 메서드를 호출하는 경우, 이것이 종종 가장 가독성이 좋은 옵션입니다.

### 핵심 요약

람다 표현식은 Java에서 깔끔한 함수형 스타일의 코드를 작성하기 위한 강력한 기능입니다. 상용구를 줄이고 가독성을 향상시키며, Stream API와 같은 현대적인 Java API와 작업하는 데 필수적입니다. 코드를 더 표현력 있고 간결하게 만들기 위해 람다를 적극적으로 활용하세요.
