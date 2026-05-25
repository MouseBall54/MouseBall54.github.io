---
typora-root-url: ../
layout: single
title: >
    JavaScript 이벤트 리스너 메모리 누수 (Event Listener Leaks) 해결 방법

date: 2025-03-09T07:27:00+09:00
lang: ko
translation_id: javascript-event-listener-leaks
header:
    teaser: /images/header_images/overlay_image_js.png
    overlay_image: /images/header_images/overlay_image_js.png
    overlay_filter: 0.5
    image_description: >
      이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: JavaScript 이벤트 리스너 메모리 누수 (Event Listener Leaks) 해결 방법
excerpt: >
    이벤트 리스너를 제거하지 않으면 메모리 누수가 발생하여 애플리케이션 성능이 저하될 수 있습니다. 이 글에서는 JavaScript에서 이벤트 리스너 누수의 원인과 해결 방법을 알아봅니다.
seo_description: >
    이벤트 리스너를 제거하지 않으면 메모리 누수가 발생하여 애플리케이션 성능이 저하될 수 있습니다. 이 글에서는 JavaScript에서 이벤트 리스너 누수의 원인과 해결 방법을 알아봅니다.
categories:
    - ko_Troubleshooting
tags:
    - JavaScript
    - Memory Leak
    - Event Listener
---


![이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: JavaScript 이벤트 리스너 메모리 누수 (Event Listener Leaks) 해결 방법](/images/header_images/overlay_image_js.png)
## JavaScript 이벤트 리스너 누수란?

이벤트 리스너 누수(Event Listener Leak)는 `addEventListener`로 등록한 이벤트 리스너를 더 이상 필요하지 않을 때 `removeEventListener`로 제거하지 않아 발생하는 메모리 누수 현상입니다. 이 문제는 특히 동적으로 DOM 요소를 추가하고 제거하는 단일 페이지 애플리케이션(SPA)에서 흔하게 발생하며, 애플리케이션의 반응성을 떨어뜨리고 심한 경우 브라우저를 멈추게 할 수 있습니다.

## 이벤트 리스너 누수의 원인

가장 큰 원인은 DOM 요소가 제거될 때 해당 요소에 부착된 이벤트 리스너가 함께 제거되지 않는다는 점입니다. 브라우저의 가비지 컬렉터는 이벤트 리스너가 DOM 요소를 참조하고, DOM 요소 또한 리스너를 참조하는 상호 참조 관계 때문에 메모리에서 이들을 해제하지 못할 수 있습니다.

**누수 발생 예제:**
```javascript
function setupComponent() {
    const button = document.getElementById('my-button');
    const handleResize = () => console.log('Resized!');

    // 이벤트 리스너 등록
    window.addEventListener('resize', handleResize);

    // 컴포넌트가 사라질 때 리스너를 제거하는 로직이 없음
    // button.remove(); // 버튼만 제거되고 window의 리스너는 남음
}

// 컴포넌트가 여러 번 생성되고 제거되면 handleResize 리스너가 계속 중첩되어 쌓임
```

## 이벤트 리스너 누수 해결 방법

### 1. `removeEventListener`로 명시적 제거

가장 기본적이고 확실한 방법은 컴포넌트나 DOM 요소가 파괴되는 시점에 등록했던 이벤트 리스너를 명시적으로 제거하는 것입니다.

**중요**: `removeEventListener`가 동작하려면 `addEventListener`에 전달했던 것과 **정확히 동일한 함수 참조**를 전달해야 합니다. 익명 함수를 사용하면 제거할 수 없습니다.

**잘못된 예 (익명 함수):**
```javascript
// 이렇게 등록하면 제거할 방법이 없음
window.addEventListener('resize', () => console.log('Resized!'));
```

**올바른 예 (함수 참조 사용):**
```javascript
const handleResize = () => console.log('Resized!');

// 등록
window.addEventListener('resize', handleResize);

// 제거
window.removeEventListener('resize', handleResize);
```

