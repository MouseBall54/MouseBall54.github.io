---
typora-root-url: ../
layout: single
title: >
    Java "Error: cannot find symbol" 해결 방법

lang: ko
translation_id: java-error-cannot-find-symbol
header:
    teaser: /images/header_images/overlay_image_java.png
    overlay_image: /images/header_images/overlay_image_java.png
    overlay_filter: 0.5
excerpt: >
    Java에서 "cannot find symbol"은 컴파일러가 코드에서 사용된 식별자(변수, 메서드, 클래스 등)를 찾을 수 없을 때 발생하는 매우 흔한 컴파일 오류입니다. 이 글에서는 원인과 해결 방법을 알아봅니다.
categories:
    - ko_Troubleshooting
tags:
    - Java
    - Compilation Error
    - Symbol
---

## Java "Error: cannot find symbol"이란?

`cannot find symbol` 오류는 Java 컴파일러가 코드에 명시된 식별자(symbol)의 선언을 찾지 못했음을 의미합니다. 여기서 "심볼"은 변수 이름, 메서드 이름, 클래스 이름, 인터페이스 이름 등 개발자가 코드에서 정의하고 사용하는 모든 이름을 가리킵니다. 이 오류는 컴파일러에게 "당신이 사용한 '...'이 무엇인지, 어디에 정의되어 있는지 모르겠습니다"라고 말하는 것과 같습니다.

오류 메시지는 보통 세 부분으로 구성됩니다:
- **symbol**: 찾을 수 없는 심볼의 이름.
- **location**: 오류가 발생한 위치 (클래스 또는 메서드).
- **(선택) variable ... of type ...**: 심볼이 사용된 컨텍스트.

**오류 발생 예제:**
```java
public class SymbolTest {
    public static void main(String[] args) {
        Strng message = "Hello, World!"; // 오타: String -> Strng
        System.out.println(mesage); // 오타: message -> mesage
    }
}
```

**컴파일 오류:**
```
SymbolTest.java:3: error: cannot find symbol
        Strng message = "Hello, World!";
        ^
  symbol:   class Strng
  location: class SymbolTest
SymbolTest.java:4: error: cannot find symbol
        System.out.println(mesage);
                           ^
  symbol:   variable mesage
  location: class SymbolTest
```

## "cannot find symbol"의 일반적인 원인과 해결 방법

### 1. 오타 (Typo)

가장 흔한 원인입니다. 변수, 메서드, 클래스 이름의 철자가 선언된 곳과 사용된 곳에서 다른 경우 발생합니다. 대소문자도 구분하므로 주의해야 합니다.

- **해결책**: 심볼의 이름을 선언부와 사용부에서 동일하게 수정합니다. 위 예제에서 `Strng`를 `String`으로, `mesage`를 `message`로 고치면 해결됩니다.

### 2. `import` 문 누락

다른 패키지에 있는 클래스를 사용하면서 해당 클래스를 `import`하지 않은 경우 발생합니다. 예를 들어, `ArrayList`를 사용하려면 `java.util.ArrayList`를 임포트해야 합니다.

- **해결책**: 필요한 클래스를 소스 파일 상단에 `import` 문을 사용하여 추가합니다.
    ```java
    import java.util.ArrayList;

    public class MyClass {
        public static void main(String[] args) {
            ArrayList<String> list = new ArrayList<>();
        }
    }
    ```

### 3. 잘못된 변수 스코프 (Scope)

변수가 선언된 스코프(블록) 밖에서 해당 변수에 접근하려고 할 때 발생합니다. 예를 들어, `for` 루프 안에서 선언된 변수는 루프 밖에서 사용할 수 없습니다.

- **해결책**: 변수를 사용하려는 코드 블록을 포함하는 더 넓은 스코프에서 변수를 선언합니다.
    ```java
    public class ScopeTest {
        public void test() {
            int myVar = 0; // 블록 외부에서 선언
            for (int i = 0; i < 5; i++) {
                myVar = i;
            }
            System.out.println(myVar); // 정상 작동
        }
    }
    ```

### 4. 잘못된 메서드 호출

존재하지 않는 메서드를 호출하거나, 매개변수의 타입이나 개수가 다른 메서드를 호출하려고 할 때 발생합니다.

- **해결책**: 호출하려는 메서드의 시그니처(이름, 매개변수)가 클래스에 정의된 것과 일치하는지 확인합니다.

### 5. 라이브러리/클래스패스 문제

외부 라이브러리(.jar 파일)를 사용하지만, 컴파일 시 클래스패스(classpath)에 해당 라이브러리를 포함하지 않은 경우 발생합니다.

- **해결책**: 컴파일 명령어에 `-cp` 또는 `-classpath` 옵션을 사용하여 라이브러리의 경로를 명시해줍니다. IDE(Eclipse, IntelliJ)를 사용하는 경우, 프로젝트 빌드 경로에 라이브러리를 추가해야 합니다.
    ```bash
    javac -cp "/path/to/library.jar;." MyProgram.java
    ```

## 결론

`cannot find symbol` 오류는 대부분 사소한 실수에서 비롯됩니다. 오류 메시지가 가리키는 심볼과 위치를 주의 깊게 살펴보고, 다음 사항들을 순서대로 점검하면 쉽게 해결할 수 있습니다:
1.  이름에 오타가 없는가?
2.  필요한 클래스를 `import` 했는가?
3.  변수의 스코프가 올바른가?
4.  메서드 시그니처가 일치하는가?
5.  외부 라이브러리가 클래스패스에 포함되었는가?
