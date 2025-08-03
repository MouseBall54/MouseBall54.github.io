---
typora-root-url: ../
layout: single
title: >
    Java "Error: ';' expected" 해결 방법
date: 2025-08-03T14:40:00+09:00
header:
    teaser: /images/header_images/overlay_image_java.png
    overlay_image: /images/header_images/overlay_image_java.png
    overlay_filter: 0.5
excerpt: >
    Java에서 "';' expected"는 문장의 끝을 나타내는 세미콜론이 누락되었을 때 발생하는 기본적인 컴파일 오류입니다. 이 글에서는 오류의 원인과 해결 방법을 알아봅니다.
categories:
    - ko_Troubleshooting
tags:
    - Java
    - Compilation Error
    - Syntax
---

## Java "Error: ';' expected"란?

`Error: ';' expected`는 Java 컴파일러가 문법적으로 문장(statement)이 끝나야 하는 위치에 세미콜론(`;`)을 찾지 못했을 때 발생하는 구문 오류입니다. Java에서 세미콜론은 각 명령문이나 선언문이 끝났음을 알리는 매우 중요한 문법 요소입니다.

이 오류는 보통 오류가 발생한 줄이나 그 바로 앞 줄에 세미콜론이 누락되었음을 의미합니다.

**오류 발생 예제:**
```java
public class SemicolonTest {
    public static void main(String[] args) {
        int number = 10 // 세미콜론 누락
        System.out.println("The number is: " + number)
    }
}
```

**컴파일 오류:**
```
SemicolonTest.java:4: error: ';' expected
        int number = 10
                       ^
SemicolonTest.java:5: error: ';' expected
        System.out.println("The number is: " + number)
                                                     ^
```
컴파일러는 `int number = 10` 라인에서 세미콜론이 누락된 것을 발견하고 오류를 보고합니다. 그리고 그 오류의 영향으로 다음 라인인 `System.out.println(...)`에서도 문법적으로 혼란이 생겨 추가 오류를 보고할 수 있습니다.

## "';' expected"의 일반적인 원인과 해결 방법

### 1. 문장 끝에 세미콜론 누락

가장 흔한 원인입니다. 변수 선언, 메서드 호출, 값 할당 등 모든 문장의 끝에는 세미콜론이 와야 합니다.

- **해결책**: 문장이 끝나는 지점에 세미콜론을 추가합니다.
    ```java
    // 수정 전
    int x = 5

    // 수정 후
    int x = 5;
    ```

### 2. `for` 루프 구문 오류

`for` 루프의 초기화, 조건, 증감 부분을 구분할 때 쉼표(`,`)를 잘못 사용하거나 세미콜론을 누락하는 경우 발생할 수 있습니다.

- **해결책**: `for` 루프의 각 부분은 반드시 세미콜론으로 구분해야 합니다.
    ```java
    // 잘못된 예
    // for (int i = 0, i < 10, i++) {}

    // 올바른 예
    for (int i = 0; i < 10; i++) {}
    ```

### 3. 메서드 선언부 오류

메서드 시그니처를 선언하는 부분에 실수로 세미콜론을 추가하면, 컴파일러는 그 지점에서 메서드 선언이 끝났다고 착각하고 몸통(`{}`) 부분을 잘못된 문법으로 인식하여 오류를 발생시킬 수 있습니다.

- **해결책**: 메서드 선언부(이름과 매개변수 목록 뒤)에는 세미콜론을 붙이지 않습니다. 단, 추상 메서드(abstract method)나 인터페이스의 메서드 선언은 예외입니다.
    ```java
    // 잘못된 예
    // public void myMethod(); {
    //     System.out.println("Hello");
    // }

    // 올바른 예
    public void myMethod() {
        System.out.println("Hello");
    }
    ```

### 4. 배열 초기화 구문 오류

배열을 초기화할 때 중괄호(`{}`) 뒤에 세미콜론을 빠뜨리는 경우입니다.

- **해결책**: 배열 초기화 문장 끝에 세미콜론을 추가합니다.
    ```java
    // 수정 전
    // int[] numbers = {1, 2, 3}

    // 수정 후
    int[] numbers = {1, 2, 3};
    ```

## 오류 메시지 읽는 팁

`';' expected` 오류가 발생하면 컴파일러가 가리키는 위치(`^` 기호)를 잘 살펴보세요. 대부분의 경우, 오류가 보고된 위치 또는 그 바로 앞 코드에 세미콜론이 필요합니다. 때로는 한 곳의 세미콜론 누락이 연쇄적으로 여러 개의 `';' expected` 또는 다른 구문 오류를 유발할 수 있으므로, 항상 첫 번째 오류 메시지부터 해결해 나가는 것이 좋습니다.

## 결론

`Error: ';' expected`는 Java의 가장 기본적인 문법 규칙 중 하나를 어겼을 때 발생합니다. 이 오류를 마주치면 당황하지 말고, 컴파일러가 알려주는 위치를 중심으로 문장의 끝에 세미콜론이 제대로 찍혀 있는지 꼼꼼히 확인하는 습관을 들이는 것이 중요합니다.

---
*작업 이력*
- *2025년 8월 3일: 포스트 초안 작성*