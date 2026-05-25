---
typora-root-url: ../
layout: single
title: >
   Java 의존성 주입(Dependency Injection)으로 결합도 낮추기

date: 2025-03-28T07:46:00+09:00
lang: ko
translation_id: java-dependency-injection
header:
   teaser: /images/header_images/overlay_image_java.png
   overlay_image: /images/header_images/overlay_image_java.png
   overlay_filter: 0.5
   image_description: >
     이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Java 의존성 주입(Dependency Injection)으로 결합도 낮추기
excerpt: >
    의존성 주입(DI)의 원리를 이해하고, Spring과 같은 프레임워크 예제를 통해 Java에서 느슨하게 결합되고, 테스트하기 쉬우며, 유지보수하기 좋은 애플리케이션을 구축하는 데 어떻게 도움이 되는지 알아보세요.
seo_description: >
    의존성 주입(DI)의 원리를 이해하고, Spring과 같은 프레임워크 예제를 통해 Java에서 느슨하게 결합되고, 테스트하기 쉬우며, 유지보수하기 좋은 애플리케이션을 구축하는 데 어떻게 도움이 되는지 알아보세요.
categories:
  - ko_Troubleshooting
tags:
  - Java
  - Dependency Injection
  - Spring
  - Design Patterns
  - Best Practices
---

![이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Java 의존성 주입(Dependency Injection)으로 결합도 낮추기](/images/header_images/overlay_image_java.png)
## 의존성 주입(Dependency Injection)이란?

**의존성 주입(DI)**은 **제어의 역전(IoC, Inversion of Control)**을 구현하는 데 사용되는 디자인 패턴입니다. 이는 종속적인 객체의 생성이 클래스 외부에서 일어나도록 하고, 이러한 의존성을 다양한 방식으로 클래스에 제공하는 것을 허용합니다. 간단히 말해, 클래스가 자신의 의존성을 직접 생성하는 대신, 외부 엔티티(종종 DI 프레임워크)에 의해 의존성이 "주입"됩니다.

이 패턴은 테스트, 유지보수, 확장이 더 쉬운 **느슨하게 결합된(loosely coupled)** 시스템을 구축하는 데 기본이 됩니다.

### 문제점: 강한 결합(Tight Coupling)

이메일을 보내는 `NotificationService`를 생각해 봅시다. DI가 없다면, 이 서비스는 자체적으로 `EmailClient` 인스턴스를 직접 생성할 수 있습니다.

**강하게 결합된 코드:**
```java
// 의존성
class EmailClient {
    public void send(String message) {
        System.out.println("이메일 발송: " + message);
    }
}

// 의존하는 클래스
class NotificationService {
    private EmailClient client;

    public NotificationService() {
        // 서비스가 자신의 의존성을 직접 생성하고 있습니다. 이것이 문제입니다!
        this.client = new EmailClient(); 
    }

    public void sendNotification(String message) {
        this.client.send(message);
    }
}
```

이 설계에는 몇 가지 문제가 있습니다:
1.  **유연성 부족:** 이메일 대신 SMS 메시지를 보내고 싶다면, `NotificationService` 클래스 자체를 변경해야 합니다.
2.  **테스트의 어려움:** `NotificationService`를 테스트할 때, 실제 `EmailClient`를 모의(mock) 또는 가짜 버전으로 쉽게 교체할 수 없습니다. 테스트는 실제로 이메일을 보내려고 시도할 것입니다.
3.  **단일 책임 원칙 위반:** `NotificationService`는 알림을 보내는 것과 `EmailClient`의 생명주기를 관리하는 두 가지 책임을 모두 가지고 있습니다.

## 해결책: 의존성 주입

DI를 사용하면 "제어를 역전"시킵니다. `EmailClient`를 생성하는 책임이 `NotificationService` 외부로 이동합니다.

먼저, 구체적인 클래스가 아닌 추상화(인터페이스)에 의존해야 합니다.

```java
// 1. 인터페이스 생성 (추상화)
interface MessageClient {
    void send(String message);
}

// 2. 구체적인 구현체 생성
class EmailClient implements MessageClient {
    @Override
    public void send(String message) {
        System.out.println("이메일 발송: " + message);
    }
}

class SmsClient implements MessageClient {
    @Override
    public void send(String message) {
        System.out.println("SMS 발송: " + message);
    }
}
```

