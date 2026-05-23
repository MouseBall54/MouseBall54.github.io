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
