typora-root-url: ../
layout: single
title: >
   Java 제네릭(Generics)을 사용한 타입 안정성 확보
date: 2025-08-05T11:05:00+09:00
header:
   teaser: /images/header_images/overlay_image_java.png
   overlay_image: /images/header_images/overlay_image_java.png
   overlay_filter: 0.5
excerpt: >
    Java 제네릭이 어떻게 작동하는지, 컴파일 시점에 타입 안정성을 어떻게 제공하는지, 그리고 컬렉션 및 사용자 정의 클래스와 함께 사용하여 유연하고 재사용 가능한 코드를 만드는 방법을 알아보세요.
categories:
  - ko_Troubleshooting
tags:
  - Java
  - Generics
  - Type Safety
  - Best Practices
---
## 제네릭(Generics)이란?

Java 5에서 도입된 **제네릭(Generics)**은 컴파일 시 타입 안정성을 제공하면서 다양한 데이터 타입과 함께 작동할 수 있는 클래스, 인터페이스, 메서드를 만들 수 있게 해줍니다. 일반적인 `Object` 타입을 사용하고 수동으로 형변환을 수행하는 대신, 클래스나 메서드가 사용할 타입을 지정할 수 있습니다. 이는 꺾쇠괄호 표기법 `<>`으로 나타냅니다.

### 제네릭 이전의 문제점

제네릭이 도입되기 전에는 `ArrayList`와 같은 컬렉션이 모든 것을 `Object`로 저장했습니다. 이는 컬렉션에 어떤 타입의 객체든 추가할 수 있다는 것을 의미했으며, 런타임에 `ClassCastException` 오류가 발생할 가능성이 있었습니다.

**제네릭 이전 코드 (안전하지 않음):**
```java
import java.util.ArrayList;
import java.util.List;

List list = new ArrayList();
list.add("hello");
list.add(123); // 컴파일 시점에는 오류가 없음

// 이 코드는 컴파일되지만, 런타임에 ClassCastException을 발생시킵니다.
String text = (String) list.get(1); 
```
이 버그를 찾으려면 프로그램을 실행해야만 했습니다. 컴파일러는 도움을 줄 수 없었습니다.

## 해결책: 타입 안정성을 위한 제네릭

제네릭은 컬렉션이 담을 수 있는 요소의 타입을 지정할 수 있게 함으로써 이 문제를 해결합니다.

**제네릭을 사용한 코드 (타입 안전):**
```java
import java.util.ArrayList;
import java.util.List;

List<String> list = new ArrayList<>(); // 이 리스트는 오직 String만 담을 수 있습니다.
list.add("hello");
// list.add(123); // 이것은 이제 컴파일 시간 오류입니다!

String text = list.get(0); // 형변환이 필요 없음
```

이제 컴파일러는 `String` 객체만 리스트에 추가되도록 강제합니다. 이는 버그를 조기에 발견하고 수동 형변환의 필요성을 없애줍니다.

### 제네릭의 핵심 개념

#### 1. 제네릭 클래스와 인터페이스

직접 제네릭 클래스와 인터페이스를 만들 수 있습니다. 타입 매개변수(일반적으로 `T`는 Type, `E`는 Element, `K`는 Key, `V`는 Value)는 플레이스홀더 역할을 합니다.

**제네릭 클래스 예시:**
```java
// 어떤 타입의 객체든 담을 수 있는 제네릭 Box 클래스
public class Box<T> {
    private T content;

    public void setContent(T content) {
        this.content = content;
    }

    public T getContent() {
        return content;
    }
}

// 사용법
Box<String> stringBox = new Box<>();
stringBox.setContent("A string");
String myString = stringBox.getContent();

Box<Integer> integerBox = new Box<>();
integerBox.setContent(42);
int myInt = integerBox.getContent();
```

#### 2. 제네릭 메서드

자체적인 타입 매개변수를 가진 제네릭 메서드를 만들 수도 있습니다. 이는 정적 유틸리티 메서드에 유용합니다.

```java
public class Utils {
    // 배열 요소를 출력하는 제네릭 메서드
    public static <E> void printArray(E[] inputArray) {
        for (E element : inputArray) {
            System.out.printf("%s ", element);
        }
        System.out.println();
    }
}

// 사용법
Integer[] intArray = { 1, 2, 3 };
String[] stringArray = { "A", "B", "C" };

Utils.printArray(intArray);   // 1 2 3 출력
Utils.printArray(stringArray); // A B C 출력
```

#### 3. 제한된 타입 매개변수 (와일드카드)

때로는 타입 인자로 사용될 수 있는 타입을 제한하고 싶을 때가 있습니다. 이는 `extends` 키워드를 사용하여 수행됩니다.

- **상한 제한 와일드카드 (`? extends Type`)**: 알 수 없는 타입이 `Type`의 하위 타입입니다. 제네릭 구조에서 *읽기*를 원할 때 유용합니다.

```java
// 이 메서드는 Number 또는 그 하위 클래스(Integer, Double 등)의 List를 받을 수 있습니다.
public void processNumbers(List<? extends Number> list) {
    for (Number num : list) {
        System.out.println(num.doubleValue());
    }
    // list.add(1); // 컴파일 오류: 상한 제한 리스트에는 추가할 수 없습니다.
}
```

- **하한 제한 와일드카드 (`? super Type`)**: 알 수 없는 타입이 `Type`의 상위 타입입니다. 제네릭 구조에 *쓰기*를 원할 때 유용합니다.

```java
// 이 메서드는 Integer 또는 그 상위 클래스(Number, Object)의 List를 받을 수 있습니다.
public void addIntegers(List<? super Integer> list) {
    list.add(10);
    list.add(20);
    // Object item = list.get(0); // Object로만 안전하게 읽을 수 있습니다.
}
```

**PECS**(Producer Extends, Consumer Super)라는 니모닉은 어떤 와일드카드를 언제 사용해야 할지 기억하는 데 도움이 됩니다.

### 핵심 요약

제네릭은 현대 Java 프로그래밍의 초석입니다. 컴파일 시점에 강력한 타입 검사를 제공하고, 명시적 형변환의 필요성을 없애며, 개발자가 더 재사용 가능하고 견고한 코드를 작성할 수 있게 해줍니다. 항상 컬렉션과 함께 제네릭을 사용하고, 코드의 품질을 향상시키기 위해 자신만의 제네릭 클래스와 메서드를 만드는 것을 고려하세요.
