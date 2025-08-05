---
typora-root-url: ../
layout: single
title: >
    JavaScript 이벤트 리스너 메모리 누수 (Event Listener Leaks) 해결 방법
date: 2025-08-03T14:25:00+09:00
header:
    teaser: /images/header_images/overlay_image_js.png
    overlay_image: /images/header_images/overlay_image_js.png
    overlay_filter: 0.5
excerpt: >
    이벤트 리스너를 제거하지 않으면 메모리 누수가 발생하여 애플리케이션 성능이 저하될 수 있습니다. 이 글에서는 JavaScript에서 이벤트 리스너 누수의 원인과 해결 방법을 알아봅니다.
categories:
    - ko_Troubleshooting
tags:
    - JavaScript
    - Memory Leak
    - Event Listener
---

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

