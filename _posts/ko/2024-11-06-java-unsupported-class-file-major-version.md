---
typora-root-url: ../
layout: single
title: >
  Unsupported Class File Major Version 해결: Java JDK 버전 불일치 고치기
seo_title: >
  Unsupported Class File Major Version 해결
date: 2024-11-06T07:46:00+09:00
last_modified_at: 2026-05-23T23:59:59+09:00
lang: ko
translation_id: java-unsupported-class-file-major-version
header:
   teaser: /images/2026-05-23-java-unsupported-class-file-major-version/java-class-file-version-hero.png
   overlay_image: /images/2026-05-23-java-unsupported-class-file-major-version/java-class-file-version-hero.png
   overlay_filter: 0.35
   image_description: >
     Unsupported Class File Major Version 해결: Java JDK 버전 불일치 고치기 주제를 한눈에 설명하는 시각 자료입니다.
excerpt: >
  Unsupported class file major version 오류를 Java runtime, compiler, Gradle/Maven toolchain, target release 버전 정렬로 해결합니다.
seo_description: >
  Unsupported class file major version 오류를 Java runtime, compiler, Gradle/Maven toolchain, target release 버전 정렬로 해결합니다.
categories:
  - ko_Troubleshooting
tags:
  - Java
  - JDK
  - Gradle
  - Maven
  - Troubleshooting
---

## 핵심 요약

`Unsupported class file major version`은 Java runtime이나 build tool이 자신보다 새 Java 버전으로 compile된 bytecode를 읽으려 할 때 발생합니다.
더 새 JDK로 실행하거나, Gradle, Maven, `javac --release`를 사용해 더 낮은 target으로 compile해야 합니다.

![Java class file version mismatch와 JDK 정렬 경로를 보여주는 이미지](/images/2026-05-23-java-unsupported-class-file-major-version/java-class-file-version-hero.png)

이미지는 mismatch를 보여줍니다.
compiler는 새 class file을 만들었지만 runtime 또는 build tool이 더 오래된 버전입니다.
해결은 build JDK, runtime JDK, target release를 맞추는 것입니다.

## 대표 오류 메시지

아래와 비슷한 오류가 나옵니다.

```text
java.lang.UnsupportedClassVersionError:
Unsupported class file major version 61
```

또는:

```text
Unsupported class file major version 65
```

숫자는 class file version을 뜻합니다.
자주 보는 mapping은 다음과 같습니다.

| Major Version | Java Version |
| ---: | --- |
| 52 | Java 8 |
| 55 | Java 11 |
| 61 | Java 17 |
| 65 | Java 21 |

예를 들어 Java 11이 Java 17 bytecode를 실행하려 하면 major version `61` 오류가 날 수 있습니다.

## 1. Java Runtime 확인

먼저 확인합니다.

```bash
java -version
```

compiler도 확인합니다.

```bash
javac -version
```

`java`와 `javac`가 서로 다른 version을 가리키면 `JAVA_HOME`과 `PATH`를 고쳐야 합니다.

macOS 또는 Linux:

```bash
echo $JAVA_HOME
which java
```

Windows PowerShell:

```powershell
echo $env:JAVA_HOME
where.exe java
```

IDE가 사용하는 runtime은 terminal과 다를 수 있습니다.
IDE project SDK도 같이 확인하세요.

## 2. Gradle 또는 Maven JVM 확인

Gradle:

```bash
./gradlew --version
```

Maven:

```bash
mvn -version
```

이 명령은 build tool이 어떤 JVM으로 실행되는지 보여줍니다.
build tool이 오래된 JDK에서 실행되면 application 시작 전부터 실패할 수 있습니다.

Gradle 프로젝트라면 Java toolchains 사용이 좋습니다.

```groovy
java {
    toolchain {
        languageVersion = JavaLanguageVersion.of(17)
    }
}
```

Maven에서는 compiler plugin 설정을 확인합니다.

```xml
<maven.compiler.release>17</maven.compiler.release>
```

프로젝트가 실제로 지원하는 version을 사용해야 합니다.

## 3. Runtime을 올릴지 Target을 낮출지 결정

유효한 해결책은 두 가지입니다.

```text
Option A: 더 새 JDK로 실행한다.
Option B: 더 낮은 Java target으로 compile한다.
```

