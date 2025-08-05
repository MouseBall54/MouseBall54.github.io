---
typora-root-url: ../
layout: single
title: >
   JavaScript innerHTML vs. textContent: 어느 것을 사용해야 할까요?
date: 2025-08-05T11:05:00+09:00
header:
   teaser: /images/header_images/overlay_image_js.png
   overlay_image: /images/header_images/overlay_image_js.png
   overlay_filter: 0.5
excerpt: >
   JavaScript에서 innerHTML과 textContent의 주요 차이점을 이해하세요. 웹 애플리케이션에서 더 나은 보안, 성능 및 예측 가능성을 위해 각 속성을 언제 사용해야 하는지 알아보세요.
categories:
   - ko_Troubleshooting
tags:
   - JavaScript
   - DOM
   - innerHTML
   - textContent
   - Security
---

## 서론

JavaScript를 사용하여 HTML 요소의 콘텐츠를 가져오거나 설정해야 할 때, `innerHTML`과 `textContent`라는 두 가지 일반적인 속성을 빠르게 접하게 됩니다. 비슷해 보일 수 있지만, 콘텐츠를 처리하는 방식에 중요한 차이가 있으며 이는 보안, 성능 및 동작에 영향을 미칩니다. 올바른 것을 선택하는 것은 강력하고 안전한 코드를 작성하는 데 필수적입니다.

이 가이드에서는 `innerHTML`과 `textContent`를 비교하여 다양한 시나리오에서 어떤 것을 사용해야 할지 결정하는 데 도움을 드립니다.

## `innerHTML`이란 무엇인가요?

`innerHTML` 속성은 요소 내에 포함된 HTML 마크업을 가져오거나 설정합니다. `innerHTML`을 설정하면 브라우저는 제공한 문자열을 HTML로 구문 분석하고 해당 요소의 DOM 트리를 다시 빌드합니다.

**예제:**
```html
<div id="my-div">이것은 <strong>오래된</strong> 텍스트입니다.</div>
```

```javascript
const myDiv = document.getElementById('my-div');

// 콘텐츠 가져오기
console.log(myDiv.innerHTML);
// 출력: 이것은 <strong>오래된</strong> 텍스트입니다.

// 콘텐츠 설정하기
myDiv.innerHTML = '이것은 <span>새로운</span> 텍스트입니다.';
// 이제 div는 span 요소를 포함한 새로운 HTML 콘텐츠를 포함합니다.
```

### `innerHTML`의 주요 특징
-   **HTML 파싱**: HTML 태그를 인식하고 렌더링합니다.
-   **보안 위험**: 사이트 간 스크립팅(XSS) 공격에 취약합니다. 신뢰할 수 없는 사용자 입력으로 `innerHTML`을 설정하면 악의적인 사용자가 브라우저에서 실행될 `<script>` 태그나 기타 유해한 마크업을 주입할 수 있습니다.
-   **성능**: HTML을 파싱하고 DOM을 재구성하는 오버헤드가 수반되므로 일반적으로 `textContent`보다 느립니다.

## `textContent`란 무엇인가요?

`textContent` 속성은 HTML 마크업 없이 요소와 모든 하위 요소의 원시 텍스트 콘텐츠를 가져오거나 설정합니다.

**예제:**
```html
<div id="my-div">이것은 <strong>오래된</strong> 텍스트입니다.</div>
```

```javascript
const myDiv = document.getElementById('my-div');

// 콘텐츠 가져오기
console.log(myDiv.textContent);
// 출력: 이것은 오래된 텍스트입니다.

// 콘텐츠 설정하기
myDiv.textContent = '이것은 <span>새로운</span> 텍스트입니다.';
// 이제 div는 "이것은 <span>새로운</span> 텍스트입니다."라는 문자열을 그대로 포함합니다.
// <span> 태그는 파싱되지 않고 일반 텍스트로 표시됩니다.
```

