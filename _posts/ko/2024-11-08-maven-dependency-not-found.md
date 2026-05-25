---
typora-root-url: ../
layout: single
title: >
  Maven dependency not found 오류 해결 방법
seo_title: >
  Maven dependency not found 해결
date: 2024-11-08T07:48:00+09:00
last_modified_at: 2026-05-23T23:59:59+09:00
lang: ko
translation_id: maven-dependency-not-found
header:
   teaser: /images/2026-05-23-maven-dependency-not-found/maven-dependency-not-found-hero.png
   overlay_image: /images/2026-05-23-maven-dependency-not-found/maven-dependency-not-found-hero.png
   overlay_filter: 0.35
   image_description: >
     Maven dependency not found 오류 해결 방법 주제를 한눈에 설명하는 시각 자료입니다.
excerpt: >
  Maven dependency not found 오류를 groupId, artifactId, version, repository, local cache, mirror, credential, dependency tree 순서로 해결합니다.
seo_description: >
  Maven dependency not found 오류를 groupId, artifactId, version, repository, local cache, mirror, credential, dependency tree 순서로 해결합니다.
categories:
  - ko_Troubleshooting
tags:
  - Maven
  - Java
  - Dependencies
  - Build
  - Troubleshooting
---

## 핵심 요약

`Maven dependency not found`는 Maven이 설정된 repository나 local cache에서 artifact를 찾지 못했다는 뜻입니다.
먼저 `groupId`, `artifactId`, `version` 좌표를 확인합니다.
그 다음 repository 선언, private repository credential, mirror 설정, stale local cache를 확인합니다.

![Maven dependency resolution 경로와 missing artifact node를 보여주는 이미지](/images/2026-05-23-maven-dependency-not-found/maven-dependency-not-found-hero.png)

이미지는 Maven의 dependency lookup 경로를 보여줍니다.
Maven은 좌표로 dependency를 찾습니다.
좌표가 틀렸거나 repository에 접근할 수 없으면 dependency tree에 missing node가 생깁니다.

## 대표 오류 메시지

아래와 비슷한 메시지가 나올 수 있습니다.

```text
Could not resolve dependencies for project ...
Could not find artifact group:artifact:jar:version
Failure to find ... was cached in the local repository
```

핵심 질문은 이것입니다.

```text
dependency 이름이 틀렸는가, 아니면 Maven이 잘못된 곳을 보고 있는가?
```

두 경우의 해결 방법은 다릅니다.

## 1. Dependency 좌표 확인

Maven dependency의 핵심 좌표는 세 가지입니다.

```xml
<dependency>
  <groupId>com.example</groupId>
  <artifactId>example-library</artifactId>
  <version>1.2.3</version>
</dependency>
```

확인할 항목:

- `groupId` 오타
- `artifactId` 오타
- 존재하지 않는 version
- snapshot repository 없이 snapshot version 사용
- packaging 또는 classifier 오류

Maven Central 또는 사내 repository browser에서 artifact를 직접 검색합니다.
블로그나 오래된 issue에 나온 version이라고 해서 실제 존재한다고 가정하면 안 됩니다.

## 2. Repository 확인

Maven Central은 기본으로 사용됩니다.
하지만 private artifact는 repository 선언이 필요합니다.

예시:

```xml
<repositories>
  <repository>
    <id>company-releases</id>
    <url>https://repo.example.com/releases</url>
  </repository>
</repositories>
```

plugin은 `repositories`가 아니라 `pluginRepositories`를 사용해야 합니다.
일반 dependency와 build plugin은 서로 다른 repository section을 통해 resolve됩니다.

internal dependency라면 다음을 확인합니다.

- repository URL이 맞는가?
- artifact가 그 repository에 publish되어 있는가?
- releases와 snapshots 중 어느 쪽을 지원하는가?
- build가 proxy나 mirror 뒤에서 실행되는가?

## 3. Private Repository Credential 확인

credential은 보통 `pom.xml`이 아니라 `~/.m2/settings.xml`에 둡니다.

예시:

```xml
<servers>
  <server>
    <id>company-releases</id>
    <username>...</username>
    <password>...</password>
  </server>
</servers>
```

`server`의 id는 `pom.xml` 또는 parent 설정의 repository id와 일치해야 합니다.
id가 다르면 Maven은 해당 repository에 credential을 사용하지 않습니다.

실제 password나 token을 source control에 commit하면 안 됩니다.

## 4. Cached Failed Resolution 제거

Maven은 실패한 lookup도 cache할 수 있습니다.
그래서 error에 cached라는 문구가 나올 수 있습니다.

