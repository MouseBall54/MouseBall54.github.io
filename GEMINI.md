## GEMINI.md 작성 지침

1. **프로젝트 개요**

   * GitHub Pages 기반 블로그 운영.
   * 포스트는 한글(/\_posts/ko)과 영어(/\_posts/en) 폴더에 저장.
   * Easy Labeling SW 홍보가 주 목적이나,
     초기에는 검색 노출을 위해 프로그래밍 이슈 해결 전략으로 진행.

2. **포스트 작성 스타일**

   * **단문체** 작성. 문장은 짧고 명확하게.
   * 내용은 **자세**하게. 핵심은 간결하게.
   * 한글 버전에도 프로그래밍 용어 및 전용 영어 단어는 영문 그대로 사용.
   * AI 작성 흔적 제거: 자연스러운 사람 글투 유지.

3. **YAML 헤더 구성 예시**

   ```yaml
   typora-root-url: ../
   layout: single
   title: "How to Fix “Permission denied (publickey)” Error with Git on Windows"
   date: 2025-07-22T22:00:00+09:00
   header:
      overlay_image: /images/header_images/overlay_image_<언어>.png
      overlay_filter: 0.5
   excerpt: >
     Fix Git’s “Permission denied (publickey)” error on Windows by creating an SSH key,
     adding it to the SSH agent, and registering it with your Git host.
   categories:
     - en_Troubleshooting
   tags:
     - Git
     - SSH
     - Windows
     - Authentication
   ```

   * **블록 스칼라**(`>`, `|`) 사용. 따옴표(`"`, `'`) 충돌 방지.
   * `tags`는 3\~5개. 모두 영어.
   * **헤더 이미지 설정**: Troubleshooting 카테고리 내 언어/툴별 YAML `overlay_image` 값

     * python: `images/header_images/overlay_image_python.png`
     * java:   `images/header_images/overlay_image_java.png`
     * js:     `images/header_images/overlay_image_js.png`
     * git:    `images/header_images/overlay_image_git.png`
  
4. **주제 및 분량**

   * 첫 300개 포스트는 모두 `Troubleshooting` 주제로.
   * 요청 시 주제당 1개 포스트 작성.

5. **작업 이력 기록**

   * 포스트 하단에 작업 이력 기록.
   * 차후 참고용.

6. **분야 균형 관리**

   * 다양한 분야 골고루 다룸.
   * 작성 후 다음 주제 분포 확인.

7. **Git 커밋 절차**

   * 글 작성 완료 후 커밋 메시지를 별도 파일에 저장.
   * `git commit -F <파일명>` 형식으로 커밋.
   * 커밋 메시지는 **한글**로 작성.

8. **검토**

   * 작성 후 이상한 부분 재확인.
   * 단문체로 작성됐는지 최종 점검.

9. **주제 및 분량**

   * 첫 300개 포스트는 모두 `Troubleshooting` 주제로.
   * 요청 시 주제당 1개 포스트 작성.

10. **작업 이력 기록**

   * 포스트 하단에 작업 이력 기록.
   * 차후 참고용.

11. **분야 균형 관리**

   * 다양한 분야 골고루 다룸.
   * 작성 후 다음 주제 분포 확인.

12. **Git 커밋 절차**

   * 글 작성 완료 후 커밋 메시지를 별도 파일에 저장.
   * `git commit -F <파일명>` 형식으로 커밋.
   * 커밋 메시지는 **한글**로 작성.

13. **검토**

   * 작성 후 이상한 부분 재확인.
   * 단문체로 작성됐는지 최종 점검.


