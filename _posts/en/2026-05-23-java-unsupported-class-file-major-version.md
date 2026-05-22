---
typora-root-url: ../
layout: single
title: >
  Unsupported Class File Major Version: How to Fix Java JDK Mismatch
seo_title: >
  Unsupported Class File Major Version
date: 2026-05-23T23:59:59+09:00
lang: en
translation_id: java-unsupported-class-file-major-version
header:
   teaser: /images/2026-05-23-java-unsupported-class-file-major-version/java-class-file-version-hero.png
   overlay_image: /images/2026-05-23-java-unsupported-class-file-major-version/java-class-file-version-hero.png
   overlay_filter: 0.35
excerpt: >
  Fix Unsupported class file major version by matching the Java runtime, compiler, Gradle or Maven toolchain, and target release used by the project.
seo_description: >
  Fix Unsupported class file major version by matching the Java runtime, compiler, Gradle or Maven toolchain, and target release used by the project.
categories:
  - en_Troubleshooting
tags:
  - Java
  - JDK
  - Gradle
  - Maven
  - Troubleshooting
---

## Quick Answer

`Unsupported class file major version` means a Java runtime or build tool is trying to read bytecode compiled for a newer Java version than it supports.
Use a newer JDK to run the project, or compile the project for an older target using Gradle, Maven, or `javac --release`.

![Java class file version mismatch diagram with compiler, bytecode, runtime, and aligned JDK path](/images/2026-05-23-java-unsupported-class-file-major-version/java-class-file-version-hero.png)

The image shows the mismatch.
The compiler produced class files for a newer level, but the runtime or build tool is older.
The fix is to align the build JDK, runtime JDK, and target release.

## Typical Error

You may see:

```text
java.lang.UnsupportedClassVersionError:
Unsupported class file major version 61
```

or:

```text
Unsupported class file major version 65
```

The number identifies the class file version.
For common versions:

| Major Version | Java Version |
| ---: | --- |
| 52 | Java 8 |
| 55 | Java 11 |
| 61 | Java 17 |
| 65 | Java 21 |

So if Java 11 tries to run Java 17 bytecode, you can get major version `61`.

## 1. Check the Java Runtime

Run:

```bash
java -version
```

Also check the compiler:

```bash
javac -version
```

If `java` and `javac` point to different versions, fix your `JAVA_HOME` and `PATH`.

On macOS or Linux:

```bash
echo $JAVA_HOME
which java
```

On Windows PowerShell:

```powershell
echo $env:JAVA_HOME
where.exe java
```

The runtime used by your IDE may still be different from the terminal.
Check the IDE project SDK too.

## 2. Check Gradle or Maven JVM

Gradle:

```bash
./gradlew --version
```

Maven:

```bash
mvn -version
```

These commands show the JVM used by the build tool.
If the build tool runs on an old JDK, it may fail before your application even starts.

For Gradle projects, prefer Java toolchains:

```groovy
java {
    toolchain {
        languageVersion = JavaLanguageVersion.of(17)
    }
}
```

For Maven, configure the compiler plugin:

```xml
<maven.compiler.release>17</maven.compiler.release>
```

Use the version your project actually supports.

## 3. Decide Whether to Upgrade Runtime or Lower Target

There are two valid fixes:

```text
Option A: Run with a newer JDK.
Option B: Compile for an older Java target.
```

Choose Option A when the project requires newer Java features or framework versions.
Choose Option B when the deployment environment is fixed to an older Java version.

Do not blindly lower the target.
If the source code uses newer APIs, compilation may pass in one place and fail at runtime elsewhere unless `--release` or a proper toolchain is used.

## 4. Check Dependency Bytecode

Sometimes your code targets Java 11, but a dependency was compiled for Java 17 or Java 21.
In that case, the error may appear while loading a library.

Fix options:

- Upgrade the runtime JDK.
- Use an older compatible dependency version.
- Check the library's release notes for minimum Java version.
- Align Spring Boot, Gradle, Maven, and plugin versions.

This is common after dependency upgrades.
Read the first dependency mentioned in the stacktrace.

## 5. Clean After Changing JDK

After changing Java versions, clean the build output:

```bash
./gradlew clean build
```

or:

```bash
mvn clean test
```

Old compiled `.class` files may still exist in `build/` or `target/`.
Cleaning ensures the project is compiled with the intended version.

## Common Mistakes

The first mistake is changing only `JAVA_HOME` but not the IDE SDK.
The terminal and IDE may use different JDKs.

The second mistake is using global Gradle or Maven without checking its JVM.
The project wrapper may use a different setup.

The third mistake is lowering the compiler target while dependencies still require a newer Java version.

The fourth mistake is fixing local Java but forgetting CI.
Update CI images and setup actions too.

## Related Reading

- [Gradle Build Failed](/en_Troubleshooting/gradle-build-failed/)
- [Maven Dependency Not Found](/en_Troubleshooting/maven-dependency-not-found/)
- [Oracle Java Virtual Machine Specification: ClassFile format](https://docs.oracle.com/javase/specs/jvms/se21/html/jvms-4.html)
- [Gradle Java toolchains](https://docs.gradle.org/current/userguide/toolchains.html)

## Final Checklist

```text
[ ] `java -version` is the expected version.
[ ] `javac -version` matches the project target.
[ ] Gradle or Maven runs with the expected JDK.
[ ] The compiler target or release is configured.
[ ] Dependencies support the selected Java version.
[ ] CI and IDE settings match local settings.
```

This error is a version alignment problem.
Once runtime, compiler, build tool, and dependencies agree, the class file major version error disappears.

## FAQ

### When should I use this guide?

Use it when you can reproduce the error and need a practical order for checking commands, versions, paths, permissions, and logs.

### What should beginners verify first?

Start with the exact error message, the command you ran, the operating system, and the tool version. These details usually narrow the cause faster than changing many settings at once.

### Which keywords should I search next?

Search for "Unsupported Class File Major Version: How to Fix Java JDK Mismatch" together with the exact error text, version, operating system, and tool name used in your environment.
