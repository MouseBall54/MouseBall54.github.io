#!/usr/bin/env python3
"""Generate paired Consumer Rights posts and local SVG context images."""

from __future__ import annotations

import html
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parents[1]
POST_DATE = "2026-05-17"
LAST_MODIFIED_AT = "2026-05-23T17:30:00+09:00"
KO_CATEGORY = "ko_Consumer_Rights"
EN_CATEGORY = "en_Consumer_Rights"


SOURCES = {
    "ftc_subscriptions": {
        "ko": "FTC Free Trials, Auto-Renewals, and Negative Option Subscriptions",
        "en": "FTC Free Trials, Auto-Renewals, and Negative Option Subscriptions",
        "url": "https://consumer.ftc.gov/node/298618",
    },
    "ftc_online_orders": {
        "ko": "FTC Online Orders and Unordered Merchandise",
        "en": "FTC Online Orders and Unordered Merchandise",
        "url": "https://consumer.ftc.gov/articles/what-do-if-youre-billed-things-you-never-got-or-you-get-unordered-products",
    },
    "ftc_reviews": {
        "ko": "FTC How to Evaluate Online Reviews",
        "en": "FTC How to Evaluate Online Reviews",
        "url": "https://consumer.ftc.gov/articles/how-evaluate-online-reviews",
    },
    "ftc_dark_patterns": {
        "ko": "FTC Dark Patterns",
        "en": "FTC Dark Patterns",
        "url": "https://www.ftc.gov/reports/bringing-dark-patterns-light",
    },
    "ftc_reportfraud": {
        "ko": "FTC ReportFraud",
        "en": "FTC ReportFraud",
        "url": "https://reportfraud.ftc.gov/",
    },
    "ftc_identity": {
        "ko": "IdentityTheft.gov",
        "en": "IdentityTheft.gov",
        "url": "https://www.identitytheft.gov/",
    },
    "ftc_warranties": {
        "ko": "FTC Warranties",
        "en": "FTC Warranties",
        "url": "https://consumer.ftc.gov/articles/warranties",
    },
    "ftc_used_car": {
        "ko": "FTC Buying a Used Car From a Dealer",
        "en": "FTC Buying a Used Car From a Dealer",
        "url": "https://consumer.ftc.gov/articles/buying-used-car-dealer",
    },
    "ftc_service_contracts": {
        "ko": "FTC Auto Service Contracts and Warranties",
        "en": "FTC Auto Service Contracts and Warranties",
        "url": "https://consumer.ftc.gov/articles/auto-warranties-and-auto-service-contracts-0",
    },
    "ftc_home_improvement": {
        "ko": "FTC How To Avoid a Home Improvement Scam",
        "en": "FTC How To Avoid a Home Improvement Scam",
        "url": "https://consumer.ftc.gov/how-avoid-home-improvement-scam",
    },
    "cfpb_card_dispute": {
        "ko": "CFPB Credit Card Charge Disputes",
        "en": "CFPB Credit Card Charge Disputes",
        "url": "https://www.consumerfinance.gov/ask-cfpb/how-do-i-dispute-a-credit-card-charge-en-61/",
    },
    "cfpb_bank_unauthorized": {
        "ko": "CFPB Unauthorized Bank Transactions",
        "en": "CFPB Unauthorized Bank Transactions",
        "url": "https://www.consumerfinance.gov/ask-cfpb/how-do-i-get-my-money-back-after-i-discovered-an-unauthorized-transaction-or-money-missing-from-my-bank-account-en-1017/",
    },
    "cfpb_bnpl": {
        "ko": "CFPB Buy Now, Pay Later Market Report",
        "en": "CFPB Buy Now, Pay Later Market Report",
        "url": "https://www.consumerfinance.gov/data-research/research-reports/buy-now-pay-later-market-trends-and-consumer-impacts/",
    },
    "cfpb_complaint": {
        "ko": "CFPB Submit a Complaint",
        "en": "CFPB Submit a Complaint",
        "url": "https://www.consumerfinance.gov/complaint/",
    },
    "dot_refunds": {
        "ko": "U.S. DOT Airline Refunds",
        "en": "U.S. DOT Airline Refunds",
        "url": "https://www.transportation.gov/airconsumer/refunds",
    },
    "dot_delays": {
        "ko": "U.S. DOT Flight Delays and Cancellations",
        "en": "U.S. DOT Flight Delays and Cancellations",
        "url": "https://www.transportation.gov/airconsumer/flight-delays",
    },
    "dot_complaint": {
        "ko": "U.S. DOT Air Travel Complaint",
        "en": "U.S. DOT Air Travel Complaint",
        "url": "https://www.transportation.gov/airconsumer/complaint-process",
    },
    "fcc_cramming": {
        "ko": "FTC Mobile Cramming",
        "en": "FTC Mobile Cramming",
        "url": "https://www.ftc.gov/news-events/topics/mobile-cramming",
    },
    "fcc_broadband_labels": {
        "ko": "FCC Broadband Labels",
        "en": "FCC Broadband Labels",
        "url": "https://docs.fcc.gov/public/attachments/DOC-401799A1.pdf",
    },
    "fcc_complaints": {
        "ko": "FCC Consumer Complaints",
        "en": "FCC Consumer Complaints",
        "url": "https://consumercomplaints.fcc.gov/",
    },
    "cpsc_recalls": {
        "ko": "CPSC Recalls",
        "en": "CPSC Recalls",
        "url": "https://www.cpsc.gov/Recalls",
    },
    "fda_recalls": {
        "ko": "FDA 101: Product Recalls",
        "en": "FDA 101: Product Recalls",
        "url": "https://www.fda.gov/consumers/consumer-updates/fda-101-product-recalls",
    },
    "nhtsa_recalls": {
        "ko": "NHTSA Recalls",
        "en": "NHTSA Recalls",
        "url": "https://www.nhtsa.gov/recalls",
    },
    "econsumer": {
        "ko": "econsumer.gov Cross-Border Complaints",
        "en": "econsumer.gov Cross-Border Complaints",
        "url": "https://www.econsumer.gov/",
    },
    "kca": {
        "ko": "Korea Consumer Agency",
        "en": "Korea Consumer Agency",
        "url": "https://www.kca.go.kr/eng/index.do",
    },
    "kftc": {
        "ko": "KFTC E-commerce Policy",
        "en": "KFTC E-commerce Policy",
        "url": "https://www.ftc.go.kr/eng/contents.do?key=560",
    },
}


