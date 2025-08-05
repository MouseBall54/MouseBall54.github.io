---
typora-root-url: ../
layout: single
title: >
    Java "Error: a public class ... must be defined in a file called ... .java" 해결 방법
date: 2025-08-03T14:30:00+09:00
header:
    teaser: /images/header_images/overlay_image_java.png
    overlay_image: /images/header_images/overlay_image_java.png
    overlay_filter: 0.5
excerpt: >
    Java에서 이 컴파일 오류는 public 클래스의 이름과 소스 파일의 이름이 일치하지 않을 때 발생합니다. 이 글에서는 오류의 원인과 해결 방법을 알아봅니다.
categories:
    - ko_Troubleshooting
tags:
    - Java
    - Compilation Error
    - Class
---

## Java "Error: a public class ... must be defined in a file called ... .java"란?

이 오류 메시지는 Java 컴파일러(javac)가 소스 코드를 컴파일할 때 발생하는 가장 기본적인 오류 중 하나입니다. Java 언어 규격에 따르면, 하나의 소스 파일(.java)에는 **최대 하나의 `public` 클래스**만 존재할 수 있으며, 만약 `public` 클래스가 존재한다면 **소스 파일의 이름은 반드시 해당 `public` 클래스의 이름과 대소문자까지 정확히 일치**해야 합니다.

## 오류의 일반적인 원인

1.  **파일 이름과 클래스 이름 불일치**: 가장 흔한 원인입니다. 예를 들어, `MyClass`라는 `public` 클래스가 `MyProgram.java`라는 파일에 저장된 경우 이 오류가 발생합니다.
2.  **대소문자 불일치**: 파일 시스템은 대소문자를 구분하지 않을 수 있지만, Java 컴파일러는 엄격하게 구분합니다. `MyClass` 클래스가 `myclass.java` 파일에 저장되면 오류가 발생합니다.
3.  **하나의 파일에 여러 `public` 클래스 선언**: 하나의 `.java` 파일 안에 두 개 이상의 `public` 클래스를 선언하려고 시도하면 발생합니다.

**오류 발생 예제:**

`AnotherClass.java` 파일:
```java
// 파일 이름은 AnotherClass.java인데, public 클래스 이름은 MyClass입니다.
public class MyClass {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}

class AnotherClass {
    // ...
}
```

위 코드를 컴파일하면 다음과 같은 오류가 발생합니다:
```
AnotherClass.java:2: error: class MyClass is public, should be declared in a file named MyClass.java
public class MyClass {
       ^
```

## 오류 해결 방법

### 1. 파일 이름을 `public` 클래스 이름과 일치시키기

가장 간단한 해결책은 `.java` 파일의 이름을 `public` 클래스의 이름과 동일하게 변경하는 것입니다.

위 예제에서 `AnotherClass.java` 파일의 이름을 `MyClass.java`로 변경하면 문제가 해결됩니다.

### 2. 클래스 이름을 파일 이름과 일치시키기

파일 이름을 변경할 수 없는 경우, `public` 클래스의 이름을 파일 이름과 일치하도록 수정합니다.

`AnotherClass.java` 파일:
```java
// 클래스 이름을 파일 이름인 AnotherClass와 일치시킵니다.
public class AnotherClass {
    public static void main(String[] args) {
        System.out.println("Hello from AnotherClass!");
    }
}

class MyClass {
    // ...
}
```

### 3. 클래스의 `public` 접근 제어자 제거

만약 클래스를 꼭 `public`으로 선언할 필요가 없다면, `public` 키워드를 제거하여 패키지-전용(package-private) 클래스로 만들 수 있습니다. `public`이 아닌 클래스는 파일 이름과 이름이 달라도 상관없습니다. 하지만 이 경우 다른 패키지에서 해당 클래스에 접근할 수 없게 됩니다.

`AnotherClass.java` 파일:
```java
// MyClass에서 public을 제거하여 오류를 해결합니다.
class MyClass {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}

public class AnotherClass {
    // 이 클래스가 public이므로 파일 이름과 일치해야 합니다.
}
```

## 결론

Java의 "public class ... must be defined in a file called ... .java" 오류는 Java의 기본 규칙을 따르지 않았을 때 발생합니다. 이 규칙은 코드를 체계적으로 구성하고, 컴파일러와 JVM이 클래스를 쉽게 찾을 수 있도록 돕기 위해 존재합니다. 문제를 해결하려면 파일 이름과 `public` 클래스 이름이 항상 대소문자까지 정확히 일치하는지 확인하는 습관을 들이는 것이 중요합니다.

