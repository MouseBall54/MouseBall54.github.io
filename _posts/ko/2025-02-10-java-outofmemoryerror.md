---
typora-root-url: ../
layout: single
title: "Java OutOfMemoryError 해결 방법"

date: 2025-02-10T07:45:00+09:00
lang: ko
translation_id: java-outofmemoryerror
excerpt: "메모리 누수나 불충분한 힙 크기와 같은 원인을 파악하여 Java의 OutOfMemoryError를 이해하고 해결합니다. 힙 덤프를 분석하고 JVM 설정을 조정하여 이 심각한 오류를 예방하는 방법을 배웁니다."
seo_description: "메모리 누수나 불충분한 힙 크기와 같은 원인을 파악하여 Java의 OutOfMemoryError를 이해하고 해결합니다. 힙 덤프를 분석하고 JVM 설정을 조정하여 이 심각한 오류를 예방하는 방법을 배웁니다."
header:
   teaser: /images/header_images/overlay_image_java.png
   overlay_image: /images/header_images/overlay_image_java.png
   overlay_filter: 0.5
   image_description: >
     이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Java OutOfMemoryError 해결 방법
categories:
  - ko_Troubleshooting
tags:
  - Java
  - OutOfMemoryError
  - JVM
  - Memory Management
  - Troubleshooting
---


![이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Java OutOfMemoryError 해결 방법](/images/header_images/overlay_image_java.png)
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

## 전문 보완 체크

**Java OutOfMemoryError 해결 방법**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 JDK 버전, 빌드 도구 설정, classpath 또는 module path, 런타임 stack trace를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

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

## 함께 보면 좋은 글

같은 주제 흐름에서 이어서 읽기 좋은 글입니다.

- [SSL: CERTIFICATE_VERIFY_FAILED 오류 해결 방법 (Windows Python)](/ko_troubleshooting/python-certificate-verify-failed/)
- [Permission denied (publickey) 오류 해결 방법 (Windows Git SSH)](/ko_troubleshooting/git-permission-denied-publickey-windows/)
