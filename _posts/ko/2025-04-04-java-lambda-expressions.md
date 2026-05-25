---
typora-root-url: ../
layout: single
title: >
   Java 람다 표현식(Lambda Expressions)으로 간결한 코드 작성하기

date: 2025-04-04T07:53:00+09:00
lang: ko
translation_id: java-lambda-expressions
header:
   teaser: /images/header_images/overlay_image_java.png
   overlay_image: /images/header_images/overlay_image_java.png
   overlay_filter: 0.5
   image_description: >
     이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Java 람다 표현식(Lambda Expressions)으로 간결한 코드 작성하기
excerpt: >
    Java 람다 표현식이 무엇인지, 함수형 인터페이스의 사용을 어떻게 단순화하는지, 그리고 더 깔끔하고 표현력 있는 코드를 작성하기 위해 사용하는 방법을 알아보세요.
seo_description: >
    Java 람다 표현식이 무엇인지, 함수형 인터페이스의 사용을 어떻게 단순화하는지, 그리고 더 깔끔하고 표현력 있는 코드를 작성하기 위해 사용하는 방법을 알아보세요.
categories:
  - ko_Troubleshooting
tags:
  - Java
  - Lambda Expressions
  - Functional Programming
  - Best Practices
---

![이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Java 람다 표현식(Lambda Expressions)으로 간결한 코드 작성하기](/images/header_images/overlay_image_java.png)
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

## 전문 보완 체크

**Java 람다 표현식(Lambda Expressions)으로 간결한 코드 작성하기**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 JDK 버전, 빌드 도구 설정, classpath 또는 module path, 런타임 stack trace를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

### 신뢰도를 높이는 증거

작업을 바꾸기 전에는 객관적인 증거를 먼저 확인해야 합니다. 쓸 만한 증거에는 `java -version`, `javac -version`, Maven 또는 Gradle 출력, 가장 작은 실패 클래스가 포함됩니다. 증거가 서로 맞지 않으면 억지로 하나의 이야기로 합치지 말고 충돌 자체를 남겨야 합니다. 빠른 해결이 한 번 성공했더라도 같은 입력, 계정, 의존성, 기기 상태에서 다시 확인하지 않았다면 아직 확정된 해결책이라고 보기 어렵습니다.

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
