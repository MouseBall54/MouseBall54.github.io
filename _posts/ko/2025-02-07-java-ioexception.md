---
typora-root-url: ../
layout: single
title: "Java에서 java.io.IOException 이해하고 처리하기"

date: 2025-02-07T07:42:00+09:00
lang: ko
translation_id: java-ioexception
excerpt: "`try-catch` 블록과 `try-with-resources`를 사용하여 I/O 작업이 실패하거나 중단되었음을 알리는 체크 예외 `java.io.IOException`을 처리하는 방법을 알아봅니다."
seo_description: "`try-catch` 블록과 `try-with-resources`를 사용하여 I/O 작업이 실패하거나 중단되었음을 알리는 체크 예외 `java.io.IOException`을 처리하는 방법을 알아봅니다."
header:
   teaser: /images/header_images/overlay_image_java.png
   overlay_image: /images/header_images/overlay_image_java.png
   overlay_filter: 0.5
   image_description: >
     이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Java에서 java.io.IOException 이해하고 처리하기
categories:
  - ko_Troubleshooting
tags:
  - Java
  - IOException
  - Exception Handling
  - File I/O
  - Troubleshooting
---


![이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Java에서 java.io.IOException 이해하고 처리하기](/images/header_images/overlay_image_java.png)
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

## 전문 보완 체크

**Java에서 java.io.IOException 이해하고 처리하기**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 JDK 버전, 빌드 도구 설정, classpath 또는 module path, 런타임 stack trace를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

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

독자가 **Java에서 java.io.IOException 이해하고 처리하기**의 첫 번째 권장 조치를 이미 시도했지만 결과가 여전히 불확실하다고 가정해 봅니다. 다음 단계는 여러 해결책을 한꺼번에 시험하는 것이 아니라 짧은 감사 기록을 만드는 것입니다. 먼저 어떤 판단을 하려는지 한 문장으로 쓰고, 환경을 한 문장으로 적고, 관찰된 결과를 한 문장으로 남깁니다. 그다음 JDK 버전, 빌드 도구 설정, classpath 또는 module path, 런타임 stack trace를 이미 확보한 사실과 대조합니다. 이렇게 해야 글이 서로 끊어진 팁 목록이 아니라 검증 가능한 절차가 됩니다.

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
