#!/usr/bin/env python3
"""Generate paired Digital Security posts and local SVG context images."""

from __future__ import annotations

import html
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parents[1]
POST_DATE = "2026-05-21"
LAST_MODIFIED_AT = "2026-05-23T13:00:00+09:00"
KO_CATEGORY = "ko_Digital_Security"
EN_CATEGORY = "en_Digital_Security"


SOURCES = {
    "cisa_secure": {
        "ko": "CISA Secure Our World",
        "en": "CISA Secure Our World",
        "url": "https://www.cisa.gov/secure-our-world",
    },
    "cisa_small": {
        "ko": "CISA Cyber Guidance for Small Businesses",
        "en": "CISA Cyber Guidance for Small Businesses",
        "url": "https://www.cisa.gov/cyber-guidance-small-businesses",
    },
    "cisa_ransom": {
        "ko": "CISA StopRansomware Guide",
        "en": "CISA StopRansomware Guide",
        "url": "https://www.cisa.gov/stopransomware/ransomware-guide",
    },
    "cisa_hygiene": {
        "ko": "CISA Cyber Hygiene Services",
        "en": "CISA Cyber Hygiene Services",
        "url": "https://www.cisa.gov/cyber-hygiene-services",
    },
    "nist_auth": {
        "ko": "NIST SP 800-63B Authentication and Authenticator Management",
        "en": "NIST SP 800-63B Authentication and Authenticator Management",
        "url": "https://pages.nist.gov/800-63-4/sp800-63b.html",
    },
    "nist_model": {
        "ko": "NIST Digital Identity Model",
        "en": "NIST Digital Identity Model",
        "url": "https://pages.nist.gov/800-63-4/sp800-63/model/",
    },
    "ftc_phishing": {
        "ko": "FTC Protect Yourself From Phishing Scams",
        "en": "FTC Protect Yourself From Phishing Scams",
        "url": "https://consumer.ftc.gov/consumer-alerts/2025/04/protect-yourself-phishing-scams",
    },
    "ftc_2fa": {
        "ko": "FTC Two-Factor Authentication Guide",
        "en": "FTC Two-Factor Authentication Guide",
        "url": "https://consumer.ftc.gov/articles/use-two-factor-authentication-protect-your-accounts",
    },
    "ftc_identity": {
        "ko": "FTC Identity Theft Guidance",
        "en": "FTC Identity Theft Guidance",
        "url": "https://consumer.ftc.gov/articles/what-know-about-identity-theft",
    },
    "ftc_smallbiz": {
        "ko": "FTC Small Business Cybersecurity",
        "en": "FTC Small Business Cybersecurity",
        "url": "https://www.ftc.gov/business-guidance/small-businesses/cybersecurity",
    },
    "kisa_boho": {
        "ko": "KISA 보호나라",
        "en": "KISA BohoNara Cybersecurity Portal",
        "url": "https://www.boho.or.kr/",
    },
    "kisa_privacy": {
        "ko": "KISA 개인정보침해 신고센터",
        "en": "KISA Personal Information Infringement Report Center",
        "url": "https://privacy.kisa.or.kr/main.do",
    },
    "kisa_spam": {
        "ko": "KISA 불법스팸대응센터",
        "en": "KISA Spam Response Center",
        "url": "https://spam.kisa.or.kr/spam/main.do",
    },
}