프로젝트가 새 Java feature나 framework version을 요구한다면 Option A가 맞습니다.
배포 환경이 오래된 Java로 고정되어 있다면 Option B를 선택합니다.

무작정 target만 낮추면 안 됩니다.
source code가 새 API를 사용한다면 `--release`나 올바른 toolchain 없이 compile/실행 불일치가 생길 수 있습니다.

## 4. Dependency Bytecode 확인

내 코드는 Java 11 target인데 dependency가 Java 17 또는 Java 21로 compile되어 있을 수 있습니다.
이 경우 library를 load하는 과정에서 오류가 날 수 있습니다.

해결 방법:

- runtime JDK를 올린다.
- 호환되는 낮은 dependency version을 사용한다.
- library release note에서 최소 Java version을 확인한다.
- Spring Boot, Gradle, Maven, plugin version을 정렬한다.

dependency upgrade 직후 자주 발생합니다.
stacktrace에서 처음 언급되는 dependency를 먼저 봅니다.

## 5. JDK 변경 후 Clean

Java version을 바꾼 뒤에는 build output을 지웁니다.

```bash
./gradlew clean build
```

또는:

```bash
mvn clean test
```

기존 `.class` 파일이 `build/` 또는 `target/`에 남아 있을 수 있습니다.
clean은 의도한 version으로 다시 compile하게 만듭니다.

## 흔한 실수

첫 번째 실수는 `JAVA_HOME`만 바꾸고 IDE SDK는 그대로 두는 것입니다.
terminal과 IDE가 다른 JDK를 쓸 수 있습니다.

두 번째 실수는 build tool JVM을 확인하지 않는 것입니다.
전역 Gradle/Maven과 project wrapper의 동작이 다를 수 있습니다.

세 번째 실수는 compiler target만 낮추고 dependency 최소 Java version을 보지 않는 것입니다.

네 번째 실수는 local Java만 고치고 CI 설정을 잊는 것입니다.
CI image와 setup action도 맞춰야 합니다.

## 전문 보완 체크

**Unsupported Class File Major Version 해결: Java JDK 버전 불일치 고치기**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 JDK 버전, 빌드 도구 설정, classpath 또는 module path, 런타임 stack trace를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

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

## 함께 보면 좋은 글

- [Gradle build failed 해결 체크리스트](/ko_troubleshooting/gradle-build-failed/)
- [Maven dependency not found 해결](/ko_troubleshooting/maven-dependency-not-found/)
- [Oracle Java Virtual Machine Specification: ClassFile format](https://docs.oracle.com/javase/specs/jvms/se21/html/jvms-4.html)
- [Gradle Java toolchains](https://docs.gradle.org/current/userguide/toolchains.html)

## 최종 체크리스트

```text
[ ] `java -version`이 기대 version이다.
[ ] `javac -version`이 project target과 맞다.
[ ] Gradle 또는 Maven이 기대 JDK로 실행된다.
[ ] compiler target 또는 release가 설정되어 있다.
[ ] dependency가 선택한 Java version을 지원한다.
[ ] CI와 IDE 설정이 local 설정과 맞다.
```

이 오류는 version alignment 문제입니다.
runtime, compiler, build tool, dependency가 같은 기준을 바라보면 해결됩니다.

## 자주 묻는 질문

### 이 글은 언제 먼저 적용하면 좋나요?

오류 메시지, 실행한 명령, 사용 중인 OS와 버전을 먼저 기록한 뒤 이 글의 원인별 순서대로 확인하는 것이 좋습니다.

### 초보자가 가장 먼저 확인할 부분은 무엇인가요?

처음에는 환경 변수, 설치 경로, 권한, 캐시처럼 재현 가능성이 높은 항목부터 확인하세요. 그다음 로그와 설정 파일을 비교하면 원인을 좁히기 쉽습니다.

### 더 찾아볼 때 어떤 키워드를 쓰면 좋나요?

추가 검색할 때는 "Unsupported Class File Major Version 해결: Java JDK 버전 불일치 고치기" 같은 핵심 문구와 error message, version, Windows, GitHub Pages, Jekyll 같은 실제 환경 키워드를 붙이면 더 정확한 결과를 얻기 쉽습니다.
