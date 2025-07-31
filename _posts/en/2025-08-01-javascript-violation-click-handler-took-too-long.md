---
typora-root-url: ../
layout: single
title: "How to Fix '[Violation] 'click' handler took ...ms' in JavaScript"
date: 2025-08-01T11:00:00+09:00
header:
   teaser: /images/header_images/overlay_image_js.png
   overlay_image: /images/header_images/overlay_image_js.png
   overlay_filter: 0.5
excerpt: >
  Optimize long-running 'click' handlers and improve browser responsiveness by deferring heavy tasks with techniques like `setTimeout`, Web Workers, and `requestAnimationFrame`.
categories:
  - en_Troubleshooting
tags:
  - JavaScript
  - Performance
  - Event Handler
  - Optimization
---

If you've ever seen the console warning `[Violation] 'click' handler took <N>ms`, it's your browser's way of telling you that a click event handler is taking too long to execute. This can lead to a sluggish, unresponsive user interface, creating a poor user experience.

This article explains why this violation occurs and how to fix it by optimizing your event handlers.

### Why Does This Violation Happen?

JavaScript runs on a single thread, which is also responsible for rendering the user interface (UI). When a user clicks a button, the associated event handler function is executed on this main thread.

If the handler performs a heavy, time-consuming task—such as complex calculations, large data processing, or synchronous network requests—it blocks the main thread. While the handler is running, the browser cannot perform any other tasks, like updating the UI, responding to other user inputs, or running animations. The page becomes frozen or janky.

Browsers have a threshold (typically around 50-100ms) for how long an event handler should take. If it exceeds this limit, the browser flags it as a "violation" to alert the developer.

### How to Fix Long-Running Event Handlers

The key is to offload heavy work from the main thread so it can remain free to handle UI updates.

#### 1. Defer Execution with `setTimeout`

The simplest way to free up the main thread is to defer the heavy task using `setTimeout` with a delay of `0`. This schedules the function to run in a separate task, after the current event handler has finished and the browser has had a chance to update the UI.

```javascript
// Before: A long-running task blocks the main thread
button.addEventListener('click', () => {
  // Simulate a heavy task
  for (let i = 0; i < 1e9; i++) {
    // ...
  }
  console.log('Task finished');
});

// After: Deferring the task with setTimeout
button.addEventListener('click', () => {
  console.log('Handler finished, UI is responsive');
  
  setTimeout(() => {
    // Simulate a heavy task
    for (let i = 0; i < 1e9; i++) {
      // ...
    }
    console.log('Deferred task finished');
  }, 0);
});
```

#### 2. Use Web Workers for Truly Heavy Computation

For CPU-intensive operations that would still block the main thread even with `setTimeout`, the best solution is a **Web Worker**. Web Workers allow you to run scripts in a background thread, completely separate from the main UI thread.

**main.js:**
```javascript
const worker = new Worker('worker.js');

button.addEventListener('click', () => {
  // Send a message to the worker to start the task
  worker.postMessage({ command: 'start' });
});

// Listen for messages back from the worker
worker.onmessage = (e) => {
  console.log('Worker finished with result:', e.data.result);
};
```

**worker.js:**
```javascript
self.onmessage = (e) => {
  if (e.data.command === 'start') {
    // Perform heavy computation
    let result = 0;
    for (let i = 0; i < 1e9; i++) {
      result += i;
    }
    // Send the result back to the main thread
    self.postMessage({ result: result });
  }
};
```

#### 3. Break Down Tasks into Chunks

If you are processing a large array or performing a series of steps, you can break the work into smaller chunks. Process one chunk, then use `setTimeout` or `requestAnimationFrame` to schedule the next chunk. This gives the browser time to handle other tasks in between.

```javascript
function processAll(data) {
  let i = 0;
  
  function doChunk() {
    const CHUNK_SIZE = 100;
    for (let j = 0; j < CHUNK_SIZE && i < data.length; j++, i++) {
      // process data[i]
    }
    
    if (i < data.length) {
      setTimeout(doChunk, 0); // Schedule the next chunk
    }
  }
  
  doChunk();
}
```

#### 4. Use `requestAnimationFrame` for UI Updates

If your long-running task involves direct DOM manipulation or animations, use `requestAnimationFrame`. This tells the browser you want to perform an animation and requests that the browser schedule a repaint of the window for the next animation frame. It's the most efficient way to handle visual updates.

### Conclusion

The `[Violation] 'click' handler took ...ms` warning is a critical performance indicator. It signals that your code is blocking the main thread and degrading the user experience. By deferring non-essential work with `setTimeout`, moving heavy computations to Web Workers, or chunking large tasks, you can keep your UI smooth and responsive.
