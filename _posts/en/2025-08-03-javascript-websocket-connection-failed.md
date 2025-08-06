---
typora-root-url: ../
layout: single
title: >
    How to Fix "WebSocket connection to '...' failed" in JavaScript

lang: en
translation_id: javascript-websocket-connection-failed
header:
    teaser: /images/header_images/overlay_image_js.png
    overlay_image: /images/header_images/overlay_image_js.png
    overlay_filter: 0.5
excerpt: >
    A WebSocket connection failure in JavaScript can occur for various reasons. This article explores the common causes of the "WebSocket connection to '...' failed" error and how to resolve it.
categories:
    - en_Troubleshooting
tags:
    - JavaScript
    - WebSocket
    - Network
---

## What is "WebSocket connection to '...' failed" in JavaScript?

This error message appears in the browser console when JavaScript code attempts to establish a connection to a WebSocket server but fails. WebSocket is a protocol that enables real-time, two-way communication between a client and a server. A connection failure can be caused by various issues, including network problems, server configuration, or client-side code.

## Common Causes of "WebSocket connection failed"

1.  **Incorrect WebSocket URL**: The URL scheme is not `ws://` or `wss://` (for secure connections), or the address or port is wrong.
2.  **Server Not Running**: The WebSocket server you are trying to connect to might be down or not running.
3.  **Firewall or Proxy Issues**: A local or network firewall, or a proxy server, might be blocking the WebSocket connection on a specific port.
4.  **CORS (Cross-Origin Resource Sharing) Issues**: If the origin of the web page and the WebSocket server are different, the connection may be rejected if the server is not configured to allow connections from that origin.
5.  **Server-Side Errors**: There might be a bug in the WebSocket server application itself, or an error could occur during the handshake process.
6.  **Mixed Content Errors**: If a page loaded over HTTPS tries to connect to an insecure `ws://` protocol, the browser will block the connection for security reasons. You must use `wss://` on HTTPS pages.

## How to Fix "WebSocket connection failed"

### 1. Verify the WebSocket URL

First, ensure the WebSocket URL in your client-side code is correct.

```javascript
// Check if the URL scheme, host, and port are correct
// Example: const socket = new WebSocket('ws://localhost:8080');
// Secure example: const socket = new WebSocket('wss://example.com/socket');

const socket = new WebSocket('ws://your-server-address:port');
```

### 2. Check the Server Status

Make sure your WebSocket server is running correctly. Check the server logs for any errors and use tools like `ping` or `netstat` to test if the server is accessible.

```bash
# Check if the server is listening on the correct port (Linux/macOS)
netstat -an | grep LISTEN | grep 8080
```

### 3. Check Firewall and Proxy Settings

Confirm that the port you are using (e.g., 8080) is allowed through your firewall. If you are on a corporate or public network, a proxy server might be blocking WebSocket traffic, so you may need to contact your network administrator.

### 4. Configure Server-Side CORS and Origin Checks

If the web page and WebSocket server have different origins, you must configure the server to allow connections from your specific origin or all origins. The implementation depends on your server framework (e.g., the `ws` library in Node.js, Spring Boot).

**Node.js `ws` library example:**
```javascript
const WebSocket = require('ws');

const wss = new WebSocket.Server({ 
    server, // http server instance
    verifyClient: (info, done) => {
        // Allow specific origins
        const allowedOrigins = ['http://localhost:3000', 'https://your-frontend.com'];
        if (allowedOrigins.includes(info.origin)) {
            done(true);
        } else {
            done(false, 403, 'Forbidden');
        }
    }
});
```

### 5. Ensure You Are Using `wss://`

If your website is served over HTTPS, you must use the secure `wss://` protocol for WebSocket connections. Modern browsers block insecure connections from secure pages.

```javascript
// Always use wss:// on an HTTPS page
if (window.location.protocol === 'https:/') {
    const socket = new WebSocket('wss://your-secure-server.com/socket');
} else {
    const socket = new WebSocket('ws://your-server-address:port');
}
```

### 6. Use Browser Developer Tools

Open your browser's developer tools (F12) and check the **Console** tab for detailed error messages. The `WS` filter in the **Network** tab allows you to inspect the WebSocket handshake request and response, which can be very helpful for debugging.

## Conclusion

A WebSocket connection failure can be caused by a combination of factors. A systematic approach, starting from the client URL and moving through the server status, network settings, and server-side logic, is necessary for effective troubleshooting. The browser's developer tools are one of the most powerful resources for diagnosing the root cause, so be sure to use them.

