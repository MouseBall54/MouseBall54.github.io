typora-root-url: ../
layout: single
title: >
   Java try-with-resources로 메모리 누수 방지하기

lang: ko
translation_id: java-try-with-resources
header:
   teaser: /images/header_images/overlay_image_java.png
   overlay_image: /images/header_images/overlay_image_java.png
   overlay_filter: 0.5
excerpt: >
    Java의 try-with-resources 구문을 사용하여 스트림이나 커넥션과 같은 리소스를 자동으로 닫고, 흔한 메모리 누수를 방지하며 코드를 더 깔끔하게 만드는 방법을 알아보세요.
categories:
  - ko_Troubleshooting
tags:
  - Java
  - try-with-resources
  - Memory Management
  - Best Practices
---
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