작업이력
- 2025년 7월 30일: Python, JavaScript, Java, Git 관련 자주 발생하는 오류 120개 목록 생성 완료.
- 2025년 7월 30일: "SyntaxError: invalid syntax" 관련 한글 및 영어 포스트 작성 완료.
- 2025년 7월 30일: "IndentationError: expected an indented block" 관련 한글 및 영어 포스트 작성 완료.
- 2025년 7월 30일: "Uncaught TypeError: Cannot read properties of null" 관련 한글 및 영어 포스트 작성 완료.
- 2025년 7월 30일: "java.lang.NullPointerException" 관련 한글 및 영어 포스트 작성 완료.
- 2025년 7월 30일: "NameError: name '...' is not defined" 관련 한글 및 영어 포스트 작성 완료.
- 2025년 7월 30일: "Uncaught TypeError: Cannot read properties of undefined" 관련 한글 및 영어 포스트 작성 완료.
- 2025년 7월 30일: "java.lang.ArrayIndexOutOfBoundsException" 관련 한글 및 영어 포스트 작성 완료.
- 2025년 7월 30일: "fatal: not a git repository" 관련 한글 및 영어 포스트 작성 완료.
- 2025년 7월 30일: "Uncaught ReferenceError: ... is not defined" 관련 한글 및 영어 포스트 작성 완료.
- 2025년 7월 30일: "fatal: remote origin already exists" 관련 한글 및 영어 포스트 작성 완료.
- 2025년 7월 30일: "Python TypeError: can only concatenate str (not 'int') to str" 관련 한글 및 영어 포스트 작성 완료.
- 2025년 7월 30일: "JavaScript Uncaught RangeError: Maximum call stack size exceeded" 관련 한글 및 영어 포스트 작성 완료.
- 2025년 7월 30일: "Python IndexError: list index out of range" 관련 한글 및 영어 포스트 작성 완료.
- 2025년 7월 30일: "JavaScript Uncaught SyntaxError: Unexpected token" 관련 한글 및 영어 포스트 작성 완료.
- 2025년 7월 30일: "Python KeyError: '...'" 관련 한글 및 영어 포스트 작성 완료.
- 2025년 7월 30일: "Python AttributeError: 'NoneType' object has no attribute '...'" 관련 한글 및 영어 포스트 작성 완료.
- 2025년 7월 30일: "Python FileNotFoundError" 관련 한글 및 영어 포스트 작성 완료.
- 2025년 7월 30일: "Python ModuleNotFoundError" 관련 한글 및 영어 포스트 작성 완료.
- 2025년 7월 31일: "java.io.FileNotFoundException" 관련 한글 및 영어 포스트 작성 완료.
- 2025년 7월 31일: "error: failed to push some refs to '...'" 관련 한글 및 영어 포스트 작성 완료.
- 2025년 7월 31일: "Uncaught URIError: URI malformed" 관련 한글 및 영어 포스트 작성 완료.
- 2025년 7월 31일: "java.lang.ClassCastException" 관련 한글 및 영어 포스트 작성 완료.
- 2025년 7월 31일: "Permission denied (publickey)" 관련 한글 및 영어 포스트 작성 완료.
- 2025년 7월 31일: "fatal: refusing to merge unrelated histories" 관련 한글 및 영어 포스트 작성 완료.
- 2025년 7월 31일: "java.io.IOException" 관련 한글 및 영어 포스트 작성 완료.
- 2025년 7월 31일: Python "ImportError", JavaScript "TypeError: is not a function", Java "SQLException", Git "local changes overwritten" 관련 한글 및 영어 포스트 작성 완료.
- 2025년 7월 31일: JavaScript 3건, Java 2건, Git 2건의 트러블슈팅 포스트 추가 작성 완료.
- 2025년 7월 31일: "java.lang.IllegalStateException" 관련 한글 및 영어 포스트 작성 완료.
- 2025년 7월 31일: Git "fatal: pathspec '...' did not match any files", "The requested URL returned error: 403", "fatal: unable to access '...': The requested URL returned error: 404" 관련 한글 및 영어 포스트 작성 완료.
- 2025년 7월 31일: Java "OutOfMemoryError", "StackOverflowError", "NoClassDefFoundError" 관련 한글 및 영어 포스트 작성 완료.
- 2025년 7월 31일: Python "ValueError", "ZeroDivisionError", "UnboundLocalError" 관련 한글 및 영어 포스트 작성 완료.

진행도
  - Python : 13/30
  - JavaScript : 10/30
  - Java : 12/30
  - Git : 11/30 

