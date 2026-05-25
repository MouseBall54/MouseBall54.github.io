---
typora-root-url: ../
layout: single
title: >
   Java "error: missing return statement" 해결 방법

date: 2025-03-31T07:49:00+09:00
lang: ko
translation_id: java-error-missing-return-statement
header:
   teaser: /images/header_images/overlay_image_java.png
   overlay_image: /images/header_images/overlay_image_java.png
   overlay_filter: 0.5
   image_description: >
     이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Java "error: missing return statement" 해결 방법
excerpt: >
    Java에서 "error: missing return statement" 오류는 반환 타입이 명시된 메서드의 모든 코드 경로가 값을 반환하도록 보장하지 않을 때 발생합니다. 이 문제를 해결하는 방법을 알아보세요.
seo_description: >
    Java에서 "error: missing return statement" 오류는 반환 타입이 명시된 메서드의 모든 코드 경로가 값을 반환하도록 보장하지 않을 때 발생합니다. 이 문제를 해결하는 방법을 알아보세요.
categories:
  - ko_Troubleshooting
tags:
  - Java
  - Compilation Error
  - Return Statement
  - Troubleshooting
---

![이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Java "error: missing return statement" 해결 방법](/images/header_images/overlay_image_java.png)
## "missing return statement" 오류 이해하기

"error: missing return statement"는 Java에서 흔히 발생하는 컴파일 시간 오류입니다. 이 오류는 메서드가 특정 타입의 값(`int`, `String`, `Object` 등)을 반환하도록 선언되었지만, 컴파일러가 분석했을 때 값을 반환하지 않고 메서드가 종료될 수 있는 경로가 하나 이상 존재할 때 발생합니다.

### 문제의 원인

Java 컴파일러는 `void`가 아닌 반환 타입을 가진 모든 메서드가 어떤 경우에도 반드시 값을 반환하도록 강제합니다. 만약 `if-else`와 같은 조건문 로직이 있다면, 각 분기점이 값을 반환하거나 모든 조건문 블록 다음에 최종 `return` 문이 존재해야 합니다.

### 일반적인 시나리오와 해결책

이 오류가 발생하는 대표적인 예시와 해결 방법을 살펴보겠습니다.

#### 1. 조건문 블록에 `return` 누락

가장 흔한 원인입니다.

**잘못된 코드:**
```java
public int getNumberSign(int number) {
    if (number > 0) {
        return 1;
    } else if (number < 0) {
        return -1;
    }
    // number가 0일 때 반환하는 구문이 없습니다.
}
```

이 예제에서 `number`가 `0`이면 `if` 또는 `else if` 조건이 모두 충족되지 않아, 메서드는 값을 반환하지 않고 종료됩니다.

**해결책:**
모든 경로가 값을 반환하도록 보장해야 합니다. 마지막에 `else` 블록을 추가하거나 기본 `return` 문을 추가할 수 있습니다.

```java
public int getNumberSign(int number) {
    if (number > 0) {
        return 1;
    } else if (number < 0) {
        return -1;
    } else {
        return 0; // number가 0인 경우를 처리합니다.
    }
}
```
또는 메서드 마지막에 기본 반환 값을 둘 수도 있습니다.
```java
public int getNumberSign(int number) {
    if (number > 0) {
        return 1;
    }
    if (number < 0) {
        return -1;
    }
    return 0; // 나머지 경우에 대한 기본 반환 값입니다.
}
```

#### 2. 반복문 내부에만 `return` 존재

컴파일러는 반복문이 최소 한 번 이상 실행될 것이라고 보장할 수 없습니다. 따라서 반복문 내부에만 `return` 문이 있는 것은 충분하지 않습니다.

**잘못된 코드:**
```java
public boolean findValue(int[] array, int value) {
    for (int item : array) {
        if (item == value) {
            return true; // 값을 찾았을 때만 반환합니다.
        }
    }
    // 반복문이 종료된 후 값을 찾지 못했을 때 어떻게 될까요?
}
```

**해결책:**
반복문이 끝난 후 값을 반환하는 `return` 문을 추가하여, 반복문에서 값을 찾지 못하고 종료되는 경우를 처리해야 합니다.

```java
public boolean findValue(int[] array, int value) {
    for (int item : array) {
        if (item == value) {
            return true;
        }
    }
    return false; // 모든 항목을 확인한 후에도 값을 찾지 못하면 false를 반환합니다.
}
```

#### 3. 복잡한 조건부 로직

로직이 복잡해지면 누락된 경로를 찾기 더 어려울 수 있습니다.

**잘못된 코드:**
```java
public String getCategory(int score) {
    if (score >= 90) {
        return "A";
    }
    if (score >= 80 && score < 90) {
        return "B";
    }
    // 80점 미만일 때 반환 값이 없습니다.
}
```

**해결책:**
`if-else if-else` 구조를 사용하여 모든 가능성을 처리하거나, 기본 반환 값을 제공해야 합니다.

```java
public String getCategory(int score) {
    if (score >= 90) {
        return "A";
    } else if (score >= 80) { // 여기서 && score < 90 조건은 불필요합니다.
        return "B";
    } else {
        return "C"; // 다른 모든 경우를 처리합니다.
    }
}
```

### 핵심 요약

"missing return statement" 오류를 피하려면 반환 타입이 있는 메서드를 작성할 때 항상 주의를 기울여야 합니다. 실행 경로가 어떻게 되든 항상 `return` 문에 도달하도록 보장해야 합니다. 이를 위한 간단한 방법은 메서드 본문 마지막에 조건 없는 최종 `return` 문을 두는 것입니다.

## 전문 보완 체크

**Java "error: missing return statement" 해결 방법**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 JDK 버전, 빌드 도구 설정, classpath 또는 module path, 런타임 stack trace를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

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

독자가 **Java "error: missing return statement" 해결 방법**의 첫 번째 권장 조치를 이미 시도했지만 결과가 여전히 불확실하다고 가정해 봅니다. 다음 단계는 여러 해결책을 한꺼번에 시험하는 것이 아니라 짧은 감사 기록을 만드는 것입니다. 먼저 어떤 판단을 하려는지 한 문장으로 쓰고, 환경을 한 문장으로 적고, 관찰된 결과를 한 문장으로 남깁니다. 그다음 JDK 버전, 빌드 도구 설정, classpath 또는 module path, 런타임 stack trace를 이미 확보한 사실과 대조합니다. 이렇게 해야 글이 서로 끊어진 팁 목록이 아니라 검증 가능한 절차가 됩니다.

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
