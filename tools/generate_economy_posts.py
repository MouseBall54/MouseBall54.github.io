#!/usr/bin/env python3
"""Generate paired Economy posts and local PNG context images."""

from __future__ import annotations

import struct
import zlib
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parents[1]
POST_DATE = "2026-05-23"
LAST_MODIFIED_AT = "2026-05-23T23:55:00+09:00"
KO_CATEGORY = "ko_Economy"
EN_CATEGORY = "en_Economy"


SOURCES = {
    "imf_weo": {
        "ko": "IMF World Economic Outlook April 2026",
        "en": "IMF World Economic Outlook April 2026",
        "url": "https://www.imf.org/en/publications/weo/issues/2026/04/14/world-economic-outlook-april-2026",
    },
    "imf_data": {
        "ko": "IMF World Economic Outlook Database",
        "en": "IMF World Economic Outlook Database",
        "url": "https://data.imf.org/Datasets/WEO",
    },
    "world_bank_gep": {
        "ko": "World Bank Global Economic Prospects",
        "en": "World Bank Global Economic Prospects",
        "url": "https://www.worldbank.org/en/publication/global-economic-prospects",
    },
    "oecd_outlook": {
        "ko": "OECD Economic Outlook",
        "en": "OECD Economic Outlook",
        "url": "https://www.oecd.org/economic-outlook/",
    },
    "fed_policy": {
        "ko": "Federal Reserve Monetary Policy",
        "en": "Federal Reserve Monetary Policy",
        "url": "https://www.federalreserve.gov/monetarypolicy.htm",
    },
    "bea_gdp": {
        "ko": "U.S. Bureau of Economic Analysis GDP",
        "en": "U.S. Bureau of Economic Analysis GDP",
        "url": "https://www.bea.gov/data/gdp/gross-domestic-product",
    },
    "bls_cpi": {
        "ko": "U.S. Bureau of Labor Statistics CPI",
        "en": "U.S. Bureau of Labor Statistics CPI",
        "url": "https://www.bls.gov/cpi/",
    },
    "bls_jobs": {
        "ko": "U.S. Bureau of Labor Statistics Employment Situation",
        "en": "U.S. Bureau of Labor Statistics Employment Situation",
        "url": "https://www.bls.gov/news.release/empsit.toc.htm",
    },
    "fred": {
        "ko": "Federal Reserve Economic Data",
        "en": "Federal Reserve Economic Data",
        "url": "https://fred.stlouisfed.org/",
    },
    "cfpb_budget": {
        "ko": "CFPB Budgeting Guide",
        "en": "CFPB Budgeting Guide",
        "url": "https://www.consumerfinance.gov/about-us/blog/budgeting-how-to-create-a-budget-and-stick-with-it/",
    },
    "cfpb_spending": {
        "ko": "CFPB Assess Your Spending",
        "en": "CFPB Assess Your Spending",
        "url": "https://www.consumerfinance.gov/owning-a-home/prepare/assess-your-spending/",
    },
    "cfpb_budget_pdf": {
        "ko": "CFPB Monthly Budget Tool",
        "en": "CFPB Monthly Budget Tool",
        "url": "https://files.consumerfinance.gov/f/documents/cfpb_well-being_monthly-budget.pdf",
    },
    "investor_compound": {
        "ko": "Investor.gov Compound Interest Calculator",
        "en": "Investor.gov Compound Interest Calculator",
        "url": "https://www.investor.gov/tools/calculators/compound-interest-calculator",
    },
    "sec_funds": {
        "ko": "SEC Mutual Funds and ETFs Guide",
        "en": "SEC Mutual Funds and ETFs Guide",
        "url": "https://www.sec.gov/about/reports-publications/investor-publications/introduction-mutual-funds",
    },
    "fdic_deposit": {
        "ko": "FDIC Deposit Insurance",
        "en": "FDIC Deposit Insurance",
        "url": "https://www.fdic.gov/resources/deposit-insurance/",
    },
    "bok_policy": {
        "ko": "Bank of Korea Monetary Policy",
        "en": "Bank of Korea Monetary Policy",
        "url": "https://www.bok.or.kr/eng/bbs/E0000634/list.do?menuNo=400069",
    },
    "bok_ecos": {
        "ko": "Bank of Korea ECOS",
        "en": "Bank of Korea ECOS",
        "url": "https://ecos.bok.or.kr/#/SearchStat",
    },
    "kosis": {
        "ko": "KOSIS Korean Statistical Information Service",
        "en": "KOSIS Korean Statistical Information Service",
        "url": "https://kosis.kr/eng/",
    },
}


