#!/usr/bin/env python3
"""Generate paired Personal Finance posts and local SVG context images."""

from __future__ import annotations

import html
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parents[1]
POST_DATE = "2026-05-20"
LAST_MODIFIED_AT = "2026-05-23T14:00:00+09:00"
KO_CATEGORY = "ko_Personal_Finance"
EN_CATEGORY = "en_Personal_Finance"


SOURCES = {
    "cfpb_goals": {
        "ko": "CFPB Your Money, Your Goals",
        "en": "CFPB Your Money, Your Goals",
        "url": "https://www.consumerfinance.gov/consumer-tools/educator-tools/your-money-your-goals/",
    },
    "cfpb_credit": {
        "ko": "CFPB Understand Your Credit Score",
        "en": "CFPB Understand Your Credit Score",
        "url": "https://www.consumerfinance.gov/consumer-tools/credit-reports-and-scores/understand-your-credit-score/",
    },
    "cfpb_reports": {
        "ko": "CFPB Free Credit Reports",
        "en": "CFPB Free Credit Reports",
        "url": "https://www.consumerfinance.gov/ask-cfpb/how-do-i-get-a-free-copy-of-my-credit-reports-en-5/",
    },
    "cfpb_debt": {
        "ko": "CFPB Debt Collection",
        "en": "CFPB Debt Collection",
        "url": "https://www.consumerfinance.gov/consumer-tools/debt-collection/",
    },
    "cfpb_mortgage": {
        "ko": "CFPB Mortgage Tools",
        "en": "CFPB Mortgage Tools",
        "url": "https://www.consumerfinance.gov/consumer-tools/mortgages/",
    },
    "cfpb_auto": {
        "ko": "CFPB Auto Loans",
        "en": "CFPB Auto Loans",
        "url": "https://www.consumerfinance.gov/consumer-tools/auto-loans/",
    },
    "investor_compound": {
        "ko": "Investor.gov Compound Interest Calculator",
        "en": "Investor.gov Compound Interest Calculator",
        "url": "https://www.investor.gov/financial-tools-calculators/calculators/compound-interest-calculator",
    },
    "investor_risk": {
        "ko": "Investor.gov Risk Tolerance",
        "en": "Investor.gov Risk Tolerance",
        "url": "https://www.investor.gov/introduction-investing/investing-basics/save-and-invest/gauge-your-risk-tolerance",
    },
    "investor_alloc": {
        "ko": "Investor.gov Asset Allocation and Diversification",
        "en": "Investor.gov Asset Allocation and Diversification",
        "url": "https://www.investor.gov/introduction-investing/getting-started/assessing-your-risk-tolerance",
    },
    "finra_alloc": {
        "ko": "FINRA Asset Allocation and Diversification",
        "en": "FINRA Asset Allocation and Diversification",
        "url": "https://www.finra.org/investors/investing/investing-basics/asset-allocation-diversification",
    },
    "finra_fees": {
        "ko": "FINRA Understanding Investment Fees",
        "en": "FINRA Understanding Investment Fees",
        "url": "https://www.finra.org/investors/investing/investing-basics/fees-commissions",
    },
    "finra_redflags": {
        "ko": "FINRA Watch for Red Flags",
        "en": "FINRA Watch for Red Flags",
        "url": "https://www.finra.org/investors/protect-your-money/watch-red-flags",
    },
    "irs_withholding": {
        "ko": "IRS Tax Withholding",
        "en": "IRS Tax Withholding",
        "url": "https://www.irs.gov/individuals/employees/tax-withholding",
    },
    "irs_estimated": {
        "ko": "IRS Publication 505",
        "en": "IRS Publication 505",
        "url": "https://www.irs.gov/publications/p505",
    },
    "ftc_money": {
        "ko": "FTC Money Matters",
        "en": "FTC Money Matters",
        "url": "https://consumer.ftc.gov/your-money",
    },
    "kinfa": {
        "ko": "서민금융진흥원",
        "en": "Korea Inclusive Finance Agency",
        "url": "https://www.kinfa.or.kr/",
    },
    "kinfa_report": {
        "ko": "서민금융 사칭 신고센터",
        "en": "KINFA Impersonation Report Center",
        "url": "https://www.kinfa.or.kr/cyber/customerServiceCenter/customerDeclareCenter.do",
    },
}


