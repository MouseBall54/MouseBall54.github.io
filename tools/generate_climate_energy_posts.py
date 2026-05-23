#!/usr/bin/env python3
"""Generate paired Climate & Energy posts and local SVG context images."""

from __future__ import annotations

import html
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parents[1]
POST_DATE = "2026-05-18"
LAST_MODIFIED_AT = "2026-05-23T16:30:00+09:00"
KO_CATEGORY = "ko_Climate_Energy"
EN_CATEGORY = "en_Climate_Energy"


SOURCES = {
    "iea_ger2026": {
        "ko": "IEA Global Energy Review 2026",
        "en": "IEA Global Energy Review 2026",
        "url": "https://www.iea.org/reports/global-energy-review-2026/key-findings",
    },
    "iea_electricity2026": {
        "ko": "IEA Electricity 2026",
        "en": "IEA Electricity 2026",
        "url": "https://www.iea.org/reports/electricity-2026/executive-summary",
    },
    "iea_energy_ai": {
        "ko": "IEA Energy and AI",
        "en": "IEA Energy and AI",
        "url": "https://www.iea.org/reports/energy-and-ai/energy-supply-for-ai",
    },
    "iea_weo2025": {
        "ko": "IEA World Energy Outlook 2025",
        "en": "IEA World Energy Outlook 2025",
        "url": "https://www.iea.org/reports/world-energy-outlook-2025/executive-summary",
    },
    "iea_renewables2025": {
        "ko": "IEA Renewables 2025",
        "en": "IEA Renewables 2025",
        "url": "https://www.iea.org/reports/renewables-2025/renewable-electricity",
    },
    "iea_grids": {
        "ko": "IEA Electricity Grids and Secure Energy Transitions",
        "en": "IEA Electricity Grids and Secure Energy Transitions",
        "url": "https://www.iea.org/reports/electricity-grids-and-secure-energy-transitions",
    },
    "iea_ev2026": {
        "ko": "IEA Global EV Outlook 2026",
        "en": "IEA Global EV Outlook 2026",
        "url": "https://www.iea.org/reports/global-ev-outlook-2026/executive-summary",
    },
    "iea_minerals2025": {
        "ko": "IEA Global Critical Minerals Outlook 2025",
        "en": "IEA Global Critical Minerals Outlook 2025",
        "url": "https://www.iea.org/reports/global-critical-minerals-outlook-2025/overview-of-outlook-for-key-minerals",
    },
    "iea_batteries": {
        "ko": "IEA Batteries and Secure Energy Transitions",
        "en": "IEA Batteries and Secure Energy Transitions",
        "url": "https://www.iea.org/reports/batteries-and-secure-energy-transitions/outlook-for-battery-demand-and-supply",
    },
    "iea_hydrogen": {
        "ko": "IEA Hydrogen",
        "en": "IEA Hydrogen",
        "url": "https://www.iea.org/energy-system/low-emissions-fuels/hydrogen",
    },
    "iea_heat_pumps": {
        "ko": "IEA The Future of Heat Pumps",
        "en": "IEA The Future of Heat Pumps",
        "url": "https://www.iea.org/reports/the-future-of-heat-pumps/executive-summary",
    },
    "wmo_climate2025": {
        "ko": "WMO State of the Global Climate 2025",
        "en": "WMO State of the Global Climate 2025",
        "url": "https://wmo.int/publication-series/state-of-global-climate/state-of-global-climate-2025",
    },
    "ipcc_ar6": {
        "ko": "IPCC AR6 Synthesis Report",
        "en": "IPCC AR6 Synthesis Report",
        "url": "https://www.ipcc.ch/report/sixth-assessment-report-cycle/",
    },
    "unep_gap2025": {
        "ko": "UNEP Emissions Gap Report 2025",
        "en": "UNEP Emissions Gap Report 2025",
        "url": "https://www.unep.org/resources/emissions-gap-report-2025",
    },
    "unfccc_paris": {
        "ko": "UNFCCC Paris Agreement",
        "en": "UNFCCC Paris Agreement",
        "url": "https://unfccc.int/process-and-meetings/the-paris-agreement",
    },
    "world_bank_climate": {
        "ko": "World Bank Climate Change Overview",
        "en": "World Bank Climate Change Overview",
        "url": "https://www.worldbank.org/en/topic/climatechange/overview",
    },
    "world_bank_carbon": {
        "ko": "World Bank Carbon Pricing Dashboard",
        "en": "World Bank Carbon Pricing Dashboard",
        "url": "https://carbonpricingdashboard.worldbank.org/what-carbon-pricing",
    },
    "oecd_tax_environment": {
        "ko": "OECD Tax and the Environment",
        "en": "OECD Tax and the Environment",
        "url": "https://www.oecd.org/en/topics/policy-issues/tax-and-the-environment.html",
    },
    "eia_steo": {
        "ko": "U.S. EIA Short-Term Energy Outlook",
        "en": "U.S. EIA Short-Term Energy Outlook",
        "url": "https://www.eia.gov/steo",
    },
    "kea": {
        "ko": "Korea Energy Agency",
        "en": "Korea Energy Agency",
        "url": "https://www.energy.or.kr/en/conts/103001000000000.do",
    },
    "kesis": {
        "ko": "Korea Energy Statistical Information System",
        "en": "Korea Energy Statistical Information System",
        "url": "https://kesis.keei.re.kr/eng",
    },
    "korea_climate_assessment": {
        "ko": "한국기후위기평가보고서 2025",
        "en": "Korean Climate Crisis Assessment Report 2025",
        "url": "https://www.climate.go.kr/home/cc_data/2025/report_2025_2.pdf",
    },
    "kma_extreme2025": {
        "ko": "한국기후위기평가보고서 2025",
        "en": "Korean Climate Crisis Assessment Report 2025",
        "url": "https://www.climate.go.kr/home/cc_data/2025/report_2025_2.pdf",
    },
    "undrr_gar": {
        "ko": "UNDRR Global Assessment Report",
        "en": "UNDRR Global Assessment Report",
        "url": "https://www.undrr.org/gar",
    },
}


