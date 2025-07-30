---
typora-root-url: ../
layout: single
title: "java.lang.ArrayIndexOutOfBoundsException 해결 방법"
date: 2025-07-30T10:00:00+09:00
excerpt: "java.lang.ArrayIndexOutOfBoundsException은 배열의 유효한 인덱스 범위를 벗어나 접근할 때 발생하는 흔한 런타임 예외입니다. 이 글에서는 오류의 원인과 해결 방법을 자세히 알아봅니다."
categories:
  - ko_Troubleshooting
tags:
  - Java
  - Exception
  - Array
  - Troubleshooting
---

## java.lang.ArrayIndexOutOfBoundsException이란?

`java.lang.ArrayIndexOutOfBoundsException`은 Java에서 배열을 다룰 때 매우 흔하게 발생하는 런타임 예외다.
이 오류는 배열에 존재하지 않는 인덱스에 접근하려고 할 때 발생한다.
Java 배열의 인덱스는 `0`부터 시작하여 `배열의 길이 - 1`까지의 범위를 가진다.
만약 이 범위를 벗어나는 인덱스를 사용하면 JVM(Java Virtual Machine)은 이 예외를 던진다.

## 주요 원인

이 오류의 원인은 명확하다. 배열의 경계를 확인하지 않고 인덱스에 접근하는 것이다.

### 1. 잘못된 인덱스 값 사용

가장 흔한 경우로, 배열의 길이를 고려하지 않고 인덱스를 직접 사용할 때 발생한다.

```java
public class Example {
    public static void main(String[] args) {
        String[] fruits = {"Apple", "Banana", "Cherry"};
        // 배열의 길이는 3, 유효 인덱스는 0, 1, 2
        
        // 오류 발생: 인덱스 3은 존재하지 않음
        System.out.println(fruits[3]); 
    }
}
```

위 코드에서 `fruits` 배열의 길이는 3이므로 유효한 인덱스는 0, 1, 2다.
하지만 코드에서는 인덱스 3에 접근하려고 시도했기 때문에 `ArrayIndexOutOfBoundsException`이 발생한다.

### 2. 반복문에서의 조건 오류

반복문을 사용할 때, 반복 조건이 배열의 경계를 넘어서도록 설정되면 이 오류가 발생할 수 있다.

```java
public class LoopExample {
    public static void main(String[] args) {
        int[] numbers = new int[5]; // 인덱스는 0부터 4까지
        
        // 오류 발생: i가 5가 될 때 numbers[5]에 접근 시도
        for (int i = 0; i <= numbers.length; i++) {
            numbers[i] = i;
        }
    }
}
```

`for` 반복문의 조건이 `i <= numbers.length`로 설정되어 있다.
`numbers.length`는 5이므로, `i`는 0부터 5까지 반복된다.
`i`가 5가 되는 마지막 반복에서 `numbers[5]`에 접근하게 되어 예외가 발생한다.
반복 조건은 `i < numbers.length`가 되어야 올바르다.

### 3. 비어 있는 배열 접근

배열이 비어 있거나 `null`인 상태에서 특정 인덱스에 접근하려 할 때도 발생할 수 있다.
물론, `null`인 배열에 접근하면 `NullPointerException`이 먼저 발생한다.

## 해결 방법

### 1. 인덱스 범위 확인

배열에 접근하기 전에 항상 인덱스가 유효한 범위 내에 있는지 확인하는 것이 가장 기본적인 해결책이다.

```java
public class SafeAccessExample {
    public static void main(String[] args) {
        String[] fruits = {"Apple", "Banana", "Cherry"};
        int index = 3;

        if (index >= 0 && index < fruits.length) {
            System.out.println(fruits[index]);
        } else {
            System.out.println("잘못된 인덱스입니다: " + index);
        }
    }
}
```

이처럼 `if` 문을 사용하여 인덱스가 `0` 이상이고 `배열의 길이`보다 작은지 확인하면 오류를 예방할 수 있다.

### 2. 향상된 for문(for-each) 사용

배열의 모든 요소를 순차적으로 접근할 때는 인덱스를 직접 다루지 않는 향상된 `for`문을 사용하는 것이 더 안전하고 간결하다.

```java
public class ForEachExample {
    public static void main(String[] args) {
        String[] fruits = {"Apple", "Banana", "Cherry"};
        
        for (String fruit : fruits) {
            System.out.println(fruit);
        }
    }
}
```

향상된 `for`문은 내부적으로 배열의 경계를 관리하므로 `ArrayIndexOutOfBoundsException`이 발생할 여지가 없다.

## 결론

`ArrayIndexOutOfBoundsException`은 배열의 경계를 확인하지 않아 발생하는 단순하지만 치명적인 오류다.
배열 인덱스에 접근하기 전에는 항상 유효 범위를 확인하는 습관을 들이고, 가능하다면 인덱스를 직접 다루지 않는 향상된 `for`문을 활용하는 것이 좋다.
이러한 기본 원칙을 지키면 안정적인 코드를 작성하는 데 큰 도움이 된다.
