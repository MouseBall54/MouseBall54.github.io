typora-root-url: ../
layout: single
title: >
   Java에서 equals()와 hashCode() 이해하기

lang: ko
translation_id: java-equals-and-hashcode
header:
   teaser: /images/header_images/overlay_image_java.png
   overlay_image: /images/header_images/overlay_image_java.png
   overlay_filter: 0.5
excerpt: >
    Java에서 equals()를 오버라이드할 때 왜 항상 hashCode()도 오버라이드해야 하는지 알아보세요. 이 두 메서드 간의 규약을 이해하고 해시 기반 컬렉션에서 어떻게 동작하는지 확인합니다.
categories:
  - ko_Troubleshooting
tags:
  - Java
  - equals
  - hashCode
  - Collections
  - Best Practices
---
## `equals()`와 `hashCode()` 사이의 규약

Java에서 `Object` 클래스에 정의된 `equals()`와 `hashCode()` 메서드는 객체의 동등성을 결정하는 데 기본이 됩니다. 사용자 정의 클래스를 만들 때, 참조 동등성(메모리 주소 기반)이 아닌 논리적 동등성(객체 상태 기반)을 정의하기 위해 종종 `equals()`를 오버라이드합니다.

하지만 이때 반드시 따라야 할 중요한 규칙이 있습니다: **`equals()`를 오버라이드하면, 반드시 `hashCode()`도 오버라이드해야 합니다.**

이는 `HashMap`, `HashSet`, `Hashtable`과 같은 해시 기반 컬렉션이 올바르게 작동하는 데 필수적인 두 메서드 간의 규약 때문입니다.

규약의 내용은 다음과 같습니다:
1.  `equals(Object)` 메서드에 따라 두 객체가 같다면, 각 객체의 `hashCode()` 메서드를 호출한 결과는 반드시 동일한 정수여야 합니다.
2.  `equals(Object)` 메서드에 따라 두 객체가 같지 않더라도, 각 객체의 `hashCode()` 메서드를 호출한 결과가 반드시 다른 정수일 필요는 없습니다. 그러나 같지 않은 객체에 대해 다른 결과를 생성하면 해시 테이블의 성능을 향상시킬 수 있습니다.

### 이 규약이 왜 중요한가?

해시 기반 컬렉션은 `hashCode()` 메서드를 사용하여 객체를 메모리의 어디에 저장할지 결정합니다(어떤 "버킷"에 넣을지). 객체를 검색하려고 할 때(예: `map.get(key)` 또는 `set.contains(object)`), 컬렉션은 다음을 수행합니다.

1.  찾으려는 객체의 해시 코드를 계산합니다.
2.  이 해시 코드를 사용하여 객체가 *있어야 할* 버킷을 빠르게 찾습니다.
3.  그런 다음 해당 버킷에 있는 (일반적으로 적은 수의) 객체들을 순회하며 `equals()` 메서드를 사용하여 정확한 일치 항목을 찾습니다.

### 규약을 어기면 어떻게 되는가?

`User` 클래스가 있고 `equals()`는 오버라이드했지만 `hashCode()`는 하지 않았다고 가정해 봅시다.

```java
class User {
    private int id;
    private String email;

    // 생성자, getter...

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        User user = (User) o;
        return id == user.id && email.equals(user.email);
    }

    // hashCode() 오버라이드가 누락되었습니다!
}
```

이제 이 클래스를 `HashSet`에서 사용해 보겠습니다.

```java
User user1 = new User(1, "test@example.com");
User user2 = new User(1, "test@example.com");

System.out.println("user1.equals(user2): " + user1.equals(user2)); // true

Set<User> userSet = new HashSet<>();
userSet.add(user1);

System.out.println("userSet.contains(user2): " + userSet.contains(user2)); // false!
```

**왜 `contains()`가 `false`를 반환할까요?**

1.  `userSet.add(user1)`이 호출되면, `HashSet`은 `user1.hashCode()`를 계산하고(`Object`의 기본 구현, 즉 메모리 주소 기반) 해당 해시 코드에 해당하는 버킷에 `user1`을 저장합니다.
2.  `userSet.contains(user2)`가 호출되면, `HashSet`은 `user2.hashCode()`를 계산합니다. `user1`과 `user2`는 메모리상 다른 객체이므로 기본 해시 코드가 다릅니다.
3.  `HashSet`은 `user2`의 해시 코드에 해당하는 버킷을 찾는데, 이는 `user1`이 저장된 버킷과 다른 버킷입니다. 아무것도 찾지 못했으므로 `equals()`를 호출하지도 않고 즉시 `false`를 반환합니다.

깨진 규약 때문에 컬렉션이 엉뚱한 곳을 찾아보게 되어, 논리적으로 동일한 객체를 찾지 못하는 것입니다.

### `hashCode()`를 올바르게 오버라이드하는 방법

이 문제를 해결하려면, 같다고 간주되는 객체에 대해 동일한 해시를 생성하도록 `hashCode()`를 구현해야 합니다. 좋은 `hashCode()` 구현은 `equals()` 메서드에서 사용된 동일한 필드를 사용해야 합니다.

**올바른 구현:**

```java
import java.util.Objects;

class User {
    private int id;
    private String email;

    // 생성자, getter...

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        User user = (User) o;
        return id == user.id && Objects.equals(email, user.email);
    }

    @Override
    public int hashCode() {
        // Objects.hash()를 사용하여 필드로부터 쉽게 해시 코드를 생성합니다.
        return Objects.hash(id, email);
    }
}
```

이렇게 수정된 `hashCode()`를 사용하면, `user1.hashCode()`와 `user2.hashCode()`는 동일한 값을 갖게 됩니다. 이제 `HashSet`은 올바른 버킷을 찾고 `equals()`를 사용하여 일치 여부를 확인하여 `contains()`에 대해 `true`를 반환합니다.

### 핵심 요약

`equals()`를 오버라이드할 때는 항상 `hashCode()`도 오버라이드하세요. 이를 수행하는 가장 쉽고 안전한 방법은 `java.util.Objects.hash()` 유틸리티 메서드를 사용하고, `equals()` 구현에 사용한 것과 동일한 필드를 전달하는 것입니다.