### Python (1-30)
1.  **SyntaxError: invalid syntax** ✅: 콜론(:) 누락, 괄호 불일치 등 기본 문법 오류 해결 방법.
2.  **IndentationError: expected an indented block** ✅: 잘못된 들여쓰기 수정 및 탭 vs. 공백 문제 해결.
3.  **NameError: name '...' is not defined** ✅: 변수 또는 함수가 정의되지 않았을 때 해결 방법.
4.  **TypeError: can only concatenate str (not "int") to str** ✅: 문자열과 숫자 등 다른 타입의 객체를 합치려 할 때 해결 방법.
5.  **IndexError: list index out of range** ✅: 리스트의 범위를 벗어난 인덱스에 접근할 때 해결 방법.
6.  **KeyError: '...'** ✅: 딕셔너리에 존재하지 않는 키에 접근할 때 해결 방법.
7.  **AttributeError: 'NoneType' object has no attribute '...'** ✅: None을 반환하는 객체의 속성에 접근하려 할 때 해결 방법.
8.  **FileNotFoundError: [Errno 2] No such file or directory** ✅: 파일을 찾을 수 없을 때 경로 문제 해결 방법.
9.  **ModuleNotFoundError: No module named '...'** ✅: 설치되지 않았거나 잘못된 이름의 모듈을 임포트할 때 해결 방법.
10. **ImportError: cannot import name '...' from '...'** ✅: 순환 참조 또는 잘못된 임포트 구문 문제 해결.
11. **ValueError: invalid literal for int() with base 10: '...'** ✅: 정수로 변환할 수 없는 문자열을 변환하려 할 때 해결 방법.
12. **ZeroDivisionError: division by zero** ✅: 0으로 나누려고 할 때 발생하는 오류 해결 방법.
13. **UnboundLocalError: local variable '...' referenced before assignment** ✅: 함수 내에서 지역 변수가 할당되기 전에 참조될 때 해결 방법.
14. **TabError: inconsistent use of tabs and spaces in indentation**: 탭과 공백을 혼용하여 들여쓰기했을 때 해결 방법.
15. **UnicodeDecodeError: 'utf-8' codec can't decode byte ...**: 파일 읽기/쓰기 시 발생하는 인코딩 문제 해결 방법.
16. **RuntimeError: dictionary changed size during iteration**: 딕셔너리 순회 중 크기가 변경될 때 해결 방법.
17. **TypeError: '...' object is not iterable**: 반복 불가능한 객체를 순회하려고 할 때 해결 방법.
18. **TypeError: missing 1 required positional argument: '...'**: 함수 호출 시 필수 인자가 누락되었을 때 해결 방법.
19. **MemoryError**: 대용량 데이터 처리 시 메모리 부족 문제 해결 및 최적화 방법.
20. **RecursionError: maximum recursion depth exceeded**: 재귀 호출이 너무 깊어질 때 해결 방법.
21. **OSError: [Errno 28] No space left on device**: 디스크 공간 부족 시 발생하는 오류 해결 방법.
22. **ConnectionError: [Errno 111] Connection refused**: 네트워크 연결이 거부될 때 방화벽 및 포트 문제 해결.
23. **TimeoutError: [WinError 10060]**: 네트워크 작업 시간 초과 시 해결 방법.
24. **PermissionError: [Errno 13] Permission denied**: 파일/디렉터리 접근 권한이 없을 때 해결 방법.
25. **IsADirectoryError: [Errno 21] Is a directory**: 파일을 예상한 위치에 디렉터리가 있을 때 해결 방법.
26. **NotADirectoryError: [Errno 20] Not a directory**: 디렉터리를 예상한 위치에 파일이 있을 때 해결 방법.
27. **TypeError: unsupported operand type(s) for +: '...' and '...'**: 지원되지 않는 타입 간의 연산 시 해결 방법.
28. **SystemError: <built-in function ...> returned NULL without setting an error**: Python 인터프리터 내부 오류 발생 시 해결 방법.
29. **FloatingPointError**: 부동 소수점 연산 오류 발생 시 해결 방법.
30. **KeyboardInterrupt**: 사용자가 Ctrl+C를 눌러 프로그램을 중단시켰을 때 예외 처리 방법.