TOPICS = [
    {
        "slug": "interest-rate-inflation-basics",
        "ko_title": "금리와 물가 기초: 중앙은행 뉴스를 생활비 언어로 읽기",
        "en_title": "Interest Rates and Inflation: Read Central Bank News in Household Terms",
        "ko_summary": "금리와 물가는 대출 이자, 예금 수익, 환율, 소비 심리로 연결되므로 숫자보다 전달 경로를 먼저 이해해야 한다.",
        "en_summary": "Interest rates and inflation affect loan costs, savings income, exchange rates, and spending decisions, so the transmission path matters more than one headline number.",
        "ko_focus": "금리 뉴스는 기준금리 하나가 아니라 물가 압력, 고용, 금융 안정, 환율 부담을 함께 보는 신호입니다.",
        "en_focus": "A rate decision is a signal about inflation pressure, employment, financial stability, and currency conditions, not only a single policy number.",
        "ko_actions": ["기준금리와 실제 대출금리를 분리합니다.", "물가 상승률과 기대 인플레이션을 함께 봅니다.", "가계 현금흐름에 미치는 월 단위 변화를 계산합니다."],
        "en_actions": ["Separate policy rates from actual borrowing rates.", "Read current inflation together with inflation expectations.", "Translate rate changes into monthly household cash flow."],
        "signals": ["policy rate", "consumer inflation", "expected inflation", "debt payment"],
        "ko_signals": ["기준금리", "소비자물가", "기대 인플레이션", "부채 상환액"],
        "sources": ["fed_policy", "bok_policy", "bls_cpi"],
        "tags": ["InterestRates", "Inflation", "CentralBanks", "Economy"],
    },
    {
        "slug": "exchange-rate-basics",
        "ko_title": "환율 기초: 원화 약세가 여행, 수입물가, 수출에 주는 영향",
        "en_title": "Exchange Rate Basics: Travel, Import Prices, and Exports",
        "ko_summary": "환율은 여행 경비뿐 아니라 에너지 수입, 식품 가격, 수출 채산성, 외화부채 부담을 동시에 움직인다.",
        "en_summary": "Exchange rates affect travel costs, imported energy, food prices, export margins, and foreign-currency debt at the same time.",
        "ko_focus": "환율이 오른다는 말은 한 통화 기준으로만 해석하면 헷갈립니다. 어느 통화가 강하고 약한지부터 적어야 합니다.",
        "en_focus": "Exchange-rate headlines are easy to misread unless the strong and weak currencies are named explicitly.",
        "ko_actions": ["원화 기준인지 달러 기준인지 먼저 적습니다.", "여행비와 수입물가 영향을 구분합니다.", "환율 변동이 기업과 가계에 반대로 작용하는 지점을 찾습니다."],
        "en_actions": ["Write whether the quote is from the won or dollar perspective.", "Separate travel cost effects from import-price effects.", "Find where households and exporters are affected differently."],
        "signals": ["currency quote", "import price", "travel cost", "export margin"],
        "ko_signals": ["환율 표시 방식", "수입물가", "여행 경비", "수출 채산성"],
        "sources": ["fred", "bok_ecos", "imf_data"],
        "tags": ["ExchangeRates", "KoreanWon", "Imports", "Exports"],
    },
    {
        "slug": "etf-vs-mutual-fund",
        "ko_title": "ETF와 펀드 차이: 수수료, 거래 방식, 세금을 먼저 비교하기",
        "en_title": "ETF vs Mutual Fund: Compare Fees, Trading, and Taxes First",
        "ko_summary": "ETF와 펀드는 모두 분산투자 도구일 수 있지만 거래 시간, 가격 결정, 비용, 세금 처리, 운용 방식이 다르다.",
        "en_summary": "ETFs and mutual funds can both provide diversification, but trading, pricing, fees, taxes, and management style differ.",
        "ko_focus": "상품 이름보다 중요한 것은 언제 어떤 가격으로 사고팔 수 있는지, 비용이 어디서 빠지는지입니다.",
        "en_focus": "The practical question is not the product label but when it trades, how it is priced, and where costs appear.",
        "ko_actions": ["총보수와 거래비용을 함께 확인합니다.", "장중 거래와 하루 1회 기준가 방식을 구분합니다.", "세금과 계좌 유형의 영향을 별도로 기록합니다."],
        "en_actions": ["Check expense ratios and trading costs together.", "Distinguish intraday trading from end-of-day NAV pricing.", "Record tax and account-type effects separately."],
        "signals": ["expense ratio", "trading price", "NAV", "tax account"],
        "ko_signals": ["총보수", "거래 가격", "기준가", "계좌 세금"],
        "sources": ["sec_funds", "fred", "cfpb_spending"],
        "tags": ["ETF", "MutualFunds", "Fees", "InvestingBasics"],
    },
    {
        "slug": "compound-interest-example",
        "ko_title": "복리 계산 예시: 수익률보다 기간과 추가 납입이 중요한 이유",
        "en_title": "Compound Interest Example: Time and Contributions Matter",
        "ko_summary": "복리는 이자가 다시 원금이 되는 구조이므로 수익률 하나보다 기간, 추가 납입, 세금, 물가를 함께 봐야 한다.",
        "en_summary": "Compound interest turns past gains into a larger base, so time, contributions, taxes, and inflation matter alongside return rate.",
        "ko_focus": "복리는 마법이 아니라 계산 방식입니다. 같은 수익률도 기간과 납입 주기가 달라지면 결과가 크게 달라집니다.",
        "en_focus": "Compounding is not magic; it is a calculation rule that changes outcomes when time and contribution cadence change.",
        "ko_actions": ["초기 금액, 월 납입액, 기간을 따로 둡니다.", "명목 수익률과 물가를 분리합니다.", "세금과 수수료를 차감한 뒤 다시 계산합니다."],
        "en_actions": ["Separate starting balance, monthly contribution, and years.", "Distinguish nominal return from inflation.", "Recalculate after taxes and fees."],
        "signals": ["starting balance", "contribution", "time horizon", "real return"],
        "ko_signals": ["초기 금액", "추가 납입", "투자 기간", "실질 수익률"],
        "sources": ["investor_compound", "bls_cpi", "sec_funds"],
        "tags": ["CompoundInterest", "Saving", "Inflation", "Finance"],
    },
    {
        "slug": "household-budget-50-30-20",
        "ko_title": "50/30/20 예산법: 규칙보다 고정비와 현금흐름 먼저 보기",
        "en_title": "50/30/20 Budget Rule: Start With Fixed Costs and Cash Flow",
        "ko_summary": "50/30/20 예산법은 출발점으로 유용하지만 소득 주기, 주거비, 부채, 비상금 목표에 맞게 조정해야 한다.",
        "en_summary": "The 50/30/20 budget rule is a useful starting point, but it must be adjusted for pay timing, housing costs, debt, and emergency savings goals.",
        "ko_focus": "예산 비율은 생활을 자동으로 고치지 않습니다. 먼저 빠져나가는 고정비와 결제일을 달력에 올려야 합니다.",
        "en_focus": "A budget ratio does not fix spending by itself. The first step is mapping fixed costs and due dates on a calendar.",
        "ko_actions": ["세후 소득을 기준으로 계산합니다.", "고정비와 변동비를 분리합니다.", "비율이 맞지 않는 이유를 주거비, 부채, 소득 변동으로 나눕니다."],
        "en_actions": ["Use after-tax income as the base.", "Separate fixed and variable expenses.", "Explain mismatches through housing, debt, or income volatility."],
        "signals": ["after-tax income", "fixed cost", "variable spending", "savings target"],
        "ko_signals": ["세후 소득", "고정비", "변동비", "저축 목표"],
        "sources": ["cfpb_budget", "cfpb_budget_pdf", "cfpb_spending"],
        "tags": ["Budgeting", "HouseholdFinance", "CashFlow", "Saving"],
    },
    {
        "slug": "emergency-fund-how-much",
        "ko_title": "비상금은 얼마가 적당할까: 3개월보다 먼저 봐야 할 생활비",
        "en_title": "How Much Emergency Fund Is Enough? Start With Essential Costs",
        "ko_summary": "비상금 목표는 몇 개월치라는 숫자보다 필수 생활비, 소득 안정성, 보험 공백, 부채 비용에 따라 달라진다.",
        "en_summary": "Emergency fund targets depend on essential expenses, income stability, insurance gaps, and debt cost more than one fixed month rule.",
        "ko_focus": "비상금은 수익을 높이는 돈이 아니라 예상 못 한 지출이 고금리 부채로 번지는 것을 막는 완충 장치입니다.",
        "en_focus": "An emergency fund is a buffer against high-cost debt, not a return-maximizing account.",
        "ko_actions": ["한 달 필수비부터 계산합니다.", "소득이 불안정하면 목표 개월 수를 늘립니다.", "보험 자기부담금과 가족 돌봄 비용을 따로 넣습니다."],
        "en_actions": ["Calculate one month of essential expenses first.", "Raise the target if income is unstable.", "Add deductibles and family-care obligations separately."],
        "signals": ["essential expense", "income stability", "deductible", "debt cost"],
        "ko_signals": ["필수 생활비", "소득 안정성", "자기부담금", "부채 비용"],
        "sources": ["cfpb_budget", "fdic_deposit", "cfpb_spending"],
        "tags": ["EmergencyFund", "Saving", "Budgeting", "Risk"],
    },
    {
        "slug": "recession-indicators-basics",
        "ko_title": "경기 침체 지표 읽기: GDP, 고용, 소비를 한 번에 보기",
        "en_title": "Recession Indicators: Read GDP, Jobs, and Consumption Together",
        "ko_summary": "경기 침체 신호는 GDP 한 줄이 아니라 고용, 실질소득, 소비, 기업투자, 금융여건이 동시에 약해지는지로 판단한다.",
        "en_summary": "Recession signals are stronger when GDP, jobs, real income, consumption, investment, and financial conditions weaken together.",
        "ko_focus": "침체라는 단어는 정치적 논쟁보다 가계와 기업의 현금흐름이 동시에 줄어드는지를 보는 데 써야 합니다.",
        "en_focus": "Recession analysis should focus on whether household and business cash flows weaken together, not on one politicized label.",
        "ko_actions": ["실질 GDP와 고용지표를 같이 봅니다.", "소비와 투자 중 어느 쪽이 먼저 꺾였는지 봅니다.", "한 달 수치보다 여러 달 방향을 확인합니다."],
        "en_actions": ["Read real GDP with labor-market data.", "Check whether consumption or investment weakened first.", "Use multi-month direction instead of one release."],
        "signals": ["real GDP", "employment", "real income", "business investment"],
        "ko_signals": ["실질 GDP", "고용", "실질소득", "기업투자"],
        "sources": ["bea_gdp", "bls_jobs", "fred"],
        "tags": ["Recession", "GDP", "LaborMarket", "Indicators"],
    },
    {
        "slug": "real-wage-purchasing-power",
        "ko_title": "실질임금과 구매력: 월급이 올랐는데 왜 빠듯한지 계산하기",
        "en_title": "Real Wages and Purchasing Power: Why Raises Can Still Feel Tight",
        "ko_summary": "월급 인상률이 물가 상승률보다 낮으면 명목 소득은 늘어도 실제 구매력은 줄어들 수 있다.",
        "en_summary": "When wage growth trails inflation, nominal income can rise while actual purchasing power falls.",
        "ko_focus": "체감 경제는 평균 임금보다 내 소비 바구니의 가격과 세후 소득이 어떻게 바뀌었는지에서 결정됩니다.",
        "en_focus": "Household economic pressure depends on after-tax income and the prices in a specific spending basket, not only average wages.",
        "ko_actions": ["세전 임금과 세후 입금액을 분리합니다.", "자주 사는 항목의 가격 변화를 기록합니다.", "명목 증가율에서 물가 상승률을 뺀 실질 변화를 봅니다."],
        "en_actions": ["Separate gross pay from take-home pay.", "Track prices for frequent purchases.", "Subtract inflation from nominal growth to estimate real change."],
        "signals": ["nominal wage", "after-tax income", "CPI", "real wage"],
        "ko_signals": ["명목임금", "세후소득", "소비자물가", "실질임금"],
        "sources": ["bls_cpi", "bls_jobs", "kosis"],
        "tags": ["Wages", "Inflation", "PurchasingPower", "Households"],
    },
    {
        "slug": "cpi-vs-personal-inflation",
        "ko_title": "CPI와 개인 물가 차이: 공식 물가와 체감 물가가 다른 이유",
        "en_title": "CPI vs Personal Inflation: Why Official Inflation Feels Different",
        "ko_summary": "CPI는 평균 소비 바구니를 추적하므로 주거, 식품, 교통 비중이 다른 개인의 체감 물가와 다를 수 있다.",
        "en_summary": "CPI tracks an average basket, so personal inflation can differ when housing, food, transport, or medical spending weights are different.",
        "ko_focus": "공식 물가가 틀렸다고 보기 전에 내 지출 비중이 CPI 가중치와 얼마나 다른지 확인해야 합니다.",
        "en_focus": "Before rejecting official inflation, compare your spending weights with the index basket.",
        "ko_actions": ["한 달 지출을 항목별 비중으로 나눕니다.", "주거비와 식비처럼 큰 항목을 따로 봅니다.", "공식 CPI는 방향, 개인 장부는 생활 판단에 씁니다."],
        "en_actions": ["Break monthly spending into category weights.", "Review large categories such as housing and food separately.", "Use official CPI for broad direction and personal records for decisions."],
        "signals": ["CPI basket", "spending weight", "housing cost", "food price"],
        "ko_signals": ["CPI 바구니", "지출 비중", "주거비", "식품 가격"],
        "sources": ["bls_cpi", "kosis", "cfpb_budget_pdf"],
        "tags": ["CPI", "Inflation", "CostOfLiving", "Budgeting"],
    },
    {
        "slug": "gdp-components-guide",
        "ko_title": "GDP 구성요소 읽기: 소비, 투자, 정부, 순수출을 나눠 보기",
        "en_title": "GDP Components: Read Consumption, Investment, Government, and Net Exports",
        "ko_summary": "GDP 성장률은 하나의 숫자지만 그 안에는 소비, 기업투자, 주택, 정부지출, 수출입 변화가 섞여 있다.",
        "en_summary": "GDP growth is one number, but it combines consumption, business investment, housing, government spending, and trade changes.",
        "ko_focus": "성장률이 같아도 소비가 강한 성장과 재고가 쌓인 성장은 의미가 다릅니다.",
        "en_focus": "The same growth rate can mean different things if it comes from consumer demand, inventories, exports, or government spending.",
        "ko_actions": ["헤드라인 성장률보다 구성요소 기여도를 봅니다.", "일회성 재고 변화와 최종수요를 구분합니다.", "수출입이 성장률을 밀었는지 끌어내렸는지 확인합니다."],
        "en_actions": ["Read component contributions below the headline.", "Separate inventory swings from final demand.", "Check whether trade lifted or reduced growth."],
        "signals": ["personal consumption", "private investment", "government spending", "net exports"],
        "ko_signals": ["민간소비", "민간투자", "정부지출", "순수출"],
        "sources": ["bea_gdp", "fred", "imf_data"],
        "tags": ["GDP", "Macroeconomics", "Growth", "Indicators"],
    },
    {
        "slug": "unemployment-rate-labor-market",
        "ko_title": "실업률과 노동시장: 낮은 실업률만 보면 놓치는 신호",
        "en_title": "Unemployment Rate and Labor Market Signals Beyond the Headline",
        "ko_summary": "실업률은 중요하지만 고용률, 경제활동참가율, 임금, 근로시간을 함께 봐야 노동시장 압력을 이해할 수 있다.",
        "en_summary": "The unemployment rate matters, but employment, participation, wages, and hours worked are needed to understand labor-market pressure.",
        "ko_focus": "낮은 실업률은 좋은 신호일 수 있지만 구직 포기, 단시간 근로, 실질임금 약화를 가릴 수도 있습니다.",
        "en_focus": "Low unemployment can be positive, but it may hide weak participation, involuntary part-time work, or soft real wages.",
        "ko_actions": ["실업률과 경제활동참가율을 같이 봅니다.", "명목임금과 실질임금을 나눕니다.", "업종별 고용 변화가 넓은지 특정 부문에 치우쳤는지 봅니다."],
        "en_actions": ["Read unemployment with labor-force participation.", "Separate nominal and real wage changes.", "Check whether job growth is broad or sector-specific."],
        "signals": ["unemployment rate", "participation rate", "wage growth", "hours worked"],
        "ko_signals": ["실업률", "경제활동참가율", "임금 상승률", "근로시간"],
        "sources": ["bls_jobs", "fred", "kosis"],
        "tags": ["LaborMarket", "Jobs", "Wages", "Economy"],
    },
    {
        "slug": "central-bank-meeting-how-to-read",
        "ko_title": "중앙은행 회의 읽는 법: 결정문, 전망, 기자회견을 분리하기",
        "en_title": "How to Read a Central Bank Meeting: Statement, Projections, Press Conference",
        "ko_summary": "중앙은행 회의는 금리 결정뿐 아니라 결정문 문구, 경제전망, 기자회견의 위험 균형을 함께 읽어야 한다.",
        "en_summary": "A central bank meeting includes the rate decision, statement language, projections, and the risk balance in the press conference.",
        "ko_focus": "시장은 금리 자체보다 다음 회의에 대한 힌트와 위험 판단이 바뀌었는지를 더 크게 반응할 때가 많습니다.",
        "en_focus": "Markets often react less to the rate itself and more to changed guidance about the next decision.",
        "ko_actions": ["이전 결정문과 달라진 단어를 표시합니다.", "성장과 물가 전망의 수정 방향을 봅니다.", "가계부채나 환율 같은 금융안정 언급을 따로 적습니다."],
        "en_actions": ["Mark words that changed from the previous statement.", "Check revisions to growth and inflation projections.", "Record financial-stability comments such as debt or currency pressure."],
        "signals": ["policy statement", "projection", "guidance", "financial stability"],
        "ko_signals": ["정책 결정문", "경제전망", "향후 지침", "금융안정"],
        "sources": ["fed_policy", "bok_policy", "oecd_outlook"],
        "tags": ["CentralBanks", "MonetaryPolicy", "Rates", "Inflation"],
    },
    {
        "slug": "bond-yield-curve-basics",
        "ko_title": "채권 금리와 수익률 곡선: 장단기 금리가 말하는 경기 기대",
        "en_title": "Bond Yields and the Yield Curve: What Short and Long Rates Signal",
        "ko_summary": "수익률 곡선은 단기 정책금리 기대와 장기 성장·물가·위험 프리미엄을 함께 반영한다.",
        "en_summary": "The yield curve reflects expected short rates, long-run growth, inflation, and risk premiums together.",
        "ko_focus": "장단기 금리 차이는 침체 예측 도구로 유명하지만 신호의 의미는 통화정책 경로와 물가 기대에 따라 달라집니다.",
        "en_focus": "The yield curve is often treated as a recession signal, but its meaning depends on policy expectations and inflation risk.",
        "ko_actions": ["2년물과 10년물 금리를 같이 봅니다.", "실질금리와 명목금리를 구분합니다.", "금리 역전이 얼마나 오래 지속되는지 확인합니다."],
        "en_actions": ["Compare two-year and ten-year yields.", "Separate nominal and real rates.", "Check how long an inversion persists."],
        "signals": ["short yield", "long yield", "curve inversion", "term premium"],
        "ko_signals": ["단기금리", "장기금리", "금리 역전", "기간 프리미엄"],
        "sources": ["fred", "fed_policy", "imf_data"],
        "tags": ["Bonds", "YieldCurve", "InterestRates", "Recession"],
    },
    {
        "slug": "household-debt-service-ratio",
        "ko_title": "가계부채 부담 읽기: 대출 잔액보다 월 상환액이 먼저다",
        "en_title": "Household Debt Burden: Monthly Payments Matter Before Balances",
        "ko_summary": "가계부채 위험은 총잔액만이 아니라 소득 대비 원리금 상환액, 변동금리 비중, 만기 구조로 판단해야 한다.",
        "en_summary": "Household debt risk depends on payments relative to income, variable-rate exposure, and maturity structure, not only total balances.",
        "ko_focus": "같은 대출 잔액도 금리와 만기에 따라 매달 버틸 수 있는 부담이 달라집니다.",
        "en_focus": "The same loan balance can be manageable or stressful depending on interest rate, maturity, and income stability.",
        "ko_actions": ["월 원리금 상환액을 세후 소득과 비교합니다.", "변동금리와 고정금리 비중을 나눕니다.", "금리 상승 시나리오를 월 단위로 계산합니다."],
        "en_actions": ["Compare monthly debt payments with take-home income.", "Separate variable-rate and fixed-rate exposure.", "Run a monthly payment scenario for higher rates."],
        "signals": ["debt payment", "take-home income", "variable rate", "refinancing date"],
        "ko_signals": ["월 상환액", "세후 소득", "변동금리", "만기일"],
        "sources": ["cfpb_spending", "bok_ecos", "fed_policy"],
        "tags": ["HouseholdDebt", "Loans", "InterestRates", "CashFlow"],
    },
    {
        "slug": "current-account-trade-balance",
        "ko_title": "경상수지와 무역수지: 수출이 좋아도 환율이 흔들릴 수 있는 이유",
        "en_title": "Current Account and Trade Balance: Why Exports Do Not Explain Everything",
        "ko_summary": "무역수지는 상품 수출입만 보지만 경상수지는 서비스, 소득, 이전까지 포함해 외화 흐름을 더 넓게 보여 준다.",
        "en_summary": "The trade balance tracks goods and services trade, while the current account adds income and transfers to show broader external flows.",
        "ko_focus": "수출이 좋아도 에너지 수입, 해외 배당, 서비스수지, 자본 흐름 때문에 환율은 다르게 움직일 수 있습니다.",
        "en_focus": "Even strong exports can coexist with currency pressure when energy imports, income flows, services, or capital flows shift.",
        "ko_actions": ["상품수지와 서비스수지를 분리합니다.", "에너지 수입액 변화를 확인합니다.", "경상수지와 환율을 같은 방향으로 단정하지 않습니다."],
        "en_actions": ["Separate goods balance from services balance.", "Check changes in energy import values.", "Avoid assuming the current account and exchange rate move one-for-one."],
        "signals": ["goods balance", "services balance", "income flow", "energy imports"],
        "ko_signals": ["상품수지", "서비스수지", "소득수지", "에너지 수입"],
        "sources": ["bok_ecos", "imf_data", "world_bank_gep"],
        "tags": ["TradeBalance", "CurrentAccount", "ExchangeRates", "Korea"],
    },
    {
        "slug": "oil-price-import-inflation",
        "ko_title": "유가와 수입물가: 국제유가가 전기요금과 장바구니까지 오는 경로",
        "en_title": "Oil Prices and Import Inflation: From Crude Markets to Household Bills",
        "ko_summary": "유가 상승은 원유 수입액, 정제비, 전기·가스요금, 운송비, 식품가격을 거쳐 생활비로 번질 수 있다.",
        "en_summary": "Higher oil prices can pass through crude imports, refining, power and gas bills, transport costs, and food prices.",
        "ko_focus": "국제유가 뉴스는 주유소 가격만 보는 것이 아니라 환율과 에너지 수입 의존도까지 함께 봐야 합니다.",
        "en_focus": "Oil-price news should be read with exchange rates and import dependence, not only pump prices.",
        "ko_actions": ["달러 유가와 원화 환산 유가를 같이 봅니다.", "전기·가스요금 조정 시차를 확인합니다.", "운송비가 식품·택배비로 전가되는 경로를 적습니다."],
        "en_actions": ["Compare dollar oil prices with local-currency oil costs.", "Check the lag in utility-price adjustment.", "Map transport cost pass-through to food and delivery prices."],
        "signals": ["oil price", "exchange rate", "utility tariff", "transport cost"],
        "ko_signals": ["국제유가", "환율", "공공요금", "운송비"],
        "sources": ["imf_weo", "world_bank_gep", "bok_ecos"],
        "tags": ["OilPrices", "ImportInflation", "Energy", "CostOfLiving"],
    },
    {
        "slug": "semiconductor-cycle-korea-economy",
        "ko_title": "반도체 경기와 한국 경제: 수출 호황이 모두에게 같지 않은 이유",
        "en_title": "Semiconductor Cycle and Korea: Why Export Booms Feel Uneven",
        "ko_summary": "반도체 수출은 한국 성장률을 끌어올릴 수 있지만 고용, 내수, 중소기업, 지역경제로 전달되는 속도는 다르다.",
        "en_summary": "Semiconductor exports can lift Korean growth, but the pass-through to jobs, domestic demand, SMEs, and regions can be uneven.",
        "ko_focus": "수출 헤드라인이 강해도 비IT 부문과 소비가 약하면 체감 경기는 다르게 나타납니다.",
        "en_focus": "Strong export headlines can coexist with weak domestic sentiment if non-IT sectors and consumption lag.",
        "ko_actions": ["전체 수출과 반도체 수출을 분리합니다.", "설비투자와 고용으로 이어지는지 봅니다.", "내수 서비스업 지표와 함께 읽습니다."],
        "en_actions": ["Separate total exports from semiconductor exports.", "Check whether export strength feeds equipment investment and jobs.", "Read it with domestic service indicators."],
        "signals": ["chip exports", "facility investment", "non-IT sector", "domestic demand"],
        "ko_signals": ["반도체 수출", "설비투자", "비IT 부문", "내수"],
        "sources": ["bok_ecos", "kosis", "world_bank_gep"],
        "tags": ["Semiconductors", "KoreaEconomy", "Exports", "Growth"],
    },
    {
        "slug": "fiscal-deficit-public-debt",
        "ko_title": "재정적자와 국가채무: 좋은 지출과 지속가능성을 같이 보기",
        "en_title": "Fiscal Deficits and Public Debt: Read Support and Sustainability Together",
        "ko_summary": "재정적자는 경기 충격을 완충할 수 있지만 이자비용, 성장률, 세입 기반, 고령화 지출과 함께 봐야 지속가능성을 판단할 수 있다.",
        "en_summary": "Fiscal deficits can cushion shocks, but sustainability depends on interest costs, growth, revenue base, and aging-related spending.",
        "ko_focus": "적자가 항상 나쁘거나 항상 좋은 것은 아닙니다. 문제는 지출 목적과 미래 상환 능력입니다.",
        "en_focus": "A deficit is not automatically good or bad. The key is the purpose of spending and future repayment capacity.",
        "ko_actions": ["일시적 경기 대응과 구조적 적자를 구분합니다.", "이자비용이 세입에서 차지하는 비중을 봅니다.", "성장률보다 부채비율이 빨리 오르는지 확인합니다."],
        "en_actions": ["Separate temporary stabilization from structural deficit.", "Compare interest cost with revenue.", "Check whether debt ratio rises faster than growth."],
        "signals": ["budget balance", "interest cost", "debt ratio", "growth rate"],
        "ko_signals": ["재정수지", "이자비용", "채무비율", "성장률"],
        "sources": ["imf_data", "world_bank_gep", "oecd_outlook"],
        "tags": ["FiscalPolicy", "PublicDebt", "Budget", "Economy"],
    },
    {
        "slug": "dollar-won-exchange-rate-checklist",
        "ko_title": "원달러 환율 체크리스트: 뉴스 한 줄보다 금리차, 유가, 수지를 같이 보기",
        "en_title": "Dollar-Won Exchange Rate Checklist: Rates, Oil, and External Balance",
        "ko_summary": "원달러 환율은 금리차, 에너지 가격, 수출입, 위험선호, 외국인 자금 흐름이 동시에 반영되는 가격이다.",
        "en_summary": "The dollar-won rate reflects rate differentials, energy prices, trade flows, risk appetite, and foreign capital movements together.",
        "ko_focus": "환율을 한 가지 이유로 설명하면 대개 틀립니다. 최소한 금리, 유가, 수지를 같은 표에 넣어야 합니다.",
        "en_focus": "Explaining a currency with one cause is usually fragile; rates, oil, and external balances should be checked together.",
        "ko_actions": ["미국과 한국의 정책금리 방향을 비교합니다.", "원화 기준 유가 부담을 계산합니다.", "무역수지와 외국인 자금 흐름을 나눠 봅니다."],
        "en_actions": ["Compare U.S. and Korean policy-rate direction.", "Translate oil prices into won costs.", "Separate trade balance from portfolio flows."],
        "signals": ["rate differential", "oil cost", "trade balance", "capital flow"],
        "ko_signals": ["금리차", "유가 부담", "무역수지", "자본 흐름"],
        "sources": ["fred", "bok_policy", "bok_ecos"],
        "tags": ["KoreanWon", "ExchangeRates", "Rates", "Oil"],
    },
    {
        "slug": "savings-rate-real-interest-rate",
        "ko_title": "저축금리와 실질금리: 예금 이자가 물가를 이기는지 확인하기",
        "en_title": "Savings Rates and Real Interest: Check Whether Interest Beats Inflation",
        "ko_summary": "예금금리가 높아 보여도 세금과 물가를 빼면 실제 구매력 증가가 작거나 마이너스일 수 있다.",
        "en_summary": "A high deposit rate can still produce little or negative purchasing-power growth after taxes and inflation.",
        "ko_focus": "저축은 안전성과 유동성이 장점이지만 실질금리를 보지 않으면 구매력 보존 여부를 놓칩니다.",
        "en_focus": "Savings provide safety and liquidity, but real interest determines whether purchasing power is preserved.",
        "ko_actions": ["세전 금리와 세후 금리를 구분합니다.", "세후 금리에서 물가 상승률을 뺍니다.", "예금자보호 한도와 만기 유동성을 확인합니다."],
        "en_actions": ["Separate pre-tax and after-tax yield.", "Subtract inflation from after-tax yield.", "Check deposit insurance limits and maturity liquidity."],
        "signals": ["deposit rate", "tax", "inflation", "deposit insurance"],
        "ko_signals": ["예금금리", "세금", "물가", "예금자보호"],
        "sources": ["fdic_deposit", "bls_cpi", "bok_ecos"],
        "tags": ["Saving", "RealInterest", "Inflation", "Banking"],
    },
    {
        "slug": "mortgage-rate-rent-affordability",
        "ko_title": "주택담보대출 금리와 임대료: 집값보다 월 부담액 먼저 계산하기",
        "en_title": "Mortgage Rates and Rent Affordability: Calculate Monthly Burden First",
        "ko_summary": "주거비 판단은 집값, 전세금, 월세만이 아니라 금리, 보증금 기회비용, 관리비, 소득 안정성을 함께 계산해야 한다.",
        "en_summary": "Housing affordability depends on price, rent, rates, deposit opportunity cost, fees, and income stability together.",
        "ko_focus": "주택 선택은 자산 가격 전망보다 매달 버틸 수 있는 현금흐름을 먼저 확인해야 합니다.",
        "en_focus": "Housing decisions should begin with monthly cash flow before asset-price expectations.",
        "ko_actions": ["대출 원리금, 월세, 관리비를 한 줄에 놓습니다.", "보증금의 기회비용을 계산합니다.", "금리 상승과 소득 감소 시나리오를 같이 봅니다."],
        "en_actions": ["Place mortgage payment, rent, and fees in one line.", "Calculate opportunity cost of deposits.", "Run scenarios for higher rates and lower income."],
        "signals": ["mortgage payment", "rent", "deposit cost", "income stability"],
        "ko_signals": ["대출 상환액", "월세", "보증금 비용", "소득 안정성"],
        "sources": ["cfpb_spending", "fed_policy", "bok_ecos"],
        "tags": ["Housing", "Mortgage", "Rent", "Affordability"],
    },
    {
        "slug": "credit-card-interest-minimum-payment",
        "ko_title": "신용카드 이자와 최소결제: 잔액이 오래 남는 구조 이해하기",
        "en_title": "Credit Card Interest and Minimum Payments: Why Balances Last",
        "ko_summary": "최소결제만 반복하면 원금이 천천히 줄고 이자가 누적되어 작은 소비도 장기 부채가 될 수 있다.",
        "en_summary": "Repeated minimum payments reduce principal slowly and let interest accumulate, turning small purchases into long-lasting debt.",
        "ko_focus": "신용카드 비용은 결제일을 넘긴 순간 물건 가격이 아니라 시간과 이자를 포함한 부채가 됩니다.",
        "en_focus": "Once a balance carries over, a purchase becomes a debt with time and interest attached.",
        "ko_actions": ["연이율을 월 이자 부담으로 바꿉니다.", "최소결제와 고정 추가상환을 비교합니다.", "새 사용을 멈춘 상태의 상환 기간을 계산합니다."],
        "en_actions": ["Translate APR into monthly interest cost.", "Compare minimum payment with fixed extra payment.", "Estimate payoff time with new spending stopped."],
        "signals": ["APR", "minimum payment", "principal", "payoff time"],
        "ko_signals": ["연이율", "최소결제", "원금", "상환 기간"],
        "sources": ["cfpb_budget", "cfpb_spending", "fed_policy"],
        "tags": ["CreditCards", "Debt", "Interest", "Budgeting"],
    },
    {
        "slug": "supply-chain-shock-inflation",
        "ko_title": "공급망 충격과 물가: 운임, 재고, 대체 공급처를 같이 보기",
        "en_title": "Supply Chain Shocks and Inflation: Freight, Inventories, and Substitutes",
        "ko_summary": "공급망 충격은 운임, 배송 지연, 재고 비용, 대체 공급처 비용을 통해 소비자 가격으로 이어질 수 있다.",
        "en_summary": "Supply-chain shocks can move into consumer prices through freight, delays, inventory costs, and expensive substitute suppliers.",
        "ko_focus": "공급망 뉴스는 항만 문제로 끝나지 않고 기업 마진, 제품 가격, 소비자 선택지 축소로 이어질 수 있습니다.",
        "en_focus": "Supply-chain news can travel from ports to margins, product prices, and fewer consumer choices.",
        "ko_actions": ["충격이 원자재, 부품, 운송 중 어디서 발생했는지 나눕니다.", "재고가 몇 달 버틸 수 있는지 봅니다.", "대체 공급처가 가격을 얼마나 올리는지 확인합니다."],
        "en_actions": ["Classify the shock as raw material, component, or transport.", "Check how many months inventory can absorb it.", "Estimate the cost of substitute suppliers."],
        "signals": ["freight cost", "delivery lag", "inventory buffer", "supplier concentration"],
        "ko_signals": ["운임", "배송 지연", "재고 완충", "공급처 집중도"],
        "sources": ["world_bank_gep", "oecd_outlook", "imf_weo"],
        "tags": ["SupplyChains", "Inflation", "Trade", "Business"],
    },
    {
        "slug": "productivity-wage-growth",
        "ko_title": "생산성과 임금: 경제가 좋아져도 임금이 늦게 움직이는 이유",
        "en_title": "Productivity and Wages: Why Pay Can Lag a Better Economy",
        "ko_summary": "생산성 증가는 장기 임금 여력을 높일 수 있지만 산업 구조, 협상력, 물가, 고용 형태에 따라 체감 속도가 달라진다.",
        "en_summary": "Productivity growth can support wages over time, but industry structure, bargaining power, inflation, and job type shape the pass-through.",
        "ko_focus": "경제 전체 생산성이 올라가도 그 이익이 모든 근로자에게 같은 속도로 전달되지는 않습니다.",
        "en_focus": "Even when the economy becomes more productive, gains do not reach every worker at the same speed.",
        "ko_actions": ["산업별 생산성과 임금을 분리합니다.", "명목임금보다 실질임금 변화를 봅니다.", "고용 형태와 근로시간 변화를 함께 확인합니다."],
        "en_actions": ["Compare productivity and wages by industry.", "Use real wage changes rather than nominal wages alone.", "Read employment type and hours worked together."],
        "signals": ["productivity", "real wage", "industry mix", "labor share"],
        "ko_signals": ["생산성", "실질임금", "산업 구성", "노동소득분배"],
        "sources": ["bls_jobs", "fred", "oecd_outlook"],
        "tags": ["Productivity", "Wages", "LaborMarket", "Growth"],
    },
    {
        "slug": "inflation-expectations-guide",
        "ko_title": "기대 인플레이션 읽기: 사람들이 믿는 물가가 실제 물가에 미치는 영향",
        "en_title": "Inflation Expectations: Why Beliefs About Prices Matter",
        "ko_summary": "기대 인플레이션은 임금 협상, 가격 책정, 중앙은행 신뢰, 장기 금리에 영향을 주는 중요한 경제 신호다.",
        "en_summary": "Inflation expectations influence wage bargaining, price setting, central-bank credibility, and long-term interest rates.",
        "ko_focus": "물가가 이미 오른 것만큼 중요한 것은 사람들이 앞으로도 계속 오를 것이라고 믿는지입니다.",
        "en_focus": "Past inflation matters, but expectations about future inflation can change behavior today.",
        "ko_actions": ["현재 CPI와 기대 인플레이션을 나눠 봅니다.", "단기 기대와 장기 기대를 구분합니다.", "중앙은행 목표와 기대치의 차이를 확인합니다."],
        "en_actions": ["Separate current CPI from expected inflation.", "Distinguish short-run and long-run expectations.", "Compare expectations with the central bank target."],
        "signals": ["current CPI", "short expectation", "long expectation", "inflation target"],
        "ko_signals": ["현재 CPI", "단기 기대", "장기 기대", "물가 목표"],
        "sources": ["fed_policy", "bls_cpi", "fred"],
        "tags": ["InflationExpectations", "CPI", "CentralBanks", "Rates"],
    },
    {
        "slug": "global-growth-forecast-how-to-read",
        "ko_title": "세계 성장률 전망 읽기: IMF·OECD·World Bank 숫자가 다른 이유",
        "en_title": "How to Read Global Growth Forecasts from IMF, OECD, and World Bank",
        "ko_summary": "세계 성장률 전망은 기관별 기준일, 국가 범위, 환율 기준, 위험 가정이 달라 숫자가 서로 다를 수 있다.",
        "en_summary": "Global growth forecasts differ because institutions use different cut-off dates, country coverage, exchange-rate assumptions, and risk scenarios.",
        "ko_focus": "전망 숫자는 정답이 아니라 가정이 붙은 시나리오입니다. 언제 어떤 정보까지 반영했는지가 중요합니다.",
        "en_focus": "A forecast is not a fact; it is a scenario with assumptions and a data cut-off date.",
        "ko_actions": ["발표일과 데이터 기준일을 확인합니다.", "기본 전망과 하방 위험을 분리합니다.", "한국 수출과 에너지 수입에 영향을 줄 경로를 표시합니다."],
        "en_actions": ["Check publication date and data cut-off.", "Separate baseline projection from downside risks.", "Map channels to Korean exports and energy imports."],
        "signals": ["forecast date", "baseline", "downside risk", "Korea channel"],
        "ko_signals": ["전망 기준일", "기본 전망", "하방 위험", "한국 전달 경로"],
        "sources": ["imf_weo", "oecd_outlook", "world_bank_gep"],
        "tags": ["GlobalEconomy", "Forecasts", "IMF", "OECD"],
    },
    {
        "slug": "trade-tariff-household-prices",
        "ko_title": "관세와 생활물가: 무역정책이 소비자 가격으로 오는 경로",
        "en_title": "Tariffs and Household Prices: How Trade Policy Reaches Consumers",
        "ko_summary": "관세는 수입업체 비용, 환율, 유통마진, 대체재 가격을 거쳐 소비자 가격과 기업 선택에 영향을 준다.",
        "en_summary": "Tariffs affect consumer prices through importer costs, exchange rates, margins, substitutes, and business sourcing decisions.",
        "ko_focus": "관세는 해외 기업만 내는 비용처럼 보이지만 실제 부담은 공급망 안에서 나뉘어 소비자에게 일부 전가될 수 있습니다.",
        "en_focus": "A tariff may be charged at the border, but the burden can be shared across suppliers, firms, and consumers.",
        "ko_actions": ["관세 대상 품목과 대체재를 확인합니다.", "수입업체가 가격을 올릴 여지가 있는지 봅니다.", "환율 변화가 관세 효과를 키우는지 줄이는지 계산합니다."],
        "en_actions": ["Identify tariffed goods and substitutes.", "Check whether importers can pass costs through.", "Calculate whether exchange-rate moves amplify or offset the tariff."],
        "signals": ["tariff rate", "import share", "substitute", "pass-through"],
        "ko_signals": ["관세율", "수입 비중", "대체재", "가격 전가"],
        "sources": ["world_bank_gep", "oecd_outlook", "imf_weo"],
        "tags": ["Tariffs", "Trade", "Inflation", "Households"],
    },
    {
        "slug": "emergency-budget-job-loss",
        "ko_title": "실직 대비 비상 예산: 평상시 예산과 위기 예산을 나누기",
        "en_title": "Emergency Budget for Job Loss: Separate Normal and Crisis Spending",
        "ko_summary": "실직 가능성에 대비하려면 평상시 예산과 별도로 필수비, 중단 가능한 지출, 현금화 순서, 지원 제도를 정리해야 한다.",
        "en_summary": "A job-loss budget separates essential costs, pausable spending, cash drawdown order, and support programs from the normal budget.",
        "ko_focus": "위기 예산은 불안을 키우기 위한 문서가 아니라 판단을 빠르게 하기 위한 사전 순서표입니다.",
        "en_focus": "A crisis budget is not a fear document; it is a decision order prepared before stress is highest.",
        "ko_actions": ["필수비와 중단 가능한 지출을 표시합니다.", "비상금 사용 순서를 정합니다.", "보험, 실업급여, 가족 지원 가능성을 확인합니다."],
        "en_actions": ["Mark essential and pausable expenses.", "Set the order for using emergency cash.", "Check insurance, unemployment support, and family-support options."],
        "signals": ["essential cost", "pausable spending", "cash runway", "support program"],
        "ko_signals": ["필수비", "중단 가능 지출", "현금 버팀 기간", "지원 제도"],
        "sources": ["cfpb_budget", "cfpb_budget_pdf", "bls_jobs"],
        "tags": ["EmergencyBudget", "JobLoss", "CashFlow", "Budgeting"],
    },
    {
        "slug": "deposit-insurance-bank-risk",
        "ko_title": "예금자보호와 은행 리스크: 금리보다 안전 한도를 먼저 확인하기",
        "en_title": "Deposit Insurance and Bank Risk: Check Safety Limits Before Yield",
        "ko_summary": "예금 선택에서는 높은 금리뿐 아니라 예금자보호 대상, 한도, 계좌 소유 구조, 만기 유동성을 확인해야 한다.",
        "en_summary": "Deposit decisions should consider insurance coverage, limits, account ownership, and maturity liquidity alongside yield.",
        "ko_focus": "예금은 단순한 투자상품이 아니라 결제와 비상자금의 기반이므로 안전 한도를 먼저 봐야 합니다.",
        "en_focus": "Deposits support payments and emergency cash, so safety coverage comes before chasing yield.",
        "ko_actions": ["보호 대상 금융기관인지 확인합니다.", "보호 한도를 계좌 소유 구조별로 봅니다.", "비상금은 만기 전에 필요한지 확인합니다."],
        "en_actions": ["Confirm whether the institution is covered.", "Check coverage limits by ownership category.", "Keep emergency cash accessible before maturity."],
        "signals": ["insured institution", "coverage limit", "ownership category", "liquidity"],
        "ko_signals": ["보호 금융기관", "보호 한도", "소유 구조", "유동성"],
        "sources": ["fdic_deposit", "cfpb_spending", "bok_ecos"],
        "tags": ["DepositInsurance", "Banking", "Savings", "Risk"],
    },
    {
        "slug": "consumer-sentiment-economic-signal",
        "ko_title": "소비심리 지표 읽기: 기분과 실제 소비를 구분하기",
        "en_title": "Consumer Sentiment as an Economic Signal: Separate Mood from Spending",
        "ko_summary": "소비심리는 가계가 느끼는 불안을 보여 주지만 실제 소비, 소득, 고용, 물가와 함께 봐야 해석이 정확하다.",
        "en_summary": "Consumer sentiment shows household anxiety, but it should be read with actual spending, income, jobs, and inflation.",
        "ko_focus": "사람들이 경제를 나쁘게 느껴도 소비가 바로 줄지 않을 수 있고, 반대로 지출은 줄었는데 심리는 늦게 반응할 수도 있습니다.",
        "en_focus": "People can feel worse before spending falls, and spending can weaken before sentiment surveys fully catch up.",
        "ko_actions": ["소비심리와 실제 소매판매를 분리합니다.", "물가 부담이 심리에 미치는 영향을 봅니다.", "고용 안정성과 부채 부담을 함께 확인합니다."],
        "en_actions": ["Separate sentiment from actual retail or consumption data.", "Check how inflation pressure affects confidence.", "Read job stability and debt burden alongside sentiment."],
        "signals": ["sentiment index", "consumption", "inflation pressure", "job security"],
        "ko_signals": ["소비심리", "소비지출", "물가 부담", "고용 안정성"],
        "sources": ["fred", "bea_gdp", "bls_cpi"],
        "tags": ["ConsumerSentiment", "Consumption", "Inflation", "Households"],
    },
    {
        "slug": "core-vs-headline-inflation",
        "ko_title": "근원물가와 헤드라인 물가: 에너지·식품 변동을 따로 보는 이유",
        "en_title": "Core vs Headline Inflation: Why Food and Energy Are Read Separately",
        "ko_summary": "헤드라인 물가는 전체 생활비 압력을 보여 주고 근원물가는 일시적 에너지·식품 변동을 제외한 추세를 보려는 지표다.",
        "en_summary": "Headline inflation shows broad cost pressure, while core inflation tries to reveal trend pressure excluding volatile food and energy.",
        "ko_focus": "가계에는 식품과 에너지가 매우 중요하지만 중앙은행은 지속적인 물가 압력을 보기 위해 근원물가도 함께 봅니다.",
        "en_focus": "Food and energy matter to households, but central banks also track core inflation to judge persistent pressure.",
        "ko_actions": ["헤드라인과 근원물가를 같은 표에 둡니다.", "식품·에너지 급등이 일시적인지 확인합니다.", "임금과 서비스 물가가 따라붙는지 봅니다."],
        "en_actions": ["Put headline and core inflation in one table.", "Check whether food and energy spikes are temporary.", "Watch whether wages and services inflation follow."],
        "signals": ["headline CPI", "core CPI", "food price", "energy price"],
        "ko_signals": ["헤드라인 CPI", "근원 CPI", "식품 가격", "에너지 가격"],
        "sources": ["bls_cpi", "fed_policy", "oecd_outlook"],
        "tags": ["Inflation", "CPI", "FoodPrices", "Energy"],
    },
    {
        "slug": "nominal-vs-real-gdp",
        "ko_title": "명목 GDP와 실질 GDP: 성장과 물가 효과를 분리하기",
        "en_title": "Nominal vs Real GDP: Separate Growth from Price Effects",
        "ko_summary": "명목 GDP는 현재 가격 기준 규모를 보여 주고 실질 GDP는 물가 효과를 제거해 생산량 변화를 보려는 지표다.",
        "en_summary": "Nominal GDP measures output at current prices, while real GDP adjusts for inflation to estimate changes in production volume.",
        "ko_focus": "가격이 올라서 GDP가 커진 것인지 실제 생산과 소비가 늘어난 것인지 구분해야 경기 판단이 가능합니다.",
        "en_focus": "To judge the economy, separate whether GDP rose because prices increased or because real activity expanded.",
        "ko_actions": ["명목 성장률과 실질 성장률을 같이 봅니다.", "GDP 디플레이터와 CPI 차이를 이해합니다.", "소득, 생산, 지출 접근법이 같은 경제를 다른 각도에서 본다는 점을 기억합니다."],
        "en_actions": ["Read nominal and real growth together.", "Understand the difference between GDP deflator and CPI.", "Remember that income, production, and expenditure are different views of the same economy."],
        "signals": ["nominal GDP", "real GDP", "GDP deflator", "production volume"],
        "ko_signals": ["명목 GDP", "실질 GDP", "GDP 디플레이터", "생산량"],
        "sources": ["bea_gdp", "imf_data", "fred"],
        "tags": ["GDP", "Inflation", "RealGrowth", "Macroeconomics"],
    },
    {
        "slug": "household-balance-sheet-basics",
        "ko_title": "가계 재무상태표: 소득보다 자산, 부채, 유동성을 함께 보기",
        "en_title": "Household Balance Sheet Basics: Assets, Debt, and Liquidity",
        "ko_summary": "가계의 경제 안전성은 월소득뿐 아니라 현금, 예금, 투자자산, 부채, 보험, 유동성의 조합으로 결정된다.",
        "en_summary": "Household resilience depends on cash, deposits, investments, debt, insurance, and liquidity, not only monthly income.",
        "ko_focus": "소득이 높아도 현금이 부족하고 부채 상환액이 크면 작은 충격에도 불안정할 수 있습니다.",
        "en_focus": "High income can still be fragile when cash is low and debt payments are large.",
        "ko_actions": ["자산을 현금성, 투자성, 사용 자산으로 나눕니다.", "부채를 이자율과 만기로 정리합니다.", "한 달 안에 쓸 수 있는 유동성을 따로 표시합니다."],
        "en_actions": ["Classify assets as cash-like, investment, or use assets.", "Organize debt by rate and maturity.", "Mark liquidity available within one month."],
        "signals": ["cash buffer", "investment asset", "debt maturity", "liquidity"],
        "ko_signals": ["현금 완충", "투자자산", "부채 만기", "유동성"],
        "sources": ["cfpb_spending", "fdic_deposit", "sec_funds"],
        "tags": ["HouseholdFinance", "BalanceSheet", "Liquidity", "Debt"],
    },
    {
        "slug": "small-business-break-even-inflation",
        "ko_title": "소상공인 손익분기점과 물가: 매출보다 마진을 먼저 지키기",
        "en_title": "Small Business Break-Even and Inflation: Protect Margin Before Revenue",
        "ko_summary": "물가와 임대료, 인건비, 원재료비가 오르면 매출이 늘어도 손익분기점이 올라 실제 이익은 줄 수 있다.",
        "en_summary": "When rent, wages, and input costs rise, higher sales can still leave a small business with less profit because break-even moves up.",
        "ko_focus": "인플레이션 시기에는 매출 증가보다 단가, 원가율, 고정비가 어떻게 바뀌는지 보는 것이 먼저입니다.",
        "en_focus": "In inflationary periods, unit price, cost ratio, and fixed costs matter before celebrating revenue growth.",
        "ko_actions": ["고정비와 변동비를 분리합니다.", "원가율이 오른 품목을 표시합니다.", "가격 인상, 메뉴 조정, 비용 절감의 효과를 각각 계산합니다."],
        "en_actions": ["Separate fixed and variable costs.", "Flag items with rising cost ratios.", "Calculate price, mix, and cost-control scenarios separately."],
        "signals": ["fixed cost", "variable cost", "gross margin", "break-even sales"],
        "ko_signals": ["고정비", "변동비", "매출총이익률", "손익분기매출"],
        "sources": ["bls_cpi", "cfpb_budget_pdf", "world_bank_gep"],
        "tags": ["SmallBusiness", "Inflation", "BreakEven", "Margins"],
    },
    {
        "slug": "global-dollar-liquidity-basics",
        "ko_title": "달러 유동성 기초: 미국 금리가 세계 금융여건에 미치는 영향",
        "en_title": "Global Dollar Liquidity: How U.S. Rates Shape Financial Conditions",
        "ko_summary": "달러 금리와 유동성은 신흥국 환율, 외채 비용, 원자재 가격, 글로벌 투자심리에 영향을 줄 수 있다.",
        "en_summary": "Dollar rates and liquidity can influence emerging-market currencies, external debt costs, commodity prices, and global risk appetite.",
        "ko_focus": "미국 금리는 미국 안에서만 끝나지 않습니다. 달러로 거래하고 빚지는 경제에는 금융여건 신호가 됩니다.",
        "en_focus": "U.S. rates do not stop at U.S. borders; they shape conditions for economies that trade or borrow in dollars.",
        "ko_actions": ["미국 정책금리와 달러 지표를 함께 봅니다.", "외화부채가 많은 부문을 확인합니다.", "원자재 가격과 신흥국 환율 반응을 같이 봅니다."],
        "en_actions": ["Read U.S. policy rates with dollar indicators.", "Identify sectors with foreign-currency debt.", "Watch commodity prices and emerging-market currencies together."],
        "signals": ["U.S. policy rate", "dollar strength", "external debt", "risk appetite"],
        "ko_signals": ["미국 기준금리", "달러 강세", "외화부채", "위험선호"],
        "sources": ["fed_policy", "imf_weo", "fred"],
        "tags": ["Dollar", "GlobalFinance", "InterestRates", "EmergingMarkets"],
    },
    {
        "slug": "economic-calendar-for-households",
        "ko_title": "가계를 위한 경제 캘린더: CPI, 고용, 금리, 환율 발표일 정리",
        "en_title": "Economic Calendar for Households: CPI, Jobs, Rates, and Exchange Rates",
        "ko_summary": "경제 캘린더를 만들면 물가, 고용, 금리, 환율 발표가 대출, 예산, 환전, 소비 계획에 주는 영향을 미리 점검할 수 있다.",
        "en_summary": "A household economic calendar helps connect CPI, jobs, rate decisions, and exchange-rate moves to loans, budgets, travel money, and spending plans.",
        "ko_focus": "경제지표를 매일 추적할 필요는 없지만 큰 발표일을 알면 중요한 결정을 충동적으로 내릴 가능성이 줄어듭니다.",
        "en_focus": "Households do not need to follow every data point, but knowing major release dates can reduce rushed decisions.",
        "ko_actions": ["월별 CPI와 고용 발표일을 표시합니다.", "중앙은행 회의일과 대출금리 조정일을 연결합니다.", "여행·수입 결제 전 환율 확인일을 둡니다."],
        "en_actions": ["Mark monthly CPI and jobs releases.", "Connect central-bank meetings with loan-rate reset dates.", "Set exchange-rate check dates before travel or import payments."],
        "signals": ["CPI release", "jobs release", "rate meeting", "FX check date"],
        "ko_signals": ["CPI 발표", "고용 발표", "금리 회의", "환율 확인일"],
        "sources": ["bls_cpi", "bls_jobs", "fed_policy"],
        "tags": ["EconomicCalendar", "Households", "CPI", "Rates"],
    },
]


