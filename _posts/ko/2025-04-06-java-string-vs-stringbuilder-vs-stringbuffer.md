---
typora-root-url: ../
layout: single
title: >
   Java: String vs. StringBuilder vs. StringBuffer 비교

date: 2025-04-06T07:10:00+09:00
lang: ko
translation_id: java-string-vs-stringbuilder-vs-stringbuffer
header:
   teaser: /images/header_images/overlay_image_java.png
   overlay_image: /images/header_images/overlay_image_java.png
   overlay_filter: 0.5
   image_description: >
     이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Java: String vs. StringBuilder vs. StringBuffer 비교
excerpt: >
    Java에서 문자열을 다루는 세 가지 주요 클래스인 String, StringBuilder, StringBuffer의 핵심 차이점을 이해하여 더 효율적이고 최적화된 코드를 작성하는 방법을 알아보세요.
seo_description: >
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

![이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Java: String vs. StringBuilder vs. StringBuffer 비교](/images/header_images/overlay_image_java.png)
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

## 전문 보완 체크

**Java: String vs. StringBuilder vs. StringBuffer 비교**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 JDK 버전, 빌드 도구 설정, classpath 또는 module path, 런타임 stack trace를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

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
