#!/usr/bin/env python3
"""Generate paired Global Affairs posts and local SVG context images."""

from __future__ import annotations

import html
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parents[1]
POST_DATE = "2026-05-22"
LAST_MODIFIED_AT = "2026-05-23T12:00:00+09:00"
KO_CATEGORY = "ko_Global_Affairs"
EN_CATEGORY = "en_Global_Affairs"


SOURCES = {
    "imf_weo": {
        "ko": "IMF World Economic Outlook, April 2026",
        "en": "IMF World Economic Outlook, April 2026",
        "url": "https://www.imf.org/en/publications/weo/issues/2026/04/14/world-economic-outlook-april-2026",
    },
    "world_bank_gep": {
        "ko": "World Bank Global Economic Prospects, January 2026",
        "en": "World Bank Global Economic Prospects, January 2026",
        "url": "https://www.worldbank.org/en/news/press-release/2026/01/13/global-economic-prospects-january-2026-press-release",
    },
    "wto_trade": {
        "ko": "WTO Global Trade Outlook and Statistics, March 2026",
        "en": "WTO Global Trade Outlook and Statistics, March 2026",
        "url": "https://www.wto.org/english/res_e/publications_e/gtos0326_e.htm",
    },
    "oecd_outlook": {
        "ko": "OECD Interim Economic Outlook, March 2026",
        "en": "OECD Interim Economic Outlook, March 2026",
        "url": "https://www.oecd.org/en/about/news/press-releases/2026/03/global-economic-outlook-remains-robust-but-has-weakened-amid-energy-shock-and-geopolitical-risks.html",
    },
    "iea_weo": {
        "ko": "IEA World Energy Outlook 2025",
        "en": "IEA World Energy Outlook 2025",
        "url": "https://www.iea.org/reports/world-energy-outlook-2025/executive-summary",
    },
    "iea_electricity": {
        "ko": "IEA Electricity 2026",
        "en": "IEA Electricity 2026",
        "url": "https://www.iea.org/reports/electricity-2026/executive-summary",
    },
    "iea_minerals": {
        "ko": "IEA Global Critical Minerals Outlook 2025",
        "en": "IEA Global Critical Minerals Outlook 2025",
        "url": "https://www.iea.org/reports/global-critical-minerals-outlook-2025/executive-summary",
    },
    "sipri_milex": {
        "ko": "SIPRI Trends in World Military Expenditure 2025",
        "en": "SIPRI Trends in World Military Expenditure 2025",
        "url": "https://www.sipri.org/publications/2026/sipri-fact-sheets/trends-world-military-expenditure-2025",
    },
    "unhcr_trends": {
        "ko": "UNHCR Global Trends",
        "en": "UNHCR Global Trends",
        "url": "https://www.unhcr.org/what-we-do/reports-and-publications/global-trends",
    },
    "wmo_2025": {
        "ko": "WMO 2025 Global Temperature Update",
        "en": "WMO 2025 Global Temperature Update",
        "url": "https://wmo.int/news/media-centre/wmo-confirms-2025-was-one-of-warmest-years-record",
    },
    "unep_gap": {
        "ko": "UNEP Emissions Gap Report 2025",
        "en": "UNEP Emissions Gap Report 2025",
        "url": "https://www.unep.org/resources/emissions-gap-report-2025",
    },
    "fao_sofi": {
        "ko": "FAO SOFI 2025",
        "en": "FAO SOFI 2025",
        "url": "https://www.fao.org/agrifood-economics/publications/detail/en/c/1740904/",
    },
    "world_bank_debt": {
        "ko": "World Bank International Debt Report 2025",
        "en": "World Bank International Debt Report 2025",
        "url": "https://www.worldbank.org/en/programs/debt-statistics/idr/products",
    },
    "world_bank_ukraine": {
        "ko": "World Bank Ukraine Recovery, Reconstruction and Reform Trust Fund",
        "en": "World Bank Ukraine Recovery, Reconstruction and Reform Trust Fund",
        "url": "https://www.worldbank.org/en/programs/urtf/overview",
    },
    "bis_annual": {
        "ko": "BIS Annual Economic Report 2025",
        "en": "BIS Annual Economic Report 2025",
        "url": "https://www.bis.org/publ/arpdf/ar2025e.htm",
    },
    "unctad_rmt": {
        "ko": "UNCTAD Review of Maritime Transport 2025",
        "en": "UNCTAD Review of Maritime Transport 2025",
        "url": "https://unctad.org/RMT",
    },
    "unctad_fdi": {
        "ko": "UNCTAD World Investment Report 2025",
        "en": "UNCTAD World Investment Report 2025",
        "url": "https://unctad.org/publication/world-investment-report-2025",
    },
    "kdi_outlook": {
        "ko": "KDI Economic Outlook 2026, 1st Half",
        "en": "KDI Economic Outlook 2026, 1st Half",
        "url": "https://www.kdi.re.kr/eng/research/economy?pub_no=19180",
    },
    "motir_exports": {
        "ko": "Korea MOTIR March 2026 Export Release",
        "en": "Korea MOTIR March 2026 Export Release",
        "url": "https://english.motir.go.kr/eng/article/EATCLdfa319ada/2559/view",
    },
    "cisa_infra": {
        "ko": "CISA Critical Infrastructure Security and Resilience",
        "en": "CISA Critical Infrastructure Security and Resilience",
        "url": "https://www.cisa.gov/infrastructure-security",
    },
    "nato_space": {
        "ko": "NATO Approach to Space",
        "en": "NATO Approach to Space",
        "url": "https://www.nato.int/en/what-we-do/deterrence-and-defence/natos-approach-to-space",
    },
    "un_population": {
        "ko": "UN World Population Prospects",
        "en": "UN World Population Prospects",
        "url": "https://population.un.org/wpp/",
    },
}