TOPICS = [
    {
        "slug": "ai-data-center-electricity-demand",
        "ko_title": "AI 데이터센터 전력 수요: 기술 뉴스가 전력망 뉴스가 되는 이유",
        "en_title": "AI Data-Center Electricity Demand: Why Tech News Is Becoming Grid News",
        "ko_summary": "AI 투자는 칩과 모델의 문제가 아니라 지역 전력망, 변전 설비, 냉각, 전력구매계약까지 묶인 인프라 경쟁으로 바뀌고 있다.",
        "en_summary": "AI investment is becoming an infrastructure race that links chips and models with local grids, substations, cooling, and power purchase agreements.",
        "ko_context": "IEA는 데이터센터 전력 수요가 빠르게 늘 수 있지만 충격은 세계 평균보다 특정 지역 전력망에 먼저 나타난다고 설명한다.",
        "en_context": "The IEA shows that data-centre electricity demand can rise quickly, but the first stress often appears in specific local grids rather than in global averages.",
        "ko_angle": "한국은 AI 반도체 공급자이면서 제조업 전력 수요가 큰 나라라서 데이터센터 입지는 전기요금, 송전망, 산업단지 경쟁력과 같이 읽어야 한다.",
        "en_angle": "Korea is both an AI semiconductor supplier and a power-intensive manufacturing economy, so data-centre siting should be read with tariffs, transmission, and industrial competitiveness.",
        "ko_actions": ["신규 데이터센터 발표를 전력망 접속 일정과 같이 확인합니다.", "전력구매계약이 실제 추가 전원인지 기존 전력 재배분인지 봅니다.", "냉각수와 지역 주민 수용성까지 비용으로 계산합니다."],
        "en_actions": ["Read new data-centre announcements with grid-connection timelines.", "Check whether power purchase agreements add new supply or reallocate existing power.", "Treat cooling water and community acceptance as real costs."],
        "ko_signals": ["전력망 접속 대기", "데이터센터 부하", "냉각수 확보", "전력구매계약"],
        "signals": ["grid connection queue", "data-centre load", "cooling water access", "power purchase agreement"],
        "sources": ["iea_energy_ai", "iea_electricity2026", "iea_ger2026"],
        "tags": ["AI", "Electricity", "Data Centers", "Grid"],
    },
    {
        "slug": "energy-security-oil-gas-shocks",
        "ko_title": "에너지 안보 읽기: 유가와 가스 가격 충격을 분리해서 보는 법",
        "en_title": "Reading Energy Security: Separate Oil and Gas Price Shocks",
        "ko_summary": "에너지 안보는 유가 한 줄이 아니라 원유, LNG, 전력, 환율, 재고, 지정학 리스크가 동시에 움직이는 복합 비용 문제다.",
        "en_summary": "Energy security is not one oil-price headline; it is a combined cost problem across crude oil, LNG, electricity, exchange rates, inventories, and geopolitical risk.",
        "ko_context": "IEA와 EIA 자료는 에너지 가격을 공급 충격, 수요 둔화, 재고, 운송 리스크로 나누어 봐야 한다는 점을 반복해서 보여준다.",
        "en_context": "IEA and EIA data repeatedly show that energy prices need to be separated into supply shocks, demand slowdown, inventories, and transport risk.",
        "ko_angle": "한국은 에너지 수입 의존도가 높아 원화 약세와 유가 상승이 겹치면 기업 원가와 가계 공공요금 논쟁이 동시에 커진다.",
        "en_angle": "Because Korea depends heavily on imported energy, a weaker won combined with higher fuel prices can hit corporate costs and household utility debates together.",
        "ko_actions": ["유가, LNG, 환율을 같은 표에 놓습니다.", "현물 가격과 장기계약 가격의 차이를 확인합니다.", "재고가 충격을 흡수하는지 가격만 움직이는지 구분합니다."],
        "en_actions": ["Put oil, LNG, and exchange rates in one table.", "Separate spot prices from long-term contract prices.", "Check whether inventories absorb the shock or prices do all the adjustment."],
        "ko_signals": ["브렌트·두바이유", "LNG 현물가", "원달러 환율", "상업 재고"],
        "signals": ["Brent and Dubai crude", "LNG spot price", "KRW/USD exchange rate", "commercial inventories"],
        "sources": ["iea_weo2025", "eia_steo", "iea_ger2026"],
        "tags": ["Energy Security", "Oil", "Natural Gas", "Inflation"],
    },
    {
        "slug": "power-grid-bottlenecks-transition",
        "ko_title": "에너지 전환의 병목은 발전량만이 아니라 전력망이다",
        "en_title": "The Energy Transition Bottleneck Is the Grid, Not Only Generation",
        "ko_summary": "재생에너지와 전기화가 늘어날수록 전력망 투자, 계통 접속, 변압기 공급, 지역 수용성이 전환 속도를 좌우한다.",
        "en_summary": "As renewables and electrification grow, grid investment, connection queues, transformer supply, and local acceptance can determine the real transition speed.",
        "ko_context": "IEA는 전력망 투자가 발전 설비 증가를 따라가지 못하면 청정전력 확대가 오히려 병목에 막힐 수 있다고 경고한다.",
        "en_context": "The IEA warns that clean-power growth can become constrained if grid investment fails to keep up with generation additions.",
        "ko_angle": "국내에서는 태양광 확대 논쟁을 발전 설비 숫자만으로 볼 것이 아니라 송전선, 배전망, 계통 안정화 비용까지 포함해야 한다.",
        "en_angle": "In Korea, solar expansion debates need to include transmission, distribution, and system-stability costs rather than only generation capacity.",
        "ko_actions": ["신규 발전량보다 계통 접속 가능 용량을 먼저 봅니다.", "송전선 건설 기간과 주민 수용성을 일정표에 넣습니다.", "저장장치와 수요반응이 병목을 얼마나 줄이는지 확인합니다."],
        "en_actions": ["Check available grid capacity before new generation capacity.", "Include transmission build time and community acceptance in the timeline.", "Estimate how storage and demand response reduce bottlenecks."],
        "ko_signals": ["계통 접속 대기", "송전망 투자", "변압기 공급", "출력제어"],
        "signals": ["connection queue", "transmission investment", "transformer supply", "curtailment"],
        "sources": ["iea_grids", "iea_electricity2026", "kesis"],
        "tags": ["Grid", "Renewables", "Electricity", "Infrastructure"],
    },
    {
        "slug": "renewables-growth-forecast-2030",
        "ko_title": "재생에너지 2030 전망: 설치량보다 계통 흡수 능력을 같이 보기",
        "en_title": "Renewables to 2030: Installed Capacity Is Not the Whole Story",
        "ko_summary": "태양광과 풍력 증가는 전력 생산비를 낮출 수 있지만 허가, 계통, 저장, 시장 설계가 따라오지 않으면 실제 활용률이 떨어진다.",
        "en_summary": "Solar and wind growth can lower power costs, but utilization falls if permitting, grids, storage, and market design do not keep pace.",
        "ko_context": "IEA Renewables 전망은 재생에너지 설치가 계속 늘지만 정책·규제·시장 변화에 따라 지역별 속도가 크게 달라진다고 설명한다.",
        "en_context": "IEA Renewables analysis shows renewable additions keep rising, but policy, regulatory, and market changes can sharply change regional speed.",
        "ko_angle": "한국 독자는 재생에너지 비중을 찬반 구도로만 보기보다 계통 보강과 전력시장 제도까지 한 세트로 봐야 한다.",
        "en_angle": "Korean readers should treat renewables, grid reinforcement, and power-market rules as one package rather than a simple pro-or-con debate.",
        "ko_actions": ["설치용량과 발전량을 구분합니다.", "허가 기간과 지역별 계통 여유를 확인합니다.", "저장장치와 유연성 자원의 확산 속도를 봅니다."],
        "en_actions": ["Separate installed capacity from actual generation.", "Check permitting timelines and regional grid headroom.", "Track the pace of storage and flexibility resources."],
        "ko_signals": ["설치용량", "실제 발전량", "허가 지연", "저장장치 보급"],
        "signals": ["installed capacity", "actual generation", "permitting delay", "storage deployment"],
        "sources": ["iea_renewables2025", "iea_grids", "iea_batteries"],
        "tags": ["Renewables", "Solar", "Wind", "Grid"],
    },
    {
        "slug": "solar-pv-curtailment-grid",
        "ko_title": "태양광 출력제어: 전기가 남는 문제가 아니라 전력망이 막히는 문제",
        "en_title": "Solar Curtailment: Not Too Much Power, but Power in the Wrong Place",
        "ko_summary": "태양광 출력제어는 재생에너지가 쓸모없다는 뜻이 아니라 시간, 장소, 수요, 전력망이 맞지 않을 때 생기는 운영 신호다.",
        "en_summary": "Solar curtailment does not mean renewables are useless; it is an operating signal that timing, location, demand, and grids are mismatched.",
        "ko_context": "전력망 보고서들은 출력제어를 발전량 확대 실패가 아니라 계통 보강, 저장, 수요 이동이 필요한 신호로 해석한다.",
        "en_context": "Grid-focused reports interpret curtailment as a signal for reinforcement, storage, and load shifting rather than as proof that added generation failed.",
        "ko_angle": "한국의 지역별 태양광 확대는 낮 시간 산업 수요, 배전망 여유, ESS, 장거리 송전 계획과 함께 읽어야 한다.",
        "en_angle": "Korea's regional solar expansion should be read with daytime industrial load, distribution capacity, batteries, and long-distance transmission plans.",
        "ko_actions": ["출력제어율을 계절별·시간대별로 나눕니다.", "발전소 위치와 수요지 거리를 봅니다.", "저장장치와 수요반응이 같은 지역에 있는지 확인합니다."],
        "en_actions": ["Break curtailment by season and time of day.", "Compare project location with demand centres.", "Check whether storage and demand response are in the same region."],
        "ko_signals": ["출력제어율", "낮 시간 수요", "배전망 여유", "ESS 입지"],
        "signals": ["curtailment rate", "daytime demand", "distribution headroom", "battery siting"],
        "sources": ["iea_renewables2025", "iea_grids", "kesis"],
        "tags": ["Solar", "Curtailment", "Grid", "Storage"],
    },
    {
        "slug": "offshore-wind-supply-chain",
        "ko_title": "해상풍력 공급망: 터빈보다 항만, 선박, 전력망을 먼저 보기",
        "en_title": "Offshore Wind Supply Chains: Ports, Vessels, and Grids Before Turbines",
        "ko_summary": "해상풍력 프로젝트는 터빈 기술만으로 움직이지 않고 항만, 설치선, 해저케이블, 주민 수용성, 전력망 접속이 함께 맞아야 진행된다.",
        "en_summary": "Offshore wind projects do not move on turbine technology alone; ports, installation vessels, subsea cables, local acceptance, and grid connections all matter.",
        "ko_context": "재생에너지 전망에서 해상풍력은 비용과 공급망 제약이 크게 드러나는 분야로, 정책 발표와 실제 준공 사이의 간격이 길다.",
        "en_context": "Renewables outlooks show offshore wind is exposed to cost and supply-chain constraints, creating long gaps between policy announcements and completion.",
        "ko_angle": "한국은 조선·철강·전력기기 강점이 있지만 인허가와 계통 접속이 늦으면 산업 기회가 실제 발전량으로 이어지기 어렵다.",
        "en_angle": "Korea has strengths in shipbuilding, steel, and electrical equipment, but slow permitting or grid connection can prevent industrial opportunity from becoming generation.",
        "ko_actions": ["터빈 수주보다 항만·설치선 확보를 봅니다.", "해저케이블과 변전 설비 납기를 확인합니다.", "어업·지역사회 협의 일정을 프로젝트 리스크로 봅니다."],
        "en_actions": ["Read ports and installation-vessel availability before turbine orders.", "Check subsea cable and substation delivery times.", "Treat fisheries and local consultation as project risk."],
        "ko_signals": ["설치선", "해저케이블", "항만 인프라", "지역 협의"],
        "signals": ["installation vessels", "subsea cables", "port infrastructure", "local consultation"],
        "sources": ["iea_renewables2025", "iea_grids", "kea"],
        "tags": ["Offshore Wind", "Supply Chains", "Renewables", "Korea"],
    },
    {
        "slug": "battery-storage-flexibility",
        "ko_title": "배터리 저장장치의 역할: 발전소가 아니라 전력망 유연성으로 보기",
        "en_title": "Battery Storage: Read It as Grid Flexibility, Not Just Generation",
        "ko_summary": "배터리 저장장치는 전기를 새로 만드는 설비가 아니라 피크 시간 이동, 재생에너지 변동성 완화, 주파수 안정에 쓰이는 유연성 자산이다.",
        "en_summary": "Battery storage does not create electricity; it shifts peak load, smooths renewable variability, and supports frequency stability as a flexibility asset.",
        "ko_context": "IEA 배터리 보고서는 저장장치가 전기차뿐 아니라 전력망의 안정성과 재생에너지 확대에 중요한 역할을 한다고 설명한다.",
        "en_context": "IEA battery analysis frames storage as important not only for EVs but also for grid stability and renewable integration.",
        "ko_angle": "한국에서는 ESS를 단순 보조금 품목이 아니라 전력망 투자 지연을 줄이고 산업단지 전력 품질을 지키는 자산으로 봐야 한다.",
        "en_angle": "In Korea, ESS should be read not only as a subsidy item but as an asset that can reduce grid delays and support industrial power quality.",
        "ko_actions": ["저장시간, 출력, 용도를 분리해 봅니다.", "피크 절감인지 재생에너지 연계인지 목적을 확인합니다.", "화재 안전과 운영 데이터 공개 수준을 점검합니다."],
        "en_actions": ["Separate duration, power rating, and use case.", "Check whether the goal is peak reduction or renewable integration.", "Review safety standards and operating-data transparency."],
        "ko_signals": ["저장시간", "피크 부하", "주파수 안정", "ESS 안전"],
        "signals": ["storage duration", "peak load", "frequency stability", "battery safety"],
        "sources": ["iea_batteries", "iea_grids", "kea"],
        "tags": ["Battery Storage", "Grid", "Renewables", "Flexibility"],
    },
    {
        "slug": "critical-minerals-refining-risk",
        "ko_title": "핵심광물 정제 리스크: 매장량보다 가공 집중도를 먼저 보기",
        "en_title": "Critical Minerals Refining Risk: Processing Concentration Before Reserves",
        "ko_summary": "핵심광물 리스크는 광산 매장량만이 아니라 정제·가공 시설이 어디에 집중되어 있는지, 수출통제가 어디서 나오는지에 달려 있다.",
        "en_summary": "Critical-minerals risk depends not only on mine reserves but also on where refining and processing are concentrated and where export controls emerge.",
        "ko_context": "IEA 핵심광물 전망은 배터리, 전력망, 전기차, 첨단 제조업에서 광물 수요가 늘며 정제 집중도가 안보 문제가 된다고 본다.",
        "en_context": "IEA critical-minerals analysis shows rising demand from batteries, grids, EVs, and advanced manufacturing, making refining concentration a security issue.",
        "ko_angle": "한국 배터리와 반도체 산업은 원재료 가격보다 특정 정제국 의존도와 우회 조달 가능성을 먼저 따져야 한다.",
        "en_angle": "Korea's battery and semiconductor sectors need to examine refining dependence and alternative procurement before looking only at raw material prices.",
        "ko_actions": ["채굴국과 정제국을 분리해 봅니다.", "수출통제와 관세 규칙을 공급망 지도에 표시합니다.", "재활용과 장기계약이 리스크를 얼마나 줄이는지 확인합니다."],
        "en_actions": ["Separate mining countries from refining countries.", "Map export controls and tariff rules onto the supply chain.", "Check how much recycling and long-term contracts reduce risk."],
        "ko_signals": ["정제 집중도", "수출통제", "장기계약", "재활용 물량"],
        "signals": ["refining concentration", "export controls", "long-term contracts", "recycling volumes"],
        "sources": ["iea_minerals2025", "iea_batteries", "iea_weo2025"],
        "tags": ["Critical Minerals", "Batteries", "Supply Chains", "Security"],
    },
    {
        "slug": "ev-market-shift-2026",
        "ko_title": "2026 전기차 시장 읽기: 성장 둔화 뉴스와 구조적 전환을 구분하기",
        "en_title": "Reading the 2026 EV Market: Separate Slowdowns from Structural Change",
        "ko_summary": "전기차 시장은 국가별 보조금, 가격, 충전 인프라, 중국 수출, 중고차 가치가 달라서 한 지역 둔화로 전체 전환을 판단하기 어렵다.",
        "en_summary": "EV markets vary by subsidies, prices, charging, Chinese exports, and used-car values, so one regional slowdown does not explain the entire transition.",
        "ko_context": "IEA Global EV Outlook 2026은 2025년 전기차 판매가 기록을 경신했지만 지역별 속도와 정책 민감도가 크게 다르다고 설명한다.",
        "en_context": "IEA Global EV Outlook 2026 shows EV sales reached a new high in 2025, while regional speeds and policy sensitivity remain very different.",
        "ko_angle": "한국 기업은 완성차 판매량뿐 아니라 배터리 판가, 중국 수출, 미국·유럽 정책 변화, 충전 인프라 투자를 함께 봐야 한다.",
        "en_angle": "Korean companies need to track not only EV sales but also battery prices, Chinese exports, US and European policies, and charging investment.",
        "ko_actions": ["판매대수와 판매비중을 구분합니다.", "보조금 종료와 가격 인하 효과를 따로 봅니다.", "중고 전기차 가격이 신규 수요에 주는 영향을 확인합니다."],
        "en_actions": ["Separate unit sales from sales share.", "Read subsidy changes separately from price cuts.", "Check how used-EV values affect new demand."],
        "ko_signals": ["판매비중", "보조금 변화", "중고차 가격", "충전 인프라"],
        "signals": ["sales share", "subsidy change", "used-car prices", "charging infrastructure"],
        "sources": ["iea_ev2026", "iea_batteries", "iea_ger2026"],
        "tags": ["Electric Vehicles", "Batteries", "Autos", "Energy"],
    },
    {
        "slug": "ev-charging-grid-load",
        "ko_title": "전기차 충전과 전력망: 충전기 숫자보다 피크 부하를 보기",
        "en_title": "EV Charging and the Grid: Peak Load Before Charger Counts",
        "ko_summary": "전기차 충전 문제는 충전기 대수만으로 해결되지 않으며 언제, 어디서, 얼마나 빠르게 충전하는지가 전력망 부담을 결정한다.",
        "en_summary": "EV charging cannot be judged by charger counts alone; when, where, and how fast vehicles charge determines the grid burden.",
        "ko_context": "IEA EV 전망은 전기차 전력 수요가 커져도 스마트충전과 V2G가 피크 부하를 줄일 수 있는 중요한 유연성 도구라고 본다.",
        "en_context": "IEA EV analysis notes that smart charging and V2G can reduce peak-load pressure as EV electricity demand grows.",
        "ko_angle": "한국 아파트·고속도로·물류차고지는 충전 수요의 시간대가 달라서 같은 충전기라도 전력망 영향이 다르게 나타난다.",
        "en_angle": "Korean apartments, highways, and logistics depots have different charging time profiles, so identical charger counts can create different grid impacts.",
        "ko_actions": ["충전기 대수와 최대출력을 분리합니다.", "퇴근 후 피크 충전과 심야 충전을 구분합니다.", "전기트럭 충전은 승용차 충전과 별도로 봅니다."],
        "en_actions": ["Separate charger count from maximum power.", "Distinguish evening peak charging from overnight charging.", "Read electric-truck charging separately from passenger cars."],
        "ko_signals": ["급속충전 출력", "피크 시간대", "스마트충전", "전기트럭 차고지"],
        "signals": ["fast-charger power", "peak hours", "smart charging", "truck depots"],
        "sources": ["iea_ev2026", "iea_electricity2026", "iea_grids"],
        "tags": ["EV Charging", "Grid", "Electric Vehicles", "Demand"],
    },
    {
        "slug": "heat-pumps-building-efficiency",
        "ko_title": "히트펌프와 건물 효율: 냉난방비를 줄이는 전기화의 조건",
        "en_title": "Heat Pumps and Building Efficiency: Conditions for Lower Heating and Cooling Costs",
        "ko_summary": "히트펌프는 냉난방 전기화를 이끌 수 있지만 단열, 피크 전력, 설치 품질, 전기요금 구조가 맞아야 비용 절감 효과가 커진다.",
        "en_summary": "Heat pumps can support building electrification, but insulation, peak power, installation quality, and tariff design shape the cost benefit.",
        "ko_context": "IEA 히트펌프 보고서는 건물 효율 개선과 히트펌프 보급을 함께 봐야 피크 전력 증가와 소비자 비용을 줄일 수 있다고 설명한다.",
        "en_context": "IEA heat-pump analysis shows that building efficiency and heat-pump deployment need to move together to reduce peak growth and consumer costs.",
        "ko_angle": "한국의 아파트와 상업건물은 냉방 피크가 중요하므로 난방 전환만이 아니라 여름 전력망 부담까지 같이 계산해야 한다.",
        "en_angle": "For Korea's apartments and commercial buildings, cooling peaks matter, so heating electrification must be considered with summer grid stress.",
        "ko_actions": ["기기 효율보다 단열 상태를 먼저 확인합니다.", "전기요금 시간대와 피크 수요를 계산합니다.", "설치 품질과 유지보수 계획을 비용에 포함합니다."],
        "en_actions": ["Check insulation before equipment efficiency.", "Calculate time-of-use tariffs and peak demand.", "Include installation quality and maintenance in the cost view."],
        "ko_signals": ["단열 등급", "냉난방 피크", "전기요금 구조", "설치 품질"],
        "signals": ["insulation rating", "heating and cooling peak", "tariff design", "installation quality"],
        "sources": ["iea_heat_pumps", "iea_electricity2026", "kea"],
        "tags": ["Heat Pumps", "Buildings", "Efficiency", "Electricity"],
    },
    {
        "slug": "industrial-electrification-heat",
        "ko_title": "산업 전기화와 공정열: 모든 열을 전기로 바꿀 수는 없다",
        "en_title": "Industrial Electrification and Process Heat: Not Every Heat Load Is Equal",
        "ko_summary": "산업 전기화는 저온 열과 고온 공정, 연속 생산, 전력 품질, 설비 교체 주기가 달라서 업종별로 다른 속도로 진행된다.",
        "en_summary": "Industrial electrification moves at different speeds because low-temperature heat, high-temperature processes, continuous production, power quality, and replacement cycles differ by sector.",
        "ko_context": "IEA 전력 수요 전망은 산업 전기화가 전력 수요 증가의 핵심 축이지만 실제 전환은 공정별 경제성에 좌우된다고 설명한다.",
        "en_context": "IEA electricity outlooks frame industrial electrification as a major demand driver, but real adoption depends on process-level economics.",
        "ko_angle": "한국 제조업은 반도체, 철강, 화학, 배터리 공정마다 전력 품질과 열 수요가 달라 단일 전환 로드맵으로 보기 어렵다.",
        "en_angle": "Korea's semiconductors, steel, chemicals, and batteries each have different power-quality and heat requirements, so one transition roadmap is too simple.",
        "ko_actions": ["저온·중온·고온 공정을 나눕니다.", "설비 교체 주기와 전력계약을 함께 봅니다.", "정전 비용과 전력 품질 요구를 전환 비용에 넣습니다."],
        "en_actions": ["Separate low-, medium-, and high-temperature processes.", "Read equipment replacement cycles with power contracts.", "Include outage costs and power-quality requirements in transition cost."],
        "ko_signals": ["공정 온도", "설비 교체 주기", "전력 품질", "정전 비용"],
        "signals": ["process temperature", "replacement cycle", "power quality", "outage cost"],
        "sources": ["iea_electricity2026", "iea_ger2026", "kesis"],
        "tags": ["Industry", "Electrification", "Manufacturing", "Electricity"],
    },
    {
        "slug": "hydrogen-ammonia-realistic-use",
        "ko_title": "수소와 암모니아의 현실적 용도: 만능 연료보다 선택적 도구로 보기",
        "en_title": "Hydrogen and Ammonia: Read Them as Selective Tools, Not Universal Fuels",
        "ko_summary": "수소와 암모니아는 모든 에너지 문제의 답이 아니라 전기화가 어려운 산업, 장거리 운송, 저장, 일부 발전 보조 용도에서 먼저 검토해야 한다.",
        "en_summary": "Hydrogen and ammonia are not answers to every energy problem; they should first be tested in hard-to-electrify industry, long-distance transport, storage, and selected power uses.",
        "ko_context": "IEA는 저배출 수소가 성장하려면 수요 창출, 운송 인프라, 인증, 비용 격차 해소가 함께 필요하다고 설명한다.",
        "en_context": "The IEA notes that low-emissions hydrogen needs demand creation, transport infrastructure, certification, and cost-gap reduction to scale.",
        "ko_angle": "한국의 수소 논의는 발전 혼소 비율보다 수입 인프라, 안전 기준, 실제 감축 효과, 산업 수요처를 먼저 따져야 한다.",
        "en_angle": "Korea's hydrogen debate should examine import infrastructure, safety standards, actual emissions reduction, and industrial offtake before blending ratios alone.",
        "ko_actions": ["수소 생산 방식과 배출계수를 확인합니다.", "수요처가 장기 구매계약을 맺을 수 있는지 봅니다.", "암모니아 운송·저장 안전 기준을 검토합니다."],
        "en_actions": ["Check production pathway and emissions intensity.", "See whether offtakers can sign long-term contracts.", "Review ammonia transport and storage safety standards."],
        "ko_signals": ["저배출 인증", "구매계약", "운송 인프라", "안전 기준"],
        "signals": ["low-emissions certification", "offtake contract", "transport infrastructure", "safety standards"],
        "sources": ["iea_hydrogen", "iea_weo2025", "kea"],
        "tags": ["Hydrogen", "Ammonia", "Industry", "Energy Transition"],
    },
    {
        "slug": "nuclear-restart-new-build-debate",
        "ko_title": "원전 재가동과 신규 건설 논쟁: 전력 안정성과 시간표를 분리하기",
        "en_title": "Nuclear Restarts and New Builds: Separate Reliability from Timelines",
        "ko_summary": "원전 논쟁은 찬반 구호보다 기존 설비 이용률, 신규 건설 기간, 안전 규제, 폐기물, 전력망 위치를 분리해야 현실적으로 읽힌다.",
        "en_summary": "Nuclear debates become clearer when existing fleet availability, new-build timelines, safety regulation, waste, and grid location are separated from slogans.",
        "ko_context": "IEA 에너지 전망은 전력 수요 증가와 에너지 안보 논의 속에서 원전의 역할이 다시 커지고 있지만 시간표와 비용이 핵심 변수라고 본다.",
        "en_context": "IEA energy outlooks show nuclear returning to energy-security debates, but timelines and costs remain decisive variables.",
        "ko_angle": "한국에서는 원전과 재생에너지를 대체 관계로만 보지 말고 반도체·AI 전력 수요, 계통 위치, 노후 설비 관리와 함께 봐야 한다.",
        "en_angle": "In Korea, nuclear and renewables should not be read only as substitutes; semiconductor and AI demand, grid location, and ageing assets also matter.",
        "ko_actions": ["기존 원전 이용률과 신규 건설 일정을 분리합니다.", "안전 규제와 주민 수용성을 비용으로 봅니다.", "전력 수요 지역과 발전소 위치의 거리를 확인합니다."],
        "en_actions": ["Separate existing fleet availability from new-build schedules.", "Treat safety regulation and local acceptance as costs.", "Compare demand centres with plant locations."],
        "ko_signals": ["이용률", "건설 기간", "안전 규제", "폐기물 관리"],
        "signals": ["capacity factor", "construction timeline", "safety regulation", "waste management"],
        "sources": ["iea_weo2025", "iea_electricity2026", "kesis"],
        "tags": ["Nuclear", "Electricity", "Reliability", "Korea"],
    },
    {
        "slug": "coal-phase-down-reliability",
        "ko_title": "석탄 감축과 전력 신뢰도: 폐쇄 일정만 보면 놓치는 것들",
        "en_title": "Coal Phase-Down and Reliability: What Closure Dates Miss",
        "ko_summary": "석탄 감축은 배출을 줄이는 핵심 과제지만 폐쇄 일정, 대체 전원, 송전망, 지역 일자리, 전력예비율을 함께 맞춰야 한다.",
        "en_summary": "Coal phase-down is central to emissions reduction, but closure dates need to align with replacement supply, grids, local jobs, and reserve margins.",
        "ko_context": "IEA와 UNEP 자료는 배출 감축 속도를 높여야 하지만 전력 시스템 신뢰도를 지키는 전환 설계가 필요하다고 강조한다.",
        "en_context": "IEA and UNEP materials underline the need for faster emissions reduction while still designing transitions that protect electricity reliability.",
        "ko_angle": "한국은 석탄발전 감축을 전기요금, 지역경제, LNG 의존도, 재생에너지 접속 문제와 함께 봐야 사회적 비용을 줄일 수 있다.",
        "en_angle": "Korea can reduce social cost only if coal phase-down is read with tariffs, local economies, LNG dependence, and renewable grid connection.",
        "ko_actions": ["폐쇄 용량과 대체 가능 용량을 같은 단위로 비교합니다.", "지역 고용과 세수 영향을 확인합니다.", "전력예비율과 피크 수요를 함께 봅니다."],
        "en_actions": ["Compare retiring capacity with replaceable capacity in the same units.", "Check local employment and tax-base impacts.", "Read reserve margin together with peak demand."],
        "ko_signals": ["폐쇄 일정", "대체 전원", "전력예비율", "지역 일자리"],
        "signals": ["closure schedule", "replacement supply", "reserve margin", "local jobs"],
        "sources": ["unep_gap2025", "iea_electricity2026", "kesis"],
        "tags": ["Coal", "Reliability", "Emissions", "Electricity"],
    },
    {
        "slug": "lng-contracts-price-risk",
        "ko_title": "LNG 장기계약과 현물가격: 가스비 뉴스를 읽는 핵심 차이",
        "en_title": "LNG Long-Term Contracts and Spot Prices: The Key Difference in Gas News",
        "ko_summary": "LNG 가격 뉴스는 현물가격, 장기계약, 유가연동, 환율, 운송비가 섞여 있어 같은 가스라도 실제 구매 비용이 다르게 나타난다.",
        "en_summary": "LNG news blends spot prices, long-term contracts, oil-indexation, exchange rates, and shipping costs, so the same gas can imply different purchase costs.",
        "ko_context": "에너지 안보 자료들은 가스 시장이 가격뿐 아니라 계약 구조와 공급 경로에 따라 취약성이 달라진다는 점을 보여준다.",
        "en_context": "Energy-security sources show that gas-market vulnerability depends on contract structure and supply routes as much as on price.",
        "ko_angle": "한국은 LNG 발전과 도시가스가 모두 생활비와 산업비용에 연결되어 있어 현물 급등과 장기계약 평균 가격을 나눠 봐야 한다.",
        "en_angle": "Korea links LNG to power generation, city gas, household costs, and industrial costs, so spot spikes and average contract prices need separate treatment.",
        "ko_actions": ["현물가와 장기계약 가격을 분리합니다.", "유가연동 시차와 환율 효과를 확인합니다.", "저장률과 겨울 수요 전망을 같이 봅니다."],
        "en_actions": ["Separate spot prices from long-term contract prices.", "Check oil-indexation lag and exchange-rate effects.", "Read storage levels with winter demand forecasts."],
        "ko_signals": ["LNG 현물가", "유가연동", "환율", "가스 저장률"],
        "signals": ["LNG spot price", "oil indexation", "exchange rate", "gas storage"],
        "sources": ["eia_steo", "iea_weo2025", "kesis"],
        "tags": ["LNG", "Natural Gas", "Energy Security", "Prices"],
    },
    {
        "slug": "carbon-pricing-ets-basics",
        "ko_title": "탄소가격과 배출권거래제: 세금 논쟁 전에 원리를 이해하기",
        "en_title": "Carbon Pricing and Emissions Trading: Understand the Mechanism Before the Tax Debate",
        "ko_summary": "탄소가격은 배출 비용을 가격에 반영해 투자 방향을 바꾸는 정책 도구이며, 세금과 배출권거래제는 작동 방식이 다르다.",
        "en_summary": "Carbon pricing is a policy tool that reflects emissions costs in prices and investment decisions; carbon taxes and emissions trading work differently.",
        "ko_context": "World Bank와 OECD 자료는 탄소가격이 단독 정책이 아니라 보조금, 규제, 혁신 투자와 함께 설계되는 정책 패키지라고 설명한다.",
        "en_context": "World Bank and OECD materials describe carbon pricing as part of a policy package that works with subsidies, regulation, and innovation investment.",
        "ko_angle": "한국 기업은 배출권 가격만 보지 말고 무상할당, 전력 간접배출, 수출 경쟁력, 탄소국경조정까지 연결해서 봐야 한다.",
        "en_angle": "Korean companies should read allowance prices together with free allocation, indirect power emissions, export competitiveness, and carbon border rules.",
        "ko_actions": ["세금과 ETS의 차이를 먼저 정리합니다.", "가격 수준보다 적용 범위와 무상할당을 봅니다.", "전력요금과 수출 규정에 미치는 영향을 계산합니다."],
        "en_actions": ["Clarify the difference between taxes and ETS first.", "Read coverage and free allocation before the price level.", "Calculate effects on power bills and export rules."],
        "ko_signals": ["배출권 가격", "무상할당", "적용 범위", "탄소국경조정"],
        "signals": ["allowance price", "free allocation", "coverage", "carbon border adjustment"],
        "sources": ["world_bank_carbon", "oecd_tax_environment", "unfccc_paris"],
        "tags": ["Carbon Pricing", "ETS", "Climate Policy", "Trade"],
    },
    {
        "slug": "climate-disclosure-scope-emissions",
        "ko_title": "기후공시와 Scope 배출량: ESG 보고서에서 실제로 봐야 할 것",
        "en_title": "Climate Disclosure and Scope Emissions: What to Read in ESG Reports",
        "ko_summary": "기후공시는 홍보 문구보다 Scope 1, 2, 3 배출량, 산정 범위, 감축 목표, 자본지출 계획이 일관되는지 확인해야 한다.",
        "en_summary": "Climate disclosure should be read through Scope 1, 2, and 3 emissions, boundary choices, reduction targets, and capital expenditure plans rather than promotional language.",
        "ko_context": "파리협정과 배출 감축 논의는 기업 공시를 단순 평판 관리가 아니라 자본조달과 공급망 평가의 자료로 바꾸고 있다.",
        "en_context": "Paris Agreement and emissions-reduction debates are turning corporate climate disclosure into evidence for financing and supply-chain evaluation.",
        "ko_angle": "한국 수출기업은 협력사의 Scope 3 요구와 RE100 전력 조달, 제품 탄소정보 요구를 함께 준비해야 한다.",
        "en_angle": "Korean exporters need to prepare for supplier Scope 3 requests, RE100 procurement, and product-level carbon data at the same time.",
        "ko_actions": ["Scope 1, 2, 3의 산정 범위를 확인합니다.", "감축 목표와 투자 계획이 연결되는지 봅니다.", "외부 검증 여부와 기준 변경 내역을 확인합니다."],
        "en_actions": ["Check boundaries for Scope 1, 2, and 3 emissions.", "Look for links between targets and investment plans.", "Review assurance and changes in methodology."],
        "ko_signals": ["Scope 3", "산정 범위", "외부 검증", "자본지출"],
        "signals": ["Scope 3", "reporting boundary", "external assurance", "capital expenditure"],
        "sources": ["unep_gap2025", "unfccc_paris", "world_bank_climate"],
        "tags": ["Climate Disclosure", "ESG", "Emissions", "Supply Chains"],
    },
    {
        "slug": "adaptation-finance-flood-heat",
        "ko_title": "기후 적응 금융: 홍수와 폭염 피해를 줄이는 돈의 쓰임",
        "en_title": "Adaptation Finance: How Money Reduces Flood and Heat Damage",
        "ko_summary": "기후 적응 금융은 배출 감축과 달리 이미 커진 폭염, 홍수, 가뭄, 해수면 리스크에 대비해 인프라와 사회 안전망을 바꾸는 투자다.",
        "en_summary": "Adaptation finance differs from mitigation: it funds infrastructure and social protection against heat, floods, droughts, and sea-level risks already increasing.",
        "ko_context": "IPCC와 World Bank는 적응 투자가 재난 후 복구비를 줄이고 취약계층 피해를 낮추는 데 핵심이라고 설명한다.",
        "en_context": "IPCC and World Bank sources frame adaptation investment as a way to reduce post-disaster recovery costs and protect vulnerable groups.",
        "ko_angle": "한국은 지하차도, 반지하, 노후 하천, 폭염 취약 노동환경처럼 도시형 리스크가 커서 적응 예산의 우선순위가 중요하다.",
        "en_angle": "Korea faces urban risks such as underpasses, semi-basement housing, ageing waterways, and heat-exposed work, making adaptation-budget priorities important.",
        "ko_actions": ["피해가 반복되는 지역을 먼저 표시합니다.", "예방 투자와 사후 복구비를 비교합니다.", "취약계층 보호와 조기경보 예산을 함께 봅니다."],
        "en_actions": ["Map locations with repeated losses first.", "Compare preventive investment with recovery spending.", "Read vulnerable-group protection with early-warning budgets."],
        "ko_signals": ["반복 피해 지역", "조기경보", "배수 인프라", "취약계층"],
        "signals": ["repeated loss areas", "early warning", "drainage infrastructure", "vulnerable groups"],
        "sources": ["ipcc_ar6", "world_bank_climate", "undrr_gar"],
        "tags": ["Adaptation", "Climate Risk", "Floods", "Heat"],
    },
    {
        "slug": "extreme-heat-city-planning",
        "ko_title": "도시 폭염 대책: 기온보다 체감온도와 취약시간을 보기",
        "en_title": "Urban Heat Planning: Heat Index and Vulnerable Hours Before Temperature",
        "ko_summary": "도시 폭염은 최고기온만이 아니라 습도, 야간 최저기온, 그늘, 냉방 접근성, 야외 노동시간이 피해 규모를 결정한다.",
        "en_summary": "Urban heat risk depends on humidity, nighttime minimums, shade, cooling access, and outdoor work hours, not only the headline temperature.",
        "ko_context": "WMO와 한국 기상청 자료는 최근 폭염과 이상기후가 건강, 전력수요, 노동, 교통 인프라에 동시에 영향을 준다는 점을 보여준다.",
        "en_context": "WMO and KMA materials show recent heat and extreme climate affecting health, power demand, labour, and transport infrastructure at the same time.",
        "ko_angle": "한국 도시는 열섬, 고령화, 에어컨 비용, 배달·건설 노동이 겹치므로 폭염 대응은 복지와 전력정책을 함께 봐야 한다.",
        "en_angle": "Korean cities combine heat islands, ageing, cooling costs, delivery work, and construction work, so heat response is both welfare and power policy.",
        "ko_actions": ["최고기온보다 체감온도와 야간기온을 봅니다.", "무더위쉼터 접근성과 운영시간을 확인합니다.", "야외노동 중지 기준과 전력 피크를 같이 봅니다."],
        "en_actions": ["Read heat index and nighttime lows before daily highs.", "Check cooling-centre access and operating hours.", "Connect outdoor-work rules with electricity peaks."],
        "ko_signals": ["체감온도", "열대야", "냉방 접근성", "야외노동"],
        "signals": ["heat index", "tropical nights", "cooling access", "outdoor work"],
        "sources": ["wmo_climate2025", "kma_extreme2025", "ipcc_ar6"],
        "tags": ["Extreme Heat", "Cities", "Public Health", "Adaptation"],
    },
    {
        "slug": "heavy-rain-flood-insurance",
        "ko_title": "집중호우와 홍수보험: 재난 뉴스에서 재무 리스크까지 읽기",
        "en_title": "Heavy Rain and Flood Insurance: From Disaster News to Financial Risk",
        "ko_summary": "집중호우 리스크는 침수 피해, 배수 인프라, 보험 보장, 부동산 가치, 지방재정까지 연결되는 재무 리스크다.",
        "en_summary": "Heavy-rain risk links flood losses, drainage infrastructure, insurance coverage, property values, and local public finance.",
        "ko_context": "IPCC와 UNDRR는 재난 리스크가 기후, 노출, 취약성, 대응능력의 조합으로 커진다고 설명한다.",
        "en_context": "IPCC and UNDRR explain disaster risk as a combination of hazard, exposure, vulnerability, and response capacity.",
        "ko_angle": "국내에서는 침수 지도, 반지하·지하주차장, 하천 주변 개발, 보험 보장 공백을 함께 봐야 피해 예방이 가능하다.",
        "en_angle": "In Korea, flood maps, semi-basement housing, underground parking, river-adjacent development, and insurance gaps need to be read together.",
        "ko_actions": ["주소별 침수 이력과 지형을 확인합니다.", "보험의 풍수해 보장 범위를 읽습니다.", "배수로·하천 정비 계획을 지방 예산과 함께 봅니다."],
        "en_actions": ["Check address-level flood history and terrain.", "Read what flood and storm insurance actually covers.", "Connect drainage and river works with local budgets."],
        "ko_signals": ["침수 이력", "보험 보장 공백", "배수 용량", "지하공간"],
        "signals": ["flood history", "insurance gap", "drainage capacity", "underground space"],
        "sources": ["ipcc_ar6", "undrr_gar", "korea_climate_assessment"],
        "tags": ["Floods", "Insurance", "Climate Risk", "Adaptation"],
    },
    {
        "slug": "sea-level-port-risk",
        "ko_title": "해수면 상승과 항만 리스크: 무역국가가 놓치면 안 되는 비용",
        "en_title": "Sea-Level Rise and Port Risk: A Hidden Cost for Trading Economies",
        "ko_summary": "해수면 상승은 먼 미래의 해안선 문제가 아니라 항만, 물류창고, 보험, 배후 산업단지, 수출입 일정에 영향을 주는 리스크다.",
        "en_summary": "Sea-level rise is not only a future coastline issue; it affects ports, warehouses, insurance, industrial zones, and import-export schedules.",
        "ko_context": "WMO와 IPCC는 해수면과 해양 열 변화가 장기간 누적되어 해안 인프라의 설계 기준을 바꾼다고 설명한다.",
        "en_context": "WMO and IPCC sources show sea-level and ocean-heat changes accumulating over long periods and changing design standards for coastal infrastructure.",
        "ko_angle": "한국의 부산, 인천, 울산, 광양 같은 항만은 무역과 산업단지의 관문이라 기후 적응 투자를 물류 경쟁력으로 봐야 한다.",
        "en_angle": "Korean ports such as Busan, Incheon, Ulsan, and Gwangyang are gateways for trade and industry, so adaptation investment is logistics competitiveness.",
        "ko_actions": ["항만별 침수·폭풍해일 노출을 봅니다.", "방재 투자와 항만 확장 계획을 함께 읽습니다.", "보험료와 물류 지연 비용을 장기 비용에 넣습니다."],
        "en_actions": ["Review port exposure to flooding and storm surge.", "Read flood-protection investment with port expansion plans.", "Include insurance and logistics delays in long-term costs."],
        "ko_signals": ["해수면 추세", "폭풍해일", "항만 방재", "물류 지연"],
        "signals": ["sea-level trend", "storm surge", "port protection", "logistics delay"],
        "sources": ["wmo_climate2025", "ipcc_ar6", "world_bank_climate"],
        "tags": ["Sea Level", "Ports", "Trade", "Climate Risk"],
    },
    {
        "slug": "food-energy-water-nexus",
        "ko_title": "식량·에너지·물 넥서스: 기후 이슈가 장바구니 가격으로 오는 길",
        "en_title": "Food-Energy-Water Nexus: How Climate Risk Reaches Grocery Prices",
        "ko_summary": "가뭄, 홍수, 에너지 가격, 비료 비용, 물 관리가 연결되면 기후 리스크는 농산물 가격과 식품기업 원가로 이동한다.",
        "en_summary": "When drought, floods, energy prices, fertilizer costs, and water management interact, climate risk moves into grocery prices and food-company costs.",
        "ko_context": "IPCC와 WMO 자료는 기후 충격이 농업, 수자원, 에너지 시스템을 동시에 건드리며 복합 리스크를 만든다고 설명한다.",
        "en_context": "IPCC and WMO materials show climate shocks affecting agriculture, water, and energy systems together, creating compound risk.",
        "ko_angle": "한국은 식량과 에너지 수입 비중이 높아 국제 곡물가격, 환율, 해상운임, 국내 수급 대책을 한 번에 봐야 한다.",
        "en_angle": "Korea imports significant food and energy, so grain prices, exchange rates, shipping costs, and domestic supply measures need one dashboard.",
        "ko_actions": ["기상 충격과 에너지 가격을 같은 주간표에 넣습니다.", "비료·운송비가 식품 가격에 반영되는 시차를 봅니다.", "수입선 다변화와 비축 정책을 확인합니다."],
        "en_actions": ["Put weather shocks and energy prices in the same weekly table.", "Track the lag from fertilizer and freight costs to food prices.", "Check import diversification and stockpile policies."],
        "ko_signals": ["가뭄·홍수", "비료 가격", "해상운임", "곡물 재고"],
        "signals": ["drought and floods", "fertilizer prices", "shipping costs", "grain stocks"],
        "sources": ["ipcc_ar6", "wmo_climate2025", "world_bank_climate"],
        "tags": ["Food Security", "Energy", "Water", "Inflation"],
    },
    {
        "slug": "climate-migration-labor-risk",
        "ko_title": "기후 이주와 노동 리스크: 인구 문제가 공급망 문제가 되는 순간",
        "en_title": "Climate Migration and Labour Risk: When Population Stress Becomes Supply-Chain Stress",
        "ko_summary": "기후 충격은 농업, 건설, 물류, 돌봄 노동을 흔들고 지역 이주와 노동력 부족을 통해 공급망 비용으로 이어질 수 있다.",
        "en_summary": "Climate shocks can disrupt agriculture, construction, logistics, and care work, then move into supply-chain costs through migration and labour shortages.",
        "ko_context": "IPCC와 World Bank는 기후 리스크가 생계, 건강, 이동, 도시 인프라를 통해 사회경제적 취약성을 키운다고 설명한다.",
        "en_context": "IPCC and World Bank sources describe climate risk increasing socioeconomic vulnerability through livelihoods, health, mobility, and urban infrastructure.",
        "ko_angle": "한국은 고령화와 제조업 인력 부족이 이미 진행 중이라 해외 노동 공급과 국내 야외노동 안전 기준을 함께 봐야 한다.",
        "en_angle": "Korea already faces ageing and manufacturing labour shortages, so overseas labour supply and domestic outdoor-work safety standards need joint attention.",
        "ko_actions": ["기후 피해 지역과 주요 원자재·노동 공급지를 연결합니다.", "야외노동 중단 기준과 생산 차질을 확인합니다.", "이주와 도시 주거 부담을 장기 리스크로 봅니다."],
        "en_actions": ["Connect climate-hit regions with raw-material and labour supply.", "Check outdoor-work stoppage rules and production disruption.", "Treat migration and urban housing pressure as long-term risk."],
        "ko_signals": ["생계 충격", "야외노동", "지역 이주", "노동 부족"],
        "signals": ["livelihood shock", "outdoor work", "regional migration", "labour shortage"],
        "sources": ["ipcc_ar6", "world_bank_climate", "undrr_gar"],
        "tags": ["Migration", "Labour", "Climate Risk", "Supply Chains"],
    },
    {
        "slug": "household-energy-saving-bills",
        "ko_title": "가정 에너지 절감: 전기요금 뉴스보다 사용 패턴을 먼저 보기",
        "en_title": "Household Energy Savings: Usage Patterns Before Tariff Headlines",
        "ko_summary": "가정 에너지 절감은 전기요금 인상 뉴스에 반응하는 일이 아니라 냉난방, 대기전력, 조명, 가전 교체, 시간대 사용을 조정하는 생활 시스템이다.",
        "en_summary": "Household energy saving is not just reacting to tariff news; it is a system of cooling, heating, standby power, lighting, appliance replacement, and time-of-use habits.",
        "ko_context": "에너지 효율 자료들은 같은 요금제에서도 사용 시간과 기기 효율에 따라 가계 부담이 크게 달라질 수 있음을 보여준다.",
        "en_context": "Energy-efficiency sources show that usage timing and equipment efficiency can change household costs even under the same tariff.",
        "ko_angle": "국내 가계는 여름 냉방과 겨울 난방, 누진 구간, 관리비 구조가 섞여 있어 월별 사용량을 먼저 봐야 한다.",
        "en_angle": "Korean households need to read monthly use first because summer cooling, winter heating, tiered tariffs, and apartment fees interact.",
        "ko_actions": ["월별 kWh와 피크 사용 시간을 기록합니다.", "냉난방 설정온도와 필터 청소를 점검합니다.", "가전 교체는 절감액과 사용 시간을 함께 계산합니다."],
        "en_actions": ["Record monthly kWh and peak-use times.", "Check cooling and heating setpoints and filter cleaning.", "Calculate appliance replacement with savings and hours of use."],
        "ko_signals": ["월별 kWh", "누진 구간", "냉방 피크", "가전 효율"],
        "signals": ["monthly kWh", "tiered tariff", "cooling peak", "appliance efficiency"],
        "sources": ["kea", "iea_heat_pumps", "iea_electricity2026"],
        "tags": ["Energy Efficiency", "Households", "Electricity", "Bills"],
    },
    {
        "slug": "small-business-energy-risk-plan",
        "ko_title": "소상공인 에너지 리스크 계획: 전기·가스비를 고정비처럼 관리하기",
        "en_title": "Small-Business Energy Risk Plan: Manage Power and Gas as Core Fixed Costs",
        "ko_summary": "소상공인은 에너지비가 매출보다 늦게 반영되는 경우가 많아 계절별 사용량, 설비 효율, 계약 조건, 가격 전가 가능성을 미리 봐야 한다.",
        "en_summary": "Small businesses often feel energy costs after revenue decisions are set, so seasonal use, equipment efficiency, contracts, and pricing power need advance review.",
        "ko_context": "전력과 가스 가격 변동은 제조업뿐 아니라 음식점, 카페, 세탁소, 냉장·냉동 소매업의 마진을 직접 흔든다.",
        "en_context": "Power and gas price changes affect not only manufacturing but also restaurants, cafes, laundries, and refrigerated retail margins.",
        "ko_angle": "한국 소상공인은 냉난방과 조리·냉장 부하가 큰 업종일수록 에너지 절감이 단순 환경 캠페인이 아니라 생존 비용 관리가 된다.",
        "en_angle": "For Korean small businesses with large cooling, heating, cooking, or refrigeration loads, energy saving is operating-cost control, not only an environmental campaign.",
        "ko_actions": ["매출 대비 에너지비 비중을 월별로 봅니다.", "노후 냉장·냉방 설비의 교체 회수기간을 계산합니다.", "영업시간과 피크요금 시간을 맞춰 봅니다."],
        "en_actions": ["Track energy cost as a monthly share of revenue.", "Calculate payback for old refrigeration and cooling equipment.", "Compare operating hours with peak tariff periods."],
        "ko_signals": ["에너지비 비중", "노후 설비", "영업 피크", "가격 전가"],
        "signals": ["energy-cost share", "old equipment", "operating peak", "pricing power"],
        "sources": ["kea", "iea_ger2026", "eia_steo"],
        "tags": ["Small Business", "Energy Costs", "Efficiency", "Risk"],
    },
    {
        "slug": "korea-semiconductor-power-demand",
        "ko_title": "한국 반도체 전력 수요: 팹 증설 뉴스에서 전력망까지 읽기",
        "en_title": "Korea Semiconductor Power Demand: From Fab Expansion to Grid Capacity",
        "ko_summary": "반도체 팹 증설은 장비 투자 뉴스만이 아니라 전력 품질, 용수, 송전망, 재생에너지 조달, 지역 인프라 부담까지 포함한다.",
        "en_summary": "Semiconductor fab expansion is not only equipment capex; it includes power quality, water, transmission, renewable procurement, and regional infrastructure pressure.",
        "ko_context": "IEA 전력 자료는 데이터센터와 산업 전기화가 전력 수요의 중요한 성장축이며 고품질 전력 공급이 경쟁력이 된다고 보여준다.",
        "en_context": "IEA electricity materials show data centres and industrial electrification as key demand drivers, making high-quality electricity a competitiveness issue.",
        "ko_angle": "한국의 반도체 클러스터는 전력망과 용수 인프라가 맞지 않으면 투자 발표가 생산능력으로 전환되는 속도가 늦어진다.",
        "en_angle": "Korean semiconductor clusters can see investment announcements turn into capacity more slowly if grids and water infrastructure lag.",
        "ko_actions": ["팹 증설 규모를 전력수요로 환산합니다.", "송전망·변전소 일정과 용수 계획을 확인합니다.", "RE100 전력 조달 가능성을 수출 조건과 함께 봅니다."],
        "en_actions": ["Translate fab expansion into electricity demand.", "Check transmission, substation, and water timelines.", "Read RE100 procurement with export requirements."],
        "ko_signals": ["팹 전력수요", "변전소 일정", "용수 계획", "RE100 조달"],
        "signals": ["fab power demand", "substation timeline", "water plan", "RE100 procurement"],
        "sources": ["iea_electricity2026", "iea_energy_ai", "kesis"],
        "tags": ["Semiconductors", "Korea", "Electricity", "RE100"],
    },
    {
        "slug": "korea-battery-supply-chain-rules",
        "ko_title": "한국 배터리 공급망 규칙: 보조금보다 원산지와 광물 기준을 보기",
        "en_title": "Korea Battery Supply-Chain Rules: Origin and Minerals Before Subsidies",
        "ko_summary": "배터리 산업의 경쟁력은 셀 기술뿐 아니라 원산지 규정, 핵심광물 조달, 재활용, 중국 의존도, 미국·유럽 정책 변화에 좌우된다.",
        "en_summary": "Battery competitiveness depends not only on cell technology but also on origin rules, critical-mineral sourcing, recycling, China exposure, and US and European policy shifts.",
        "ko_context": "IEA 핵심광물과 배터리 자료는 전기차 성장 뒤에 광물 조달, 정제 집중도, 재활용, 배터리 가격의 복합 리스크가 있다고 설명한다.",
        "en_context": "IEA minerals and battery reports show complex risks behind EV growth: sourcing, refining concentration, recycling, and battery prices.",
        "ko_angle": "한국 배터리 기업은 해외 공장 위치와 광물 원산지 조건이 보조금 수혜와 고객 계약에 직접 영향을 주므로 정책 변화를 매출 변수로 봐야 한다.",
        "en_angle": "Korean battery makers need to treat plant location and mineral-origin rules as revenue variables because they affect incentives and customer contracts.",
        "ko_actions": ["광물 원산지와 정제지를 분리해 추적합니다.", "재활용 원료 비중과 장기계약을 확인합니다.", "미국·유럽 보조금 조건 변경을 고객별로 매핑합니다."],
        "en_actions": ["Track mineral origin separately from refining location.", "Check recycled material shares and long-term contracts.", "Map US and EU incentive changes by customer."],
        "ko_signals": ["광물 원산지", "정제지", "재활용", "보조금 조건"],
        "signals": ["mineral origin", "refining location", "recycling", "incentive rules"],
        "sources": ["iea_minerals2025", "iea_batteries", "iea_ev2026"],
        "tags": ["Batteries", "Supply Chains", "Korea", "Critical Minerals"],
    },
    {
        "slug": "renewable-ppa-re100-export",
        "ko_title": "재생에너지 PPA와 RE100: 수출기업이 전력계약을 봐야 하는 이유",
        "en_title": "Renewable PPAs and RE100: Why Exporters Need to Read Power Contracts",
        "ko_summary": "RE100과 재생에너지 PPA는 이미지 캠페인이 아니라 고객 요구, 탄소공시, 전력가격, 공급망 평가와 연결되는 수출 경쟁력 요소다.",
        "en_summary": "RE100 and renewable PPAs are not branding exercises; they connect customer requirements, climate disclosure, power prices, and supply-chain evaluation.",
        "ko_context": "재생에너지와 기후공시 흐름은 기업이 전력 사용의 배출계수와 조달 방식을 더 구체적으로 설명하도록 압박한다.",
        "en_context": "Renewable and disclosure trends are pushing companies to explain electricity emissions factors and procurement methods more specifically.",
        "ko_angle": "한국 수출기업은 재생에너지 조달 비용과 안정성을 제품 가격, 납품 조건, 글로벌 고객 감사 대응에 반영해야 한다.",
        "en_angle": "Korean exporters need to reflect renewable procurement cost and reliability in product pricing, delivery terms, and global customer audits.",
        "ko_actions": ["PPA가 물리적 전력인지 인증서 기반인지 구분합니다.", "계약 기간과 가격 조정 조건을 봅니다.", "제품 탄소정보와 연결되는 증빙 자료를 정리합니다."],
        "en_actions": ["Separate physical power from certificate-based procurement.", "Review contract duration and price-adjustment terms.", "Organize evidence that links procurement to product carbon data."],
        "ko_signals": ["PPA 가격", "계약 기간", "인증서", "고객 감사"],
        "signals": ["PPA price", "contract duration", "certificates", "customer audit"],
        "sources": ["iea_renewables2025", "unfccc_paris", "kea"],
        "tags": ["RE100", "PPA", "Exports", "Renewables"],
    },
    {
        "slug": "climate-policy-news-reading-system",
        "ko_title": "기후·에너지 정책 뉴스 읽는 시스템: 목표, 수단, 비용, 시간표",
        "en_title": "A Reading System for Climate and Energy Policy News: Targets, Tools, Costs, Timelines",
        "ko_summary": "기후·에너지 정책은 목표 수치만 보면 과장되거나 과소평가되기 쉽고, 실제로는 정책수단, 재원, 인허가, 전력망, 산업 수요를 함께 봐야 한다.",
        "en_summary": "Climate and energy policy is easy to overrate or dismiss if read only through targets; tools, funding, permits, grids, and industrial demand decide implementation.",
        "ko_context": "파리협정, UNEP 배출격차, IEA 에너지 전망은 목표와 현재 정책 사이의 차이를 확인하는 반복 가능한 읽기 틀을 제공한다.",
        "en_context": "The Paris Agreement, UNEP emissions-gap work, and IEA energy outlooks provide a repeatable framework for comparing targets with current policies.",
        "ko_angle": "국내 정책도 탄소중립 목표, 전력수급계획, 산업전략, 전기요금, 지역 수용성이 연결되어 있어 부처 발표 하나로 판단하기 어렵다.",
        "en_angle": "Korean policy links carbon-neutrality targets, power plans, industrial strategy, tariffs, and local acceptance, so one ministry announcement is never enough.",
        "ko_actions": ["목표 연도와 중간 이행 지표를 분리합니다.", "정책수단이 보조금, 규제, 가격, 공공투자인지 구분합니다.", "예산과 인허가 일정이 목표와 맞는지 확인합니다."],
        "en_actions": ["Separate target year from interim indicators.", "Classify tools as subsidies, regulation, pricing, or public investment.", "Check whether budgets and permits match the target."],
        "ko_signals": ["목표 연도", "정책수단", "예산", "인허가 일정"],
        "signals": ["target year", "policy tool", "budget", "permitting timeline"],
        "sources": ["unfccc_paris", "unep_gap2025", "iea_weo2025"],
        "tags": ["Climate Policy", "Energy Policy", "Planning", "Korea"],
    },
    {
        "slug": "climate-risk-scenario-planning",
        "ko_title": "기후 리스크 시나리오: 평균 전망보다 꼬리 위험을 먼저 보기",
        "en_title": "Climate-Risk Scenario Planning: Tail Risks Before Average Forecasts",
        "ko_summary": "기후 리스크는 평균 기온이나 평균 강수량보다 극단값, 동시다발 충격, 취약 인프라, 복구 능력이 실제 피해를 좌우한다.",
        "en_summary": "Climate risk is driven less by average temperature or rainfall than by extremes, compound shocks, fragile infrastructure, and recovery capacity.",
        "ko_context": "IPCC와 한국기후위기평가보고서는 영향과 적응을 평균 변화가 아니라 지역별 취약성과 노출의 조합으로 읽어야 한다고 말한다.",
        "en_context": "IPCC and Korea's climate-risk assessment show impacts and adaptation should be read through regional vulnerability and exposure, not only average change.",
        "ko_angle": "한국 기업과 지자체는 평균 예측보다 침수, 폭염, 산불, 공급망 중단 같은 꼬리 위험을 운영계획에 넣어야 한다.",
        "en_angle": "Korean companies and local governments need to put tail risks such as flooding, heat, wildfire, and supply-chain interruption into operating plans.",
        "ko_actions": ["평균값과 극단값을 다른 표에 둡니다.", "단일 재난보다 동시다발 재난을 검토합니다.", "복구 시간과 대체 공급 경로를 정합니다."],
        "en_actions": ["Put averages and extremes in separate tables.", "Test compound events, not only single disasters.", "Set recovery times and alternative supply routes."],
        "ko_signals": ["극단값", "동시다발 재난", "복구 시간", "대체 공급망"],
        "signals": ["extreme values", "compound events", "recovery time", "alternative supply chain"],
        "sources": ["ipcc_ar6", "korea_climate_assessment", "undrr_gar"],
        "tags": ["Climate Risk", "Scenarios", "Adaptation", "Resilience"],
    },
    {
        "slug": "extreme-weather-supply-chain-map",
        "ko_title": "이상기후 공급망 지도: 공장보다 항만·도로·전력부터 표시하기",
        "en_title": "Extreme-Weather Supply-Chain Map: Ports, Roads, and Power Before Factories",
        "ko_summary": "이상기후 공급망 관리는 공장 위치만이 아니라 항만, 도로, 철도, 전력, 물류창고, 협력사 복구 능력을 지도화해야 한다.",
        "en_summary": "Extreme-weather supply-chain planning requires mapping ports, roads, rail, power, warehouses, and supplier recovery capacity, not only factory locations.",
        "ko_context": "WMO와 UNDRR 자료는 극한기상이 직접 피해뿐 아니라 물류 지연, 전력 중단, 사회 시스템 부담을 통해 경제 피해를 키운다고 설명한다.",
        "en_context": "WMO and UNDRR sources show extreme weather increasing economic damage through logistics delays, power outages, and stress on social systems.",
        "ko_angle": "한국 수출기업은 해외 공장뿐 아니라 국내 항만, 부품 협력사, 냉장 물류, 전력 복구 시간을 공급망 리스크에 넣어야 한다.",
        "en_angle": "Korean exporters should include domestic ports, component suppliers, cold logistics, and power-restoration time in supply-chain risk.",
        "ko_actions": ["1차 협력사보다 핵심 병목 인프라를 먼저 표시합니다.", "정전·침수·도로 차단 시 대체 경로를 정합니다.", "협력사의 복구 시간 목표를 계약에 넣습니다."],
        "en_actions": ["Map critical bottleneck infrastructure before tier-one suppliers.", "Set alternative routes for outages, floods, and road closures.", "Put supplier recovery-time objectives into contracts."],
        "ko_signals": ["항만 노출", "정전 시간", "도로 차단", "협력사 복구"],
        "signals": ["port exposure", "outage duration", "road closure", "supplier recovery"],
        "sources": ["wmo_climate2025", "undrr_gar", "world_bank_climate"],
        "tags": ["Extreme Weather", "Supply Chains", "Resilience", "Logistics"],
    },
    {
        "slug": "water-stress-energy-industry",
        "ko_title": "물 스트레스와 에너지 산업: 전력·반도체·배터리의 숨은 제약",
        "en_title": "Water Stress and Energy-Intensive Industry: A Hidden Constraint for Power, Chips, and Batteries",
        "ko_summary": "물 스트레스는 발전소 냉각, 반도체 초순수, 배터리 공정, 데이터센터 냉각을 동시에 제약할 수 있는 산업 인프라 리스크다.",
        "en_summary": "Water stress can constrain power-plant cooling, semiconductor ultrapure water, battery processes, and data-centre cooling at the same time.",
        "ko_context": "기후 리스크 자료는 물 부족과 홍수가 모두 산업 인프라에 영향을 줄 수 있어 물 관리를 에너지 정책과 함께 봐야 한다고 설명한다.",
        "en_context": "Climate-risk sources show that both water scarcity and flooding can affect industrial infrastructure, so water management belongs in energy policy.",
        "ko_angle": "한국의 첨단산업 클러스터는 전력뿐 아니라 용수 확보와 방류 기준이 맞아야 확장 가능성이 유지된다.",
        "en_angle": "Korea's advanced-industry clusters need water supply and discharge standards, not only electricity, to maintain expansion capacity.",
        "ko_actions": ["전력 사용량과 용수 사용량을 같은 프로젝트 표에 둡니다.", "가뭄과 홍수 노출을 모두 봅니다.", "재이용수와 비상 취수 계획을 확인합니다."],
        "en_actions": ["Put power use and water use in the same project table.", "Check exposure to both drought and flood.", "Review recycled-water and emergency-intake plans."],
        "ko_signals": ["용수 확보", "초순수", "냉각수", "방류 기준"],
        "signals": ["water supply", "ultrapure water", "cooling water", "discharge standards"],
        "sources": ["ipcc_ar6", "world_bank_climate", "iea_energy_ai"],
        "tags": ["Water", "Industry", "Semiconductors", "Climate Risk"],
    },
    {
        "slug": "energy-efficiency-first-fuel",
        "ko_title": "에너지 효율은 첫 번째 연료다: 절약이 아니라 생산성 전략으로 보기",
        "en_title": "Energy Efficiency as the First Fuel: Productivity, Not Just Saving",
        "ko_summary": "에너지 효율은 덜 쓰자는 캠페인이 아니라 같은 생산과 생활을 더 적은 에너지로 달성해 수입비용, 전력망 투자, 배출을 동시에 줄이는 전략이다.",
        "en_summary": "Energy efficiency is not merely using less; it delivers the same output and comfort with less energy, reducing import bills, grid investment, and emissions together.",
        "ko_context": "IEA 에너지 전망은 수요 증가 속에서 효율 개선이 에너지 안보와 배출 감축을 동시에 지원하는 핵심 수단이라고 설명한다.",
        "en_context": "IEA energy outlooks frame efficiency improvement as a key tool that supports both energy security and emissions reduction amid demand growth.",
        "ko_angle": "한국은 에너지 수입과 제조업 전력 수요가 커서 효율 투자가 연료비 절감뿐 아니라 산업 경쟁력과 무역수지에 연결된다.",
        "en_angle": "Because Korea imports energy and has power-intensive manufacturing, efficiency investment links fuel-cost savings with industrial competitiveness and the trade balance.",
        "ko_actions": ["절감률보다 회수기간과 운영 안정성을 봅니다.", "설비 효율과 운전 방식 개선을 분리합니다.", "효율 투자가 피크 수요를 얼마나 줄이는지 계산합니다."],
        "en_actions": ["Read payback and operational reliability before headline savings.", "Separate equipment efficiency from operating practice.", "Calculate how efficiency investment reduces peak demand."],
        "ko_signals": ["회수기간", "피크 절감", "설비 효율", "운전 최적화"],
        "signals": ["payback period", "peak reduction", "equipment efficiency", "operational optimization"],
        "sources": ["iea_ger2026", "iea_electricity2026", "kea"],
        "tags": ["Energy Efficiency", "Productivity", "Electricity", "Industry"],
    },
    {
        "slug": "climate-finance-project-quality",
        "ko_title": "기후금융 프로젝트 품질: 녹색 이름보다 실제 감축과 적응 효과 보기",
        "en_title": "Climate-Finance Project Quality: Impact Before Green Labels",
        "ko_summary": "기후금융은 녹색 이름이 붙었다고 충분하지 않으며 실제 감축량, 적응 효과, 추가성, 지역 피해 감소, 사후 측정 방식이 중요하다.",
        "en_summary": "Climate finance is not sufficient because a project has a green label; actual emissions reduction, adaptation impact, additionality, local loss reduction, and measurement matter.",
        "ko_context": "World Bank와 UNEP 자료는 기후금융을 투입액이 아니라 결과와 피해 감소로 평가해야 한다는 방향을 강화하고 있다.",
        "en_context": "World Bank and UNEP materials increasingly push climate finance to be evaluated by outcomes and loss reduction, not only by money committed.",
        "ko_angle": "한국 금융기관과 기업은 해외 프로젝트의 녹색 라벨보다 데이터, 기준, 검증, 지역사회 리스크를 확인해야 평판 리스크를 줄일 수 있다.",
        "en_angle": "Korean financial institutions and companies can reduce reputation risk by checking data, standards, verification, and community risk behind overseas project labels.",
        "ko_actions": ["감축량 산정 기준과 기준선을 확인합니다.", "적응 프로젝트는 피해 감소 지표를 봅니다.", "외부 검증과 사후 모니터링 계획을 요구합니다."],
        "en_actions": ["Check emissions accounting and baseline assumptions.", "For adaptation projects, read loss-reduction metrics.", "Require external verification and post-project monitoring."],
        "ko_signals": ["추가성", "기준선", "피해 감소", "외부 검증"],
        "signals": ["additionality", "baseline", "loss reduction", "external verification"],
        "sources": ["world_bank_climate", "unep_gap2025", "ipcc_ar6"],
        "tags": ["Climate Finance", "ESG", "Adaptation", "Emissions"],
    },
    {
        "slug": "resilience-budget-local-government",
        "ko_title": "지자체 회복력 예산: 재난 후 복구보다 예방 투자를 먼저 보기",
        "en_title": "Local Resilience Budgets: Prevention Before Post-Disaster Recovery",
        "ko_summary": "지자체 회복력 예산은 제방, 배수, 폭염쉼터, 산사태, 취약계층 보호처럼 재난 전 피해를 줄이는 투자에 얼마나 배분되는지가 핵심이다.",
        "en_summary": "Local resilience budgets should be judged by how much they invest before disasters in levees, drainage, cooling shelters, landslide prevention, and protection of vulnerable people.",
        "ko_context": "UNDRR와 IPCC는 재난 위험을 줄이려면 사후 복구보다 노출과 취약성을 줄이는 계획이 우선되어야 한다고 설명한다.",
        "en_context": "UNDRR and IPCC materials stress reducing exposure and vulnerability before disasters, not relying only on recovery afterward.",
        "ko_angle": "한국 지자체는 고령화, 지하공간, 노후 인프라, 집중호우가 겹쳐 중앙정부 지원 이전에 지역별 위험지도와 예산 우선순위가 필요하다.",
        "en_angle": "Korean local governments face ageing, underground spaces, ageing infrastructure, and heavy rain together, so local risk maps and budget priorities matter before central support arrives.",
        "ko_actions": ["재난 유형별 반복 피해 지역을 예산표에 연결합니다.", "유지보수 예산과 신규 토목사업을 구분합니다.", "취약계층 보호 예산을 별도로 확인합니다."],
        "en_actions": ["Connect repeated-loss locations with budget lines.", "Separate maintenance budgets from new construction projects.", "Check dedicated funding for vulnerable groups."],
        "ko_signals": ["예방 예산", "노후 인프라", "위험지도", "취약계층"],
        "signals": ["prevention budget", "ageing infrastructure", "risk map", "vulnerable groups"],
        "sources": ["undrr_gar", "korea_climate_assessment", "world_bank_climate"],
        "tags": ["Resilience", "Local Government", "Adaptation", "Budget"],
    },
    {
        "slug": "energy-import-bill-exchange-rate",
        "ko_title": "에너지 수입액과 환율: 원화 약세가 전기·가스비로 오는 경로",
        "en_title": "Energy Import Bills and Exchange Rates: How a Weaker Won Reaches Power and Gas Costs",
        "ko_summary": "에너지 가격이 안정돼도 원화가 약하면 수입액과 공기업 비용 부담이 커질 수 있어 유가와 환율을 같이 봐야 한다.",
        "en_summary": "Even when global energy prices stabilize, a weaker won can raise import bills and utility cost pressure, so fuel prices and exchange rates belong together.",
        "ko_context": "에너지 시장 전망은 가격 자체뿐 아니라 통화, 재고, 계약 구조가 수입국의 실제 비용을 바꾼다는 점을 보여준다.",
        "en_context": "Energy-market outlooks show that currencies, inventories, and contracts change the actual cost for importing countries, not only commodity prices.",
        "ko_angle": "한국의 전기·가스요금 논쟁은 국제 가격, 환율, 공기업 재무, 물가 정책이 얽혀 있어 한 달 가격만으로 판단하기 어렵다.",
        "en_angle": "Korea's power and gas tariff debates combine global prices, exchange rates, utility finances, and inflation policy, so one month of prices is too narrow.",
        "ko_actions": ["원화 기준 에너지 가격을 계산합니다.", "공기업 연료비 조정 시차를 확인합니다.", "가계와 산업용 요금 영향을 분리합니다."],
        "en_actions": ["Calculate energy prices in won terms.", "Check the lag in utility fuel-cost adjustments.", "Separate household and industrial tariff effects."],
        "ko_signals": ["원화 환산 가격", "연료비 조정", "공기업 재무", "산업용 요금"],
        "signals": ["won-denominated price", "fuel-cost adjustment", "utility finances", "industrial tariff"],
        "sources": ["eia_steo", "iea_ger2026", "kesis"],
        "tags": ["Exchange Rates", "Energy Imports", "Utilities", "Korea"],
    },
    {
        "slug": "clean-tech-industrial-policy",
        "ko_title": "청정기술 산업정책: 보조금 경쟁보다 공급망 위치를 보기",
        "en_title": "Clean-Tech Industrial Policy: Supply-Chain Position Before Subsidy Headlines",
        "ko_summary": "청정기술 산업정책은 보조금 규모보다 태양광, 배터리, 전력기기, 전기차, 수소 장비의 어느 공급망 단계에 설 것인지가 중요하다.",
        "en_summary": "Clean-tech industrial policy depends less on subsidy size than on where a country sits in solar, batteries, grid equipment, EVs, and hydrogen equipment supply chains.",
        "ko_context": "IEA 전망들은 에너지 전환이 기술 배치뿐 아니라 제조, 무역, 광물, 전력망 장비의 산업 경쟁으로 바뀌고 있음을 보여준다.",
        "en_context": "IEA outlooks show the energy transition becoming an industrial contest across manufacturing, trade, minerals, and grid equipment, not only technology deployment.",
        "ko_angle": "한국은 배터리와 전력기기 강점이 있지만 원재료와 시장 접근 규칙에 취약해 산업정책을 공급망 전체로 봐야 한다.",
        "en_angle": "Korea has strengths in batteries and electrical equipment but remains exposed to raw materials and market-access rules, so policy needs a full supply-chain view.",
        "ko_actions": ["보조금 총액보다 지원 대상 공급망 단계를 봅니다.", "국내 생산과 해외 생산의 규칙 차이를 확인합니다.", "인력·전력·광물 병목을 산업정책에 포함합니다."],
        "en_actions": ["Read the supported supply-chain stage before the total subsidy amount.", "Compare rules for domestic and overseas production.", "Include labour, electricity, and mineral bottlenecks in policy analysis."],
        "ko_signals": ["공급망 단계", "보조금 조건", "전력기기", "시장 접근"],
        "signals": ["supply-chain stage", "subsidy conditions", "grid equipment", "market access"],
        "sources": ["iea_weo2025", "iea_minerals2025", "iea_renewables2025"],
        "tags": ["Clean Tech", "Industrial Policy", "Supply Chains", "Korea"],
    },
]


