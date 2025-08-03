---
typora-root-url: ../
layout: single
title: >
    Java ConcurrentModificationException 처리 방법
date: 2025-08-03T11:10:00+09:00
header:
   teaser: /images/header_images/overlay_image_java.png
   overlay_image: /images/header_images/overlay_image_java.png
   overlay_filter: 0.5
excerpt: >
    Java에서 ConcurrentModificationException을 해결하는 방법을 배웁니다. 이 예외는 컬렉션을 반복하는 동안 수정될 때 발생합니다.
categories:
  - ko_Troubleshooting
tags:
  - Java
  - Exception
  - ConcurrentModificationException
  - Collections
---

## ConcurrentModificationException이란?

이 예외는 Java에서 발생합니다.
`ArrayList`나 `HashMap` 같은 컬렉션과 관련 있습니다.
오류는 반복(iteration) 중에 일어납니다.
컬렉션을 순회합니다.
동시에 컬렉션을 수정하려고 시도합니다.
수정은 요소 추가, 제거, 업데이트를 포함합니다.
이 행위는 대부분의 표준 컬렉션에서 허용되지 않습니다.
반복자(iterator)가 변경을 감지합니다.
그리고 `ConcurrentModificationException`을 발생시킵니다.
이것은 "fail-fast" 동작입니다.
동시 수정으로 인한 예측 불가능한 결과를 방지합니다.

## 주요 원인과 해결 방법

주요 원인은 컬렉션을 반복하면서 수정하는 것입니다.

### 반복 중 리스트 수정

흔한 실수는 for-each 루프 안에서 요소를 제거하는 것입니다.

**문제 코드:**
```java
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<String> fruits = new ArrayList<>();
        fruits.add("Apple");
        fruits.add("Banana");
        fruits.add("Cherry");

        // 이 루프는 ConcurrentModificationException을 발생시킵니다.
        for (String fruit : fruits) {
            if (fruit.equals("Banana")) {
                fruits.remove("Banana"); 
            }
        }
    }
}
```
for-each 루프는 내부적으로 반복자를 사용합니다.
`fruits.remove()` 호출은 리스트의 구조를 변경합니다.
반복자는 이를 감지하고 실패합니다.

**해결 방법 1: 반복자 명시적 사용**

반복자의 `remove()` 메서드를 사용할 수 있습니다.
이것이 반복 중에 컬렉션을 수정하는 안전한 방법입니다.

**수정된 코드:**
```java
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<String> fruits = new ArrayList<>();
        fruits.add("Apple");
        fruits.add("Banana");
        fruits.add("Cherry");

        Iterator<String> iterator = fruits.iterator();
        while (iterator.hasNext()) {
            String fruit = iterator.next();
            if (fruit.equals("Banana")) {
                iterator.remove(); // 안전한 제거
            }
        }
        System.out.println(fruits); // 출력: [Apple, Cherry]
    }
}
```

**해결 방법 2: `removeIf()` 사용 (Java 8 이상)**

간단한 조건부 제거를 위해 Java 8은 `removeIf()`를 도입했습니다.
더 간결하고 오류 발생 가능성이 적습니다.

**수정된 코드 (Java 8 이상):**
```java
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<String> fruits = new ArrayList<>();
        fruits.add("Apple");
        fruits.add("Banana");
        fruits.add("Cherry");

        fruits.removeIf(fruit -> fruit.equals("Banana")); // 깔끔하고 안전함

        System.out.println(fruits); // 출력: [Apple, Cherry]
    }
}
```

**해결 방법 3: 반복을 위한 복사본 생성**

컬렉션의 복사본을 순회할 수 있습니다.
그런 다음 원본 컬렉션을 안전하게 수정할 수 있습니다.
이 방법은 단순한 제거보다 복잡한 로직에 유용합니다.

**수정된 코드:**
```java
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<String> fruits = new ArrayList<>();
        fruits.add("Apple");
        fruits.add("Banana");
        fruits.add("Cherry");

        List<String> toRemove = new ArrayList<>();
        for (String fruit : fruits) {
            if (fruit.equals("Banana")) {
                toRemove.add(fruit);
            }
        }
        fruits.removeAll(toRemove);

        System.out.println(fruits); // 출력: [Apple, Cherry]
    }
}
```

## 결론

`ConcurrentModificationException`은 흔한 문제입니다.
멀티스레드 및 단일 스레드 코드의 버그로부터 사용자를 보호합니다.
for-each 루프 안에서 직접 컬렉션을 수정하지 마세요.
대신 `Iterator`, `removeIf()` 메서드, 또는 임시 컬렉션을 사용하세요.
올바른 방법을 선택하는 것은 특정 요구에 따라 다릅니다.
이러한 관행은 더 안전하고 깨끗한 Java 코드를 작성하는 데 도움이 됩니다.