LEGACY_IMAGES = {
    "compound-interest-example": ["compound-interest-hero.png"],
    "emergency-fund-how-much": ["emergency-fund-hero.png"],
    "etf-vs-mutual-fund": ["etf-vs-mutual-fund-hero.png"],
    "exchange-rate-basics": ["exchange-rate-hero.png"],
    "household-budget-50-30-20": ["budget-50-30-20-hero.png"],
    "interest-rate-inflation-basics": ["interest-inflation-hero.png"],
    "recession-indicators-basics": ["recession-indicators-hero.png"],
}


def yaml_list(items: list[str]) -> str:
    return "\n".join(f"  - {item}" for item in items)


def hex_to_rgb(value: str) -> tuple[int, int, int]:
    value = value.lstrip("#")
    return tuple(int(value[index : index + 2], 16) for index in (0, 2, 4))


def blend(a: tuple[int, int, int], b: tuple[int, int, int], ratio: float) -> tuple[int, int, int]:
    return tuple(int(a[i] * (1 - ratio) + b[i] * ratio) for i in range(3))


def png_chunk(kind: bytes, data: bytes) -> bytes:
    return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data) & 0xFFFFFFFF)


def write_png(path: Path, title: str, labels: list[str], palette: tuple[str, str], variant: int) -> None:
    width, height = 1200, 675
    base = hex_to_rgb(palette[0])
    accent = hex_to_rgb(palette[1])
    paper = (248, 250, 252)
    ink = (15, 23, 42)
    muted = blend(base, ink, 0.54)
    rows: list[bytes] = []
    title_weight = sum(ord(ch) for ch in title) % 160

    for y in range(height):
        vertical = y / (height - 1)
        left = blend(base, paper, 0.08 + vertical * 0.10)
        mid = blend(muted, paper, 0.12 + vertical * 0.08)
        right = blend(ink, accent, 0.22 + variant * 0.04)
        panel = blend(paper, accent, 0.06)
        line = blend(accent, paper, 0.24)

        if y % 72 == 0:
            row = bytes(blend(left, paper, 0.18)) * width
        elif 278 <= y <= 548:
            row = bytes(left) * 70 + bytes(panel) * 520 + bytes(mid) * 220 + bytes(right) * 390
        elif 140 + variant * 18 <= y <= 170 + variant * 18:
            row = bytes(left) * (500 + title_weight) + bytes(line) * 420 + bytes(right) * (280 - title_weight)
        elif 344 <= y <= 506 and (y - 344) % 54 < 18:
            row = bytes(left) * 94 + bytes(line) * 438 + bytes(mid) * 268 + bytes(right) * 400
        elif 156 <= y <= 566 and (y + title_weight) % 118 < 14:
            row = bytes(left) * 710 + bytes(mid) * 130 + bytes(line) * 240 + bytes(right) * 120
        else:
            row = bytes(left) * 620 + bytes(mid) * 240 + bytes(right) * 340
        rows.append(b"\x00" + row)

    raw = b"".join(rows)
    png = (
        b"\x89PNG\r\n\x1a\n"
        + png_chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0))
        + png_chunk(b"IDAT", zlib.compress(raw, 6))
        + png_chunk(b"IEND", b"")
    )
    path.write_bytes(png)