def slug_path(slug: str, lang: str) -> str:
    category = KO_CATEGORY if lang == "ko" else EN_CATEGORY
    return f"/{category.lower()}/{slug}/"


def svg_text_lines(lines: list[str], x: int, y: int, size: int = 30, gap: int = 44) -> str:
    return "\n".join(
        f'<text x="{x}" y="{y + index * gap}" font-family="Arial, sans-serif" font-size="{size}" fill="#16302b">{html.escape(line)}</text>'
        for index, line in enumerate(lines)
    )


def write_svg(topic: dict[str, object]) -> None:
    slug = str(topic["slug"])
    image_dir = ROOT / "images" / f"{POST_DATE}-{slug}"
    image_dir.mkdir(parents=True, exist_ok=True)

    title = str(topic["en_title"])
    ko_title = str(topic["ko_title"])
    signals = list(topic["signals"])
    ko_signals = list(topic["ko_signals"])

    hero = f"""<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="720" viewBox="0 0 1280 720" role="img" aria-labelledby="title desc">
  <title id="title">{html.escape(title)}</title>
  <desc id="desc">Climate and energy briefing image with core signals, Korea-facing channels, and reader action points.</desc>
  <rect width="1280" height="720" fill="#f4efe4"/>
  <circle cx="1060" cy="120" r="210" fill="#f2c166" opacity="0.52"/>
  <circle cx="220" cy="620" r="250" fill="#8ab7a1" opacity="0.34"/>
  <path d="M0 462 C180 398 320 520 520 444 C760 354 900 358 1280 292 L1280 720 L0 720 Z" fill="#dce9dd"/>
  <rect x="82" y="92" width="1116" height="536" rx="40" fill="#fffdf6" opacity="0.92"/>
  <text x="124" y="158" font-family="Arial, sans-serif" font-size="28" letter-spacing="4" fill="#5f6f52">CLIMATE &amp; ENERGY</text>
  <text x="124" y="222" font-family="Arial, sans-serif" font-size="42" font-weight="700" fill="#15352f">{html.escape(title[:64])}</text>
  <text x="124" y="280" font-family="Arial, sans-serif" font-size="28" fill="#33524b">{html.escape(ko_title[:70])}</text>
  <g transform="translate(124 342)">
    <rect width="280" height="118" rx="24" fill="#1f6f5f"/>
    <text x="28" y="48" font-family="Arial, sans-serif" font-size="25" font-weight="700" fill="#ffffff">Demand</text>
    <text x="28" y="86" font-family="Arial, sans-serif" font-size="22" fill="#e8fff8">load, timing, peaks</text>
  </g>
  <g transform="translate(456 342)">
    <rect width="280" height="118" rx="24" fill="#c46a3a"/>
    <text x="28" y="48" font-family="Arial, sans-serif" font-size="25" font-weight="700" fill="#ffffff">Supply</text>
    <text x="28" y="86" font-family="Arial, sans-serif" font-size="22" fill="#fff1e8">fuel, grid, storage</text>
  </g>
  <g transform="translate(788 342)">
    <rect width="280" height="118" rx="24" fill="#304f73"/>
    <text x="28" y="48" font-family="Arial, sans-serif" font-size="25" font-weight="700" fill="#ffffff">Risk</text>
    <text x="28" y="86" font-family="Arial, sans-serif" font-size="22" fill="#edf5ff">price, climate, policy</text>
  </g>
  <path d="M404 400 H456" stroke="#16302b" stroke-width="8" stroke-linecap="round"/>
  <path d="M736 400 H788" stroke="#16302b" stroke-width="8" stroke-linecap="round"/>
  <text x="124" y="540" font-family="Arial, sans-serif" font-size="25" fill="#16302b">Reader task: separate targets, tools, costs, timelines, and Korea-facing transmission channels.</text>
</svg>
"""

    signal_lines = [f"{index + 1}. {signal}" for index, signal in enumerate(signals[:4])]
    ko_signal_lines = [f"{index + 1}. {signal}" for index, signal in enumerate(ko_signals[:4])]
    signal_map = f"""<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="720" viewBox="0 0 1280 720" role="img" aria-labelledby="title desc">
  <title id="title">{html.escape(title)} signal map</title>
  <desc id="desc">Checklist-style climate and energy signal map for policy, business, household, and Korea-facing analysis.</desc>
  <rect width="1280" height="720" fill="#eef3ed"/>
  <rect x="70" y="72" width="1140" height="576" rx="36" fill="#ffffff"/>
  <text x="112" y="142" font-family="Arial, sans-serif" font-size="36" font-weight="700" fill="#16302b">Signal Map</text>
  <text x="112" y="192" font-family="Arial, sans-serif" font-size="25" fill="#56645c">{html.escape(title[:78])}</text>
  <rect x="112" y="240" width="492" height="300" rx="28" fill="#f4efe4"/>
  <text x="146" y="292" font-family="Arial, sans-serif" font-size="29" font-weight="700" fill="#1f6f5f">English Signals</text>
  {svg_text_lines(signal_lines, 146, 352, 25, 46)}
  <rect x="676" y="240" width="492" height="300" rx="28" fill="#e8f0ec"/>
  <text x="710" y="292" font-family="Arial, sans-serif" font-size="29" font-weight="700" fill="#1f6f5f">한국어 신호</text>
  {svg_text_lines(ko_signal_lines, 710, 352, 25, 46)}
  <text x="112" y="598" font-family="Arial, sans-serif" font-size="24" fill="#33413c">Read the next update by checking direction, duration, channel, and implementation capacity.</text>
</svg>
"""

    (image_dir / "hero.svg").write_text(hero, encoding="utf-8")
    (image_dir / "signal-map.svg").write_text(signal_map, encoding="utf-8")