snapshot과 metadata를 다시 확인하게 하려면:

```bash
mvn -U clean package
```

특정 dependency만 stuck 상태라면 local repository에서 해당 artifact directory만 삭제합니다.

```text
~/.m2/repository/com/example/example-library/
```

처음부터 `~/.m2/repository` 전체를 지우는 것은 피하는 편이 좋습니다.
다시 받는 데 오래 걸리고 실제 원인을 숨길 수 있습니다.

## 5. Dependency Tree 확인

실행합니다.

```bash
mvn dependency:tree
```

transitive dependency라면 어떤 library가 해당 dependency를 끌고 왔는지 볼 수 있습니다.

더 자세히 보려면:

```bash
mvn dependency:tree -Dverbose
```

version conflict가 있다면 dependency management로 의도한 version을 고정합니다.
잘못된 transitive dependency라면 가져오는 dependency에서 exclude하고, 올바른 dependency를 명시적으로 추가합니다.

## 6. Mirror와 Proxy 확인

회사 환경에서는 Maven mirror를 쓰는 경우가 많습니다.
`settings.xml`의 mirror가 모든 repository 요청을 다른 곳으로 보낼 수 있습니다.

아래 설정을 확인합니다.

```xml
<mirrors>
  <mirror>
    <mirrorOf>*</mirrorOf>
    <url>...</url>
  </mirror>
</mirrors>
```

mirror가 down 상태이거나, 오래되었거나, artifact를 가지고 있지 않으면 Maven Central에 artifact가 있어도 실패할 수 있습니다.
이 경우 mirror를 고치거나 repository admin에게 sync를 요청해야 합니다.

proxy 설정도 download를 막을 수 있습니다.
`settings.xml`과 network 환경을 같이 확인합니다.

## 흔한 실수

첫 번째 실수는 artifact 존재 여부를 확인하기 전에 코드를 바꾸는 것입니다.
dependency-not-found 오류는 대부분 좌표나 repository 문제입니다.

두 번째 실수는 repository를 잘못된 section에 추가하는 것입니다.
build plugin은 `pluginRepositories`가 필요합니다.

세 번째 실수는 credential을 `pom.xml`에 commit하는 것입니다.
`settings.xml` 또는 CI secret을 사용해야 합니다.

네 번째 실수는 Maven cache 전체를 즉시 삭제하는 것입니다.
먼저 `mvn -U` 또는 특정 artifact 삭제를 시도하세요.

## 전문 보완 체크

**Maven dependency not found 오류 해결 방법**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 JDK 버전, 빌드 도구 설정, classpath 또는 module path, 런타임 stack trace를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

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
- [Java Cannot Find Symbol 오류 해결](/ko_troubleshooting/java-error-cannot-find-symbol/)
- [Maven: Introduction to repositories](https://maven.apache.org/guides/introduction/introduction-to-repositories.html)
- [Maven: Dependency mechanism](https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html)

## 최종 체크리스트

```text
[ ] `groupId`, `artifactId`, `version`이 정확하다.
[ ] artifact가 Maven Central 또는 의도한 private repository에 존재한다.
[ ] repository 또는 plugin repository가 올바른 위치에 선언되어 있다.
[ ] private repository credential의 id가 repository id와 일치한다.
[ ] cached failure에 대해 `mvn -U`를 시도했다.
[ ] mirror와 proxy가 resolution을 막지 않는다.
[ ] `mvn dependency:tree`로 transitive dependency 문제를 확인했다.
```

Maven dependency 오류는 lookup 문제로 보면 해결이 빨라집니다.
Maven이 무엇을 찾는지 확인하고, 그 다음 어디를 볼 수 있는지 확인하세요.

## 자주 묻는 질문

### 이 글은 언제 먼저 적용하면 좋나요?

오류 메시지, 실행한 명령, 사용 중인 OS와 버전을 먼저 기록한 뒤 이 글의 원인별 순서대로 확인하는 것이 좋습니다.

### 초보자가 가장 먼저 확인할 부분은 무엇인가요?

처음에는 환경 변수, 설치 경로, 권한, 캐시처럼 재현 가능성이 높은 항목부터 확인하세요. 그다음 로그와 설정 파일을 비교하면 원인을 좁히기 쉽습니다.

### 더 찾아볼 때 어떤 키워드를 쓰면 좋나요?

추가 검색할 때는 "Maven dependency not found 오류 해결 방법" 같은 핵심 문구와 error message, version, Windows, GitHub Pages, Jekyll 같은 실제 환경 키워드를 붙이면 더 정확한 결과를 얻기 쉽습니다.
