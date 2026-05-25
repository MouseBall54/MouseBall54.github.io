---
typora-root-url: ../
layout: single
title: "Java NumberFormatException 예외 처리 방법"

date: 2025-02-09T07:44:00+09:00
lang: ko
translation_id: java-numberformatexception-handling
permalink: /ko_troubleshooting/java-numberformatexception-handling/
excerpt: "파싱 전 문자열을 검증하고, 안전한 숫자 변환을 위해 try-catch 블록을 사용하여 Java의 NumberFormatException을 예방하고 처리하는 방법을 배웁니다."
seo_description: "파싱 전 문자열을 검증하고, 안전한 숫자 변환을 위해 try-catch 블록을 사용하여 Java의 NumberFormatException을 예방하고 처리하는 방법을 배웁니다."
header:
   teaser: /images/header_images/overlay_image_java.png
   overlay_image: /images/header_images/overlay_image_java.png
   overlay_filter: 0.5
   image_description: >
     이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Java NumberFormatException 예외 처리 방법
categories:
  - ko_Troubleshooting
tags:
  - Java
  - NumberFormatException
  - Exception Handling
  - Parsing
---


![이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Java NumberFormatException 예외 처리 방법](/images/header_images/overlay_image_java.png)
## 서론

`java.lang.NumberFormatException`은 문자열을 숫자 유형(예: `int`, `float`, `double` 등)으로 변환하려고 할 때 해당 문자열이 적절한 형식이 아닐 경우 발생하는 Java의 일반적인 unchecked exception이다. 이는 unchecked exception이므로 컴파일러가 처리를 강제하지 않아, 제대로 관리하지 않으면 예기치 않은 프로그램 충돌로 이어질 수 있다. 이 가이드에서는 `NumberFormatException`의 원인과 효과적인 처리 방법을 설명한다.

## NumberFormatException의 일반적인 원인

이 예외는 `Integer.parseInt()`, `Double.parseDouble()`, `Float.parseFloat()`와 같은 메서드에서 여러 조건 하에 발생한다.

### 1. 문자열에 숫자가 아닌 문자가 포함된 경우

가장 흔한 원인은 숫자(및 앞쪽 부호 `-` 또는 `+`) 이외의 문자가 포함된 문자열을 파싱하려고 할 때다.

```java
String notANumber = "123a";
int number = Integer.parseInt(notANumber); 
// NumberFormatException 발생: For input string: "123a"
```

### 2. 문자열에 공백이 포함된 경우

문자열의 시작이나 끝에 있는 공백도 이 예외를 유발할 수 있다.

```java
String withSpace = " 123 ";
int number = Integer.parseInt(withSpace);
// NumberFormatException 발생: For input string: " 123 "
```
**참고**: `Integer.valueOf()`와 같은 일부 메서드는 공백을 다르게 처리할 수 있지만, `parseInt()`는 엄격하다. 문자열을 먼저 `trim()`하는 것이 좋은 습관이다.

### 3. 문자열이 비어 있거나 `null`인 경우

빈 문자열이나 `null` 값을 파싱하려고 하면 `NumberFormatException`이 발생한다.

```java
String empty = "";
int number1 = Integer.parseInt(empty); // NumberFormatException 발생

String nullStr = null;
int number2 = Integer.parseInt(nullStr); // NumberFormatException 발생
```

### 4. 문자열이 표현하는 숫자가 범위를 벗어난 경우

문자열이 대상 데이터 유형의 최대값보다 크거나 최소값보다 작은 숫자를 나타내는 경우 `NumberFormatException`이 발생한다.

```java
String tooBig = "2147483648"; // Integer.MAX_VALUE보다 1 큼
int number = Integer.parseInt(tooBig);
// NumberFormatException 발생: For input string: "2147483648"
```

### 5. 잘못된 소수점 또는 부호 형식

부동 소수점 숫자의 경우, 여러 개의 소수점이나 잘못된 위치의 부호가 있으면 오류가 발생한다.

```java
String badDouble = "12.34.56";
double number = Double.parseDouble(badDouble);
// NumberFormatException 발생
```

## NumberFormatException 처리 방법

이 예외를 처리하는 두 가지 주요 전략이 있다: 파싱 전 유효성 검사와 `try-catch` 블록 사용이다.

### 전략 1: 파싱 전 유효성 검사 (LBYL - Look Before You Leap)

문자열을 파싱하기 전에 유효한 숫자인지 확인할 수 있다. 일반적인 방법은 정규 표현식을 사용하는 것이다.

**예시:**
```java
public boolean isNumeric(String str) {
    if (str == null) {
        return false;
    }
    // 문자열이 유효한 정수인지 확인하는 정규식
    return str.matches("-?\d+"); 
}

String input = "123";
if (isNumeric(input)) {
    int number = Integer.parseInt(input);
    System.out.println("파싱된 숫자: " + number);
} else {
    System.out.println("잘못된 숫자 형식입니다.");
}
```
이 접근 방식은 예외를 발생시키지 않으므로 잘못된 입력이 흔한 경우 성능이 더 좋을 수 있다.

### 전략 2: `try-catch` 블록 사용 (EAFP - Easier to Ask for Forgiveness than Permission)

이것은 예외를 처리하는 가장 일반적이고 견고한 방법이다. 변환을 시도하고 실패할 경우 `NumberFormatException`을 잡는다.

**예시:**
```java
String input = "abc";
int number;
try {
    number = Integer.parseInt(input);
    System.out.println("성공적으로 파싱됨: " + number);
} catch (NumberFormatException e) {
    System.err.println("잘못된 숫자 형식: " + input);
    // 기본값을 제공하거나 오류 메시지를 표시
    number = 0; // 기본값
}
// 프로그램은 계속 실행됨
System.out.println("숫자의 값은: " + number);
```
이 접근 방식은 특히 파싱 로직이 간단할 때 더 깨끗하고 가독성이 좋다.

## 모범 사례

- **입력값 다듬기**: 파싱하기 전에 항상 `str.trim()`을 사용하여 사용자 입력의 앞뒤 공백을 제거한다.
- **`null` 처리**: `NullPointerException`이나 `NumberFormatException`을 피하기 위해 `null` 입력을 명시적으로 확인한다.
- **올바른 전략 선택**:
  - 잘못된 입력이 자주 예상되는 경우, 정규식으로 사전 검증(LBYL)하는 것이 성능에 더 좋을 수 있다.
  - 잘못된 입력이 드문 경우(진정한 예외적인 경우), `try-catch`(EAFP) 접근 방식이 명확성 때문에 일반적으로 선호된다.
- **사용자 피드백 제공**: 사용자 대면 애플리케이션에서는 예외를 잡고 프로그램이 충돌하는 대신 명확하고 사용자 친화적인 오류 메시지를 제공한다.

이러한 기술을 적용하면 숫자 변환을 다룰 때 Java 애플리케이션을 더 탄력적이고 사용자 친화적으로 만들 수 있다.

## 전문 보완 체크

**Java NumberFormatException 예외 처리 방법**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 JDK 버전, 빌드 도구 설정, classpath 또는 module path, 런타임 stack trace를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

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