def bounded_text(value: str, minimum: int, maximum: int, suffix: str) -> str:
    text = value if len(value) >= minimum else f"{value} {suffix}"
    if len(text) > maximum:
        text = text[: maximum - 3].rstrip() + "..."
    return text


def seo_title(topic: dict[str, object], lang: str) -> str:
    title = str(topic["ko_title"] if lang == "ko" else topic["en_title"])
    return bounded_text(title, 10 if lang == "ko" else 20, 70, "economy guide")


def seo_description(topic: dict[str, object], lang: str) -> str:
    if lang == "ko":
        return bounded_text(
            str(topic["ko_summary"]),
            60,
            170,
            "공식 자료를 바탕으로 생활비, 부채, 환율, 예산 판단에 연결해 설명합니다.",
        )
    return bounded_text(
        str(topic["en_summary"]),
        80,
        170,
        "It uses official sources to connect the signal to household budgets, debt, prices, and risk checks.",
    )


def source_notes(source_keys: list[str], lang: str) -> str:
    return "\n".join(f"- [{SOURCES[key][lang]}]({SOURCES[key]['url']})" for key in source_keys)


def related_links(index: int, lang: str) -> str:
    related = [TOPICS[(index + 1) % len(TOPICS)], TOPICS[(index + 13) % len(TOPICS)]]
    category_path = KO_CATEGORY.lower() if lang == "ko" else EN_CATEGORY.lower()
    if lang == "ko":
        return "\n".join(f"- [{topic['ko_title']}](/{{category}}/{topic['slug']}/)".replace("{category}", category_path) for topic in related)
    return "\n".join(f"- [{topic['en_title']}](/{{category}}/{topic['slug']}/)".replace("{category}", category_path) for topic in related)


