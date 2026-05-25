---
typora-root-url: ../
layout: single
title: "Java StackOverflowError 해결 방법"

date: 2025-02-12T07:47:00+09:00
lang: ko
translation_id: java-stackoverflowerror
excerpt: "코드에서 무한 재귀를 식별하여 Java의 StackOverflowError를 이해하고 해결합니다. 재귀 함수를 디버깅하고, 반복적인 해결책으로 리팩토링하며, 필요할 때 스레드 스택 크기를 늘리는 방법을 배웁니다."
seo_description: "코드에서 무한 재귀를 식별하여 Java의 StackOverflowError를 이해하고 해결합니다. 재귀 함수를 디버깅하고, 반복적인 해결책으로 리팩토링하며, 필요할 때 스레드 스택 크기를 늘리는 방법을 배웁니다."
header:
   teaser: /images/header_images/overlay_image_java.png
   overlay_image: /images/header_images/overlay_image_java.png
   overlay_filter: 0.5
   image_description: >
     이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Java StackOverflowError 해결 방법
categories:
  - ko_Troubleshooting
tags:
  - Java
  - StackOverflowError
  - Recursion
  - JVM
  - Troubleshooting
---


![이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Java StackOverflowError 해결 방법](/images/header_images/overlay_image_java.png)
## `StackOverflowError`란?

`java.lang.StackOverflowError`는 애플리케이션의 호출 스택이 소진되었음을 나타내는 Java의 런타임 오류다. 메서드가 호출될 때마다 새로운 "스택 프레임"이 호출 스택에 푸시된다. 이 프레임은 해당 메서드 호출의 지역 변수, 매개변수, 반환 주소를 저장한다. 중첩된 메서드 호출의 깊이가 너무 깊어지면 스택 공간이 부족해지고 JVM은 `StackOverflowError`를 발생시킨다.

이것은 `Exception`이 아닌 `Error`로, 애플리케이션이 일반적으로 잡으려고 시도해서는 안 되는 심각한 문제를 나타낸다.

## 주요 원인과 해결 방법

`StackOverflowError`의 압도적인 원인은 무한하거나 지나치게 깊은 재귀 호출이다.

### 1. 무한 재귀

이것이 고전적인 원인이다. 재귀 함수는 반드시 재귀를 멈추는 조건인 **기저 사례(base case)**를 가져야 한다. 이 기저 사례가 없거나, 잘못되었거나, 결코 충족되지 않으면 함수는 스택이 가득 찰 때까지 무한정 자신을 호출하게 된다.

#### 문제 코드

팩토리얼을 계산하지만 기저 사례가 없는 함수를 생각해보자.

```java
public class FactorialError {
    public static int calculate(int n) {
        // 기저 사례 누락: 재귀가 멈추지 않음
        return n * calculate(n - 1);
    }

    public static void main(String[] args) {
        try {
            calculate(5);
        } catch (StackOverflowError e) {
            System.err.println("StackOverflowError 발생!");
            // 오류는 표준 에러로 출력되지만, 여기서는 시연을 위해 잡음
        }
    }
}
```

이 예제에서 `calculate()`는 `5, 4, 3, 2, 1, 0, -1, -2, ...`로 호출되며 절대 종료되지 않는다.

#### 해결 방법: 기저 사례 추가

모든 재귀 함수가 반드시 도달할 수 있는 잘 정의된 기저 사례를 갖도록 해야 한다.

```java
public class FactorialSolution {
    public static int calculate(int n) {
        // 기저 사례: n이 1 이하일 때 재귀를 멈춤
        if (n <= 1) {
            return 1;
        }
        return n * calculate(n - 1);
    }

    public static void main(String[] args) {
        System.out.println("5의 팩토리얼: " + calculate(5)); // 출력: 120
    }
}
```

### 2. 깊지만 유한한 재귀

때로는 재귀가 무한하지는 않지만, 필요한 호출 횟수가 기본 스택 크기에 비해 너무 클 수 있다. 이는 깊은 트리나 긴 리스트와 같은 매우 큰 데이터 구조를 처리할 때 발생할 수 있다.

#### 문제 코드

