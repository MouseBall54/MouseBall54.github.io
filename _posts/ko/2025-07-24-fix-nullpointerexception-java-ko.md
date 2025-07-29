---
typora-root-url: ../
layout: single
title: " How to Fix “ModuleNotFoundError: No module named '…'” in Python"
date: 2025-07-24T22:00:00+09:00
excerpt: "NullPointerException은 null 참조 접근 시 발생. null 검사, Optional, 초기화, 어노테이션 사용으로 예방."
categories:
  - ko_Troubleshooting
tags:
  - Java
  - NullPointerException
---

## 소개

NullPointerException은 Java에서 가장 흔한 런타임 오류다.
객체가 null인 상태에서 메서드 호출이나 필드 접근을 시도할 때 발생한다.

## 오류 내용

```
Exception in thread "main" java.lang.NullPointerException
    at com.example.MyClass.main(MyClass.java:10)
```

null인 변수에 .length(), .get() 등을 호출하면 예외가 발생한다.

## 주요 원인

* 객체를 생성하지 않고 사용함.
* 메서드가 null을 반환함.
* 컬렉션 조회 후 결과를 검증하지 않음.
* Wrapper 타입 자동 언박싱 시 null 처리 누락.

## 해결 방법 1: null 검사

```java
if (obj != null) {
    obj.doSomething();
}
```

예외 발생 우선 차단.

## 해결 방법 2: Optional 사용

```java
Optional<String> opt = Optional.ofNullable(text);
opt.ifPresent(s -> System.out.println(s.length()));
```

null 처리를 명시적으로 구현.

## 해결 방법 3: 올바른 초기화

```java
List<String> list = new ArrayList<>();
```

필드나 변수는 선언과 동시에 초기화 권장.

## 해결 방법 4: @NonNull / @Nullable 어노테이션

```java
public void process(@NonNull String input) { … }
```

IDE와 정적 분석 도구가 컴파일 단계에서 경고 제공.

## 해결 방법 5: 자동 언박싱 주의

```java
Integer count = getCount();
if (count != null) {
    int c = count;  // 안전 언박싱
}
```

Wrapper 타입 null 검사 필수.

## 결론

NullPointerException은 대부분 사전 검사와 올바른 초기화로 예방 가능하다.
Optional과 nullability 어노테이션을 적극 활용하자.

