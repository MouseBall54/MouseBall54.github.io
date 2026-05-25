---
typora-root-url: ../
layout: single
title: >
   Java try-with-resources로 메모리 누수 방지하기

date: 2025-04-07T07:11:00+09:00
lang: ko
translation_id: java-try-with-resources
header:
   teaser: /images/header_images/overlay_image_java.png
   overlay_image: /images/header_images/overlay_image_java.png
   overlay_filter: 0.5
   image_description: >
     이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Java try-with-resources로 메모리 누수 방지하기
excerpt: >
    Java의 try-with-resources 구문을 사용하여 스트림이나 커넥션과 같은 리소스를 자동으로 닫고, 흔한 메모리 누수를 방지하며 코드를 더 깔끔하게 만드는 방법을 알아보세요.
seo_description: >
    Java의 try-with-resources 구문을 사용하여 스트림이나 커넥션과 같은 리소스를 자동으로 닫고, 흔한 메모리 누수를 방지하며 코드를 더 깔끔하게 만드는 방법을 알아보세요.
categories:
  - ko_Troubleshooting
tags:
  - Java
  - try-with-resources
  - Memory Management
  - Best Practices
---

![이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Java try-with-resources로 메모리 누수 방지하기](/images/header_images/overlay_image_java.png)
## 문제점: 리소스 누수

Java에서 파일 스트림, 데이터베이스 커넥션, 네트워크 소켓과 같은 외부 리소스를 사용할 때는 작업이 끝나면 명시적으로 닫아야 합니다. 만약 그렇게 하지 않으면 리소스가 계속 열려 있어 시스템 메모리나 데이터베이스 커넥션을 소모하게 됩니다. 이를 **리소스 누수(resource leak)**라고 하며, 결국 `OutOfMemoryError`나 다른 심각한 장애를 일으켜 애플리케이션을 중단시킬 수 있습니다.

### 과거의 방식: `finally` 블록

Java 7 이전에는 리소스가 반드시 닫히도록 보장하는 표준적인 방법이 `finally` 블록을 사용하는 것이었습니다. 이 패턴은 장황하고 오류가 발생하기 쉽습니다.

**전통적인 `finally` 블록:**
```java
FileReader reader = null;
try {
    reader = new FileReader("file.txt");
    // ... reader로 작업 수행
} catch (IOException e) {
    // 예외 처리
} finally {
    if (reader != null) {
        try {
            reader.close(); // 이 또한 IOException을 던질 수 있습니다.
        } catch (IOException e) {
            // close 예외 처리
        }
    }
}
```

이 코드는 다루기 불편합니다. `close()` 메서드 자체가 `IOException`을 던질 수 있기 때문에, `close()` 호출이 또 다른 `try-catch` 블록 안에 중첩되어 있습니다. 이는 코드를 읽고 유지보수하기 어렵게 만듭니다.

## 해결책: `try-with-resources`

Java 7에서는 이 과정을 단순화하기 위해 `try-with-resources` 구문을 도입했습니다. 이 구문은 `java.lang.AutoCloseable` 또는 `java.io.Closeable` 인터페이스를 구현하는 모든 리소스를 자동으로 닫아줍니다.

### 작동 방식

`try` 키워드 뒤의 괄호 안에 리소스를 선언합니다. 그러면 Java 런타임은 `try` 블록이 정상적으로 완료되든 예외가 발생하든 상관없이 블록의 끝에서 해당 리소스의 `close()` 메서드가 호출될 것을 보장합니다.

**`try-with-resources` 예시:**
```java
import java.io.FileReader;
import java.io.IOException;

public void readFile() {
    try (FileReader reader = new FileReader("file.txt")) {
        // ... reader로 작업 수행
        // reader는 여기서 자동으로 닫힙니다!
    } catch (IOException e) {
        // FileReader 생성자나 읽기 작업에서 발생한 예외 처리
    }
}
```

이 코드는 훨씬 더 깔끔하고 안전합니다:
- **간결함:** `finally` 블록이나 null 확인이 필요 없습니다.
- **안전함:** 리소스가 반드시 닫힘을 보장합니다.
- **억제된 예외:** `try` 블록 내부에서 예외가 발생하고 `close()` 메서드에서도 또 다른 예외가 발생하면, `close()` 메서드의 예외는 *억제됩니다*. 주된 예외가 전파되는데, 보통 이것이 원하는 동작입니다.

### 여러 리소스 사용하기

세미콜론으로 구분하여 `try-with-resources` 구문 안에 여러 리소스를 선언할 수 있습니다. 리소스들은 생성된 순서의 역순으로 닫힙니다.

```java
import java.io.FileInputStream;
import java.io.BufferedInputStream;
import java.io.IOException;

public void readMultipleFiles() {
    try (FileInputStream fis = new FileInputStream("file1.txt");
         BufferedInputStream bis = new BufferedInputStream(fis)) {
        // bis로 작업 수행
        // bis가 먼저 닫히고, 그 다음 fis가 닫힙니다.
    } catch (IOException e) {
        // 예외 처리
    }
}
```

### `try-with-resources`와 함께 사용할 수 있는 것은?

`java.lang.AutoCloseable`을 구현하는 모든 객체를 사용할 수 있습니다. 이 인터페이스는 `void close() throws Exception`이라는 단일 메서드를 가집니다. `InputStream`, `OutputStream`, `Reader`, `Writer`, `java.sql.Connection`, `Statement`, `ResultSet`과 같이 닫아야 하는 대부분의 표준 Java 리소스가 이 인터페이스를 구현합니다.

또한, 직접 만든 클래스에서 `AutoCloseable`을 구현하여 `try-with-resources` 구문에서 사용할 수 있도록 할 수 있습니다.

```java
class MyResource implements AutoCloseable {
    public MyResource() {
        System.out.println("리소스 생성됨.");
    }

    public void doWork() {
        System.out.println("작업 수행 중.");
    }

    @Override
    public void close() {
        System.out.println("리소스 닫힘.");
    }
}

// 사용법
public void useCustomResource() {
    try (MyResource res = new MyResource()) {
        res.doWork();
    }
    // "리소스 생성됨.", "작업 수행 중.", "리소스 닫힘."이 출력됩니다.
}
```

### 핵심 요약

닫아야 하는 리소스를 다룰 때는 항상 `try-with-resources` 구문을 사용하세요. 이것은 Java에서 리소스를 관리하는 현대적이고 안전하며 선호되는 방식으로, 효과적으로 리소스 누수를 방지하고 코드를 단순화합니다.

## 전문 보완 체크

**Java try-with-resources로 메모리 누수 방지하기**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 JDK 버전, 빌드 도구 설정, classpath 또는 module path, 런타임 stack trace를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

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

독자가 **Java try-with-resources로 메모리 누수 방지하기**의 첫 번째 권장 조치를 이미 시도했지만 결과가 여전히 불확실하다고 가정해 봅니다. 다음 단계는 여러 해결책을 한꺼번에 시험하는 것이 아니라 짧은 감사 기록을 만드는 것입니다. 먼저 어떤 판단을 하려는지 한 문장으로 쓰고, 환경을 한 문장으로 적고, 관찰된 결과를 한 문장으로 남깁니다. 그다음 JDK 버전, 빌드 도구 설정, classpath 또는 module path, 런타임 stack trace를 이미 확보한 사실과 대조합니다. 이렇게 해야 글이 서로 끊어진 팁 목록이 아니라 검증 가능한 절차가 됩니다.

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
