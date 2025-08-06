---
typora-root-url: ../
layout: single
title: "java.lang.UnsupportedOperationException 처리 방법"

lang: ko
translation_id: java-unsupportedoperationexception
header:
   teaser: /images/header_images/overlay_image_java.png
   overlay_image: /images/header_images/overlay_image_java.png
   overlay_filter: 0.5
excerpt: >
  `Arrays.asList()`와 같이 수정 불가능한 컬렉션을 수정하려고 할 때 주로 발생하는 `UnsupportedOperationException`을 이해하고 해결하는 방법을 알아봅니다.
categories:
  - ko_Troubleshooting
tags:
  - Java
  - Exception
  - Collections
  - UnsupportedOperationException
---

`java.lang.UnsupportedOperationException`은 요청된 작업이 지원되지 않음을 알리는 Java의 일반적인 런타임 예외입니다. 모든 메서드에서 발생할 수 있지만, Java 컬렉션 프레임워크로 작업할 때, 특히 수정 불가능한 컬렉션을 수정하려고 할 때 가장 자주 나타납니다.

이 글에서는 이 예외의 일반적인 원인을 살펴보고 명확한 해결책을 제공합니다.

### `UnsupportedOperationException`은 왜 발생하나요?

이 예외는 객체의 클래스나 인터페이스가 특정 메서드를 선언했음에도 불구하고 해당 객체가 그 메서드를 지원하지 않음을 나타내기 위해 발생합니다. 가장 고전적인 예는 고정 크기 또는 수정 불가능한 컬렉션에서 요소를 추가하거나 제거하려고 할 때입니다.

#### 일반적인 원인: `Arrays.asList()`의 리스트 수정

이 예외의 가장 빈번한 원인은 `java.util.Arrays.asList()`가 반환하는 `List`입니다.

```java
import java.util.Arrays;
import java.util.List;

public class ExceptionExample {
    public static void main(String[] args) {
        String[] array = {"one", "two"};
        List<String> list = Arrays.asList(array);

        // 이 줄에서 UnsupportedOperationException이 발생합니다
        list.add("three"); 
    }
}
```

**왜 이런 일이 발생할까요?**
`Arrays.asList()` 메서드는 표준 `java.util.ArrayList`를 생성하지 않습니다. 대신, 원본 배열을 감싸는 private 내부 클래스(`java.util.Arrays$ArrayList`)를 반환합니다. 이 리스트는 **고정 크기**입니다. 기존 요소를 변경할 수는 있지만(예: `list.set(0, "new_one")`), 요소를 추가하거나 제거하여 크기를 변경할 수는 없습니다. `add()` 및 `remove()` 메서드는 구현되지 않았으므로 `UnsupportedOperationException`을 발생시킵니다.

### 예외 해결 방법

해결책은 수정 불가능한 컬렉션에서 수정 가능한 새 컬렉션을 만드는 것입니다.

#### 해결책: 수정 가능한 `ArrayList` 생성하기

문제를 해결하려면 `Arrays.asList()`의 리스트를 새로운 `java.util.ArrayList` 인스턴스로 감싸세요. 이렇게 하면 모든 작업이 가능한, 수정 가능한 실제 복사본이 생성됩니다.

```java
import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;

public class SolutionExample {
    public static void main(String[] args) {
        String[] array = {"one", "two"};
        List<String> fixedList = Arrays.asList(array);

        // 고정 크기 리스트에서 수정 가능한 새 ArrayList 생성
        List<String> modifiableList = new ArrayList<>(fixedList);

        // 이제 이 코드는 완벽하게 작동합니다
        modifiableList.add("three"); 

        System.out.println(modifiableList); // 출력: [one, two, three]
    }
}
```

고정 크기 리스트를 `ArrayList` 생성자에 전달함으로써, 요소 추가 및 제거를 포함한 모든 컬렉션 작업을 지원하는 새 리스트를 만들 수 있습니다.

#### 다른 원인들

`Arrays.asList()`가 가장 일반적인 원인이지만, 다른 시나리오에서도 이 예외가 발생할 수 있습니다.

1.  **수정 불가능한 컬렉션**: `Collections.unmodifiableList()`, `Collections.unmodifiableSet()` 또는 `Collections.unmodifiableMap()`과 같은 메서드를 사용하는 경우. 이들은 명시적으로 수정을 방지하도록 설계되었습니다.
    ```java
    List<String> list = new ArrayList<>();
    list.add("a");
    List<String> unmodifiable = Collections.unmodifiableList(list);
    unmodifiable.add("b"); // UnsupportedOperationException 발생
    ```

2.  **불변 컬렉션 (Java 9 이상)**: `List.of()`, `Set.of()` 또는 `Map.of()`를 사용하는 경우. 이러한 팩토리 메서드는 진정한 불변 컬렉션을 생성합니다.
    ```java
    List<String> immutableList = List.of("a", "b");
    immutableList.add("c"); // UnsupportedOperationException 발생
    ```

3.  **맵의 키 집합**: `Map`의 `keySet()` 메서드는 키의 `Set` 뷰를 반환합니다. 이 집합에는 요소를 추가할 수 없지만, 제거는 가능합니다(맵에서도 해당 항목이 제거됨).

### 결론

`UnsupportedOperationException`은 객체가 설계되지 않은 작업을 수행하려고 한다는 명확한 신호입니다. 컬렉션과 관련하여 이 예외가 발생하면, 일반적으로 고정 크기 또는 수정 불가능한 컬렉션의 크기를 변경하려고 한다는 의미입니다. 표준 해결책은 기존 컬렉션에서 수정 가능한 새 컬렉션 인스턴스(예: `ArrayList` 또는 `HashSet`)를 만드는 것입니다.
