---
typora-root-url: ../
layout: single
title: >
    java.lang.NumberFormatException 해결 방법

date: 2025-03-08T07:26:00+09:00
lang: ko
translation_id: java-numberformatexception
header:
   teaser: /images/header_images/overlay_image_java.png
   overlay_image: /images/header_images/overlay_image_java.png
   overlay_filter: 0.5
   image_description: >
     이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: java.lang.NumberFormatException 해결 방법
excerpt: >
    부적절한 형식의 문자열을 숫자 값으로 변환하려고 할 때 발생하는 java.lang.NumberFormatException을 해결하는 방법을 알아보세요.
seo_description: >
    부적절한 형식의 문자열을 숫자 값으로 변환하려고 할 때 발생하는 java.lang.NumberFormatException을 해결하는 방법을 알아보세요.
categories:
  - ko_Troubleshooting
tags:
  - Java
  - Exception
  - NumberFormatException
  - Debugging
---


![이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: java.lang.NumberFormatException 해결 방법](/images/header_images/overlay_image_java.png)
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

## 전문 보완 체크

**java.lang.NumberFormatException 해결 방법**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 JDK 버전, 빌드 도구 설정, classpath 또는 module path, 런타임 stack trace를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

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

## 적용 검토 시나리오

독자가 **java.lang.NumberFormatException 해결 방법**의 첫 번째 권장 조치를 이미 시도했지만 결과가 여전히 불확실하다고 가정해 봅니다. 다음 단계는 여러 해결책을 한꺼번에 시험하는 것이 아니라 짧은 감사 기록을 만드는 것입니다. 먼저 어떤 판단을 하려는지 한 문장으로 쓰고, 환경을 한 문장으로 적고, 관찰된 결과를 한 문장으로 남깁니다. 그다음 JDK 버전, 빌드 도구 설정, classpath 또는 module path, 런타임 stack trace를 이미 확보한 사실과 대조합니다. 이렇게 해야 글이 서로 끊어진 팁 목록이 아니라 검증 가능한 절차가 됩니다.

### 감사 기록 양식

| 항목 | 예시 기준 | 이유 |
| --- | --- | --- |
| 관찰 | 조치 전 실제로 본 내용 | 기준 상태를 객관화합니다 |
| 증거 | `java -version`, `javac -version` | 판단을 기록에 연결합니다 |
| 가정 | 믿고 있지만 아직 증명하지 못한 내용 | 숨은 추정을 드러냅니다 |
| 조치 | 한 번에 하나의 변경 | 결과의 원인을 추적하게 합니다 |
| 중단 기준 | 멈추고 도움을 요청할 조건 | 반복적인 시행착오를 줄입니다 |

### 품질 경계

같은 결과가 통제된 재확인 뒤에도 반복될 때만 이 안내를 강한 결론으로 보아야 합니다. 계정, 기기, 데이터 샘플, 의존성 버전, 계약 조건, 공식 규칙이 달라졌다면 결론의 강도를 낮추고 가설로 다루는 편이 안전합니다. 검색 독자는 급한 문제를 안고 들어오는 경우가 많아 맥락을 건너뛰기 쉽습니다. 전문적인 글은 위험한 판단을 천천히 하게 만들면서도 다음 행동은 분명하게 제시해야 합니다.

## 함께 보면 좋은 글

같은 주제 흐름에서 이어서 읽기 좋은 글입니다.

- [SSL: CERTIFICATE_VERIFY_FAILED 오류 해결 방법 (Windows Python)](/ko_troubleshooting/python-certificate-verify-failed/)
- [Permission denied (publickey) 오류 해결 방법 (Windows Git SSH)](/ko_troubleshooting/git-permission-denied-publickey-windows/)