TOPICS = [
    {
        "slug": "paycheck-budget-calendar",
        "ko_title": "월급날 예산 캘린더 만들기: 돈이 사라지기 전에 이름 붙이기",
        "en_title": "Paycheck Budget Calendar: Name the Money Before It Disappears",
        "ko_summary": "예산은 지출을 억누르는 장부가 아니라 월급이 들어온 순간 고정비, 저축, 변동비, 예비비에 역할을 배정하는 운영표다.",
        "en_summary": "A budget is not a punishment ledger; it is an operating calendar that assigns each paycheck to bills, savings, flexible spending, and reserves.",
        "ko_point": "월급이 들어온 뒤 남는 돈을 보는 방식은 늦습니다. 먼저 빠져나갈 날짜와 금액을 달력에 올리면 과소비보다 현금흐름 부족을 먼저 막을 수 있습니다.",
        "en_point": "Looking at what is left after spending is late. Put due dates and amounts on a calendar first so you prevent cash-flow gaps before overspending starts.",
        "ko_actions": ["고정비 결제일을 월급일 기준으로 다시 배열합니다.", "저축과 투자 이체일을 지출보다 먼저 둡니다.", "주별 생활비 한도를 현금흐름표에 표시합니다."],
        "en_actions": ["Reorder fixed-bill due dates around payday.", "Schedule savings and investing transfers before flexible spending.", "Set weekly spending caps in a cash-flow view."],
        "signals": ["bill due dates", "payday timing", "weekly spending cap", "buffer balance"],
        "ko_signals": ["고정비 결제일", "월급 입금일", "주별 생활비 한도", "완충 잔액"],
        "sources": ["cfpb_goals", "ftc_money"],
        "tags": ["Budgeting", "Cash Flow", "Personal Finance", "Planning"],
    },
    {
        "slug": "emergency-fund-tiers",
        "ko_title": "비상금 3단계 설계: 100만원, 한 달, 6개월을 나누는 이유",
        "en_title": "Three Emergency Fund Tiers: Starter Cash, One Month, and Six Months",
        "ko_summary": "비상금은 하나의 숫자가 아니라 작은 사고, 소득 공백, 장기 위기를 나누어 버티게 하는 현금 완충 장치다.",
        "en_summary": "An emergency fund is not one magic number; it is a cash buffer for small shocks, income gaps, and longer emergencies.",
        "ko_point": "처음부터 큰 금액을 목표로 잡으면 포기하기 쉽습니다. 소액 즉시자금, 한 달 생활비, 장기 안전망을 분리하면 진행 상황이 보입니다.",
        "en_point": "A large target can feel impossible. Separating starter cash, one-month expenses, and a longer safety net makes progress visible.",
        "ko_actions": ["첫 단계는 소액 사고를 막을 현금으로 시작합니다.", "두 번째는 한 달 필수 지출을 기준으로 잡습니다.", "세 번째는 직업 안정성과 부양가족 수에 맞춰 조정합니다."],
        "en_actions": ["Start with cash for small emergencies.", "Set the second tier around one month of essentials.", "Adjust the long tier for job stability and dependents."],
        "signals": ["essential expenses", "income volatility", "dependents", "deductibles"],
        "ko_signals": ["필수 지출", "소득 변동성", "부양가족", "보험 자기부담금"],
        "sources": ["cfpb_goals", "ftc_money"],
        "tags": ["Emergency Fund", "Savings", "Budgeting", "Risk"],
    },
    {
        "slug": "sinking-funds-irregular-expenses",
        "ko_title": "싱킹펀드로 비정기 지출 막기: 명절, 보험료, 여행비를 월별로 쪼개기",
        "en_title": "Sinking Funds for Irregular Expenses: Turning Annual Bills Into Monthly Plans",
        "ko_summary": "비정기 지출은 예상하지 못한 지출이 아니라 준비하지 않은 지출인 경우가 많다. 싱킹펀드는 연간 비용을 월별 저축으로 바꾼다.",
        "en_summary": "Many irregular expenses are not surprises; they are unplanned known costs. Sinking funds convert annual bills into monthly savings.",
        "ko_point": "보험료, 자동차세, 명절, 여행, 경조사는 매년 반복됩니다. 목록화하면 카드값 폭증 대신 월별 준비금으로 처리할 수 있습니다.",
        "en_point": "Insurance, taxes, holidays, travel, and gifts often repeat. Listing them turns card spikes into planned monthly reserves.",
        "ko_actions": ["지난 12개월의 비정기 지출을 모읍니다.", "항목별 연간 금액을 12로 나눕니다.", "통장이나 예산 앱에서 목적별 잔액을 분리합니다."],
        "en_actions": ["Collect irregular expenses from the last 12 months.", "Divide each annual amount by 12.", "Separate balances by purpose in an account or budget app."],
        "signals": ["annual insurance", "holiday costs", "car expenses", "family events"],
        "ko_signals": ["연간 보험료", "명절 비용", "자동차 지출", "경조사"],
        "sources": ["cfpb_goals", "ftc_money"],
        "tags": ["Budgeting", "Savings", "Cash Flow", "Planning"],
    },
    {
        "slug": "debt-avalanche-vs-snowball",
        "ko_title": "부채 상환 눈사태와 눈덩이 방식: 이자 절감과 지속성 사이 선택",
        "en_title": "Debt Avalanche vs Snowball: Choosing Between Interest Savings and Momentum",
        "ko_summary": "부채 상환 전략은 수학적으로 유리한 방식과 행동적으로 지속 가능한 방식 사이에서 자신의 현금흐름에 맞게 선택해야 한다.",
        "en_summary": "Debt payoff strategy is a tradeoff between the mathematically efficient route and the behaviorally sustainable route.",
        "ko_point": "고금리부터 갚으면 이자를 줄일 수 있지만, 작은 빚부터 없애면 성취감이 빠릅니다. 중요한 것은 새 빚을 만들지 않는 현금흐름입니다.",
        "en_point": "Paying high-rate debt first can reduce interest, while paying small balances first can build momentum. The core is preventing new debt.",
        "ko_actions": ["모든 부채의 잔액, 금리, 최소상환액을 적습니다.", "최소상환액은 모두 유지합니다.", "추가 상환액을 한 부채에 집중합니다."],
        "en_actions": ["List every balance, rate, and minimum payment.", "Keep all minimum payments current.", "Focus extra payments on one debt at a time."],
        "signals": ["APR", "minimum payment", "balance size", "new borrowing"],
        "ko_signals": ["APR", "최소상환액", "잔액 규모", "신규 차입"],
        "sources": ["cfpb_debt", "cfpb_goals"],
        "tags": ["Debt", "Budgeting", "APR", "Cash Flow"],
    },
    {
        "slug": "credit-card-minimum-payment-trap",
        "ko_title": "신용카드 최소결제의 함정: 이번 달을 넘기면 다음 달이 커진다",
        "en_title": "The Minimum Payment Trap: Why Next Month Gets More Expensive",
        "ko_summary": "최소결제는 연체를 막는 임시 장치일 수 있지만 잔액과 이자를 오래 남겨 다음 달 현금흐름을 더 약하게 만들 수 있다.",
        "en_summary": "A minimum payment can prevent delinquency, but it can also leave balances and interest that weaken next month's cash flow.",
        "ko_point": "카드값을 전액 갚지 못한 달은 소비 문제가 아니라 현금흐름 경고입니다. 결제일 조정, 지출 중단, 상환 계획이 같이 필요합니다.",
        "en_point": "A month when you cannot pay in full is a cash-flow warning. Due-date changes, spending pauses, and a payoff plan belong together.",
        "ko_actions": ["카드별 APR과 잔액을 확인합니다.", "새 결제를 일시 중단할 카드를 정합니다.", "다음 월급에서 추가 상환액을 먼저 배정합니다."],
        "en_actions": ["Check APR and balance by card.", "Choose which card to stop using temporarily.", "Assign extra payoff money from the next paycheck first."],
        "signals": ["revolving balance", "APR", "late fee", "credit utilization"],
        "ko_signals": ["이월 잔액", "APR", "연체료", "한도 사용률"],
        "sources": ["cfpb_credit", "cfpb_debt", "ftc_money"],
        "tags": ["Credit Cards", "Debt", "APR", "Credit Score"],
    },
    {
        "slug": "credit-score-factors",
        "ko_title": "신용점수 핵심 요인: 점수보다 보고서 내용을 먼저 보기",
        "en_title": "Credit Score Factors: Read the Report Before the Number",
        "ko_summary": "신용점수는 하나의 숫자처럼 보이지만 실제로는 결제 이력, 한도 사용률, 계좌 기간, 신규 신청, 보고서 오류가 합쳐진 결과다.",
        "en_summary": "A credit score looks like one number, but it reflects payment history, utilization, account age, new applications, and report accuracy.",
        "ko_point": "점수만 보는 습관은 원인을 놓치게 합니다. 보고서 항목을 확인해야 잘못된 정보, 낯선 계좌, 연체 기록을 고칠 수 있습니다.",
        "en_point": "Watching only the score hides the cause. Reviewing report items helps you find errors, unfamiliar accounts, and late-payment records.",
        "ko_actions": ["신용보고서를 정기적으로 확인합니다.", "결제일 자동화와 알림을 설정합니다.", "카드 한도 사용률을 낮게 유지합니다."],
        "en_actions": ["Review credit reports regularly.", "Automate payments or reminders.", "Keep credit utilization low."],
        "signals": ["payment history", "credit utilization", "report errors", "new applications"],
        "ko_signals": ["결제 이력", "한도 사용률", "보고서 오류", "신규 신청"],
        "sources": ["cfpb_credit", "cfpb_reports"],
        "tags": ["Credit Score", "Credit Report", "Debt", "Consumer Finance"],
    },
    {
        "slug": "credit-report-dispute",
        "ko_title": "신용보고서 오류 정정 순서: 증거를 모아 양쪽에 이의제기하기",
        "en_title": "Credit Report Dispute Order: Gather Evidence and Dispute Both Sides",
        "ko_summary": "신용보고서 오류는 점수를 낮출 수 있으므로 보고기관과 정보를 제공한 금융회사 양쪽에 근거 자료를 붙여 정정 요청을 해야 한다.",
        "en_summary": "Credit report errors can lower scores, so disputes should include evidence and be sent to both the reporting company and the data furnisher.",
        "ko_point": "말로만 항의하면 추적이 어렵습니다. 어떤 항목이 왜 틀렸는지, 어떤 자료가 맞는지, 언제 보냈는지를 기록해야 합니다.",
        "en_point": "Verbal complaints are hard to track. Record what is wrong, why it is wrong, what evidence supports you, and when you sent it.",
        "ko_actions": ["오류 항목을 표시한 보고서 사본을 보관합니다.", "영수증, 완납증명, 계좌 내역을 첨부합니다.", "접수일과 회신 기한을 기록합니다."],
        "en_actions": ["Save a copy of the report with the error marked.", "Attach receipts, payoff letters, or account records.", "Track submission date and response deadline."],
        "signals": ["wrong account", "duplicate debt", "incorrect late payment", "old address"],
        "ko_signals": ["모르는 계좌", "중복 채무", "잘못된 연체", "오래된 주소"],
        "sources": ["cfpb_reports", "cfpb_credit"],
        "tags": ["Credit Report", "Dispute", "Consumer Rights", "Credit Score"],
    },
    {
        "slug": "loan-apr-total-cost",
        "ko_title": "대출 금리와 APR 차이: 월상환액보다 총비용을 먼저 계산하기",
        "en_title": "Interest Rate vs APR: Read Total Loan Cost Before the Monthly Payment",
        "ko_summary": "대출 비교에서는 월상환액이 작아 보이는지보다 금리, 수수료, 기간, 중도상환 조건을 합친 총비용을 봐야 한다.",
        "en_summary": "Loan comparison should focus on total cost across rate, fees, term, and prepayment terms, not just a smaller-looking monthly payment.",
        "ko_point": "기간을 늘리면 월상환액은 줄지만 총이자는 늘 수 있습니다. APR과 총상환액을 함께 보면 가격표가 더 정확해집니다.",
        "en_point": "A longer term can lower the monthly payment while raising total interest. APR and total repayment make the price tag clearer.",
        "ko_actions": ["월상환액, APR, 총상환액을 같은 표에 둡니다.", "수수료와 중도상환 조건을 확인합니다.", "대출 기간을 줄였을 때의 총비용을 비교합니다."],
        "en_actions": ["Put monthly payment, APR, and total repayment in one table.", "Check fees and prepayment terms.", "Compare total cost under a shorter term."],
        "signals": ["APR", "loan term", "fees", "total repayment"],
        "ko_signals": ["APR", "대출 기간", "수수료", "총상환액"],
        "sources": ["cfpb_auto", "cfpb_mortgage", "cfpb_goals"],
        "tags": ["Loans", "APR", "Debt", "Consumer Finance"],
    },
    {
        "slug": "bnpl-installment-risk",
        "ko_title": "BNPL과 할부 결제 리스크: 작은 결제가 여러 개일 때 생기는 착시",
        "en_title": "BNPL and Installment Risk: The Illusion of Many Small Payments",
        "ko_summary": "BNPL과 할부는 구매 장벽을 낮추지만 여러 결제가 겹치면 실제 월 고정지출이 보이지 않게 커질 수 있다.",
        "en_summary": "BNPL and installments lower purchase friction, but stacked small payments can hide the real monthly fixed-spending load.",
        "ko_point": "한 번의 결제는 작아도 네 개가 겹치면 카드값처럼 행동합니다. 결제일과 총잔액을 예산에 반영해야 합니다.",
        "en_point": "One payment may be small, but several stacked plans behave like a credit card bill. Put due dates and total balances into the budget.",
        "ko_actions": ["모든 할부와 BNPL 결제일을 한 달 달력에 표시합니다.", "새 결제 전 기존 잔액을 확인합니다.", "환불 시 결제 취소와 잔여 청구를 따로 확인합니다."],
        "en_actions": ["Put all installment and BNPL due dates on one calendar.", "Check existing balances before a new plan.", "After returns, confirm both cancellation and remaining charges."],
        "signals": ["stacked payments", "late fees", "return mismatch", "subscription overlap"],
        "ko_signals": ["겹친 결제", "연체료", "환불 불일치", "구독 중복"],
        "sources": ["ftc_money", "cfpb_goals"],
        "tags": ["BNPL", "Installments", "Budgeting", "Debt"],
    },
    {
        "slug": "auto-loan-total-cost",
        "ko_title": "자동차 대출 총비용 계산: 차값보다 기간과 보험료가 더 중요할 때",
        "en_title": "Auto Loan Total Cost: When Term and Insurance Matter More Than Sticker Price",
        "ko_summary": "자동차 구매 예산은 차량 가격뿐 아니라 대출 기간, 금리, 보험료, 세금, 정비비, 감가상각을 함께 봐야 현실적이다.",
        "en_summary": "A car budget needs loan term, rate, insurance, taxes, maintenance, and depreciation, not just the sticker price.",
        "ko_point": "긴 대출은 월상환액을 낮추지만 차 가치보다 빚이 더 오래 남을 수 있습니다. 유지비까지 포함해야 감당 가능성이 보입니다.",
        "en_point": "A long loan can lower the payment while debt outlasts the car's value. Affordability only shows up after ownership costs are included.",
        "ko_actions": ["월상환액에 보험, 세금, 주유, 정비비를 더합니다.", "대출 기간별 총이자를 비교합니다.", "중고차라면 수리 예비비를 따로 둡니다."],
        "en_actions": ["Add insurance, taxes, fuel, and maintenance to the payment.", "Compare total interest by term.", "Keep a repair reserve for used cars."],
        "signals": ["loan term", "insurance premium", "maintenance reserve", "depreciation"],
        "ko_signals": ["대출 기간", "보험료", "정비 예비비", "감가상각"],
        "sources": ["cfpb_auto", "cfpb_goals"],
        "tags": ["Auto Loans", "Budgeting", "Debt", "APR"],
    },
    {
        "slug": "mortgage-affordability-stress-test",
        "ko_title": "주택대출 감당 가능성 테스트: 승인 가능 금액과 살 수 있는 금액은 다르다",
        "en_title": "Mortgage Affordability Stress Test: Approval Amount Is Not Affordability",
        "ko_summary": "주택대출은 승인 한도보다 이자 상승, 보험료, 세금, 수리비, 소득 공백을 견딜 수 있는지가 더 중요한 판단 기준이다.",
        "en_summary": "Mortgage affordability is less about the approval amount and more about surviving rate changes, insurance, taxes, repairs, and income gaps.",
        "ko_point": "대출 한도는 금융회사 기준이고 생활 가능성은 가계 기준입니다. 고정비가 너무 커지면 저축과 비상금이 먼저 무너집니다.",
        "en_point": "A lender's limit is not the household's comfort zone. If housing costs crowd out savings and buffers, the risk is already visible.",
        "ko_actions": ["원리금, 관리비, 세금, 보험, 수리비를 한 표에 둡니다.", "금리 1-2%p 상승 시나리오를 계산합니다.", "주택 구입 후에도 비상금이 남는지 확인합니다."],
        "en_actions": ["Put principal, interest, fees, taxes, insurance, and repairs in one table.", "Run a 1-2 percentage point rate stress test.", "Confirm emergency cash remains after closing."],
        "signals": ["housing ratio", "interest rate reset", "repair reserve", "closing costs"],
        "ko_signals": ["주거비 비율", "금리 재산정", "수리 예비비", "취득 비용"],
        "sources": ["cfpb_mortgage", "cfpb_goals"],
        "tags": ["Mortgage", "Housing", "Budgeting", "Debt"],
    },
    {
        "slug": "rent-vs-buy-framework",
        "ko_title": "전월세와 매수 비교 프레임: 가격 전망보다 현금흐름 먼저 보기",
        "en_title": "Rent vs Buy Framework: Cash Flow Before Price Forecasts",
        "ko_summary": "집을 살지 빌릴지의 판단은 가격이 오를지보다 거주 기간, 초기비용, 대출 부담, 이동성, 수리 책임을 함께 비교해야 한다.",
        "en_summary": "Rent-vs-buy decisions should compare time horizon, upfront cost, debt load, mobility, and repair responsibility before price forecasts.",
        "ko_point": "매수는 강제저축처럼 보일 수 있지만 유동성과 집중위험을 줄입니다. 임차는 비용처럼 보이지만 이동성과 현금 여유를 줍니다.",
        "en_point": "Buying can feel like forced saving but reduces liquidity and concentrates risk. Renting can feel like cost but preserves flexibility and cash.",
        "ko_actions": ["최소 거주 기간을 먼저 정합니다.", "초기비용과 기회비용을 계산합니다.", "수리비와 이동 가능성을 숫자로 적습니다."],
        "en_actions": ["Define the minimum expected stay first.", "Calculate upfront costs and opportunity costs.", "Put repair risk and mobility into numbers."],
        "signals": ["time horizon", "upfront cash", "monthly housing cost", "mobility need"],
        "ko_signals": ["거주 기간", "초기 현금", "월 주거비", "이동 필요성"],
        "sources": ["cfpb_mortgage", "cfpb_goals"],
        "tags": ["Housing", "Mortgage", "Renting", "Planning"],
    },
    {
        "slug": "insurance-deductible-buffer",
        "ko_title": "보험 자기부담금과 비상금: 보험이 있어도 현금이 필요한 이유",
        "en_title": "Insurance Deductibles and Cash Buffers: Why Coverage Still Needs Cash",
        "ko_summary": "보험은 큰 손실을 줄이지만 자기부담금, 면책기간, 보상 전 선지출 때문에 별도 현금 완충이 필요하다.",
        "en_summary": "Insurance reduces large losses, but deductibles, waiting periods, and upfront costs still require a cash buffer.",
        "ko_point": "보험료를 낮추려고 자기부담금을 높였다면 그만큼 비상금도 같이 커져야 합니다. 보험과 현금은 대체재가 아니라 조합입니다.",
        "en_point": "If you raise deductibles to lower premiums, your emergency fund should rise too. Insurance and cash are complements, not substitutes.",
        "ko_actions": ["보험별 자기부담금 최대치를 적습니다.", "청구 전 필요한 선지출을 추정합니다.", "비상금 목표에 자기부담금 합계를 반영합니다."],
        "en_actions": ["List the maximum deductible by policy.", "Estimate upfront spending before reimbursement.", "Add deductible exposure to the emergency fund target."],
        "signals": ["deductible", "waiting period", "claim paperwork", "cash reserve"],
        "ko_signals": ["자기부담금", "면책기간", "청구 서류", "현금 예비비"],
        "sources": ["cfpb_goals", "ftc_money"],
        "tags": ["Insurance", "Emergency Fund", "Risk", "Budgeting"],
    },
    {
        "slug": "subscription-audit",
        "ko_title": "구독 지출 감사: 작은 자동결제가 예산을 잠식하는 방식",
        "en_title": "Subscription Audit: How Small Auto-Payments Eat the Budget",
        "ko_summary": "구독 지출은 한 건씩 보면 작지만 자동결제와 무료체험 전환이 누적되면 고정비처럼 예산을 잠식한다.",
        "en_summary": "Subscriptions look small one by one, but auto-payments and trial conversions can turn them into a hidden fixed-cost layer.",
        "ko_point": "구독을 줄이는 목표는 무조건 취소가 아니라 사용빈도와 대체 가능성을 기준으로 예산 자리를 다시 배정하는 것입니다.",
        "en_point": "The goal is not canceling everything; it is assigning budget space based on actual use and available substitutes.",
        "ko_actions": ["카드 명세서에서 자동결제를 모두 표시합니다.", "최근 30일 사용 여부를 확인합니다.", "무료체험 종료일을 캘린더에 넣습니다."],
        "en_actions": ["Mark every auto-payment on card statements.", "Check whether you used it in the last 30 days.", "Put trial end dates on the calendar."],
        "signals": ["auto-renewal", "trial conversion", "unused service", "family plan overlap"],
        "ko_signals": ["자동갱신", "무료체험 전환", "미사용 서비스", "가족요금제 중복"],
        "sources": ["ftc_money", "cfpb_goals"],
        "tags": ["Subscriptions", "Budgeting", "Cash Flow", "Spending"],
    },
    {
        "slug": "tax-withholding-checkup",
        "ko_title": "세금 원천징수 점검: 환급액보다 현금흐름을 기준으로 보기",
        "en_title": "Tax Withholding Checkup: Read Refunds Through Cash Flow",
        "ko_summary": "세금 원천징수는 환급을 크게 받는 게임이 아니라 연중 현금흐름과 납부 부족 위험을 균형 있게 맞추는 과정이다.",
        "en_summary": "Tax withholding is not a game of maximizing refunds; it balances year-round cash flow against underpayment risk.",
        "ko_point": "환급이 크면 강제저축처럼 보일 수 있지만 그 돈은 연중 사용할 수 없던 현금입니다. 반대로 부족하면 납부 부담이 한 번에 옵니다.",
        "en_point": "A large refund can feel like forced saving, but it was cash unavailable during the year. Too little withholding creates a lump-sum problem.",
        "ko_actions": ["소득 변화, 부양가족, 부업 여부를 점검합니다.", "예상 세액과 원천징수액을 중간에 비교합니다.", "국가별 세법 차이는 공식 계산도구로 확인합니다."],
        "en_actions": ["Review income changes, dependents, and side income.", "Compare expected tax with withholding during the year.", "Use official calculators because rules differ by country."],
        "signals": ["income change", "side income", "tax credits", "refund size"],
        "ko_signals": ["소득 변화", "부업 소득", "세액공제", "환급액"],
        "sources": ["irs_withholding", "irs_estimated"],
        "tags": ["Taxes", "Cash Flow", "Withholding", "Planning"],
    },
    {
        "slug": "freelancer-tax-buckets",
        "ko_title": "프리랜서 세금 통장 나누기: 매출과 내 돈을 분리하는 습관",
        "en_title": "Freelancer Tax Buckets: Separating Revenue From Your Own Money",
        "ko_summary": "프리랜서와 부업 소득자는 입금액 전체를 생활비로 보면 세금과 비용을 늦게 발견한다. 세금, 비용, 생활비 통장을 나눠야 한다.",
        "en_summary": "Freelancers and side earners should not treat gross receipts as spendable income. Separate tax, business cost, and living expense buckets.",
        "ko_point": "입금일에는 돈이 많아 보이지만 신고일에는 부족해질 수 있습니다. 비율을 정해 자동 분리하면 세금 스트레스가 줄어듭니다.",
        "en_point": "Cash can look abundant on payment day and short on tax day. Automatic percentage buckets reduce stress.",
        "ko_actions": ["입금 즉시 세금 예상분을 별도 통장으로 옮깁니다.", "업무 비용과 개인 지출 결제수단을 분리합니다.", "분기마다 예상세금과 실제 수익을 비교합니다."],
        "en_actions": ["Move estimated tax money to a separate account when paid.", "Separate business and personal payment methods.", "Compare estimated taxes with actual profit quarterly."],
        "signals": ["gross receipts", "business expenses", "quarterly estimates", "cash reserve"],
        "ko_signals": ["총입금액", "업무비용", "분기 예상세금", "현금 예비비"],
        "sources": ["irs_estimated", "cfpb_goals"],
        "tags": ["Freelance", "Taxes", "Cash Flow", "Budgeting"],
    },
    {
        "slug": "risk-tolerance-time-horizon",
        "ko_title": "투자 위험감내도와 기간: 같은 ETF도 목표에 따라 다르게 보인다",
        "en_title": "Risk Tolerance and Time Horizon: The Same ETF Looks Different by Goal",
        "ko_summary": "투자 상품의 좋고 나쁨은 목표 기간과 손실 감내도에 따라 달라진다. 단기 돈과 장기 돈은 같은 위험을 가져서는 안 된다.",
        "en_summary": "An investment's fit depends on time horizon and loss tolerance. Short-term money and long-term money should not carry the same risk.",
        "ko_point": "집 계약금처럼 곧 쓸 돈은 변동성을 견디기 어렵고, 은퇴자금처럼 긴 돈은 너무 낮은 수익률도 위험이 될 수 있습니다.",
        "en_point": "A down-payment fund cannot tolerate much volatility, while retirement money can face risk from returns that are too low.",
        "ko_actions": ["목표별 사용 시점을 적습니다.", "최대 손실 시 행동을 미리 정합니다.", "단기·중기·장기 돈을 다른 계좌나 표로 분리합니다."],
        "en_actions": ["Write the spending date for each goal.", "Define what you would do after a large loss.", "Separate short-, medium-, and long-term money in accounts or tables."],
        "signals": ["time horizon", "loss tolerance", "liquidity need", "goal date"],
        "ko_signals": ["투자 기간", "손실 감내도", "유동성 필요", "목표 날짜"],
        "sources": ["investor_risk", "investor_alloc"],
        "tags": ["Investing", "Risk Tolerance", "Time Horizon", "Planning"],
    },
    {
        "slug": "asset-allocation-diversification",
        "ko_title": "자산배분과 분산투자: 수익률보다 먼저 위험을 나누는 법",
        "en_title": "Asset Allocation and Diversification: Splitting Risk Before Chasing Return",
        "ko_summary": "자산배분은 어떤 상품이 오를지 맞히는 일이 아니라 주식, 채권, 현금 같은 자산군을 목표와 위험에 맞게 나누는 과정이다.",
        "en_summary": "Asset allocation is not guessing the winner; it divides stocks, bonds, cash, and other assets according to goals and risk.",
        "ko_point": "분산은 수익을 보장하지 않지만 한 자산이나 한 종목에 과도하게 기대는 위험을 줄입니다. 목표별 배분표가 필요합니다.",
        "en_point": "Diversification does not guarantee returns, but it reduces reliance on one asset or one security. Each goal needs its own allocation.",
        "ko_actions": ["목표별 주식, 채권, 현금 비중을 정합니다.", "한 종목이나 한 섹터 집중도를 확인합니다.", "연 1회 배분이 크게 벗어났는지 봅니다."],
        "en_actions": ["Set stock, bond, and cash weights by goal.", "Check concentration in one security or sector.", "Review annually whether allocation drifted."],
        "signals": ["asset mix", "concentration risk", "correlation", "rebalancing date"],
        "ko_signals": ["자산 비중", "집중위험", "상관관계", "리밸런싱 날짜"],
        "sources": ["finra_alloc", "investor_alloc"],
        "tags": ["Asset Allocation", "Diversification", "Investing", "Risk"],
    },
    {
        "slug": "investment-fees-expense-ratio",
        "ko_title": "투자 수수료와 비용비율: 작아 보여도 장기 수익률을 갉아먹는 숫자",
        "en_title": "Investment Fees and Expense Ratios: Small Numbers That Compound Against You",
        "ko_summary": "투자 수수료는 매년 작아 보여도 장기 복리에서는 수익률을 지속적으로 깎는다. 상품 비교에는 비용비율과 거래비용이 함께 필요하다.",
        "en_summary": "Investment fees can look small each year, but over long horizons they compound against returns. Compare expense ratios and transaction costs together.",
        "ko_point": "수익률 전망은 불확실하지만 비용은 비교적 확실합니다. 같은 전략이라면 비용 차이가 장기 결과를 바꿀 수 있습니다.",
        "en_point": "Expected returns are uncertain, but costs are more predictable. For similar strategies, fee differences can change long-term outcomes.",
        "ko_actions": ["펀드 비용비율과 판매수수료를 확인합니다.", "거래 빈도와 세금 영향을 함께 봅니다.", "비슷한 상품 간 총비용을 비교합니다."],
        "en_actions": ["Check fund expense ratios and sales charges.", "Include trading frequency and tax effects.", "Compare total costs across similar products."],
        "signals": ["expense ratio", "sales charge", "turnover", "tracking difference"],
        "ko_signals": ["비용비율", "판매수수료", "회전율", "추적오차"],
        "sources": ["finra_fees", "investor_compound"],
        "tags": ["Investment Fees", "ETFs", "Mutual Funds", "Compounding"],
    },
    {
        "slug": "etf-selection-checklist",
        "ko_title": "ETF 선택 체크리스트: 이름보다 지수, 비용, 거래량, 보유종목 보기",
        "en_title": "ETF Selection Checklist: Index, Cost, Liquidity, and Holdings Before the Name",
        "ko_summary": "ETF 이름은 비슷해도 추종지수, 보유종목, 비용, 거래량, 환헤지 여부가 다르면 완전히 다른 상품이 될 수 있다.",
        "en_summary": "ETFs with similar names can differ sharply by index, holdings, cost, liquidity, and currency hedging.",
        "ko_point": "테마 이름만 보고 고르면 같은 섹터에 과도하게 집중될 수 있습니다. ETF는 포장보다 안에 든 종목과 규칙을 봐야 합니다.",
        "en_point": "Buying by theme name can create hidden concentration. Look through the package to holdings and rules.",
        "ko_actions": ["추종지수와 상위 보유종목을 확인합니다.", "비용비율과 거래량을 봅니다.", "기존 포트폴리오와 겹치는 비중을 계산합니다."],
        "en_actions": ["Check the index and top holdings.", "Review expense ratio and trading volume.", "Measure overlap with your current portfolio."],
        "signals": ["index methodology", "top holdings", "expense ratio", "liquidity"],
        "ko_signals": ["지수 방법론", "상위 보유종목", "비용비율", "유동성"],
        "sources": ["finra_alloc", "finra_fees", "investor_alloc"],
        "tags": ["ETF", "Investing", "Fees", "Diversification"],
    },
    {
        "slug": "target-date-fund-basics",
        "ko_title": "타깃데이트펀드 기본: 은퇴 시점에 맞춘 자동 자산배분 이해하기",
        "en_title": "Target-Date Fund Basics: Understanding Automatic Allocation by Retirement Year",
        "ko_summary": "타깃데이트펀드는 목표 은퇴연도에 맞춰 자산배분이 점차 보수적으로 변하도록 설계된 펀드지만 비용과 운용 방식은 상품마다 다르다.",
        "en_summary": "A target-date fund gradually shifts allocation toward a retirement year, but costs and glide paths vary by product.",
        "ko_point": "자동이라는 말은 방치해도 된다는 뜻이 아닙니다. 목표연도, 주식비중, 비용, 다른 계좌와의 중복을 확인해야 합니다.",
        "en_point": "Automatic does not mean ignore. Check target year, equity share, fees, and overlap with other accounts.",
        "ko_actions": ["목표연도와 실제 은퇴 계획이 맞는지 봅니다.", "현재 주식·채권 비중을 확인합니다.", "다른 연금계좌와 중복 위험을 점검합니다."],
        "en_actions": ["Check whether the target year matches your real plan.", "Review current stock and bond exposure.", "Check overlap with other retirement accounts."],
        "signals": ["target year", "glide path", "expense ratio", "equity share"],
        "ko_signals": ["목표연도", "글라이드패스", "비용비율", "주식비중"],
        "sources": ["finra_alloc", "investor_alloc", "finra_fees"],
        "tags": ["Target Date Fund", "Retirement", "Asset Allocation", "Investing"],
    },
    {
        "slug": "portfolio-rebalancing-rules",
        "ko_title": "포트폴리오 리밸런싱 규칙: 오른 자산을 파는 것이 왜 어려운가",
        "en_title": "Portfolio Rebalancing Rules: Why Selling Winners Feels Hard",
        "ko_summary": "리밸런싱은 수익률 예측이 아니라 목표 위험 수준으로 돌아가는 절차다. 미리 정한 규칙이 없으면 감정이 결정을 대신한다.",
        "en_summary": "Rebalancing is not return prediction; it is a process for returning to target risk. Without rules, emotions take over.",
        "ko_point": "오른 자산을 일부 파는 것은 아깝고 떨어진 자산을 사는 것은 불안합니다. 그래서 날짜 기준이나 비중 기준이 필요합니다.",
        "en_point": "Selling winners feels painful and adding to laggards feels risky. Date-based or threshold-based rules reduce improvisation.",
        "ko_actions": ["목표 자산비중을 기록합니다.", "정기 점검일이나 허용 범위를 정합니다.", "세금과 수수료를 고려해 신규 납입으로 먼저 조정합니다."],
        "en_actions": ["Record target allocation.", "Set a review date or drift threshold.", "Use new contributions first when taxes or fees matter."],
        "signals": ["allocation drift", "threshold band", "taxable account", "new contributions"],
        "ko_signals": ["비중 이탈", "허용 범위", "과세계좌", "신규 납입"],
        "sources": ["finra_alloc", "investor_alloc"],
        "tags": ["Rebalancing", "Asset Allocation", "Investing", "Risk"],
    },
    {
        "slug": "retirement-contribution-order",
        "ko_title": "은퇴저축 우선순위 세우기: 비상금, 고금리 부채, 장기투자 순서",
        "en_title": "Retirement Contribution Order: Emergency Cash, High-Rate Debt, Then Long-Term Investing",
        "ko_summary": "은퇴저축은 무조건 많이 넣기보다 비상금, 고금리 부채, 세제혜택, 장기 목표를 같은 순서표에 놓고 결정해야 한다.",
        "en_summary": "Retirement saving should be decided with emergency cash, high-rate debt, tax benefits, and long-term goals in one priority map.",
        "ko_point": "비상금 없이 투자하면 작은 사고에 장기자금을 깨게 되고, 고금리 부채를 방치하면 투자수익보다 이자가 빠르게 쌓일 수 있습니다.",
        "en_point": "Investing without emergency cash can force withdrawals, while high-rate debt can compound against you faster than investments help.",
        "ko_actions": ["비상금 최소 단계를 먼저 채웁니다.", "고금리 부채 상환과 장기투자를 비교합니다.", "세제혜택 계좌의 조건과 인출 제한을 확인합니다."],
        "en_actions": ["Fund the starter emergency tier first.", "Compare high-rate debt payoff with long-term investing.", "Review tax benefits and withdrawal limits of accounts."],
        "signals": ["emergency cash", "debt APR", "tax benefit", "withdrawal rule"],
        "ko_signals": ["비상금", "부채 APR", "세제혜택", "인출 규칙"],
        "sources": ["investor_risk", "irs_withholding", "cfpb_debt"],
        "tags": ["Retirement", "Debt", "Savings", "Planning"],
    },
    {
        "slug": "inflation-adjusted-goals",
        "ko_title": "물가를 반영한 목표금액 계산: 오늘의 1천만원은 미래에도 같지 않다",
        "en_title": "Inflation-Adjusted Goals: Today's Amount Is Not Tomorrow's Buying Power",
        "ko_summary": "장기 목표금액은 현재 가격만으로 정하면 부족해질 수 있다. 교육비, 주거비, 은퇴 생활비는 물가와 기간을 함께 반영해야 한다.",
        "en_summary": "Long-term goals can fall short if based only on today's prices. Education, housing, and retirement needs should include inflation and time.",
        "ko_point": "물가는 매년 조금씩 움직여도 10년, 20년 뒤에는 목표금액을 크게 바꿉니다. 명목금액과 실질 구매력을 구분해야 합니다.",
        "en_point": "Even modest annual inflation can materially change a 10- or 20-year target. Separate nominal amounts from real purchasing power.",
        "ko_actions": ["목표 날짜와 현재 비용을 적습니다.", "보수적인 물가 상승률 시나리오를 적용합니다.", "매년 목표금액과 저축률을 업데이트합니다."],
        "en_actions": ["Write the goal date and current cost.", "Apply conservative inflation scenarios.", "Update target amount and saving rate annually."],
        "signals": ["goal date", "current cost", "inflation assumption", "saving rate"],
        "ko_signals": ["목표 날짜", "현재 비용", "물가 가정", "저축률"],
        "sources": ["investor_compound", "cfpb_goals"],
        "tags": ["Inflation", "Savings Goals", "Planning", "Personal Finance"],
    },
    {
        "slug": "travel-fx-budget",
        "ko_title": "여행 환전 예산: 환율보다 수수료와 결제 방식을 같이 보기",
        "en_title": "Travel FX Budget: Exchange Rate, Fees, and Payment Method Together",
        "ko_summary": "해외여행 예산은 환율 한 줄보다 카드 수수료, 현금 인출 수수료, 환전 시점, 비상 결제수단을 함께 봐야 한다.",
        "en_summary": "A travel budget needs card fees, ATM fees, exchange timing, and backup payment methods, not just the headline exchange rate.",
        "ko_point": "좋은 환율을 찾다가 결제 수수료와 현금 인출비를 놓치면 총비용이 커질 수 있습니다. 결제 방식별 예산표가 필요합니다.",
        "en_point": "A good rate can be offset by card and ATM fees. Budget by payment method, not only currency.",
        "ko_actions": ["카드 해외결제 수수료와 환전 수수료를 확인합니다.", "현금, 카드, 비상카드 비중을 나눕니다.", "귀국 후 남은 외화와 카드 청구액을 기록합니다."],
        "en_actions": ["Check card foreign-transaction fees and exchange fees.", "Split cash, primary card, and backup card amounts.", "Record leftover cash and card charges after returning."],
        "signals": ["exchange spread", "card fee", "ATM fee", "backup payment"],
        "ko_signals": ["환전 스프레드", "카드 수수료", "ATM 수수료", "비상 결제수단"],
        "sources": ["cfpb_goals", "ftc_money"],
        "tags": ["Travel Budget", "FX", "Fees", "Cash Flow"],
    },
    {
        "slug": "investment-scam-red-flags",
        "ko_title": "투자 사기 위험 신호: 원금보장 고수익이라는 말부터 의심하기",
        "en_title": "Investment Scam Red Flags: Start With Guaranteed High Returns",
        "ko_summary": "투자 사기는 높은 수익률보다 원금보장, 비밀 유지, 모집 보상, 등록되지 않은 상품, 출금 지연 같은 신호로 먼저 드러난다.",
        "en_summary": "Investment scams reveal themselves through guaranteed returns, secrecy, recruitment rewards, unregistered products, and withdrawal delays.",
        "ko_point": "좋은 기회를 놓칠까 두려운 마음이 검증을 방해합니다. 등록 여부, 보관기관, 수익 구조, 출금 절차를 먼저 확인해야 합니다.",
        "en_point": "Fear of missing out blocks verification. Check registration, custody, return source, and withdrawal process first.",
        "ko_actions": ["원금보장 고수익 문구를 별도 표시합니다.", "등록된 금융회사와 상품인지 확인합니다.", "입금 전 가족이나 제3자에게 설명해 봅니다."],
        "en_actions": ["Flag guaranteed high-return language.", "Verify whether the firm and product are registered.", "Explain the offer to a third party before sending money."],
        "signals": ["guaranteed returns", "secrecy", "recruitment bonus", "withdrawal delay"],
        "ko_signals": ["원금보장 고수익", "비밀 유지 요구", "모집 보상", "출금 지연"],
        "sources": ["finra_redflags", "kinfa_report", "ftc_money"],
        "tags": ["Investment Scams", "Fraud", "Investor Protection", "Risk"],
    },
    {
        "slug": "first-paycheck-plan",
        "ko_title": "첫 월급 사용 계획: 소비보다 자동화 구조를 먼저 만들기",
        "en_title": "First Paycheck Plan: Build Automation Before Lifestyle Inflation",
        "ko_summary": "첫 월급은 소비를 늘리기 전에 비상금, 고정비, 저축 자동이체, 신용 관리 습관을 만드는 가장 좋은 시점이다.",
        "en_summary": "The first paycheck is the best moment to build emergency cash, bill structure, automatic savings, and credit habits before lifestyle inflation.",
        "ko_point": "처음 높아진 생활비는 나중에 줄이기 어렵습니다. 월급일 자동이체와 고정비 상한을 먼저 두면 선택지가 남습니다.",
        "en_point": "Lifestyle costs are harder to reduce after they rise. Payday automation and fixed-cost limits preserve options.",
        "ko_actions": ["월급일 다음날 저축 자동이체를 설정합니다.", "월 고정비 상한을 정합니다.", "신용카드는 결제일과 한도를 먼저 관리합니다."],
        "en_actions": ["Set savings transfer for the day after payday.", "Define a monthly fixed-cost ceiling.", "Control credit card due dates and limits first."],
        "signals": ["payday automation", "fixed costs", "credit limit", "starter emergency fund"],
        "ko_signals": ["월급일 자동화", "고정비", "카드 한도", "초기 비상금"],
        "sources": ["cfpb_goals", "cfpb_credit"],
        "tags": ["Young Adults", "Budgeting", "Savings", "Credit"],
    },
    {
        "slug": "couple-money-meeting",
        "ko_title": "부부·커플 돈 회의: 싸우지 않기 위한 월 30분 의제",
        "en_title": "Couple Money Meeting: A 30-Minute Monthly Agenda That Reduces Fights",
        "ko_summary": "커플의 돈 문제는 금액보다 기대와 역할이 달라 생긴다. 월 30분 회의로 고정비, 목표, 비상금, 개인 지출을 나누어야 한다.",
        "en_summary": "Money conflict often comes from mismatched expectations and roles, not only amounts. A monthly meeting separates bills, goals, buffers, and personal spending.",
        "ko_point": "모든 지출을 허락받는 구조는 오래가기 어렵습니다. 공동 목표와 개인 재량 지출을 함께 인정하는 규칙이 필요합니다.",
        "en_point": "A permission-based system rarely lasts. Couples need rules that protect shared goals and personal spending autonomy.",
        "ko_actions": ["공동 고정비와 개인 지출을 구분합니다.", "비상금 목표와 부채 상환 현황을 함께 봅니다.", "다음 달 큰 지출을 미리 합의합니다."],
        "en_actions": ["Separate shared bills from personal spending.", "Review emergency fund and debt payoff together.", "Agree on large upcoming expenses before the month starts."],
        "signals": ["shared bills", "personal allowance", "large purchase", "debt visibility"],
        "ko_signals": ["공동 고정비", "개인 재량비", "큰 구매", "부채 공개"],
        "sources": ["cfpb_goals", "ftc_money"],
        "tags": ["Couples", "Budgeting", "Money Meeting", "Planning"],
    },
    {
        "slug": "parents-support-boundaries",
        "ko_title": "부모님 지원과 내 재무 경계: 효도와 파산을 구분하는 기준",
        "en_title": "Supporting Parents Without Breaking Your Own Financial Plan",
        "ko_summary": "부모님 지원은 감정만으로 결정하면 장기 재무가 무너질 수 있다. 정기 지원, 긴급 지원, 대출 보증, 의료비를 구분해야 한다.",
        "en_summary": "Supporting parents can damage long-term finances if decided only emotionally. Separate regular support, emergencies, guarantees, and medical costs.",
        "ko_point": "도울 수 있는 금액과 빌려줄 수 없는 금액을 미리 정해야 가족관계와 재무계획을 동시에 지킬 수 있습니다.",
        "en_point": "Set what you can give and what you cannot lend before a crisis. That protects both relationships and the financial plan.",
        "ko_actions": ["월 지원 가능 금액을 예산에 넣습니다.", "대출 보증은 최악의 경우 전액 상환 가능성을 기준으로 봅니다.", "의료·간병비는 형제자매와 역할을 나눕니다."],
        "en_actions": ["Put monthly support in the budget.", "Treat loan guarantees as if you may owe the full amount.", "Divide medical and care roles with siblings when possible."],
        "signals": ["monthly support", "loan guarantee", "medical cost", "sibling agreement"],
        "ko_signals": ["월 지원액", "대출 보증", "의료비", "형제자매 합의"],
        "sources": ["cfpb_goals", "cfpb_debt"],
        "tags": ["Family Finance", "Budgeting", "Debt", "Planning"],
    },
    {
        "slug": "monthly-money-dashboard",
        "ko_title": "월간 돈 대시보드: 순자산, 현금흐름, 부채, 목표를 한 장에 보기",
        "en_title": "Monthly Money Dashboard: Net Worth, Cash Flow, Debt, and Goals on One Page",
        "ko_summary": "재무관리는 완벽한 앱보다 매달 같은 기준으로 순자산, 현금흐름, 부채, 목표 진행률을 보는 대시보드가 더 중요하다.",
        "en_summary": "Personal finance improves less from a perfect app and more from a monthly dashboard for net worth, cash flow, debt, and goal progress.",
        "ko_point": "한 달의 감정은 숫자를 왜곡합니다. 같은 날짜, 같은 항목, 같은 방식으로 보면 생활 습관과 재무 흐름이 분리되어 보입니다.",
        "en_point": "Monthly emotions distort the story. Same date, same categories, same method makes habits and finances easier to separate.",
        "ko_actions": ["매월 같은 날 순자산을 기록합니다.", "수입, 고정비, 변동비, 저축률을 업데이트합니다.", "다음 달 한 가지 행동만 정합니다."],
        "en_actions": ["Record net worth on the same date each month.", "Update income, fixed costs, flexible spending, and saving rate.", "Choose one action for the next month."],
        "signals": ["net worth", "saving rate", "debt balance", "goal progress"],
        "ko_signals": ["순자산", "저축률", "부채 잔액", "목표 진행률"],
        "sources": ["cfpb_goals", "investor_compound"],
        "tags": ["Money Dashboard", "Budgeting", "Net Worth", "Planning"],
    },
]