TOPICS = [
    {
        "slug": "phishing-message-triage",
        "ko_title": "피싱 문자와 이메일 30초 판별법: 링크를 누르기 전 확인할 것",
        "en_title": "A 30-Second Phishing Triage: What to Check Before You Click",
        "ko_summary": "피싱은 완벽한 보안 지식보다 멈춤, 발신자 확인, 별도 경로 접속이라는 짧은 루틴이 있을 때 피해 확률이 크게 줄어든다.",
        "en_summary": "Phishing risk drops when users have a short routine: pause, verify the sender, and open the service through a trusted route instead of the message link.",
        "ko_risk": "공격자는 배송, 세금, 카드 결제, 계정 정지처럼 급한 감정을 건드리는 문장을 먼저 보냅니다.",
        "en_risk": "Attackers start with urgency: delivery, tax, card payment, account suspension, or a limited-time warning.",
        "ko_actions": ["링크를 누르기 전 발신자 주소와 도메인을 분리해서 봅니다.", "공식 앱이나 즐겨찾기로 직접 접속합니다.", "첨부파일은 요청자와 별도 채널로 확인합니다."],
        "en_actions": ["Separate the sender name from the actual domain.", "Open the service through the official app or bookmark.", "Confirm attachments through a separate channel."],
        "ko_signals": ["급한 결제 요구", "낯선 단축 URL", "맞춤법이 어색한 기관명", "첨부파일 실행 요청"],
        "en_signals": ["urgent payment request", "unknown short link", "odd agency name", "attachment execution request"],
        "sources": ["ftc_phishing", "cisa_secure", "kisa_boho"],
        "tags": ["Phishing", "Email Security", "Scams", "Cyber Hygiene"],
    },
    {
        "slug": "smishing-parcel-scam",
        "ko_title": "택배 스미싱 대응법: 운송장 링크가 왔을 때 안전하게 확인하는 순서",
        "en_title": "Parcel Smishing Response: A Safe Order for Checking Delivery Links",
        "ko_summary": "택배 스미싱은 일상적인 기다림을 악용하므로 문자 속 링크가 아니라 택배사 공식 앱, 주문 내역, 고객센터 경로로 확인해야 한다.",
        "en_summary": "Parcel smishing abuses everyday delivery anxiety, so delivery status should be checked through official apps, order history, or customer support routes.",
        "ko_risk": "가짜 배송 조회 페이지는 휴대폰 번호, 인증번호, 앱 설치 권한을 차례로 요구하며 계정 탈취로 이어질 수 있습니다.",
        "en_risk": "Fake tracking pages can ask for phone numbers, verification codes, or app permissions before moving toward account takeover.",
        "ko_actions": ["문자 링크 대신 쇼핑몰 주문 내역을 먼저 봅니다.", "APK 설치나 프로파일 설치 요청은 거절합니다.", "실수로 입력했다면 비밀번호와 결제수단을 즉시 점검합니다."],
        "en_actions": ["Check the store order history before using any text link.", "Reject APK or profile installation requests.", "If you entered data, review passwords and payment methods immediately."],
        "ko_signals": ["미수령 택배 압박", "주소 정정 수수료", "앱 설치 유도", "인증번호 재입력"],
        "en_signals": ["undelivered package pressure", "address correction fee", "app installation prompt", "verification code retry"],
        "sources": ["kisa_boho", "kisa_spam", "ftc_phishing"],
        "tags": ["Smishing", "Mobile Security", "Scams", "Korea"],
    },
    {
        "slug": "voice-phishing-family-code",
        "ko_title": "보이스피싱 가족 암호 만들기: 급한 전화에서 먼저 확인할 한 문장",
        "en_title": "Family Code Words for Voice Phishing: One Sentence to Verify Urgent Calls",
        "ko_summary": "가족 사칭 전화는 감정적으로 빠르게 몰아붙이므로 가족끼리 미리 정한 확인 질문과 송금 보류 규칙이 필요하다.",
        "en_summary": "Impersonation calls move fast emotionally, so families need a pre-agreed verification question and a no-transfer pause rule.",
        "ko_risk": "AI 음성, 메신저 탈취, 전화번호 조작이 결합되면 목소리만으로는 가족 여부를 판단하기 어렵습니다.",
        "en_risk": "AI voice, stolen messengers, and caller-ID manipulation can make voice-only verification unreliable.",
        "ko_actions": ["가족끼리만 아는 짧은 암호 질문을 정합니다.", "송금 전 10분 보류와 재통화 규칙을 둡니다.", "경찰·금감원·기관은 계좌 이체를 요구하지 않는다는 원칙을 공유합니다."],
        "en_actions": ["Set a short family-only verification question.", "Use a 10-minute hold and callback rule before any transfer.", "Share the rule that agencies do not demand urgent transfers."],
        "ko_signals": ["급한 사고 주장", "통화 끊지 말라는 압박", "현금·상품권 요구", "비밀 유지 요구"],
        "en_signals": ["urgent accident claim", "pressure not to hang up", "cash or gift-card demand", "secrecy demand"],
        "sources": ["ftc_phishing", "kisa_boho", "cisa_secure"],
        "tags": ["Voice Phishing", "Family Safety", "Scams", "Verification"],
    },
    {
        "slug": "password-manager-first-setup",
        "ko_title": "비밀번호 관리자 처음 설정하기: 실패하지 않는 도입 순서",
        "en_title": "Password Manager First Setup: A Practical Adoption Order That Sticks",
        "ko_summary": "비밀번호 관리자는 모든 계정을 한 번에 바꾸는 도구가 아니라 중요한 계정부터 긴 고유 비밀번호로 전환하는 운영 방식이다.",
        "en_summary": "A password manager is not a one-day reset project; it is an operating habit for moving critical accounts to long, unique passwords first.",
        "ko_risk": "같은 비밀번호를 여러 곳에 쓰면 한 사이트 유출이 이메일, 쇼핑, 금융, 클라우드 계정으로 번집니다.",
        "en_risk": "Password reuse turns one site breach into a risk for email, shopping, finance, and cloud accounts.",
        "ko_actions": ["이메일과 금융 계정부터 등록합니다.", "마스터 비밀번호는 긴 문장형으로 만듭니다.", "복구코드와 긴급 접근 방법을 종이에 보관합니다."],
        "en_actions": ["Start with email and financial accounts.", "Use a long phrase as the master password.", "Store recovery codes and emergency access steps offline."],
        "ko_signals": ["중복 비밀번호", "브라우저 자동저장만 의존", "복구코드 미보관", "가족 공유 계정"],
        "en_signals": ["reused passwords", "browser-only storage", "missing recovery codes", "shared family accounts"],
        "sources": ["cisa_secure", "nist_auth", "ftc_2fa"],
        "tags": ["Passwords", "Password Manager", "Account Security", "MFA"],
    },
    {
        "slug": "passkeys-vs-passwords",
        "ko_title": "패스키와 비밀번호 차이: 피싱에 강한 로그인으로 바꾸는 법",
        "en_title": "Passkeys vs Passwords: Moving Toward Phishing-Resistant Sign-In",
        "ko_summary": "패스키는 사용자가 비밀번호를 기억하지 않고도 기기 기반 인증으로 로그인하는 방식이며, 피싱 사이트에 비밀번호를 입력하는 위험을 줄인다.",
        "en_summary": "Passkeys let users sign in with device-based authentication instead of memorized passwords, reducing the risk of typing secrets into phishing sites.",
        "ko_risk": "비밀번호와 SMS 인증은 가짜 로그인 페이지, SIM 탈취, 중간자 공격에 약해질 수 있습니다.",
        "en_risk": "Passwords and SMS codes can be exposed through fake login pages, SIM attacks, or adversary-in-the-middle flows.",
        "ko_actions": ["이메일, 클라우드, 개발자 계정부터 패스키를 켭니다.", "여분 기기나 보안키를 복구 수단으로 둡니다.", "패스키 지원 여부를 계정 보안 메뉴에서 확인합니다."],
        "en_actions": ["Enable passkeys first on email, cloud, and developer accounts.", "Keep a spare device or security key as recovery.", "Check passkey support in account security settings."],
        "ko_signals": ["패스키 지원", "보안키 등록", "복구기기 부족", "SMS만 사용하는 2FA"],
        "en_signals": ["passkey support", "security key registration", "limited recovery devices", "SMS-only 2FA"],
        "sources": ["nist_auth", "cisa_secure", "ftc_2fa"],
        "tags": ["Passkeys", "Authentication", "MFA", "Phishing"],
    },
    {
        "slug": "mfa-authenticator-vs-sms",
        "ko_title": "인증앱과 SMS 2단계 인증 비교: 어떤 계정부터 바꿀까",
        "en_title": "Authenticator Apps vs SMS MFA: Which Accounts to Upgrade First",
        "ko_summary": "2단계 인증은 켜는 것만큼 방식 선택이 중요하다. 중요한 계정은 SMS보다 인증앱, 패스키, 보안키처럼 피싱 저항성이 높은 방식으로 옮겨야 한다.",
        "en_summary": "Turning on MFA matters, but method choice matters too. Critical accounts should move from SMS toward authenticator apps, passkeys, or security keys.",
        "ko_risk": "SMS 코드는 번호 이동 사기, 악성앱, 피싱 페이지에서 노출될 수 있습니다.",
        "en_risk": "SMS codes can be exposed through SIM swap fraud, malware, or phishing pages.",
        "ko_actions": ["이메일과 금융 계정부터 인증앱으로 바꿉니다.", "복구코드를 저장하고 예비 인증수단을 등록합니다.", "푸시 승인 알림은 요청 위치와 시간을 확인합니다."],
        "en_actions": ["Upgrade email and financial accounts first.", "Save recovery codes and register a backup factor.", "Check request location and time before approving push prompts."],
        "ko_signals": ["SIM 스와핑", "푸시 폭탄", "복구코드 부재", "기기 분실"],
        "en_signals": ["SIM swap", "push bombing", "missing recovery codes", "lost device"],
        "sources": ["ftc_2fa", "nist_auth", "cisa_secure"],
        "tags": ["MFA", "Authentication", "SMS", "Account Security"],
    },
    {
        "slug": "account-recovery-lockout-plan",
        "ko_title": "계정 복구 계획: 휴대폰을 잃어버려도 잠기지 않는 구조 만들기",
        "en_title": "Account Recovery Plan: Avoiding Lockout After Losing a Phone",
        "ko_summary": "강한 인증은 복구 계획과 함께 설계해야 한다. 휴대폰 분실, 번호 변경, 해외 체류 같은 상황을 미리 가정해야 잠금을 피할 수 있다.",
        "en_summary": "Strong authentication needs recovery design. Plan for lost phones, number changes, and travel before they become account lockout events.",
        "ko_risk": "2FA 기기 하나에만 의존하면 보안은 강해져도 실제 복구 가능성이 낮아집니다.",
        "en_risk": "Relying on one MFA device can strengthen security while lowering real recoverability.",
        "ko_actions": ["복구코드를 오프라인으로 보관합니다.", "예비 이메일과 예비 인증수단을 등록합니다.", "분기마다 계정 복구 경로를 테스트합니다."],
        "en_actions": ["Store recovery codes offline.", "Register backup email and backup factors.", "Test account recovery paths once a quarter."],
        "ko_signals": ["단일 인증기기", "오래된 전화번호", "복구 이메일 미확인", "해외 로그인 제한"],
        "en_signals": ["single auth device", "old phone number", "unverified recovery email", "travel login limits"],
        "sources": ["nist_auth", "ftc_2fa", "cisa_secure"],
        "tags": ["Account Recovery", "MFA", "Passwords", "Resilience"],
    },
    {
        "slug": "email-account-security-baseline",
        "ko_title": "이메일 계정 보안 기준선: 모든 계정의 열쇠를 먼저 지키기",
        "en_title": "Email Account Security Baseline: Protecting the Key to Every Account",
        "ko_summary": "이메일은 비밀번호 재설정과 알림을 받는 중심 계정이므로 다른 계정보다 먼저 긴 비밀번호, MFA, 복구 경로 점검이 필요하다.",
        "en_summary": "Email receives resets and alerts, so it needs long unique passwords, MFA, and recovery checks before most other accounts.",
        "ko_risk": "이메일이 탈취되면 공격자는 다른 서비스의 비밀번호를 재설정하고 알림 메일을 숨길 수 있습니다.",
        "en_risk": "Once email is compromised, attackers can reset other services and hide warning messages.",
        "ko_actions": ["이메일에는 가장 강한 인증수단을 씁니다.", "자동 전달 규칙과 로그인 기록을 확인합니다.", "복구 이메일과 휴대폰 번호를 최신 상태로 둡니다."],
        "en_actions": ["Use the strongest factor on email.", "Review forwarding rules and login history.", "Keep recovery email and phone number current."],
        "ko_signals": ["자동 전달 규칙", "낯선 로그인", "비밀번호 재설정 메일", "복구수단 변경"],
        "en_signals": ["forwarding rules", "unknown login", "password reset email", "recovery method change"],
        "sources": ["cisa_secure", "nist_auth", "ftc_phishing"],
        "tags": ["Email Security", "Account Security", "MFA", "Phishing"],
    },
    {
        "slug": "smartphone-security-checklist",
        "ko_title": "스마트폰 보안 체크리스트: 앱 권한과 잠금화면부터 점검하기",
        "en_title": "Smartphone Security Checklist: Start With App Permissions and Lock Screen",
        "ko_summary": "스마트폰은 인증기기, 결제수단, 사진 저장소, 업무 알림창이므로 앱 권한과 잠금화면이 곧 계정 보안의 출발점이다.",
        "en_summary": "A phone is an authenticator, wallet, photo archive, and work notification center, so permissions and lock screen settings are account security basics.",
        "ko_risk": "악성앱이나 과도한 권한은 문자, 알림, 연락처, 파일 접근을 통해 피싱과 계정 탈취를 쉽게 만듭니다.",
        "en_risk": "Malicious or over-permissioned apps can expose texts, notifications, contacts, and files.",
        "ko_actions": ["앱 권한에서 문자, 알림, 접근성 권한을 먼저 봅니다.", "화면 잠금과 원격 찾기 기능을 켭니다.", "공식 앱마켓 외 설치를 막습니다."],
        "en_actions": ["Review SMS, notification, and accessibility permissions first.", "Enable screen lock and find-my-device features.", "Block installation outside official app stores."],
        "ko_signals": ["접근성 권한", "알림 읽기 권한", "출처 불명 앱", "잠금화면 미설정"],
        "en_signals": ["accessibility permission", "notification access", "unknown-source app", "no lock screen"],
        "sources": ["cisa_secure", "kisa_boho", "ftc_phishing"],
        "tags": ["Mobile Security", "App Permissions", "Privacy", "Cyber Hygiene"],
    },
    {
        "slug": "public-wifi-vpn-real-risk",
        "ko_title": "공용 와이파이와 VPN: 실제로 위험한 순간과 안전한 사용법",
        "en_title": "Public Wi-Fi and VPNs: The Real Risk Moments and Safer Use",
        "ko_summary": "공용 와이파이는 무조건 금지보다 네트워크 이름 확인, HTTPS, 자동연결 해제, 민감 작업 회피가 현실적인 방어선이다.",
        "en_summary": "Public Wi-Fi is best handled with network-name verification, HTTPS, disabled auto-join, and avoiding sensitive tasks rather than vague fear.",
        "ko_risk": "가짜 와이파이, 캡티브 포털 피싱, 암호화되지 않은 접속, 자동 연결이 주요 위험입니다.",
        "en_risk": "Fake hotspots, captive-portal phishing, unencrypted connections, and auto-join are the main risks.",
        "ko_actions": ["매장 직원에게 정확한 네트워크 이름을 확인합니다.", "자동연결을 끄고 금융 작업은 모바일 데이터로 처리합니다.", "VPN은 신뢰할 수 있는 제공자와 업무 정책에 맞춰 씁니다."],
        "en_actions": ["Confirm the exact network name with staff.", "Disable auto-join and use mobile data for banking.", "Use VPNs from trusted providers and according to work policy."],
        "ko_signals": ["비슷한 SSID", "로그인 포털 결제 요구", "HTTPS 경고", "자동 연결"],
        "en_signals": ["lookalike SSID", "portal payment request", "HTTPS warning", "auto-join"],
        "sources": ["cisa_secure", "ftc_phishing", "cisa_small"],
        "tags": ["Wi-Fi", "VPN", "Mobile Security", "Privacy"],
    },
    {
        "slug": "browser-extension-security",
        "ko_title": "브라우저 확장 프로그램 보안: 편리함이 계정 탈취로 바뀌는 지점",
        "en_title": "Browser Extension Security: Where Convenience Turns Into Account Risk",
        "ko_summary": "브라우저 확장 프로그램은 웹페이지와 로그인 상태에 접근할 수 있으므로 설치 수보다 권한, 개발자 신뢰, 업데이트 이력을 봐야 한다.",
        "en_summary": "Browser extensions can access pages and sessions, so permissions, developer trust, and update history matter more than install count alone.",
        "ko_risk": "확장 프로그램이 모든 사이트 읽기 권한을 가지면 입력값, 쿠키, 업무 페이지 내용이 노출될 수 있습니다.",
        "en_risk": "Extensions with broad site access can expose inputs, cookies, and work-page content.",
        "ko_actions": ["사용하지 않는 확장 프로그램을 삭제합니다.", "권한이 넓은 확장은 업무 브라우저에서 분리합니다.", "개발자 변경과 최근 리뷰를 확인합니다."],
        "en_actions": ["Remove extensions you no longer use.", "Separate broad-permission extensions from work browsers.", "Review developer changes and recent reviews."],
        "ko_signals": ["모든 사이트 접근", "개발자 변경", "리뷰 급변", "업무 계정 브라우저 공유"],
        "en_signals": ["all-sites permission", "developer change", "review swing", "shared work browser"],
        "sources": ["cisa_secure", "nist_auth", "cisa_small"],
        "tags": ["Browser Security", "Extensions", "Privacy", "Account Security"],
    },
    {
        "slug": "software-update-routine",
        "ko_title": "보안 업데이트 루틴: 미루지 않아도 되는 현실적인 패치 습관",
        "en_title": "Software Update Routine: A Realistic Patch Habit You Can Keep",
        "ko_summary": "업데이트는 귀찮은 팝업이 아니라 이미 알려진 취약점을 닫는 가장 비용 효율적인 보안 행동이다.",
        "en_summary": "Updates are not just annoying prompts; they are one of the lowest-cost ways to close known vulnerabilities.",
        "ko_risk": "오래된 브라우저, OS, 라우터, NAS, 플러그인은 자동화된 공격의 쉬운 표적이 됩니다.",
        "en_risk": "Old browsers, operating systems, routers, NAS devices, and plugins become easy targets for automated attacks.",
        "ko_actions": ["OS와 브라우저 자동 업데이트를 켭니다.", "월 1회 라우터와 NAS 펌웨어를 확인합니다.", "업무용 앱은 호환성 테스트 후 정해진 날짜에 적용합니다."],
        "en_actions": ["Enable OS and browser auto-updates.", "Check router and NAS firmware monthly.", "Patch work apps on a scheduled date after compatibility checks."],
        "ko_signals": ["재부팅 미루기", "지원 종료 OS", "펌웨어 방치", "취약 플러그인"],
        "en_signals": ["delayed reboot", "end-of-support OS", "ignored firmware", "vulnerable plugin"],
        "sources": ["cisa_secure", "cisa_hygiene", "cisa_small"],
        "tags": ["Patching", "Updates", "Cyber Hygiene", "Vulnerabilities"],
    },
    {
        "slug": "backup-3-2-1-ransomware",
        "ko_title": "랜섬웨어 대비 3-2-1 백업: 복구 가능한 백업인지 확인하는 법",
        "en_title": "3-2-1 Backup for Ransomware: How to Know Whether You Can Really Recover",
        "ko_summary": "백업은 파일을 복사했다는 사실보다 랜섬웨어 이후 실제로 복구할 수 있는지, 오프라인·불변 백업이 있는지가 핵심이다.",
        "en_summary": "Backup quality is about recoverability after ransomware, not just copied files. Offline or immutable copies matter.",
        "ko_risk": "항상 연결된 백업 드라이브와 동기화 클라우드는 감염된 파일까지 함께 덮어쓸 수 있습니다.",
        "en_risk": "Always-connected drives and sync-only cloud folders can overwrite good files with encrypted or deleted versions.",
        "ko_actions": ["중요 파일은 3개 사본, 2개 매체, 1개 오프라인 원칙으로 둡니다.", "복구 테스트를 분기마다 진행합니다.", "백업 계정에는 강한 MFA를 적용합니다."],
        "en_actions": ["Keep three copies, two media types, and one offline copy.", "Run recovery tests quarterly.", "Protect backup accounts with strong MFA."],
        "ko_signals": ["동기화만 있는 백업", "복구 테스트 없음", "백업 계정 MFA 없음", "오래된 외장하드"],
        "en_signals": ["sync-only backup", "no restore test", "no MFA on backup account", "old external drive"],
        "sources": ["cisa_ransom", "cisa_secure", "kisa_boho"],
        "tags": ["Backup", "Ransomware", "Resilience", "Data Protection"],
    },
    {
        "slug": "ransomware-first-hour",
        "ko_title": "랜섬웨어 의심 첫 1시간: 전원, 네트워크, 신고 순서",
        "en_title": "The First Hour of Suspected Ransomware: Power, Network, and Reporting Order",
        "ko_summary": "랜섬웨어가 의심될 때는 당황해서 파일을 지우기보다 네트워크 분리, 증거 보존, 내부 연락, 신고 채널 확인 순서가 중요하다.",
        "en_summary": "When ransomware is suspected, the first priority is network isolation, evidence preservation, internal escalation, and reporting paths, not random cleanup.",
        "ko_risk": "무작정 재부팅하거나 복구툴을 실행하면 로그와 증거가 사라지고 피해 범위를 파악하기 어려워질 수 있습니다.",
        "en_risk": "Random rebooting or cleanup tools can erase logs and make scope assessment harder.",
        "ko_actions": ["감염 의심 장비를 네트워크에서 분리합니다.", "화면, 파일명, 시간, 계정 정보를 기록합니다.", "조직 담당자와 공식 신고 채널에 즉시 공유합니다."],
        "en_actions": ["Disconnect suspected devices from the network.", "Record screenshots, filenames, time, and accounts.", "Escalate internally and use official reporting channels."],
        "ko_signals": ["확장자 일괄 변경", "랜섬노트", "공유폴더 암호화", "관리자 계정 이상 로그인"],
        "en_signals": ["mass extension change", "ransom note", "encrypted shared folders", "admin account anomaly"],
        "sources": ["cisa_ransom", "kisa_boho", "cisa_small"],
        "tags": ["Ransomware", "Incident Response", "Small Business", "Backup"],
    },
    {
        "slug": "identity-theft-response",
        "ko_title": "개인정보 도용 대응 순서: 유출을 알게 된 날 해야 할 일",
        "en_title": "Identity Theft Response Order: What to Do the Day You Learn About Exposure",
        "ko_summary": "개인정보 도용은 한 번의 신고로 끝나지 않는다. 계정 잠금, 비밀번호 변경, 결제수단 점검, 공식 신고 기록을 동시에 남겨야 한다.",
        "en_summary": "Identity theft response is not one report. It requires account locks, password changes, payment review, and official records at the same time.",
        "ko_risk": "이름, 휴대폰, 생년월일, 이메일 조합은 통신, 쇼핑, 금융, 중고거래 인증에 반복 사용될 수 있습니다.",
        "en_risk": "Names, phone numbers, birth dates, and email addresses can be reused across telecom, shopping, finance, and marketplace verification.",
        "ko_actions": ["이메일과 금융 계정 비밀번호를 먼저 바꿉니다.", "카드사와 통신사 알림을 점검합니다.", "공식 개인정보 침해 신고 경로에 기록을 남깁니다."],
        "en_actions": ["Change email and financial account passwords first.", "Review card and mobile-carrier alerts.", "File a record through official identity-theft or privacy channels."],
        "ko_signals": ["모르는 본인인증", "낯선 배송지", "카드 소액결제", "통신사 변경 알림"],
        "en_signals": ["unknown verification", "new shipping address", "small card charge", "mobile-carrier change alert"],
        "sources": ["ftc_identity", "kisa_privacy", "cisa_secure"],
        "tags": ["Identity Theft", "Privacy", "Incident Response", "Accounts"],
    },
    {
        "slug": "data-breach-password-rotation",
        "ko_title": "개인정보 유출 후 비밀번호 변경 순서: 모든 계정을 한 번에 바꾸지 말 것",
        "en_title": "Password Rotation After a Breach: Do Not Change Every Account at Random",
        "ko_summary": "유출 소식을 들으면 모든 계정을 무작정 바꾸기보다 이메일, 금융, 같은 비밀번호를 쓴 계정부터 우선순위를 정해야 한다.",
        "en_summary": "After a breach notice, prioritize email, financial accounts, and reused-password accounts instead of randomly changing everything.",
        "ko_risk": "중복 비밀번호를 오래 방치하면 공격자가 자동 대입으로 다른 서비스까지 침투할 수 있습니다.",
        "en_risk": "Leaving reused passwords in place enables credential-stuffing attacks across other services.",
        "ko_actions": ["유출된 서비스와 같은 비밀번호를 쓴 계정을 찾습니다.", "이메일 계정을 먼저 보호합니다.", "비밀번호 관리자에 고유 비밀번호로 재등록합니다."],
        "en_actions": ["Find accounts that shared the breached password.", "Secure email first.", "Move accounts into a password manager with unique passwords."],
        "ko_signals": ["유출 공지", "로그인 실패 알림", "비밀번호 재사용", "낯선 기기 등록"],
        "en_signals": ["breach notice", "failed login alert", "password reuse", "unknown device registration"],
        "sources": ["cisa_secure", "ftc_identity", "nist_auth"],
        "tags": ["Data Breach", "Passwords", "Credential Stuffing", "Privacy"],
    },
    {
        "slug": "privacy-settings-social-media",
        "ko_title": "SNS 개인정보 설정: 공개 범위를 줄이면 사기도 줄어든다",
        "en_title": "Social Media Privacy Settings: Less Exposure Means Fewer Scam Angles",
        "ko_summary": "SNS 공개 정보는 단순한 사생활 문제가 아니라 가족 사칭, 생일 기반 인증 추측, 위치 추적, 맞춤형 피싱의 재료가 된다.",
        "en_summary": "Public social media details are not just privacy trivia; they fuel impersonation, birthday-based guessing, location tracking, and tailored phishing.",
        "ko_risk": "공개 생일, 학교, 직장, 가족관계, 여행 일정은 공격자에게 신뢰감 있는 시나리오를 제공합니다.",
        "en_risk": "Public birthdays, schools, employers, family ties, and travel schedules help attackers write believable scenarios.",
        "ko_actions": ["생일, 연락처, 친구목록 공개 범위를 줄입니다.", "과거 게시물 공개 범위를 일괄 점검합니다.", "위치 태그는 실시간보다 사후 공유로 바꿉니다."],
        "en_actions": ["Reduce visibility for birthday, contact details, and friend lists.", "Review old-post visibility in bulk.", "Share location after the fact, not live."],
        "ko_signals": ["공개 친구목록", "실시간 위치", "가족관계 노출", "전화번호 공개"],
        "en_signals": ["public friend list", "live location", "family relationship exposure", "public phone number"],
        "sources": ["cisa_secure", "ftc_phishing", "kisa_privacy"],
        "tags": ["Privacy", "Social Media", "Scams", "Family Safety"],
    },
    {
        "slug": "shopping-scam-red-flags",
        "ko_title": "온라인 쇼핑 사기 신호: 최저가보다 먼저 볼 7가지",
        "en_title": "Online Shopping Scam Red Flags: Seven Checks Before the Lowest Price",
        "ko_summary": "온라인 쇼핑 사기는 가격보다 결제 방식, 사업자 정보, 환불 정책, 후기 패턴, 도메인 이력이 먼저 말해준다.",
        "en_summary": "Shopping scams show up in payment method, seller identity, refund policy, review patterns, and domain behavior before price alone tells the story.",
        "ko_risk": "과도한 할인, 계좌이체 유도, 연락처 부재, 복사된 상품 설명은 결제 후 잠적 가능성을 높입니다.",
        "en_risk": "Extreme discounts, bank-transfer pressure, missing contacts, and copied product descriptions raise the chance of non-delivery.",
        "ko_actions": ["카드 결제와 안전결제 여부를 확인합니다.", "사업자 정보와 고객센터 경로를 검색합니다.", "후기는 날짜와 문장 반복을 봅니다."],
        "en_actions": ["Check card or protected payment options.", "Search seller identity and support channels.", "Review dates and repeated wording in reviews."],
        "ko_signals": ["비정상 최저가", "계좌이체만 가능", "환불정책 부재", "후기 문장 반복"],
        "en_signals": ["unrealistic low price", "bank transfer only", "missing refund policy", "repeated review wording"],
        "sources": ["ftc_phishing", "cisa_secure", "kisa_boho"],
        "tags": ["Shopping Scams", "Payments", "Consumer Security", "Fraud"],
    },
    {
        "slug": "marketplace-secondhand-scam",
        "ko_title": "중고거래 사기 예방: 안전결제와 직거래보다 중요한 기록 남기기",
        "en_title": "Secondhand Marketplace Scam Prevention: Records Matter More Than Speed",
        "ko_summary": "중고거래에서는 빠른 거래보다 대화 기록, 결제 경로, 판매자 평판, 물품 확인 절차를 남기는 것이 사후 대응력을 높인다.",
        "en_summary": "In secondhand marketplaces, keeping chat records, payment trails, seller reputation, and item-verification steps improves your response options.",
        "ko_risk": "거래 외부 메신저 이동, 선입금 압박, 배송 인증 사진 재사용은 흔한 위험 신호입니다.",
        "en_risk": "Moving off-platform, upfront-payment pressure, and reused shipping proof are common warning signs.",
        "ko_actions": ["플랫폼 안에서 대화와 결제를 유지합니다.", "물품 사진에는 날짜와 요청 문구를 넣게 합니다.", "직거래는 공개 장소와 동행 원칙을 둡니다."],
        "en_actions": ["Keep chat and payment inside the platform.", "Ask for a dated photo with a requested phrase.", "Use public places and a companion for in-person trades."],
        "ko_signals": ["외부 메신저 유도", "시세보다 낮은 가격", "선입금 압박", "사진 재사용"],
        "en_signals": ["off-platform messaging", "below-market price", "upfront pressure", "reused photo"],
        "sources": ["ftc_phishing", "kisa_boho", "cisa_secure"],
        "tags": ["Marketplace", "Fraud", "Consumer Security", "Payments"],
    },
    {
        "slug": "qr-code-quishing",
        "ko_title": "QR코드 피싱 대응: 스캔하기 전 주소와 맥락 확인하기",
        "en_title": "QR Code Phishing: Check the Destination and Context Before Scanning",
        "ko_summary": "QR코드는 편리하지만 사용자가 주소를 보지 않고 스캔하기 쉬워 가짜 결제, 가짜 주차요금, 가짜 로그인 페이지로 이어질 수 있다.",
        "en_summary": "QR codes are convenient, but they make it easy to skip URL checking, leading to fake payments, fake parking fees, or fake login pages.",
        "ko_risk": "스티커로 덧붙인 QR코드나 낯선 안내문은 정상 서비스처럼 보이는 피싱 페이지로 연결될 수 있습니다.",
        "en_risk": "Stickered QR codes or unfamiliar notices can point to phishing pages that look like normal services.",
        "ko_actions": ["스캔 후 열기 전 도메인을 확인합니다.", "결제는 공식 앱에서 직접 진행합니다.", "공공장소 QR코드는 훼손·덧붙임 흔적을 봅니다."],
        "en_actions": ["Check the domain before opening after scanning.", "Pay through the official app directly.", "Look for tampering or stickers on public QR codes."],
        "ko_signals": ["덧붙인 스티커", "단축 URL", "즉시 결제 요구", "로그인 재입력"],
        "en_signals": ["sticker overlay", "short URL", "instant payment demand", "login re-entry"],
        "sources": ["ftc_phishing", "cisa_secure", "kisa_boho"],
        "tags": ["QR Code", "Phishing", "Payments", "Mobile Security"],
    },
    {
        "slug": "cloud-drive-sharing-risk",
        "ko_title": "클라우드 드라이브 공유 보안: 링크 하나가 전체 폴더가 되지 않게 하기",
        "en_title": "Cloud Drive Sharing Security: Keep One Link From Becoming the Whole Folder",
        "ko_summary": "클라우드 공유는 편리하지만 링크 공개 범위, 편집 권한, 만료일, 외부 공유 알림을 관리하지 않으면 자료 유출로 이어진다.",
        "en_summary": "Cloud sharing is useful, but unmanaged link visibility, edit rights, expiry dates, and external sharing alerts can create data exposure.",
        "ko_risk": "전체 폴더 공개 링크, 편집 권한, 개인 계정 공유는 회사 자료와 개인정보를 동시에 노출할 수 있습니다.",
        "en_risk": "Public folder links, edit permissions, and personal-account sharing can expose company data and personal information together.",
        "ko_actions": ["공유 링크는 특정 사용자로 제한합니다.", "편집 권한은 필요한 사람에게만 줍니다.", "프로젝트 종료 후 외부 공유 링크를 회수합니다."],
        "en_actions": ["Restrict links to named users.", "Give edit rights only when needed.", "Revoke external links after the project ends."],
        "ko_signals": ["전체공개 링크", "편집 권한", "만료일 없음", "개인 계정 공유"],
        "en_signals": ["public link", "edit rights", "no expiry", "personal account sharing"],
        "sources": ["cisa_small", "cisa_secure", "nist_auth"],
        "tags": ["Cloud Security", "Data Sharing", "Privacy", "Small Business"],
    },
    {
        "slug": "home-router-security",
        "ko_title": "가정용 공유기 보안: 와이파이 이름보다 관리자 페이지가 먼저다",
        "en_title": "Home Router Security: Admin Settings Matter More Than the Wi-Fi Name",
        "ko_summary": "가정용 공유기는 집 안 모든 기기의 관문이므로 관리자 비밀번호, 펌웨어, 원격관리, 게스트 네트워크를 우선 점검해야 한다.",
        "en_summary": "A home router is the gateway for every device, so admin passwords, firmware, remote management, and guest networks come first.",
        "ko_risk": "기본 관리자 비밀번호와 오래된 펌웨어는 자동화된 공격과 악성 DNS 변경의 표적이 됩니다.",
        "en_risk": "Default admin passwords and outdated firmware are targets for automated attacks and malicious DNS changes.",
        "ko_actions": ["관리자 비밀번호를 기본값에서 바꿉니다.", "펌웨어 업데이트와 자동 업데이트를 확인합니다.", "손님과 IoT 기기는 게스트 네트워크로 분리합니다."],
        "en_actions": ["Change the default admin password.", "Check firmware and auto-update settings.", "Put guests and IoT devices on a guest network."],
        "ko_signals": ["기본 관리자 계정", "원격관리 켜짐", "오래된 펌웨어", "모든 기기 같은 네트워크"],
        "en_signals": ["default admin account", "remote management enabled", "old firmware", "all devices on one network"],
        "sources": ["cisa_secure", "cisa_hygiene", "kisa_boho"],
        "tags": ["Router Security", "Wi-Fi", "Home Network", "IoT"],
    },
    {
        "slug": "smart-home-iot-security",
        "ko_title": "스마트홈 IoT 보안: 카메라와 가전을 별도 네트워크에 두는 이유",
        "en_title": "Smart Home IoT Security: Why Cameras and Appliances Need Separation",
        "ko_summary": "IoT 기기는 편리하지만 업데이트 수명, 기본 비밀번호, 클라우드 계정 보안이 약하면 집 안 네트워크의 약한 고리가 된다.",
        "en_summary": "IoT devices are convenient, but weak update lifecycles, default passwords, and cloud-account security can make them the weakest link at home.",
        "ko_risk": "카메라, 도어락, 스피커, 로봇청소기는 사생활과 물리적 공간에 연결되어 있어 계정 탈취 피해가 더 직접적입니다.",
        "en_risk": "Cameras, locks, speakers, and robot vacuums connect to private spaces, so account takeover has more direct consequences.",
        "ko_actions": ["구매 전 업데이트 지원 기간을 확인합니다.", "IoT는 게스트 네트워크에 둡니다.", "제조사 계정에는 MFA를 켭니다."],
        "en_actions": ["Check update-support life before buying.", "Place IoT on a guest network.", "Turn on MFA for vendor accounts."],
        "ko_signals": ["기본 비밀번호", "지원 종료 기기", "카메라 외부접속", "공유 계정"],
        "en_signals": ["default password", "unsupported device", "external camera access", "shared account"],
        "sources": ["cisa_secure", "cisa_hygiene", "ftc_2fa"],
        "tags": ["IoT", "Smart Home", "Privacy", "Home Network"],
    },
    {
        "slug": "child-online-safety-family-device",
        "ko_title": "아이 온라인 안전 설정: 차단보다 대화와 기기 규칙이 먼저다",
        "en_title": "Child Online Safety Settings: Rules and Conversation Before Blocking",
        "ko_summary": "아이 기기 보안은 차단앱 하나로 끝나지 않는다. 결제, 위치, 사진 공유, 낯선 대화, 계정 복구를 가족 규칙으로 정해야 한다.",
        "en_summary": "Children's device safety is not solved by one blocking app. Payments, location, photo sharing, stranger chats, and account recovery need family rules.",
        "ko_risk": "게임 채팅, 무료 아이템, 친구 요청, 위치 공유가 사기와 개인정보 노출의 입구가 될 수 있습니다.",
        "en_risk": "Game chats, free-item offers, friend requests, and location sharing can become entry points for scams and privacy exposure.",
        "ko_actions": ["앱 설치와 결제는 보호자 승인으로 둡니다.", "실명, 학교, 위치 공유 금지 규칙을 정합니다.", "문제 상황을 숨기지 않고 말할 수 있는 대응 문장을 정합니다."],
        "en_actions": ["Require guardian approval for installs and payments.", "Set rules against sharing real name, school, and location.", "Agree on a phrase children can use when something feels wrong."],
        "ko_signals": ["무료 아이템 미끼", "낯선 DM", "위치 공유", "부모 몰래 결제"],
        "en_signals": ["free item lure", "unknown DM", "location sharing", "hidden payment"],
        "sources": ["cisa_secure", "ftc_phishing", "kisa_privacy"],
        "tags": ["Child Safety", "Family Security", "Privacy", "Mobile Security"],
    },
    {
        "slug": "elderly-scam-prevention",
        "ko_title": "부모님 디지털 사기 예방: 대신 설정보다 함께 확인하는 루틴",
        "en_title": "Digital Scam Prevention for Older Adults: Build a Shared Check Routine",
        "ko_summary": "부모님 보안은 자녀가 대신 설정하는 것보다 낯선 전화, 문자, 앱 설치, 송금 요청을 함께 확인하는 약속이 더 오래간다.",
        "en_summary": "Security for older adults lasts longer when families build a shared check routine for calls, texts, app installs, and transfer requests.",
        "ko_risk": "기관 사칭, 가족 사칭, 원격제어 앱 설치, 상품권 결제 요구는 고령층을 반복적으로 노립니다.",
        "en_risk": "Agency impersonation, family impersonation, remote-control apps, and gift-card payment requests repeatedly target older adults.",
        "ko_actions": ["송금 전 가족에게 확인하는 규칙을 둡니다.", "원격제어 앱 설치는 금지 목록으로 정합니다.", "자주 쓰는 기관 앱만 홈 화면에 남깁니다."],
        "en_actions": ["Create a family confirmation rule before transfers.", "Put remote-control app installation on a do-not-install list.", "Keep only trusted agency apps on the home screen."],
        "ko_signals": ["검찰·경찰 사칭", "원격제어 앱", "상품권 요구", "통화 유지 압박"],
        "en_signals": ["agency impersonation", "remote-control app", "gift-card demand", "pressure to stay on call"],
        "sources": ["ftc_phishing", "kisa_boho", "cisa_secure"],
        "tags": ["Elder Safety", "Scams", "Family Security", "Mobile Security"],
    },
    {
        "slug": "small-business-cyber-baseline",
        "ko_title": "소상공인 보안 기준선: 돈을 많이 쓰기 전 먼저 할 10가지",
        "en_title": "Small Business Cyber Baseline: Ten Things to Do Before Buying More Tools",
        "ko_summary": "소상공인 보안은 비싼 솔루션보다 이메일 MFA, 백업, 업데이트, 결제 권한 분리, 직원 피싱 교육 같은 기본선이 먼저다.",
        "en_summary": "Small business security starts with email MFA, backups, updates, payment separation, and phishing training before expensive tools.",
        "ko_risk": "작은 매장은 계정 하나, 노트북 하나, 공유 비밀번호 하나가 결제·예약·고객정보 전체를 멈출 수 있습니다.",
        "en_risk": "One account, one laptop, or one shared password can stop payments, bookings, and customer records for a small operation.",
        "ko_actions": ["대표 이메일에 MFA를 켭니다.", "매출·고객 파일은 복구 가능한 백업을 둡니다.", "계좌이체 승인 권한을 두 사람 이상 확인하게 합니다."],
        "en_actions": ["Enable MFA on owner email.", "Keep recoverable backups for sales and customer files.", "Require two-person approval for payment changes."],
        "ko_signals": ["공유 비밀번호", "백업 없음", "대표자 단일 승인", "직원 퇴사 계정 방치"],
        "en_signals": ["shared password", "no backup", "single-owner approval", "stale former-employee account"],
        "sources": ["cisa_small", "ftc_smallbiz", "cisa_ransom"],
        "tags": ["Small Business", "Cyber Hygiene", "MFA", "Backup"],
    },
    {
        "slug": "employee-phishing-drill",
        "ko_title": "직원 피싱 훈련 설계: 속인 사람 찾기가 아니라 신고 루틴 만들기",
        "en_title": "Employee Phishing Drills: Build Reporting Habits, Not Blame",
        "ko_summary": "피싱 훈련의 목적은 누가 속았는지 공개하는 것이 아니라 의심 메일을 빠르게 신고하고 같은 피해를 줄이는 조직 루틴을 만드는 것이다.",
        "en_summary": "The goal of phishing drills is not public blame. It is a fast reporting habit that reduces repeat harm across the organization.",
        "ko_risk": "처벌 중심 훈련은 직원이 실수를 숨기게 만들고 실제 사고 대응 시간을 늦춥니다.",
        "en_risk": "Punitive drills make people hide mistakes and slow down real incident response.",
        "ko_actions": ["신고 버튼이나 메일 주소를 명확히 둡니다.", "훈련 후 정답보다 신호를 설명합니다.", "신고한 직원을 긍정적으로 피드백합니다."],
        "en_actions": ["Make the report button or mailbox obvious.", "Explain signals after drills, not only answers.", "Give positive feedback to reporters."],
        "ko_signals": ["신고 경로 불명확", "공개 망신", "훈련만 있고 교육 없음", "실제 신고 지연"],
        "en_signals": ["unclear reporting path", "public shaming", "drill without education", "delayed real reports"],
        "sources": ["cisa_small", "ftc_smallbiz", "ftc_phishing"],
        "tags": ["Phishing Training", "Workplace Security", "Small Business", "Incident Response"],
    },
    {
        "slug": "invoice-payment-fraud",
        "ko_title": "송금 계좌 변경 사기: 거래처 메일을 믿기 전 확인할 절차",
        "en_title": "Invoice Payment Fraud: Verify Vendor Bank Changes Before Trusting Email",
        "ko_summary": "거래처 계좌 변경 사기는 이메일 한 통으로 자금을 빼내므로 결제 전 별도 연락, 이중승인, 변경 이력 기록이 필요하다.",
        "en_summary": "Vendor bank-change fraud can move money with one email, so separate verification, dual approval, and change records are essential.",
        "ko_risk": "공격자는 실제 거래처 메일함을 탈취하거나 비슷한 도메인을 만들어 자연스러운 청구서를 보냅니다.",
        "en_risk": "Attackers may compromise a real vendor mailbox or use a lookalike domain to send believable invoices.",
        "ko_actions": ["계좌 변경은 기존 전화번호로 재확인합니다.", "새 계좌 첫 송금은 소액 테스트와 이중승인을 둡니다.", "도메인 철자와 회신주소를 확인합니다."],
        "en_actions": ["Verify bank changes through a known phone number.", "Use small test payments and dual approval for first transfers.", "Check domain spelling and reply-to addresses."],
        "ko_signals": ["갑작스러운 계좌 변경", "회신주소 불일치", "긴급 송금 압박", "문서 양식 미묘한 차이"],
        "en_signals": ["sudden bank change", "reply-to mismatch", "urgent transfer pressure", "subtle invoice difference"],
        "sources": ["ftc_smallbiz", "cisa_small", "ftc_phishing"],
        "tags": ["Business Email Compromise", "Payments", "Small Business", "Fraud"],
    },
    {
        "slug": "domain-email-spoofing-dmarc",
        "ko_title": "도메인 이메일 사칭 막기: SPF, DKIM, DMARC를 실무적으로 이해하기",
        "en_title": "Stopping Domain Email Spoofing: A Practical View of SPF, DKIM, and DMARC",
        "ko_summary": "SPF, DKIM, DMARC는 이메일을 완벽히 안전하게 만들지는 않지만 내 도메인을 사칭한 메일을 줄이고 탐지하는 기본 장치다.",
        "en_summary": "SPF, DKIM, and DMARC do not make email perfect, but they reduce and detect mail that spoofs your domain.",
        "ko_risk": "도메인 인증 설정이 없으면 공격자가 회사 도메인처럼 보이는 발신자로 청구서와 로그인 링크를 보낼 수 있습니다.",
        "en_risk": "Without domain authentication, attackers can send invoices and login links that appear to come from your company domain.",
        "ko_actions": ["DNS에 SPF와 DKIM을 먼저 설정합니다.", "DMARC는 모니터링 모드로 시작해 보고서를 봅니다.", "거절 정책은 정상 메일 흐름을 확인한 뒤 단계적으로 올립니다."],
        "en_actions": ["Set SPF and DKIM in DNS first.", "Start DMARC in monitoring mode and read reports.", "Move to stricter policies after confirming legitimate mail flow."],
        "ko_signals": ["도메인 사칭", "DMARC 없음", "마케팅 메일 누락", "보고서 미확인"],
        "en_signals": ["domain spoofing", "missing DMARC", "lost marketing mail", "unread reports"],
        "sources": ["cisa_small", "ftc_smallbiz", "cisa_hygiene"],
        "tags": ["Email Security", "DMARC", "Small Business", "DNS"],
    },
    {
        "slug": "security-checkup-monthly-routine",
        "ko_title": "월간 보안 점검 루틴: 30분으로 계정과 기기를 정리하는 법",
        "en_title": "Monthly Security Checkup: A 30-Minute Routine for Accounts and Devices",
        "ko_summary": "보안은 큰 결심보다 반복 가능한 월간 루틴이 강하다. 계정, 기기, 백업, 결제 알림을 30분 안에 점검하는 방식이면 충분하다.",
        "en_summary": "Security improves through repeatable monthly routines. A 30-minute review of accounts, devices, backups, and payment alerts is enough to reduce many risks.",
        "ko_risk": "작은 설정 방치가 누적되면 오래된 기기, 퇴사자 계정, 중복 비밀번호, 끊긴 백업이 한 번에 문제를 만듭니다.",
        "en_risk": "Neglected settings accumulate into old devices, stale accounts, reused passwords, and broken backups.",
        "ko_actions": ["로그인 기록과 연결 기기를 봅니다.", "자동 업데이트와 백업 성공 여부를 확인합니다.", "카드·계좌 알림과 구독 내역을 정리합니다."],
        "en_actions": ["Review login history and connected devices.", "Check auto-updates and backup success.", "Review card alerts and subscriptions."],
        "ko_signals": ["낯선 기기", "실패한 백업", "업데이트 대기", "모르는 구독"],
        "en_signals": ["unknown device", "failed backup", "pending update", "unknown subscription"],
        "sources": ["cisa_secure", "cisa_hygiene", "ftc_identity"],
        "tags": ["Security Checklist", "Cyber Hygiene", "Accounts", "Backup"],
    },
]


