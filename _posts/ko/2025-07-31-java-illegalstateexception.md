---
typora-root-url: ../
layout: single
title: "Java IllegalStateException 해결 방법"

lang: ko
translation_id: java-illegalstateexception
excerpt: "Java의 IllegalStateException의 원인을 이해하고 객체가 올바른 상태에 있을 때만 메서드를 호출하여 해결하는 방법을 배웁니다. 실용적인 예제를 통해 확인하세요."
header:
   teaser: /images/header_images/overlay_image_java.png
   overlay_image: /images/header_images/overlay_image_java.png
   overlay_filter: 0.5
categories:
  - ko_Troubleshooting
tags:
  - Java
  - Exception
  - IllegalStateException
  - Troubleshooting
---

## `IllegalStateException`이란?

Java에서 `IllegalStateException`은 런타임 예외이다. 이는 메서드가 부적절하거나 잘못된 시점에 호출되었음을 나타낸다. 즉, 객체가 요청된 작업을 수행하기에 올바른 상태가 아니라는 의미다. 이 문제는 객체의 생명주기나 상태에 맞지 않게 객체를 사용할 때 자주 발생한다.

## 주요 원인과 해결 방법

`IllegalStateException`이 발생하는 일반적인 시나리오와 해결 방법을 살펴보자.

### 1. Iterator의 잘못된 사용

가장 흔한 원인 중 하나는 `Iterator`에서 `next()`를 호출하기 전에 `remove()`를 호출하는 것이다.

#### 문제 코드

```java
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class IteratorExample {
    public static void main(String[] args) {
        List<String> list = new ArrayList<>();
        list.add("A");
        list.add("B");

        Iterator<String> iterator = list.iterator();
        
        try {
            // next()를 먼저 호출하지 않았기 때문에 IllegalStateException 발생
            iterator.remove(); 
        } catch (IllegalStateException e) {
            System.err.println("예외 발생: " + e.getMessage());
        }
    }
}
```

`remove()` 메서드는 `next()` 호출 한 번당 한 번만 호출할 수 있다. `next()` 호출 없이 `remove()`를 호출하면 예외가 발생한다.

#### 해결 방법

`remove()`를 호출하기 전에 항상 `next()`를 먼저 호출해야 한다. 이렇게 하면 이터레이터가 제거할 유효한 요소에 위치하게 된다.

```java
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class IteratorSolution {
    public static void main(String[] args) {
        List<String> list = new ArrayList<>();
        list.add("A");
        list.add("B");

        Iterator<String> iterator = list.iterator();
        
        if (iterator.hasNext()) {
            iterator.next(); // 첫 번째 요소로 이동
            iterator.remove(); // 이제 안전하게 제거 가능
        }
        
        System.out.println("제거 후 리스트: " + list); // 출력: [B]
    }
}
```

### 2. 닫힌 리소스에 대한 작업

이미 닫힌 `Scanner`나 `Stream`과 같은 리소스를 사용하려고 시도하는 경우에도 이 예외가 발생할 수 있다.

#### 문제 코드

```java
import java.util.Scanner;

public class ScannerExample {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        scanner.close();
        
        try {
            // 스캐너가 닫혔기 때문에 IllegalStateException 발생
            scanner.nextLine(); 
        } catch (IllegalStateException e) {
            System.err.println("예외 발생: " + e.getMessage());
        }
    }
}
```

`close()`가 호출되면 `Scanner` 객체는 더 이상 입력을 읽을 수 있는 상태가 아니다.

#### 해결 방법

리소스를 닫기 전에 필요한 모든 작업을 수행해야 한다. `try-with-resources` 블록을 사용하는 것이 리소스 생명주기를 효과적으로 관리하는 가장 좋은 방법이다.

```java
import java.util.Scanner;

public class ScannerSolution {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.print("이름을 입력하세요: ");
            String name = scanner.nextLine();
            System.out.println("안녕하세요, " + name);
        } 
        // 스캐너는 여기서 자동으로 닫힌다.
        // 더 이상 작업이 필요 없다.
    }
}
```

### 3. 사용자 정의 클래스의 잘못된 상태

메서드가 특정 순서로만 호출되어야 하는 클래스를 정의할 수 있다. 순서가 위반되면 `IllegalStateException`을 발생시켜 계약을 강제할 수 있다.

#### 문제 코드

```java
public class ConnectionManager {
    private boolean connected = false;

    public void connect() {
        this.connected = true;
        System.out.println("연결되었습니다.");
    }

    public void sendData(String data) {
        if (!connected) {
            throw new IllegalStateException("연결되지 않았습니다. 데이터를 보낼 수 없습니다.");
        }
        System.out.println("데이터 전송: " + data);
    }

    public static void main(String[] args) {
        ConnectionManager manager = new ConnectionManager();
        try {
            // connect()를 호출하지 않았기 때문에 IllegalStateException 발생
            manager.sendData("안녕하세요");
        } catch (IllegalStateException e) {
            System.err.println("예외 발생: " + e.getMessage());
        }
    }
}
```

#### 해결 방법

메서드를 호출하기 전에 항상 객체가 올바른 상태인지 확인해야 한다. 이 경우 `sendData()` 전에 `connect()`를 호출한다.

```java
public class ConnectionManagerSolution {
    private boolean connected = false;

    public void connect() {
        this.connected = true;
        System.out.println("연결되었습니다.");
    }

    public void sendData(String data) {
        if (!connected) {
            throw new IllegalStateException("연결되지 않았습니다. 데이터를 보낼 수 없습니다.");
        }
        System.out.println("데이터 전송: " + data);
    }

    public static void main(String[] args) {
        ConnectionManagerSolution manager = new ConnectionManagerSolution();
        manager.connect(); // 먼저 연결을 설정한다
        manager.sendData("안녕하세요, 세상!"); // 이제 데이터를 안전하게 보낼 수 있다
    }
}
```

## 결론

`IllegalStateException`은 예방적 성격의 예외이다. 객체의 상태에 따라 메서드가 올바르게 사용되도록 강제하여 프로그래밍 오류를 조기에 발견하는 데 도움을 준다. 이 예외를 피하려면 상태 기반의 전제 조건이 있는 메서드를 호출하기 전에 항상 객체가 적절한 상태인지 확인하는 습관을 들여야 한다.
