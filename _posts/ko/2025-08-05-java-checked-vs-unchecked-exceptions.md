typora-root-url: ../
layout: single
title: >
   Java 예외: Checked Exception vs. Unchecked Exception
date: 2025-08-05T10:25:00+09:00
header:
   teaser: /images/header_images/overlay_image_java.png
   overlay_image: /images/header_images/overlay_image_java.png
   overlay_filter: 0.5
excerpt: >
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
