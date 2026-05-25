---
typora-root-url: ../
layout: single
title: >
   Java "error: unreachable statement" 해결 방법

date: 2025-04-01T07:50:00+09:00
lang: ko
translation_id: java-error-unreachable-statement
header:
   teaser: /images/header_images/overlay_image_java.png
   overlay_image: /images/header_images/overlay_image_java.png
   overlay_filter: 0.5
   image_description: >
     이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Java "error: unreachable statement" 해결 방법
excerpt: >
    절대 실행될 수 없는 코드가 있을 때 발생하는 Java의 "unreachable statement" 컴파일 시간 오류의 원인을 이해하고 해결하는 방법을 알아보세요.
seo_description: >
    절대 실행될 수 없는 코드가 있을 때 발생하는 Java의 "unreachable statement" 컴파일 시간 오류의 원인을 이해하고 해결하는 방법을 알아보세요.
categories:
  - ko_Troubleshooting
tags:
  - Java
  - Compilation Error
  - Unreachable Code
  - Troubleshooting
---

![이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Java "error: unreachable statement" 해결 방법](/images/header_images/overlay_image_java.png)
## "unreachable statement" 오류 이해하기

"error: unreachable statement"는 Java의 컴파일 시간 오류로, 코드에 절대 실행될 수 없는 문장이 있음을 나타냅니다. Java 언어 명세는 모든 문장이 도달 가능해야 한다고 요구합니다. 만약 도달할 수 없는 코드가 있다면, 이는 종종 잘못된 로직을 가리키는 프로그래밍 오류로 간주됩니다.

이 오류는 개발자가 죽은 코드(dead code)를 찾아 제거하여 프로그램을 더 깨끗하고 이해하기 쉽게 만드는 데 도움을 줍니다.

### 일반적인 시나리오와 해결책

이 오류를 유발하는 일반적인 상황들을 살펴보겠습니다.

#### 1. `return` 문 뒤에 오는 코드

`return` 문은 메서드에서 즉시 빠져나가게 하므로, 같은 블록 내에서 `return` 문 뒤에 있는 모든 코드는 도달할 수 없습니다.

**잘못된 코드:**
```java
public int getValue() {
    return 10;
    System.out.println("This will never be printed."); // 도달할 수 없는 코드
}
```

**해결책:**
도달할 수 없는 코드를 제거하거나, 실행되어야 하는 코드라면 `return` 문 앞으로 옮깁니다.

```java
public int getValue() {
    System.out.println("This will be printed.");
    return 10;
}
```

#### 2. `throw` 또는 `break` 뒤에 오는 코드

`return`과 유사하게, 제어를 무조건적으로 이전하는 문장들은 같은 블록 내의 후속 코드를 도달할 수 없게 만듭니다.

**`throw` 다음:**
```java
public void checkValue(int value) {
    if (value < 0) {
        throw new IllegalArgumentException("Value cannot be negative.");
        System.out.println("Error logged."); // 도달할 수 없는 코드
    }
}
```

**반복문 안의 `break` 다음:**
```java
public void findFirstItem() {
    while (true) {
        System.out.println("Found item.");
        break;
        System.out.println("This is unreachable."); // 도달할 수 없는 코드
    }
}
```

**해결책:**
의도된 코드 경로만 존재하도록 코드를 재구성해야 합니다. 실행되어야 하는 로직은 제어 이전 문장 앞에 위치해야 합니다.

```java
public void checkValue(int value) {
    if (value < 0) {
        System.out.println("Error logged."); // throw 앞으로 옮깁니다.
        throw new IllegalArgumentException("Value cannot be negative.");
    }
}
```

#### 3. 무한 루프

컴파일러가 루프가 무한하다고 판단할 수 있는 경우, 해당 루프 바로 다음에 오는 모든 코드는 도달할 수 없는 것으로 표시됩니다.

**잘못된 코드:**
```java
public void runForever() {
    while (true) {
        // 이 루프는 절대 끝나지 않습니다.
    }
    System.out.println("This is unreachable."); // 도달할 수 없는 코드
}
```
`for` 루프 또한 무한 루프가 될 수 있습니다.
```java
public void anotherInfiniteLoop() {
    for (;;) {
        // 무한 루프
    }
    System.out.println("Also unreachable."); // 도달할 수 없는 코드
}
```

**해결책:**
만약 무한 루프가 의도된 것(예: 지속적으로 연결을 수신 대기하는 서버 애플리케이션)이라면, 그 뒤에 오는 코드는 실수일 가능성이 높으므로 제거해야 합니다. 루프가 무한이 아니어야 한다면, 루프를 종료할 수 있는 `break` 문이나 조건을 추가해야 합니다.

```java
public void runWithCondition(int limit) {
    int i = 0;
    while (true) {
        i++;
        if (i > limit) {
            break; // 이 구문이 루프를 종료시킵니다.
        }
    }
    System.out.println("This is now reachable."); // 이제 도달 가능합니다.
}
```

### 핵심 요약

"unreachable statement" 오류는 컴파일러가 코드의 일부 로직에 결함이 있음을 알려주는 신호입니다. 절대 실행될 수 없는 문장을 검토하고 제거하라는 의미입니다. 항상 제어 흐름 문장(`return`, `throw`, `break`, `continue`)이 올바르게 배치되었는지, 그리고 루프에 명확한 종료 조건이 있는지 확인하세요.

## 전문 보완 체크

**Java "error: unreachable statement" 해결 방법**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 JDK 버전, 빌드 도구 설정, classpath 또는 module path, 런타임 stack trace를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

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

독자가 **Java "error: unreachable statement" 해결 방법**의 첫 번째 권장 조치를 이미 시도했지만 결과가 여전히 불확실하다고 가정해 봅니다. 다음 단계는 여러 해결책을 한꺼번에 시험하는 것이 아니라 짧은 감사 기록을 만드는 것입니다. 먼저 어떤 판단을 하려는지 한 문장으로 쓰고, 환경을 한 문장으로 적고, 관찰된 결과를 한 문장으로 남깁니다. 그다음 JDK 버전, 빌드 도구 설정, classpath 또는 module path, 런타임 stack trace를 이미 확보한 사실과 대조합니다. 이렇게 해야 글이 서로 끊어진 팁 목록이 아니라 검증 가능한 절차가 됩니다.

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
