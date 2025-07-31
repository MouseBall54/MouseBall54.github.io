---
typora-root-url: ../
layout: single
title: "Java NoClassDefFoundError 해결 방법"
date: 2025-07-31T12:30:00+09:00
excerpt: "컴파일 시점에는 있었지만 런타임에 누락된 클래스로 인해 발생하는 Java의 NoClassDefFoundError의 원인을 이해하고 해결합니다. 클래스패스를 확인하고, 의존성을 관리하며, 정적 초기화 실패를 수정하는 방법을 배웁니다."
header:
   teaser: /images/header_images/overlay_image_java.png
   overlay_image: /images/header_images/overlay_image_java.png
   overlay_filter: 0.5
categories:
  - ko_Troubleshooting
tags:
  - Java
  - NoClassDefFoundError
  - Classpath
  - JVM
  - Troubleshooting
---

## `NoClassDefFoundError`란?

`java.lang.NoClassDefFoundError`는 Java에서 흔하고 종종 혼란스러운 오류다. 이는 Java 가상 머신(JVM)이 런타임에 클래스를 로드하려고 할 때, 해당 클래스가 컴파일 시점에는 있었지만 실행 중인 클래스패스에서 찾을 수 없을 때 발생한다.

이것을 `ClassNotFoundException`과 구별하는 것이 중요하다.
*   **`ClassNotFoundException`**: `Class.forName()`, `ClassLoader.loadClass()`, 또는 `ClassLoader.findSystemClass()`를 사용하여 동적으로 클래스를 로드하려고 할 때 클래스가 클래스패스에 없는 경우 발생하는 예외다. 이는 종종 복구 가능한 상황이다.
*   **`NoClassDefFoundError`**: JVM이 컴파일 중에는 클래스 정의를 찾을 수 있었지만, 런타임에 필요한 `.class` 파일을 찾지 못했음을 나타내는 오류다. 이는 보통 애플리케이션의 설정이나 패키징 문제점을 가리킨다.

## 주요 원인과 해결 방법

이 오류의 일반적인 원인을 분석해보자.

### 1. 클래스패스에 누락된 의존성

이것이 가장 빈번한 원인이다. 코드가 라이브러리(예: JAR 파일)에 대해 컴파일되었지만, 애플리케이션을 실행할 때 해당 라이브러리가 클래스패스에 포함되지 않은 경우다.

#### 예시 시나리오

`library.jar`의 `com.example.SomeClass` 클래스를 사용하는 코드를 컴파일한다.

```bash
# library.jar가 클래스패스에 있으므로 컴파일 성공
javac -cp ".;library.jar" MyClass.java
```

하지만 실행할 때 `library.jar`를 포함하는 것을 잊어버린다.

```bash
# 런타임에 실패
java MyClass 
# com.example.SomeClass에 대해 NoClassDefFoundError 발생
```

#### 해결 방법: 클래스패스 확인 및 수정

모든 필수 JAR 파일이 런타임 클래스패스에 있는지 확인한다.

*   **명령줄:** `-cp` 또는 `-classpath` 플래그를 사용하여 필요한 모든 라이브러리를 지정한다.

    ```bash
    java -cp ".;library.jar" MyClass
    ```
*   **빌드 도구 (Maven/Gradle):** 빌드 도구를 사용하는 경우, `pom.xml`이나 `build.gradle` 파일에 의존성이 올바른 범위(보통 `compile` 또는 `runtime`)로 정의되어 있는지 확인한다.

    *   **Maven `pom.xml`:**
        ```xml
        <dependency>
            <groupId>com.example</groupId>
            <artifactId>library</artifactId>
            <version>1.0</version>
            <scope>compile</scope>
        </dependency>
        ```
    *   **Gradle `build.gradle`:**
        ```groovy
        dependencies {
            implementation 'com.example:library:1.0'
        }
        ```
    그런 다음, 도구를 사용하여 애플리케이션을 빌드하면 의존성이 올바르게 패키징된다(예: fat JAR 또는 `lib` 디렉터리).

*   **IDE (Eclipse/IntelliJ):** 프로젝트의 빌드 경로 또는 모듈 설정을 확인하여 라이브러리가 의존성으로 포함되어 있는지 확인한다.

### 2. 정적 초기화 블록의 예외

클래스에 `static` 블록이 있는 경우, 해당 코드는 클래스가 처음 로드될 때 실행된다. 이 정적 블록 내에서 예외가 발생하면 JVM은 클래스 로드에 실패하고 `ExceptionInInitializerError`를 발생시킨다.

이후 해당 클래스를 사용하려는 모든 시도는 `NoClassDefFoundError`를 초래하게 되는데, 이는 근본 원인이 초기 예외였기 때문에 오해의 소지가 있을 수 있다.

#### 문제 코드

```java
public class MyClassWithStaticError {
    static {
        // ArithmeticException을 발생시킴
        int result = 10 / 0; 
    }

    public void doSomething() {
        System.out.println("무언가 하는 중...");
    }
}

public class Main {
    public static void main(String[] args) {
        try {
            // 첫 번째 시도는 ExceptionInInitializerError를 발생시킴
            new MyClassWithStaticError(); 
        } catch (Throwable t) {
            System.err.println("첫 번째 오류: " + t);
        }

        try {
            // 두 번째 시도는 NoClassDefFoundError를 발생시킴
            new MyClassWithStaticError(); 
        } catch (Throwable t) {
            System.err.println("두 번째 오류: " + t);
        }
    }
}
```

#### 해결 방법: 정적 초기화 수정

애플리케이션 로그에서 초기 `ExceptionInInitializerError`를 주의 깊게 확인한다. 해당 오류의 스택 트레이스는 문제를 일으키는 정적 블록의 정확한 줄을 가리킬 것이다. 정적 코드의 근본적인 문제(예: null 포인터, 구성 오류 또는 리소스 로딩 실패)를 해결한다.

### 3. 잘못된 패키징 또는 배포

웹 애플리케이션(예: WAR 파일)을 배포할 때, 필요한 JAR 파일을 `WEB-INF/lib` 디렉터리에 포함하는 것을 잊을 수 있다. 애플리케이션은 IDE에서는 잘 컴파일되지만 서버에서는 런타임에 실패할 것이다.

#### 해결 방법: 아티팩트 확인

패키징된 아티팩트(JAR, WAR, EAR)의 내용을 검사하여 모든 의존성 JAR이 올바른 위치에 포함되어 있는지 확인한다.
*   WAR 파일의 경우, `WEB-INF/lib` 디렉터리를 확인한다.
*   fat JAR의 경우, 의존성 클래스가 내부에 번들로 포함되어 있는지 확인한다.

## 결론

`NoClassDefFoundError`는 근본적으로 클래스패스 문제다. 이는 컴파일 시점에는 있었던 의존성이 런타임에는 누락되었음을 알려준다. 이를 해결하려면 다음을 수행해야 한다.
1.  **로그 확인:** 이전에 발생한 `ExceptionInInitializerError`가 있는지 확인한다.
2.  **런타임 클래스패스 검증:** 필요한 모든 JAR이 있는지 확인한다.
3.  **빌드 구성 및 패키징된 아티팩트 검사:** Maven, Gradle 설정과 WAR, JAR 파일을 검사하여 의존성이 올바르게 포함되었는지 확인한다.
