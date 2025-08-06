---
typora-root-url: ../
layout: single
title: "Java에서 java.io.IOException 이해하고 처리하기"

lang: ko
translation_id: java-ioexception
excerpt: "`try-catch` 블록과 `try-with-resources`를 사용하여 I/O 작업이 실패하거나 중단되었음을 알리는 체크 예외 `java.io.IOException`을 처리하는 방법을 알아봅니다."
header:
   teaser: /images/header_images/overlay_image_java.png
   overlay_image: /images/header_images/overlay_image_java.png
   overlay_filter: 0.5
categories:
  - ko_Troubleshooting
tags:
  - Java
  - IOException
  - Exception Handling
  - File I/O
  - Troubleshooting
---

## `java.io.IOException`이란 무엇인가?

`java.io.IOException`은 실패하거나 중단된 I/O(입출력) 작업을 위한 범용 신호 역할을 하는 Java의 체크 예외(checked exception)이다. 이는 `FileNotFoundException`, `EOFException`, `SocketException`과 같은 다른 많은 특정 I/O 예외의 상위 클래스이다.

체크 예외이므로, I/O 작업을 수행하고 이 예외를 발생시킬 수 있는 모든 메서드는 `try-catch` 블록을 사용하여 처리하거나 `throws` 절에 선언해야 한다.

## 일반적인 원인

`IOException`은 다음과 같은 데이터 전송과 관련된 다양한 이유로 발생할 수 있다:

1.  **파일을 찾을 수 없음**: 존재하지 않는 파일을 읽으려고 시도하는 경우 (종종 하위 클래스인 `FileNotFoundException`으로 신호됨).
2.  **권한 거부**: 파일이나 디렉터리를 읽거나 쓸 수 있는 필요한 권한이 없는 경우.
3.  **디스크 공간 부족**: 공간이 없는 디스크에 쓰려고 시도하는 경우.
4.  **네트워크 문제**: 네트워크 I/O 중에 네트워크 연결이 끊어지거나, 원격 서버를 사용할 수 없거나, 방화벽이 연결을 차단하는 경우.
5.  **스트림이 닫힘**: 이미 닫힌 스트림에서 읽거나 쓰려고 시도하는 경우.
6.  **하드웨어 오류**: 물리적 I/O 장치(예: 하드 드라이브 또는 네트워크 카드)가 실패하는 경우.

## 해결 방법

`IOException`을 올바르게 처리하는 것은 I/O 실패를 정상적으로 관리할 수 있는 강력한 애플리케이션을 구축하는 데 중요하다.

### 1. `try-catch` 블록 사용

`IOException`을 처리하는 가장 직접적인 방법은 I/O 코드를 `try-catch` 블록으로 감싸는 것이다.

```java
import java.io.FileReader;
import java.io.IOException;

public class IoExceptionExample {
    public void readFile(String filePath) {
        FileReader reader = null;
        try {
            reader = new FileReader(filePath);
            int character;
            while ((character = reader.read()) != -1) {
                System.out.print((char) character);
            }
        } catch (IOException e) {
            // 예외 처리 (예: 로그 기록, 사용자 친화적인 메시지 표시)
            System.err.println("I/O 오류가 발생했습니다: " + e.getMessage());
            e.printStackTrace();
        } finally {
            // 리소스가 항상 닫히도록 보장
            if (reader != null) {
                try {
                    reader.close();
                } catch (IOException e) {
                    System.err.println("리더를 닫지 못했습니다: " + e.getMessage());
                }
            }
        }
    }
}
```

여기서 `finally` 블록은 리소스 누수를 방지하기 위해 `FileReader`가 닫히도록 보장하는 데 필수적이다.

### 2. `try-with-resources` 문 사용 (권장)

Java 7에 도입된 `try-with-resources` 문은 스트림과 같은 리소스를 처리하는 더 우아하고 안전한 방법이다. `java.lang.AutoCloseable` 인터페이스를 구현하는 모든 리소스를 자동으로 닫아 코드를 크게 단순화하고 리소스 누수 위험을 줄인다.

```java
import java.io.FileReader;
import java.io.IOException;

public class TryWithResourcesExample {
    public void readFile(String filePath) {
        // FileReader가 자동으로 닫힘
        try (FileReader reader = new FileReader(filePath)) {
            int character;
            while ((character = reader.read()) != -1) {
                System.out.print((char) character);
            }
        } catch (IOException e) {
            // 예외 처리
            System.err.println("I/O 오류가 발생했습니다: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
```

이 현대적인 접근 방식은 `finally` 블록을 사용하는 것보다 덜 장황하고 오류 발생 가능성이 적다.

### 3. `throws`로 예외 선언

현재 메서드에서 예외를 처리하는 것이 적절하지 않은 경우, `throws` 키워드를 사용하여 메서드 시그니처에 예외를 선언할 수 있다. 이는 예외 처리 책임을 호출하는 메서드에 넘긴다.

```java
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

public class ThrowsExample {
    // 메서드가 IOException을 발생시킬 수 있음을 선언
    public String readFileAsString(String filePath) throws IOException {
        return new String(Files.readAllBytes(Paths.get(filePath)));
    }

    public void processFile() {
        try {
            String content = readFileAsString("my-file.txt");
            System.out.println(content);
        } catch (IOException e) {
            // 호출하는 메서드가 처리해야 함
            System.err.println("파일 처리 실패: " + e.getMessage());
        }
    }
}
```

`try-catch`로 직접 처리하거나 `throws`로 위임하는 등 적절한 전략을 선택하여 `IOException`을 효과적으로 관리하고 복원력 있는 Java 애플리케이션을 구축할 수 있다.