def normalize_markdown(text: str) -> str:
    normalized = "\n".join(line[4:] if line.startswith("    ") else line for line in text.splitlines()).lstrip()
    return normalized.replace("sidebar:\nnav:", "sidebar:\n    nav:") + "\n"


def ko_intro(topic: dict[str, object]) -> str:
    first = topic["ko_signals"][0]
    return (
        f"경제 뉴스는 숫자를 많이 아는 것보다 **{first}** 같은 신호가 생활비와 의사결정으로 어떻게 이어지는지 읽는 일이 중요합니다. "
        f"이 글은 **{topic['ko_title']}** 주제를 공식 자료와 가계 관점으로 정리합니다."
    )


def en_intro(topic: dict[str, object]) -> str:
    first = topic["signals"][0]
    return (
        f"Economic news becomes useful when a signal such as **{first}** is translated into prices, debt, income, and decisions. "
        f"This guide explains **{topic['en_title']}** with official-source context and household-level checks."
    )


def ko_disclaimer(topic: dict[str, object]) -> str:
    return (
        f"이 글은 교육용 경제 해설이며 개인별 투자 조언, 세무 조언, 법률 조언, 재무 조언이 아닙니다. "
        f"**{topic['ko_title']}**를 실제 결정에 적용할 때는 거주 국가의 규칙, 세금, 수수료, 계약 조건, 본인의 위험 감내도를 별도로 확인해야 합니다."
    )


