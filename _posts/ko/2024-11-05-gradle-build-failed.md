---
typora-root-url: ../
layout: single
title: >
  Gradle build failed 해결 체크리스트
seo_title: >
  Gradle build failed 해결
date: 2024-11-05T07:45:00+09:00
last_modified_at: 2026-05-23T23:59:59+09:00
lang: ko
translation_id: gradle-build-failed
header:
   teaser: /images/2026-05-23-gradle-build-failed/gradle-build-failed-hero.png
   overlay_image: /images/2026-05-23-gradle-build-failed/gradle-build-failed-hero.png
   overlay_filter: 0.35
   image_description: >
     Gradle build failed 해결 체크리스트 주제를 한눈에 설명하는 시각 자료입니다.
excerpt: >
  Gradle build failed 오류를 첫 실패 task, --stacktrace, Gradle wrapper, Java version, dependency resolution, test report 순서로 디버깅합니다.
seo_description: >
  Gradle build failed 오류를 첫 실패 task, --stacktrace, Gradle wrapper, Java version, dependency resolution, test report 순서로 디버깅합니다.
categories:
  - ko_Troubleshooting
tags:
  - Gradle
  - Java
  - Build
  - SpringBoot
  - Troubleshooting
---

## 핵심 요약

`Gradle build failed`가 보이면 무작정 cache나 build directory를 지우기 전에 첫 번째로 실패한 task를 찾아야 합니다.
`--stacktrace`로 다시 실행하고, Gradle wrapper, Java version, dependency resolution, compile error, test failure를 분리해서 확인합니다.

![Gradle build pipeline에서 실패한 task와 진단 경로를 보여주는 이미지](/images/2026-05-23-gradle-build-failed/gradle-build-failed-hero.png)

이미지는 build pipeline을 보여줍니다.
하나의 task 실패가 전체 build 실패로 이어질 수 있습니다.
중요한 것은 뒤따르는 증상 전체가 아니라 첫 실패 task를 찾는 것입니다.

## 1. 첫 번째 실패 Task 읽기

실행합니다.

```bash
./gradlew build
```

Windows:

```powershell
.\gradlew.bat build
```

아래와 같은 첫 실패 line을 찾습니다.

```text
> Task :compileJava FAILED
> Task :test FAILED
> Task :bootJar FAILED
```

첫 실패가 가장 중요합니다.
뒤의 실패는 결과일 수 있습니다.

## 2. Stacktrace로 다시 실행

아래 명령을 사용합니다.

```bash
./gradlew build --stacktrace
```

dependency나 plugin 문제라면:

```bash
./gradlew build --info
```

`--debug`는 log가 매우 커질 수 있으므로 필요할 때만 사용합니다.

stacktrace는 실패가 Java compile error인지, test assertion인지, missing dependency인지, plugin version 문제인지, configuration 문제인지, permission 문제인지 알려줍니다.

## 3. Gradle Wrapper 사용

프로젝트 wrapper를 우선 사용합니다.

```bash
./gradlew --version
```

전역 설치된 `gradle`보다 wrapper가 안전합니다.
wrapper는 프로젝트가 기대하는 Gradle version을 고정합니다.

wrapper가 없다면 프로젝트 설정 문제입니다.
공유 repository라면 아래 파일들이 commit되어 있어야 합니다.

```text
gradlew
gradlew.bat
gradle/wrapper/gradle-wrapper.jar
gradle/wrapper/gradle-wrapper.properties
```

plugin과 Java version 호환성을 확인하지 않고 Gradle version을 조용히 바꾸면 안 됩니다.

## 4. Java Version 확인

많은 Gradle 실패는 실제로 Java version mismatch입니다.

확인합니다.

```bash
java -version
./gradlew --version
```

봐야 할 항목은 다음과 같습니다.

- Gradle이 사용하는 JVM
- 프로젝트가 요구하는 Java version
- toolchain configuration
- Spring Boot 또는 plugin compatibility

프로젝트가 Gradle Java toolchains를 사용한다면 Gradle이 의도한 version을 선택하게 둡니다.
그렇지 않다면 `JAVA_HOME`을 기대 JDK로 맞춥니다.

## 5. Dependency Resolution 분리

오류가 unresolved dependency, repository, metadata를 언급한다면 아래를 실행합니다.

```bash
./gradlew dependencies
```

