---
typora-root-url: ../
layout: single
title: >
   Java에서 IllegalArgumentException 처리하는 방법

date: 2025-03-30T07:48:00+09:00
lang: ko
translation_id: java-error-illegalargumentexception
header:
   teaser: /images/header_images/overlay_image_java.png
   overlay_image: /images/header_images/overlay_image_java.png
   overlay_filter: 0.5
   image_description: >
     이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Java에서 IllegalArgumentException 처리하는 방법
excerpt: >
    IllegalArgumentException이 무엇인지, 왜 발생하는지, 그리고 메서드 인자를 검증하고 코드의 견고성을 향상시키기 위해 효과적으로 사용하는 방법을 알아보세요.
seo_description: >
    IllegalArgumentException이 무엇인지, 왜 발생하는지, 그리고 메서드 인자를 검증하고 코드의 견고성을 향상시키기 위해 효과적으로 사용하는 방법을 알아보세요.
categories:
  - ko_Troubleshooting
tags:
  - Java
  - Exceptions
  - IllegalArgumentException
  - Best Practices
---

![이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Java에서 IllegalArgumentException 처리하는 방법](/images/header_images/overlay_image_java.png)
## `IllegalArgumentException`이란 무엇인가?

`IllegalArgumentException`은 메서드에 부적절하거나 잘못된 인수가 전달되었음을 나타내기 위해 발생하는 Java의 **unchecked exception**입니다. 이것은 `RuntimeException`의 하위 클래스로, 컴파일러가 `try-catch` 블록이나 `throws` 절로 처리하도록 강제하지 않는다는 의미입니다.

이 예외는 메서드와 호출자 사이의 규약을 강제하는 중요한 도구입니다. 호출자가 메서드 사용의 전제 조건을 위반했음을 알리는 신호입니다.

### 언제 그리고 왜 발생하는가?

호출자가 메서드의 정의에 따라 유효하지 않은 인수를 전달했을 때 수동으로 `IllegalArgumentException`을 발생시켜야 합니다. 이는 메서드 시작 부분에서 **인수 검증**을 수행하는 방법입니다.

일반적인 시나리오는 다음과 같습니다:
- 값이 예상 범위를 벗어날 때 (예: 나이에 음수 값).
- 객체가 유효하지 않은 상태일 때.
- 문자열이 필수 형식과 일치하지 않을 때.
- 인수가 `null`이 아니어야 할 때 `null`일 경우 (이 경우에는 `NullPointerException`이 더 구체적일 때가 많습니다).

이 예외를 조기에 발생시킴으로써, 유효하지 않은 데이터로 메서드가 계속 진행되는 것을 막을 수 있으며, 이는 나중에 더 모호한 오류나 잘못된 동작으로 이어질 수 있습니다.

### `IllegalArgumentException`을 발생시키는 방법

사용자의 나이를 설정하는 메서드 예제를 살펴보겠습니다. 나이는 음수가 아닌 정수여야 합니다.

```java
public class User {
    private String name;
    private int age;

    public void setAge(int age) {
        if (age < 0) {
            // 나이가 유효하지 않으면 예외를 발생시킵니다.
            throw new IllegalArgumentException("Age cannot be negative. Received: " + age);
        }
        this.age = age;
    }
    // 다른 메서드들...
}
```

이 예제에서:
1.  `setAge` 메서드는 먼저 `age` 매개변수를 검증합니다.
2.  `age`가 0보다 작으면, 설명적인 메시지와 함께 새로운 `IllegalArgumentException`을 생성합니다.
3.  `throw` 키워드는 즉시 메서드 실행을 중단하고 예외를 호출 스택 위로 전달합니다.

오류 메시지는 중요합니다. 메서드를 사용하는 개발자가 문제를 쉽게 디버깅할 수 있도록 인수에 무엇이 잘못되었는지 명확하게 설명해야 합니다.

### `IllegalArgumentException`을 처리하는 방법

`IllegalArgumentException`은 unchecked exception이므로, 이를 잡을 의무는 없습니다. 이것은 일반적으로 호출자 측의 **프로그래밍 오류**를 나타냅니다. 이를 "처리"하는 가장 좋은 방법은 호출 코드를 수정하여 유효하지 않은 인수를 절대 전달하지 않도록 하는 것입니다.

예를 들어, `setAge`를 호출하는 코드는 다음과 같이 수정되어야 합니다.

**잘못된 호출 코드 (버그):**
```java
User user = new User();
int ageFromUserInput = -5; // 이것은 검증되었어야 합니다.
user.setAge(ageFromUserInput); // IllegalArgumentException 발생
```

**수정된 호출 코드:**
```java
User user = new User();
int ageFromUserInput = -5;

// 메서드를 호출하기 전에 입력을 검증합니다.
if (ageFromUserInput >= 0) {
    user.setAge(ageFromUserInput);
} else {
    System.err.println("Invalid age entered. Please provide a valid age.");
}
```

드물게, 완전히 제어할 수 없는 외부 입력으로 인해 유효하지 않은 인수가 들어오는 경우와 같이 이를 잡고 싶을 때도 있습니다.

```java
try {
    int age = Integer.parseInt(userInput);
    user.setAge(age);
} catch (IllegalArgumentException e) {
    // 오류를 기록하고 사용자에게 알립니다.
    System.err.println("Error: " + e.getMessage());
    // 다시 입력을 요청합니다.
}
```

### `IllegalArgumentException` vs. `IllegalStateException`

`IllegalArgumentException`을 `IllegalStateException`과 혼동하지 않는 것이 중요합니다.

- **`IllegalArgumentException`**: 문제는 호출자에 의해 메서드*로* 전달된 인수에 있습니다.
- **`IllegalStateException`**: 문제는 메서드가 호출된 *객체의 상태*에 있습니다. 인수는 유효할 수 있지만, 객체가 해당 작업을 수행하기에 적절한 상태가 아닌 경우입니다.

**`IllegalStateException`의 예시:**
```java
public class Connection {
    private boolean isOpen = false;

    public void sendData(String data) {
        if (!isOpen) {
            throw new IllegalStateException("Connection is not open. Cannot send data.");
        }
        // ... 데이터 전송
    }
    // ... 열기/닫기 위한 다른 메서드들
}
```

### 핵심 요약

`IllegalArgumentException`을 사용하여 메서드를 견고하고 자체적으로 문서화되도록 만드세요. 메서드 시작 시 인수를 검증하고 이 예외를 발생시킴으로써, 잘못된 사용에 대한 즉각적이고 명확한 피드백을 제공하여 버그를 예방하고 코드를 더 쉽게 유지보수할 수 있도록 돕습니다.

## 전문 보완 체크

**Java에서 IllegalArgumentException 처리하는 방법**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 JDK 버전, 빌드 도구 설정, classpath 또는 module path, 런타임 stack trace를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

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

독자가 **Java에서 IllegalArgumentException 처리하는 방법**의 첫 번째 권장 조치를 이미 시도했지만 결과가 여전히 불확실하다고 가정해 봅니다. 다음 단계는 여러 해결책을 한꺼번에 시험하는 것이 아니라 짧은 감사 기록을 만드는 것입니다. 먼저 어떤 판단을 하려는지 한 문장으로 쓰고, 환경을 한 문장으로 적고, 관찰된 결과를 한 문장으로 남깁니다. 그다음 JDK 버전, 빌드 도구 설정, classpath 또는 module path, 런타임 stack trace를 이미 확보한 사실과 대조합니다. 이렇게 해야 글이 서로 끊어진 팁 목록이 아니라 검증 가능한 절차가 됩니다.

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
