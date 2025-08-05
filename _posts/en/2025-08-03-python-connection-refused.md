---
typora-root-url: ../
layout: single
title: >
    How to Fix "ConnectionError: [Errno 111] Connection refused" in Python
date: 2025-08-03T16:00:00+09:00
header:
    teaser: /images/header_images/overlay_image_python.png
    overlay_image: /images/header_images/overlay_image_python.png
    overlay_filter: 0.5
excerpt: >
    In Python, a "Connection refused" error occurs when a network connection is rejected by the target server. This article explains the causes of the error and how to fix it.
categories:
    - en_Troubleshooting
tags:
    - Python
    - ConnectionError
    - Network
    - Socket
---

## What is "ConnectionError: [Errno 111] Connection refused" in Python?

`ConnectionError: [Errno 111] Connection refused` is an error that indicates a connection attempt to a remote server was rejected. This typically happens when using networking libraries like `socket` or `requests`. The number `111` is the error code for "Connection refused" on Linux systems (other operating systems, like Windows, may show a different error code).

This error is not usually a problem with the client-side code, but rather a signal that the **server is not ready to accept the client's connection**.

## Common Causes of "Connection refused"

1.  **Server Not Running**: This is the most common cause. No application is running on the target IP address and port.
2.  **Incorrect IP Address or Port**: The server is running, but the client is trying to connect to the wrong IP address or port number.
3.  **Firewall**: A firewall on the server, the client, or a network device in between (like a router) is blocking the connection to the specified port.
4.  **Server Listening Address Misconfiguration**: The server application might be bound only to `localhost` or `127.0.0.1`. In this case, it can only accept connections from within the same machine. To allow external connections, it must be bound to `0.0.0.0`.
5.  **Server Connection Backlog Exceeded**: The server is rejecting new connections because its queue for pending connections is full. This can happen under very high server load.

## How to Fix "Connection refused"

### 1. Check the Server Status

First, verify that the server you are trying to connect to is running correctly.

-   If you have direct access to the server, check if the application's process is running.
-   Review the server logs to ensure there were no errors on startup.

### 2. Verify the IP Address and Port

Double-check that the IP address and port hardcoded in your client code match the address and port the server is listening on.

You can use the `netstat` command on the server to see which ports are being listened on.

```bash
# Linux/macOS
netstat -an | grep LISTEN

# Windows
netstat -an | findstr "LISTENING"
```

### 3. Check Firewall Settings

Ensure the server's firewall is configured to allow connections on the target port. For example, you need to check if the port (e.g., 8080) is allowed in the inbound rules of `ufw` or `firewalld` on Linux, or in the Windows Firewall settings.

You may also need to check that outbound connections are not blocked on the client side.

### 4. Check the Server's Listening Address

Make sure the server application is configured to accept connections from all network interfaces. When setting up a web or API server, the host address should typically be set to `0.0.0.0`, not `127.0.0.1`, to allow external access.

**Flask Example:**
```python
# Only accepts connections from localhost
# app.run(host='127.0.0.1', port=5000)

# Accepts connections from any IP address
app.run(host='0.0.0.0', port=5000)
```

### 5. Perform a Simple Connection Test

You can use a simple tool like `telnet` or `nc` (netcat) to test if a basic TCP connection can be established from the client machine to the server.

```bash
telnet <server_ip> <port>
# Example: telnet 192.168.1.100 8080
```
If you also get a "Connection refused" error here, it confirms that the problem is with the network or server configuration, not your Python code.

## Conclusion

`ConnectionError: [Errno 111] Connection refused` is a common issue in network programming, and its cause usually lies with the server's state or network configuration rather than the client's code. To resolve it, a systematic approach is needed: check if the server is running correctly, listening on the right address and port, and not being blocked by a firewall.