TOPICS = [
    {
        "slug": "global-growth-fragmentation-2026",
        "ko_title": "2026년 세계 성장 둔화와 분절화: 숫자보다 중요한 해석법",
        "en_title": "Global Growth and Fragmentation in 2026: How to Read the New Baseline",
        "ko_summary": "IMF와 World Bank 전망을 함께 놓고 보면 2026년 세계경제의 핵심은 경기침체 여부보다 낮은 성장, 높은 불확실성, 정책 신뢰의 동시 관리다.",
        "en_summary": "Read IMF and World Bank projections together and the central issue is not a single recession call, but the combined pressure of slower growth, uncertainty, and policy credibility.",
        "ko_angle": "한국처럼 수출, 에너지, 금융시장이 모두 열려 있는 경제는 세계 성장률 한 줄보다 교역량, 원자재 가격, 달러 유동성의 조합을 먼저 봐야 한다.",
        "en_angle": "For open economies such as Korea, the growth headline matters less than the mix of trade volumes, commodity prices, and dollar funding conditions.",
        "signals": ["global growth forecast", "inflation path", "trade policy uncertainty", "public debt stress"],
        "ko_signals": ["세계 성장률 전망", "물가 재상승 여부", "무역정책 불확실성", "공공부채 부담"],
        "sources": ["imf_weo", "world_bank_gep", "oecd_outlook"],
        "tags": ["Global Economy", "Geopolitics", "Inflation", "Trade"],
    },
    {
        "slug": "trade-fragmentation-tariff-risk",
        "ko_title": "관세와 무역 분절화 리스크: 공급망 뉴스 읽는 순서",
        "en_title": "Tariffs and Trade Fragmentation: A Practical Reading Order for Supply-Chain News",
        "ko_summary": "WTO와 OECD 전망은 무역량 자체보다 정책 불확실성이 기업의 재고, 투자, 가격 결정에 누적되는 과정을 봐야 한다는 점을 보여준다.",
        "en_summary": "WTO and OECD updates show that the real issue is how policy uncertainty accumulates inside inventories, investment decisions, and pricing power.",
        "ko_angle": "한국 기업은 관세율보다 최종 수요 지역, 중간재 이동 경로, 환율 충격을 한 장의 지도로 묶어야 무역 뉴스를 덜 흔들리며 읽을 수 있다.",
        "en_angle": "Korean exporters need a map that links final demand, intermediate-goods routes, and currency shocks rather than reacting only to tariff headlines.",
        "signals": ["effective tariff rates", "export orders", "supplier rerouting", "inventory build-up"],
        "ko_signals": ["실효 관세율", "제조업 수출 주문", "공급처 우회", "재고 누적"],
        "sources": ["wto_trade", "oecd_outlook", "unctad_fdi"],
        "tags": ["Trade", "Tariffs", "Supply Chains", "Policy Risk"],
    },
    {
        "slug": "middle-east-energy-shock-risk",
        "ko_title": "중동 에너지 충격이 세계경제를 흔드는 경로",
        "en_title": "How a Middle East Energy Shock Moves Through the World Economy",
        "ko_summary": "중동 충돌은 유가만의 문제가 아니라 물가 기대, 운송비, 비료 가격, 금융시장 변동성을 동시에 건드리는 복합 충격이다.",
        "en_summary": "A Middle East energy shock is not only about oil; it can move inflation expectations, shipping costs, fertilizer prices, and financial volatility at the same time.",
        "ko_angle": "한국 독자는 두바이유 가격만 보지 말고 에너지 수입액, 정유·석화 마진, 항공·해운 비용까지 함께 확인해야 한다.",
        "en_angle": "Korean readers should track energy import costs, refining and petrochemical margins, and air and sea freight costs, not just the Dubai crude headline.",
        "signals": ["oil price curve", "Hormuz disruption risk", "energy import bill", "inflation expectations"],
        "ko_signals": ["유가 선물곡선", "호르무즈 해협 리스크", "에너지 수입액", "기대 인플레이션"],
        "sources": ["imf_weo", "oecd_outlook", "kdi_outlook"],
        "tags": ["Energy Security", "Middle East", "Inflation", "Oil"],
    },
    {
        "slug": "red-sea-shipping-chokepoints",
        "ko_title": "홍해와 해상 병목: 해운 리스크가 소비자 가격으로 번지는 과정",
        "en_title": "Red Sea and Maritime Chokepoints: How Shipping Risk Reaches Consumer Prices",
        "ko_summary": "해상 운송은 세계 상품무역의 기본 인프라이며, 특정 해협의 병목은 운송거리, 보험료, 납기, 재고비용을 동시에 올린다.",
        "en_summary": "Maritime transport is the base layer of goods trade, and chokepoint stress can raise sailing distance, insurance costs, delivery times, and inventory costs together.",
        "ko_angle": "한국은 원유·가스·중간재·완제품 흐름이 모두 바다에 걸려 있어 해운 뉴스가 곧 수출 채산성과 생활물가 뉴스가 된다.",
        "en_angle": "For Korea, maritime disruptions affect energy imports, intermediate goods, finished exports, corporate margins, and consumer prices at once.",
        "signals": ["vessel rerouting", "freight indexes", "insurance premiums", "port congestion"],
        "ko_signals": ["선박 우회", "운임지수", "보험료", "항만 혼잡"],
        "sources": ["unctad_rmt", "oecd_outlook", "motir_exports"],
        "tags": ["Shipping", "Trade", "Supply Chains", "Inflation"],
    },
    {
        "slug": "critical-minerals-supply-chain",
        "ko_title": "핵심광물 공급망: 배터리와 AI 시대의 새로운 에너지 안보",
        "en_title": "Critical Minerals Supply Chains: The New Energy Security Layer for Batteries and AI",
        "ko_summary": "IEA는 핵심광물 문제가 전기차와 재생에너지를 넘어 AI 칩, 방산, 항공우주까지 연결되는 전략 리스크라고 본다.",
        "en_summary": "The IEA frames critical minerals as a strategic risk that reaches beyond EVs and renewables into AI chips, defense, aerospace, and advanced manufacturing.",
        "ko_angle": "한국은 배터리, 반도체, 자동차가 동시에 핵심광물에 노출되어 있어 가격보다 정제 집중도와 수출통제를 먼저 봐야 한다.",
        "en_angle": "Korea's batteries, semiconductors, and autos are all exposed, so refining concentration and export controls matter more than spot prices alone.",
        "signals": ["refining concentration", "export controls", "battery metal prices", "recycling capacity"],
        "ko_signals": ["정제 집중도", "수출통제", "배터리 금속 가격", "재활용 설비"],
        "sources": ["iea_minerals", "iea_weo", "motir_exports"],
        "tags": ["Critical Minerals", "Batteries", "Energy Security", "Semiconductors"],
    },
    {
        "slug": "semiconductor-export-controls",
        "ko_title": "반도체 수출통제와 AI 하드웨어 경쟁의 다음 국면",
        "en_title": "Semiconductor Export Controls and the Next Phase of AI Hardware Competition",
        "ko_summary": "AI 하드웨어 경쟁은 첨단 칩뿐 아니라 장비, 소재, 희소금속, 전력 인프라가 하나의 패키지로 움직이는 경쟁이다.",
        "en_summary": "AI hardware competition is a bundled contest across advanced chips, tools, materials, rare minerals, and electricity infrastructure.",
        "ko_angle": "한국 반도체 수출 호조는 기회이지만, 특정 국가 수요와 소재 통제에 과도하게 묶이면 업황 변동성이 커진다.",
        "en_angle": "Korea's semiconductor export strength is an opportunity, but reliance on concentrated demand and controlled materials can amplify cycle risk.",
        "signals": ["advanced chip demand", "equipment import data", "materials controls", "data-center capex"],
        "ko_signals": ["첨단 칩 수요", "장비 수입", "소재 통제", "데이터센터 투자"],
        "sources": ["motir_exports", "iea_minerals", "iea_electricity"],
        "tags": ["Semiconductors", "AI", "Export Controls", "Korea"],
    },
    {
        "slug": "ai-data-center-electricity-demand",
        "ko_title": "AI 데이터센터 전력 수요: 기술주 뉴스가 전력망 뉴스가 되는 이유",
        "en_title": "AI Data-Center Electricity Demand: Why Tech News Is Becoming Grid News",
        "ko_summary": "IEA Electricity 2026은 전력 수요가 데이터센터, 산업, 냉방, 전기차를 통해 경제성장보다 빠르게 움직일 수 있음을 보여준다.",
        "en_summary": "IEA Electricity 2026 shows electricity demand can outpace economic growth as data centres, industry, cooling, and EVs reshape the load profile.",
        "ko_angle": "한국은 AI 반도체 공급자이자 전력 다소비 제조업 국가이므로 전력망 병목이 수출 경쟁력의 변수가 된다.",
        "en_angle": "Korea is both an AI chip supplier and a power-intensive manufacturing economy, so grid bottlenecks can become an export-competitiveness issue.",
        "signals": ["data-center load", "grid connection queues", "power prices", "renewables and nuclear output"],
        "ko_signals": ["데이터센터 부하", "계통 접속 대기", "전력가격", "재생에너지·원전 발전량"],
        "sources": ["iea_electricity", "iea_weo", "motir_exports"],
        "tags": ["AI", "Electricity", "Data Centers", "Infrastructure"],
    },
    {
        "slug": "energy-transition-grid-bottlenecks",
        "ko_title": "에너지 전환의 병목은 발전량보다 전력망이다",
        "en_title": "The Energy Transition Bottleneck Is the Grid, Not Only Generation",
        "ko_summary": "재생에너지와 전기화가 늘수록 핵심 질문은 전기를 얼마나 만들 수 있느냐에서 어디로, 언제, 얼마나 안정적으로 보낼 수 있느냐로 이동한다.",
        "en_summary": "As renewables and electrification expand, the main question shifts from how much electricity can be generated to where and when it can be delivered reliably.",
        "ko_angle": "한국의 산업단지, 반도체 클러스터, 데이터센터 입지는 전력망 투자 속도와 함께 봐야 현실적인 경쟁력 평가가 가능하다.",
        "en_angle": "Korea's industrial parks, semiconductor clusters, and data-centre plans need to be evaluated alongside grid investment speed.",
        "signals": ["transmission investment", "curtailment rates", "peak demand", "industrial power contracts"],
        "ko_signals": ["송전망 투자", "출력제어", "피크 수요", "산업용 전력계약"],
        "sources": ["iea_electricity", "iea_weo", "oecd_outlook"],
        "tags": ["Energy Transition", "Grid", "Electricity", "Industry"],
    },
    {
        "slug": "nuclear-energy-comeback",
        "ko_title": "원전 재부상: 에너지 안보와 전력 수요가 만든 현실적 선택지",
        "en_title": "The Nuclear Energy Comeback: A Realist Response to Security and Power Demand",
        "ko_summary": "원전은 기후정책만의 이슈가 아니라 전력망 안정성, 산업용 전력, 에너지 수입 의존도를 동시에 낮추려는 전략의 일부로 돌아오고 있다.",
        "en_summary": "Nuclear power is returning not only as climate policy but as a strategy for grid stability, industrial electricity, and lower import dependence.",
        "ko_angle": "한국에서는 원전 뉴스가 전기요금, 산업정책, 수출형 원전, 사용후핵연료 논쟁까지 한 번에 연결된다.",
        "en_angle": "In Korea, nuclear policy links power bills, industrial strategy, exportable reactors, and spent-fuel governance in one debate.",
        "signals": ["reactor restarts", "new capacity plans", "power price stability", "fuel-cycle policy"],
        "ko_signals": ["원전 재가동", "신규 설비 계획", "전력가격 안정성", "연료주기 정책"],
        "sources": ["iea_electricity", "iea_weo", "kdi_outlook"],
        "tags": ["Nuclear Energy", "Energy Security", "Electricity", "Korea"],
    },
    {
        "slug": "defense-spending-surge",
        "ko_title": "방위비 급증의 경제학: 안보 지출은 성장과 재정에 무엇을 남기나",
        "en_title": "The Economics of Rising Defense Spending: Growth, Inflation, and Fiscal Trade-offs",
        "ko_summary": "SIPRI와 IMF 자료는 방위비 증가가 단기 수요를 만들 수 있지만 재정, 물가, 사회지출의 선택 문제를 남긴다는 점을 보여준다.",
        "en_summary": "SIPRI and IMF data show defense buildups can support short-term demand while leaving harder trade-offs for budgets, inflation, and social spending.",
        "ko_angle": "한국은 안보 리스크가 상시적이므로 방위비 논쟁을 총액보다 조달 구조, 국내 산업 파급, 재정 지속성으로 나눠 봐야 한다.",
        "en_angle": "Korea should read defense spending debates through procurement structure, domestic industrial spillovers, and fiscal sustainability, not totals alone.",
        "signals": ["military burden", "procurement mix", "deficit financing", "dual-use technology"],
        "ko_signals": ["군사비 부담률", "조달 구성", "적자 재원", "민군 겸용 기술"],
        "sources": ["sipri_milex", "imf_weo", "bis_annual"],
        "tags": ["Defense", "Fiscal Policy", "Geopolitics", "Security"],
    },
    {
        "slug": "ukraine-reconstruction-finance",
        "ko_title": "우크라이나 재건금융: 전쟁 이후 시장을 읽는 현실적 기준",
        "en_title": "Ukraine Reconstruction Finance: A Realistic Framework for the Postwar Market",
        "ko_summary": "우크라이나 재건은 원조 뉴스가 아니라 에너지, 주택, 물류, 민간자본, 제도개혁이 맞물린 장기 프로젝트다.",
        "en_summary": "Ukraine reconstruction is not just aid news; it is a long project across energy, housing, logistics, private capital, and institutional reform.",
        "ko_angle": "한국 기업에는 인프라·건설·에너지 장비 기회가 보일 수 있지만, 전쟁 리스크와 보증 구조를 먼저 확인해야 한다.",
        "en_angle": "Korean firms may see opportunities in infrastructure, construction, and energy equipment, but war risk and guarantee structures come first.",
        "signals": ["donor guarantees", "energy reconstruction", "private capital mobilization", "insurance and demining"],
        "ko_signals": ["공여국 보증", "에너지 재건", "민간자본 동원", "보험·지뢰 제거"],
        "sources": ["world_bank_ukraine", "sipri_milex", "world_bank_debt"],
        "tags": ["Ukraine", "Reconstruction", "Development Finance", "Infrastructure"],
    },
    {
        "slug": "food-security-price-risk",
        "ko_title": "식량안보와 식품물가: 기후보다 먼저 지갑에 도착하는 세계정세",
        "en_title": "Food Security and Food Prices: The Global Issue That Reaches Wallets First",
        "ko_summary": "FAO SOFI 2025는 식품 가격 인플레이션이 저소득층의 건강한 식단 접근과 아동 영양에 직접 영향을 준다고 설명한다.",
        "en_summary": "FAO's SOFI 2025 explains how food price inflation directly weakens low-income access to healthy diets and affects child nutrition.",
        "ko_angle": "한국 소비자는 국제 곡물가, 환율, 에너지 가격, 유통비가 합쳐져 장바구니 가격으로 바뀌는 경로를 봐야 한다.",
        "en_angle": "Korean households should track how global grains, exchange rates, energy prices, and distribution costs combine into grocery prices.",
        "signals": ["grain prices", "fertilizer costs", "food CPI", "import dependency"],
        "ko_signals": ["곡물가격", "비료비", "식품 CPI", "수입 의존도"],
        "sources": ["fao_sofi", "oecd_outlook", "unep_gap"],
        "tags": ["Food Security", "Inflation", "Climate Risk", "Households"],
    },
    {
        "slug": "forced-displacement-migration-pressure",
        "ko_title": "강제이주와 난민 압력: 숫자 뒤의 노동·주거·정치 리스크",
        "en_title": "Forced Displacement and Migration Pressure: Labor, Housing, and Political Risk Behind the Numbers",
        "ko_summary": "UNHCR 수치는 전쟁과 폭력이 이동을 만들고, 이동은 다시 노동시장, 주택, 교육, 정치 갈등으로 번진다는 사실을 보여준다.",
        "en_summary": "UNHCR data show how conflict and violence create displacement, which then reshapes labor markets, housing, education, and politics.",
        "ko_angle": "한국은 직접 난민 유입 규모보다 고령화 노동시장, 해외건설·개발협력, 국제여론의 변화까지 함께 읽어야 한다.",
        "en_angle": "Korea should connect displacement trends with ageing labor markets, overseas development work, and shifting global public opinion.",
        "signals": ["refugee flows", "return conditions", "aid funding", "urban absorption capacity"],
        "ko_signals": ["난민 이동", "귀환 여건", "원조 재원", "도시 수용력"],
        "sources": ["unhcr_trends", "world_bank_ukraine", "fao_sofi"],
        "tags": ["Migration", "Refugees", "Conflict", "Labor"],
    },
    {
        "slug": "climate-risk-insurance-gap",
        "ko_title": "기후 리스크와 보험 공백: 재난은 왜 금융문제가 되는가",
        "en_title": "Climate Risk and the Insurance Gap: Why Disasters Become Financial Problems",
        "ko_summary": "WMO와 UNEP 자료를 함께 보면 기후 리스크는 자연재해 통계가 아니라 보험료, 부동산, 지방재정, 기업공시의 문제로 이동하고 있다.",
        "en_summary": "Read WMO and UNEP together and climate risk shifts from weather statistics to insurance, property, local budgets, and corporate disclosure.",
        "ko_angle": "한국에서는 집중호우, 폭염, 해안 침수, 농산물 가격이 보험과 재정 부담을 통해 생활비로 연결된다.",
        "en_angle": "In Korea, heavy rain, heat, coastal exposure, and food prices can all become living-cost issues through insurance and public budgets.",
        "signals": ["insured losses", "premium repricing", "municipal budgets", "heat and flood alerts"],
        "ko_signals": ["보험 손실", "보험료 재산정", "지방재정", "폭염·홍수 경보"],
        "sources": ["wmo_2025", "unep_gap", "fao_sofi"],
        "tags": ["Climate Risk", "Insurance", "Disasters", "Finance"],
    },
    {
        "slug": "emissions-gap-policy-risk",
        "ko_title": "배출격차 보고서 읽기: 기후정책은 왜 산업정책이 되었나",
        "en_title": "Reading the Emissions Gap: Why Climate Policy Has Become Industrial Policy",
        "ko_summary": "UNEP Emissions Gap Report는 현재 정책과 목표 사이의 간극이 탄소가격, 보조금, 무역장벽, 기술투자 논쟁으로 번지고 있음을 보여준다.",
        "en_summary": "UNEP's Emissions Gap Report shows how the gap between current policy and targets is becoming a fight over carbon prices, subsidies, trade rules, and technology investment.",
        "ko_angle": "한국 기업은 탄소중립 선언보다 고객사 배출 요구, 전력 믹스, 탄소국경조정, 공정 전환비용을 같이 봐야 한다.",
        "en_angle": "Korean firms need to read customer emissions demands, power mix, carbon border rules, and process-transition costs together.",
        "signals": ["NDC ambition", "carbon prices", "clean-tech subsidies", "scope 3 requirements"],
        "ko_signals": ["NDC 상향", "탄소가격", "청정기술 보조금", "Scope 3 요구"],
        "sources": ["unep_gap", "iea_weo", "unctad_fdi"],
        "tags": ["Climate Policy", "Industrial Policy", "Emissions", "Trade"],
    },
    {
        "slug": "sovereign-debt-stress",
        "ko_title": "국가부채 스트레스: 고금리 이후 개발도상국이 맞는 두 번째 충격",
        "en_title": "Sovereign Debt Stress: The Second Shock After High Interest Rates",
        "ko_summary": "World Bank와 IMF 자료는 부채 문제가 단순한 재정 지표가 아니라 개발투자, 통화가치, 식량·에너지 보조금 여력을 결정한다고 말한다.",
        "en_summary": "World Bank and IMF updates show sovereign debt is not just a fiscal ratio; it shapes development investment, currencies, and food and energy support.",
        "ko_angle": "한국 독자는 신흥국 부채 뉴스를 원자재 수요, 수출시장 안정성, 달러 강세 리스크와 연결해 읽는 편이 유용하다.",
        "en_angle": "Korean readers should connect emerging-market debt stress with commodity demand, export-market stability, and dollar strength.",
        "signals": ["debt service", "currency depreciation", "IMF programs", "capital outflows"],
        "ko_signals": ["채무상환액", "통화 절하", "IMF 프로그램", "자본유출"],
        "sources": ["world_bank_debt", "imf_weo", "bis_annual"],
        "tags": ["Sovereign Debt", "Emerging Markets", "Dollar", "Development"],
    },
    {
        "slug": "dollar-funding-financial-stability",
        "ko_title": "달러 유동성과 금융안정: 세계정세가 환율로 번역되는 방식",
        "en_title": "Dollar Funding and Financial Stability: How Geopolitics Gets Translated Into FX",
        "ko_summary": "BIS는 무역 긴장, 비은행 금융, 통화시스템 변화가 금융시장 연결성을 키운다고 본다. 달러 조달비용은 그 연결성의 가장 빠른 신호다.",
        "en_summary": "The BIS highlights trade tensions, non-bank finance, and monetary-system change. Dollar funding costs are one of the fastest signals of that connectivity.",
        "ko_angle": "한국에서는 원달러 환율, 외국인 주식·채권 흐름, 기업 달러부채가 동시에 움직일 때 세계정세의 압력이 커진다.",
        "en_angle": "For Korea, global pressure rises when USD/KRW, foreign portfolio flows, and corporate dollar debt move in the same direction.",
        "signals": ["cross-currency basis", "Treasury yields", "portfolio flows", "bank dollar liquidity"],
        "ko_signals": ["통화스와프 베이시스", "미국채 금리", "외국인 자금", "은행 달러 유동성"],
        "sources": ["bis_annual", "imf_weo", "world_bank_debt"],
        "tags": ["Dollar", "Financial Stability", "FX", "Capital Flows"],
    },
    {
        "slug": "stablecoins-monetary-sovereignty",
        "ko_title": "스테이블코인과 통화주권: 결제 혁신 뒤에 있는 정책 질문",
        "en_title": "Stablecoins and Monetary Sovereignty: The Policy Questions Behind Payment Innovation",
        "ko_summary": "BIS의 차세대 통화시스템 논의는 토큰화와 스테이블코인을 기술 이슈가 아니라 중앙은행 돈, 은행예금, 국채시장 설계의 문제로 본다.",
        "en_summary": "The BIS discussion of next-generation money treats tokenisation and stablecoins as questions about central bank money, bank deposits, and government bond markets.",
        "ko_angle": "한국은 원화 결제 인프라, 외화 스테이블코인 사용, 가상자산 규제, 은행 유동성 관리가 한데 묶일 수 있다.",
        "en_angle": "Korea may have to connect won payment infrastructure, foreign-currency stablecoin use, crypto regulation, and bank-liquidity management.",
        "signals": ["reserve assets", "redemption rules", "bank deposit shifts", "cross-border payments"],
        "ko_signals": ["준비자산", "상환 규칙", "예금 이동", "국경간 결제"],
        "sources": ["bis_annual", "imf_weo", "world_bank_debt"],
        "tags": ["Stablecoins", "Monetary Policy", "Fintech", "BIS"],
    },
    {
        "slug": "demographic-aging-fiscal-pressure",
        "ko_title": "인구고령화와 재정압박: 세계가 동시에 늙을 때 생기는 문제",
        "en_title": "Demographic Ageing and Fiscal Pressure: What Happens When the World Ages Together",
        "ko_summary": "인구 전망은 출산율 문제가 아니라 연금, 의료, 노동공급, 이민정책, 자동화 투자의 장기 재정표다.",
        "en_summary": "Population projections are not only about fertility; they are a long fiscal map for pensions, healthcare, labor supply, migration, and automation.",
        "ko_angle": "한국은 가장 빠른 고령화 국가 중 하나이므로 세계 인구 흐름을 노동력 확보와 생산성 투자 관점에서 읽어야 한다.",
        "en_angle": "As one of the fastest-ageing economies, Korea should read global demographics through labor supply and productivity investment.",
        "signals": ["old-age dependency", "labor-force participation", "health spending", "migration policy"],
        "ko_signals": ["노년부양비", "경제활동참가율", "의료비", "이민정책"],
        "sources": ["un_population", "world_bank_gep", "kdi_outlook"],
        "tags": ["Demographics", "Fiscal Policy", "Labor", "Ageing"],
    },
    {
        "slug": "migration-policy-labor-market",
        "ko_title": "이민정책과 노동시장: 인구 감소 시대의 경쟁력 변수",
        "en_title": "Migration Policy and Labor Markets: A Competitiveness Variable in the Ageing Era",
        "ko_summary": "이민정책은 국경관리만의 문제가 아니라 돌봄, 제조, 건설, 교육, 도시주거를 동시에 바꾸는 노동시장 정책이다.",
        "en_summary": "Migration policy is not only border control; it changes care work, manufacturing, construction, education, and urban housing at once.",
        "ko_angle": "한국은 숙련·비숙련 인력 부족을 동시에 겪기 때문에 유학생, 지역정착, 사회통합 비용을 같이 설계해야 한다.",
        "en_angle": "Korea faces both skilled and lower-wage labor shortages, so student visas, regional settlement, and integration costs need one design.",
        "signals": ["work visa quotas", "wage gaps", "housing pressure", "integration budgets"],
        "ko_signals": ["취업비자 쿼터", "임금 격차", "주거 압력", "통합 예산"],
        "sources": ["un_population", "unhcr_trends", "world_bank_gep"],
        "tags": ["Migration", "Labor Market", "Demographics", "Policy"],
    },
    {
        "slug": "friend-shoring-supply-chain-cost",
        "ko_title": "프렌드쇼어링의 비용: 안정적 공급망은 공짜가 아니다",
        "en_title": "The Cost of Friend-Shoring: Resilient Supply Chains Are Not Free",
        "ko_summary": "공급망을 우방 중심으로 재배치하면 정치 리스크는 줄 수 있지만 중복투자, 단가 상승, 시장 분할이라는 비용이 생긴다.",
        "en_summary": "Moving supply chains toward trusted partners can reduce political risk, but it adds duplication, higher unit costs, and market fragmentation.",
        "ko_angle": "한국 기업은 미국, 중국, EU, ASEAN 생산거점을 단순 대체가 아니라 고객·규제·물류별 포트폴리오로 재설계해야 한다.",
        "en_angle": "Korean firms need portfolio design across the US, China, EU, and ASEAN rather than a simple replacement of one production base with another.",
        "signals": ["FDI project counts", "local-content rules", "supplier redundancy", "unit production cost"],
        "ko_signals": ["FDI 프로젝트", "현지조달 규정", "공급처 중복", "단위 생산비"],
        "sources": ["unctad_fdi", "wto_trade", "iea_minerals"],
        "tags": ["Friend-Shoring", "FDI", "Supply Chains", "Trade"],
    },
    {
        "slug": "green-industrial-policy-subsidies",
        "ko_title": "녹색 산업정책과 보조금 경쟁: 기후와 보호무역의 경계",
        "en_title": "Green Industrial Policy and Subsidy Competition: Where Climate Meets Protectionism",
        "ko_summary": "청정기술 보조금은 배출 감축을 빠르게 만들 수 있지만 무역분쟁, 예산 부담, 공급과잉 논쟁도 동시에 만든다.",
        "en_summary": "Clean-tech subsidies can accelerate decarbonisation, but they also create trade disputes, fiscal costs, and overcapacity debates.",
        "ko_angle": "한국 배터리·태양광·전력기기 기업은 보조금 수혜만 보지 말고 원산지, 탄소발자국, 현지 생산요건을 같이 봐야 한다.",
        "en_angle": "Korean battery, solar, and power-equipment firms should track origin rules, carbon footprint rules, and local production requirements together.",
        "signals": ["subsidy rules", "local content", "carbon border measures", "factory utilisation"],
        "ko_signals": ["보조금 규정", "현지조달", "탄소국경조정", "공장 가동률"],
        "sources": ["unep_gap", "unctad_fdi", "wto_trade"],
        "tags": ["Industrial Policy", "Climate", "Subsidies", "Trade"],
    },
    {
        "slug": "water-security-geopolitics",
        "ko_title": "물 안보와 지정학: 식량·전력·도시가 만나는 리스크",
        "en_title": "Water Security and Geopolitics: Where Food, Power, and Cities Meet",
        "ko_summary": "물 부족과 홍수는 농산물 가격, 수력발전, 반도체 공정, 도시 인프라를 동시에 건드리는 복합 리스크다.",
        "en_summary": "Water scarcity and floods can hit food prices, hydropower, semiconductor processes, and urban infrastructure at the same time.",
        "ko_angle": "한국은 물 부족 국가 논쟁보다 산업용수, 집중호우, 댐·하천 관리, 농산물 수급을 한 묶음으로 봐야 한다.",
        "en_angle": "Korea should connect industrial water, heavy rain, dam and river management, and agricultural supply rather than treating water as one issue.",
        "signals": ["drought indices", "flood losses", "industrial water permits", "food import prices"],
        "ko_signals": ["가뭄지수", "홍수 피해", "산업용수 허가", "식품 수입가격"],
        "sources": ["wmo_2025", "fao_sofi", "iea_minerals"],
        "tags": ["Water Security", "Climate", "Food", "Infrastructure"],
    },
    {
        "slug": "arctic-route-geopolitics",
        "ko_title": "북극항로와 해운 지정학: 짧아진 길이 곧 안전한 길은 아니다",
        "en_title": "Arctic Routes and Maritime Geopolitics: A Shorter Route Is Not Always Safer",
        "ko_summary": "북극항로 논의는 거리 단축만이 아니라 보험, 구조 능력, 군사긴장, 환경규제, 항만 인프라의 합산 문제다.",
        "en_summary": "Arctic-route debates are not only about distance; they combine insurance, rescue capacity, military tension, environmental rules, and port infrastructure.",
        "ko_angle": "한국 조선·해운업은 북극항로를 장기 옵션으로 보되 단기 수익보다 규제와 안전 인프라를 먼저 점검해야 한다.",
        "en_angle": "Korean shipbuilders and carriers can treat Arctic routes as a long option, but safety infrastructure and regulation come before short-term savings.",
        "signals": ["ice conditions", "insurance coverage", "port readiness", "naval activity"],
        "ko_signals": ["해빙 상태", "보험 보장", "항만 준비", "군사 활동"],
        "sources": ["unctad_rmt", "wmo_2025", "nato_space"],
        "tags": ["Arctic", "Shipping", "Geopolitics", "Climate"],
    },
    {
        "slug": "space-security-satellite-risk",
        "ko_title": "우주안보와 위성 리스크: 통신·금융·군사 인프라의 공통 약점",
        "en_title": "Space Security and Satellite Risk: The Shared Weakness of Communications, Finance, and Defense",
        "ko_summary": "NATO의 우주 접근은 위성이 군사뿐 아니라 통신, 위치정보, 금융, 기상, 재난 대응의 핵심 인프라가 되었음을 보여준다.",
        "en_summary": "NATO's approach to space shows satellites have become core infrastructure for communications, positioning, finance, weather, and crisis response.",
        "ko_angle": "한국은 위성통신, 정찰위성, 자율주행, 금융결제, 해운 위치정보가 모두 우주 인프라에 기대고 있다는 점을 봐야 한다.",
        "en_angle": "Korea should read satellite communications, reconnaissance, autonomous mobility, payments, and shipping navigation as one space-infrastructure stack.",
        "signals": ["satellite outages", "space debris alerts", "PNT resilience", "commercial constellation policy"],
        "ko_signals": ["위성 장애", "우주잔해 경보", "PNT 복원력", "상업위성 정책"],
        "sources": ["nato_space", "cisa_infra", "unctad_rmt"],
        "tags": ["Space Security", "Satellites", "Infrastructure", "Defense"],
    },
    {
        "slug": "cyber-resilience-critical-infrastructure",
        "ko_title": "핵심 인프라 사이버 복원력: 해킹 뉴스가 생활 리스크가 되는 이유",
        "en_title": "Cyber Resilience for Critical Infrastructure: Why Hacking News Becomes Daily-Life Risk",
        "ko_summary": "CISA는 핵심 인프라를 전력, 통신, 물, 운송처럼 일상 기능을 지탱하는 시스템으로 본다. 사이버 리스크는 곧 서비스 중단 리스크다.",
        "en_summary": "CISA treats critical infrastructure as the systems that sustain daily functions such as power, communications, water, and transport. Cyber risk is service-continuity risk.",
        "ko_angle": "한국 독자는 랜섬웨어 뉴스를 기업 피해액보다 병원, 물류, 항만, 결제망의 복구시간 관점에서 읽어야 한다.",
        "en_angle": "Korean readers should read ransomware news through recovery time for hospitals, logistics, ports, and payment networks rather than victim count alone.",
        "signals": ["incident recovery time", "OT exposure", "backup testing", "supplier access controls"],
        "ko_signals": ["복구시간", "OT 노출", "백업 점검", "협력사 접근권한"],
        "sources": ["cisa_infra", "bis_annual", "nato_space"],
        "tags": ["Cybersecurity", "Critical Infrastructure", "Resilience", "Risk"],
    },
    {
        "slug": "election-disinformation-risk",
        "ko_title": "선거 허위정보와 AI: 민주주의 리스크를 읽는 실무 기준",
        "en_title": "Election Disinformation and AI: A Practical Standard for Reading Democratic Risk",
        "ko_summary": "AI 생성 콘텐츠가 늘수록 선거 리스크는 가짜뉴스 여부를 넘어 출처 확인, 배포 속도, 플랫폼 대응, 신뢰 회복 비용의 문제로 커진다.",
        "en_summary": "As AI-generated content spreads, election risk moves beyond fact-checking into source verification, distribution speed, platform response, and trust-repair costs.",
        "ko_angle": "한국 선거에서도 딥페이크, 여론조사 해석, 해외 플랫폼 확산, 언론 신뢰가 동시에 움직이므로 검증 루틴이 필요하다.",
        "en_angle": "Korean elections also need verification routines because deepfakes, polling narratives, foreign platforms, and media trust interact.",
        "signals": ["content provenance", "platform takedown speed", "official election notices", "cross-border amplification"],
        "ko_signals": ["콘텐츠 출처", "플랫폼 삭제 속도", "선관위 공지", "국경간 확산"],
        "sources": ["cisa_infra", "bis_annual", "un_population"],
        "tags": ["Disinformation", "AI", "Elections", "Democracy"],
    },
    {
        "slug": "korea-export-exposure-global-fragmentation",
        "ko_title": "한국 수출과 세계 분절화: 반도체 호황 뒤에 남는 취약점",
        "en_title": "Korea's Export Exposure to Global Fragmentation: Vulnerabilities Behind the Semiconductor Boom",
        "ko_summary": "MOTIR의 2026년 3월 수출 자료는 반도체 호황의 힘을 보여주지만, 동시에 에너지·물류·보호무역 리스크가 수출 불확실성을 키운다는 점도 드러낸다.",
        "en_summary": "Korea's March 2026 export release shows the strength of the semiconductor boom, but also the way energy, logistics, and protectionism raise export uncertainty.",
        "ko_angle": "한국 독자는 수출 총액보다 반도체 집중도, 지역별 수요, 중동 물류 리스크, 원화 환율을 함께 봐야 한다.",
        "en_angle": "Korean readers should track semiconductor concentration, regional demand, Middle East logistics risk, and the won exchange rate together.",
        "signals": ["semiconductor export share", "China and US demand", "Middle East route disruption", "KRW exchange rate"],
        "ko_signals": ["반도체 수출 비중", "중국·미국 수요", "중동 항로 차질", "원화 환율"],
        "sources": ["motir_exports", "kdi_outlook", "wto_trade"],
        "tags": ["Korea", "Exports", "Semiconductors", "Trade"],
    },
    {
        "slug": "household-cost-global-issue-link",
        "ko_title": "생활비와 세계정세 연결법: 유가·환율·식품가격을 한 번에 보기",
        "en_title": "Linking Household Costs to Global Affairs: Oil, FX, and Food Prices in One View",
        "ko_summary": "세계정세는 추상적 뉴스가 아니라 유가, 환율, 식품 가격, 전기요금, 보험료를 통해 가계부에 들어온다.",
        "en_summary": "Global affairs enter household budgets through oil, exchange rates, food prices, electricity bills, and insurance premiums.",
        "ko_angle": "한국 가계는 원달러 환율, 국제유가, 식품 CPI, 전기·가스 요금 조정 시점을 월별로 묶어 보는 습관이 필요하다.",
        "en_angle": "Korean households benefit from a monthly view that links USD/KRW, global oil, food CPI, and electricity and gas tariff decisions.",
        "signals": ["oil and gas prices", "USD/KRW", "food CPI", "utility tariff schedules"],
        "ko_signals": ["유가·가스 가격", "원달러 환율", "식품 CPI", "공공요금 조정"],
        "sources": ["oecd_outlook", "fao_sofi", "wmo_2025"],
        "tags": ["Household Costs", "Inflation", "FX", "Energy"],
    },
    {
        "slug": "global-affairs-reading-system",
        "ko_title": "세계정세 읽기 시스템: 헤드라인보다 먼저 볼 5개의 축",
        "en_title": "A Global Affairs Reading System: Five Axes to Check Before the Headline",
        "ko_summary": "세계정세를 꾸준히 읽으려면 사건을 외우기보다 성장, 에너지, 무역, 금융, 사회안정이라는 5개 축으로 분류하는 습관이 필요하다.",
        "en_summary": "To read global affairs consistently, classify events across growth, energy, trade, finance, and social stability instead of memorizing headlines.",
        "ko_angle": "한국 독자는 각 축을 수출, 환율, 물가, 안보, 고용으로 번역하면 국내 뉴스와 해외 뉴스를 같은 표에서 비교할 수 있다.",
        "en_angle": "Korean readers can translate the five axes into exports, FX, prices, security, and jobs to compare domestic and international news in one table.",
        "signals": ["growth shock", "energy shock", "trade shock", "funding shock", "social stability shock"],
        "ko_signals": ["성장 충격", "에너지 충격", "무역 충격", "자금 충격", "사회안정 충격"],
        "sources": ["imf_weo", "iea_weo", "wto_trade", "bis_annual"],
        "tags": ["Global Affairs", "Reading System", "Risk", "Strategy"],
    },
]