TOPICS = [
    {
        "slug": "subscription-cancel-free-trial",
        "ko_title": "무료체험과 자동결제 해지: 캘린더와 증거를 먼저 남기기",
        "en_title": "Free Trial and Auto-Renewal Cancellation: Calendar and Evidence First",
        "ko_summary": "무료체험은 체험 기간, 자동결제일, 해지 경로, 확인 메일을 함께 기록해야 예상하지 못한 반복 결제를 줄일 수 있다.",
        "en_summary": "Free trials become safer when the trial period, renewal date, cancellation path, and confirmation email are recorded together.",
        "ko_problem": "문제는 가입 화면은 쉽고 해지 화면은 늦게 찾게 되는 구조입니다.",
        "en_problem": "The practical problem is that sign-up is easy while the cancellation path is often found too late.",
        "ko_actions": ["가입 직후 자동결제일을 캘린더에 넣습니다.", "해지 버튼 위치와 확인 메일을 캡처합니다.", "결제 전날이 아니라 최소 2일 전에 해지 여부를 결정합니다."],
        "en_actions": ["Add the renewal date to a calendar immediately after signing up.", "Capture the cancellation path and confirmation email.", "Decide at least two days before billing, not the night before."],
        "ko_signals": ["무료체험 종료일", "자동결제 문구", "해지 확인 메일", "환불 정책"],
        "signals": ["trial end date", "auto-renewal language", "cancellation confirmation", "refund policy"],
        "sources": ["ftc_subscriptions", "kftc"],
        "tags": ["Subscriptions", "Refunds", "Consumer Rights", "Billing"],
    },
    {
        "slug": "online-order-never-arrived",
        "ko_title": "온라인 주문이 오지 않을 때: 배송 지연과 미배송을 구분하기",
        "en_title": "Online Order Never Arrived: Separate Delay From Non-Delivery",
        "ko_summary": "온라인 주문 분쟁은 주문일, 약속 배송일, 판매자 답변, 운송장 상태, 결제수단을 시간순으로 정리해야 해결 속도가 빨라진다.",
        "en_summary": "Online order disputes move faster when order date, promised delivery, seller responses, tracking status, and payment method are placed on a timeline.",
        "ko_problem": "판매자와 카드사에 같은 설명을 반복하다 보면 중요한 날짜가 흐려질 수 있습니다.",
        "en_problem": "Key dates become blurry when the same story is repeated to the seller and card issuer.",
        "ko_actions": ["주문 확인서와 약속 배송일을 저장합니다.", "판매자 문의는 채팅보다 기록이 남는 방식으로 보냅니다.", "미배송이 확인되면 결제수단별 분쟁 기간을 확인합니다."],
        "en_actions": ["Save the order confirmation and promised delivery date.", "Contact the seller through a channel that leaves records.", "Check payment-dispute deadlines once non-delivery is clear."],
        "ko_signals": ["약속 배송일", "운송장 정체", "판매자 무응답", "결제 분쟁 기한"],
        "signals": ["promised delivery date", "tracking stalled", "seller silence", "payment dispute deadline"],
        "sources": ["ftc_online_orders", "cfpb_card_dispute", "kca"],
        "tags": ["Online Shopping", "Delivery", "Refunds", "Disputes"],
    },
    {
        "slug": "return-refund-evidence-folder",
        "ko_title": "반품과 환불 증거 폴더: 영수증, 사진, 대화 기록을 한곳에 모으기",
        "en_title": "Return and Refund Evidence Folder: Receipts, Photos, and Messages Together",
        "ko_summary": "반품·환불은 감정적 항의보다 구매 조건, 상품 상태, 반품 접수, 배송 증빙, 판매자 답변을 한 폴더로 묶는 편이 효과적이다.",
        "en_summary": "Return and refund disputes are stronger when purchase terms, item condition, return request, shipping proof, and seller messages are stored in one folder.",
        "ko_problem": "분쟁이 길어지면 사진과 대화 기록이 앱 안에 흩어지고 증거가 약해집니다.",
        "en_problem": "When a dispute lasts, photos and messages scatter across apps and weaken the evidence trail.",
        "ko_actions": ["상품 수령 직후 포장과 하자를 사진으로 남깁니다.", "반품 접수 번호와 발송 영수증을 저장합니다.", "환불 예정일이 지나면 같은 자료로 단계적으로 이의제기합니다."],
        "en_actions": ["Photograph packaging and defects immediately after delivery.", "Save the return authorization and shipping receipt.", "Escalate with the same evidence after the refund date passes."],
        "ko_signals": ["구매 조건", "하자 사진", "반품 접수 번호", "환불 예정일"],
        "signals": ["purchase terms", "defect photos", "return authorization", "refund due date"],
        "sources": ["ftc_online_orders", "kca", "cfpb_card_dispute"],
        "tags": ["Refunds", "Returns", "Evidence", "Online Shopping"],
    },
    {
        "slug": "credit-card-charge-dispute",
        "ko_title": "신용카드 결제 이의제기: 차지백 전에 확인할 순서",
        "en_title": "Credit Card Charge Dispute: What to Check Before a Chargeback",
        "ko_summary": "신용카드 이의제기는 청구 오류, 미배송, 취소 미반영, 중복 결제처럼 사유를 분리하고 카드사 기한 안에 자료를 제출해야 한다.",
        "en_summary": "Credit card disputes require separating billing errors, non-delivery, failed cancellation, and duplicate charges, then submitting evidence within issuer deadlines.",
        "ko_problem": "카드사에 '억울하다'고 말하는 것보다 정확한 분쟁 사유와 날짜가 더 중요합니다.",
        "en_problem": "For card issuers, a precise reason and timeline matter more than a general feeling that the charge is unfair.",
        "ko_actions": ["청구서 날짜와 거래일을 구분합니다.", "판매자에게 먼저 문의한 기록을 남깁니다.", "카드사 양식에는 금액, 날짜, 사유, 증거를 짧게 정리합니다."],
        "en_actions": ["Separate statement date from transaction date.", "Keep a record of seller contact first.", "Summarize amount, date, reason, and evidence in the issuer form."],
        "ko_signals": ["청구 오류", "중복 결제", "판매자 답변", "카드사 제출 기한"],
        "signals": ["billing error", "duplicate charge", "seller response", "issuer deadline"],
        "sources": ["cfpb_card_dispute", "cfpb_complaint"],
        "tags": ["Credit Cards", "Chargebacks", "Disputes", "Billing"],
    },
    {
        "slug": "debit-bank-unauthorized-charge",
        "ko_title": "체크카드·계좌 무단출금: 발견 즉시 해야 할 기록과 신고",
        "en_title": "Debit Card or Bank Unauthorized Charge: Records and Reports to Make Fast",
        "ko_summary": "계좌 무단거래는 발견 시각, 거래 내역, 카드·계좌 차단, 금융기관 신고, 경찰 또는 소비자기관 신고 기록을 빠르게 남겨야 한다.",
        "en_summary": "Unauthorized bank or debit transactions require fast records of discovery time, transaction details, account blocking, bank notice, and complaint records.",
        "ko_problem": "신용카드보다 계좌에서 돈이 직접 빠져나간 상황은 시간 기록과 신고 순서가 더 중요합니다.",
        "en_problem": "When money leaves the account directly, timing and notice records become especially important.",
        "ko_actions": ["거래를 발견한 시간을 적고 화면을 캡처합니다.", "카드와 계좌 접근을 즉시 차단합니다.", "금융기관 신고 번호와 담당 부서를 기록합니다."],
        "en_actions": ["Write the discovery time and capture the transaction screen.", "Block the card and account access immediately.", "Record the bank report number and department."],
        "ko_signals": ["발견 시각", "무단거래 금액", "계좌 차단", "신고 접수 번호"],
        "signals": ["discovery time", "unauthorized amount", "account block", "report number"],
        "sources": ["cfpb_bank_unauthorized", "ftc_identity", "kca"],
        "tags": ["Debit Cards", "Banking", "Fraud", "Disputes"],
    },
    {
        "slug": "bnpl-refund-dispute",
        "ko_title": "BNPL 환불 분쟁: 할부 앱과 판매자 기록을 따로 관리하기",
        "en_title": "BNPL Refund Dispute: Track the App and the Seller Separately",
        "ko_summary": "후불결제와 BNPL은 판매자 환불과 결제앱 상환 일정이 따로 움직일 수 있어 환불 승인일과 청구 중단 여부를 분리해서 봐야 한다.",
        "en_summary": "BNPL refunds can split seller approval from payment-app repayment schedules, so refund approval and payment pause need separate tracking.",
        "ko_problem": "판매자가 환불했다고 말해도 BNPL 앱의 청구가 즉시 멈추지 않을 수 있습니다.",
        "en_problem": "A seller may say the refund is approved while the BNPL app continues its own billing schedule.",
        "ko_actions": ["판매자 환불 승인 화면과 BNPL 앱 화면을 모두 저장합니다.", "상환 예정일 전에 앱 고객센터에 분쟁 상태를 알립니다.", "연체 수수료와 신용 영향 문구를 확인합니다."],
        "en_actions": ["Save both seller refund approval and the BNPL app screen.", "Notify the app support before the next repayment date.", "Check late fees and credit-reporting language."],
        "ko_signals": ["환불 승인일", "상환 예정일", "연체 수수료", "앱 고객센터 기록"],
        "signals": ["refund approval date", "repayment date", "late fee", "app support record"],
        "sources": ["cfpb_bnpl", "cfpb_complaint"],
        "tags": ["BNPL", "Refunds", "Credit", "Disputes"],
    },
    {
        "slug": "fake-review-triage",
        "ko_title": "가짜 리뷰 판별 루틴: 별점보다 패턴과 증거를 보기",
        "en_title": "Fake Review Triage: Patterns and Evidence Before Star Ratings",
        "ko_summary": "가짜 리뷰는 별점 하나로 판단하기 어렵고 작성 시점, 반복 문구, 사진의 구체성, 구매 인증, 부정 리뷰 대응을 함께 봐야 한다.",
        "en_summary": "Fake reviews are hard to spot from stars alone; timing, repeated wording, photo specificity, verified purchases, and seller responses need to be read together.",
        "ko_problem": "리뷰 수가 많아도 같은 문장과 같은 시점의 글이 몰려 있으면 신뢰도가 달라집니다.",
        "en_problem": "A large review count means less when similar wording appears in a short time window.",
        "ko_actions": ["최신순과 낮은 별점 리뷰를 함께 봅니다.", "반복 문구와 과도하게 일반적인 칭찬을 표시합니다.", "외부 비교 사이트와 리콜 정보를 같이 확인합니다."],
        "en_actions": ["Read newest and low-star reviews together.", "Flag repeated wording and generic praise.", "Compare with outside sources and recall information."],
        "ko_signals": ["반복 문구", "짧은 기간 리뷰 폭증", "구매 인증", "부정 리뷰 대응"],
        "signals": ["repeated wording", "review spike", "verified purchase", "response to criticism"],
        "sources": ["ftc_reviews", "ftc_reportfraud"],
        "tags": ["Reviews", "Online Shopping", "Scams", "Consumer Rights"],
    },
    {
        "slug": "dark-pattern-checkout",
        "ko_title": "다크패턴 결제 화면: 숨은 동의와 반복 결제를 찾는 법",
        "en_title": "Dark Pattern Checkout: Finding Hidden Consent and Recurring Charges",
        "ko_summary": "다크패턴은 소비자가 의도하지 않은 선택을 하도록 화면을 설계하는 방식이므로 체크박스, 회색 글씨, 기본 선택, 타이머 문구를 확인해야 한다.",
        "en_summary": "Dark patterns steer choices through interface design, so check boxes, grey text, default selections, countdown language, and recurring-charge wording.",
        "ko_problem": "결제 직전 화면은 빠르게 넘기기 쉬워 가장 비싼 실수가 생기는 위치가 됩니다.",
        "en_problem": "Checkout screens are easy to rush through, which makes them the place where costly mistakes happen.",
        "ko_actions": ["결제 전 최종 화면을 캡처합니다.", "기본 선택된 추가 서비스와 구독 항목을 해제합니다.", "가격, 배송비, 세금, 반복 결제 문구를 한 줄씩 봅니다."],
        "en_actions": ["Capture the final checkout screen.", "Remove default add-ons and subscription boxes.", "Read price, shipping, tax, and recurring-charge language line by line."],
        "ko_signals": ["기본 선택", "회색 글씨", "카운트다운", "반복 결제"],
        "signals": ["default selection", "grey text", "countdown pressure", "recurring charge"],
        "sources": ["ftc_dark_patterns", "ftc_subscriptions"],
        "tags": ["Dark Patterns", "Checkout", "Subscriptions", "Online Shopping"],
    },
    {
        "slug": "junk-fees-total-price",
        "ko_title": "숨은 수수료와 총가격 비교: 결제 마지막 화면까지 봐야 하는 이유",
        "en_title": "Junk Fees and Total Price: Why the Last Checkout Screen Matters",
        "ko_summary": "숨은 수수료는 기본 가격 비교를 무너뜨리므로 배송비, 서비스료, 플랫폼 수수료, 취소 수수료를 포함한 총가격으로 비교해야 한다.",
        "en_summary": "Hidden fees break simple price comparison, so shipping, service fees, platform fees, and cancellation fees need to be included in total price.",
        "ko_problem": "검색 결과의 낮은 가격이 결제 마지막 화면에서는 가장 비싼 선택이 될 수 있습니다.",
        "en_problem": "The lowest search-result price can become the most expensive option at final checkout.",
        "ko_actions": ["비교표에는 첫 가격이 아니라 최종 결제액을 넣습니다.", "취소 수수료와 환불 불가 조건을 따로 표시합니다.", "회원가나 쿠폰 적용 조건을 스크린샷으로 남깁니다."],
        "en_actions": ["Put final checkout price, not first listed price, in the comparison table.", "Mark cancellation fees and non-refundable terms separately.", "Screenshot membership and coupon conditions."],
        "ko_signals": ["서비스료", "배송비", "취소 수수료", "쿠폰 조건"],
        "signals": ["service fee", "shipping fee", "cancellation fee", "coupon conditions"],
        "sources": ["ftc_dark_patterns", "ftc_online_orders", "kftc"],
        "tags": ["Fees", "Pricing", "Online Shopping", "Consumer Rights"],
    },
    {
        "slug": "marketplace-seller-verification",
        "ko_title": "마켓플레이스 판매자 확인: 플랫폼 이름만 믿지 않기",
        "en_title": "Marketplace Seller Verification: Do Not Trust the Platform Name Alone",
        "ko_summary": "마켓플레이스 구매는 플랫폼, 실제 판매자, 배송 주체, 반품 주소, 고객센터가 다를 수 있어 거래 상대를 먼저 확인해야 한다.",
        "en_summary": "Marketplace purchases can split platform, seller, shipper, return address, and support desk, so identify the actual counterparty first.",
        "ko_problem": "유명 플랫폼에서 샀다는 사실만으로 판매자 신뢰와 환불 가능성이 자동 보장되지는 않습니다.",
        "en_problem": "Buying on a famous platform does not automatically prove seller reliability or refund ease.",
        "ko_actions": ["판매자명, 사업자 정보, 반품 주소를 저장합니다.", "상품 페이지와 결제 페이지의 판매자가 같은지 봅니다.", "해외 배송과 국내 반품 가능 여부를 구분합니다."],
        "en_actions": ["Save seller name, business information, and return address.", "Check whether seller identity matches across product and payment pages.", "Separate overseas shipping from local return availability."],
        "ko_signals": ["실제 판매자", "반품 주소", "사업자 정보", "해외 배송"],
        "signals": ["actual seller", "return address", "business information", "overseas shipping"],
        "sources": ["ftc_online_orders", "econsumer", "kca"],
        "tags": ["Marketplaces", "Online Shopping", "Cross Border", "Refunds"],
    },
    {
        "slug": "cross-border-shopping-complaint",
        "ko_title": "해외직구 분쟁 제기: 국내 쇼핑몰처럼 처리되지 않을 때",
        "en_title": "Cross-Border Shopping Complaint: When It Does Not Work Like a Local Store",
        "ko_summary": "해외직구는 언어, 관할, 반품 배송비, 통관, 결제 분쟁 절차가 달라서 주문 전 판매자 위치와 분쟁 창구를 확인해야 한다.",
        "en_summary": "Cross-border shopping adds language, jurisdiction, return shipping, customs, and payment-dispute differences, so seller location and complaint channels matter before ordering.",
        "ko_problem": "국내 소비자 기준으로 환불을 기대했지만 실제 판매자는 해외 법인일 수 있습니다.",
        "en_problem": "A buyer may expect local refund norms while the actual seller is a foreign business.",
        "ko_actions": ["판매자 국가와 반품 배송비 부담 주체를 확인합니다.", "통관·관세·반품 불가 품목을 주문 전에 봅니다.", "분쟁 시 플랫폼, 결제사, 국제 소비자 신고 창구를 순서대로 사용합니다."],
        "en_actions": ["Check seller country and who pays return shipping.", "Review customs, duties, and non-returnable items before ordering.", "Escalate through platform, payment provider, and cross-border complaint channels."],
        "ko_signals": ["판매자 국가", "반품 국제배송비", "통관 조건", "국제 신고 창구"],
        "signals": ["seller country", "international return shipping", "customs terms", "cross-border complaint channel"],
        "sources": ["econsumer", "ftc_online_orders", "kca"],
        "tags": ["Cross Border", "Online Shopping", "Disputes", "Refunds"],
    },
    {
        "slug": "product-recall-check-routine",
        "ko_title": "제품 리콜 확인 루틴: 아이용품과 전자제품은 구매 후에도 확인하기",
        "en_title": "Product Recall Check Routine: Keep Checking After You Buy",
        "ko_summary": "제품 안전 리콜은 구매 후에도 발생할 수 있으므로 영수증, 모델명, 제조번호를 저장하고 리콜 데이터베이스를 주기적으로 확인해야 한다.",
        "en_summary": "Safety recalls can appear after purchase, so receipts, model numbers, and serial numbers should be saved and checked against recall databases.",
        "ko_problem": "리콜 소식은 판매자가 직접 알려주지 않으면 놓치기 쉽습니다.",
        "en_problem": "Recall news is easy to miss when the seller does not directly notify the buyer.",
        "ko_actions": ["모델명과 제조번호를 사진으로 저장합니다.", "어린이용품, 배터리 제품, 가전은 리콜 검색을 정기적으로 합니다.", "리콜 조치가 수리, 환불, 교환 중 무엇인지 확인합니다."],
        "en_actions": ["Photograph model and serial numbers.", "Check recalls regularly for children's products, battery products, and appliances.", "Confirm whether the remedy is repair, refund, or replacement."],
        "ko_signals": ["모델명", "제조번호", "리콜 조치", "구매처 기록"],
        "signals": ["model number", "serial number", "recall remedy", "purchase record"],
        "sources": ["cpsc_recalls", "kca"],
        "tags": ["Recalls", "Product Safety", "Consumer Rights", "Home"],
    },
    {
        "slug": "food-recall-home-routine",
        "ko_title": "식품 리콜 확인: 냉장고와 영수증을 같이 보는 습관",
        "en_title": "Food Recall Routine: Check the Refrigerator and Receipt Together",
        "ko_summary": "식품 리콜은 브랜드명만으로 부족하고 제품명, 유통기한, 로트번호, 구매처, 보관 상태를 함께 확인해야 한다.",
        "en_summary": "Food recalls require more than brand recognition; product name, expiration date, lot code, store, and storage status should be checked together.",
        "ko_problem": "같은 브랜드라도 특정 로트만 리콜되는 경우가 많아 대충 버리거나 대충 먹는 판단은 위험합니다.",
        "en_problem": "A recall often applies to specific lots, so guessing by brand alone can be unsafe or wasteful.",
        "ko_actions": ["냉장고 식품의 로트번호와 유통기한을 확인합니다.", "리콜 공지의 제품 사진과 문구를 비교합니다.", "섭취 후 증상이 있으면 의료기관과 공식 신고 창구를 확인합니다."],
        "en_actions": ["Check lot codes and expiration dates in the refrigerator.", "Compare the recall notice with product photos and wording.", "If symptoms occur after eating, seek medical help and official reporting channels."],
        "ko_signals": ["로트번호", "유통기한", "구매처", "섭취 후 증상"],
        "signals": ["lot code", "expiration date", "purchase store", "symptoms after eating"],
        "sources": ["fda_recalls", "kca"],
        "tags": ["Food Safety", "Recalls", "Home", "Consumer Rights"],
    },
    {
        "slug": "vehicle-recall-vin-check",
        "ko_title": "자동차 리콜 VIN 확인: 중고차와 가족차도 주기적으로 보기",
        "en_title": "Vehicle Recall VIN Check: Review Used and Family Cars Regularly",
        "ko_summary": "자동차 리콜은 차량번호보다 VIN과 제조 연식으로 확인하는 것이 정확하며 중고차 구매 전후에도 미수리 리콜을 확인해야 한다.",
        "en_summary": "Vehicle recalls are more accurately checked by VIN and model year, and open recalls should be reviewed before and after buying a used car.",
        "ko_problem": "중고차는 이전 소유자에게 리콜 통지가 갔을 수 있어 새 구매자가 놓치기 쉽습니다.",
        "en_problem": "Used-car recall notices may have gone to a previous owner, leaving the new buyer unaware.",
        "ko_actions": ["VIN을 사진으로 저장하고 공식 리콜 검색에 입력합니다.", "중고차 계약 전 미수리 리콜 여부를 확인합니다.", "리콜 수리 예약과 완료 기록을 보관합니다."],
        "en_actions": ["Photograph the VIN and enter it into official recall lookup.", "Check open recalls before signing for a used car.", "Keep recall repair appointments and completion records."],
        "ko_signals": ["VIN", "미수리 리콜", "수리 예약", "완료 기록"],
        "signals": ["VIN", "open recall", "repair appointment", "completion record"],
        "sources": ["nhtsa_recalls", "ftc_used_car"],
        "tags": ["Vehicle Recalls", "Used Cars", "Safety", "Consumer Rights"],
    },
    {
        "slug": "used-car-before-buying",
        "ko_title": "중고차 구매 전 체크: 가격보다 이력과 계약 조건을 먼저 보기",
        "en_title": "Used Car Before Buying: History and Contract Terms Before Price",
        "ko_summary": "중고차 구매는 낮은 가격보다 차량 이력, 보증 범위, 사고·침수 여부, 수리 기록, 금융 조건, 계약서 문구를 먼저 확인해야 한다.",
        "en_summary": "Used-car buying should start with history, warranty coverage, accident or flood records, repair records, finance terms, and contract wording before price.",
        "ko_problem": "차량 상태와 금융 조건을 따로 보면 실제 총비용을 과소평가하기 쉽습니다.",
        "en_problem": "Looking at car condition and financing separately can underestimate the real total cost.",
        "ko_actions": ["차량 이력과 리콜 여부를 확인합니다.", "시운전과 독립 정비 점검을 요청합니다.", "보증 제외 항목과 금융 비용을 계약서에서 확인합니다."],
        "en_actions": ["Check vehicle history and recalls.", "Ask for a test drive and independent inspection.", "Read warranty exclusions and finance costs in the contract."],
        "ko_signals": ["차량 이력", "침수·사고", "보증 제외", "금융 총비용"],
        "signals": ["vehicle history", "flood or accident", "warranty exclusion", "finance total cost"],
        "sources": ["ftc_used_car", "nhtsa_recalls", "cfpb_complaint"],
        "tags": ["Used Cars", "Contracts", "Warranty", "Consumer Rights"],
    },
    {
        "slug": "warranty-vs-service-contract",
        "ko_title": "보증과 서비스계약 차이: 무료 권리와 유료 상품을 구분하기",
        "en_title": "Warranty vs Service Contract: Separate Included Rights From Paid Add-Ons",
        "ko_summary": "보증, 연장보증, 서비스계약은 비용, 보장 범위, 제외 조건, 청구 절차가 달라서 결제 전 같은 표로 비교해야 한다.",
        "en_summary": "Warranties, extended warranties, and service contracts differ in cost, coverage, exclusions, and claim process, so compare them in one table before paying.",
        "ko_problem": "기본 보증으로 이미 되는 수리를 유료 계약으로 다시 사는 경우가 생길 수 있습니다.",
        "en_problem": "Consumers can end up paying for a service contract that overlaps with included warranty coverage.",
        "ko_actions": ["기본 보증 기간과 보장 항목을 먼저 읽습니다.", "유료 서비스계약의 제외 조건과 본인부담금을 확인합니다.", "청구 창구와 수리 기간을 구매 전에 묻습니다."],
        "en_actions": ["Read included warranty period and coverage first.", "Check service-contract exclusions and deductibles.", "Ask about claim channels and repair timelines before buying."],
        "ko_signals": ["기본 보증", "연장보증", "제외 조건", "본인부담금"],
        "signals": ["included warranty", "extended warranty", "exclusions", "deductible"],
        "sources": ["ftc_warranties", "ftc_service_contracts"],
        "tags": ["Warranty", "Service Contracts", "Repairs", "Consumer Rights"],
    },
    {
        "slug": "repair-estimate-consent",
        "ko_title": "수리 견적과 동의 기록: 예상보다 비싼 청구를 줄이는 법",
        "en_title": "Repair Estimates and Consent Records: Reducing Surprise Bills",
        "ko_summary": "수리 분쟁은 사전 견적, 추가 작업 승인, 교체 부품, 보증 여부, 결제 전 설명을 기록하면 불필요한 청구 논쟁을 줄일 수 있다.",
        "en_summary": "Repair disputes are easier to manage when initial estimate, approval for extra work, parts replaced, warranty status, and pre-payment explanation are recorded.",
        "ko_problem": "수리 중 추가 작업이 생겼다는 말만 듣고 동의 기록이 없으면 금액 다툼이 커집니다.",
        "en_problem": "When extra work is approved only verbally, the final bill can become difficult to challenge.",
        "ko_actions": ["수리 전 견적서를 문자나 이메일로 받습니다.", "추가 작업은 금액과 이유를 확인한 뒤 승인합니다.", "교체 부품과 작업 내역을 영수증에 남깁니다."],
        "en_actions": ["Get the repair estimate by text or email before work begins.", "Approve extra work only after amount and reason are clear.", "Keep replaced parts and work details on the invoice."],
        "ko_signals": ["사전 견적", "추가 작업 승인", "교체 부품", "작업 보증"],
        "signals": ["initial estimate", "extra-work approval", "replaced parts", "repair warranty"],
        "sources": ["ftc_warranties", "kca"],
        "tags": ["Repairs", "Estimates", "Warranty", "Disputes"],
    },
    {
        "slug": "flight-cancellation-refund",
        "ko_title": "항공편 취소 환불: 바우처와 현금 환불을 구분하기",
        "en_title": "Flight Cancellation Refund: Separate Vouchers From Cash Refunds",
        "ko_summary": "항공편 취소 환불은 누가 취소했는지, 대체편을 수락했는지, 결제수단이 무엇인지에 따라 처리 경로가 달라진다.",
        "en_summary": "Flight-cancellation refunds depend on who cancelled, whether an alternative was accepted, and what payment method was used.",
        "ko_problem": "바우처 제안을 수락하면 현금 환불 논의가 복잡해질 수 있습니다.",
        "en_problem": "Accepting a voucher can complicate a later request for cash refund.",
        "ko_actions": ["항공사 취소와 승객 취소를 구분합니다.", "대체편·바우처 수락 여부를 기록합니다.", "환불 요청일과 항공사 답변을 저장합니다."],
        "en_actions": ["Separate airline cancellation from passenger cancellation.", "Record whether an alternative flight or voucher was accepted.", "Save refund request date and airline response."],
        "ko_signals": ["항공사 취소", "바우처 수락", "환불 요청일", "결제수단"],
        "signals": ["airline cancellation", "voucher acceptance", "refund request date", "payment method"],
        "sources": ["dot_refunds", "dot_complaint", "cfpb_card_dispute"],
        "tags": ["Air Travel", "Refunds", "Travel", "Disputes"],
    },
    {
        "slug": "flight-delay-documentation",
        "ko_title": "항공편 지연 기록법: 보상보다 먼저 증거를 모으기",
        "en_title": "Flight Delay Documentation: Evidence Before Compensation Claims",
        "ko_summary": "항공편 지연은 원인, 지연 시간, 안내 방송, 식사·숙박 제공, 연결편 손실, 추가 비용 영수증을 한 타임라인에 모아야 한다.",
        "en_summary": "Flight delays should be documented with cause, delay time, announcements, meals or lodging offered, missed connections, and extra-cost receipts.",
        "ko_problem": "공항에서 받은 안내가 앱 기록과 다를 수 있어 현장 증거가 중요합니다.",
        "en_problem": "Airport announcements can differ from app records, making contemporaneous evidence important.",
        "ko_actions": ["출발·도착 예정과 실제 시간을 캡처합니다.", "항공사 안내 메시지와 공항 안내판을 저장합니다.", "추가 비용 영수증과 연결편 손실 내역을 보관합니다."],
        "en_actions": ["Capture scheduled and actual departure and arrival times.", "Save airline messages and airport-board photos.", "Keep receipts and missed-connection details."],
        "ko_signals": ["지연 원인", "실제 지연 시간", "연결편 손실", "추가 비용"],
        "signals": ["delay cause", "actual delay time", "missed connection", "extra costs"],
        "sources": ["dot_delays", "dot_complaint"],
        "tags": ["Air Travel", "Flight Delays", "Travel", "Evidence"],
    },
    {
        "slug": "travel-booking-platform-dispute",
        "ko_title": "여행 예약 플랫폼 분쟁: 항공사·호텔·플랫폼 책임을 나누기",
        "en_title": "Travel Booking Platform Dispute: Split Airline, Hotel, and Platform Responsibility",
        "ko_summary": "여행 예약 플랫폼 분쟁은 실제 서비스 제공자와 결제·예약 중개자가 달라 취소 규정, 환불 주체, 고객센터 기록을 분리해야 한다.",
        "en_summary": "Travel booking disputes often split service provider from payment or booking intermediary, so cancellation terms, refund party, and support records must be separated.",
        "ko_problem": "플랫폼은 호텔에 문의하라고 하고 호텔은 플랫폼에 문의하라고 하는 책임 회피가 생길 수 있습니다.",
        "en_problem": "The platform may send the consumer to the hotel while the hotel sends the consumer back to the platform.",
        "ko_actions": ["예약 확인서에서 계약 상대와 결제 상대를 확인합니다.", "취소 규정의 시간대와 기준일을 캡처합니다.", "플랫폼과 서비스 제공자에게 같은 자료를 보내 기록을 남깁니다."],
        "en_actions": ["Identify contract party and payment party in the booking confirmation.", "Capture cancellation terms including time zone and cutoff date.", "Send the same evidence to platform and provider."],
        "ko_signals": ["계약 상대", "결제 상대", "취소 기준일", "고객센터 기록"],
        "signals": ["contract party", "payment party", "cancellation cutoff", "support record"],
        "sources": ["ftc_online_orders", "dot_refunds", "econsumer"],
        "tags": ["Travel Booking", "Refunds", "Platforms", "Disputes"],
    },
    {
        "slug": "hotel-resort-fee-check",
        "ko_title": "호텔 리조트피와 추가요금: 숙박비 총액을 비교하는 법",
        "en_title": "Hotel Resort Fees and Add-Ons: Compare the Total Stay Cost",
        "ko_summary": "숙박 예약은 객실 요금만이 아니라 리조트피, 세금, 청소비, 주차비, 보증금, 취소 수수료를 포함한 총액으로 비교해야 한다.",
        "en_summary": "Hotel comparison needs total stay cost including resort fees, taxes, cleaning fees, parking, deposits, and cancellation fees.",
        "ko_problem": "검색 결과의 1박 요금은 실제 체크아웃 비용과 크게 다를 수 있습니다.",
        "en_problem": "The nightly search result can differ sharply from the actual checkout cost.",
        "ko_actions": ["최종 결제 전 총액 화면을 저장합니다.", "현장 결제 비용과 보증금 반환 조건을 확인합니다.", "취소 수수료와 무료 취소 기한을 따로 표시합니다."],
        "en_actions": ["Save the final total before payment.", "Check on-property fees and deposit return terms.", "Mark cancellation fee and free-cancellation cutoff separately."],
        "ko_signals": ["리조트피", "보증금", "현장 결제", "무료 취소 기한"],
        "signals": ["resort fee", "deposit", "on-property charge", "free-cancellation cutoff"],
        "sources": ["ftc_dark_patterns", "ftc_online_orders"],
        "tags": ["Hotels", "Travel", "Fees", "Refunds"],
    },
    {
        "slug": "telecom-bill-cramming",
        "ko_title": "통신요금 무단 부가서비스: 작은 금액도 매월 확인하기",
        "en_title": "Telecom Bill Cramming: Check Small Monthly Add-Ons",
        "ko_summary": "통신요금 고지서의 작은 부가서비스도 반복 청구되면 큰 비용이 되므로 서비스명, 가입일, 승인 기록, 해지 확인을 확인해야 한다.",
        "en_summary": "Small add-ons on phone bills become costly when repeated, so service name, enrollment date, authorization record, and cancellation confirmation should be checked.",
        "ko_problem": "매월 소액이라 지나치기 쉬운 항목이 실제로는 동의하지 않은 청구일 수 있습니다.",
        "en_problem": "A small recurring line item can hide an unauthorized charge.",
        "ko_actions": ["고지서의 모든 부가서비스명과 금액을 읽습니다.", "가입 동의 기록을 요청합니다.", "해지와 환불 요청 번호를 저장합니다."],
        "en_actions": ["Read every add-on name and amount on the bill.", "Ask for the authorization record.", "Save cancellation and refund request numbers."],
        "ko_signals": ["부가서비스명", "가입일", "동의 기록", "해지 확인"],
        "signals": ["add-on name", "enrollment date", "authorization record", "cancellation confirmation"],
        "sources": ["fcc_cramming", "fcc_complaints", "kca"],
        "tags": ["Telecom", "Billing", "Cramming", "Consumer Rights"],
    },
    {
        "slug": "broadband-label-speed-bill",
        "ko_title": "인터넷 요금제 라벨 읽기: 속도보다 총비용과 제한 조건 보기",
        "en_title": "Broadband Label Reading: Total Cost and Limits Before Speed",
        "ko_summary": "인터넷 요금제는 다운로드 속도뿐 아니라 월 총액, 장비 임대료, 데이터 제한, 약정, 할인 종료 후 요금을 함께 봐야 한다.",
        "en_summary": "Broadband plans should be compared by total monthly cost, equipment rental, data limits, contract term, and post-promotion price, not speed alone.",
        "ko_problem": "첫 달 할인 가격과 실제 13개월째 청구액이 다를 수 있습니다.",
        "en_problem": "The first-month promotional price can differ from the bill after the discount expires.",
        "ko_actions": ["월 요금, 장비료, 세금, 수수료를 합산합니다.", "할인 종료일과 약정 해지금을 기록합니다.", "속도 보장 조건과 실제 측정 방법을 확인합니다."],
        "en_actions": ["Add monthly fee, equipment, taxes, and fees.", "Record promotion end date and early termination fee.", "Check speed terms and measurement method."],
        "ko_signals": ["월 총액", "장비 임대료", "데이터 제한", "할인 종료일"],
        "signals": ["total monthly cost", "equipment rental", "data cap", "promotion end date"],
        "sources": ["fcc_broadband_labels", "fcc_complaints"],
        "tags": ["Broadband", "Internet", "Billing", "Contracts"],
    },
    {
        "slug": "mobile-plan-contract-change",
        "ko_title": "휴대폰 요금제 변경: 위약금과 할인 반환금을 먼저 계산하기",
        "en_title": "Mobile Plan Change: Calculate Penalties and Lost Discounts First",
        "ko_summary": "휴대폰 요금제 변경은 월 요금만 보면 안 되고 약정, 단말기 할부, 선택약정 할인, 부가서비스, 위약금까지 총비용으로 봐야 한다.",
        "en_summary": "Mobile plan changes should be read as total cost including contract term, device installment, plan discount, add-ons, and penalties.",
        "ko_problem": "월 요금이 낮아 보여도 할인 반환금과 단말기 잔액 때문에 총비용이 높아질 수 있습니다.",
        "en_problem": "A lower monthly plan can become expensive after lost discounts and remaining device payments.",
        "ko_actions": ["변경 전후 12개월 총비용을 비교합니다.", "위약금과 할인 반환금을 문자로 확인합니다.", "부가서비스 자동 가입 여부를 체크합니다."],
        "en_actions": ["Compare 12-month total cost before and after the change.", "Get penalties and discount clawbacks in writing.", "Check for automatic add-on enrollment."],
        "ko_signals": ["약정 기간", "단말기 잔액", "할인 반환금", "부가서비스"],
        "signals": ["contract term", "device balance", "discount clawback", "add-on service"],
        "sources": ["fcc_cramming", "kca"],
        "tags": ["Mobile Plans", "Contracts", "Billing", "Telecom"],
    },
    {
        "slug": "children-app-privacy-consent",
        "ko_title": "아동 앱 개인정보 동의: 무료 게임의 권한과 결제를 같이 보기",
        "en_title": "Children's App Privacy Consent: Permissions and Purchases Together",
        "ko_summary": "아동 앱은 무료처럼 보여도 위치, 연락처, 광고 식별자, 앱 내 결제, 구독 동의가 얽힐 수 있어 보호자 설정을 먼저 확인해야 한다.",
        "en_summary": "Children's apps may look free while combining location, contacts, ad identifiers, in-app purchases, and subscription consent, so guardian settings matter first.",
        "ko_problem": "아이 계정에서 생긴 결제와 데이터 수집은 뒤늦게 발견하면 정리하기 어렵습니다.",
        "en_problem": "Payments and data collection from a child's account become harder to untangle after the fact.",
        "ko_actions": ["앱 권한과 앱 내 결제 허용 여부를 확인합니다.", "무료체험과 구독 전환 문구를 보호자 계정에서 봅니다.", "광고·추적·위치 권한을 최소화합니다."],
        "en_actions": ["Check app permissions and in-app purchase settings.", "Review trial and subscription conversion text from the guardian account.", "Minimize ad, tracking, and location permissions."],
        "ko_signals": ["위치 권한", "앱 내 결제", "무료체험", "보호자 승인"],
        "signals": ["location permission", "in-app purchase", "free trial", "guardian approval"],
        "sources": ["ftc_subscriptions", "ftc_reportfraud", "kca"],
        "tags": ["Children", "Apps", "Privacy", "Subscriptions"],
    },
    {
        "slug": "identity-theft-after-shopping",
        "ko_title": "쇼핑 후 개인정보 도용 의심: 결제 분쟁과 신원도용 대응을 나누기",
        "en_title": "Identity Theft After Shopping: Separate Payment Dispute From Identity Recovery",
        "ko_summary": "쇼핑 이후 개인정보 도용이 의심되면 결제 취소만으로 끝내지 말고 계정, 카드, 신용정보, 신고 기록을 단계별로 정리해야 한다.",
        "en_summary": "If identity theft is suspected after shopping, payment reversal is not enough; accounts, cards, credit records, and reports need a staged response.",
        "ko_problem": "한 번의 결제 사고가 계정 탈취나 신용정보 문제로 이어질 수 있습니다.",
        "en_problem": "One payment incident can expand into account takeover or credit-file problems.",
        "ko_actions": ["문제 거래와 계정 접속 기록을 분리합니다.", "카드 교체와 비밀번호 변경을 같은 날 처리합니다.", "신원도용 신고와 복구 계획을 문서로 남깁니다."],
        "en_actions": ["Separate transaction evidence from account-access evidence.", "Replace cards and change passwords on the same day.", "Document identity-theft report and recovery plan."],
        "ko_signals": ["무단거래", "계정 접속", "카드 교체", "신원도용 신고"],
        "signals": ["unauthorized transaction", "account access", "card replacement", "identity-theft report"],
        "sources": ["ftc_identity", "cfpb_card_dispute", "ftc_reportfraud"],
        "tags": ["Identity Theft", "Fraud", "Credit Cards", "Recovery"],
    },
    {
        "slug": "gym-membership-cancel",
        "ko_title": "헬스장 회원권 해지: 구두 약속보다 계약서와 해지 확인",
        "en_title": "Gym Membership Cancellation: Contract and Confirmation Over Verbal Promises",
        "ko_summary": "헬스장 회원권 분쟁은 약정 기간, 자동연장, 중도해지 수수료, 양도 가능 여부, 해지 확인서를 계약서에서 확인해야 한다.",
        "en_summary": "Gym membership disputes depend on contract term, auto-renewal, early cancellation fee, transferability, and written cancellation confirmation.",
        "ko_problem": "직원이 말한 조건과 계약서의 자동연장 문구가 다르면 증명하기 어렵습니다.",
        "en_problem": "A staff promise is difficult to prove if the contract says something different about renewal.",
        "ko_actions": ["계약 전 자동연장과 해지 수수료를 표시합니다.", "해지 요청은 날짜가 남는 방식으로 보냅니다.", "마지막 결제와 환불 산정 내역을 요청합니다."],
        "en_actions": ["Mark auto-renewal and cancellation fee before signing.", "Send cancellation through a dated channel.", "Request final charge and refund calculation details."],
        "ko_signals": ["자동연장", "중도해지 수수료", "양도 조건", "해지 확인"],
        "signals": ["auto-renewal", "early cancellation fee", "transfer terms", "cancellation confirmation"],
        "sources": ["ftc_subscriptions", "kca"],
        "tags": ["Memberships", "Contracts", "Subscriptions", "Refunds"],
    },
    {
        "slug": "rental-car-damage-fees",
        "ko_title": "렌터카 손상비 분쟁: 인수·반납 사진이 핵심 증거",
        "en_title": "Rental Car Damage Fees: Pickup and Return Photos Are Core Evidence",
        "ko_summary": "렌터카 손상비는 차량 인수 전후 사진, 연료·주행거리, 기존 흠집, 보험 조건, 반납 확인 기록이 없으면 다투기 어렵다.",
        "en_summary": "Rental car damage fees are difficult to dispute without pickup and return photos, fuel and mileage records, pre-existing damage, insurance terms, and return confirmation.",
        "ko_problem": "반납 후 며칠 뒤 청구된 손상비는 현장 사진이 없으면 반박 자료가 약합니다.",
        "en_problem": "A damage bill sent days after return is hard to challenge without photos from the lot.",
        "ko_actions": ["인수 전 외관과 휠, 유리, 내부를 동영상으로 기록합니다.", "직원이 표시한 기존 흠집 문서를 저장합니다.", "반납 시 연료, 주행거리, 차량 상태를 다시 촬영합니다."],
        "en_actions": ["Record exterior, wheels, glass, and interior before driving away.", "Save staff-marked pre-existing damage forms.", "Photograph fuel, mileage, and condition at return."],
        "ko_signals": ["인수 사진", "기존 흠집", "보험 조건", "반납 확인"],
        "signals": ["pickup photos", "pre-existing damage", "insurance terms", "return confirmation"],
        "sources": ["ftc_online_orders", "cfpb_card_dispute", "econsumer"],
        "tags": ["Rental Cars", "Travel", "Fees", "Evidence"],
    },
    {
        "slug": "home-repair-contractor-deposit",
        "ko_title": "집수리 계약금 분쟁: 견적서, 공정표, 선금 조건을 먼저 고정하기",
        "en_title": "Home Repair Contractor Deposit: Lock Estimate, Milestones, and Payment Terms First",
        "ko_summary": "집수리와 인테리어 계약은 계약금, 공정표, 자재, 완료일, 추가비용 승인, 하자보수 조건을 문서로 남겨야 분쟁을 줄일 수 있다.",
        "en_summary": "Home repair contracts need written records of deposit, milestones, materials, completion date, extra-work approval, and warranty terms to reduce disputes.",
        "ko_problem": "방문 판매식 권유나 급한 수리 상황에서는 계약금과 추가비용 조건을 충분히 확인하지 못하기 쉽습니다.",
        "en_problem": "Door-to-door offers or urgent repairs can push consumers into paying deposits before the scope and extra-cost rules are clear.",
        "ko_actions": ["공사 범위, 자재, 완료일, 총액이 들어간 서면 견적을 받습니다.", "선금과 중도금은 공정 단계와 연결합니다.", "추가 작업은 금액과 이유를 문자나 이메일로 승인합니다."],
        "en_actions": ["Get a written estimate with scope, materials, completion date, and total price.", "Tie deposit and progress payments to milestones.", "Approve extra work by text or email with amount and reason."],
        "ko_signals": ["계약금", "공정표", "추가 작업 승인", "하자보수 조건"],
        "signals": ["deposit", "milestone schedule", "extra-work approval", "repair warranty terms"],
        "sources": ["ftc_home_improvement", "kca", "ftc_reportfraud"],
        "tags": ["Home Repair", "Contracts", "Deposits", "Scams"],
    },
    {
        "slug": "complaint-escalation-map",
        "ko_title": "소비자 민원 제기 순서: 판매자, 플랫폼, 결제사, 기관으로 단계화하기",
        "en_title": "Consumer Complaint Escalation Map: Seller, Platform, Payment Provider, Agency",
        "ko_summary": "소비자 민원은 처음부터 모든 기관에 보내기보다 판매자, 플랫폼, 결제사, 감독기관 순서로 같은 증거를 정리해 단계적으로 올리는 편이 효과적이다.",
        "en_summary": "Consumer complaints work better when the same evidence is escalated step by step through seller, platform, payment provider, and agency instead of being scattered everywhere.",
        "ko_problem": "분노한 긴 글보다 날짜와 금액, 요청사항, 증거를 담은 짧은 표가 더 잘 작동합니다.",
        "en_problem": "A short table with dates, amounts, request, and evidence usually works better than an angry long message.",
        "ko_actions": ["사건 타임라인을 한 페이지로 만듭니다.", "원하는 해결책을 환불, 교환, 수리, 청구 취소 중 하나로 씁니다.", "각 단계의 접수 번호와 답변 기한을 기록합니다."],
        "en_actions": ["Create a one-page event timeline.", "State the requested remedy as refund, replacement, repair, or charge reversal.", "Record case numbers and response deadlines at each step."],
        "ko_signals": ["타임라인", "요청 해결책", "접수 번호", "답변 기한"],
        "signals": ["timeline", "requested remedy", "case number", "response deadline"],
        "sources": ["cfpb_complaint", "fcc_complaints", "dot_complaint", "ftc_reportfraud"],
        "tags": ["Complaints", "Disputes", "Evidence", "Consumer Rights"],
    },
]


