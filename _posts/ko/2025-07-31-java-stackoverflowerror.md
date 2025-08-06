---
typora-root-url: ../
layout: single
title: "Java StackOverflowError 해결 방법"

lang: ko
translation_id: java-stackoverflowerror
excerpt: "코드에서 무한 재귀를 식별하여 Java의 StackOverflowError를 이해하고 해결합니다. 재귀 함수를 디버깅하고, 반복적인 해결책으로 리팩토링하며, 필요할 때 스레드 스택 크기를 늘리는 방법을 배웁니다."
header:
   teaser: /images/header_images/overlay_image_java.png
   overlay_image: /images/header_images/overlay_image_java.png
   overlay_filter: 0.5
categories:
  - ko_Troubleshooting
tags:
  - Java
  - StackOverflowError
  - Recursion
  - JVM
  - Troubleshooting
---

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
