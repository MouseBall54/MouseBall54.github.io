---
typora-root-url: ../
layout: single
title: "Java에서 java.lang.ClassCastException 해결 방법"
date: 2025-07-31T14:00:00+09:00
excerpt: "객체를 캐스팅하기 전에 `instanceof`와 같은 검사를 통해 타입 안전성을 확보하여 `java.lang.ClassCastException`을 이해하고 예방하는 방법을 알아봅니다."
header:
   teaser: /images/header_images/overlay_image_java.png
   overlay_image: /images/header_images/overlay_image_java.png
   overlay_filter: 0.5
categories:
  - ko_Troubleshooting
tags:
  - Java
  - ClassCastException
  - Exception
  - Type Casting
  - Troubleshooting
---

## `ClassCastException`이란 무엇인가?

`java.lang.ClassCastException`은 JVM(Java Virtual Machine)이 객체를 해당 객체의 인스턴스가 아닌 타입으로 캐스팅하려고 할 때 발생하는 런타임 예외이다. 이 오류는 컴파일 시점에는 확인할 수 없는 잘못된 타입 변환을 나타내며, 종종 컬렉션이나 제네릭 타입과 함께 발생한다.

예를 들어, `Integer` 객체를 `String` 클래스로 캐스팅하려고 하면 `String`이 `Integer`의 상위 클래스나 인터페이스가 아니기 때문에 실패한다.

## 일반적인 원인

1.  **잘못된 다운캐스팅**: 객체가 실제로 해당 하위 클래스의 인스턴스인지 확인하지 않고 상위 클래스 객체를 하위 클래스 타입 중 하나로 캐스팅하려고 시도하는 경우.
2.  **컬렉션의 잘못된 처리**: 원시(non-generic) 컬렉션에 다른 타입의 객체를 저장한 다음, 검색 시 특정 타입으로 캐스팅하려고 시도하는 경우.
3.  **프레임워크 및 라이브러리 오용**: 예상과 다른 프록시 객체나 타입을 반환하는 프레임워크(예: Hibernate, Spring)의 객체를 잘못 구현하거나 사용하는 경우.

## 해결 방법

`ClassCastException`을 예방하는 핵심은 캐스팅을 수행하기 전에 타입 안전성을 보장하는 것이다.

### 1. `instanceof` 연산자 사용

객체를 캐스팅하기 전에 `instanceof` 연산자를 사용하여 객체가 대상 타입의 인스턴스인지 확인한다. 이는 예외를 예방하는 가장 신뢰할 수 있는 방법이다.

```java
public void processObject(Object obj) {
    if (obj instanceof String) {
        String str = (String) obj; // 안전한 캐스팅
        System.out.println("문자열: " + str);
    } else {
        System.out.println("객체는 문자열이 아닙니다.");
    }
}
```

### 2. 타입 안전 컬렉션을 위한 제네릭 사용

컬렉션으로 작업할 때는 항상 제네릭을 사용하여 컬렉션이 담을 수 있는 객체의 타입을 지정한다. 이를 통해 컴파일러가 런타임에 `ClassCastException`이 발생하기 훨씬 전에 컴파일 시점에서 타입 불일치를 잡아낼 수 있다.

```java
// 안전하지 않음: 원시 리스트는 모든 객체 타입을 담을 수 있음
List rawList = new ArrayList();
rawList.add("Hello");
rawList.add(123); // Integer 추가

// 이 줄은 런타임에 ClassCastException을 유발함
// String text = (String) rawList.get(1);

// 안전함: 제네릭 리스트는 타입 안전성을 강제함
List<String> genericList = new ArrayList<>();
genericList.add("World");
// genericList.add(456); // 이 줄은 컴파일 시점 오류를 유발함

String text = genericList.get(0); // 캐스팅 필요 없음
```

### 3. `Class.isInstance()` 메서드 사용

`instanceof`와 유사하게 `Class.isInstance()` 메서드를 사용할 수 있다. 이는 대상 타입이 런타임에 동적으로 결정될 때 유용할 수 있다.

```java
public void checkAndCast(Object obj, Class<?> targetType) {
    if (targetType.isInstance(obj)) {
        Object castedObj = targetType.cast(obj); // 안전한 캐스트
        System.out.println(targetType.getName() + "(으)로 성공적으로 캐스팅되었습니다.");
    } else {
        System.out.println(targetType.getName() + "(으)로 캐스팅할 수 없습니다.");
    }
}

// 사용 예시
checkAndCast("A string", String.class); // 성공
checkAndCast(123, String.class);      // 실패
```

### 4. 프레임워크 및 API 문서 검토

타사 라이브러리나 프레임워크로 작업할 때 예외가 발생하면 해당 문서를 주의 깊게 검토한다. 메서드가 예상과 다른 프록시 객체나 하위 클래스 타입을 반환할 수 있다. 정확한 반환 타입을 이해하는 것이 중요하다.

`instanceof` 확인으로 방어적인 코드를 작성하고 Java의 제네릭 시스템을 활용하면 `ClassCastException`을 제거하고 더 강력하고 타입 안전한 애플리케이션을 만들 수 있다.