def escape_svg_text(value: str) -> str:
    return html.escape(value, quote=True)


def write_svg(path: Path, title: str, subtitle: str, labels: list[str], palette: tuple[str, str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    label_lines = "\n".join(
        f'<text x="88" y="{330 + index * 42}" fill="#f8fafc" font-size="24" font-family="Georgia, serif">{escape_svg_text(label)}</text>'
        for index, label in enumerate(labels[:5])
    )
    circles = "\n".join(
        f'<circle cx="{760 + index * 74}" cy="{168 + (index % 2) * 54}" r="{32 + index * 3}" fill="#ffffff" fill-opacity="{0.12 + index * 0.03:.2f}"/>'
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
    <pattern id="grid" width="60" height="60" patternUnits="userSpaceOnUse">
      <path d="M 60 0 L 0 0 0 60" fill="none" stroke="#ffffff" stroke-opacity="0.10" stroke-width="1"/>
    </pattern>
  </defs>
  <rect width="1200" height="675" fill="url(#bg)"/>
  <rect width="1200" height="675" fill="url(#grid)"/>
  <path d="M80 520 C260 410 370 450 530 330 C670 225 760 280 910 155 C1030 55 1120 100 1190 56" fill="none" stroke="#facc15" stroke-width="10" stroke-linecap="round" opacity="0.88"/>
  <path d="M0 600 C210 540 330 650 510 570 C725 470 850 660 1200 500 L1200 675 L0 675 Z" fill="#020617" fill-opacity="0.34"/>
  {circles}
  <text x="72" y="110" fill="#f8fafc" font-size="48" font-family="Georgia, serif" font-weight="700">{escape_svg_text(title)}</text>
  <text x="76" y="164" fill="#e2e8f0" font-size="26" font-family="Georgia, serif">{escape_svg_text(subtitle)}</text>
  <rect x="66" y="278" width="520" height="244" rx="26" fill="#020617" fill-opacity="0.36" stroke="#ffffff" stroke-opacity="0.20"/>
  {label_lines}
  <text x="76" y="610" fill="#cbd5e1" font-size="22" font-family="Georgia, serif">MouseBall54 Global Affairs Briefing</text>
</svg>
"""
    path.write_text(svg, encoding="utf-8")


def yaml_list(items: list[str]) -> str:
    return "\n".join(f"  - {item}" for item in items)


def normalize_markdown(text: str) -> str:
    """Remove template indentation while preserving Markdown list indentation."""
    normalized = "\n".join(line[4:] if line.startswith("    ") else line for line in text.splitlines()).lstrip()
    return normalized.replace("sidebar:\nnav:", "sidebar:\n    nav:") + "\n"


def source_notes(source_keys: list[str], lang: str) -> str:
    items = []
    for key in source_keys:
        source = SOURCES[key]
        items.append(f"- [{source[lang]}]({source['url']})")
    return "\n".join(items)


def related_links(index: int, lang: str) -> str:
    current = TOPICS[index]
    related = [TOPICS[(index + 1) % len(TOPICS)], TOPICS[(index + 7) % len(TOPICS)]]
    category_path = KO_CATEGORY.lower() if lang == "ko" else EN_CATEGORY.lower()
    if lang == "ko":
        return "\n".join(f"- [{topic['ko_title']}](/{{category}}/{topic['slug']}/)".replace("{category}", category_path) for topic in related)
    return "\n".join(f"- [{topic['en_title']}](/{{category}}/{topic['slug']}/)".replace("{category}", category_path) for topic in related)


def ko_post(topic: dict[str, object], index: int) -> str:
    slug = str(topic["slug"])
    image_dir = f"/images/{POST_DATE}-{slug}"
    signals = topic["ko_signals"]
    signal_items = "\n".join(f"- **{signal}**: 숫자 자체보다 전월 대비 방향, 정책 반응, 시장 가격 반영 여부를 함께 확인합니다." for signal in signals)
    checklist = "\n".join(f"- **{signal}** 신호가 악화될 때 한국 수출, 물가, 환율 중 어느 경로가 먼저 움직이는지 기록합니다." for signal in signals[:3])
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
    translation_id: global-affairs-{slug}
    header:
      teaser: {image_dir}/hero.svg
      overlay_image: {image_dir}/hero.svg
      overlay_filter: 0.45
      image_description: >
        {topic["ko_title"]}의 핵심 신호와 한국 경제 연결 경로를 요약한 세계정세 브리핑 이미지입니다.
    excerpt: >
      {topic["ko_summary"]}
    seo_description: >
      {topic["ko_summary"]}
    categories:
      - {KO_CATEGORY}
    tags:
    {yaml_list(topic["tags"])}
    ---

    세계정세는 멀리 있는 뉴스처럼 보이지만 실제로는 **수출 주문, 환율, 유가, 식품 가격, 전기요금, 안보 비용**으로 번역되어 생활과 기업 실적에 들어옵니다.

    {topic["ko_summary"]}

    이 글은 한 가지 결론을 강하게 주장하기보다, 독자가 다음 뉴스를 볼 때 무엇을 먼저 확인해야 하는지 정리하는 실전형 브리핑입니다.

    ![{topic["ko_title"]} 핵심 흐름 요약]({image_dir}/hero.svg)

    ## 왜 지금 중요한가

    {topic["ko_angle"]}

    2026년의 세계정세는 사건 하나가 한 분야에만 머물지 않는다는 점이 특징입니다. 에너지 충격은 물가와 무역수지를 흔들고, 무역 분절화는 투자와 고용으로 번지며, 금융시장의 불안은 다시 정책 여력을 줄입니다.

    그래서 이 주제는 단순히 “좋다” 또는 “나쁘다”로 읽으면 안 됩니다. **충격의 방향, 지속 기간, 한국으로 전달되는 경로**를 나누어야 합니다. 같은 뉴스라도 단기 가격 충격인지, 공급망 구조 변화인지, 제도 변화인지에 따라 대응이 완전히 달라집니다.

    ## 핵심 신호

    {signal_items}

    위 신호는 단독으로 해석하지 않는 편이 좋습니다. 예를 들어 가격이 오르더라도 재고가 충분하면 충격은 짧을 수 있고, 반대로 가격이 안정되어도 수출통제나 보험료가 올라가면 기업 비용은 늦게 상승할 수 있습니다.

    ![{topic["ko_title"]} 신호 점검표]({image_dir}/signal-map.svg)

    ## 한국 독자 관점

    한국 경제는 반도체, 자동차, 배터리, 정유·석화, 해운, 금융시장이 세계 흐름에 깊게 연결되어 있습니다. 따라서 국내 뉴스만 보아서는 원인을 놓치기 쉽습니다.

    {topic["ko_angle"]}

    개인 독자라면 이 주제를 가계부의 고정비와 변동비로 번역해 볼 수 있습니다. 기업 독자라면 매출보다 먼저 원가, 납기, 환헤지, 고객 지역 노출도를 확인해야 합니다. 정책 뉴스라면 목표보다 집행 속도와 재원 조달 방식을 봐야 합니다.

    ## 다음 뉴스를 읽는 순서

    1. 먼저 이슈가 **가격 충격**인지 **물량 충격**인지 구분합니다.
    2. 그다음 충격이 하루짜리 뉴스인지, 분기 단위로 이어질 구조 변화인지 확인합니다.
    3. 마지막으로 한국에 들어오는 경로를 수출, 수입물가, 금융시장, 안보비용, 생활비 중 하나로 표시합니다.

    ## 독자 체크리스트

    {checklist}
    - 같은 사안을 다루는 공식 통계와 민간 해설을 분리해서 읽습니다.
    - 헤드라인보다 발표 날짜, 기준 시점, 전망의 전제 조건을 먼저 확인합니다.

    ## 참고할 공식 자료

    {source_notes(topic["sources"], "ko")}

    ## 함께 보면 좋은 글

    {related_links(index, "ko")}
    """)


def en_post(topic: dict[str, object], index: int) -> str:
    slug = str(topic["slug"])
    image_dir = f"/images/{POST_DATE}-{slug}"
    signals = topic["signals"]
    signal_items = "\n".join(f"- **{signal}**: watch the direction, policy response, and market pricing rather than the number alone." for signal in signals)
    checklist = "\n".join(f"- Track whether {signal} first affects exports, prices, funding, or public budgets." for signal in signals[:3])
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
    translation_id: global-affairs-{slug}
    header:
      teaser: {image_dir}/hero.svg
      overlay_image: {image_dir}/hero.svg
      overlay_filter: 0.45
      image_description: >
        A global affairs briefing image showing core signals and Korea-facing transmission channels for this issue.
    excerpt: >
      {topic["en_summary"]}
    seo_description: >
      {topic["en_summary"]}
    categories:
      - {EN_CATEGORY}
    tags:
    {yaml_list(topic["tags"])}
    ---

    Global affairs often looks abstract until it shows up in **export orders, exchange rates, oil prices, food costs, power bills, insurance premiums, and security budgets**.

    {topic["en_summary"]}

    This briefing does not try to turn a complex issue into one strong prediction. It gives readers a practical order for reading the next update without being pulled around by every headline.

    ![{topic["en_title"]} core flow summary]({image_dir}/hero.svg)

    ## Why This Issue Matters

    {topic["en_angle"]}

    The defining feature of the 2026 global environment is that shocks rarely stay inside one category. Energy stress can move inflation and trade balances. Trade fragmentation can change investment and jobs. Financial volatility can reduce the room for fiscal support.

    That is why this issue should not be read as simply good or bad. The useful question is **direction, duration, and transmission**. A one-day price shock, a quarterly supply disruption, and a permanent rule change require different decisions.

    ## Current Signals To Watch

    {signal_items}

    These indicators should not be read in isolation. A price can rise while inventories absorb the shock. A price can look stable while export controls, insurance costs, or compliance burdens quietly raise corporate costs later.

    ![{topic["en_title"]} signal checklist]({image_dir}/signal-map.svg)

    ## Korea-Facing Angle

    Korea is deeply exposed through semiconductors, autos, batteries, refining and petrochemicals, shipping, and financial markets. Domestic news often carries an external cause that is easy to miss.

    {topic["en_angle"]}

    Household readers can translate the issue into fixed and variable costs. Business readers should check cost, delivery time, FX hedging, and customer-region exposure before looking only at revenue. Policy readers should ask how quickly the announced measure can be funded and implemented.

    ## How To Read The Next Update

    1. Decide whether the event is mainly a **price shock** or a **volume shock**.
    2. Check whether it is a short news cycle or a structural change that can last for quarters.
    3. Mark the Korea-facing channel: exports, import prices, financial markets, security costs, or household costs.

    ## Reader Checklist

    {checklist}
    - Separate official data from interpretation and commentary.
    - Check the release date, reference period, and assumptions before using any forecast.

    ## Source Notes

    {source_notes(topic["sources"], "en")}

    ## Related Reading

    {related_links(index, "en")}
    """)


def category_page(lang: str) -> str:
    if lang == "ko":
        return dedent("""\
        ---
        title: "Global Affairs"
        layout: archive
        permalink: /ko_global_affairs/
        lang: ko
        seo_description: >
          세계 성장, 무역 분절화, 에너지 안보, 핵심광물, 방위비, 기후 리스크, 이민, 한국 수출 노출도를 공식 자료 기반으로 읽는 한국어 세계정세 브리핑 모음입니다.
        sidebar:
            nav: "sidebar-category"
        ---

        Global Affairs 카테고리는 세계정세를 헤드라인 중심이 아니라 **성장, 에너지, 무역, 금융, 사회안정, 한국 연결 경로**로 나누어 읽기 위한 브리핑 모음입니다.

        각 글은 IMF, World Bank, WTO, OECD, IEA, SIPRI, UNHCR, WMO, UNEP, FAO, BIS, UNCTAD, KDI, MOTIR 같은 공식 자료를 우선 참고합니다. 목적은 단기 전망을 맞히는 것이 아니라, 다음 뉴스를 볼 때 어떤 지표와 경로를 먼저 확인해야 하는지 정리하는 것입니다.

        처음 읽는다면 세계 성장과 무역 분절화로 큰 지도를 잡고, 그다음 에너지·핵심광물·반도체 글로 한국 경제와의 연결을 확인하는 순서가 좋습니다. 생활비 관점이 필요하다면 식량안보와 가계비용 글을 함께 읽어 보세요.

        ## 먼저 읽기

        - [2026년 세계 성장 둔화와 분절화](/ko_global_affairs/global-growth-fragmentation-2026/)
        - [관세와 무역 분절화 리스크](/ko_global_affairs/trade-fragmentation-tariff-risk/)
        - [한국 수출과 세계 분절화](/ko_global_affairs/korea-export-exposure-global-fragmentation/)

        ## 최신 글

        {% assign posts = site.categories["ko_Global_Affairs"] %}
        {% for post in posts %}
          {% include archive-single.html type=page.entries_layout %}
        {% endfor %}
        """)
    return dedent("""\
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
    """)


def main() -> None:
    palettes = [
        ("#0f172a", "#0369a1"),
        ("#111827", "#b45309"),
        ("#172554", "#7c2d12"),
        ("#064e3b", "#1d4ed8"),
        ("#312e81", "#be123c"),
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
            "Signals, transmission channels, and Korea-facing exposure",
            list(topic["signals"]),
            palette,
        )
        write_svg(
            image_path / "signal-map.svg",
            "Signal Map",
            str(topic["en_title"])[:80],
            list(topic["signals"]),
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
