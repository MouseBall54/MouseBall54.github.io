---
typora-root-url: ../
layout: single
title: >
   Java 예외: Checked Exception vs. Unchecked Exception

date: 2025-03-27T07:45:00+09:00
lang: ko
translation_id: java-checked-vs-unchecked-exceptions
header:
   teaser: /images/header_images/overlay_image_java.png
   overlay_image: /images/header_images/overlay_image_java.png
   overlay_filter: 0.5
   image_description: >
     이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Java 예외: Checked Exception vs. Unchecked Exception
excerpt: >
    Java의 checked exception과 unchecked exception의 차이점, 사용 시기, 그리고 코드 설계와 안정성에 미치는 영향을 알아보세요.
seo_description: >
    Java의 checked exception과 unchecked exception의 차이점, 사용 시기, 그리고 코드 설계와 안정성에 미치는 영향을 알아보세요.
categories:
  - ko_Troubleshooting
tags:
  - Java
  - Exceptions
  - Checked Exception
  - Unchecked Exception
  - Best Practices
---

![이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Java 예외: Checked Exception vs. Unchecked Exception](/images/header_images/overlay_image_java.png)
## Java의 예외 계층 구조 이해하기

Java에서 모든 예외와 에러 타입은 `Throwable` 클래스의 하위 클래스입니다. 이 클래스는 두 개의 주요 직접 하위 클래스인 `Error`와 `Exception`을 가집니다.

- **`Error`**: `OutOfMemoryError`나 `StackOverflowError`와 같이 합리적인 애플리케이션이 잡으려고 시도해서는 안 되는 심각한 문제를 나타냅니다. 이들은 거의 항상 복구 불가능합니다.
- **`Exception`**: 합리적인 애플리케이션이 잡고 싶어 할 수 있는 조건을 나타냅니다. 이것이 우리가 예외 처리에서 집중하는 클래스입니다.

`Exception` 클래스 자체는 **checked exception**과 **unchecked exception**이라는 두 가지 카테고리의 예외에 대한 부모입니다.

![Java 예외 계층 구조](https://i.imgur.com/s5l4VjD.png)
*(예외 계층 구조의 단순화된 다이어그램)*

### Checked Exceptions (확인된 예외)

**Checked exception**은 Java 컴파일러가 컴파일 시점에 *확인하는* 예외입니다. 이들은 `Exception`의 하위 클래스이지만 `RuntimeException`을 상속하지는 않습니다.

- **규칙:** 메서드가 checked exception을 던질 수 있다면, 반드시 `try-catch` 블록을 사용하여 처리하거나 `throws` 키워드를 사용하여 시그니처에 선언해야 합니다.
- **목적:** 외부 조건으로 인해 발생하는 예측 가능하지만 예방할 수 없는 문제에 사용됩니다. 메서드의 호출자는 이러한 실패 시나리오를 어떻게 처리할지 강제로 고려하게 됩니다.
- **예시:**
  - `IOException`: I/O 작업 중 오류가 발생했을 때 (예: 존재하지 않는 파일 읽기).
  - `SQLException`: 데이터베이스와 상호작용하는 동안 오류가 발생했을 때.
  - `ClassNotFoundException`: 런타임에 필요한 클래스를 찾을 수 없을 때.

**예시:**
```java
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

public void readFile(String fileName) throws IOException { // 예외 선언
    File file = new File(fileName);
    FileReader reader = new FileReader(file);
    // ... 파일 읽기
}

public void processFile() {
    try {
        readFile("my-file.txt"); // 예외 처리
    } catch (IOException e) {
        System.err.println("Failed to read file: " + e.getMessage());
    }
}
```

### Unchecked Exceptions (미확인 예외)

**Unchecked exception**은 컴파일러가 컴파일 시점에 *확인하지 않는* 예외입니다. Java에서는 이들 모두 `RuntimeException`의 하위 클래스입니다.

- **규칙:** unchecked exception을 처리하거나 선언할 의무가 없습니다.
- **목적:** 일반적으로 코드의 버그와 같은 프로그래밍 오류나 논리적 결함을 나타냅니다. 이는 런타임에 처리하기보다는 이상적으로는 수정되어야 할 문제입니다.
- **예시:**
  - `NullPointerException`: `null` 객체 참조의 멤버에 접근하려고 할 때.
  - `ArrayIndexOutOfBoundsException`: 배열에 잘못된 인덱스를 사용하여 접근할 때.
  - `IllegalArgumentException`: 메서드에 유효하지 않은 인수를 전달했을 때.
  - `NumberFormatException`: 숫자가 아닌 문자열을 숫자로 변환하려고 할 때.

**예시:**
```java
public void printLength(String text) {
    // NullPointerException을 선언할 필요 없음
    // 호출자는 유효하고 null이 아닌 문자열을 전달할 것으로 예상됨
    System.out.println(text.length()); 
}

public void run() {
    // 호출 코드는 try-catch를 사용하도록 강제되지 않음
    printLength(null); // 이것은 런타임에 NullPointerException을 던질 것임
}
```

### 주요 차이점 요약

| 기능             | Checked Exception                               | Unchecked Exception (RuntimeException)          |
| ------------------- | ----------------------------------------------- | ----------------------------------------------- |
| **컴파일러 확인**  | 예 (컴파일 시점에 확인됨)                   | 아니요 (컴파일 시점에 확인되지 않음)                |
| **처리**        | 반드시 처리(`try-catch`)하거나 선언(`throws`)해야 함 | 처리 또는 선언이 선택 사항임                 |
| **부모 클래스**    | `Exception` (단, `RuntimeException`은 아님)        | `RuntimeException`                              |
| **나타내는 것**      | 복구 가능한 외부 조건 (예: I/O)     | 프로그래밍 오류/버그 (예: null 포인터)    |
| **예시**         | `IOException`, `SQLException`                   | `NullPointerException`, `IndexOutOfBoundsException` |

### 언제 무엇을 사용해야 할까?

- **Checked exception 사용:** 호출자가 현실적으로 복구할 수 있을 것으로 예상되는 조건에 사용합니다. 클라이언트가 유용한 복구 조치를 취할 수 있다면 checked exception이 좋은 선택입니다. 예를 들어, 파일을 찾을 수 없는 경우 사용자에게 다른 파일 이름을 입력하라는 메시지를 표시할 수 있습니다.
- **Unchecked exception 사용:** 프로그래밍 오류를 나타내는 데 사용합니다. `NullPointerException`은 호출자가 잡아서 처리하기보다는 코드에서 수정되어야 할 버그(예: null 확인 추가)를 시사합니다.

이 차이점을 이해함으로써 Java에서 더 견고하고 유지보수하기 좋은 API와 애플리케이션을 설계할 수 있습니다.

## 전문 보완 체크

**Java 예외: Checked Exception vs. Unchecked Exception**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 JDK 버전, 빌드 도구 설정, classpath 또는 module path, 런타임 stack trace를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

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
