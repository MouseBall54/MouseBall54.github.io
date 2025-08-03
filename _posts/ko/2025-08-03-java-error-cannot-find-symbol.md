---
typora-root-url: ../
layout: single
title: >
    자바 Error: cannot find symbol 해결 방법 (가장 흔한 오류)
date: 2025-08-03T10:50:00+09:00
header:
   teaser: /images/header_images/overlay_image_java.png
   overlay_image: /images/header_images/overlay_image_java.png
   overlay_filter: 0.5
excerpt: >
    자바 컴파일 시 가장 흔하게 발생하는 `cannot find symbol` 오류의 다양한 원인(오타, 임포트 누락, 스코프 문제 등)과 해결책을 알아봅니다.
categories:
  - ko_Troubleshooting
tags:
  - Java
  - Compilation Error
  - cannot find symbol
  - import
  - scope
---

## 문제 상황

`Error: cannot find symbol`은 자바 개발자가 가장 흔하게 마주치는 컴파일 오류 중 하나입니다. 이 오류는 컴파일러가 코드에 사용된 식별자(identifier)를 찾을 수 없을 때 발생합니다. 여기서 '심볼(symbol)'은 변수, 메서드, 클래스, 인터페이스 등의 이름을 의미합니다.

컴파일러가 특정 심볼의 선언을 찾지 못하면, 그 심볼이 무엇인지, 어떤 타입인지 알 수 없으므로 코드를 바이트코드로 변환할 수 없습니다. 오류 메시지는 보통 다음과 같은 형식을 가집니다.

```
<FileName>.java:<LineNumber>: error: cannot find symbol
  symbol:   <symbol_type> <symbol_name>
  location: <location_where_error_occurred>
```

## 오류 발생 원인과 해결 방법

이 오류의 원인은 다양하지만, 대부분 몇 가지 간단한 실수에 기인합니다.

### 1. 오타 (Typo)

가장 흔한 원인입니다. 변수나 메서드, 클래스의 이름을 잘못 입력한 경우입니다. 특히 대소문자 구분에 유의해야 합니다.

-   **오류 코드:**
    ```java
    public class Main {
        public static void main(String[] args) {
            String myMessage = "Hello";
            System.out.println(myMssage); // 'myMessage'를 'myMssage'로 잘못 입력
        }
    }
    ```
-   **해결책:** `myMssage`를 `myMessage`로 올바르게 수정합니다. 심볼의 철자와 대소문자를 꼼꼼히 확인하세요.

### 2. 클래스 임포트(import) 누락

다른 패키지에 있는 클래스를 사용하면서 `import` 구문을 추가하지 않은 경우입니다.

-   **오류 코드:**
    ```java
    public class Main {
        public static void main(String[] args) {
            // ArrayList는 java.util 패키지에 있으나 import하지 않음
            ArrayList<String> list = new ArrayList<>();
            list.add("test");
        }
    }
    ```
-   **해결책:** 파일 상단에 필요한 클래스를 임포트하는 구문을 추가합니다.
    ```java
    import java.util.ArrayList; // 이 줄을 추가
    
    public class Main {
        // ...
    }
    ```
    대부분의 IDE(통합 개발 환경)는 `Alt+Enter` 또는 `Ctrl+Space` 등의 단축키로 자동 임포트 기능을 제공합니다.

### 3. 변수의 유효 범위(Scope) 문제

변수가 선언된 코드 블록(`{ }`) 밖에서 해당 변수에 접근하려고 할 때 발생합니다.

-   **오류 코드:**
    ```java
    public class Main {
        public static void main(String[] args) {
            for (int i = 0; i < 5; i++) {
                String message = "Count: " + i;
            }
            // 'message' 변수는 for 루프 안에서만 유효합니다.
            System.out.println(message); // 여기서 'message'를 찾을 수 없음
        }
    }
    ```
-   **해결책:** 변수를 사용하려는 범위보다 더 넓은 범위에서 선언해야 합니다.
    ```java
    public class Main {
        public static void main(String[] args) {
            String message = ""; // main 메서드 범위에서 선언
            for (int i = 0; i < 5; i++) {
                message = "Count: " + i;
            }
            System.out.println(message);
        }
    }
    ```

### 4. 잘못된 라이브러리/클래스패스 설정

외부 라이브러리(.jar 파일)를 사용하지만, 프로젝트의 빌드 경로(classpath)에 해당 라이브러리를 추가하지 않은 경우에도 이 오류가 발생할 수 있습니다.

-   **해결책:**
    -   **Maven/Gradle 사용자:** `pom.xml`이나 `build.gradle` 파일에 의존성(dependency)이 올바르게 추가되었는지 확인하고 프로젝트를 다시 빌드합니다.
    -   **IDE 사용자:** 프로젝트 설정에서 빌드 경로(Build Path) 또는 라이브러리(Libraries) 항목에 해당 `.jar` 파일이 제대로 포함되었는지 확인합니다.

## 결론

`cannot find symbol` 오류는 당황하기 쉽지만, 원인은 명확한 경우가 많습니다. 오류가 발생하면 다음 사항들을 순서대로 점검해 보세요.

1.  **오타 확인**: 변수, 메서드, 클래스 이름의 철자와 대소문자를 확인합니다.
2.  **`import` 문 확인**: 사용하려는 클래스가 제대로 임포트되었는지 확인합니다.
3.  **유효 범위(Scope) 확인**: 변수가 선언된 블록 안에서만 사용되고 있는지 확인합니다.
4.  **라이브러리 설정 확인**: 외부 라이브러리를 사용한다면 빌드 경로에 잘 추가되었는지 확인합니다.

이러한 기본적인 사항들을 확인하는 것만으로도 대부분의 `cannot find symbol` 오류를 해결할 수 있습니다.