def source_notes(topic: dict[str, object], lang: str) -> str:
    return "\n".join(
        f"- [{SOURCES[key][lang]}]({SOURCES[key]['url']})"
        for key in topic["sources"]
    )


def bullet_lines(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)


def clean_body(text: str) -> str:
    lines = [line[8:] if line.startswith("        ") else line for line in text.splitlines()]
    return "\n".join(lines).strip() + "\n"


def signal_bullets(topic: dict[str, object], lang: str) -> str:
    signals = topic["ko_signals"] if lang == "ko" else topic["signals"]
    if lang == "ko":
        return "\n".join(
            f"- **{signal}**: 단일 수치보다 방향, 지속 기간, 정책 반응, 국내 전달 경로를 함께 확인합니다."
            for signal in signals
        )
    return "\n".join(
        f"- **{signal}**: read direction, duration, policy response, and domestic transmission before treating it as a standalone number."
        for signal in signals
    )


def related_links(index: int, lang: str) -> str:
    total = len(TOPICS)
    related = [TOPICS[(index + 1) % total], TOPICS[(index + 2) % total]]
    if lang == "ko":
        return "\n".join(f"- [{item['ko_title']}]({slug_path(item['slug'], 'ko')})" for item in related)
    return "\n".join(f"- [{item['en_title']}]({slug_path(item['slug'], 'en')})" for item in related)


