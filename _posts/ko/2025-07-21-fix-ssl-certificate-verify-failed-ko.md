---
typora-root-url: ../
layout: single
title: "SSL: CERTIFICATE_VERIFY_FAILED 오류 해결 방법 (Windows Python)"
excerpt: "Windows Python에서 SSL: CERTIFICATE_VERIFY_FAILED 오류를 certifi 설치, REQUESTS_CA_BUNDLE/SSL_CERT_FILE 설정, 올바른 CA 번들 사용으로 해결하는 방법."
date: 2025-07-21T22:00:00+09:00
header:
   teaser: /images/header_images/overlay_image_python.png
   overlay_image: /images/header_images/overlay_image_python.png
   overlay_filter: 0.3
categories:
  - ko_Troubleshooting
tags:
  - SSL
  - Python
  - Windows
  - Security
---


## 소개

SSL 인증서 검증 실패 오류를 해결합니다.
Python `requests`나 `ssl` 라이브러리에서 자주 발생합니다.
Windows 환경에서 원인과 대응책을 정리했습니다.

## 오류 내용

```
SSLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:…)
```

인증 기관(CA) 번들을 찾지 못하거나 신뢰하지 못할 때 발생합니다.

## 주요 원인

* 시스템에 CA 인증서가 없거나 오래됨.
* 환경 변수 설정이 잘못됨.
* 회사 프록시가 SSL을 가로챔.
* Python이 OS의 인증서 저장소를 찾지 못함.

## 해결 방법 1: Certifi 사용

1. `certifi` 설치

   ```bash
   pip install certifi
   ```
2. 코드에서 번들 지정

   ```python
   import requests, certifi

   resp = requests.get(
       "https://example.com",
       verify=certifi.where()
   )
   print(resp.status_code)
   ```

## 해결 방법 2: REQUESTS\_CA\_BUNDLE 설정

1. 번들 경로 확인

   ```bash
   python -c "import certifi; print(certifi.where())"
   ```
2. PowerShell에서 환경 변수 등록

   ```powershell
   setx REQUESTS_CA_BUNDLE "C:\path\to\cacert.pem"
   ```
3. 터미널이나 IDE 재시작

## 해결 방법 3: SSL\_CERT\_FILE 설정 (Windows)

1. PEM 파일 다운로드 (예: curl.se/docs/caextract.html)
2. PowerShell에 설정 추가

   ```powershell
   setx SSL_CERT_FILE "C:\path\to\cacert.pem"
   ```
3. 터미널이나 IDE 재시작

## 해결 방법 4: 검증 우회 (테스트 전용)

```python
import requests
resp = requests.get("https://example.com", verify=False)
print(resp.status_code)
```

> **주의:** MITM 공격에 취약해집니다.

## 해결 방법 5: 세션 단위 번들 지정

```python
import requests

sess = requests.Session()
sess.verify = "C:\\path\\to\\cacert.pem"

resp = sess.get("https://example.com")
print(resp.ok)
```

## 결론

정상 CA 번들을 사용하세요.
`certifi`나 시스템 인증서를 권장합니다.
실서비스에서는 검증 우회를 피하세요.

