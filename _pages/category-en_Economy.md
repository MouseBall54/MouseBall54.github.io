---
title: "Economy"
layout: archive
permalink: /en_economy/
lang: en
seo_description: >
  Educational economy guides connecting interest rates, inflation, exchange rates, GDP, jobs, debt, budgeting, emergency funds, ETFs, and household costs.
sidebar:
    nav: "sidebar-category"
---

The Economy category is educational content for connecting economic indicators to household decisions. It covers interest rates, inflation, exchange rates, GDP, jobs, household debt, budgeting, emergency funds, trade, oil prices, semiconductor cycles, and basic fund comparisons.

The articles refer to official or institution-grade sources such as the IMF, World Bank, OECD, Federal Reserve, BEA, BLS, FRED, Bank of Korea, KOSIS, CFPB, SEC, and FDIC. They are not personal financial advice. Use them to read the numbers, write assumptions, and check how fees, taxes, contracts, inflation, and time horizon change the result.

Start with budgeting, emergency funds, interest rates, inflation, exchange rates, and recession indicators. Then move into GDP, jobs, oil prices, household debt, and yield-curve guides.

## Start Here

- [50/30/20 Budget Rule](/en_economy/household-budget-50-30-20/)
- [How Much Emergency Fund Is Enough?](/en_economy/emergency-fund-how-much/)
- [Interest Rates and Inflation](/en_economy/interest-rate-inflation-basics/)
- [Exchange Rate Basics](/en_economy/exchange-rate-basics/)
- [Recession Indicators](/en_economy/recession-indicators-basics/)

## Latest Articles

{% assign posts = site.categories["en_Economy"] %}
{% for post in posts %}
  {% include archive-single.html type=page.entries_layout %}
{% endfor %}
