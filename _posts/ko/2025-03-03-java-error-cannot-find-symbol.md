---
typora-root-url: ../
layout: single
title: >
    Java "Error: cannot find symbol" 해결 방법

date: 2025-03-03T07:21:00+09:00
lang: ko
translation_id: java-error-cannot-find-symbol
header:
    teaser: /images/header_images/overlay_image_java.png
    overlay_image: /images/header_images/overlay_image_java.png
    overlay_filter: 0.5
    image_description: >
      이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Java "Error: cannot find symbol" 해결 방법
excerpt: >
    Java에서 "cannot find symbol"은 컴파일러가 코드에서 사용된 식별자(변수, 메서드, 클래스 등)를 찾을 수 없을 때 발생하는 매우 흔한 컴파일 오류입니다. 이 글에서는 원인과 해결 방법을 알아봅니다.
seo_description: >
    Java에서 "cannot find symbol"은 컴파일러가 코드에서 사용된 식별자(변수, 메서드, 클래스 등)를 찾을 수 없을 때 발생하는 매우 흔한 컴파일 오류입니다. 이 글에서는 원인과 해결 방법을 알아봅니다.
categories:
    - ko_Troubleshooting
tags:
    - Java
    - Compilation Error
    - Symbol
---


![이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Java "Error: cannot find symbol" 해결 방법](/images/header_images/overlay_image_java.png)
## Java "Error: cannot find symbol"이란?

`cannot find symbol` 오류는 Java 컴파일러가 코드에 명시된 식별자(symbol)의 선언을 찾지 못했음을 의미합니다. 여기서 "심볼"은 변수 이름, 메서드 이름, 클래스 이름, 인터페이스 이름 등 개발자가 코드에서 정의하고 사용하는 모든 이름을 가리킵니다. 이 오류는 컴파일러에게 "당신이 사용한 '...'이 무엇인지, 어디에 정의되어 있는지 모르겠습니다"라고 말하는 것과 같습니다.

오류 메시지는 보통 세 부분으로 구성됩니다:
- **symbol**: 찾을 수 없는 심볼의 이름.
- **location**: 오류가 발생한 위치 (클래스 또는 메서드).
- **(선택) variable ... of type ...**: 심볼이 사용된 컨텍스트.

**오류 발생 예제:**
```java
public class SymbolTest {
    public static void main(String[] args) {
        Strng message = "Hello, World!"; // 오타: String -> Strng
        System.out.println(mesage); // 오타: message -> mesage
    }
}
```

**컴파일 오류:**
```
SymbolTest.java:3: error: cannot find symbol
        Strng message = "Hello, World!";
        ^
  symbol:   class Strng
  location: class SymbolTest
SymbolTest.java:4: error: cannot find symbol
        System.out.println(mesage);
                           ^
  symbol:   variable mesage
  location: class SymbolTest
```

## "cannot find symbol"의 일반적인 원인과 해결 방법

### 1. 오타 (Typo)

가장 흔한 원인입니다. 변수, 메서드, 클래스 이름의 철자가 선언된 곳과 사용된 곳에서 다른 경우 발생합니다. 대소문자도 구분하므로 주의해야 합니다.

- **해결책**: 심볼의 이름을 선언부와 사용부에서 동일하게 수정합니다. 위 예제에서 `Strng`를 `String`으로, `mesage`를 `message`로 고치면 해결됩니다.

### 2. `import` 문 누락

다른 패키지에 있는 클래스를 사용하면서 해당 클래스를 `import`하지 않은 경우 발생합니다. 예를 들어, `ArrayList`를 사용하려면 `java.util.ArrayList`를 임포트해야 합니다.

- **해결책**: 필요한 클래스를 소스 파일 상단에 `import` 문을 사용하여 추가합니다.
    ```java
    import java.util.ArrayList;

    public class MyClass {
        public static void main(String[] args) {
            ArrayList<String> list = new ArrayList<>();
        }
    }
    ```

### 3. 잘못된 변수 스코프 (Scope)

변수가 선언된 스코프(블록) 밖에서 해당 변수에 접근하려고 할 때 발생합니다. 예를 들어, `for` 루프 안에서 선언된 변수는 루프 밖에서 사용할 수 없습니다.

- **해결책**: 변수를 사용하려는 코드 블록을 포함하는 더 넓은 스코프에서 변수를 선언합니다.
    ```java
    public class ScopeTest {
        public void test() {
            int myVar = 0; // 블록 외부에서 선언
            for (int i = 0; i < 5; i++) {
                myVar = i;
            }
            System.out.println(myVar); // 정상 작동
        }
    }
    ```

### 4. 잘못된 메서드 호출