def escape_svg_text(value: str) -> str:
    return html.escape(value, quote=True)


def write_svg(path: Path, title: str, subtitle: str, labels: list[str], palette: tuple[str, str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    label_lines = "\n".join(
        f'<text x="84" y="{322 + index * 42}" fill="#fff7ed" font-size="23" font-family="Trebuchet MS, sans-serif">{escape_svg_text(label)}</text>'
        for index, label in enumerate(labels[:5])
    )
    bars = "\n".join(
        f'<rect x="{735 + index * 78}" y="{410 - index * 34}" width="46" height="{90 + index * 34}" rx="12" fill="#fbbf24" fill-opacity="{0.42 + index * 0.08:.2f}"/>'
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
    <pattern id="dots" width="38" height="38" patternUnits="userSpaceOnUse">
      <circle cx="4" cy="4" r="2" fill="#ffffff" fill-opacity="0.12"/>
    </pattern>
  </defs>
  <rect width="1200" height="675" fill="url(#bg)"/>
  <rect width="1200" height="675" fill="url(#dots)"/>
  <path d="M80 530 C210 430 300 455 430 350 C555 250 668 300 800 205 C930 112 1036 140 1120 86" fill="none" stroke="#fef3c7" stroke-width="9" stroke-linecap="round" opacity="0.88"/>
  {bars}
  <rect x="60" y="270" width="570" height="270" rx="30" fill="#111827" fill-opacity="0.50" stroke="#ffffff" stroke-opacity="0.18"/>
  <text x="72" y="108" fill="#f8fafc" font-size="45" font-family="Trebuchet MS, sans-serif" font-weight="700">{escape_svg_text(title)}</text>
  <text x="76" y="160" fill="#ffedd5" font-size="25" font-family="Trebuchet MS, sans-serif">{escape_svg_text(subtitle)}</text>
  {label_lines}
  <text x="76" y="610" fill="#fde68a" font-size="22" font-family="Trebuchet MS, sans-serif">MouseBall54 Personal Finance Guide</text>
</svg>
"""
    path.write_text(svg, encoding="utf-8")


def yaml_list(items: list[str]) -> str:
    return "\n".join(f"  - {item}" for item in items)


def normalize_markdown(text: str) -> str:
    normalized = "\n".join(line[4:] if line.startswith("    ") else line for line in text.splitlines()).lstrip()
    return normalized.replace("sidebar:\nnav:", "sidebar:\n    nav:") + "\n"


def source_notes(source_keys: list[str], lang: str) -> str:
    return "\n".join(f"- [{SOURCES[key][lang]}]({SOURCES[key]['url']})" for key in source_keys)


def related_links(index: int, lang: str) -> str:
    related = [TOPICS[(index + 1) % len(TOPICS)], TOPICS[(index + 11) % len(TOPICS)]]
    category_path = KO_CATEGORY.lower() if lang == "ko" else EN_CATEGORY.lower()
    if lang == "ko":
        return "\n".join(f"- [{topic['ko_title']}](/{{category}}/{topic['slug']}/)".replace("{category}", category_path) for topic in related)
    return "\n".join(f"- [{topic['en_title']}](/{{category}}/{topic['slug']}/)".replace("{category}", category_path) for topic in related)


def ko_post(topic: dict[str, object], index: int) -> str:
    slug = str(topic["slug"])
    image_dir = f"/images/{POST_DATE}-{slug}"
    signals = "\n".join(f"- **{signal}**: 이 숫자가 바뀌면 예산, 부채, 저축 목표 중 어느 항목이 영향을 받는지 확인합니다." for signal in topic["ko_signals"])
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
    translation_id: personal-finance-{slug}
    header:
      teaser: {image_dir}/hero.svg
      overlay_image: {image_dir}/hero.svg
      overlay_filter: 0.45
      image_description: >
        개인재무 판단에 필요한 핵심 숫자와 실행 순서를 요약한 교육용 점검 이미지입니다.
    excerpt: >
      {topic["ko_summary"]}
    seo_description: >
      {topic["ko_summary"]}
    categories:
      - {KO_CATEGORY}
    tags:
    {yaml_list(topic["tags"])}
    ---

    개인재무는 수익률 맞히기보다 **현금흐름, 부채 비용, 위험 완충, 목표 기간**을 꾸준히 관리하는 일입니다.

    {topic["ko_summary"]}

    이 글은 특정 상품 추천이나 개인별 재무 조언이 아닙니다. 공식 자료를 바탕으로 스스로 판단할 때 확인할 순서와 질문을 정리한 교육용 가이드입니다.

    ![{topic["ko_title"]} 핵심 재무 흐름]({image_dir}/hero.svg)

    ## 왜 중요한가

    {topic["ko_point"]}

    돈 문제는 보통 한 번의 큰 실수보다 작은 누락이 누적되며 커집니다. 결제일을 놓치거나, 수수료를 보지 않거나, 목표 기간과 위험 수준을 섞으면 같은 소득에서도 선택지가 줄어듭니다.

    그래서 먼저 봐야 할 것은 상품 이름이 아니라 **숫자의 위치**입니다. 이 돈이 언제 필요하고, 실패하면 어떤 비용이 생기며, 복구하려면 얼마의 시간이 필요한지를 적어야 합니다.

    ## 먼저 확인할 숫자

    {signals}

    숫자는 혼자서 답을 주지 않습니다. 같은 금리라도 기간이 다르면 부담이 달라지고, 같은 저축률이라도 비상금이 없으면 장기 목표를 깨게 될 수 있습니다.

    ![{topic["ko_title"]} 실행 체크리스트]({image_dir}/checklist.svg)

    ## 실행 순서

    {actions}

    가능하면 한 번에 완벽히 바꾸려 하지 마세요. 이번 달에 하나의 자동이체, 하나의 결제일, 하나의 부채 항목만 정리해도 다음 달 판단이 쉬워집니다.

    ## 실수하기 쉬운 지점

    가장 흔한 실수는 월상환액, 예상수익률, 할인율처럼 보기 쉬운 숫자만 보는 것입니다. 실제 재무 판단에는 총비용, 수수료, 세금, 유동성, 행동 지속성이 같이 들어갑니다.

    특히 부채와 투자를 동시에 다룰 때는 고금리 부채, 비상금, 장기투자 목적을 섞지 않는 것이 중요합니다. 단기 돈과 장기 돈은 같은 계좌에 있어도 다른 규칙으로 관리해야 합니다.

    ## 월간 점검 체크리스트

    {checklist}
    - 이번 결정이 예산, 비상금, 부채, 장기 목표 중 어디에 영향을 주는지 적습니다.
    - 국가별 세금과 금융 규정은 적용 지역의 공식 안내로 다시 확인합니다.

    ## 참고할 공식 자료

    {source_notes(topic["sources"], "ko")}

    ## 함께 보면 좋은 글

    {related_links(index, "ko")}
    """)


def en_post(topic: dict[str, object], index: int) -> str:
    slug = str(topic["slug"])
    image_dir = f"/images/{POST_DATE}-{slug}"
    signals = "\n".join(f"- **{signal}**: when this changes, check whether the impact hits budget, debt, savings, or long-term goals." for signal in topic["signals"])
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
    translation_id: personal-finance-{slug}
    header:
      teaser: {image_dir}/hero.svg
      overlay_image: {image_dir}/hero.svg
      overlay_filter: 0.45
      image_description: >
        An educational personal finance checklist image showing key numbers and action steps.
    excerpt: >
      {topic["en_summary"]}
    seo_description: >
      {topic["en_summary"]}
    categories:
      - {EN_CATEGORY}
    tags:
    {yaml_list(topic["tags"])}
    ---

    Personal finance is less about guessing returns and more about managing **cash flow, debt cost, risk buffers, and time horizon** consistently.

    {topic["en_summary"]}

    This article is educational and is not individualized financial advice or a product recommendation. It uses official-source guidance to organize the questions to ask before deciding.

    ![{topic["en_title"]} core finance flow]({image_dir}/hero.svg)

    ## Why It Matters

    {topic["en_point"]}

    Money problems often grow from accumulated small gaps rather than one dramatic mistake. Missing due dates, ignoring fees, or mixing time horizons can reduce options even when income stays the same.

    The first thing to identify is not the product name but **where the number belongs**. When will this money be needed, what is the cost of being wrong, and how long would recovery take?

    ## Numbers To Check First

    {signals}

    Numbers do not answer the question alone. The same rate changes with term length. The same saving rate behaves differently when there is no emergency buffer.

    ![{topic["en_title"]} action checklist]({image_dir}/checklist.svg)

    ## Practical Order

    {actions}

    Do not try to fix every part of the system in one month. One automated transfer, one bill due date, or one debt line can make next month's decision clearer.

    ## Common Mistakes

    The most common mistake is focusing only on visible numbers such as monthly payment, expected return, or discount rate. Real decisions also include total cost, fees, taxes, liquidity, and behavioral sustainability.

    When debt and investing overlap, avoid mixing high-rate debt, emergency cash, and long-term investments into one mental bucket. Short-term money and long-term money need different rules.

    ## Monthly Checkup

    {checklist}
    - Write whether the decision affects budget, emergency cash, debt, or long-term goals.
    - Recheck tax and financial rules through official guidance for the country where they apply.

    ## Source Notes

    {source_notes(topic["sources"], "en")}

    ## Related Reading

    {related_links(index, "en")}
    """)


def category_page(lang: str) -> str:
    if lang == "ko":
        return dedent("""\
        ---
        title: "Personal Finance"
        layout: archive
        permalink: /ko_personal_finance/
        lang: ko
        seo_description: >
          예산, 비상금, 부채 상환, 신용점수, 대출 총비용, 세금 준비, ETF, 자산배분, 은퇴저축, 투자 사기 예방을 다루는 교육용 개인재무 가이드입니다.
        sidebar:
            nav: "sidebar-category"
        ---

        Personal Finance 카테고리는 개인과 가정이 매달 반복해서 마주치는 돈 문제를 교육용 관점에서 정리합니다. 예산표, 비상금, 신용점수, 대출, 세금 준비, 투자 위험관리, 은퇴저축, 투자 사기 예방처럼 검색 수요가 꾸준하고 실제 판단에 바로 연결되는 주제를 다룹니다.

        이 카테고리는 특정 상품 추천이나 개인별 투자 조언을 제공하지 않습니다. CFPB, SEC Investor.gov, FINRA, IRS, FTC, 서민금융진흥원 같은 공식 자료를 참고해 스스로 확인해야 할 숫자, 질문, 실행 순서를 제시합니다.

        처음 읽는다면 월급날 예산 캘린더, 비상금 3단계, 부채 상환 방식부터 시작하세요. 투자 글은 위험감내도와 기간, 자산배분, 수수료 글을 먼저 읽은 뒤 개별 상품을 보는 순서가 안전합니다.

        ## 먼저 읽기

        - [월급날 예산 캘린더 만들기](/ko_personal_finance/paycheck-budget-calendar/)
        - [비상금 3단계 설계](/ko_personal_finance/emergency-fund-tiers/)
        - [투자 위험감내도와 기간](/ko_personal_finance/risk-tolerance-time-horizon/)

        ## 최신 글

        {% assign posts = site.categories["ko_Personal_Finance"] %}
        {% for post in posts %}
          {% include archive-single.html type=page.entries_layout %}
        {% endfor %}
        """)
    return dedent("""\
    ---
    title: "Personal Finance"
    layout: archive
    permalink: /en_personal_finance/
    lang: en
    seo_description: >
      Educational personal finance guides on budgeting, emergency funds, debt payoff, credit scores, loan costs, taxes, ETFs, asset allocation, retirement saving, and scam red flags.
    sidebar:
        nav: "sidebar-category"
    ---

    The Personal Finance category organizes practical money decisions that individuals and households face every month. It covers budgets, emergency funds, credit scores, loans, taxes, investment risk, retirement saving, and fraud prevention.

    This category does not provide individualized financial advice or product recommendations. It refers to official sources such as CFPB, SEC Investor.gov, FINRA, IRS, FTC, and Korea Inclusive Finance Agency to frame the numbers, questions, and action order readers should verify for themselves.

    Start with the paycheck budget calendar, emergency fund tiers, and debt payoff framework. For investing topics, read risk tolerance, asset allocation, and fee guides before comparing individual products.

    ## Start Here

    - [Paycheck Budget Calendar](/en_personal_finance/paycheck-budget-calendar/)
    - [Three Emergency Fund Tiers](/en_personal_finance/emergency-fund-tiers/)
    - [Risk Tolerance and Time Horizon](/en_personal_finance/risk-tolerance-time-horizon/)

    ## Latest Articles

    {% assign posts = site.categories["en_Personal_Finance"] %}
    {% for post in posts %}
      {% include archive-single.html type=page.entries_layout %}
    {% endfor %}
    """)


def main() -> None:
    palettes = [
        ("#164e63", "#92400e"),
        ("#0f172a", "#15803d"),
        ("#1e293b", "#b45309"),
        ("#312e81", "#0f766e"),
        ("#111827", "#a16207"),
    ]

    for index, topic in enumerate(TOPICS):
        slug = str(topic["slug"])
        image_path = ROOT / "images" / f"{POST_DATE}-{slug}"
        palette = palettes[index % len(palettes)]

        (ROOT / "_posts" / "ko" / f"{POST_DATE}-{slug}.md").write_text(
            normalize_markdown(ko_post(topic, index)),
            encoding="utf-8",
        )
        (ROOT / "_posts" / "en" / f"{POST_DATE}-{slug}.md").write_text(
            normalize_markdown(en_post(topic, index)),
            encoding="utf-8",
        )
        write_svg(
            image_path / "hero.svg",
            str(topic["en_title"])[:64],
            "Cash flow, risk buffers, and decision order",
            list(topic["signals"]),
            palette,
        )
        write_svg(
            image_path / "checklist.svg",
            "Personal Finance Checklist",
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
