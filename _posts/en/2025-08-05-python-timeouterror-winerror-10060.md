---
typora-root-url: ../
layout: single
title: >
   How to Fix Python TimeoutError: [WinError 10060] A connection attempt failed

lang: en
translation_id: python-timeouterror-winerror-10060
header:
   teaser: /images/header_images/overlay_image_python.png
   overlay_image: /images/header_images/overlay_image_python.png
   overlay_filter: 0.5
excerpt: >
   Learn how to resolve the Python TimeoutError: [WinError 10060], which occurs when a network connection times out. This guide covers causes like firewalls, incorrect addresses, and server issues, providing clear solutions.
categories:
   - en_Troubleshooting
tags:
   - Python
   - TimeoutError
   - WinError 10060
   - Networking
   - Troubleshooting
---

## Introduction

When working with network programming in Python, you might encounter the `TimeoutError: [WinError 10060]`. This error indicates that a connection attempt failed because the connected party did not properly respond after a period of time, or an established connection failed because the connected host has failed to respond. It's a common issue, especially in applications that rely on network sockets, such as web clients, APIs, or database connectors.

This guide will walk you through the common causes of this error and provide step-by-step solutions to fix it.

## What Causes `TimeoutError: [WinError 10060]`?

This error typically occurs due to one of the following reasons:

1.  **Incorrect IP Address or Port**: The server you are trying to connect to does not exist at the specified IP address or is not listening on the specified port.
2.  **Firewall Restrictions**: A firewall on your local machine, network, or the remote server is blocking the connection.
3.  **Server Not Running or Overloaded**: The server application is not running, has crashed, or is too busy to accept new connections.
4.  **Network Issues**: General network problems, such as packet loss or high latency, can prevent a timely response.
5.  **Short Timeout Value**: The timeout configured in your Python script is too short for the server to respond, especially for long-running operations.

## How to Fix the Error

Let's explore the solutions for each of the causes mentioned above.

### 1. Verify the IP Address and Port

The first step is to ensure that the IP address and port you are trying to connect to are correct.

-   **Check for typos**: Double-check the IP address and port number in your code.
-   **Confirm server details**: Verify with the server administrator that you have the correct connection details.
-   **Use network tools**: You can use tools like `ping` or `telnet` to test connectivity.

```bash
# Ping the server to check if it's reachable
ping example.com

# Telnet to the specific port to see if it's open
telnet example.com 8080
```

If `ping` fails or `telnet` cannot connect, the issue is likely with the address or network accessibility.

### 2. Check Firewall Settings

Firewalls are a common culprit. Check the firewall settings on both your client machine and the remote server.

-   **Local Firewall**: Temporarily disable your local firewall (e.g., Windows Defender Firewall) to see if the connection succeeds. If it does, create an outbound rule to allow your Python script to make connections.
-   **Network Firewall**: If you are on a corporate or restricted network, contact your network administrator to ensure the connection is not being blocked.
-   **Server Firewall**: The server's firewall might be blocking incoming connections on the required port. Ensure the port is open for incoming traffic.

### 3. Ensure the Server is Running and Responsive

Confirm that the server application you are trying to connect to is running and able to handle new connections.

-   **Check server status**: Log in to the server and check if the service or application is active.
-   **Review server logs**: Server logs can provide valuable information about why it might not be responding, such as errors or resource limitations.
-   **Test with another client**: Try connecting from a different client or tool to rule out a client-side issue.

### 4. Increase the Timeout Value

If the server is running but takes a long time to process requests, the default timeout in your client might be too short. You can increase the timeout value in your Python code.

For example, when using the popular `requests` library:

```python
import requests

try:
    # Set a longer timeout (e.g., 30 seconds)
    response = requests.get('http://example.com', timeout=30)
    print("Connection successful!")
except requests.exceptions.Timeout:
    print("The request timed out.")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
```

If you are working with raw sockets, you can use `socket.settimeout()`:

```python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(30)  # Set a 30-second timeout

try:
    s.connect(('example.com', 8080))
    print("Connection successful!")
except socket.timeout:
    print("The connection timed out.")
except socket.error as e:
    print(f"An error occurred: {e}")
finally:
    s.close()
```

### 5. Implement Retry Logic

Network connections can be unreliable. Implementing a retry mechanism with an exponential backoff strategy can make your application more resilient to transient network issues.

Here is an example of how to implement simple retry logic:

```python
import requests
import time

def connect_with_retry(url, retries=3, delay=5):
    for i in range(retries):
        try:
            response = requests.get(url, timeout=10)
            return response
        except requests.exceptions.Timeout:
            print(f"Timeout on attempt {i+1}. Retrying in {delay} seconds...")
            time.sleep(delay)
    raise ConnectionError(f"Failed to connect to {url} after {retries} attempts.")

try:
    response = connect_with_retry('http://example.com')
    print("Connection successful!")
except ConnectionError as e:
    print(e)
```

## Conclusion

The `TimeoutError: [WinError 10060]` is a common network-related error in Python on Windows. By systematically checking the server address, firewall rules, server status, and connection timeouts, you can effectively diagnose and resolve the issue. Implementing robust error handling, such as increasing timeouts and adding retry logic, will make your network applications more reliable.
