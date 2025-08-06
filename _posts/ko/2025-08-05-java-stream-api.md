typora-root-url: ../
layout: single
title: >
   Java Stream API로 데이터 처리하기

lang: ko
translation_id: java-stream-api
header:
   teaser: /images/header_images/overlay_image_java.png
   overlay_image: /images/header_images/overlay_image_java.png
   overlay_filter: 0.5
excerpt: >
    데이터 컬렉션 처리를 위한 Java Stream API의 강력한 기능을 알아보세요. 스트림을 사용하여 복잡한 데이터 조작을 위한 선언적이고 효율적이며 가독성 높은 코드를 작성하는 방법을 배웁니다.
categories:
  - ko_Troubleshooting
tags:
  - Java
  - Stream API
  - Functional Programming
  - Collections
---
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
