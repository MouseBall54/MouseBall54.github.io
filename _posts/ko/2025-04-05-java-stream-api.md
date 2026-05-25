---
typora-root-url: ../
layout: single
title: >
   Java Stream API로 데이터 처리하기

date: 2025-04-05T07:54:00+09:00
lang: ko
translation_id: java-stream-api
header:
   teaser: /images/header_images/overlay_image_java.png
   overlay_image: /images/header_images/overlay_image_java.png
   overlay_filter: 0.5
   image_description: >
     이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Java Stream API로 데이터 처리하기
excerpt: >
    데이터 컬렉션 처리를 위한 Java Stream API의 강력한 기능을 알아보세요. 스트림을 사용하여 복잡한 데이터 조작을 위한 선언적이고 효율적이며 가독성 높은 코드를 작성하는 방법을 배웁니다.
seo_description: >
    데이터 컬렉션 처리를 위한 Java Stream API의 강력한 기능을 알아보세요. 스트림을 사용하여 복잡한 데이터 조작을 위한 선언적이고 효율적이며 가독성 높은 코드를 작성하는 방법을 배웁니다.
categories:
  - ko_Troubleshooting
tags:
  - Java
  - Stream API
  - Functional Programming
  - Collections
---

![이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Java Stream API로 데이터 처리하기](/images/header_images/overlay_image_java.png)
## Stream API란?

Java 8에서 도입된 **Stream API**는 컬렉션과 같은 요소의 시퀀스를 처리하기 위한 강력한 도구입니다. 스트림은 데이터 구조 자체가 아니며, 대신 컬렉션, 배열 또는 I/O 채널에서 입력을 받아 해당 데이터에 대해 함수형, 선언적 스타일로 복잡한 데이터 처리 연산을 수행할 수 있게 해줍니다.

### 스트림의 주요 특징

- **선언적(Declarative):** *어떻게* 할지가 아니라 *무엇을* 할지 설명합니다. 이는 전통적인 반복문에 비해 더 가독성 높은 코드로 이어집니다.
- **파이프라이닝(Pipelining):** 많은 스트림 연산은 스트림 자체를 반환하므로, 연산을 파이프라인으로 연결할 수 있습니다.
- **내부 반복(Internal Iteration):** 외부에서 반복하는(`for-each` 루프 등) 컬렉션과 달리, 스트림은 내부적으로 반복을 처리합니다.
- **소모성(Consumable):** 스트림은 한 번만 순회할 수 있습니다. 최종 연산이 수행된 후에는 스트림이 소모되어 재사용할 수 없습니다.

### 명령형에서 선언형 스타일로

간단한 작업을 예로 들어 보겠습니다: `Person` 객체 리스트가 주어졌을 때, 18세 이상인 모든 사람의 이름을 알파벳순으로 정렬하여 찾으세요.

**명령형 스타일 (전통적인 루프):**
```java
List<Person> people = ...;
List<String> result = new ArrayList<>();

for (Person p : people) {
    if (p.getAge() > 18) {
        result.add(p.getName());
    }
}

Collections.sort(result);
```
이 코드는 장황합니다. 중간 리스트를 만들고 반복과 정렬을 명시적으로 관리해야 합니다.

**선언형 스타일 (Stream API):**
```java
List<Person> people = ...;
List<String> result = people.stream() // 1. 리스트에서 스트림 얻기
    .filter(p -> p.getAge() > 18)      // 2. 18세 이상인 사람 필터링
    .map(Person::getName)              // 3. Person 객체를 이름으로 매핑
    .sorted()                          // 4. 이름 정렬
    .collect(Collectors.toList());     // 5. 결과를 새 리스트로 수집
```
이 스트림 파이프라인은 훨씬 더 간결하고 표현력이 풍부합니다. 연산의 순서를 명확하게 보여줍니다.

### 일반적인 스트림 연산

스트림 연산은 두 가지 범주로 나뉩니다:

#### 1. 중간 연산 (Intermediate Operations)

이러한 연산은 스트림을 다른 스트림으로 변환합니다. 항상 **지연(lazy)** 실행되며, 최종 연산이 호출될 때까지 실행되지 않습니다.

- **`filter(Predicate<T>)`**: 주어진 조건을 만족하는 요소로 구성된 스트림을 반환합니다.
- **`map(Function<T, R>)`**: 주어진 함수를 요소에 적용한 결과로 구성된 스트림을 반환합니다.
- **`sorted()`**: 정렬된 스트림을 반환합니다.
- **`distinct()`**: 중복된 요소가 제거된 스트림을 반환합니다.
- **`limit(long n)`**: 스트림의 길이를 `n` 이하로 자릅니다.

#### 2. 최종 연산 (Terminal Operations)

이러한 연산은 결과나 부수 효과(side-effect)를 생성합니다. 최종 연산이 수행된 후에는 스트림 파이프라인이 소모된 것으로 간주되어 다시 사용할 수 없습니다.

- **`collect(Collector<T, A, R>)`**: 요소를 `List`, `Set`, `Map`으로 수집하는 것과 같은 가변 축소 연산을 수행합니다.
- **`forEach(Consumer<T>)`**: 스트림의 각 요소에 대해 작업을 수행합니다.
- **`count()`**: 스트림의 요소 수를 반환합니다.
- **`findFirst()`**: 첫 번째 요소를 설명하는 `Optional`을 반환합니다.
- **`anyMatch(Predicate<T>)`**: 주어진 조건을 만족하는 요소가 있는지 여부를 반환합니다.
- **`reduce(...)`**: 스트림의 요소에 대한 축소 연산을 수행합니다 (예: 숫자 합산).

### 예시: 더 복잡한 파이프라인

30세 이상인 모든 고유하고 활성 상태인 직원의 총 급여를 찾아봅시다.

```java
class Employee {
    // name, age, salary, isActive에 대한 getter...
}

List<Employee> employees = ...;

double totalSalary = employees.stream()
    .filter(e -> e.getAge() > 30)       // 30세 이상 직원 유지
    .filter(Employee::isActive)         // 활성 상태 직원 유지
    .distinct()                         // 각 직원이 한 번만 계산되도록 보장
    .mapToDouble(Employee::getSalary)   // 급여를 DoubleStream으로 가져오기
    .sum();                             // 급여 합산
```

### 병렬 스트림 (Parallel Streams)

Stream API는 연산을 병렬화하는 것도 쉽게 만듭니다. `stream()` 대신 `parallelStream()`을 호출하기만 하면, API는 여러 스레드에 걸쳐 데이터를 병렬로 처리하려고 시도하여 멀티코어 프로세서에서 실행 속도를 높일 수 있습니다.

```java
long count = people.parallelStream()
    .filter(p -> p.getAge() > 18)
    .count();
```

**주의:** 병렬 스트림이 항상 더 빠른 것은 아닙니다. 오버헤드가 있으며, 대용량 데이터셋과 계산 비용이 높고 쉽게 병렬화할 수 있는 작업에 가장 적합합니다.

### 핵심 요약

Stream API는 현대 Java 개발의 필수적인 부분입니다. 복잡한 데이터 처리 작업을 위해 가독성 높고 선언적인 코드를 작성할 수 있게 해줍니다. 중간 연산과 최종 연산을 연결함으로써, 전통적인 명령형 코드보다 이해하기 쉬운 강력하고 효율적인 데이터 파이프라인을 만들 수 있습니다.

## 전문 보완 체크

**Java Stream API로 데이터 처리하기**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 JDK 버전, 빌드 도구 설정, classpath 또는 module path, 런타임 stack trace를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

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