def en_disclaimer(topic: dict[str, object]) -> str:
    return (
        f"This article is educational and is not financial advice, investment advice, tax advice, or legal advice. "
        f"Before applying **{topic['en_title']}**, check local rules, taxes, fees, contracts, and your own risk capacity."
    )


def ko_signal_items(topic: dict[str, object]) -> str:
    title = topic["ko_title"]
    return "\n".join(
        f"- **{signal}**: {title}를 볼 때 이 신호의 최신값, 방향, 내 예산이나 부채에 미치는 영향을 함께 적습니다."
        for signal in topic["ko_signals"]
    )


def en_signal_items(topic: dict[str, object]) -> str:
    title = topic["en_title"]
    return "\n".join(
        f"- **{signal}**: for {title}, record the latest value, direction, and effect on your budget or debt."
        for signal in topic["signals"]
    )


def ko_action_items(topic: dict[str, object]) -> str:
    return "\n".join(f"- {action}" for action in topic["ko_actions"])


def en_action_items(topic: dict[str, object]) -> str:
    return "\n".join(f"- {action}" for action in topic["en_actions"])


def ko_field_example(topic: dict[str, object]) -> str:
    first = topic["ko_signals"][0]
    second = topic["ko_signals"][1]
    action = topic["ko_actions"][0]
    return (
        f"현장에서 적용할 때는 먼저 '{action}' 단계를 한 번만 해 봅니다. 그런 다음 **{first}** 값이 좋아질 때와 나빠질 때 "
        f"가계 예산, 대출 상환, 저축 목표 중 어느 항목이 움직이는지 표시합니다. **{second}** 신호는 단독으로 판단하지 말고 "
        "이전 달, 전년 같은 달, 공식 전망의 가정과 비교합니다. 이렇게 하면 경제 뉴스를 맞히는 문제가 아니라 내 결정을 늦출지, "
        "줄일지, 유지할지 정하는 기준표가 됩니다."
    )


