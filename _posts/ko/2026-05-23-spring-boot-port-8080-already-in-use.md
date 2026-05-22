---
typora-root-url: ../
layout: single
title: >
  Spring Boot port 8080 already in use 해결 방법
seo_title: >
  Spring Boot port 8080 already in use 해결
date: 2026-05-23T23:59:57+09:00
lang: ko
translation_id: spring-boot-port-8080-already-in-use
header:
   teaser: /images/2026-05-23-spring-boot-port-8080-already-in-use/spring-boot-port-8080-hero.png
   overlay_image: /images/2026-05-23-spring-boot-port-8080-already-in-use/spring-boot-port-8080-hero.png
   overlay_filter: 0.35
excerpt: >
  Spring Boot port 8080 already in use 오류를 포트 점유 프로세스 확인, 안전한 종료, server.port 변경, Docker/IDE 세션 점검 순서로 해결합니다.
seo_description: >
  Spring Boot port 8080 already in use 오류를 포트 점유 프로세스 확인, 안전한 종료, server.port 변경, Docker/IDE 세션 점검 순서로 해결합니다.
categories:
  - ko_Troubleshooting
tags:
  - Java
  - SpringBoot
  - Port8080
  - Backend
  - Troubleshooting
---

## 핵심 요약

Spring Boot web application은 기본적으로 `8080` 포트를 사용하는 경우가 많습니다.
이미 다른 process가 해당 포트를 사용 중이면 application이 시작되지 않습니다.
포트를 점유한 process를 찾고, 올바른 process를 종료하거나, `server.port`로 Spring Boot 포트를 바꾸면 됩니다.

![Spring Boot 로컬 서버 포트 충돌과 대체 포트 설정 흐름을 보여주는 이미지](/images/2026-05-23-spring-boot-port-8080-already-in-use/spring-boot-port-8080-hero.png)

이미지는 일반적인 두 가지 해결책을 보여줍니다.
점유된 포트를 비우거나, application을 다른 포트로 실행하는 것입니다.
무엇이 포트를 쓰는지 확인하기 전에는 임의로 process를 종료하지 않는 편이 안전합니다.

## 대표 오류 메시지

아래와 비슷한 메시지가 나옵니다.

```text
Web server failed to start. Port 8080 was already in use.
```

다음 명령에서 발생할 수 있습니다.

```bash
./gradlew bootRun
mvn spring-boot:run
java -jar app.jar
```

application code 자체가 문제는 아닐 수 있습니다.
embedded web server가 포트를 bind하기 전에 실패한 것입니다.

## 1. 어떤 Process가 포트를 쓰는지 확인

Windows PowerShell:

```powershell
Get-NetTCPConnection -LocalPort 8080 | Select-Object LocalAddress,LocalPort,State,OwningProcess
```

그 다음 process를 확인합니다.

```powershell
Get-Process -Id <PID>
```

macOS 또는 Linux:

```bash
lsof -i :8080
```

또는:

```bash
ss -ltnp | grep ':8080'
```

목표는 소유자를 찾는 것입니다.
다른 Spring Boot app, Node dev server, container port mapping, IDE run configuration, local proxy가 원인일 수 있습니다.

## 2. 올바른 Process를 종료

예전 dev server라면 먼저 정상 종료합니다.
실행 중인 terminal에서 다음을 누릅니다.

```text
Ctrl+C
```

IDE에서 실행했다면 run configuration을 stop합니다.
container라면 container를 stop합니다.

강제 종료는 안전하다고 확신할 때만 사용합니다.

Windows:

```powershell
Stop-Process -Id <PID>
```

macOS 또는 Linux:

```bash
kill <PID>
```

정상 종료가 안 될 때만:

```bash
kill -9 <PID>
```

잘못된 process를 종료하면 database, proxy, 다른 개발 도구를 끊을 수 있습니다.

## 3. Spring Boot Port 변경

두 서비스를 동시에 실행해야 한다면 application port를 바꿉니다.