이제 `NotificationService`에 의존성을 주입할 수 있습니다.

### 의존성 주입의 종류

세 가지 일반적인 DI 유형이 있습니다:

#### 1. 생성자 주입 (Constructor Injection)

의존성이 클래스 생성자를 통해 제공됩니다. 이것이 가장 일반적이고 권장되는 접근 방식입니다.

```java
class NotificationService {
    private final MessageClient client; // 인터페이스에 의존

    // 의존성이 생성자를 통해 주입됩니다.
    public NotificationService(MessageClient client) {
        this.client = client;
    }

    public void sendNotification(String message) {
        this.client.send(message);
    }
}

// 사용법:
MessageClient emailClient = new EmailClient();
NotificationService notificationService = new NotificationService(emailClient);
notificationService.sendNotification("이메일로 안녕하세요!");

// SMS로 전환하려면 다른 구현체를 주입하기만 하면 됩니다:
MessageClient smsClient = new SmsClient();
NotificationService smsNotificationService = new NotificationService(smsClient);
smsNotificationService.sendNotification("SMS로 안녕하세요!");
```
**장점:** 의존성이 명확하게 명시되고 `final`로 만들 수 있어, 인스턴스화 후에 변경되지 않음을 보장합니다.

#### 2. 세터(Setter) 또는 메서드 주입

의존성이 public 세터 메서드를 통해 제공됩니다.

```java
class NotificationService {
    private MessageClient client;

    public void setClient(MessageClient client) {
        this.client = client;
    }
    // ...
}
```
**장점:** 선택적 의존성이거나 객체가 생성된 후 의존성을 변경해야 할 때 유용합니다.

#### 3. 필드 주입 (Field Injection)

의존성이 클래스의 필드에 직접 주입됩니다. 이는 Spring과 같은 프레임워크에서 흔하지만, 의존성을 숨기고 DI 컨테이너 없이는 테스트를 더 어렵게 만들기 때문에 종종 덜 이상적인 것으로 간주됩니다.

**Spring 프레임워크 예시:**
```java
@Component // Spring에게 이 클래스를 빈(bean)으로 관리하라고 알림
class NotificationService {
    @Autowired // Spring에게 여기에 의존성을 주입하라고 알림
    private MessageClient client;

    // ...
}
```

### 의존성 주입 프레임워크 (Spring, Guice)

수동으로 의존성을 생성하고 주입하는 것(생성자 주입 예시에서 보았듯이)은 대규모 애플리케이션에서는 지루한 작업이 될 수 있습니다. DI 프레임워크는 이 과정을 자동화합니다.

- **Spring:** 가장 인기 있는 Java 프레임워크 중 하나입니다. 객체( "빈"이라 불림)의 생명주기를 관리하고 `@Autowired`와 같은 어노테이션을 사용하여 필요한 곳에 주입하는 강력한 DI 컨테이너를 가지고 있습니다.
- **Google Guice:** 의존성을 연결하기 위해 어노테이션을 사용하는 경량 DI 프레임워크입니다.

이러한 프레임워크는 설정(XML 또는 어노테이션)을 사용하여 주어진 인터페이스에 대해 어떤 구현체를 주입할지 파악합니다.

### 핵심 요약

의존성 주입은 느슨하게 결합되고 테스트하기 쉬운 애플리케이션을 구축하기 위한 강력한 패턴입니다. 외부 엔티티가 클래스에 의존성을 제공하게 함으로써 코드를 더 유연하고, 모듈화되고, 유지보수하기 쉽게 만듭니다. DI를 수동으로 구현할 수도 있지만, Spring이나 Guice와 같은 프레임워크를 사용하는 것이 현대 Java 애플리케이션의 표준 접근 방식입니다.

## 전문 보완 체크

**Java 의존성 주입(Dependency Injection)으로 결합도 낮추기**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 JDK 버전, 빌드 도구 설정, classpath 또는 module path, 런타임 stack trace를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

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