def en_field_example(topic: dict[str, object]) -> str:
    first = topic["signals"][0]
    second = topic["signals"][1]
    action = str(topic["en_actions"][0]).rstrip(".")
    return (
        f"A practical application can start with one small step: '{action}'. Then mark what changes in your budget, debt payment, or savings goal "
        f"when **{first}** improves or worsens. Read **{second}** against last month, the same month last year, and the assumptions in official forecasts. "
        "This turns economic news from a prediction game into a decision table for delaying, reducing, or maintaining a plan."
    )


def ko_indicator_context(topic: dict[str, object]) -> str:
    first = topic["ko_signals"][0]
    second = topic["ko_signals"][1]
    return (
        f"**{first}**와 **{second}** 같은 경제지표는 단독 숫자로 쓰면 오해하기 쉽습니다. 발표일, 기준 기간, 전월 대비인지 "
        "전년 대비인지, 명목값인지 실질값인지 확인해야 합니다. 특히 가계 판단에서는 평균 경제보다 내 소득 주기, 부채 금리, "
        f"고정비, 환율 노출이 **{topic['ko_title']}** 해석에 더 직접적인 영향을 줄 수 있습니다."
    )


def en_indicator_context(topic: dict[str, object]) -> str:
    first = topic["signals"][0]
    second = topic["signals"][1]
    return (
        f"Indicators such as **{first}** and **{second}** are easy to misuse when they are read as isolated numbers. "
        "Check the release date, reference period, month-over-month or year-over-year basis, and whether the number is nominal or real. "
        f"For household decisions, income timing, debt rates, fixed costs, and currency exposure can matter more than the average economy when reading **{topic['en_title']}**."
    )


def ko_decision_context(topic: dict[str, object]) -> str:
    first = topic["ko_signals"][0]
    action = topic["ko_actions"][0]
    return (
        f"이 순서는 **{first}** 방향을 맞히기 위한 예측 절차가 아닙니다. '{action}' 단계처럼 경제 뉴스가 내 생활비, 대출, "
        "저축, 소비 결정을 어떻게 바꾸는지 확인하기 위한 정리법입니다. 같은 지표라도 고정금리 대출자, 변동금리 대출자, "
        "수출기업 근로자, 해외여행 준비자에게 의미가 다르게 나타날 수 있습니다."
    )


def en_decision_context(topic: dict[str, object]) -> str:
    first = topic["signals"][0]
    action = str(topic["en_actions"][0]).rstrip(".")
    return (
        f"This order is not a prediction system for **{first}**. It is a way to use '{action}' to connect economic news to living costs, "
        "debt, savings, and spending decisions. The same indicator can mean different things for a fixed-rate borrower, a variable-rate borrower, "
        "an export-sector worker, or a household planning overseas travel."
    )


def ko_checklist(topic: dict[str, object]) -> str:
    first = topic["ko_signals"][0]
    second = topic["ko_signals"][1]
    return "\n".join(
        [
            f"- **{first}** 최신값과 발표일을 기록합니다.",
            f"- **{second}**가 내 지출, 부채, 소득 중 어디에 영향을 주는지 표시합니다.",
            "- 한 달 수치만 보지 말고 3개월 이상 방향을 확인합니다.",
            "- 숫자가 바뀌어도 투자나 대출 결정을 즉시 바꾸지 말고 수수료, 세금, 계약 조건을 같이 확인합니다.",
        ]
    )


