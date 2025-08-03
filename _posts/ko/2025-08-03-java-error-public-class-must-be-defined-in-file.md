---
typora-root-url: ../
layout: single
title: >
    자바 Error: a public class ... must be defined in a file called ... .java 해결 방법
date: 2025-08-03T10:40:00+09:00
header:
   teaser: /images/header_images/overlay_image_java.png
   overlay_image: /images/header_images/overlay_image_java.png
   overlay_filter: 0.5
excerpt: >
    자바에서 `public` 클래스의 이름과 `.java` 파일의 이름이 일치하지 않을 때 발생하는 컴파일 오류의 원인과 해결 방법을 알아봅니다.
categories:
  - ko_Troubleshooting
tags:
  - Java
  - Compilation Error
  - public class
---

## 문제 상황

자바 소스 코드를 컴파일할 때 다음과 같은 오류 메시지를 만날 수 있습니다.

```
Error: a public class <ClassName> must be defined in a file called <ClassName>.java
```

이 오류는 자바의 핵심 규칙 중 하나를 위반했을 때 발생합니다. 그 규칙은 바로 **하나의 소스 파일(.java)에는 최대 하나의 `public` 클래스만 존재할 수 있으며, 그 `public` 클래스의 이름은 반드시 소스 파일의 이름과 대소문자까지 정확히 일치해야 한다**는 것입니다.

컴파일러는 이 규칙을 통해 클래스를 파일 시스템에서 쉽게 찾을 수 있습니다.

## 오류 발생 코드 예시

예를 들어, `MyProgram.java`라는 파일 안에 다음과 같이 코드를 작성했다고 가정해 보겠습니다.

**파일 이름: `MyProgram.java`**

```java
// 파일 이름은 MyProgram.java이지만, public 클래스 이름은 HelloWorld입니다.
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

이 코드를 컴파일하려고 하면, 컴파일러는 `public` 클래스인 `HelloWorld`가 `HelloWorld.java` 파일에 있어야 한다고 판단하여 다음과 같은 오류를 발생시킵니다.

```
MyProgram.java:2: error: class HelloWorld is public, should be declared in a file named HelloWorld.java
public class HelloWorld {
       ^
1 error
```

## 해결 방법

이 문제는 매우 간단하게 해결할 수 있습니다.

### 1. 파일 이름을 클래스 이름과 일치시키기

가장 일반적인 해결책은 `.java` 파일의 이름을 `public` 클래스의 이름과 동일하게 변경하는 것입니다.

-   위 예시에서 `MyProgram.java` 파일의 이름을 `HelloWorld.java`로 변경합니다.

이 방법은 클래스의 이름을 그대로 유지하고 싶을 때 사용합니다.

### 2. 클래스 이름을 파일 이름과 일치시키기

반대로, 파일 이름을 유지하고 싶다면 `public` 클래스의 이름을 파일 이름에 맞게 수정하면 됩니다.

-   `MyProgram.java` 파일의 내용을 다음과 같이 수정합니다.

**파일 이름: `MyProgram.java`**

```java
// 클래스 이름을 파일 이름인 MyProgram과 일치시킵니다.
public class MyProgram {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

### 3. 클래스에서 `public` 키워드 제거하기 (권장하지 않음)

만약 클래스가 다른 패키지에서 접근할 필요가 없다면 `public` 접근 제어자를 제거할 수도 있습니다. `public`이 아닌 클래스는 파일 이름과 달라도 컴파일 오류가 발생하지 않습니다.

**파일 이름: `MyProgram.java`**

```java
// public 키워드를 제거하면 클래스 이름과 파일 이름이 달라도 됩니다.
class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

하지만 이 방법은 클래스의 접근 범위를 변경하므로 신중하게 사용해야 합니다. 대부분의 경우, 클래스를 `public`으로 유지하고 파일 이름과 클래스 이름을 일치시키는 것이 가장 좋은 방법입니다.

## 결론

`Error: a public class ... must be defined in a file called ... .java` 오류는 자바의 기본적인 명명 규칙을 따르지 않았기 때문에 발생합니다. 이 오류를 해결하려면 다음 중 하나를 선택하세요.

1.  **파일 이름**을 `public` 클래스 이름에 맞게 변경합니다.
2.  **`public` 클래스 이름**을 파일 이름에 맞게 변경합니다.

자바에서는 코드의 구조와 가독성을 위해 파일 이름과 `public` 클래스 이름을 일치시키는 것이 표준적인 관례이므로, 항상 이 규칙을 따르는 것이 좋습니다.