### JavaScript (31-60)
31. **Uncaught TypeError: Cannot read properties of null (reading '...')** ✅: DOM 요소가 로드되기 전에 접근하려 할 때 해결 방법.
32. **Uncaught TypeError: Cannot read properties of undefined (reading '...')** ✅: 정의되지 않은 객체의 속성에 접근하려 할 때 해결 방법.
33. **Uncaught ReferenceError: ... is not defined** ✅: 변수나 함수가 선언되지 않았거나 스코프 밖에 있을 때 해결 방법.
34. **Uncaught SyntaxError: Unexpected token '...'** ✅: 잘못된 문법이나 예상치 못한 토큰을 사용했을 때 해결 방법.
35. **Uncaught RangeError: Maximum call stack size exceeded** ✅: 무한 재귀 호출로 인해 스택이 가득 찼을 때 해결 방법.
36. **Uncaught URIError: URI malformed** ✅: `decodeURIComponent()` 등에서 잘못된 URI를 사용할 때 해결 방법.
37. **TypeError: '...' is not a function** ✅: 함수가 아닌 것을 함수처럼 호출하려 할 때 해결 방법.
38. **SyntaxError: Invalid or unexpected token** ✅: 코드에 유효하지 않은 문자나 토큰이 포함되었을 때 해결 방법.
39. **ReferenceError: assignment to undeclared variable "..."** ✅: 선언되지 않은 변수에 값을 할당하려 할 때 해결 방법 (Strict Mode).
40. **TypeError: Assignment to constant variable** ✅: `const`로 선언된 변수에 재할당하려 할 때 해결 방법.
41. **Cross-Origin Read Blocking (CORB)**: 다른 출처의 리소스를 차단할 때 CORS 정책 설정 방법.
42. **Failed to fetch**: 네트워크 요청 실패 시 원인 분석 및 해결 (CORS, 네트워크 문제 등).
43. **[Violation] 'click' handler took ...ms**: 긴 실행 시간으로 브라우저 반응성을 저해하는 이벤트 핸들러 최적화.
44. **[Violation] Forced reflow while executing JavaScript**: 불필요한 레이아웃 재계산을 유발하는 코드 최적화.
45. **Uncaught DOMException: Failed to execute '...' on '...'': The node to be removed is not a child of this node.**: DOM에서 존재하지 않는 자식 노드를 제거하려 할 때 해결 방법.
46. **Uncaught (in promise) ...**: 프로미스 체인에서 `catch`로 처리되지 않은 예외 해결 방법.
47. **SyntaxError: Unexpected end of input**: 코드 블록이 제대로 닫히지 않았을 때 (괄호, 따옴표 등) 해결 방법.
48. **SyntaxError: missing ) after argument list**: 함수 호출 시 괄호가 누락되었을 때 해결 방법.
49. **SyntaxError: Unterminated string literal**: 문자열이 제대로 닫히지 않았을 때 해결 방법.
50. **TypeError: Reduce of empty array with no initial value**: 초기값 없이 빈 배열에 `reduce()`를 호출할 때 해결 방법.
51. **WebSocket connection to '...' failed**: 웹소켓 연결 실패 시 원인 분석 및 해결.
52. **"this" is undefined**: 콜백 함수나 이벤트 핸들러에서 `this`가 `undefined`가 되는 문제 해결 (화살표 함수, `bind` 등).
53. **Event listener leaks**: 이벤트 리스너가 제대로 제거되지 않아 발생하는 메모리 누수 문제 해결.
54. **Insecure mixed content**: HTTPS 페이지에서 HTTP 리소스를 로드할 때 발생하는 보안 경고 해결.
55. **jQuery is not defined**: jQuery가 로드되기 전에 사용하려 할 때 해결 방법.
56. **`innerHTML` vs. `textContent`**: 보안 및 성능 측면에서 두 속성의 올바른 사용법.
57. **`==` vs. `===`**: 느슨한 동등성과 엄격한 동등성의 차이 및 올바른 사용법.
58. **`let`, `const`, `var`**: 변수 선언 키워드의 스코프 및 호이스팅 차이점.
59. **`Promise.all` vs. `Promise.race`**: 여러 프로미스를 병렬로 처리하는 방법과 차이점.
60. **`async/await` error handling**: `try...catch`를 사용한 비동기 코드의 예외 처리 방법.

