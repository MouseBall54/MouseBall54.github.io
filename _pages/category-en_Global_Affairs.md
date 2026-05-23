---
title: "Global Affairs"
layout: archive
permalink: /en_global_affairs/
lang: en
seo_description: >
  Official-source global affairs briefings on growth, trade, energy security, defense, climate, migration, and Korea-facing risk.
sidebar:
    nav: "sidebar-category"
---

The Global Affairs category helps readers interpret international issues through **growth, energy, trade, finance, social stability, and Korea-facing transmission channels** rather than through headlines alone.

The articles prioritize official sources such as the IMF, World Bank, WTO, OECD, IEA, SIPRI, UNHCR, WMO, UNEP, FAO, BIS, UNCTAD, KDI, and Korea's MOTIR. The goal is not to predict every event. The goal is to build a repeatable reading system for deciding which signals matter first.

Start with global growth and trade fragmentation to build the map. Then move into energy security, critical minerals, semiconductors, and Korea's export exposure. If you want the household angle, read the food-security and household-cost briefings together.

## Start Here

- [Global Growth and Fragmentation in 2026](/en_global_affairs/global-growth-fragmentation-2026/)
- [Tariffs and Trade Fragmentation](/en_global_affairs/trade-fragmentation-tariff-risk/)
- [Korea's Export Exposure to Global Fragmentation](/en_global_affairs/korea-export-exposure-global-fragmentation/)

## Latest Articles

{% assign posts = site.categories["en_Global_Affairs"] %}
{% for post in posts %}
  {% include archive-single.html type=page.entries_layout %}
{% endfor %}
