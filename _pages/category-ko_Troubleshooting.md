---
title: "Troubleshooting"
layout: archive
permalink: /ko_Troubleshooting/
lang: ko
seo_description: >
  Python, JavaScript, Java, Git, Docker, GitHub Actions 오류를 빠르게 재현하고 해결하는 개발자 트러블슈팅 글 모음입니다.
sidebar:
    nav: "sidebar-category"
---

Troubleshooting 카테고리는 개발 중 자주 만나는 오류를 재현 가능한 순서로 해결하는 글을 모읍니다. Python, JavaScript, Java, Git, Docker, GitHub Actions, Jekyll 오류를 중심으로 원인, 빠른 해결, 검증 방법을 제공합니다.

오류 메시지를 그대로 검색해 들어왔다면 같은 도구와 버전 조건을 먼저 확인하고, 마지막 검증 단계까지 실행해 보세요.

각 글은 무작정 설정을 바꾸기보다 현재 상태를 확인하고, 원인을 좁힌 뒤, 마지막에 재발 방지 기준을 남기는 흐름으로 구성되어 있습니다. 같은 오류가 반복될 때 팀 문서로 옮기기 쉽습니다.

## 먼저 읽기

- [Windows에서 python 명령어가 안 될 때 해결 방법](/ko_Troubleshooting/python-command-not-found-windows/)
- [Node.js Cannot find module 오류 해결 방법](/ko_Troubleshooting/node-cannot-find-module/)
- [GitHub Actions build failed 해결 방법](/ko_Troubleshooting/github-actions-build-failed/)

## 최신 글

{% assign posts = site.categories.ko_Troubleshooting %}
{% for post in posts %}
  {% include archive-single.html type=page.entries_layout %}
{% endfor %}