def en_checklist(topic: dict[str, object]) -> str:
    first = topic["signals"][0]
    second = topic["signals"][1]
    return "\n".join(
        [
            f"- Record the latest **{first}** value and release date.",
            f"- Mark whether **{second}** affects spending, debt, or income.",
            "- Check at least a three-month direction instead of one release.",
            "- Before changing investment or debt decisions, check fees, taxes, contract terms, and liquidity.",
        ]
    )


def ko_faq(topic: dict[str, object]) -> str:
    first = topic["ko_signals"][0]
    second = topic["ko_signals"][1]
    return dedent(f"""\
    ### 이 지표 하나만 보고 판단해도 되나요?

    아니요. **{first}**는 중요한 출발점이지만, **{second}**와 소득, 부채, 지출 구조를 함께 봐야 합니다. 경제지표는 평균을 보여 주기 때문에 개인의 현금흐름과 다를 수 있습니다.

    ### 최신 {first} 수치가 나오면 바로 예산이나 투자 결정을 바꿔야 하나요?

    보통은 한 번의 발표보다 방향과 맥락이 중요합니다. 최소한 이전 **{first}** 수치, **{second}** 변화, 공식 전망의 가정, 내 계약 조건을 확인한 뒤 움직이는 편이 안전합니다.

    ### 한국 독자는 어떤 점을 추가로 확인해야 하나요?

    **{topic["ko_title"]}**를 한국 상황에 적용할 때는 원화 환율, 에너지 수입 부담, 가계부채 금리, 국내 세금과 금융상품 규칙을 함께 확인해야 합니다. 해외 자료가 유용해도 실제 적용은 국내 제도와 비용 구조에 맞춰야 합니다.
    """)


def en_faq(topic: dict[str, object]) -> str:
    first = topic["signals"][0]
    second = topic["signals"][1]
    return dedent(f"""\
    ### Can one indicator be enough for a decision?

    No. **{first}** is a useful starting point, but it should be read with **{second}**, income, debt, and spending structure. Economic data describes averages, while household cash flow can differ.

    ### Should a new {first} release immediately change my budget or investment plan?

    Usually no. Direction and context matter more than one release. Compare **{first}** with the previous release, the **{second}** direction, official forecast assumptions, fees, taxes, and contract terms.

    ### What should Korean readers check separately?

    For **{topic["en_title"]}**, Korean readers should also check the won exchange rate, imported energy costs, household loan rates, local taxes, and domestic financial-product rules. Global data is useful, but application depends on local costs and institutions.
    """)


def ko_post(topic: dict[str, object], index: int) -> str:
    slug = str(topic["slug"])
    image_dir = f"/images/{POST_DATE}-{slug}"
    return dedent(f"""\
    ---
    layout: single
    title: >
      {topic["ko_title"]}
    seo_title: >
      {seo_title(topic, "ko")}
    date: {POST_DATE}T{7 + index // 3:02d}:{(index % 3) * 18:02d}:00+09:00
    last_modified_at: {LAST_MODIFIED_AT}
    lang: ko
    translation_id: economy-{slug}
    header:
      teaser: {image_dir}/hero.png
      overlay_image: {image_dir}/hero.png
      overlay_filter: 0.38
      image_description: >
        {topic["ko_title"]}의 핵심 경제 신호와 가계 의사결정 경로를 요약한 이미지입니다.
    excerpt: >
      {topic["ko_summary"]}
    seo_description: >
      {seo_description(topic, "ko")}
    categories:
      - {KO_CATEGORY}
    tags:
    {yaml_list(topic["tags"])}
    ---

    {ko_intro(topic)}

    {topic["ko_summary"]}

    {ko_disclaimer(topic)}

    ![{topic["ko_title"]} 핵심 경제 흐름]({image_dir}/hero.png)

    ## 핵심 요약

    {topic["ko_focus"]}

    {ko_indicator_context(topic)}

    ## 먼저 확인할 신호

    {ko_signal_items(topic)}

    ![{topic["ko_title"]} 확인 체크리스트]({image_dir}/checklist.png)

    ## 실무 적용 순서

    {ko_action_items(topic)}

    {ko_decision_context(topic)}

    ## 가계 적용 예시

    {ko_field_example(topic)}

    ## 체크리스트

    {ko_checklist(topic)}

    ## 자주 묻는 질문

    {ko_faq(topic)}

    ## 참고할 공식 자료

    {source_notes(topic["sources"], "ko")}

    ## 함께 보면 좋은 글

    {related_links(index, "ko")}
    """)


def en_post(topic: dict[str, object], index: int) -> str:
    slug = str(topic["slug"])
    image_dir = f"/images/{POST_DATE}-{slug}"
    return dedent(f"""\
    ---
    layout: single
    title: >
      {topic["en_title"]}
    seo_title: >
      {seo_title(topic, "en")}
    date: {POST_DATE}T{7 + index // 3:02d}:{(index % 3) * 18:02d}:00+09:00
    last_modified_at: {LAST_MODIFIED_AT}
    lang: en
    translation_id: economy-{slug}
    header:
      teaser: {image_dir}/hero.png
      overlay_image: {image_dir}/hero.png
      overlay_filter: 0.38
      image_description: >
        Economy guide image summarizing the key signal and household decision path for this topic.
    excerpt: >
      {topic["en_summary"]}
    seo_description: >
      {seo_description(topic, "en")}
    categories:
      - {EN_CATEGORY}
    tags:
    {yaml_list(topic["tags"])}
    ---

    {en_intro(topic)}

    {topic["en_summary"]}

    {en_disclaimer(topic)}

    ![{topic["en_title"]} core economic flow]({image_dir}/hero.png)

    ## Quick Summary

    {topic["en_focus"]}

    {en_indicator_context(topic)}

    ## Signals To Check First

    {en_signal_items(topic)}

    ![{topic["en_title"]} decision checklist]({image_dir}/checklist.png)

    ## Practical Reading Order

    {en_action_items(topic)}

    {en_decision_context(topic)}

    ## Household Example

    {en_field_example(topic)}

    ## Checklist

    {en_checklist(topic)}

    ## FAQ

    {en_faq(topic)}

    ## Source Notes

    {source_notes(topic["sources"], "en")}

    ## Related Reading

    {related_links(index, "en")}
    """)


def category_page(lang: str) -> str:
    if lang == "ko":
        return dedent("""\
        ---
        title: "Economy"
        layout: archive
        permalink: /ko_economy/
        lang: ko
        seo_description: >
          금리, 물가, 환율, GDP, 고용, 가계부채, 예산, 비상금, ETF와 펀드 차이처럼 경제 뉴스와 생활비 판단을 연결하는 교육용 경제 가이드입니다.
        sidebar:
            nav: "sidebar-category"
        ---

        Economy 카테고리는 투자 추천이 아니라 경제지표와 생활비 판단을 연결하는 교육용 글을 모읍니다. 금리, 물가, 환율, GDP, 고용, 가계부채, 예산, 비상금, 수출입, 유가, 반도체 경기처럼 검색 수요가 꾸준하고 실생활 판단에 영향을 주는 주제를 다룹니다.

        각 글은 IMF, World Bank, OECD, Federal Reserve, BEA, BLS, FRED, Bank of Korea, KOSIS, CFPB, SEC, FDIC 등 공식 또는 제도권 자료를 참고합니다. 모든 글은 개인별 투자 조언이나 재무 조언이 아니라 숫자를 읽고 가정을 점검하기 위한 자료입니다.

        처음에는 예산, 비상금, 금리와 물가, 환율, 경기 침체 지표 글을 읽고, 그다음 GDP, 고용, 유가, 가계부채, 수익률 곡선 글로 확장하면 좋습니다.

        ## 먼저 읽기

        - [50/30/20 예산법](/ko_economy/household-budget-50-30-20/)
        - [비상금은 얼마가 적당할까](/ko_economy/emergency-fund-how-much/)
        - [금리와 물가 기초](/ko_economy/interest-rate-inflation-basics/)
        - [환율 기초](/ko_economy/exchange-rate-basics/)
        - [경기 침체 지표 읽기](/ko_economy/recession-indicators-basics/)

        ## 최신 글

        {% assign posts = site.categories["ko_Economy"] %}
        {% for post in posts %}
          {% include archive-single.html type=page.entries_layout %}
        {% endfor %}
        """)
    return dedent("""\
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
    """)


def main() -> None:
    palettes = [
        ("#0f766e", "#f59e0b"),
        ("#1d4ed8", "#22c55e"),
        ("#7c2d12", "#38bdf8"),
        ("#334155", "#f97316"),
    ]
    for index, topic in enumerate(TOPICS):
        slug = str(topic["slug"])
        image_dir = ROOT / "images" / f"{POST_DATE}-{slug}"
        image_dir.mkdir(parents=True, exist_ok=True)
        for legacy_name in LEGACY_IMAGES.get(slug, []):
            legacy_path = image_dir / legacy_name
            if legacy_path.exists():
                legacy_path.unlink()
        palette = palettes[index % len(palettes)]
        write_png(
            image_dir / "hero.png",
            str(topic["en_title"]),
            [str(item) for item in topic["signals"]],
            palette,
            index % 3,
        )
        write_png(
            image_dir / "checklist.png",
            str(topic["en_title"]),
            [str(item) for item in topic["en_actions"]],
            (palette[0], "#eab308"),
            (index + 1) % 3,
        )
        (ROOT / "_posts" / "ko" / f"{POST_DATE}-{slug}.md").write_text(normalize_markdown(ko_post(topic, index)), encoding="utf-8")
        (ROOT / "_posts" / "en" / f"{POST_DATE}-{slug}.md").write_text(normalize_markdown(en_post(topic, index)), encoding="utf-8")
    (ROOT / "_pages" / "category-ko_Economy.md").write_text(normalize_markdown(category_page("ko")), encoding="utf-8")
    (ROOT / "_pages" / "category-en_Economy.md").write_text(normalize_markdown(category_page("en")), encoding="utf-8")
    print(f"Generated {len(TOPICS)} paired Economy topics.")


if __name__ == "__main__":
    main()
