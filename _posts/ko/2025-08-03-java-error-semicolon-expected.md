---
typora-root-url: ../
layout: single
title: >
    자바 Error: ';' expected 해결 방법 (가장 기본적인 실수)
date: 2025-08-03T11:40:00+09:00
header:
   teaser: /images/header_images/overlay_image_java.png
   overlay_image: /images/header_images/overlay_image_java.png
   overlay_filter: 0.5
excerpt: >
    자바에서 모든 구문의 끝을 알려주는 세미콜론(;)을 빠뜨렸을 때 발생하는 `Error: ';' expected` 컴파일 오류의 원인과 해결책을 알아봅니다.
categories:
  - ko_Troubleshooting
tags:
  - Java
  - Compilation Error
  - SyntaxError
---

## 문제 상황

`Error: ';' expected`는 자바를 처음 배우는 사람들이 가장 흔하게 마주치는 컴파일 오류 중 하나입니다. 이 오류의 의미는 매우 명확합니다. 자바 컴파일러가 **코드의 특정 위치에 세미콜론(`;`)이 있어야 한다고 예상했지만, 찾지 못했다**는 뜻입니다.

자바에서 세미콜론은 하나의 구문(statement)이 끝났음을 알리는 매우 중요한 문법적 요소입니다. 변수 선언, 값 할당, 메서드 호출, `return` 문 등 대부분의 구문은 반드시 세미콜론으로 끝나야 합니다.

## 오류 발생 코드 예시

가장 일반적인 예시는 구문의 끝에 세미콜론을 잊어버리는 것입니다.

### 1. 변수 선언 시 세미콜론 누락

```java
public class Main {
    public static void main(String[] args) {
        String message = "Hello, World!" // 세미콜론이 없습니다.
        System.out.println(message);
    }
}
```

컴파일러는 `String message = "Hello, World!"` 구문이 끝난 뒤 세미콜론이 올 것을 예상했지만, 바로 다음 줄의 `System.out.println(message)`를 마주했기 때문에 오류를 발생시킵니다. 오류 메시지는 보통 다음과 같이 나타납니다.

```
Main.java:4: error: ';' expected
        System.out.println(message)
                                   ^
```
오류가 보고되는 위치는 세미콜론이 누락된 줄의 다음 줄 시작 부분일 수 있다는 점에 유의하세요.

### 2. 메서드 호출 시 세미콜론 누락

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello") // 세미콜론이 없습니다.
    }
}
```

## 해결 방법

이 오류는 100% 문법적인 문제이므로 해결 방법은 단 하나입니다.

### 세미콜론(`;`) 추가하기

오류가 발생한 위치를 확인하고, 컴파일러가 지적한 곳 또는 그 앞 구문의 끝에 빠진 세미콜론을 추가하면 됩니다.

```java
// 수정된 코드
public class Main {
    public static void main(String[] args) {
        String message = "Hello, World!"; // 세미콜론 추가
        System.out.println(message);
    }
}
```

### 세미콜론을 사용하지 않는 경우

참고로, 자바의 모든 곳에 세미콜론이 필요한 것은 아닙니다. 다음 경우에는 세미콜론을 사용하지 않습니다.

-   **클래스나 메서드 선언부:** `public class Main { ... }` 또는 `public void myMethod() { ... }`
-   **제어문(if, for, while)의 조건부:** `if (condition) { ... }` 또는 `for (int i=0; i<5; i++) { ... }`
-   **패키지 선언 및 임포트 구문:** `package com.example;` 이나 `import java.util.List;` 처럼 이들은 구문이므로 세미콜론으로 끝납니다. (이 부분은 혼동하기 쉬우나, 선언부가 아닌 구문으로 취급됩니다.)

정확히는 **코드 블록(`{ ... }`) 자체의 끝에는 세미콜론을 붙이지 않는다**고 기억하는 것이 좋습니다.

## 결론

`Error: ';' expected`는 자바의 가장 기본적인 문법 규칙을 지키지 않았을 때 발생합니다. 오류가 발생하면,

1.  컴파일러가 지적한 코드 줄 또는 그 바로 윗 줄을 확인합니다.
2.  구문의 끝에 세미콜론이 빠져있는지 확인하고 추가합니다.

대부분의 최신 IDE(통합 개발 환경)는 코드를 작성하는 동안 이런 실수를 실시간으로 감지하고 수정 제안을 해주므로, IDE의 도움을 받는 것이 좋습니다.
