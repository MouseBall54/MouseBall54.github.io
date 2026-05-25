---
typora-root-url: ../
layout: single
title: "java.lang.ArrayIndexOutOfBoundsException 해결 방법"

date: 2025-01-08T07:12:00+09:00
lang: ko
translation_id: java-arrayindexoutofboundsexception
excerpt: "java.lang.ArrayIndexOutOfBoundsException은 배열의 유효한 인덱스 범위를 벗어나 접근할 때 발생하는 흔한 런타임 예외입니다. 이 글에서는 오류의 원인과 해결 방법을 자세히 알아봅니다."
seo_description: "java.lang.ArrayIndexOutOfBoundsException은 배열의 유효한 인덱스 범위를 벗어나 접근할 때 발생하는 흔한 런타임 예외입니다. 이 글에서는 오류의 원인과 해결 방법을 자세히 알아봅니다."
header:
   teaser: /images/header_images/overlay_image_java.png
   overlay_image: /images/header_images/overlay_image_java.png
   overlay_filter: 0.5
   image_description: >
     이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: java.lang.ArrayIndexOutOfBoundsException 해결 방법
categories:
  - ko_Troubleshooting
tags:
  - Java
  - Exception
  - Array
  - Troubleshooting
---


![이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: java.lang.ArrayIndexOutOfBoundsException 해결 방법](/images/header_images/overlay_image_java.png)
## java.lang.ArrayIndexOutOfBoundsException이란?

`java.lang.ArrayIndexOutOfBoundsException`은 Java에서 배열을 다룰 때 매우 흔하게 발생하는 런타임 예외다.
이 오류는 배열에 존재하지 않는 인덱스에 접근하려고 할 때 발생한다.
Java 배열의 인덱스는 `0`부터 시작하여 `배열의 길이 - 1`까지의 범위를 가진다.
만약 이 범위를 벗어나는 인덱스를 사용하면 JVM(Java Virtual Machine)은 이 예외를 던진다.

## 주요 원인

이 오류의 원인은 명확하다. 배열의 경계를 확인하지 않고 인덱스에 접근하는 것이다.

### 1. 잘못된 인덱스 값 사용

가장 흔한 경우로, 배열의 길이를 고려하지 않고 인덱스를 직접 사용할 때 발생한다.

```java
public class Example {
    public static void main(String[] args) {
        String[] fruits = {"Apple", "Banana", "Cherry"};
        // 배열의 길이는 3, 유효 인덱스는 0, 1, 2
        
        // 오류 발생: 인덱스 3은 존재하지 않음
        System.out.println(fruits[3]); 
    }
}
```

위 코드에서 `fruits` 배열의 길이는 3이므로 유효한 인덱스는 0, 1, 2다.
하지만 코드에서는 인덱스 3에 접근하려고 시도했기 때문에 `ArrayIndexOutOfBoundsException`이 발생한다.

### 2. 반복문에서의 조건 오류

반복문을 사용할 때, 반복 조건이 배열의 경계를 넘어서도록 설정되면 이 오류가 발생할 수 있다.

```java
public class LoopExample {
    public static void main(String[] args) {
        int[] numbers = new int[5]; // 인덱스는 0부터 4까지
        
        // 오류 발생: i가 5가 될 때 numbers[5]에 접근 시도
        for (int i = 0; i <= numbers.length; i++) {
            numbers[i] = i;
        }
    }
}
```

`for` 반복문의 조건이 `i <= numbers.length`로 설정되어 있다.
`numbers.length`는 5이므로, `i`는 0부터 5까지 반복된다.
`i`가 5가 되는 마지막 반복에서 `numbers[5]`에 접근하게 되어 예외가 발생한다.
반복 조건은 `i < numbers.length`가 되어야 올바르다.

### 3. 비어 있는 배열 접근

배열이 비어 있거나 `null`인 상태에서 특정 인덱스에 접근하려 할 때도 발생할 수 있다.
물론, `null`인 배열에 접근하면 `NullPointerException`이 먼저 발생한다.

## 해결 방법

### 1. 인덱스 범위 확인

배열에 접근하기 전에 항상 인덱스가 유효한 범위 내에 있는지 확인하는 것이 가장 기본적인 해결책이다.

```java
public class SafeAccessExample {
    public static void main(String[] args) {
        String[] fruits = {"Apple", "Banana", "Cherry"};
        int index = 3;

        if (index >= 0 && index < fruits.length) {
            System.out.println(fruits[index]);
        } else {
            System.out.println("잘못된 인덱스입니다: " + index);
        }
    }
}
```

이처럼 `if` 문을 사용하여 인덱스가 `0` 이상이고 `배열의 길이`보다 작은지 확인하면 오류를 예방할 수 있다.

### 2. 향상된 for문(for-each) 사용

배열의 모든 요소를 순차적으로 접근할 때는 인덱스를 직접 다루지 않는 향상된 `for`문을 사용하는 것이 더 안전하고 간결하다.

```java
public class ForEachExample {
    public static void main(String[] args) {
        String[] fruits = {"Apple", "Banana", "Cherry"};
        
        for (String fruit : fruits) {
            System.out.println(fruit);
        }
    }
}
```

향상된 `for`문은 내부적으로 배열의 경계를 관리하므로 `ArrayIndexOutOfBoundsException`이 발생할 여지가 없다.

## 결론

`ArrayIndexOutOfBoundsException`은 배열의 경계를 확인하지 않아 발생하는 단순하지만 치명적인 오류다.
배열 인덱스에 접근하기 전에는 항상 유효 범위를 확인하는 습관을 들이고, 가능하다면 인덱스를 직접 다루지 않는 향상된 `for`문을 활용하는 것이 좋다.
이러한 기본 원칙을 지키면 안정적인 코드를 작성하는 데 큰 도움이 된다.

## 전문 보완 체크

**java.lang.ArrayIndexOutOfBoundsException 해결 방법**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 JDK 버전, 빌드 도구 설정, classpath 또는 module path, 런타임 stack trace를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

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

독자가 **java.lang.ArrayIndexOutOfBoundsException 해결 방법**의 첫 번째 권장 조치를 이미 시도했지만 결과가 여전히 불확실하다고 가정해 봅니다. 다음 단계는 여러 해결책을 한꺼번에 시험하는 것이 아니라 짧은 감사 기록을 만드는 것입니다. 먼저 어떤 판단을 하려는지 한 문장으로 쓰고, 환경을 한 문장으로 적고, 관찰된 결과를 한 문장으로 남깁니다. 그다음 JDK 버전, 빌드 도구 설정, classpath 또는 module path, 런타임 stack trace를 이미 확보한 사실과 대조합니다. 이렇게 해야 글이 서로 끊어진 팁 목록이 아니라 검증 가능한 절차가 됩니다.

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