### Java (61-90)
61. **NullPointerException** ✅: `null` 참조를 가진 객체의 멤버에 접근할 때 해결 방법.
62. **ArrayIndexOutOfBoundsException** ✅: 배열의 범위를 벗어난 인덱스에 접근할 때 해결 방법.
62. **ArrayIndexOutOfBoundsException**: 배열의 범위를 벗어난 인덱스에 접근할 때 해결 방법.
63. **FileNotFoundException** ✅: 지정된 경로에서 파일을 찾을 수 없을 때 해결 방법.
64. **ClassCastException** ✅: 호환되지 않는 클래스 간에 객체를 형변환하려 할 때 해결 방법.
65. **IOException** ✅: 입출력 작업 실패 시 예외 처리 방법.
66. **SQLException** ✅: 데이터베이스 접근 오류 시 해결 방법.
67. **NumberFormatException** ✅: 숫자로 변환할 수 없는 문자열을 변환하려 할 때 해결 방법.
68. **IllegalArgumentException** ✅: 메서드에 부적절한 인수를 전달했을 때 해결 방법.
69. **IllegalStateException** ✅: 객체의 상태가 메서드 호출에 적합하지 않을 때 해결 방법.
70. **OutOfMemoryError** ✅: 힙 메모리 부족 시 해결 및 JVM 튜닝 방법.
71. **StackOverflowError** ✅: 무한 재귀 호출로 스택이 가득 찼을 때 해결 방법.
72. **NoClassDefFoundError** ✅: 런타임에 클래스를 찾을 수 없을 때 클래스패스 문제 해결.
73. **UnsupportedOperationException**: 지원되지 않는 연산을 호출했을 때 해결 방법.
74. **ConcurrentModificationException**: 컬렉션 순회 중 수정이 발생했을 때 해결 방법.
75. **ArithmeticException: / by zero**: 정수를 0으로 나눌 때 해결 방법.
76. **Error: a public class ... must be defined in a file called ... .java**: 클래스 이름과 파일 이름이 다를 때 해결 방법.
77. **Error: cannot find symbol**: 변수, 메서드, 클래스를 찾을 수 없을 때 (오타, 임포트 누락 등) 해결 방법.
78. **Error: ‘;’ expected**: 세미콜론이 누락되었을 때 해결 방법.
79. **Error: incompatible types**: 호환되지 않는 타입 간의 할당 시 해결 방법.
80. **Error: missing return statement**: 값을 반환해야 하는 메서드에 `return`문이 없을 때 해결 방법.
81. **Error: variable ... might not have been initialized**: 초기화되지 않은 지역 변수를 사용하려 할 때 해결 방법.
82. **Error: unreachable statement**: `return`문 뒤에 코드가 있어 실행될 수 없을 때 해결 방법.
83. **`String` vs. `StringBuilder` vs. `StringBuffer`**: 문자열 처리 성능 최적화 방법.
84. **`equals()` and `hashCode()`**: 두 메서드를 올바르게 오버라이딩하는 방법.
85. **Checked vs. Unchecked Exceptions**: 예외 종류와 올바른 처리 전략.
86. **`try-with-resources`**: 리소스 자동 해제를 통한 메모리 누수 방지.
87. **Generics (`<>`)**: 타입 안정성을 높이는 제네릭 사용법.
88. **Lambda Expressions**: 람다식을 활용한 간결한 코드 작성법.
89. **Stream API**: 컬렉션 데이터를 효율적으로 처리하는 스트림 사용법.
90. **Dependency Injection**: 의존성 주입을 통한 코드 결합도 낮추기 (Spring, Guice 등).