### `textContent`의 주요 특징
-   **일반 텍스트만**: 모든 콘텐츠를 원시 텍스트로 처리하고 HTML 태그를 파싱하지 않습니다.
-   **보안**: HTML 태그를 문자 그대로 렌더링하여 콘텐츠를 자동으로 살균(sanitize)하므로 XSS 공격을 효과적으로 방지합니다.
-   **성능**: HTML 파싱 없이 텍스트 노드를 직접 조작하므로 `innerHTML`보다 훨씬 빠릅니다.
-   **CSS 인지**: `textContent`는 CSS에 의해 숨겨진 요소(예: `display: none;`)를 포함한 모든 요소의 텍스트를 반환합니다. 반면, 유사한 `innerText` 속성은 숨겨진 텍스트를 포함하지 않습니다.

## `innerHTML` vs. `textContent`: 비교

| 기능 | `innerHTML` | `textContent` |
| --- | --- | --- |
| **콘텐츠 유형** | HTML 문자열 | 일반 텍스트 문자열 |
| **보안** | **XSS에 취약**. 신뢰할 수 있는 콘텐츠에만 사용하세요. | **기본적으로 안전**. HTML을 자동으로 살균합니다. |
| **성능** | 느림 (HTML 파싱으로 인해) | 빠름 (직접적인 텍스트 조작) |
| **사용법** | 명시적으로 HTML 마크업을 렌더링해야 할 때. | 일반 텍스트로만 작업해야 할 때. |
| **출력** | HTML 태그, 주석, 텍스트를 반환합니다. | 텍스트 콘텐츠만 반환합니다. |

## 어느 것을 사용해야 할까요?

간단한 경험 법칙은 다음과 같습니다.

> **`innerHTML`을 사용해야 하는 구체적이고 안전한 이유가 없는 한 항상 `textContent`를 기본으로 사용하세요.**

-   **`textContent`를 사용하는 경우:**
    -   사용자 입력에서 오는 텍스트를 설정할 때.
    -   일반 텍스트만 표시하거나 업데이트해야 할 때.
    -   보안과 성능이 우선순위일 때.

-   **`innerHTML`을 사용하는 경우:**
    -   완전히 제어할 수 있는 콘텐츠(예: 하드코딩된 템플릿)를 설정할 때.
    -   명시적으로 HTML 요소(`<strong>`, `<span>`, `<a>` 등)를 생성하여 DOM에 삽입해야 할 때.

### `innerText`에 대한 참고 사항

`innerText`라는 세 번째 유사한 속성이 있습니다. `textContent`와는 몇 가지 면에서 다릅니다.
-   `innerText`는 CSS를 인지하므로 `display: none;`으로 숨겨진 요소의 텍스트를 반환하지 않습니다.
-   `innerText`는 리플로우(성능에 부담이 큰 레이아웃 재계산)를 유발하지만 `textContent`는 그렇지 않습니다.
-   오래된 브라우저에서는 일부 일관되지 않은 동작을 보입니다.

이러한 이유로, `innerText`의 CSS 인지 동작이 특별히 필요하지 않은 한, 성능과 예측 가능성 면에서 **일반적으로 `textContent`가 선호되는 속성**입니다.

## 결론

`innerHTML`과 `textContent`의 차이점을 이해하는 것은 안전하고 효율적인 JavaScript를 작성하는 데 중요합니다. `innerHTML`은 동적 HTML을 만드는 데 강력하지만 보안 위험을 무시할 수 없습니다. `textContent`는 모든 일반 텍스트 작업에 대해 더 안전하고 빠른 대안을 제공합니다.

두 가지 중 하나를 의식적으로 선택함으로써 XSS 취약점으로부터 애플리케이션을 보호하고 더 나은 성능을 보장할 수 있습니다. 기억하세요: **기본적으로 `textContent`를 사용하고, `innerHTML`은 주의해서 사용하세요.**