def post_front_matter(topic: dict[str, object], lang: str, index: int) -> str:
    slug = topic["slug"]
    category = KO_CATEGORY if lang == "ko" else EN_CATEGORY
    title = topic["ko_title"] if lang == "ko" else topic["en_title"]
    summary = topic["ko_summary"] if lang == "ko" else topic["en_summary"]
    image_description = (
        "기후·에너지 이슈의 핵심 신호, 국내 전달 경로, 정책·산업 리스크를 요약한 교육용 이미지입니다."
        if lang == "ko"
        else "Climate and energy briefing image summarizing core signals, domestic transmission channels, and policy or industry risk."
    )
    tags = "\n".join(f"  - {tag}" for tag in topic["tags"])
    minute = index % 60
    return f"""---
layout: single
title: >
  {title}
seo_title: >
  {title}
date: {POST_DATE}T09:{minute:02d}:00+09:00
last_modified_at: {LAST_MODIFIED_AT}
lang: {lang}
translation_id: climate-energy-{slug}
header:
  teaser: /images/{POST_DATE}-{slug}/hero.svg
  overlay_image: /images/{POST_DATE}-{slug}/hero.svg
  overlay_filter: 0.45
  image_description: >
    {image_description}
excerpt: >
  {summary}
seo_description: >
  {summary}
categories:
  - {category}
tags:
{tags}
---
"""