### Git (91-120)
91.  **fatal: not a git repository** ✅: Git 저장소가 아닌 디렉터리에서 Git 명령을 실행할 때 해결 방법.
92.  **fatal: remote origin already exists** ✅: 원격 저장소 'origin'이 이미 존재할 때 해결 방법.
93.  **error: failed to push some refs to '...'** ✅: 원격 저장소에 로컬보다 최신 커밋이 있을 때 해결 방법 (`git pull`).
94.  **Permission denied (publickey)** ✅: SSH 키 인증 실패 시 해결 방법.
95.  **fatal: refusing to merge unrelated histories** ✅: 관련 없는 두 프로젝트를 병합하려 할 때 해결 방법.
96.  **error: Your local changes to the following files would be overwritten by merge** ✅: 커밋하지 않은 변경 사항이 병합으로 덮어쓰여질 위험이 있을 때 (`git stash`).
97.  **fatal: pathspec '...' did not match any files** ✅: `git add` 또는 `git rm` 등에서 파일 경로가 잘못되었을 때 해결 방법.
98.  **The requested URL returned error: 403** ✅: 원격 저장소에 접근할 권한이 없을 때 (HTTPS 인증).
99.  **fatal: unable to access '...': The requested URL returned error: 404** ✅: 원격 저장소 주소가 잘못되었을 때 해결 방법.
100. **error: src refspec ... does not match any**: 푸시하려는 브랜치 이름이 로컬에 존재하지 않을 때 해결 방법.
101. **fatal: A branch named '...' already exists**: 이미 존재하는 이름으로 브랜치를 생성하려 할 때 해결 방법.
102. **Detached HEAD state**: 특정 커밋을 직접 체크아웃하여 '분리된 HEAD' 상태가 되었을 때 해결 방법.
103. **fatal: bad object ...**: Git 개체 파일이 손상되었을 때 해결 방법.
104. **error: object file ... is empty**: Git 개체 파일이 비어 있을 때 해결 방법.
105. **fatal: index file corrupt**: 인덱스 파일(.git/index)이 손상되었을 때 해결 방법.
106. **Reverting a commit**: 특정 커밋을 되돌리는 `git revert` 사용법.
107. **Resetting a commit**: 특정 커밋으로 되돌아가는 `git reset`의 세 가지 옵션 (soft, mixed, hard).
108. **Amending a commit**: 최신 커밋 메시지 또는 내용을 수정하는 `git commit --amend` 사용법.
109. **Interactive rebase**: 여러 커밋을 합치거나 수정하는 `git rebase -i` 사용법.
110. **Cherry-picking a commit**: 다른 브랜치의 특정 커밋만 현재 브랜치로 가져오는 `git cherry-pick` 사용법.
111. **Resolving merge conflicts**: 병합 충돌 발생 시 수동으로 해결하는 방법.
112. **Using `.gitignore`**: 특정 파일 및 디렉터리를 Git 추적에서 제외하는 방법.
113. **Git LFS (Large File Storage)**: 대용량 파일을 효율적으로 관리하는 방법.
114. **Git Submodules**: 다른 Git 저장소를 하위 디렉터리로 포함하는 방법.
115. **Git hooks**: 특정 Git 이벤트(커밋, 푸시 등)에 자동으로 스크립트를 실행하는 방법.
116. **fatal: could not read Username for 'https://...': terminal prompts disabled**: 터미널 프롬프트가 비활성화된 환경에서 인증 오류 발생 시 해결 방법.
117. **LF will be replaced by CRLF**: Windows와 macOS/Linux 간의 줄 바꿈 문자 차이 문제 해결.
118. **error: RPC failed; curl 56 Recv failure**: 대용량 푸시/클론 시 네트워크 문제 해결.
119. **fatal: early EOF**: 예기치 않게 서버 연결이 종료될 때 해결 방법.
120. **`git bisect`**: 버그를 유발한 커밋을 자동으로 찾아내는 방법.