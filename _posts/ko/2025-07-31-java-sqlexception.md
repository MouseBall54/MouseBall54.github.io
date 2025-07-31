---
typora-root-url: ../
layout: single
title: "Java \"java.sql.SQLException\" 예외 처리 방법"
date: 2025-07-31T22:00:00+09:00
excerpt: "데이터베이스 연결, 구문을 올바르게 관리하고 try-catch-finally 블록을 사용하여 리소스가 닫히도록 보장함으로써 java.sql.SQLException을 처리하는 방법을 배웁니다."
categories:
  - ko_Troubleshooting
tags:
  - Java
  - JDBC
  - SQL
  - Database
  - Exception
---

## 서론

`java.sql.SQLException`은 데이터베이스 접근 오류나 기타 오류에 대한 정보를 제공하는 Java의 checked exception이다. JDBC(Java Database Connectivity)를 사용하여 데이터베이스 작업을 할 때마다 이 예외를 마주칠 가능성이 높다. 견고하고 신뢰할 수 있는 데이터베이스 애플리케이션을 구축하려면 적절한 처리가 매우 중요하다. 이 가이드에서는 `SQLException`의 일반적인 원인과 처리 모범 사례를 다룬다.

## SQLException의 일반적인 원인

`SQLException`은 광범위한 데이터베이스 관련 문제에 대한 일반적인 예외다. 몇 가지 일반적인 원인은 다음과 같다.

- **연결 문제**:
  - 잘못된 데이터베이스 URL, 사용자 이름 또는 비밀번호.
  - 데이터베이스 서버가 다운되었거나 연결할 수 없는 경우.
  - 네트워크 문제 또는 방화벽 제한.
- **SQL 구문 오류**:
  - SQL 쿼리의 오타 (예: `SELECT *` 대신 `SELEC *`).
  - 잘못된 테이블 또는 열 이름.
- **데이터 무결성 문제**:
  - 기본 키 열에 중복된 값을 삽입하려고 시도.
  - 외래 키 제약 조건 위반.
  - `null`을 허용하지 않는 열에 `null`을 삽입.
- **리소스 문제**:
  - 데이터베이스 연결 시간 초과.
  - 커서 또는 기타 데이터베이스 리소스 부족.
- **권한/특권 오류**:
  - 데이터베이스 사용자가 작업을 수행하는 데 필요한 권한(예: SELECT, INSERT, UPDATE)이 없는 경우.

## SQLException 처리 방법

`SQLException`은 checked exception이므로 컴파일러가 강제로 처리하도록 요구한다. 이를 처리하는 표준 방법은 `try-catch` 블록을 사용하는 것이다.

### 1. 리소스 관리를 위한 `try-catch-finally` 사용

Java 7 이전에는 `try-catch-finally` 블록이 `Connection`, `Statement`, `ResultSet`과 같은 데이터베이스 리소스가 오류 발생 시에도 항상 닫히도록 보장하는 표준 방법이었다.

#### 예시

```java
Connection conn = null;
Statement stmt = null;
ResultSet rs = null;
try {
    conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/mydb", "user", "password");
    stmt = conn.createStatement();
    rs = stmt.executeQuery("SELECT id, name FROM users");
    while (rs.next()) {
        // 결과 집합 처리
    }
} catch (SQLException e) {
    e.printStackTrace(); // 또는 로거 사용
} finally {
    try {
        if (rs != null) rs.close();
    } catch (SQLException e) { /* 무시 */ }
    try {
        if (stmt != null) stmt.close();
    } catch (SQLException e) { /* 무시 */ }
    try {
        if (conn != null) conn.close();
    } catch (SQLException e) { /* 무시 */ }
}
```
`finally` 블록 내의 중첩된 `try-catch` 블록은 리소스를 닫는 것 또한 `SQLException`을 발생시킬 수 있기 때문에 필요하다.

### 2. `try-with-resources` 사용 (Java 7 이상)

Java 7에서는 리소스 관리를 크게 단순화하는 `try-with-resources` 문이 도입되었다. `java.lang.AutoCloseable` 인터페이스를 구현하는 모든 객체(`Connection`, `Statement`, `ResultSet` 포함)는 `try-with-resources` 문에서 사용할 수 있다. 리소스는 블록이 끝날 때 자동으로 닫힌다.

#### 예시

```java
String sql = "SELECT id, name FROM users";
try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/mydb", "user", "password");
     Statement stmt = conn.createStatement();
     ResultSet rs = stmt.executeQuery(sql)) {

    while (rs.next()) {
        // 결과 집합 처리
        int id = rs.getInt("id");
        String name = rs.getString("name");
        System.out.println("ID: " + id + ", Name: " + name);
    }
} catch (SQLException e) {
    // 예외를 로깅하고 사용자 친화적인 메시지 제공
    // 예: SLF4J와 같은 로깅 프레임워크 사용
    // LOGGER.error("데이터베이스 오류 발생", e);
    e.printStackTrace();
}
```
이 코드는 `finally` 블록 접근 방식보다 훨씬 깨끗하고 오류 발생 가능성이 적다.

## SQLException 처리 모범 사례

- **구체적으로 처리하기**: `SQLException`에는 `SQLTimeoutException` 및 `SQLIntegrityConstraintViolationException`과 같은 하위 클래스가 있다. 이러한 특정 하위 클래스를 잡으면 더 맞춤화된 오류 처리가 가능하다.
- **로깅 프레임워크 사용**: `e.printStackTrace()`로 스택 트레이스를 출력하는 대신 Log4j, SLF4J 또는 Logback과 같은 적절한 로깅 프레임워크를 사용한다. 이를 통해 출력을 제어하고 파일로 보내며 로그 수준을 관리할 수 있다.
- **의미 있는 정보 제공**: `SQLException` 객체에는 귀중한 정보가 포함되어 있다.
  - `e.getMessage()`: 오류에 대한 설명을 제공한다.
  - `e.getErrorCode()`: 공급업체별 오류 코드를 제공한다.
  - `e.getSQLState()`: 표준 5자리 SQLSTATE 코드를 제공한다.
  이 정보를 로깅하는 것은 디버깅에 매우 중요하다.
- **예외 삼키지 않기**: 빈 `catch` 블록을 피한다. 최소한 예외를 로그로 남긴다. 이를 무시하면 디버깅이 거의 불가능해진다.
- **우아한 실패**: 사용자 대면 애플리케이션에서 원시 예외 세부 정보를 사용자에게 노출하지 않는다. `SQLException`을 잡고 개발자를 위해 세부 정보를 로깅한 다음 사용자 친화적인 오류 메시지(예: "데이터를 검색할 수 없습니다. 나중에 다시 시도하십시오.")를 표시한다.

이러한 지침을 따르면 데이터베이스와 안전하고 신뢰성 있게 상호 작용하는 견고한 Java 코드를 작성할 수 있다.
