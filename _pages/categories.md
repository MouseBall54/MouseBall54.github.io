---
layout: archive
title: "Categories"
permalink: /categories/
seo_description: >
  MouseBall54 Toolbox category hub grouped by language and topic for troubleshooting, AI trends, global affairs, digital security, personal finance, health literacy, study, economy, and Easy Labeling articles.
sidebar:
    nav: "sidebar-category"
---

This site uses one category per post. Categories are split by language first and topic second so Korean and English article lists stay predictable.

Use the links below instead of the raw Jekyll category names. Each hub has an introduction, recommended starting articles, and the latest posts for that language and topic.

{% assign ko_troubleshooting = site.categories["ko_Troubleshooting"] | where_exp: "post", "post.hidden != true" %}
{% assign ko_ai = site.categories["ko_AI_Trends"] | where_exp: "post", "post.hidden != true" %}
{% assign ko_global = site.categories["ko_Global_Affairs"] | where_exp: "post", "post.hidden != true" %}
{% assign ko_security = site.categories["ko_Digital_Security"] | where_exp: "post", "post.hidden != true" %}
{% assign ko_personal_finance = site.categories["ko_Personal_Finance"] | where_exp: "post", "post.hidden != true" %}
{% assign ko_health = site.categories["ko_Health_Literacy"] | where_exp: "post", "post.hidden != true" %}
{% assign ko_study = site.categories["ko_Study"] | where_exp: "post", "post.hidden != true" %}
{% assign ko_economy = site.categories["ko_Economy"] | where_exp: "post", "post.hidden != true" %}
{% assign ko_easy = site.categories["ko_easy_labeling"] | where_exp: "post", "post.hidden != true" %}
{% assign en_troubleshooting = site.categories["en_Troubleshooting"] | where_exp: "post", "post.hidden != true" %}
{% assign en_ai = site.categories["en_AI_Trends"] | where_exp: "post", "post.hidden != true" %}
{% assign en_global = site.categories["en_Global_Affairs"] | where_exp: "post", "post.hidden != true" %}
{% assign en_security = site.categories["en_Digital_Security"] | where_exp: "post", "post.hidden != true" %}
{% assign en_personal_finance = site.categories["en_Personal_Finance"] | where_exp: "post", "post.hidden != true" %}
{% assign en_health = site.categories["en_Health_Literacy"] | where_exp: "post", "post.hidden != true" %}
{% assign en_study = site.categories["en_Study"] | where_exp: "post", "post.hidden != true" %}
{% assign en_economy = site.categories["en_Economy"] | where_exp: "post", "post.hidden != true" %}
{% assign en_easy = site.categories["en_easy_labeling"] | where_exp: "post", "post.hidden != true" %}

## 한국어

| Topic | Articles | Hub |
| --- | ---: | --- |
| Troubleshooting | {{ ko_troubleshooting | size }} | [개발 오류 해결 글](/ko_troubleshooting/) |
| AI Trends | {{ ko_ai | size }} | [AI 실무 워크플로우](/ko_ai_trends/) |
| Global Affairs | {{ ko_global | size }} | [세계정세 브리핑](/ko_global_affairs/) |
| Digital Security | {{ ko_security | size }} | [디지털 보안 가이드](/ko_digital_security/) |
| Personal Finance | {{ ko_personal_finance | size }} | [개인재무 가이드](/ko_personal_finance/) |
| Health Literacy | {{ ko_health | size }} | [건강 리터러시](/ko_health_literacy/) |
| Study | {{ ko_study | size }} | [공부 시스템](/ko_study/) |
| Economy | {{ ko_economy | size }} | [경제 기초](/ko_economy/) |
| Easy Labeling | {{ ko_easy | size }} | [이미지 라벨링](/ko_easy_labeling/) |

## English

| Topic | Articles | Hub |
| --- | ---: | --- |
| Troubleshooting | {{ en_troubleshooting | size }} | [Developer error fixes](/en_troubleshooting/) |
| AI Trends | {{ en_ai | size }} | [AI workflow guides](/en_ai_trends/) |
| Global Affairs | {{ en_global | size }} | [Global affairs briefings](/en_global_affairs/) |
| Digital Security | {{ en_security | size }} | [Digital security guides](/en_digital_security/) |
| Personal Finance | {{ en_personal_finance | size }} | [Personal finance guides](/en_personal_finance/) |
| Health Literacy | {{ en_health | size }} | [Health literacy guides](/en_health_literacy/) |
| Study | {{ en_study | size }} | [Study systems](/en_study/) |
| Economy | {{ en_economy | size }} | [Economy basics](/en_economy/) |
| Easy Labeling | {{ en_easy | size }} | [Image labeling guides](/en_easy_labeling/) |
