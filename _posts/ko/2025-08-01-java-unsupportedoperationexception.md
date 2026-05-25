---
typora-root-url: ../
layout: single
title: "java.lang.UnsupportedOperationException 처리 방법"

date: 2025-08-01T00:00:00+09:00
lang: ko
translation_id: java-unsupportedoperationexception
header:
   teaser: /images/header_images/overlay_image_java.png
   overlay_image: /images/header_images/overlay_image_java.png
   overlay_filter: 0.5
   image_description: >
     이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: java.lang.UnsupportedOperationException 처리 방법
excerpt: >
  `Arrays.asList()`와 같이 수정 불가능한 컬렉션을 수정하려고 할 때 주로 발생하는 `UnsupportedOperationException`을 이해하고 해결하는 방법을 알아봅니다.
seo_description: >
  `Arrays.asList()`와 같이 수정 불가능한 컬렉션을 수정하려고 할 때 주로 발생하는 `UnsupportedOperationException`을 이해하고 해결하는 방법을 알아봅니다.
categories:
  - ko_Troubleshooting
tags:
  - Java
  - Exception
  - Collections
  - UnsupportedOperationException
---


![이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: java.lang.UnsupportedOperationException 처리 방법](/images/header_images/overlay_image_java.png)
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

## 전문 보완 체크

**java.lang.UnsupportedOperationException 처리 방법**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 JDK 버전, 빌드 도구 설정, classpath 또는 module path, 런타임 stack trace를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

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

독자가 **java.lang.UnsupportedOperationException 처리 방법**의 첫 번째 권장 조치를 이미 시도했지만 결과가 여전히 불확실하다고 가정해 봅니다. 다음 단계는 여러 해결책을 한꺼번에 시험하는 것이 아니라 짧은 감사 기록을 만드는 것입니다. 먼저 어떤 판단을 하려는지 한 문장으로 쓰고, 환경을 한 문장으로 적고, 관찰된 결과를 한 문장으로 남깁니다. 그다음 JDK 버전, 빌드 도구 설정, classpath 또는 module path, 런타임 stack trace를 이미 확보한 사실과 대조합니다. 이렇게 해야 글이 서로 끊어진 팁 목록이 아니라 검증 가능한 절차가 됩니다.

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
