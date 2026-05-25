---
typora-root-url: ../
layout: single
title: "Java `java.io.FileNotFoundException` 해결 방법"

date: 2025-02-04T07:39:00+09:00
lang: ko
translation_id: java-filenotfoundexception
excerpt: "파일 경로, 권한을 확인하고 올바른 리소스 처리 방법을 사용하여 `java.io.FileNotFoundException`을 해결하는 방법을 알아봅니다."
seo_description: "파일 경로, 권한을 확인하고 올바른 리소스 처리 방법을 사용하여 `java.io.FileNotFoundException`을 해결하는 방법을 알아봅니다."
header:
   teaser: /images/header_images/overlay_image_java.png
   overlay_image: /images/header_images/overlay_image_java.png
   overlay_filter: 0.5
   image_description: >
     이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Java `java.io.FileNotFoundException` 해결 방법
categories:
  - ko_Troubleshooting
tags:
  - Java
  - Exception
  - File I/O
  - Troubleshooting
---


![이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Java java.io.FileNotFoundException 해결 방법](/images/header_images/overlay_image_java.png)
## `FileNotFoundException`이란?

`java.io.FileNotFoundException`은 Java에서 지정된 경로에 파일이 존재하지 않을 때 접근하려고 시도하면 발생하는 일반적인 체크 예외(checked exception)이다. 파일을 읽거나 쓰려고 할 때 발생할 수 있으며, `IOException`의 하위 클래스이다.

## 일반적인 원인

1.  **잘못된 파일 경로**: 가장 흔한 원인은 파일 경로의 오타나 잘못된 경로 지정이다.
2.  **파일이 존재하지 않음**: 접근하려는 파일이 이동되었거나, 삭제되었거나, 생성된 적이 없다.
3.  **권한 문제**: 애플리케이션이 파일이나 디렉터리에 대한 필요한 읽기/쓰기 권한을 가지고 있지 않다.
4.  **상대 경로 vs. 절대 경로**: 상대 경로와 절대 경로의 혼동으로 인해 프로그램이 잘못된 디렉터리에서 파일을 찾을 수 있다. 상대 경로는 현재 작업 디렉터리를 기준으로 확인된다.

## 해결 방법

### 1. 파일 경로 확인

파일 경로가 올바른지 다시 확인한다. 철자와 디렉터리 구분자에 주의를 기울여야 한다.

```java
// 잘못된 경로
File file = new File("C:\\data\\my_file.txt"); // 오타 확인

// 올바른 경로
File file = new File("C:\\data\\myfile.txt");
```

`file.exists()`와 `file.getAbsolutePath()`를 사용하여 경로 문제를 디버깅할 수 있다.

```java
File file = new File("relative/path/to/file.txt");
System.out.println("접근 시도 경로: " + file.getAbsolutePath());

if (!file.exists()) {
    System.out.println("이 위치에 파일이 존재하지 않습니다.");
}
```

### 2. 파일 권한 확인

애플리케이션이 파일 및 상위 디렉터리에 대한 읽기 또는 쓰기 권한을 가지고 있는지 확인한다. Linux/macOS에서는 `ls -l`을 사용할 수 있고, Windows에서는 파일 속성의 보안 탭에서 확인할 수 있다.

### 3. `try-with-resources`를 사용한 올바른 처리

파일 스트림으로 작업할 때는 항상 `try-with-resources` 문을 사용하여 예외가 발생하더라도 스트림이 자동으로 닫히도록 해야 한다. 이는 리소스 누수를 방지한다.

```java
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;

public class FileReaderExample {
    public static void main(String[] args) {
        File file = new File("path/to/your/file.txt");
        try (FileInputStream fis = new FileInputStream(file)) {
            // 파일 읽기
            int content;
            while ((content = fis.read()) != -1) {
                System.out.print((char) content);
            }
        } catch (FileNotFoundException e) {
            System.err.println("오류: 지정된 경로에서 파일을 찾을 수 없습니다.");
            e.printStackTrace();
        } catch (IOException e) {
            System.err.println("오류: I/O 오류가 발생했습니다.");
            e.printStackTrace();
        }
    }
}
```

### 4. 파일 또는 디렉터리가 없으면 생성하기

애플리케이션이 파일을 생성해야 하는 경우, 파일이 존재하는지 확인하고 존재하지 않으면 생성할 수 있다.

```java
import java.io.File;
import java.io.IOException;

public class FileCreationExample {
    public static void main(String[] args) {
        try {
            File file = new File("path/to/new_file.txt");

            // 상위 디렉터리가 없으면 생성
            File parentDir = file.getParentFile();
            if (!parentDir.exists()) {
                parentDir.mkdirs();
            }

            // 파일이 없으면 생성
            if (file.createNewFile()) {
                System.out.println("파일 생성됨: " + file.getName());
            } else {
                System.out.println("파일이 이미 존재합니다.");
            }
        } catch (IOException e) {
            System.err.println("파일 생성 중 오류가 발생했습니다.");
            e.printStackTrace();
        }
    }
}
```

경로, 권한을 체계적으로 확인하고 강력한 오류 처리를 사용하면 `FileNotFoundException`을 효과적으로 해결할 수 있다.

## 전문 보완 체크

**Java `java.io.FileNotFoundException` 해결 방법**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 JDK 버전, 빌드 도구 설정, classpath 또는 module path, 런타임 stack trace를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

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

독자가 **Java `java.io.FileNotFoundException` 해결 방법**의 첫 번째 권장 조치를 이미 시도했지만 결과가 여전히 불확실하다고 가정해 봅니다. 다음 단계는 여러 해결책을 한꺼번에 시험하는 것이 아니라 짧은 감사 기록을 만드는 것입니다. 먼저 어떤 판단을 하려는지 한 문장으로 쓰고, 환경을 한 문장으로 적고, 관찰된 결과를 한 문장으로 남깁니다. 그다음 JDK 버전, 빌드 도구 설정, classpath 또는 module path, 런타임 stack trace를 이미 확보한 사실과 대조합니다. 이렇게 해야 글이 서로 끊어진 팁 목록이 아니라 검증 가능한 절차가 됩니다.

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
