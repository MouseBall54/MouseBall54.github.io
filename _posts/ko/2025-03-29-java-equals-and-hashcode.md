---
typora-root-url: ../
layout: single
title: >
   Java에서 equals()와 hashCode() 이해하기

date: 2025-03-29T07:47:00+09:00
lang: ko
translation_id: java-equals-and-hashcode
header:
   teaser: /images/header_images/overlay_image_java.png
   overlay_image: /images/header_images/overlay_image_java.png
   overlay_filter: 0.5
   image_description: >
     이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Java에서 equals()와 hashCode() 이해하기
excerpt: >
    Java에서 equals()를 오버라이드할 때 왜 항상 hashCode()도 오버라이드해야 하는지 알아보세요. 이 두 메서드 간의 규약을 이해하고 해시 기반 컬렉션에서 어떻게 동작하는지 확인합니다.
seo_description: >
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

![이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Java에서 equals()와 hashCode() 이해하기](/images/header_images/overlay_image_java.png)
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

## 전문 보완 체크

**Java에서 equals()와 hashCode() 이해하기**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 JDK 버전, 빌드 도구 설정, classpath 또는 module path, 런타임 stack trace를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

### 신뢰도를 높이는 증거

작업을 바꾸기 전에는 객관적인 증거를 먼저 확인해야 합니다. 쓸 만한 증거에는 `java -version`, `javac -version`, Maven 또는 Gradle 출력, 가장 작은 실패 클래스가 포함됩니다. 증거가 서로 맞지 않으면 억지로 하나의 이야기로 합치지 말고 충돌 자체를 남겨야 합니다. 빠른 해결이 한 번 성공했더라도 같은 입력, 계정, 의존성, 기기 상태에서 다시 확인하지 않았다면 아직 확정된 해결책이라고 보기 어렵습니다.

### 검토 표

| 검토 항목 | 확인할 내용 | 중요한 이유 |
| --- | --- | --- |
| 범위 | 이 글이 다루는 정확한 사례 | 조언을 과도하게 적용하지 않게 합니다 |
| 기준 상태 | 변경 전 상태 | 되돌리기와 비교를 가능하게 합니다 |
| 변경 | 실제로 수행한 가장 작은 조치 | 숨은 부작용을 줄입니다 |
| 결과 | 변경 뒤 관찰한 출력 또는 반응 | 기대와 증거를 구분합니다 |
| 재확인 | 결론을 다시 볼 시점 | 글의 정확도를 유지합니다 |

### 예외 상황과 실패 모드

주요 위험은 증상만 고치고 원인을 남기는 상황, 서로 무관한 변경을 같은 테스트에 섞는 상황입니다. 생산 데이터, 개인정보, 돈, 건강, 법적 권리, 보안 복구가 관련되어 있다면 넓은 해결책을 바로 적용하기보다 먼저 증거를 모으는 보수적인 접근이 낫습니다. 같은 제목의 문제라도 환경이 다르면 원인이 달라질 수 있으므로, 독자는 명령이나 결정을 복사하기 전에 자신의 조건이 글의 가정과 맞는지 비교해야 합니다.

### 유지보수 기준

이 안내는 의존성, 운영체제, 빌드 도구가 바뀐 뒤 다시 확인해야 합니다. 좋은 업데이트는 글 전체를 다시 쓰는 것이 아니라 예시, 링크, 명령, 화면, 판단 기준이 현재 동작과 여전히 맞는지 확인하는 일입니다. 기존 결론이 유효하면 확인 날짜를 남기고, 바뀌었다면 무엇이 바뀌었고 왜 이전 조언만으로 부족한지 설명해야 합니다.

### 실행 전 질문

- 문제나 판단이 실제임을 보여 주는 가장 작은 관찰 신호는 무엇인가?
- 공식 출처는 무엇이고, 내부 판단은 어느 부분인가?
- 변경 전에 반드시 캡처해야 할 기록은 무엇인가?
- 어떤 결과가 나오면 이 글의 조언이 맞지 않는다고 볼 것인가?
- 같은 문제가 반복될 때 누가 이 기록을 다시 봐야 하는가?

## 함께 보면 좋은 글

같은 주제 흐름에서 이어서 읽기 좋은 글입니다.

- [SSL: CERTIFICATE_VERIFY_FAILED 오류 해결 방법 (Windows Python)](/ko_troubleshooting/python-certificate-verify-failed/)
- [Permission denied (publickey) 오류 해결 방법 (Windows Git SSH)](/ko_troubleshooting/git-permission-denied-publickey-windows/)
