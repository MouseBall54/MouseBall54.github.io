---
typora-root-url: ../
layout: single
title: >
    Java ConcurrentModificationException 처리 방법

date: 2025-03-02T07:20:00+09:00
lang: ko
translation_id: java-concurrentmodificationexception
header:
   teaser: /images/header_images/overlay_image_java.png
   overlay_image: /images/header_images/overlay_image_java.png
   overlay_filter: 0.5
   image_description: >
     이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Java ConcurrentModificationException 처리 방법
excerpt: >
    Java에서 ConcurrentModificationException을 해결하는 방법을 배웁니다. 이 예외는 컬렉션을 반복하는 동안 수정될 때 발생합니다.
seo_description: >
    Java에서 ConcurrentModificationException을 해결하는 방법을 배웁니다. 이 예외는 컬렉션을 반복하는 동안 수정될 때 발생합니다.
categories:
  - ko_Troubleshooting
tags:
  - Java
  - Exception
  - ConcurrentModificationException
  - Collections
---


![이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Java ConcurrentModificationException 처리 방법](/images/header_images/overlay_image_java.png)
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

## 전문 보완 체크

**Java ConcurrentModificationException 처리 방법**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 JDK 버전, 빌드 도구 설정, classpath 또는 module path, 런타임 stack trace를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

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

## 적용 검토 시나리오

독자가 **Java ConcurrentModificationException 처리 방법**의 첫 번째 권장 조치를 이미 시도했지만 결과가 여전히 불확실하다고 가정해 봅니다. 다음 단계는 여러 해결책을 한꺼번에 시험하는 것이 아니라 짧은 감사 기록을 만드는 것입니다. 먼저 어떤 판단을 하려는지 한 문장으로 쓰고, 환경을 한 문장으로 적고, 관찰된 결과를 한 문장으로 남깁니다. 그다음 JDK 버전, 빌드 도구 설정, classpath 또는 module path, 런타임 stack trace를 이미 확보한 사실과 대조합니다. 이렇게 해야 글이 서로 끊어진 팁 목록이 아니라 검증 가능한 절차가 됩니다.

### 감사 기록 양식

| 항목 | 예시 기준 | 이유 |
| --- | --- | --- |
| 관찰 | 조치 전 실제로 본 내용 | 기준 상태를 객관화합니다 |
| 증거 | `java -version`, `javac -version` | 판단을 기록에 연결합니다 |
| 가정 | 믿고 있지만 아직 증명하지 못한 내용 | 숨은 추정을 드러냅니다 |
| 조치 | 한 번에 하나의 변경 | 결과의 원인을 추적하게 합니다 |
| 중단 기준 | 멈추고 도움을 요청할 조건 | 반복적인 시행착오를 줄입니다 |

### 품질 경계

같은 결과가 통제된 재확인 뒤에도 반복될 때만 이 안내를 강한 결론으로 보아야 합니다. 계정, 기기, 데이터 샘플, 의존성 버전, 계약 조건, 공식 규칙이 달라졌다면 결론의 강도를 낮추고 가설로 다루는 편이 안전합니다. 검색 독자는 급한 문제를 안고 들어오는 경우가 많아 맥락을 건너뛰기 쉽습니다. 전문적인 글은 위험한 판단을 천천히 하게 만들면서도 다음 행동은 분명하게 제시해야 합니다.

## 함께 보면 좋은 글

같은 주제 흐름에서 이어서 읽기 좋은 글입니다.

- [SSL: CERTIFICATE_VERIFY_FAILED 오류 해결 방법 (Windows Python)](/ko_troubleshooting/python-certificate-verify-failed/)
- [Permission denied (publickey) 오류 해결 방법 (Windows Git SSH)](/ko_troubleshooting/git-permission-denied-publickey-windows/)
