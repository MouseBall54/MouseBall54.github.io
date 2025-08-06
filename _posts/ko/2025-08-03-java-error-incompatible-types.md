---
typora-root-url: ../
layout: single
title: >
    Java "Error: incompatible types" 해결 방법

lang: ko
translation_id: java-error-incompatible-types
header:
    teaser: /images/header_images/overlay_image_java.png
    overlay_image: /images/header_images/overlay_image_java.png
    overlay_filter: 0.5
excerpt: >
    Java에서 "incompatible types" 오류는 서로 호환되지 않는 타입의 값을 변수에 할당하거나 메서드에 전달하려고 할 때 발생하는 컴파일 오류입니다. 이 글에서는 원인과 해결 방법을 알아봅니다.
categories:
    - ko_Troubleshooting
tags:
    - Java
    - Compilation Error
    - Type System
---

## Java "Error: incompatible types"란?

`Error: incompatible types`는 Java의 정적 타입 시스템(static type system)이 변수에 할당하려는 값의 타입이 변수 선언 시의 타입과 호환되지 않는다고 판단할 때 발생하는 컴파일 오류입니다. Java는 타입 안전성(type safety)을 중요하게 생각하므로, 컴파일러는 코드 실행 전에 타입 불일치 문제를 엄격하게 검사합니다.

오류 메시지는 보통 어떤 타입이 필요한데(required) 어떤 타입이 발견되었는지(found)를 명확히 알려줍니다.

**오류 메시지 형식:**
`incompatible types: <발견된 타입> cannot be converted to <필요한 타입>`

**오류 발생 예제:**
```java
public class TypeTest {
    public static void main(String[] args) {
        // 정수(int) 타입 변수에 문자열(String)을 할당하려고 함
        int number = "123"; 
    }
}
```

**컴파일 오류:**
```
TypeTest.java:4: error: incompatible types: String cannot be converted to int
        int number = "123";
                     ^
```

## "incompatible types"의 일반적인 원인과 해결 방법

### 1. 변수에 잘못된 타입의 값 할당

가장 기본적인 원인입니다. 변수에 선언된 타입과 다른 타입의 값을 직접 할당하려고 할 때 발생합니다.

-   **해결책**: 변수에 맞는 타입의 값을 할당하거나, 변수의 타입을 값에 맞게 변경합니다. 만약 타입 변환이 필요하다면, 적절한 변환 메서드를 사용해야 합니다.
    ```java
    // 해결 1: 올바른 타입의 값 할당
    int number = 123;

    // 해결 2: 문자열을 정수로 변환
    String text = "123";
    int numberFromString = Integer.parseInt(text);
    ```

### 2. 메서드 반환 타입과 변수 타입 불일치

메서드가 반환하는 값의 타입과 그 값을 받으려는 변수의 타입이 호환되지 않을 때 발생합니다.

-   **해결책**: 메서드의 반환 타입에 맞는 변수를 사용하거나, 메서드가 의도한 대로 올바른 타입을 반환하고 있는지 확인합니다.
    ```java
    public class MethodTest {
        public String getName() {
            return "Java";
        }

        public static void main(String[] args) {
            MethodTest mt = new MethodTest();
            // int nameLength = mt.getName(); // 오류: String을 int에 할당 불가
            String name = mt.getName(); // 올바른 타입
            int nameLength = name.length(); // String의 길이를 얻음
        }
    }
    ```

### 3. 상속 관계에서의 잘못된 타입 할당 (Downcasting)

부모 클래스 타입의 객체를 자식 클래스 타입의 변수에 명시적인 형변환(casting) 없이 할당하려고 할 때 발생합니다. 모든 `Dog`는 `Animal`이지만, 모든 `Animal`이 `Dog`는 아니기 때문입니다.

-   **해결책**: 자식 클래스로의 형변환이 안전한지 `instanceof` 연산자로 확인하고, 명시적으로 형변환을 수행합니다.
    ```java
    class Animal {}
    class Dog extends Animal {}

    public class CastingTest {
        public static void main(String[] args) {
            Animal myAnimal = new Dog();
            // Dog myDog = myAnimal; // 오류: Animal을 Dog에 할당 불가

            if (myAnimal instanceof Dog) {
                Dog myDog = (Dog) myAnimal; // 명시적 형변환
            }
        }
    }
    ```

### 4. 제네릭(Generics) 타입 불일치

제네릭을 사용하는 컬렉션 등에서 타입 매개변수가 일치하지 않을 때 발생합니다.

-   **해결책**: 선언된 제네릭 타입과 일치하는 타입의 객체를 사용합니다.
    ```java
    import java.util.ArrayList;
    import java.util.List;

    public class GenericTest {
        public static void main(String[] args) {
            List<String> names = new ArrayList<>();
            // names.add(123); // 오류: List<String>에 int를 추가할 수 없음
            names.add("Java"); // 정상
        }
    }
    ```

## 결론

`Error: incompatible types`는 Java의 강력한 타입 시스템 덕분에 런타임이 아닌 컴파일 시점에 잠재적인 버그를 잡을 수 있도록 도와주는 유용한 오류입니다. 이 오류를 만나면 컴파일러가 알려주는 "required" 타입과 "found" 타입을 주의 깊게 살펴보고, 두 타입이 호환되도록 코드를 수정해야 합니다. 값의 타입을 바꾸거나, 변수의 타입을 바꾸거나, 혹은 명시적인 형변환을 통해 문제를 해결할 수 있습니다.