def ko_body(topic: dict[str, object], index: int) -> str:
    slug = topic["slug"]
    return clean_body(
        f"""
        {topic["ko_summary"]}

        이 글은 특정 에너지 설비, 주식, 펀드, 정책을 권유하는 글이 아닙니다. 공식 자료를 바탕으로 **기후·에너지 뉴스를 읽는 순서**를 정리하는 교육용 브리핑입니다.

        ![{topic["ko_title"]} 핵심 흐름 요약](/images/{POST_DATE}-{slug}/hero.svg)

        ## 왜 지금 봐야 하나

        {topic["ko_context"]}

        기후와 에너지 이슈는 한 번에 여러 경로로 움직입니다. 국제 유가가 오르면 물가와 환율 부담이 커지고, 전력망 투자가 늦어지면 AI·반도체·배터리 투자의 실제 속도도 느려질 수 있습니다. 반대로 효율 개선이나 저장장치 투자는 연료 수입과 전력망 부담을 동시에 줄일 수 있습니다.

        {topic["ko_angle"]}

        그래서 이 주제는 찬반 구도로만 읽기 어렵습니다. 목표 수치, 정책 수단, 예산, 인허가, 공급망, 지역 수용성을 함께 봐야 다음 뉴스가 구조적 변화인지 단기 소음인지 구분할 수 있습니다.

        ## 핵심 구조

        - **수요**: 전력, 냉난방, 운송, 산업 공정, 데이터센터가 언제 어디서 늘어나는지 봅니다.
        - **공급**: 발전원 비중보다 전력망, 연료 조달, 저장장치, 설비 납기를 함께 봅니다.
        - **가격**: 국제 가격과 환율, 계약 구조, 보조금, 세금이 최종 비용을 바꿉니다.
        - **리스크**: 폭염, 홍수, 해수면, 지정학, 수출통제처럼 서로 다른 충격이 동시에 올 수 있습니다.

        ## 현재 읽어야 할 신호

        {signal_bullets(topic, "ko")}

        이 신호들은 하나씩 보면 과장되거나 과소평가되기 쉽습니다. 예를 들어 발전 설비가 늘어도 송전망이 부족하면 실제 전력 공급은 막힐 수 있습니다. 국제 가격이 내려도 환율이나 계약 구조 때문에 국내 비용은 늦게 내려갈 수 있습니다.

        ![{topic["ko_title"]} 점검 신호 지도](/images/{POST_DATE}-{slug}/signal-map.svg)

        ## 국내 연결 경로

        한국 독자는 이 주제를 최소 세 단계로 읽는 편이 좋습니다.

        1. 국제 자료에서 방향을 확인합니다.
        2. 국내 전력, 수입, 산업, 생활비로 이어지는 경로를 표시합니다.
        3. 실제 실행을 막는 병목을 찾습니다.

        에너지 전환은 발표보다 실행이 느릴 수 있습니다. 전력망은 짧은 기간에 복제하기 어렵고, 핵심광물과 전력기기는 조달처가 제한될 수 있습니다. 기후 적응도 비슷합니다. 위험을 알고 있어도 예산, 토지, 주민 수용성, 유지보수 체계가 없으면 피해를 줄이기 어렵습니다.

        ## 실무 체크리스트

        {bullet_lines(topic["ko_actions"])}

        이 체크리스트는 단기 전망을 맞히기 위한 것이 아닙니다. 다음 발표나 통계가 나왔을 때 무엇이 바뀌었고 무엇이 그대로인지 확인하기 위한 기준선입니다.

        ## 숫자를 볼 때 주의할 점

        같은 수치라도 기준 연도, 측정 단위, 포함 범위가 다르면 의미가 달라집니다. 설치용량과 실제 발전량은 다르고, 평균 기온과 극한 폭염 위험도 다릅니다. 기업의 배출량도 Scope 1, Scope 2, Scope 3가 서로 다른 질문에 답합니다.

        따라서 기후·에너지 자료를 볼 때는 먼저 **기준선, 기간, 단위, 지역 범위, 정책 가정**을 확인하세요. 그다음 한국의 수입 구조, 전력망 위치, 산업 노출, 가계 비용으로 번역해야 합니다.

        ## 공식 자료로 다시 확인하기

        {source_notes(topic, "ko")}

        ## 함께 보면 좋은 글

        {related_links(index, "ko")}
        """
    )


