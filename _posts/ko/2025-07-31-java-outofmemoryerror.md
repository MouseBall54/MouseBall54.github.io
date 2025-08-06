---
typora-root-url: ../
layout: single
title: "Java OutOfMemoryError 해결 방법"

lang: ko
translation_id: java-outofmemoryerror
excerpt: "메모리 누수나 불충분한 힙 크기와 같은 원인을 파악하여 Java의 OutOfMemoryError를 이해하고 해결합니다. 힙 덤프를 분석하고 JVM 설정을 조정하여 이 심각한 오류를 예방하는 방법을 배웁니다."
header:
   teaser: /images/header_images/overlay_image_java.png
   overlay_image: /images/header_images/overlay_image_java.png
   overlay_filter: 0.5
categories:
  - ko_Troubleshooting
tags:
  - Java
  - OutOfMemoryError
  - JVM
  - Memory Management
  - Troubleshooting
---

## `OutOfMemoryError`란?

`java.lang.OutOfMemoryError`(OOM)는 Java 개발자가 직면할 수 있는 가장 심각한 오류 중 하나다. 이것은 일반적인 예외(`Exception`)가 아니라 `Error`로, 일반적인 애플리케이션이 잡으려고 시도해서는 안 되는 심각한 문제를 나타낸다. 이 오류는 Java 가상 머신(JVM)이 메모리 부족으로 객체를 할당할 수 없고, 가비지 컬렉터(GC)가 더 이상 메모리를 확보할 수 없을 때 발생한다.

여러 종류의 `OutOfMemoryError`가 있지만, 가장 흔한 것은 `java.lang.OutOfMemoryError: Java heap space`이다.

## 주요 원인과 해결 방법

이 오류의 주된 원인과 해결 방법을 살펴보자.

### 1. 불충분한 힙 크기 (단순한 경우)

때로는 애플리케이션이 JVM이 할당한 기본 힙 크기보다 실제로 더 많은 메모리를 필요로 하는 경우가 있다.

#### 해결 방법: 힙 크기 늘리기

`-Xmx` JVM 플래그를 사용하여 최대 힙 크기를 늘릴 수 있다. 예를 들어, 최대 힙 크기를 2GB로 설정하려면 다음과 같이 한다.

```bash
java -Xmx2g -jar my-application.jar
```

*   `-Xms`: 초기 힙 크기를 설정한다.
*   `-Xmx`: 최대 힙 크기를 설정한다.

초기 크기와 최대 크기를 동일한 값으로 설정하면(예: `-Xms2g -Xmx2g`) JVM이 힙 크기를 조정하는 것을 방지하여 메모리를 많이 사용하는 애플리케이션에서 약간의 성능 향상을 기대할 수 있다.

하지만 단순히 힙 크기를 늘리는 것은 종종 임시방편에 불과하다. 근본 원인이 메모리 누수라면, 애플리케이션은 결국 다시 사용 가능한 모든 메모리를 소모하게 될 것이다.

### 2. 메모리 누수 (일반적인 주범)

메모리 누수는 `OutOfMemoryError`의 가장 흔한 원인이다. Java에서 메모리 누수는 애플리케이션에서 더 이상 필요하지 않은 객체가 여전히 참조되고 있어 가비지 컬렉터가 제거하지 못할 때 발생한다. 시간이 지남에 따라 이러한 참조되지 않는 객체들이 쌓여 힙 공간을 가득 채우게 된다.

#### 메모리 누수의 일반적인 원인:

*   **정적(Static) 필드:** `static` 필드에 의해 참조되는 객체는 명시적으로 `null`로 설정하지 않는 한 애플리케이션의 전체 수명 동안 메모리에 남아있다.
*   **닫히지 않은 리소스:** 스트림, 연결 또는 세션과 같은 리소스를 닫지 않으면 객체가 메모리에 남아있게 된다.
*   **부적절한 `equals()` 및 `hashCode()`:** `HashMap`의 키나 `HashSet`의 요소로 객체를 사용할 때, 잘못된 `hashCode()` 또는 `equals()` 구현은 중복 항목을 유발하고 객체가 제거되는 것을 막을 수 있다.
*   **ThreadLocals:** 애플리케이션 서버에서 제대로 정리되지 않은 `ThreadLocal` 변수는 메모리 누수를 유발할 수 있다. 애플리케이션 서버의 스레드는 종종 풀링되어 재사용되기 때문이다.

#### 해결 방법: 힙 덤프 분석

메모리 누수를 진단하는 가장 효과적인 방법은 힙 덤프를 분석하는 것이다. 힙 덤프는 Java 프로세스의 메모리 스냅샷이다.

1.  **힙 덤프 생성:**
    다음 플래그를 사용하여 `OutOfMemoryError`가 발생할 때 JVM이 자동으로 힙 덤프를 생성하도록 구성할 수 있다.

    ```bash
    java -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/path/to/heapdumps -jar my-application.jar
    ```
    이렇게 하면 지정된 디렉터리에 `.hprof` 파일이 생성된다.

2.  **덤프 분석:**
    메모리 분석 도구를 사용하여 힙 덤프 파일을 검사한다. 인기 있는 도구는 다음과 같다.
    *   **Eclipse Memory Analyzer (MAT):** 힙 덤프를 분석하기 위한 강력한 오픈 소스 도구다. 잠재적인 메모리 누수를 자동으로 식별할 수 있다.
    *   **VisualVM:** JDK에 포함되어 있으며, 힙 덤프를 생성하고 메모리 사용량에 대한 개요를 제공할 수 있다.
    *   **YourKit 및 JProfiler:** 고급 메모리 분석 기능을 갖춘 상용 프로파일러다.

덤프를 분석할 때 다음을 찾아보자.
*   **거대한 객체 컬렉션:** 제어할 수 없이 커지는 `List`나 `Map`.
*   **수명이 짧아야 하지만 그렇지 않은 객체:** 어떤 객체가 이들을 참조하여 가비지 컬렉션되지 못하게 하는지 식별한다.

### 3. Finalizer의 과도한 사용

`finalize()` 메서드가 있는 객체는 가비지 컬렉터의 특별한 처리가 필요하다. 이들은 낮은 우선순위의 별도 스레드에서 실행되는 파이널라이제이션 큐에 들어간다. 만약 파이널라이저 스레드가 객체 생성 속도를 따라가지 못하면, 힙은 파이널라이즈되기를 기다리는 객체로 가득 차 `OutOfMemoryError`를 유발할 수 있다.

#### 해결 방법: Finalizer 사용 자제

`finalize()`의 사용은 강력히 권장되지 않는다. 예측 불가능하며 성능 문제와 메모리 문제를 일으킬 수 있다. 대신 `try-with-resources`나 명시적인 `close()` 메서드를 사용하여 리소스를 결정론적으로 관리해야 한다.

## 결론

`OutOfMemoryError`는 신중한 조사가 필요한 심각한 문제다. 힙 크기를 늘리는 것이 빠른 해결책이 될 수 있지만, 종종 근본적인 메모리 누수를 가릴 뿐이다. 가장 좋은 접근 방식은 애플리케이션의 메모리 사용량을 사전에 분석하고, 오류 발생 시 힙 덤프를 생성하며, Eclipse MAT와 같은 도구를 사용하여 근본 원인을 정확히 찾아내는 것이다. 애플리케이션이 메모리를 어떻게 관리하는지 이해함으로써 더 견고하고 확장 가능한 Java 애플리케이션을 구축할 수 있다.
