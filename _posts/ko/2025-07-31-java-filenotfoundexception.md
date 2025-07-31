---
typora-root-url: ../
layout: single
title: "Java `java.io.FileNotFoundException` 해결 방법"
date: 2025-07-31T10:00:00+09:00
excerpt: "파일 경로, 권한을 확인하고 올바른 리소스 처리 방법을 사용하여 `java.io.FileNotFoundException`을 해결하는 방법을 알아봅니다."
categories:
  - ko_Troubleshooting
tags:
  - Java
  - Exception
  - File I/O
  - Troubleshooting
---

## `FileNotFoundException`이란?

`java.io.FileNotFoundException`은 Java에서 지정된 경로에 파일이 존재하지 않을 때 접근하려고 시도하면 발생하는 일반적인 체크 예외(checked exception)이다. 파일을 읽거나 쓰려고 할 때 발생할 수 있으며, `IOException`의 하위 클래스이다.

## 일반적인 원인

1.  **잘못된 파일 경로**: 가장 흔한 원인은 파일 경로의 오타나 잘못된 경로 지정이다.
2.  **파일이 존재하지 않음**: 접근하려는 파일이 이동되었거나, 삭제되었거나, 생성된 적이 없다.
3.  **권한 문제**: 애플리케이션이 파일이나 디렉터리에 대한 필요한 읽기/쓰기 권한을 가지고 있지 않다.
4.  **상대 경로 vs. 절대 경로**: 상대 경로와 절대 경로의 혼동으로 인해 프로그램이 잘못된 디렉터리에서 파일을 찾을 수 있다. 상대 경로는 현재 작업 디렉터리를 기준으로 확인된다.

## 해결 방법

### 1. 파일 경로 확인

파일 경로가 올바른지 다시 확인한다. 철자와 디렉터리 구분자에 주의를 기울여야 한다.

```java
// 잘못된 경로
File file = new File("C:\\data\\my_file.txt"); // 오타 확인

// 올바른 경로
File file = new File("C:\\data\\myfile.txt");
```

`file.exists()`와 `file.getAbsolutePath()`를 사용하여 경로 문제를 디버깅할 수 있다.

```java
File file = new File("relative/path/to/file.txt");
System.out.println("접근 시도 경로: " + file.getAbsolutePath());

if (!file.exists()) {
    System.out.println("이 위치에 파일이 존재하지 않습니다.");
}
```

### 2. 파일 권한 확인

애플리케이션이 파일 및 상위 디렉터리에 대한 읽기 또는 쓰기 권한을 가지고 있는지 확인한다. Linux/macOS에서는 `ls -l`을 사용할 수 있고, Windows에서는 파일 속성의 보안 탭에서 확인할 수 있다.

### 3. `try-with-resources`를 사용한 올바른 처리

파일 스트림으로 작업할 때는 항상 `try-with-resources` 문을 사용하여 예외가 발생하더라도 스트림이 자동으로 닫히도록 해야 한다. 이는 리소스 누수를 방지한다.

```java
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;

public class FileReaderExample {
    public static void main(String[] args) {
        File file = new File("path/to/your/file.txt");
        try (FileInputStream fis = new FileInputStream(file)) {
            // 파일 읽기
            int content;
            while ((content = fis.read()) != -1) {
                System.out.print((char) content);
            }
        } catch (FileNotFoundException e) {
            System.err.println("오류: 지정된 경로에서 파일을 찾을 수 없습니다.");
            e.printStackTrace();
        } catch (IOException e) {
            System.err.println("오류: I/O 오류가 발생했습니다.");
            e.printStackTrace();
        }
    }
}
```

### 4. 파일 또는 디렉터리가 없으면 생성하기

애플리케이션이 파일을 생성해야 하는 경우, 파일이 존재하는지 확인하고 존재하지 않으면 생성할 수 있다.

```java
import java.io.File;
import java.io.IOException;

public class FileCreationExample {
    public static void main(String[] args) {
        try {
            File file = new File("path/to/new_file.txt");

            // 상위 디렉터리가 없으면 생성
            File parentDir = file.getParentFile();
            if (!parentDir.exists()) {
                parentDir.mkdirs();
            }

            // 파일이 없으면 생성
            if (file.createNewFile()) {
                System.out.println("파일 생성됨: " + file.getName());
            } else {
                System.out.println("파일이 이미 존재합니다.");
            }
        } catch (IOException e) {
            System.err.println("파일 생성 중 오류가 발생했습니다.");
            e.printStackTrace();
        }
    }
}
```

경로, 권한을 체계적으로 확인하고 강력한 오류 처리를 사용하면 `FileNotFoundException`을 효과적으로 해결할 수 있다.