def en_body(topic: dict[str, object], index: int) -> str:
    slug = topic["slug"]
    return clean_body(
        f"""
        {topic["en_summary"]}

        This article is an educational briefing, not investment advice, legal advice, or a recommendation to buy a specific energy product. It gives readers a practical order for reading **climate and energy news** with official-source context.

        ![{topic["en_title"]} core flow summary](/images/{POST_DATE}-{slug}/hero.svg)

        ## Why This Matters Now

        {topic["en_context"]}

        Climate and energy issues rarely move through one channel. An oil shock can affect inflation and exchange rates. A slow grid build-out can delay AI, semiconductor, battery, and factory investments. Efficiency and storage can reduce fuel imports and grid stress at the same time.

        {topic["en_angle"]}

        This is why the topic should not be reduced to a simple for-or-against debate. Targets, policy tools, budgets, permits, supply chains, and local acceptance need to be read together before judging whether a headline is structural change or short-term noise.

        ## Core Structure

        - **Demand**: check when and where power, cooling, transport, industrial processes, and data centres increase load.
        - **Supply**: read generation mix together with grids, fuel procurement, storage, and equipment delivery.
        - **Price**: international prices, exchange rates, contracts, subsidies, and taxes change the final cost.
        - **Risk**: heat, floods, sea level, geopolitics, and export controls can arrive as compound shocks.

        ## Signals To Watch

        {signal_bullets(topic, "en")}

        These signals can mislead when they are read alone. Generation capacity can rise while grid constraints prevent useful output. Global fuel prices can fall while domestic costs remain sticky because of exchange rates or contract lags.

        ![{topic["en_title"]} signal checklist map](/images/{POST_DATE}-{slug}/signal-map.svg)

        ## Korea-Facing Transmission

        A practical reading order for Korean readers has three steps.

        1. Use official international sources to identify the direction of change.
        2. Translate the issue into domestic channels: imports, electricity, exports, industrial costs, household bills, or local disaster risk.
        3. Find the implementation bottleneck: grid capacity, permitting, finance, equipment, local acceptance, data, or maintenance.

        Energy transitions can be slower than announcements. Grids cannot be copied quickly. Critical minerals and electrical equipment can have concentrated supply chains. Climate adaptation has the same problem: knowing the risk is not enough if budgets, land, maintenance, and local trust are missing.

        ## Practical Checklist

        {bullet_lines(topic["en_actions"])}

        This checklist is not for predicting the next price move. It is a baseline for checking what changed, what did not change, and which constraint matters most when a new policy, forecast, or company announcement appears.

        ## How To Read The Numbers

        The same number can mean different things depending on the baseline year, unit, coverage, and region. Installed capacity is not the same as actual generation. Average temperature is not the same as extreme heat risk. Corporate emissions can answer different questions depending on Scope 1, Scope 2, and Scope 3 boundaries.

        Before using climate or energy data, check the **baseline, period, unit, geographic coverage, and policy assumptions**. Then translate the number into Korea's import structure, grid geography, industrial exposure, and household cost channels.

        ## Source Notes

        {source_notes(topic, "en")}

        ## Related Reading

        {related_links(index, "en")}
        """
    )