**클래스 컴포넌트 패턴:**
```javascript
class MyComponent {
    constructor() {
        this.handleScroll = this.handleScroll.bind(this);
    }

    mount() {
        window.addEventListener('scroll', this.handleScroll);
    }

    unmount() {
        // 컴포넌트가 사라질 때 리스너 제거
        window.removeEventListener('scroll', this.handleScroll);
        console.log('Event listener removed.');
    }

    handleScroll() {
        console.log('Scrolled!');
    }
}

const component = new MyComponent();
component.mount();
// ... 시간이 지난 후
component.unmount();
```

### 2. `AbortController` 사용 (최신 방법)

`AbortController`는 이벤트 리스너를 포함한 비동기 작업을 한 번에 중단시키는 데 사용될 수 있는 최신 API입니다. `addEventListener`의 `signal` 옵션과 함께 사용하면 여러 개의 이벤트 리스너를 한 번에 깔끔하게 제거할 수 있습니다.

```javascript
const controller = new AbortController();
const signal = controller.signal;

const handleClick = () => console.log('Clicked!');
const handleMouseOver = () => console.log('Mouse over!');

// signal 옵션을 사용하여 리스너 등록
document.getElementById('my-btn').addEventListener('click', handleClick, { signal });
document.getElementById('my-btn').addEventListener('mouseover', handleMouseOver, { signal });

// 필요 없어지면 컨트롤러의 abort() 메서드를 호출하여 모든 리스너를 한 번에 제거
// controller.abort();
// console.log('All event listeners removed.');
```

### 3. 이벤트 위임 (Event Delegation)

이벤트 위임은 여러 자식 요소의 이벤트를 부모 요소 하나에서 처리하는 패턴입니다. 개별 요소마다 리스너를 등록하는 대신 상위 요소에 하나의 리스너만 등록하므로, 리스너 관리 부담이 줄어들고 동적으로 추가/제거되는 요소에도 효과적으로 대응할 수 있습니다.

```html
<ul id="parent-list">
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
</ul>
```
```javascript
document.getElementById('parent-list').addEventListener('click', (event) => {
    // event.target은 실제 클릭된 자식 요소를 가리킴
    if (event.target && event.target.matches('li')) {
        console.log('Clicked item:', event.target.textContent);
    }
});
```

## 결론

이벤트 리스너 누수는 쉽게 간과할 수 있지만 애플리케이션 성능에 심각한 영향을 미칠 수 있습니다. 컴포넌트의 생명주기(lifecycle)를 명확히 이해하고, 요소가 제거될 때 반드시 등록된 리스너를 `removeEventListener`나 `AbortController`를 통해 제거하는 습관을 들이는 것이 중요합니다. 이벤트 위임 패턴은 리스너 관리를 단순화하는 좋은 대안이 될 수 있습니다.

## 전문 보완 체크

**JavaScript 이벤트 리스너 메모리 누수 (Event Listener Leaks) 해결 방법**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 실행 환경, 정확한 오류 경계, 최소 재현 예제, 되돌릴 수 있는 경로를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

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

독자가 **JavaScript 이벤트 리스너 메모리 누수 (Event Listener Leaks) 해결 방법**의 첫 번째 권장 조치를 이미 시도했지만 결과가 여전히 불확실하다고 가정해 봅니다. 다음 단계는 여러 해결책을 한꺼번에 시험하는 것이 아니라 짧은 감사 기록을 만드는 것입니다. 먼저 어떤 판단을 하려는지 한 문장으로 쓰고, 환경을 한 문장으로 적고, 관찰된 결과를 한 문장으로 남깁니다. 그다음 실행 환경, 정확한 오류 경계, 최소 재현 예제, 되돌릴 수 있는 경로를 이미 확보한 사실과 대조합니다. 이렇게 해야 글이 서로 끊어진 팁 목록이 아니라 검증 가능한 절차가 됩니다.

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