특정 configuration을 확인하려면:

```bash
./gradlew dependencies --configuration runtimeClasspath
```

흔한 원인은 다음과 같습니다.

- group, artifact, version 오타
- repository 선언 누락
- private repository credential 누락
- corporate proxy 차단
- plugin repository 누락
- offline mode 활성화

최근 dependency를 바꿨다면 그 변경부터 isolate합니다.

## 6. Compile Failure와 Test Failure 분리

compile이 실패한다면:

```bash
./gradlew compileJava
```

Kotlin이라면:

```bash
./gradlew compileKotlin
```

test가 실패한다면:

```bash
./gradlew test
```

그리고 test report를 확인합니다.

```text
build/reports/tests/test/index.html
```

test skip을 기본 해결책으로 삼지 마세요.
`-x test`는 나머지 build가 되는지 확인할 때만 사용합니다.

```bash
./gradlew build -x test
```

그 다음 실패한 test를 고쳐야 합니다.

## 7. Clean은 필요할 때만 사용

아래 명령을 시도할 수 있습니다.

```bash
./gradlew clean build
```

이 명령은 project build output을 지웁니다.
dependency 실수, plugin incompatibility, 잘못된 source code를 고치지는 못합니다.

cache가 의심될 때는 dependency refresh를 사용합니다.

```bash
./gradlew build --refresh-dependencies
```

처음부터 전체 Gradle cache를 삭제하는 것은 피하는 편이 좋습니다.
느리고, 실제 원인을 숨길 수 있습니다.

## 흔한 실수

첫 번째 실수는 마지막 error만 보는 것입니다.
최종 summary는 너무 일반적일 수 있습니다.

두 번째 실수는 `./gradlew` 대신 전역 Gradle을 쓰는 것입니다.
개발자와 CI의 version 차이를 만들 수 있습니다.

세 번째 실수는 test를 영구적으로 skip하는 것입니다.
`-x test`로 build가 통과한다면 build가 고쳐진 것이 아니라 test failure가 확인된 것입니다.

네 번째 실수는 여러 version을 한 번에 바꾸는 것입니다.
Gradle, plugin, Java, dependency는 따로 바꿔야 어떤 변경이 결과를 만들었는지 알 수 있습니다.

## 함께 보면 좋은 글

- [Spring Boot port 8080 already in use 해결](/ko_troubleshooting/spring-boot-port-8080-already-in-use/)
- [Java incompatible types 오류 해결](/ko_troubleshooting/java-error-incompatible-types/)
- [Gradle: Troubleshooting builds](https://docs.gradle.org/current/userguide/troubleshooting.html)
- [Gradle: The Gradle Wrapper](https://docs.gradle.org/current/userguide/gradle_wrapper.html)

## 최종 체크리스트

```text
[ ] 첫 번째 실패 task를 찾았다.
[ ] `--stacktrace`로 다시 실행했다.
[ ] 전역 Gradle이 아니라 `./gradlew`를 사용했다.
[ ] Java version과 toolchain을 확인했다.
[ ] dependency resolution을 따로 확인했다.
[ ] compile failure와 test failure를 분리했다.
[ ] clean 또는 refresh는 원인을 좁힌 뒤 사용했다.
```

Gradle 실패는 build를 pipeline으로 보면 다루기 쉬워집니다.
첫 번째로 깨진 단계를 찾고, 그 단계만 직접 디버깅하세요.

## 자주 묻는 질문

### 이 글은 언제 먼저 적용하면 좋나요?

오류 메시지, 실행한 명령, 사용 중인 OS와 버전을 먼저 기록한 뒤 이 글의 원인별 순서대로 확인하는 것이 좋습니다.

### 초보자가 가장 먼저 확인할 부분은 무엇인가요?

처음에는 환경 변수, 설치 경로, 권한, 캐시처럼 재현 가능성이 높은 항목부터 확인하세요. 그다음 로그와 설정 파일을 비교하면 원인을 좁히기 쉽습니다.

### 더 찾아볼 때 어떤 키워드를 쓰면 좋나요?

추가 검색할 때는 "Gradle build failed 해결 체크리스트" 같은 핵심 문구와 error message, version, Windows, GitHub Pages, Jekyll 같은 실제 환경 키워드를 붙이면 더 정확한 결과를 얻기 쉽습니다.