`src/main/resources/application.properties`:

```properties
server.port=8081
```

`application.yml`:

```yaml
server:
  port: 8081
```

실행 시점에 넘길 수도 있습니다.

```bash
java -jar app.jar --server.port=8081
```

Gradle에서는:

```bash
./gradlew bootRun --args='--server.port=8081'
```

여러 서비스를 함께 띄우는 개발 환경에서는 이 방식이 가장 깔끔한 경우가 많습니다.

## 4. 테스트에서는 Random Port 사용

테스트나 임시 실행에서는 사용 가능한 포트를 자동으로 고르게 할 수 있습니다.

```properties
server.port=0
```

통합 테스트처럼 정확한 포트가 중요하지 않을 때 유용합니다.
일반 로컬 개발에서는 고정 포트가 더 편합니다.
브라우저 URL, frontend proxy, README 명령이 예측 가능하기 때문입니다.

## 5. IDE와 DevTools Restart 확인

이전 application이 완전히 종료되지 않았을 수 있습니다.
자주 발생하는 상황은 다음과 같습니다.

- IDE run session이 아직 active 상태
- Spring Boot DevTools가 app을 재시작함
- 이전 terminal process가 background에 남아 있음
- Docker container가 host port 8080을 mapping 중
- 다른 profile이 예상과 다른 port를 설정함

IDE의 실행 세션을 확인합니다.
container도 확인합니다.

```bash
docker ps
```

`0.0.0.0:8080->...` 같은 mapping이 보이면 container가 host port를 쓰고 있습니다.
container를 stop하거나 port mapping을 바꿔야 합니다.

## 6. 해결 확인

process를 종료하거나 port를 바꾼 뒤 app을 다시 시작합니다.

```bash
./gradlew bootRun
```

그 다음 port를 확인합니다.

```bash
curl http://localhost:8081/
```

Actuator health endpoint가 있다면:

```bash
curl http://localhost:8081/actuator/health
```

backend port를 바꿨다면 frontend proxy, API base URL, Docker Compose mapping, README 명령도 함께 수정해야 합니다.

## 흔한 실수

첫 번째 실수는 무엇인지 확인하지 않고 process를 종료하는 것입니다.
포트 충돌은 로컬 문제이고, 다른 중요한 서비스가 해당 포트를 쓰고 있을 수 있습니다.

두 번째 실수는 잘못된 profile에 `server.port`를 설정하는 것입니다.
`spring.profiles.active=dev`로 실행한다면 `application-dev.properties` 또는 `application-dev.yml`도 확인해야 합니다.

세 번째 실수는 backend port만 바꾸고 frontend proxy를 그대로 두는 것입니다.
app은 시작되지만 API 호출이 실패합니다.

네 번째 실수는 Docker port mapping을 잊는 것입니다.
Java process를 종료해도 container가 host port `8080`을 쓰고 있으면 해결되지 않습니다.

## 함께 보면 좋은 글

- [Java Cannot Find Symbol 오류 해결](/ko_Troubleshooting/java-error-cannot-find-symbol/)
- [Java incompatible types 오류 해결](/ko_Troubleshooting/java-error-incompatible-types/)
- [Spring Boot application properties: server.port](https://docs.spring.io/spring-boot/appendix/application-properties/index.html#application-properties.server.server.port)

## 최종 체크리스트

```text
[ ] 오류가 port binding 문제인지 확인했다.
[ ] 해당 포트를 쓰는 process를 찾았다.
[ ] 올바른 process를 종료하거나 새 port를 선택했다.
[ ] active profile의 `server.port`를 설정했다.
[ ] application을 다시 시작했다.
[ ] port 변경 시 frontend proxy, Docker mapping, 문서도 갱신했다.
```

`port 8080 already in use`는 대부분 Spring logic bug가 아닙니다.
로컬 환경의 port 충돌입니다.
먼저 포트 소유자를 찾고, 비울지 옮길지 결정하면 됩니다.