def write_post(topic: dict[str, object], index: int, lang: str) -> None:
    slug = topic["slug"]
    title_body = ko_body(topic, index) if lang == "ko" else en_body(topic, index)
    relative_dir = ROOT / "_posts" / lang
    relative_dir.mkdir(parents=True, exist_ok=True)
    path = relative_dir / f"{POST_DATE}-{slug}.md"
    path.write_text(post_front_matter(topic, lang, index) + "\n" + title_body, encoding="utf-8")


def write_category_pages() -> None:
    pages = {
        "ko": {
            "path": ROOT / "_pages" / "category-ko_Climate_Energy.md",
            "permalink": "/ko_climate_energy/",
            "title": "Climate & Energy",
            "seo": "전력망, AI 데이터센터, 재생에너지, 배터리, 핵심광물, 탄소가격, 폭염, 홍수, 기후적응, 한국 산업 리스크를 공식 자료 기반으로 읽는 기후·에너지 글 모음입니다.",
            "body": """
Climate & Energy 카테고리는 기후와 에너지를 환경 구호가 아니라 **전력망, 산업 경쟁력, 생활비, 공급망, 재난 회복력**의 관점에서 읽기 위한 브리핑 모음입니다.

각 글은 IEA, IPCC, WMO, UNEP, UNFCCC, World Bank, OECD, EIA, 한국 에너지·기후 관련 공식 자료를 우선 참고합니다. 목표는 특정 정책이나 기술을 홍보하는 것이 아니라, 다음 뉴스가 나왔을 때 수요, 공급, 가격, 리스크, 국내 전달 경로를 차분히 나누어 보는 기준을 만드는 것입니다.

처음 읽는다면 AI 데이터센터 전력 수요, 전력망 병목, 재생에너지 전망으로 큰 지도를 잡고, 그다음 배터리·핵심광물·RE100·폭염·홍수 적응 글로 확장하는 순서가 좋습니다.

## 먼저 읽기

- [AI 데이터센터 전력 수요](/ko_climate_energy/ai-data-center-electricity-demand/)
- [에너지 전환의 병목은 전력망이다](/ko_climate_energy/power-grid-bottlenecks-transition/)
- [기후·에너지 정책 뉴스 읽는 시스템](/ko_climate_energy/climate-policy-news-reading-system/)

## 최신 글

{% assign posts = site.categories["ko_Climate_Energy"] %}
{% for post in posts %}
  {% include archive-single.html type=page.entries_layout %}
{% endfor %}
""",
        },
        "en": {
            "path": ROOT / "_pages" / "category-en_Climate_Energy.md",
            "permalink": "/en_climate_energy/",
            "title": "Climate & Energy",
            "seo": "Official-source climate and energy briefings on grids, AI data centers, renewables, batteries, carbon pricing, heat, floods, adaptation, and Korea-facing industry risk.",
            "body": """
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
""",
        },
    }

    for lang, data in pages.items():
        data["path"].write_text(
            dedent(
                f"""---
title: "{data["title"]}"
layout: archive
permalink: {data["permalink"]}
lang: {lang}
seo_description: >
  {data["seo"]}
sidebar:
    nav: "sidebar-category"
---

{data["body"].strip()}
"""
            ),
            encoding="utf-8",
        )


def main() -> None:
    for index, topic in enumerate(TOPICS):
        write_svg(topic)
        write_post(topic, index, "ko")
        write_post(topic, index, "en")
    write_category_pages()
    print(f"Generated {len(TOPICS)} paired Climate & Energy topics.")


if __name__ == "__main__":
    main()