매우 깊은 데이터 구조를 순회하는 함수는 스택을 소진시킬 수 있다.

```java
class Node {
    Node child;
}

public class DeepRecursion {
    public static int countDepth(Node node) {
        if (node == null) {
            return 0;
        }
        return 1 + countDepth(node.child);
    }

    public static void main(String[] args) {
        // 매우 깊은 연결 리스트 생성 (예: 100,000개 노드)
        Node head = new Node();
        Node current = head;
        for (int i = 0; i < 100000; i++) {
            current.child = new Node();
            current = current.child;
        }

        try {
            // StackOverflowError를 유발할 가능성이 높음
            countDepth(head);
        } catch (StackOverflowError e) {
            System.err.println("깊은 재귀로 인한 StackOverflowError 발생.");
        }
    }
}
```

#### 해결 방법 A: 스택 크기 늘리기

깊은 재귀가 합법적이고 피할 수 없는 경우, `-Xss` JVM 플래그를 사용하여 스레드 스택 크기를 늘릴 수 있다. 기본 크기는 JVM과 OS에 따라 다르지만 일반적으로 256k에서 1m 사이다.

```bash
# 스택 크기를 2MB로 설정
java -Xss2m -jar my-application.jar
```

**주의:** 이것은 최후의 수단으로 사용해야 한다. 스택 크기를 늘리면 각 스레드가 더 많은 메모리를 소비하게 되어 생성할 수 있는 총 스레드 수가 줄어든다. 근본적인 문제는 종종 재귀 알고리즘 자체에 있다.

#### 해결 방법 B: 재귀를 반복으로 변환

더 견고한 해결책은 재귀 알고리즘을 반복적인 알고리즘으로 리팩토링하는 것이다. 반복적인 해결책은 루프와 함께 `Stack`이나 `Queue`와 같은 데이터 구조를 사용하여 상태를 관리하며, 이는 호출 스택이 아닌 힙에 저장된다. 힙은 스택보다 훨씬 크다.

```java
import java.util.Stack;

class Node {
    Node child;
}

public class IterativeSolution {
    public static int countDepth(Node node) {
        int depth = 0;
        Node current = node;
        while (current != null) {
            depth++;
            current = current.child;
        }
        return depth;
    }

    public static void main(String[] args) {
        // 매우 깊은 연결 리스트 생성
        Node head = new Node();
        Node current = head;
        for (int i = 0; i < 100000; i++) {
            current.child = new Node();
            current = current.child;
        }
        
        // 이 반복적인 접근 방식은 StackOverflowError를 유발하지 않음
        int depth = countDepth(head);
        System.out.println("구조의 깊이: " + depth);
    }
}
```

## 결론

`StackOverflowError`는 거의 항상 잘못된 재귀 알고리즘의 직접적인 결과다. 디버깅의 첫 단계는 재귀 함수에 누락되거나 잘못된 기저 사례가 있는지 검사하는 것이다. 재귀가 유효하지만 너무 깊다면, 스택 크기를 늘리는 것에 의존하기 전에 반복적인 해결책으로 리팩토링하는 것을 고려해야 한다. 이는 더 확장 가능하고 메모리 효율적인 코드로 이어질 것이다.

## 전문 보완 체크

**Java StackOverflowError 해결 방법**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 JDK 버전, 빌드 도구 설정, classpath 또는 module path, 런타임 stack trace를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

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

독자가 **Java StackOverflowError 해결 방법**의 첫 번째 권장 조치를 이미 시도했지만 결과가 여전히 불확실하다고 가정해 봅니다. 다음 단계는 여러 해결책을 한꺼번에 시험하는 것이 아니라 짧은 감사 기록을 만드는 것입니다. 먼저 어떤 판단을 하려는지 한 문장으로 쓰고, 환경을 한 문장으로 적고, 관찰된 결과를 한 문장으로 남깁니다. 그다음 JDK 버전, 빌드 도구 설정, classpath 또는 module path, 런타임 stack trace를 이미 확보한 사실과 대조합니다. 이렇게 해야 글이 서로 끊어진 팁 목록이 아니라 검증 가능한 절차가 됩니다.

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