def escape_svg_text(value: str) -> str:
    return html.escape(value, quote=True)


def write_svg(path: Path, title: str, subtitle: str, labels: list[str], palette: tuple[str, str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    label_lines = "\n".join(
        f'<text x="90" y="{334 + index * 40}" fill="#ecfeff" font-size="23" font-family="Verdana, sans-serif">{escape_svg_text(label)}</text>'
        for index, label in enumerate(labels[:5])
    )
    nodes = "\n".join(
        f'<circle cx="{755 + index * 82}" cy="{190 + (index % 2) * 84}" r="34" fill="#22d3ee" fill-opacity="{0.20 + index * 0.04:.2f}" stroke="#ecfeff" stroke-opacity="0.45"/>'
        for index in range(5)
    )
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="675" viewBox="0 0 1200 675" role="img" aria-labelledby="title desc">
  <title id="title">{escape_svg_text(title)}</title>
  <desc id="desc">{escape_svg_text(subtitle)}</desc>
  <defs>
    <linearGradient id="bg" x1="0" x2="1" y1="0" y2="1">
      <stop offset="0%" stop-color="{palette[0]}"/>
      <stop offset="100%" stop-color="{palette[1]}"/>
    </linearGradient>
    <pattern id="mesh" width="52" height="52" patternUnits="userSpaceOnUse">
      <path d="M0 26 H52 M26 0 V52" stroke="#ffffff" stroke-opacity="0.08" stroke-width="1"/>
    </pattern>
  </defs>
  <rect width="1200" height="675" fill="url(#bg)"/>
  <rect width="1200" height="675" fill="url(#mesh)"/>
  <path d="M120 500 L260 380 L408 438 L560 285 L724 330 L880 205 L1050 248" fill="none" stroke="#a7f3d0" stroke-width="9" stroke-linecap="round" stroke-linejoin="round" opacity="0.9"/>
  <rect x="68" y="278" width="548" height="258" rx="28" fill="#020617" fill-opacity="0.48" stroke="#ffffff" stroke-opacity="0.18"/>
  {nodes}
  <text x="72" y="108" fill="#f8fafc" font-size="46" font-family="Verdana, sans-serif" font-weight="700">{escape_svg_text(title)}</text>
  <text x="76" y="160" fill="#cffafe" font-size="25" font-family="Verdana, sans-serif">{escape_svg_text(subtitle)}</text>
  {label_lines}
  <text x="76" y="610" fill="#d1fae5" font-size="22" font-family="Verdana, sans-serif">MouseBall54 Digital Security Playbook</text>
</svg>
"""
    path.write_text(svg, encoding="utf-8")


def yaml_list(items: list[str]) -> str:
    return "\n".join(f"  - {item}" for item in items)


def normalize_markdown(text: str) -> str:
    normalized = "\n".join(line[4:] if line.startswith("    ") else line for line in text.splitlines()).lstrip()
    return normalized.replace("sidebar:\nnav:", "sidebar:\n    nav:") + "\n"


def source_notes(source_keys: list[str], lang: str) -> str:
    lines = []
    for key in source_keys:
        source = SOURCES[key]
        lines.append(f"- [{source[lang]}]({source['url']})")
    return "\n".join(lines)


def related_links(index: int, lang: str) -> str:
    related = [TOPICS[(index + 1) % len(TOPICS)], TOPICS[(index + 9) % len(TOPICS)]]
    category_path = KO_CATEGORY.lower() if lang == "ko" else EN_CATEGORY.lower()
    if lang == "ko":
        return "\n".join(f"- [{topic['ko_title']}](/{{category}}/{topic['slug']}/)".replace("{category}", category_path) for topic in related)
    return "\n".join(f"- [{topic['en_title']}](/{{category}}/{topic['slug']}/)".replace("{category}", category_path) for topic in related)


def ko_post(topic: dict[str, object], index: int) -> str:
    slug = str(topic["slug"])
    image_dir = f"/images/{POST_DATE}-{slug}"
    signals = "\n".join(f"- **{signal}**: 이 신호가 보이면 즉시 멈추고 공식 경로로 다시 확인합니다." for signal in topic["ko_signals"])
    actions = "\n".join(f"- {action}" for action in topic["ko_actions"])
    checklist = "\n".join(f"- {action.replace('합니다.', '했는지 확인합니다.')}" for action in topic["ko_actions"])
    return dedent(f"""\
    ---
    layout: single
    title: >
      {topic["ko_title"]}
    seo_title: >
      {topic["ko_title"]}
    date: {POST_DATE}T{8 + index // 3:02d}:{(index % 3) * 20:02d}:00+09:00
    last_modified_at: {LAST_MODIFIED_AT}
    lang: ko
    translation_id: digital-security-{slug}
    header:
      teaser: {image_dir}/hero.svg
      overlay_image: {image_dir}/hero.svg
      overlay_filter: 0.45
      image_description: >
        {topic["ko_title"]}의 위험 신호와 대응 순서를 요약한 디지털 보안 점검 이미지입니다.
    excerpt: >
      {topic["ko_summary"]}
    seo_description: >
      {topic["ko_summary"]}
    categories:
      - {KO_CATEGORY}
    tags:
    {yaml_list(topic["tags"])}
    ---

    디지털 보안은 전문가만의 일이 아닙니다. 계정 하나, 문자 하나, 백업 하나가 **돈, 개인정보, 가족 안전, 업무 연속성**으로 바로 연결됩니다.

    {topic["ko_summary"]}

    이 글은 제품을 추천하기보다 실제 상황에서 바로 쓸 수 있는 점검 순서와 대응 문장을 정리합니다.

    ![{topic["ko_title"]} 핵심 보안 흐름]({image_dir}/hero.svg)

    ## 왜 위험한가

    {topic["ko_risk"]}

    공격은 대개 기술보다 감정과 습관을 먼저 건드립니다. 급하게 만들고, 확인할 시간을 줄이고, 평소 쓰던 경로가 아니라 메시지 안의 링크나 전화 지시를 따르게 합니다.

    그래서 핵심은 완벽한 지식이 아니라 **멈춤, 별도 확인, 기록 보존, 복구 가능성**입니다. 이 네 가지가 있으면 실수하더라도 피해를 줄일 수 있습니다.

    ## 먼저 볼 위험 신호

    {signals}

    위험 신호가 하나만 보여도 바로 차단하거나 삭제할 필요는 없습니다. 먼저 화면을 캡처하고, 공식 앱이나 주소창 직접 입력처럼 통제 가능한 경로로 다시 확인하세요.

    ![{topic["ko_title"]} 대응 체크리스트]({image_dir}/checklist.svg)

    ## 바로 적용할 순서

    {actions}

    가능하면 가족이나 팀 안에서 같은 규칙을 씁니다. 한 사람이 링크를 누르지 않는 것보다, 모두가 같은 확인 문장을 쓰는 편이 사고 대응이 빠릅니다.

    ## 실수했을 때

    이미 정보를 입력했거나 파일을 열었다면 숨기지 않는 것이 가장 중요합니다. 비밀번호를 바꾸고, 결제수단을 확인하고, 연결된 기기와 로그인 기록을 봅니다.

    업무 계정이나 고객정보가 관련되어 있다면 내부 담당자에게 즉시 공유해야 합니다. 빠른 공유는 책임 회피가 아니라 피해 범위를 줄이는 보안 행동입니다.

    ## 월간 점검 체크리스트

    {checklist}
    - 로그인 기록, 연결 기기, 복구 이메일, 결제 알림을 함께 확인합니다.
    - 보안 설정을 바꾼 날짜와 이유를 짧게 기록합니다.

    ## 참고할 공식 자료

    {source_notes(topic["sources"], "ko")}

    ## 함께 보면 좋은 글

    {related_links(index, "ko")}
    """)


def en_post(topic: dict[str, object], index: int) -> str:
    slug = str(topic["slug"])
    image_dir = f"/images/{POST_DATE}-{slug}"
    signals = "\n".join(f"- **{signal}**: pause immediately and verify through a trusted route." for signal in topic["en_signals"])
    actions = "\n".join(f"- {action}" for action in topic["en_actions"])
    checklist = "\n".join(f"- Confirm that you can: {action[0].lower() + action[1:]}" for action in topic["en_actions"])
    return dedent(f"""\
    ---
    layout: single
    title: >
      {topic["en_title"]}
    seo_title: >
      {topic["en_title"]}
    date: {POST_DATE}T{8 + index // 3:02d}:{(index % 3) * 20:02d}:00+09:00
    last_modified_at: {LAST_MODIFIED_AT}
    lang: en
    translation_id: digital-security-{slug}
    header:
      teaser: {image_dir}/hero.svg
      overlay_image: {image_dir}/hero.svg
      overlay_filter: 0.45
      image_description: >
        A digital security checklist image summarizing risk signals and response steps for this topic.
    excerpt: >
      {topic["en_summary"]}
    seo_description: >
      {topic["en_summary"]}
    categories:
      - {EN_CATEGORY}
    tags:
    {yaml_list(topic["tags"])}
    ---

    Digital security is not only for specialists. One account, one message, or one missing backup can affect **money, privacy, family safety, and business continuity**.

    {topic["en_summary"]}

    This guide avoids product recommendations. It focuses on practical routines and response steps that work when the situation is already stressful.

    ![{topic["en_title"]} core security flow]({image_dir}/hero.svg)

    ## What Can Go Wrong

    {topic["en_risk"]}

    Most attacks start with emotion and habit before they require advanced technology. They create urgency, reduce verification time, and move users away from trusted paths into links, attachments, calls, or chat instructions.

    The useful baseline is **pause, verify separately, preserve records, and keep recovery possible**. Those four habits reduce damage even when a mistake has already happened.

    ## Warning Signals To Check First

    {signals}

    A warning signal does not always mean you should delete everything immediately. First capture the evidence, then verify through a controlled route such as the official app, a saved bookmark, or a known phone number.

    ![{topic["en_title"]} response checklist]({image_dir}/checklist.svg)

    ## Practical Setup Order

    {actions}

    If the risk affects family or a team, use the same rule together. A shared verification phrase is more reliable than expecting everyone to improvise under pressure.

    ## If You Already Made a Mistake

    If you entered information or opened a suspicious file, do not hide it. Change passwords, review payment methods, and check connected devices and login history.

    If work accounts or customer data are involved, tell the responsible person quickly. Fast reporting is a security control, not an admission of failure.

    ## Monthly Checkup

    {checklist}
    - Review login history, connected devices, recovery email, and payment alerts together.
    - Record the date and reason when you change a security setting.

    ## Source Notes

    {source_notes(topic["sources"], "en")}

    ## Related Reading

    {related_links(index, "en")}
    """)


def category_page(lang: str) -> str:
    if lang == "ko":
        return dedent("""\
        ---
        title: "Digital Security"
        layout: archive
        permalink: /ko_digital_security/
        lang: ko
        seo_description: >
          피싱, 스미싱, 비밀번호, 패스키, 2단계 인증, 백업, 랜섬웨어, 개인정보 도용, 소상공인 보안까지 실전 점검 순서로 정리한 한국어 디지털 보안 가이드 모음입니다.
        sidebar:
            nav: "sidebar-category"
        ---

        Digital Security 카테고리는 개인, 가족, 소상공인, 작은 팀이 바로 적용할 수 있는 보안 루틴을 정리합니다. 어려운 보안 용어를 나열하기보다 피싱 문자, 계정 탈취, 백업 실패, 결제 사기, 공유기 설정처럼 실제로 자주 발생하는 상황을 기준으로 설명합니다.

        각 글은 CISA, NIST, FTC, KISA 보호나라, 개인정보침해 신고센터 같은 공식 자료를 참고합니다. 목적은 비싼 보안 제품을 고르는 것이 아니라, 링크를 누르기 전 멈추는 법, 계정을 복구 가능하게 만드는 법, 사고가 난 뒤 피해를 줄이는 법을 익히는 것입니다.

        처음 읽는다면 피싱 판별법, 비밀번호 관리자, 2단계 인증 글부터 시작하세요. 가족이나 매장 운영이 중요하다면 부모님 사기 예방, 소상공인 보안 기준선, 송금 계좌 변경 사기 글을 함께 보는 것이 좋습니다.

        ## 먼저 읽기

        - [피싱 문자와 이메일 30초 판별법](/ko_digital_security/phishing-message-triage/)
        - [비밀번호 관리자 처음 설정하기](/ko_digital_security/password-manager-first-setup/)
        - [소상공인 보안 기준선](/ko_digital_security/small-business-cyber-baseline/)

        ## 최신 글

        {% assign posts = site.categories["ko_Digital_Security"] %}
        {% for post in posts %}
          {% include archive-single.html type=page.entries_layout %}
        {% endfor %}
        """)
    return dedent("""\
    ---
    title: "Digital Security"
    layout: archive
    permalink: /en_digital_security/
    lang: en
    seo_description: >
      Practical digital security guides covering phishing, smishing, passwords, passkeys, MFA, backups, ransomware, identity theft, privacy, and small business cyber hygiene.
    sidebar:
        nav: "sidebar-category"
    ---

    The Digital Security category turns common cyber risks into practical routines for individuals, families, small businesses, and small teams. It focuses on real situations such as phishing messages, account takeover, failed backups, payment fraud, home router settings, and cloud sharing mistakes.

    The articles refer to official sources such as CISA, NIST, FTC, KISA BohoNara, and privacy reporting channels. The goal is not to recommend expensive tools. The goal is to build habits: pause before clicking, verify through a trusted route, keep accounts recoverable, and report incidents early.

    Start with phishing triage, password managers, and MFA. If you run a shop or small team, read the small-business baseline, invoice payment fraud, and employee phishing drill articles together.

    ## Start Here

    - [A 30-Second Phishing Triage](/en_digital_security/phishing-message-triage/)
    - [Password Manager First Setup](/en_digital_security/password-manager-first-setup/)
    - [Small Business Cyber Baseline](/en_digital_security/small-business-cyber-baseline/)

    ## Latest Articles

    {% assign posts = site.categories["en_Digital_Security"] %}
    {% for post in posts %}
      {% include archive-single.html type=page.entries_layout %}
    {% endfor %}
    """)


def main() -> None:
    palettes = [
        ("#0f172a", "#0e7490"),
        ("#111827", "#047857"),
        ("#1e1b4b", "#0f766e"),
        ("#172554", "#7c3aed"),
        ("#312e81", "#0369a1"),
    ]

    for index, topic in enumerate(TOPICS):
        slug = str(topic["slug"])
        ko_path = ROOT / "_posts" / "ko" / f"{POST_DATE}-{slug}.md"
        en_path = ROOT / "_posts" / "en" / f"{POST_DATE}-{slug}.md"
        image_path = ROOT / "images" / f"{POST_DATE}-{slug}"
        palette = palettes[index % len(palettes)]

        ko_path.write_text(normalize_markdown(ko_post(topic, index)), encoding="utf-8")
        en_path.write_text(normalize_markdown(en_post(topic, index)), encoding="utf-8")
        write_svg(
            image_path / "hero.svg",
            str(topic["en_title"])[:64],
            "Risk signals, safe routines, and recovery-first security",
            list(topic["en_signals"]),
            palette,
        )
        write_svg(
            image_path / "checklist.svg",
            "Security Checklist",
            str(topic["en_title"])[:80],
            list(topic["en_actions"]),
            (palette[1], palette[0]),
        )

    (ROOT / "_pages" / f"category-{KO_CATEGORY}.md").write_text(
        normalize_markdown(category_page("ko")),
        encoding="utf-8",
    )
    (ROOT / "_pages" / f"category-{EN_CATEGORY}.md").write_text(
        normalize_markdown(category_page("en")),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
