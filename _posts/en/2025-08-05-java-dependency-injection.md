typora-root-url: ../
layout: single
title: >
   Lowering Coupling with Dependency Injection in Java
date: 2025-08-05T11:20:00+09:00
header:
   teaser: /images/header_images/overlay_image_java.png
   overlay_image: /images/header_images/overlay_image_java.png
   overlay_filter: 0.5
excerpt: >
    Understand the principle of Dependency Injection (DI) and how it helps in building loosely coupled, testable, and maintainable applications in Java, with examples from frameworks like Spring.
categories:
  - en_Troubleshooting
tags:
  - Java
  - Dependency Injection
  - Spring
  - Design Patterns
  - Best Practices
---
## What is Dependency Injection?

**Dependency Injection (DI)** is a design pattern used to implement **Inversion of Control (IoC)**. It allows the creation of dependent objects to occur outside of a class and provides those dependencies to the class in various ways. In simple terms, instead of a class creating its own dependencies, the dependencies are "injected" into it by an external entity (often a DI framework).

This pattern is fundamental to building loosely coupled systems, which are easier to test, maintain, and extend.

### The Problem: Tight Coupling

Let's consider a `NotificationService` that sends emails. Without DI, the service might create its own `EmailClient` instance directly.

**Tightly Coupled Code:**
```java
// The dependency
class EmailClient {
    public void send(String message) {
        System.out.println("Sending email: " + message);
    }
}

// The dependent class
class NotificationService {
    private EmailClient client;

    public NotificationService() {
        // The service is creating its own dependency. This is a problem!
        this.client = new EmailClient(); 
    }

    public void sendNotification(String message) {
        this.client.send(message);
    }
}
```

This design has several problems:
1.  **Inflexible:** If we want to switch to sending SMS messages instead of emails, we have to change the `NotificationService` class itself.
2.  **Hard to Test:** When testing `NotificationService`, we cannot easily replace the real `EmailClient` with a mock or fake version. The test would actually try to send an email.
3.  **Violates Single Responsibility Principle:** `NotificationService` is responsible for both sending notifications *and* managing the lifecycle of `EmailClient`.

## The Solution: Dependency Injection

With DI, we "invert the control." The responsibility of creating the `EmailClient` is moved outside the `NotificationService`.

First, we should depend on an abstraction (interface) rather than a concrete class.

```java
// 1. Create an interface (the abstraction)
interface MessageClient {
    void send(String message);
}

// 2. Create concrete implementations
class EmailClient implements MessageClient {
    @Override
    public void send(String message) {
        System.out.println("Sending email: " + message);
    }
}

class SmsClient implements MessageClient {
    @Override
    public void send(String message) {
        System.out.println("Sending SMS: " + message);
    }
}
```

Now, we can inject the dependency into `NotificationService`.

### Types of Dependency Injection

There are three common types of DI:

#### 1. Constructor Injection

The dependencies are provided through the class constructor. This is the most common and recommended approach.

```java
class NotificationService {
    private final MessageClient client; // Depend on the interface

    // The dependency is injected via the constructor
    public NotificationService(MessageClient client) {
        this.client = client;
    }

    public void sendNotification(String message) {
        this.client.send(message);
    }
}

// Usage:
MessageClient emailClient = new EmailClient();
NotificationService notificationService = new NotificationService(emailClient);
notificationService.sendNotification("Hello via Email!");

// To switch to SMS, just inject a different implementation:
MessageClient smsClient = new SmsClient();
NotificationService smsNotificationService = new NotificationService(smsClient);
smsNotificationService.sendNotification("Hello via SMS!");
```
**Benefits:** Dependencies are clearly stated and can be made `final`, ensuring they are not changed after instantiation.

#### 2. Setter (or Method) Injection

The dependencies are provided through public setter methods.

```java
class NotificationService {
    private MessageClient client;

    public void setClient(MessageClient client) {
        this.client = client;
    }
    // ...
}
```
**Benefits:** Useful for optional dependencies or when you need to change the dependency after the object has been created.

#### 3. Field Injection

Dependencies are injected directly into the fields of a class. This is common in frameworks like Spring but is often considered less ideal because it hides the dependencies and makes testing harder without a DI container.

**Spring Framework Example:**
```java
@Component // Tells Spring to manage this class as a bean
class NotificationService {
    @Autowired // Tells Spring to inject the dependency here
    private MessageClient client;

    // ...
}
```

### Dependency Injection Frameworks (Spring, Guice)

Manually creating and injecting dependencies (as shown in the constructor injection example) can become tedious in large applications. DI frameworks automate this process.

- **Spring:** One of the most popular Java frameworks. It has a powerful DI container that manages the lifecycle of objects (called "beans") and injects them where needed using annotations like `@Autowired`.
- **Google Guice:** A lightweight DI framework that also uses annotations to wire dependencies together.

These frameworks use configuration (XML or annotations) to understand which implementation to inject for a given interface.

### Key Takeaway

Dependency Injection is a powerful pattern for building loosely coupled and highly testable applications. By letting an external entity provide dependencies to your classes, you make your code more flexible, modular, and maintainable. While you can implement DI manually, using a framework like Spring or Guice is the standard approach for modern Java applications.
