---
typora-root-url: ../
layout: single
title: "JavaScript '[Violation] 'click' handler took ...ms' 경고 해결 방법"
date: 2025-08-01T11:00:00+09:00
header:
   teaser: /images/header_images/overlay_image_js.png
   overlay_image: /images/header_images/overlay_image_js.png
   overlay_filter: 0.5
excerpt: >
  `setTimeout`, Web Worker, `requestAnimationFrame`과 같은 기술을 사용하여 무거운 작업을 지연시켜 오래 실행되는 'click' 핸들러를 최적화하고 브라우저 응답성을 개선합니다.
categories:
  - ko_Troubleshooting
tags:
  - JavaScript
  - Performance
  - Event Handler
  - Optimization
---

콘솔에서 `[Violation] 'click' handler took <N>ms`라는 경고를 본 적이 있다면, 이는 클릭 이벤트 핸들러가 실행되는 데 너무 오랜 시간이 걸린다는 브라우저의 신호입니다. 이는 느리고 응답 없는 사용자 인터페이스로 이어져 좋지 않은 사용자 경험을 유발할 수 있습니다.

이 글에서는 이 위반이 발생하는 이유와 이벤트 핸들러를 최적화하여 해결하는 방법을 설명합니다.

### 이 위반은 왜 발생하나요?

JavaScript는 사용자 인터페이스(UI) 렌더링도 담당하는 단일 스레드에서 실행됩니다. 사용자가 버튼을 클릭하면 연결된 이벤트 핸들러 함수가 이 메인 스레드에서 실행됩니다.

만약 핸들러가 복잡한 계산, 대용량 데이터 처리 또는 동기식 네트워크 요청과 같은 무겁고 시간이 많이 걸리는 작업을 수행하면 메인 스레드를 차단합니다. 핸들러가 실행되는 동안 브라우저는 UI 업데이트, 다른 사용자 입력에 대한 응답 또는 애니메이션 실행과 같은 다른 작업을 수행할 수 없습니다. 페이지가 멈추거나 버벅거리게 됩니다.

브라우저는 이벤트 핸들러가 소요되어야 하는 시간에 대한 임계값(일반적으로 약 50-100ms)을 가지고 있습니다. 이 한도를 초과하면 브라우저는 개발자에게 경고하기 위해 이를 "위반"으로 표시합니다.

### 오래 실행되는 이벤트 핸들러 해결 방법

핵심은 메인 스레드가 UI 업데이트를 처리할 수 있도록 무거운 작업을 메인 스레드에서 분리하는 것입니다.

#### 1. `setTimeout`으로 실행 지연하기

메인 스레드를 확보하는 가장 간단한 방법은 `setTimeout`을 `0`의 지연 시간과 함께 사용하여 무거운 작업을 지연시키는 것입니다. 이는 현재 이벤트 핸들러가 완료되고 브라우저가 UI를 업데이트할 기회를 가진 후, 별도의 태스크에서 함수를 실행하도록 예약합니다.

```javascript
// 이전: 오래 실행되는 작업이 메인 스레드를 차단함
button.addEventListener('click', () => {
  // 무거운 작업 시뮬레이션
  for (let i = 0; i < 1e9; i++) {
    // ...
  }
  console.log('작업 완료');
});

// 이후: setTimeout으로 작업 지연하기
button.addEventListener('click', () => {
  console.log('핸들러 완료, UI 응답성 유지');
  
  setTimeout(() => {
    // 무거운 작업 시뮬레이션
    for (let i = 0; i < 1e9; i++) {
      // ...
    }
    console.log('지연된 작업 완료');
  }, 0);
});
```

#### 2. 정말 무거운 계산에는 Web Worker 사용하기

`setTimeout`으로도 메인 스레드를 차단할 수 있는 CPU 집약적인 작업의 경우, 가장 좋은 해결책은 **Web Worker**입니다. Web Worker를 사용하면 메인 UI 스레드와 완전히 분리된 백그라운드 스레드에서 스크립트를 실행할 수 있습니다.

**main.js:**
```javascript
const worker = new Worker('worker.js');

button.addEventListener('click', () => {
  // 워커에게 작업을 시작하라는 메시지 전송
  worker.postMessage({ command: 'start' });
});

// 워커로부터 오는 메시지 수신
worker.onmessage = (e) => {
  console.log('워커 작업 완료, 결과:', e.data.result);
};
```

**worker.js:**
```javascript
self.onmessage = (e) => {
  if (e.data.command === 'start') {
    // 무거운 계산 수행
    let result = 0;
    for (let i = 0; i < 1e9; i++) {
      result += i;
    }
    // 결과를 메인 스레드로 다시 전송
    self.postMessage({ result: result });
  }
};
```

#### 3. 작업을 청크(Chunk)로 나누기

큰 배열을 처리하거나 일련의 단계를 수행하는 경우, 작업을 더 작은 청크로 나눌 수 있습니다. 한 청크를 처리한 다음 `setTimeout` 또는 `requestAnimationFrame`을 사용하여 다음 청크를 예약합니다. 이렇게 하면 브라우저가 그 사이에 다른 작업을 처리할 시간을 가질 수 있습니다.

```javascript
function processAll(data) {
  let i = 0;
  
  function doChunk() {
    const CHUNK_SIZE = 100;
    for (let j = 0; j < CHUNK_SIZE && i < data.length; j++, i++) {
      // data[i] 처리
    }
    
    if (i < data.length) {
      setTimeout(doChunk, 0); // 다음 청크 예약
    }
  }
  
  doChunk();
}
```

#### 4. UI 업데이트에는 `requestAnimationFrame` 사용하기

오래 실행되는 작업이 직접적인 DOM 조작이나 애니메이션을 포함하는 경우 `requestAnimationFrame`을 사용하세요. 이는 브라우저에 애니메이션을 수행하고 싶다고 알리고, 다음 애니메이션 프레임에 창을 다시 그리도록 요청합니다. 시각적 업데이트를 처리하는 가장 효율적인 방법입니다.

### 결론

`[Violation] 'click' handler took ...ms` 경고는 중요한 성능 지표입니다. 이는 코드가 메인 스레드를 차단하고 사용자 경험을 저하시키고 있음을 나타냅니다. `setTimeout`으로 필수적이지 않은 작업을 지연시키거나, 무거운 계산을 Web Worker로 옮기거나, 큰 작업을 청크로 나누어 UI를 부드럽고 응답성 있게 유지할 수 있습니다.
