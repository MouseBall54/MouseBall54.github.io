---
title: "Climate & Energy"
layout: archive
permalink: /en_climate_energy/
lang: en
seo_description: >
  Official-source climate and energy briefings on grids, AI data centers, renewables, batteries, carbon pricing, heat, floods, adaptation, and Korea-facing industry risk.
sidebar:
    nav: "sidebar-category"
---

The Climate & Energy category helps readers interpret climate and energy news through **grids, industrial competitiveness, household costs, supply chains, and disaster resilience** rather than slogans alone.

The articles prioritize official sources such as the IEA, IPCC, WMO, UNEP, UNFCCC, World Bank, OECD, EIA, and Korean energy and climate agencies. The goal is not to promote one technology or policy. The goal is to build a repeatable reading system for separating demand, supply, price, risk, and Korea-facing transmission channels.

Start with AI data-centre electricity demand, grid bottlenecks, and renewables outlooks to build the map. Then move into batteries, critical minerals, RE100, heat, flood adaptation, and local resilience budgets.

## Start Here

- [AI Data-Center Electricity Demand](/en_climate_energy/ai-data-center-electricity-demand/)
- [The Energy Transition Bottleneck Is the Grid](/en_climate_energy/power-grid-bottlenecks-transition/)
- [A Reading System for Climate and Energy Policy News](/en_climate_energy/climate-policy-news-reading-system/)

## Latest Articles

{% assign posts = site.categories["en_Climate_Energy"] %}
{% for post in posts %}
  {% include archive-single.html type=page.entries_layout %}
{% endfor %}