존재하지 않는 메서드를 호출하거나, 매개변수의 타입이나 개수가 다른 메서드를 호출하려고 할 때 발생합니다.

- **해결책**: 호출하려는 메서드의 시그니처(이름, 매개변수)가 클래스에 정의된 것과 일치하는지 확인합니다.

### 5. 라이브러리/클래스패스 문제

외부 라이브러리(.jar 파일)를 사용하지만, 컴파일 시 클래스패스(classpath)에 해당 라이브러리를 포함하지 않은 경우 발생합니다.

- **해결책**: 컴파일 명령어에 `-cp` 또는 `-classpath` 옵션을 사용하여 라이브러리의 경로를 명시해줍니다. IDE(Eclipse, IntelliJ)를 사용하는 경우, 프로젝트 빌드 경로에 라이브러리를 추가해야 합니다.
    ```bash
    javac -cp "/path/to/library.jar;." MyProgram.java
    ```

## 결론

`cannot find symbol` 오류는 대부분 사소한 실수에서 비롯됩니다. 오류 메시지가 가리키는 심볼과 위치를 주의 깊게 살펴보고, 다음 사항들을 순서대로 점검하면 쉽게 해결할 수 있습니다:
1.  이름에 오타가 없는가?
2.  필요한 클래스를 `import` 했는가?
3.  변수의 스코프가 올바른가?
4.  메서드 시그니처가 일치하는가?
5.  외부 라이브러리가 클래스패스에 포함되었는가?

## 전문 보완 체크

**Java "Error: cannot find symbol" 해결 방법**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 실행 환경, 정확한 오류 경계, 최소 재현 예제, 되돌릴 수 있는 경로를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

### 신뢰도를 높이는 증거

작업을 바꾸기 전에는 객관적인 증거를 먼저 확인해야 합니다. 쓸 만한 증거에는 전체 명령 출력, 버전 번호, 변경된 파일, 기대 동작과 실제 동작가 포함됩니다. 증거가 서로 맞지 않으면 억지로 하나의 이야기로 합치지 말고 충돌 자체를 남겨야 합니다. 빠른 해결이 한 번 성공했더라도 같은 입력, 계정, 의존성, 기기 상태에서 다시 확인하지 않았다면 아직 확정된 해결책이라고 보기 어렵습니다.

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

## 적용 검토 시나리오

독자가 **Java "Error: cannot find symbol" 해결 방법**의 첫 번째 권장 조치를 이미 시도했지만 결과가 여전히 불확실하다고 가정해 봅니다. 다음 단계는 여러 해결책을 한꺼번에 시험하는 것이 아니라 짧은 감사 기록을 만드는 것입니다. 먼저 어떤 판단을 하려는지 한 문장으로 쓰고, 환경을 한 문장으로 적고, 관찰된 결과를 한 문장으로 남깁니다. 그다음 실행 환경, 정확한 오류 경계, 최소 재현 예제, 되돌릴 수 있는 경로를 이미 확보한 사실과 대조합니다. 이렇게 해야 글이 서로 끊어진 팁 목록이 아니라 검증 가능한 절차가 됩니다.

### 감사 기록 양식

| 항목 | 예시 기준 | 이유 |
| --- | --- | --- |
| 관찰 | 조치 전 실제로 본 내용 | 기준 상태를 객관화합니다 |
| 증거 | 전체 명령 출력, 버전 번호 | 판단을 기록에 연결합니다 |
| 가정 | 믿고 있지만 아직 증명하지 못한 내용 | 숨은 추정을 드러냅니다 |
| 조치 | 한 번에 하나의 변경 | 결과의 원인을 추적하게 합니다 |
| 중단 기준 | 멈추고 도움을 요청할 조건 | 반복적인 시행착오를 줄입니다 |

### 품질 경계

같은 결과가 통제된 재확인 뒤에도 반복될 때만 이 안내를 강한 결론으로 보아야 합니다. 계정, 기기, 데이터 샘플, 의존성 버전, 계약 조건, 공식 규칙이 달라졌다면 결론의 강도를 낮추고 가설로 다루는 편이 안전합니다. 검색 독자는 급한 문제를 안고 들어오는 경우가 많아 맥락을 건너뛰기 쉽습니다. 전문적인 글은 위험한 판단을 천천히 하게 만들면서도 다음 행동은 분명하게 제시해야 합니다.

## 함께 보면 좋은 글

같은 주제 흐름에서 이어서 읽기 좋은 글입니다.

- [SSL: CERTIFICATE_VERIFY_FAILED 오류 해결 방법 (Windows Python)](/ko_troubleshooting/python-certificate-verify-failed/)
- [Permission denied (publickey) 오류 해결 방법 (Windows Git SSH)](/ko_troubleshooting/git-permission-denied-publickey-windows/)