def slug_path(slug: str, lang: str) -> str:
    category = KO_CATEGORY if lang == "ko" else EN_CATEGORY
    return f"/{category.lower()}/{slug}/"


def svg_lines(lines: list[str], x: int, y: int, size: int = 28, gap: int = 42) -> str:
    return "\n".join(
        f'<text x="{x}" y="{y + index * gap}" font-family="Arial, sans-serif" font-size="{size}" fill="#24303f">{html.escape(line)}</text>'
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
  <desc id="desc">Consumer rights briefing image with evidence, timeline, escalation, and refund decision points.</desc>
  <rect width="1280" height="720" fill="#f7f1e6"/>
  <circle cx="1050" cy="120" r="230" fill="#f4b45f" opacity="0.42"/>
  <circle cx="160" cy="610" r="240" fill="#86b8d8" opacity="0.34"/>
  <rect x="84" y="88" width="1112" height="544" rx="42" fill="#fffdf8" opacity="0.95"/>
  <text x="130" y="158" font-family="Arial, sans-serif" font-size="28" letter-spacing="4" fill="#6b6f7d">CONSUMER RIGHTS</text>
  <text x="130" y="220" font-family="Arial, sans-serif" font-size="42" font-weight="700" fill="#1f2a44">{html.escape(title[:66])}</text>
  <text x="130" y="276" font-family="Arial, sans-serif" font-size="28" fill="#41506a">{html.escape(ko_title[:70])}</text>
  <g transform="translate(132 350)">
    <rect width="250" height="116" rx="24" fill="#2c5f8a"/>
    <text x="26" y="48" font-family="Arial, sans-serif" font-size="25" font-weight="700" fill="#ffffff">Evidence</text>
    <text x="26" y="84" font-family="Arial, sans-serif" font-size="21" fill="#eaf5ff">receipt, screenshot</text>
  </g>
  <g transform="translate(430 350)">
    <rect width="250" height="116" rx="24" fill="#c06442"/>
    <text x="26" y="48" font-family="Arial, sans-serif" font-size="25" font-weight="700" fill="#ffffff">Timeline</text>
    <text x="26" y="84" font-family="Arial, sans-serif" font-size="21" fill="#fff1ea">dates, deadlines</text>
  </g>
  <g transform="translate(728 350)">
    <rect width="250" height="116" rx="24" fill="#4e7c59"/>
    <text x="26" y="48" font-family="Arial, sans-serif" font-size="25" font-weight="700" fill="#ffffff">Escalation</text>
    <text x="26" y="84" font-family="Arial, sans-serif" font-size="21" fill="#edfff1">seller, agency</text>
  </g>
  <text x="132" y="548" font-family="Arial, sans-serif" font-size="25" fill="#24303f">Start with the contract, preserve proof, then escalate through the right channel.</text>
</svg>
"""

    signal_lines = [f"{index + 1}. {signal}" for index, signal in enumerate(signals[:4])]
    ko_signal_lines = [f"{index + 1}. {signal}" for index, signal in enumerate(ko_signals[:4])]
    checklist = f"""<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="720" viewBox="0 0 1280 720" role="img" aria-labelledby="title desc">
  <title id="title">{html.escape(title)} evidence checklist</title>
  <desc id="desc">Checklist image for consumer evidence, deadline tracking, and escalation records.</desc>
  <rect width="1280" height="720" fill="#edf4f7"/>
  <rect x="74" y="72" width="1132" height="576" rx="36" fill="#ffffff"/>
  <text x="118" y="142" font-family="Arial, sans-serif" font-size="36" font-weight="700" fill="#1f2a44">Evidence Checklist</text>
  <text x="118" y="192" font-family="Arial, sans-serif" font-size="25" fill="#506070">{html.escape(title[:80])}</text>
  <rect x="118" y="244" width="500" height="300" rx="28" fill="#f7f1e6"/>
  <text x="152" y="296" font-family="Arial, sans-serif" font-size="29" font-weight="700" fill="#2c5f8a">English Signals</text>
  {svg_lines(signal_lines, 152, 356, 25, 46)}
  <rect x="662" y="244" width="500" height="300" rx="28" fill="#e8f1e9"/>
  <text x="696" y="296" font-family="Arial, sans-serif" font-size="29" font-weight="700" fill="#2c5f8a">한국어 신호</text>
  {svg_lines(ko_signal_lines, 696, 356, 25, 46)}
  <text x="118" y="600" font-family="Arial, sans-serif" font-size="24" fill="#24303f">Keep every complaint short: date, amount, promise, evidence, request, next deadline.</text>
</svg>
"""

    (image_dir / "hero.svg").write_text(hero, encoding="utf-8")
    (image_dir / "checklist.svg").write_text(checklist, encoding="utf-8")


def source_notes(topic: dict[str, object], lang: str) -> str:
    return "\n".join(f"- [{SOURCES[key][lang]}]({SOURCES[key]['url']})" for key in topic["sources"])


def bullet_lines(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)


def signal_bullets(topic: dict[str, object], lang: str) -> str:
    signals = topic["ko_signals"] if lang == "ko" else topic["signals"]
    if lang == "ko":
        return "\n".join(
            f"- **{signal}**: {topic['ko_title']}에서는 이 항목의 금액, 날짜, 약속 문구, 증거 위치를 같이 확인합니다."
            for signal in signals
        )
    return "\n".join(
        f"- **{signal}**: in {topic['en_title']}, check amount, date, promise wording, and where the evidence is stored."
        for signal in signals
    )


def evidence_bullets(topic: dict[str, object], lang: str) -> str:
    if lang == "ko":
        labels = ["영수증과 주문번호", "약관과 화면 캡처", "대화 기록", "기한"]
        details = [
            f"항목 **{topic['ko_signals'][0]}**을 확인할 수 있는 거래번호, 결제수단, 판매자명을 저장합니다.",
            f"{topic['ko_signals'][1]}와 관련된 취소·환불·수수료 문구를 결제 전후로 캡처합니다.",
            f"{topic['ko_signals'][2]}에 대해 판매자나 플랫폼이 답한 날짜와 담당 채널을 남깁니다.",
            f"항목 **{topic['ko_signals'][3]}**이 지나기 전에 다음 단계로 올릴 기준일을 캘린더에 둡니다.",
        ]
        return "\n".join(f"- **{label}**: {detail}" for label, detail in zip(labels, details))

    labels = ["Receipt and order number", "Terms and screenshots", "Message records", "Deadlines"]
    details = [
        f"save transaction ID, payment method, and seller identity that prove {topic['signals'][0]}.",
        f"capture cancellation, refund, and fee language related to {topic['signals'][1]} before and after payment.",
        f"keep dated seller or platform replies about {topic['signals'][2]}.",
        f"put the next escalation date on a calendar before {topic['signals'][3]} becomes stale.",
    ]
    return "\n".join(f"- **{label}**: {detail}" for label, detail in zip(labels, details))


def ko_case_frame(topic: dict[str, object]) -> str:
    return (
        f"{topic['ko_title']}의 핵심은 다음 두 항목을 같은 타임라인에 올리는 것입니다: "
        f"**{topic['ko_signals'][0]}**, **{topic['ko_signals'][1]}**. {topic['ko_problem']} "
        f"이때 **{topic['ko_signals'][2]}** 관련 기록이 "
        f"남아 있지 않으면 판매자, 플랫폼, 결제사 중 어디에 먼저 제기해야 하는지 흐려집니다."
    )


def en_case_frame(topic: dict[str, object]) -> str:
    return (
        f"The core of {topic['en_title']} is putting {topic['signals'][0]} and {topic['signals'][1]} "
        f"on the same timeline. {topic['en_problem']} Without a record of {topic['signals'][2]}, "
        f"it becomes harder to decide whether to escalate to the seller, platform, or payment provider first."
    )


def ko_signal_context(topic: dict[str, object]) -> str:
    return (
        f"항목 **{topic['ko_signals'][0]}**은 사건의 시작점이고 **{topic['ko_signals'][3]}**은 다음 단계로 올릴 기준점입니다. "
        f"둘 사이에 두 항목인 **{topic['ko_signals'][1]}**, **{topic['ko_signals'][2]}**을 넣으면 민원 내용이 짧아지고, "
        f"같은 자료를 판매자·플랫폼·결제사에 반복해서 사용할 수 있습니다."
    )


def en_signal_context(topic: dict[str, object]) -> str:
    return (
        f"{topic['signals'][0]} is the starting point and {topic['signals'][3]} is the escalation trigger. "
        f"Putting {topic['signals'][1]} and {topic['signals'][2]} between them shortens the complaint and lets "
        f"the same evidence be reused with seller, platform, or payment provider."
    )


def ko_handling_context(topic: dict[str, object]) -> str:
    return (
        f"처리 순서는 '{topic['ko_actions'][0]}'에서 시작합니다. 이후 '{topic['ko_actions'][1]}'를 완료해야 "
        f"상대방이 '자료 부족'을 이유로 답변을 미루는 상황을 줄일 수 있습니다."
    )


def en_handling_context(topic: dict[str, object]) -> str:
    return (
        f"The handling order starts with: {topic['en_actions'][0]} After that, {topic['en_actions'][1]} "
        f"reduces the chance that the other party delays by saying records are incomplete."
    )


def related_links(index: int, lang: str) -> str:
    total = len(TOPICS)
    related = [TOPICS[(index + 1) % total], TOPICS[(index + 2) % total]]
    if lang == "ko":
        return "\n".join(f"- [{item['ko_title']}]({slug_path(item['slug'], 'ko')})" for item in related)
    return "\n".join(f"- [{item['en_title']}]({slug_path(item['slug'], 'en')})" for item in related)


def front_matter(topic: dict[str, object], lang: str, index: int) -> str:
    slug = topic["slug"]
    category = KO_CATEGORY if lang == "ko" else EN_CATEGORY
    title = topic["ko_title"] if lang == "ko" else topic["en_title"]
    summary = topic["ko_summary"] if lang == "ko" else topic["en_summary"]
    image_description = (
        "소비자 분쟁에서 증거, 날짜, 계약 문구, 신고 순서를 한눈에 정리한 교육용 이미지입니다."
        if lang == "ko"
        else "Consumer rights briefing image organizing evidence, dates, contract wording, and escalation order for disputes."
    )
    tags = "\n".join(f"  - {tag}" for tag in topic["tags"])
    minute = index % 60
    return f"""---
layout: single
title: >
  {title}
seo_title: >
  {title}
date: {POST_DATE}T10:{minute:02d}:00+09:00
last_modified_at: {LAST_MODIFIED_AT}
lang: {lang}
translation_id: consumer-rights-{slug}
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


def clean_body(text: str) -> str:
    lines = [line[8:] if line.startswith("        ") else line for line in text.splitlines()]
    return "\n".join(lines).strip() + "\n"


def ko_body(topic: dict[str, object], index: int) -> str:
    slug = topic["slug"]
    return clean_body(
        f"""
        {topic["ko_summary"]}

        이 글은 법률 자문이 아닙니다. **{topic["ko_title"]}**에서 필요한 증거 정리, 날짜 확인, 단계적 이의제기를 공식 자료 기반으로 설명하는 교육용 가이드입니다.

        ![{topic["ko_title"]} 핵심 흐름 요약](/images/{POST_DATE}-{slug}/hero.svg)

        ## 왜 이 문제가 자주 생기나

        {ko_case_frame(topic)}

        이 문제를 해결하려면 감정적인 설명보다 **짧은 타임라인과 증거 묶음**이 먼저입니다. 특히 세 항목인 **{topic["ko_signals"][0]}**, **{topic["ko_signals"][1]}**, **{topic["ko_signals"][2]}**이 한 장에 모이면 판매자에게 보낼 문구와 공식기관에 제출할 문구가 거의 같아집니다.

        ## 먼저 저장할 자료

        {evidence_bullets(topic, "ko")}

        ## 현재 확인할 신호

        {signal_bullets(topic, "ko")}

        {ko_signal_context(topic)}

        ![{topic["ko_title"]} 증거 체크리스트](/images/{POST_DATE}-{slug}/checklist.svg)

        ## 실전 처리 순서

        {bullet_lines(topic["ko_actions"])}

        {ko_handling_context(topic)}

        ## 민원 문구를 짧게 쓰는 법

        긴 감정 설명보다 다음 형식이 더 잘 작동합니다.

        1. 항목 **{topic["ko_signals"][0]}**이 발생한 날짜와 금액을 씁니다.
        2. 항목 **{topic["ko_signals"][1]}** 관련해 판매자나 서비스가 약속한 조건을 씁니다.
        3. 원하는 해결책을 하나로 정합니다. 예를 들어 환불, 교환, 수리, 청구 취소 중 하나입니다.
        4. **{topic["ko_signals"][2]}**, **{topic["ko_signals"][3]}**을 증거 목록과 답변 기한으로 붙입니다.

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

        This article is educational information, not legal advice. It explains a practical workflow for **{topic["en_title"]}** using evidence, dates, deadlines, and official-source escalation references.

        ![{topic["en_title"]} core flow summary](/images/{POST_DATE}-{slug}/hero.svg)

        ## Why This Problem Happens

        {en_case_frame(topic)}

        The practical solution starts with a **short timeline and evidence folder**, not a long emotional explanation. When {topic["signals"][0]}, {topic["signals"][1]}, and {topic["signals"][2]} are on one page, the seller message and agency complaint can use almost the same facts.

        ## What To Save First

        {evidence_bullets(topic, "en")}

        ## Signals To Watch

        {signal_bullets(topic, "en")}

        {en_signal_context(topic)}

        ![{topic["en_title"]} evidence checklist](/images/{POST_DATE}-{slug}/checklist.svg)

        ## Practical Handling Order

        {bullet_lines(topic["en_actions"])}

        {en_handling_context(topic)}

        ## How To Write a Short Complaint

        A short structured complaint usually works better than a long frustrated message.

        1. State when {topic["signals"][0]} happened and the amount involved.
        2. State the promise or policy connected to {topic["signals"][1]}.
        3. State one requested remedy: refund, replacement, repair, or charge reversal.
        4. Attach evidence for {topic["signals"][2]} and use {topic["signals"][3]} as the next deadline.

        ## Source Notes

        {source_notes(topic, "en")}

        ## Related Reading

        {related_links(index, "en")}
        """
    )


def write_post(topic: dict[str, object], index: int, lang: str) -> None:
    slug = topic["slug"]
    body = ko_body(topic, index) if lang == "ko" else en_body(topic, index)
    post_dir = ROOT / "_posts" / lang
    post_dir.mkdir(parents=True, exist_ok=True)
    (post_dir / f"{POST_DATE}-{slug}.md").write_text(front_matter(topic, lang, index) + "\n" + body, encoding="utf-8")


def write_category_pages() -> None:
    pages = {
        "ko": {
            "path": ROOT / "_pages" / "category-ko_Consumer_Rights.md",
            "permalink": "/ko_consumer_rights/",
            "title": "Consumer Rights",
            "seo": "환불, 구독해지, 차지백, 리콜, 항공권, 통신요금, 가짜리뷰, 다크패턴, 해외직구 분쟁을 공식 자료 기반으로 정리한 소비자 권리 가이드입니다.",
            "body": """
Consumer Rights 카테고리는 소비자 분쟁을 감정적인 항의가 아니라 **영수증, 약관, 날짜, 증거, 단계적 민원**으로 풀어 가기 위한 실전 가이드 모음입니다.

각 글은 FTC, CFPB, FCC, DOT, CPSC, FDA, NHTSA, econsumer.gov, Korea Consumer Agency, Korea Fair Trade Commission 같은 공식 자료를 우선 참고합니다. 목적은 법률 자문이 아니라, 환불·구독해지·배송지연·차지백·리콜·통신요금·여행 예약 분쟁에서 어떤 자료를 먼저 남겨야 하는지 정리하는 것입니다.

처음 읽는다면 무료체험 자동결제, 온라인 주문 미배송, 신용카드 이의제기 글부터 시작하세요. 그다음 리콜, 항공편 환불, 통신요금, 해외직구 글로 확장하면 소비자 문제를 더 빠르게 구조화할 수 있습니다.

## 먼저 읽기

- [무료체험과 자동결제 해지](/ko_consumer_rights/subscription-cancel-free-trial/)
- [온라인 주문이 오지 않을 때](/ko_consumer_rights/online-order-never-arrived/)
- [신용카드 결제 이의제기](/ko_consumer_rights/credit-card-charge-dispute/)

## 최신 글

{% assign posts = site.categories["ko_Consumer_Rights"] %}
{% for post in posts %}
  {% include archive-single.html type=page.entries_layout %}
{% endfor %}
""",
        },
        "en": {
            "path": ROOT / "_pages" / "category-en_Consumer_Rights.md",
            "permalink": "/en_consumer_rights/",
            "title": "Consumer Rights",
            "seo": "Official-source consumer rights guides for refunds, subscriptions, chargebacks, recalls, flights, telecom bills, fake reviews, dark patterns, and cross-border shopping disputes.",
            "body": """
The Consumer Rights category helps readers handle everyday disputes through **receipts, terms, dates, evidence, and step-by-step escalation** instead of scattered messages.

The articles prioritize official sources such as the FTC, CFPB, FCC, DOT, CPSC, FDA, NHTSA, econsumer.gov, Korea Consumer Agency, and Korea Fair Trade Commission. They are not legal advice. They give readers a practical workflow for refunds, subscriptions, delivery delays, chargebacks, recalls, telecom bills, travel booking disputes, and cross-border shopping problems.

Start with free-trial cancellation, online non-delivery, and credit-card disputes. Then move into product recalls, airline refunds, telecom billing, and marketplace or cross-border disputes.

## Start Here

- [Free Trial and Auto-Renewal Cancellation](/en_consumer_rights/subscription-cancel-free-trial/)
- [Online Order Never Arrived](/en_consumer_rights/online-order-never-arrived/)
- [Credit Card Charge Dispute](/en_consumer_rights/credit-card-charge-dispute/)

## Latest Articles

{% assign posts = site.categories["en_Consumer_Rights"] %}
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
    print(f"Generated {len(TOPICS)} paired Consumer Rights topics.")


if __name__ == "__main__":
    main()
