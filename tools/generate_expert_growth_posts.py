#!/usr/bin/env python3
"""Generate paired expert growth posts across the main non-troubleshooting fields."""

from __future__ import annotations

import html
import re
from datetime import date, timedelta
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parents[1]
START_DATE = date(2026, 5, 24)
LAST_MODIFIED_AT = "2026-05-24T23:40:00+09:00"


SOURCES = {
    "ai": [
        ("OpenAI Agents Guide", "https://platform.openai.com/docs/guides/agents"),
        ("OpenAI Structured Outputs Guide", "https://platform.openai.com/docs/guides/structured-outputs"),
        ("NIST AI Risk Management Framework", "https://www.nist.gov/itl/ai-risk-management-framework"),
        ("OWASP Top 10 for LLM Applications", "https://owasp.org/www-project-top-10-for-large-language-model-applications/"),
    ],
    "global": [
        ("IMF World Economic Outlook", "https://www.imf.org/en/Publications/WEO"),
        ("World Bank Global Economic Prospects", "https://www.worldbank.org/en/publication/global-economic-prospects"),
        ("WTO Global Trade Outlook and Statistics", "https://www.wto.org/english/res_e/publications_e/trade_outlook25_e.htm"),
        ("UNCTAD Review of Maritime Transport", "https://unctad.org/RMT"),
    ],
    "climate": [
        ("IEA World Energy Outlook", "https://www.iea.org/reports/world-energy-outlook-2025"),
        ("IEA Electricity", "https://www.iea.org/reports/electricity-2026"),
        ("IPCC AR6 Synthesis Report", "https://www.ipcc.ch/report/sixth-assessment-report-cycle/"),
        ("Korea Energy Statistical Information System", "https://kesis.keei.re.kr/eng"),
    ],
    "consumer": [
        ("FTC Consumer Advice", "https://consumer.ftc.gov/"),
        ("CFPB Consumer Complaints", "https://www.consumerfinance.gov/complaint/"),
        ("Korea Consumer Agency", "https://www.kca.go.kr/eng/index.do"),
        ("econsumer.gov Cross-Border Complaints", "https://www.econsumer.gov/"),
    ],
    "security": [
        ("CISA Secure Our World", "https://www.cisa.gov/secure-our-world"),
        ("CISA StopRansomware Guide", "https://www.cisa.gov/stopransomware/ransomware-guide"),
        ("NIST Digital Identity Guidelines", "https://pages.nist.gov/800-63-4/"),
        ("KISA BohoNara", "https://www.boho.or.kr/"),
    ],
    "finance": [
        ("CFPB Consumer Tools", "https://www.consumerfinance.gov/consumer-tools/"),
        ("SEC Investor.gov", "https://www.investor.gov/"),
        ("FINRA Investor Insights", "https://www.finra.org/investors/insights"),
        ("Korea Financial Supervisory Service", "https://www.fss.or.kr/eng/main/main.do"),
    ],
    "health": [
        ("CDC Health Topics", "https://www.cdc.gov/health-topics.html"),
        ("NIH MedlinePlus", "https://medlineplus.gov/"),
        ("WHO Health Topics", "https://www.who.int/health-topics"),
        ("FDA Consumer Updates", "https://www.fda.gov/consumers/consumer-updates"),
    ],
    "study": [
        ("IES What Works Clearinghouse Practice Guides", "https://ies.ed.gov/ncee/wwc/PracticeGuides"),
        ("Education Endowment Foundation", "https://educationendowmentfoundation.org.uk/education-evidence"),
        ("Cornell Learning Strategies Center", "https://lsc.cornell.edu/"),
        ("Purdue OWL", "https://owl.purdue.edu/"),
    ],
    "economy": [
        ("IMF Data and Reports", "https://www.imf.org/en/Data"),
        ("World Bank Data", "https://data.worldbank.org/"),
        ("OECD Economic Outlook", "https://www.oecd.org/en/topics/economic-outlook.html"),
        ("Bank of Korea ECOS", "https://ecos.bok.or.kr/"),
    ],
    "labeling": [
        ("Easy Labeling GitHub Repository", "https://github.com/MouseBall54/easy_labeling"),
        ("Ultralytics Object Detection Dataset Docs", "https://docs.ultralytics.com/datasets/detect/"),
        ("CVAT Dataset Formats", "https://docs.cvat.ai/docs/dataset_management/formats/"),
        ("MDN File System API", "https://developer.mozilla.org/en-US/docs/Web/API/File_System_API"),
    ],
}


FIELDS = {
    "ai": {
        "ko_category": "ko_AI_Trends",
        "en_category": "en_AI_Trends",
        "ko_path": "ko_ai_trends",
        "en_path": "en_ai_trends",
        "tags": ["AI", "Governance", "Workflow", "Evaluation"],
        "ko_related": [
            ("AI Agent Workflow 2026", "/ko_ai_trends/ai-agent-workflow-2026/"),
            ("NIST AI RMF 팀 체크리스트", "/ko_ai_trends/nist-ai-rmf-team-checklist/"),
        ],
        "en_related": [
            ("AI Agent Workflow 2026", "/en_ai_trends/ai-agent-workflow-2026/"),
            ("NIST AI RMF Team Checklist", "/en_ai_trends/nist-ai-rmf-team-checklist/"),
        ],
        "ko_intro": "AI 도입에서 조회수를 끄는 글은 새 모델 이름을 나열하는 글이 아니라 실제 팀이 실패하는 지점을 먼저 잡아 주는 글입니다.",
        "en_intro": "Useful AI trend content is not a list of model names. It should explain where real teams fail and how to verify the workflow.",
        "ko_disclaimer": "이 글은 특정 모델이나 벤더를 추천하지 않고, 검증 가능한 운영 기준을 세우기 위한 교육용 안내입니다.",
        "en_disclaimer": "This is an educational workflow guide, not a recommendation for a specific model or vendor.",
    },
    "global": {
        "ko_category": "ko_Global_Affairs",
        "en_category": "en_Global_Affairs",
        "ko_path": "ko_global_affairs",
        "en_path": "en_global_affairs",
        "tags": ["Geopolitics", "Trade", "Korea", "Risk"],
        "ko_related": [
            ("세계정세 읽기 시스템", "/ko_global_affairs/global-affairs-reading-system/"),
            ("한국 수출과 글로벌 분절화", "/ko_global_affairs/korea-export-exposure-global-fragmentation/"),
        ],
        "en_related": [
            ("Global Affairs Reading System", "/en_global_affairs/global-affairs-reading-system/"),
            ("Korea Export Exposure to Global Fragmentation", "/en_global_affairs/korea-export-exposure-global-fragmentation/"),
        ],
        "ko_intro": "세계정세 글은 사건 해설에서 멈추면 약합니다. 한국의 수출, 수입물가, 에너지, 금융 여건으로 이어지는 경로를 보여 줘야 검색 독자가 오래 머뭅니다.",
        "en_intro": "Global affairs content becomes stronger when it connects events to exports, import prices, energy, finance, and Korea-facing risk channels.",
        "ko_disclaimer": "이 글은 국제정세를 이해하기 위한 교육용 해설이며 정책, 투자, 법률 조언이 아닙니다.",
        "en_disclaimer": "This is educational analysis, not policy, investment, or legal advice.",
    },
    "climate": {
        "ko_category": "ko_Climate_Energy",
        "en_category": "en_Climate_Energy",
        "ko_path": "ko_climate_energy",
        "en_path": "en_climate_energy",
        "tags": ["Energy", "Climate", "Grid", "Korea"],
        "ko_related": [
            ("에너지 전환의 병목은 전력망이다", "/ko_climate_energy/power-grid-bottlenecks-transition/"),
            ("AI 데이터센터 전력 수요", "/ko_climate_energy/ai-data-center-electricity-demand/"),
        ],
        "en_related": [
            ("The Energy Transition Bottleneck Is the Grid", "/en_climate_energy/power-grid-bottlenecks-transition/"),
            ("AI Data-Center Electricity Demand", "/en_climate_energy/ai-data-center-electricity-demand/"),
        ],
        "ko_intro": "기후·에너지 주제는 선언보다 비용, 전력망, 산업경쟁력, 가계요금으로 연결해야 실무 독자에게 가치가 생깁니다.",
        "en_intro": "Climate and energy posts earn attention when targets are connected to costs, grids, industrial competitiveness, and household bills.",
        "ko_disclaimer": "이 글은 교육용 에너지 브리핑이며 투자 조언이나 특정 기술 홍보가 아닙니다.",
        "en_disclaimer": "This is an educational energy briefing, not investment advice or technology promotion.",
    },
    "consumer": {
        "ko_category": "ko_Consumer_Rights",
        "en_category": "en_Consumer_Rights",
        "ko_path": "ko_consumer_rights",
        "en_path": "en_consumer_rights",
        "tags": ["ConsumerRights", "Refunds", "Evidence", "Disputes"],
        "ko_related": [
            ("온라인 주문이 오지 않을 때", "/ko_consumer_rights/online-order-never-arrived/"),
            ("반품과 환불 증거 폴더", "/ko_consumer_rights/return-refund-evidence-folder/"),
        ],
        "en_related": [
            ("Online Order Never Arrived", "/en_consumer_rights/online-order-never-arrived/"),
            ("Return and Refund Evidence Folder", "/en_consumer_rights/return-refund-evidence-folder/"),
        ],
        "ko_intro": "소비자 권리 글은 법 조항 나열보다 날짜, 계약 문구, 증거, 판매자와 결제수단의 책임 구분을 알려 줄 때 검색 가치가 큽니다.",
        "en_intro": "Consumer-rights content performs when it turns a frustrating dispute into dates, contract language, evidence, and escalation order.",
        "ko_disclaimer": "이 글은 소비자 분쟁 대응을 돕는 교육용 정보이며 법률 조언이 아닙니다.",
        "en_disclaimer": "This is educational consumer information, not legal advice.",
    },
    "security": {
        "ko_category": "ko_Digital_Security",
        "en_category": "en_Digital_Security",
        "ko_path": "ko_digital_security",
        "en_path": "en_digital_security",
        "tags": ["Cybersecurity", "AccountSecurity", "Scams", "Recovery"],
        "ko_related": [
            ("피싱 문자와 이메일 30초 판별법", "/ko_digital_security/phishing-message-triage/"),
            ("랜섬웨어 첫 1시간 대응", "/ko_digital_security/ransomware-first-hour/"),
        ],
        "en_related": [
            ("A 30-Second Phishing Triage", "/en_digital_security/phishing-message-triage/"),
            ("Ransomware First Hour", "/en_digital_security/ransomware-first-hour/"),
        ],
        "ko_intro": "디지털 보안 글은 공포를 키우는 대신 빠른 확인, 신고, 복구 루틴을 제시해야 실제 피해를 줄입니다.",
        "en_intro": "Digital security content should reduce harm with verification, reporting, and recovery routines rather than fear.",
        "ko_disclaimer": "보안 사고가 의심되면 계정 차단, 금융기관 신고, 공식 기관 안내 확인을 지체하지 마세요.",
        "en_disclaimer": "If an incident is suspected, act quickly: lock accounts, contact financial providers, and check official reporting guidance.",
    },
    "finance": {
        "ko_category": "ko_Personal_Finance",
        "en_category": "en_Personal_Finance",
        "ko_path": "ko_personal_finance",
        "en_path": "en_personal_finance",
        "tags": ["PersonalFinance", "Budgeting", "Risk", "Planning"],
        "ko_related": [
            ("월별 돈 대시보드", "/ko_personal_finance/monthly-money-dashboard/"),
            ("투자 사기 경고 신호", "/ko_personal_finance/investment-scam-red-flags/"),
        ],
        "en_related": [
            ("Monthly Money Dashboard", "/en_personal_finance/monthly-money-dashboard/"),
            ("Investment Scam Red Flags", "/en_personal_finance/investment-scam-red-flags/"),
        ],
        "ko_intro": "개인금융 글은 수익률 예측보다 현금흐름, 수수료, 부채, 세금, 리스크 허용 범위를 스스로 확인하게 만드는 글이 오래갑니다.",
        "en_intro": "Personal finance content lasts when it helps readers verify cash flow, fees, debt, taxes, and risk tolerance rather than predict returns.",
        "ko_disclaimer": "이 글은 교육용 정보이며 개인별 투자, 세금, 대출, 법률 조언이 아닙니다.",
        "en_disclaimer": "This is educational information, not individualized investment, tax, lending, or legal advice.",
    },
    "health": {
        "ko_category": "ko_Health_Literacy",
        "en_category": "en_Health_Literacy",
        "ko_path": "ko_health_literacy",
        "en_path": "en_health_literacy",
        "tags": ["HealthLiteracy", "Prevention", "Safety", "Routine"],
        "ko_related": [
            ("병원 방문 질문 목록", "/ko_health_literacy/doctor-visit-question-list/"),
            ("응급 계획과 기본 응급처치", "/ko_health_literacy/first-aid-emergency-plan/"),
        ],
        "en_related": [
            ("Doctor Visit Question List", "/en_health_literacy/doctor-visit-question-list/"),
            ("First Aid Emergency Plan", "/en_health_literacy/first-aid-emergency-plan/"),
        ],
        "ko_intro": "건강 문해력 글은 진단을 대신하지 않고 독자가 증상, 날짜, 생활기록, 질문을 정리해 의료진과 더 잘 대화하게 도와야 합니다.",
        "en_intro": "Health-literacy content should not diagnose. It should help readers organize symptoms, dates, routines, and questions for professionals.",
        "ko_disclaimer": "이 글은 진단, 치료, 복용량 안내가 아닙니다. 갑작스럽거나 심한 증상, 호흡곤란, 흉통, 의식 저하, 자해 위험은 즉시 응급서비스나 의료진에게 연락하세요.",
        "en_disclaimer": "This is not diagnosis, treatment, or dosage guidance. For sudden, severe, or safety-critical symptoms, contact emergency services or a qualified clinician.",
    },
    "study": {
        "ko_category": "ko_Study",
        "en_category": "en_Study",
        "ko_path": "ko_study",
        "en_path": "en_study",
        "tags": ["StudySkills", "Learning", "Retrieval", "Planning"],
        "ko_related": [
            ("Active Recall 공부법", "/ko_study/active-recall-study-method/"),
            ("Spaced Repetition 복습 일정", "/ko_study/spaced-repetition-schedule/"),
        ],
        "en_related": [
            ("Active Recall Study Method", "/en_study/active-recall-study-method/"),
            ("Spaced Repetition Schedule", "/en_study/spaced-repetition-schedule/"),
        ],
        "ko_intro": "공부 글은 동기부여 문장이 아니라 실제 산출물, 회상 질문, 오답, 복습 간격을 바꾸는 루틴이어야 검색 독자에게 남습니다.",
        "en_intro": "Study content should change the reader's routine: outputs, retrieval prompts, mistakes, and review intervals.",
        "ko_disclaimer": "이 글은 학습 루틴을 설계하기 위한 교육용 안내이며, 개인의 학교·시험 제도에 맞게 조정해야 합니다.",
        "en_disclaimer": "This is educational guidance for study routines and should be adjusted to the learner's course and exam context.",
    },
    "economy": {
        "ko_category": "ko_Economy",
        "en_category": "en_Economy",
        "ko_path": "ko_economy",
        "en_path": "en_economy",
        "tags": ["Economy", "Inflation", "Households", "Indicators"],
        "ko_related": [
            ("경제 캘린더를 가계 관점에서 읽기", "/ko_economy/economic-calendar-for-households/"),
            ("물가 기대 읽는 법", "/ko_economy/inflation-expectations-guide/"),
        ],
        "en_related": [
            ("Economic Calendar for Households", "/en_economy/economic-calendar-for-households/"),
            ("Inflation Expectations Guide", "/en_economy/inflation-expectations-guide/"),
        ],
        "ko_intro": "경제 글은 지표 이름을 설명하는 데서 끝나지 않고 가계의 가격, 임금, 이자, 환율, 저축 압력으로 번역해야 조회 가치가 생깁니다.",
        "en_intro": "Economy posts become useful when indicators are translated into prices, wages, interest payments, exchange rates, savings, and household pressure.",
        "ko_disclaimer": "이 글은 경제 지표를 이해하기 위한 교육용 설명이며 투자, 세금, 대출, 법률 조언이 아닙니다.",
        "en_disclaimer": "This is educational economic information, not investment, tax, lending, legal, or personal financial advice.",
    },
    "labeling": {
        "ko_category": "ko_easy_labeling",
        "en_category": "en_easy_labeling",
        "ko_path": "ko_easy_labeling",
        "en_path": "en_easy_labeling",
        "tags": ["EasyLabeling", "YOLO", "Dataset", "Annotation"],
        "ko_related": [
            ("Easy Labeling으로 YOLO 데이터셋 만들기", "/ko_easy_labeling/easy-labeling-yolo-dataset/"),
            ("Segmentation과 Detection 라벨 선택", "/ko_easy_labeling/segmentation-vs-detection-labels/"),
        ],
        "en_related": [
            ("Build a YOLO Dataset with Easy Labeling", "/en_easy_labeling/easy-labeling-yolo-dataset/"),
            ("Segmentation vs Detection Labels", "/en_easy_labeling/segmentation-vs-detection-labels/"),
        ],
        "ko_intro": "Easy Labeling 글은 도구 홍보가 아니라 Detection, Segmentation, 클래스 파일, 로컬 저장, 검수 샘플링을 학습 데이터 품질과 연결해야 합니다.",
        "en_intro": "Easy Labeling posts should connect Detection, Segmentation, class files, local saves, and review sampling to dataset quality.",
        "ko_disclaimer": "Easy Labeling 실행 링크: [https://mouseball54.github.io/easy_labeling/](https://mouseball54.github.io/easy_labeling/).",
        "en_disclaimer": "Launch Easy Labeling: [https://mouseball54.github.io/easy_labeling/](https://mouseball54.github.io/easy_labeling/).",
    },
}


TOPICS = {
    "ai": [
        ("agent-eval-harness", "AI Agent Eval Harness: 자동 실행 전 실패 사례를 모으는 법", "AI Agent Eval Harness: Collect Failure Cases Before Automation", "eval set", "tool trace"),
        ("tool-permission-design", "AI Tool Permission 설계: 읽기, 초안, 실행 권한을 나누기", "AI Tool Permission Design: Split Read, Draft, and Execute", "permission tier", "approval gate"),
        ("rag-observability", "RAG Observability: 검색 로그와 답변 근거를 함께 남기기", "RAG Observability: Log Retrieval and Answer Evidence Together", "retrieval log", "citation span"),
        ("multimodal-qa-checklist", "Multimodal AI QA 체크리스트: 이미지와 텍스트 오류를 따로 보기", "Multimodal AI QA Checklist: Separate Image and Text Failures", "input modality", "review sample"),
        ("prompt-injection-incident-response", "Prompt Injection 사고 대응: 차단보다 기록과 복구 절차", "Prompt Injection Incident Response: Records and Recovery Before Blocking", "attack path", "rollback"),
        ("synthetic-data-risk-register", "Synthetic Data Risk Register: 합성데이터가 편향을 숨기지 않게 하기", "Synthetic Data Risk Register: Stop Synthetic Data from Hiding Bias", "data lineage", "bias check"),
        ("ai-cost-ledger", "AI Cost Ledger: 토큰 비용보다 재시도와 검토 시간을 기록하기", "AI Cost Ledger: Track Retries and Review Time, Not Only Tokens", "retry rate", "review cost"),
        ("model-routing-fallback", "Model Routing과 Fallback: 저렴한 모델과 고품질 모델을 나누는 기준", "Model Routing and Fallback: When to Use Cheap or Strong Models", "routing rule", "quality floor"),
        ("structured-output-contract", "Structured Output Contract: JSON Schema를 제품 계약으로 쓰기", "Structured Output Contract: Treat JSON Schema as a Product Contract", "schema field", "validation error"),
        ("ai-procurement-scorecard", "AI Procurement Scorecard: 벤더 데모보다 운영 책임을 묻기", "AI Procurement Scorecard: Ask About Operations Before Vendor Demos", "vendor control", "data boundary"),
        ("private-data-redaction-workflow", "Private Data Redaction Workflow: AI 입력 전에 지울 것과 남길 것", "Private Data Redaction Workflow: What to Remove Before AI Input", "PII field", "retention rule"),
        ("eval-dataset-versioning", "Eval Dataset Versioning: 모델 비교 전에 평가세트를 고정하기", "Eval Dataset Versioning: Freeze Test Sets Before Comparing Models", "eval version", "benchmark drift"),
        ("human-review-queue-design", "Human Review Queue 설계: AI가 자신 없는 사례를 사람에게 넘기는 법", "Human Review Queue Design: Route Uncertain AI Cases to People", "confidence signal", "review SLA"),
        ("ai-accessibility-workflow", "AI Accessibility Workflow: 접근성 검수를 자동화할 때 놓치기 쉬운 것", "AI Accessibility Workflow: What Automation Misses", "alt text", "manual check"),
        ("coding-agent-ci-guardrails", "Coding Agent CI Guardrails: 테스트 없는 자동 수정을 막기", "Coding Agent CI Guardrails: Block Automated Changes Without Tests", "test gate", "diff scope"),
        ("voice-ai-consent-logging", "Voice AI Consent Logging: 녹음, 요약, 보관 기준을 먼저 정하기", "Voice AI Consent Logging: Define Recording, Summary, and Retention", "consent record", "retention period"),
        ("answer-engine-content-structure", "Answer Engine Content Structure: AI 검색이 인용하기 쉬운 문서 구조", "Answer Engine Content Structure: Make Pages Easier to Cite", "answer block", "source note"),
        ("agent-memory-governance", "Agent Memory Governance: 편리한 기억 기능의 삭제와 범위 관리", "Agent Memory Governance: Scope and Deletion for Persistent Context", "memory scope", "delete path"),
        ("ai-incident-postmortem", "AI Incident Postmortem: 환각, 도구오류, 권한오류를 분리해 기록하기", "AI Incident Postmortem: Separate Hallucination, Tool, and Permission Failures", "failure type", "owner"),
        ("ai-workflow-slo", "AI Workflow SLO: 정확도만이 아니라 지연, 비용, 검토율을 목표로 잡기", "AI Workflow SLO: Set Targets for Latency, Cost, and Review Rate", "latency target", "review rate"),
    ],
    "global": [
        ("chip-export-control-map", "반도체 수출통제 지도: 장비, 소재, 고객국을 함께 보기", "Semiconductor Export Control Map: Tools, Materials, and Buyer Countries", "export license", "customer exposure"),
        ("red-sea-insurance-cost", "홍해 리스크와 해상보험료: 운임 뉴스가 가격으로 번지는 길", "Red Sea Risk and Marine Insurance: How Freight News Reaches Prices", "insurance premium", "rerouting"),
        ("dollar-liquidity-stress", "달러 유동성 스트레스: 환율 뉴스가 기업 자금조달로 이어지는 과정", "Dollar Liquidity Stress: From FX News to Corporate Funding", "dollar funding", "hedging cost"),
        ("critical-minerals-country-risk", "핵심광물 국가 리스크: 가격보다 정제 집중도를 먼저 보기", "Critical Minerals Country Risk: Refining Concentration Before Price", "refining share", "export control"),
        ("food-price-shock-map", "식량 가격 충격 지도: 곡물, 비료, 운송비를 한 번에 보기", "Food Price Shock Map: Grains, Fertilizer, and Freight Together", "grain price", "fertilizer cost"),
        ("defense-industrial-base", "방산 산업 기반 읽기: 국방비 증가가 공급망을 압박하는 방식", "Defense Industrial Base: How Spending Growth Strains Supply Chains", "order backlog", "industrial capacity"),
        ("migration-labor-market-channel", "이주와 노동시장: 세계정세가 임금과 돌봄 비용에 닿는 경로", "Migration and Labor Markets: How Global Affairs Reach Wages and Care Costs", "labor shortage", "visa policy"),
        ("arctic-shipping-route-risk", "북극 항로 리스크: 짧은 항로보다 보험, 인프라, 안보를 보기", "Arctic Shipping Route Risk: Insurance, Infrastructure, and Security Before Distance", "ice condition", "port capacity"),
        ("semiconductor-subsidy-competition", "반도체 보조금 경쟁: 공장 유치보다 전력과 인력 병목", "Semiconductor Subsidy Competition: Power and Talent Bottlenecks", "fab incentive", "power access"),
        ("sovereign-debt-restructuring", "국가부채 재조정 뉴스 읽기: 채권자, 통화, 만기 구조", "Sovereign Debt Restructuring: Creditors, Currency, and Maturity", "debt service", "creditor group"),
        ("election-disinformation-supply-chain", "선거 허위정보와 공급망: 정치 리스크가 기업 계획을 흔드는 법", "Election Disinformation and Supply Chains: Political Risk for Business Planning", "policy uncertainty", "trust signal"),
        ("cyber-infrastructure-diplomacy", "사이버 인프라 외교: 해저케이블과 클라우드 리전의 지정학", "Cyber Infrastructure Diplomacy: Subsea Cables and Cloud Regions", "subsea cable", "data route"),
        ("stablecoin-cross-border-risk", "스테이블코인과 국경간 결제: 편의보다 통화 주권 리스크", "Stablecoins and Cross-Border Payments: Convenience vs Monetary Risk", "reserve asset", "payment rail"),
        ("cross-border-data-rules", "국경간 데이터 규칙: AI와 클라우드 시대의 새 무역 장벽", "Cross-Border Data Rules: New Trade Friction for AI and Cloud", "data transfer", "localization"),
        ("taiwan-strait-scenario-korea", "대만해협 시나리오와 한국: 반도체, 해운, 금융시장 경로", "Taiwan Strait Scenarios and Korea: Chips, Shipping, and Markets", "chip supply", "shipping route"),
        ("wto-dispute-business-signal", "WTO 분쟁을 기업 신호로 읽는 법: 판정 전부터 봐야 할 것", "Reading WTO Disputes as Business Signals Before Rulings", "trade remedy", "policy signal"),
        ("middle-east-shipping-premium", "중동 긴장과 선박 프리미엄: 에너지와 소비재 가격의 연결", "Middle East Tension and Shipping Premiums: Energy and Consumer Goods", "shipping premium", "oil route"),
        ("ukraine-reconstruction-supply", "우크라이나 재건 수요: 건설, 에너지, 금융의 장기 파이프라인", "Ukraine Reconstruction Demand: Long Pipelines in Construction, Energy, and Finance", "reconstruction fund", "project pipeline"),
        ("climate-migration-city-risk", "기후 이주와 도시 리스크: 주택, 물, 노동시장 압력", "Climate Migration and City Risk: Housing, Water, and Labor Pressure", "displacement", "urban capacity"),
        ("korea-export-scenario-table", "한국 수출 시나리오 표: 미국, 중국, EU 수요를 나눠 보기", "Korea Export Scenario Table: Separate US, China, and EU Demand", "export order", "regional demand"),
    ],
    "climate": [
        ("grid-interconnection-queue", "전력망 접속 대기열: 재생에너지 프로젝트가 멈추는 지점", "Grid Interconnection Queues: Where Renewable Projects Stall", "connection queue", "grid capacity"),
        ("industrial-heat-electrification", "산업열 전기화: 공장 에너지 전환에서 가장 어려운 구간", "Industrial Heat Electrification: The Hard Part of Factory Decarbonization", "process heat", "electric boiler"),
        ("data-center-ppa-quality", "데이터센터 PPA 품질: 친환경 전력 주장 검증법", "Data-Center PPA Quality: How to Check Clean Power Claims", "additionality", "hourly match"),
        ("offshore-wind-vessel-bottleneck", "해상풍력 설치선 병목: 터빈보다 먼저 확인할 공급망", "Offshore Wind Vessel Bottlenecks: Supply Chains Before Turbines", "installation vessel", "port window"),
        ("battery-recycling-economics", "배터리 재활용 경제성: 광물 가격보다 회수율과 품질", "Battery Recycling Economics: Recovery Rate and Quality Before Metal Prices", "recovery rate", "black mass"),
        ("heat-pump-retrofit-plan", "히트펌프 리트로핏 계획: 건물 단열과 전기요금을 함께 보기", "Heat Pump Retrofit Plan: Insulation and Power Bills Together", "building envelope", "peak load"),
        ("lng-contract-optionality", "LNG 장기계약 옵션: 가격 안정과 유연성의 trade-off", "LNG Contract Optionality: Stability vs Flexibility", "contract term", "spot exposure"),
        ("solar-curtailment-dashboard", "태양광 출력제어 대시보드: 시간대, 지역, 수요를 같이 보기", "Solar Curtailment Dashboard: Time, Region, and Demand Together", "curtailment rate", "local demand"),
        ("green-hydrogen-offtake-risk", "그린수소 Offtake 리스크: 생산보다 구매 계약이 먼저다", "Green Hydrogen Offtake Risk: Buyers Before Production", "offtake contract", "delivered cost"),
        ("ev-charging-demand-response", "EV 충전 수요반응: 충전소가 전력망 자원이 되는 법", "EV Charging Demand Response: Turning Chargers into Grid Resources", "managed charging", "peak demand"),
        ("smr-project-reality-check", "SMR 프로젝트 현실 점검: 발표, 인허가, 비용, 계통 접속", "SMR Project Reality Check: Announcements, Permits, Cost, and Grid", "licensing", "project cost"),
        ("carbon-border-supplier-data", "탄소국경조정과 공급업체 데이터: 수출기업의 준비 순서", "Carbon Border Adjustment and Supplier Data: Preparation Order for Exporters", "embedded emissions", "supplier record"),
        ("scope3-data-room", "Scope 3 데이터룸: 협력사 배출량을 수집할 때 필요한 구조", "Scope 3 Data Room: Structure for Supplier Emissions Records", "supplier form", "audit trail"),
        ("port-climate-adaptation", "항만 기후적응: 해수면, 폭풍, 물류 지연을 비용으로 보기", "Port Climate Adaptation: Sea Level, Storms, and Logistics Delay", "port exposure", "downtime"),
        ("semiconductor-water-stress", "반도체 공장과 물 스트레스: 전력만큼 중요한 생산 리스크", "Semiconductor Fabs and Water Stress: Production Risk Beyond Power", "water withdrawal", "recycling rate"),
        ("critical-minerals-refining-korea", "핵심광물 정제 리스크와 한국 산업: 배터리 원가의 숨은 변수", "Critical Minerals Refining Risk and Korean Industry", "refining concentration", "battery cost"),
        ("capacity-payment-basics", "용량요금 기본 개념: 전기요금에 숨어 있는 신뢰도 비용", "Capacity Payments Basics: Reliability Costs Inside Power Bills", "capacity market", "reserve margin"),
        ("virtual-power-plant-practical", "Virtual Power Plant 실무 개념: 분산 자원이 전력시장에 들어오는 방식", "Virtual Power Plant Basics: How Distributed Resources Enter Power Markets", "aggregator", "flexibility"),
        ("apartment-energy-efficiency", "아파트 에너지 효율: 냉난방비를 줄이는 설비와 행동 점검표", "Apartment Energy Efficiency: Equipment and Behavior Checklist", "insulation", "meter data"),
        ("extreme-heat-peak-load", "폭염과 피크 전력: 냉방 수요가 전력망을 압박하는 순서", "Extreme Heat and Peak Load: How Cooling Demand Stresses the Grid", "cooling load", "peak reserve"),
    ],
    "consumer": [
        ("subscription-evidence-timeline", "구독 해지 증거 타임라인: 자동결제 분쟁을 줄이는 기록법", "Subscription Evidence Timeline: Records That Reduce Auto-Renewal Disputes", "renewal date", "confirmation email"),
        ("bnpl-refund-chain", "BNPL 환불 분쟁: 판매자, 플랫폼, 결제사가 나뉘는 지점", "BNPL Refund Chain: Seller, Platform, and Payment Provider Roles", "installment plan", "refund status"),
        ("airline-refund-rule-check", "항공권 환불 규칙 확인: 지연, 취소, 일정 변경을 나눠 보기", "Airline Refund Rule Check: Delay, Cancellation, and Schedule Change", "flight status", "refund rule"),
        ("hotel-resort-fee-proof", "호텔 리조트피 증거 확보: 총액 표시와 체크인 청구 비교", "Hotel Resort Fee Evidence: Compare Total Price and Check-In Charges", "advertised price", "fee disclosure"),
        ("marketplace-counterfeit-claim", "마켓플레이스 위조품 의심: 판매자 증거와 플랫폼 신고 순서", "Marketplace Counterfeit Claim: Seller Evidence and Platform Escalation", "seller identity", "product proof"),
        ("warranty-claim-escalation", "보증수리 거절 대응: 보증서 문구와 수리 내역 정리법", "Warranty Claim Escalation: Organize Warranty Terms and Repair Records", "warranty term", "repair log"),
        ("mobile-plan-price-change", "모바일 요금제 변경 통보: 약정, 고지, 해지권 확인 순서", "Mobile Plan Price Change: Contract, Notice, and Cancellation Rights", "contract term", "notice date"),
        ("broadband-label-comparison", "Broadband Label 비교법: 속도, 수수료, 데이터 제한을 한 표로 보기", "Broadband Label Comparison: Speed, Fees, and Data Limits in One Table", "monthly fee", "data cap"),
        ("used-car-contract-red-flags", "중고차 계약서 red flags: 구두 약속보다 문서가 중요한 이유", "Used Car Contract Red Flags: Documents Before Verbal Promises", "dealer fee", "vehicle history"),
        ("home-repair-change-order", "집수리 추가비용 분쟁: change order를 받기 전 확인할 것", "Home Repair Change Orders: What to Check Before Extra Charges", "scope change", "written approval"),
        ("gym-freeze-cancel-policy", "헬스장 휴회와 해지 정책: 자동결제 전 확인할 문구", "Gym Freeze and Cancellation Policy: Terms to Check Before Billing", "freeze period", "cancellation window"),
        ("dark-pattern-refund-flow", "Dark Pattern 환불 흐름: 해지 버튼을 숨기는 화면 기록법", "Dark Pattern Refund Flow: Document Screens That Hide Cancellation", "screen capture", "negative option"),
        ("fake-review-purchase-risk", "가짜 리뷰 판별: 별점보다 구매 위험을 줄이는 확인 순서", "Fake Review Triage: Reduce Purchase Risk Beyond Star Ratings", "review pattern", "seller history"),
        ("cross-border-return-cost", "해외직구 반품 비용: 관세, 배송비, 플랫폼 책임 확인", "Cross-Border Return Cost: Duties, Shipping, and Platform Responsibility", "return shipping", "customs duty"),
        ("children-app-privacy-check", "어린이 앱 개인정보 점검: 권한, 광고, 보호자 동의", "Children's App Privacy Check: Permissions, Ads, and Parental Consent", "app permission", "parent consent"),
        ("delivery-photo-proof", "배송 완료 사진 증거: 미수령 분쟁에서 확인할 위치와 시간", "Delivery Photo Proof: Location and Time in Non-Delivery Claims", "delivery photo", "address match"),
        ("rental-car-toll-fee", "렌터카 톨비와 추가요금: 반납 후 청구서를 검토하는 법", "Rental Car Toll and Add-On Fees: Review Charges After Return", "toll fee", "return receipt"),
        ("product-recall-household-log", "제품 리콜 가정 기록부: 모델명과 구매처를 남겨야 하는 이유", "Household Product Recall Log: Model Numbers and Purchase Sources", "model number", "recall notice"),
        ("travel-platform-refund-gap", "여행 플랫폼 환불 공백: 항공사와 플랫폼 책임을 나누기", "Travel Platform Refund Gap: Separate Airline and Platform Responsibility", "booking channel", "refund owner"),
        ("repair-estimate-consent-proof", "수리 견적 동의 증거: 승인 전후 금액이 달라질 때", "Repair Estimate Consent Proof: When Approved and Final Costs Differ", "estimate", "approval record"),
    ],
    "security": [
        ("passkey-rollout-plan", "패스키 전환 계획: 이메일 계정부터 피싱 저항성을 높이기", "Passkey Rollout Plan: Start With Email for Phishing Resistance", "passkey", "recovery device"),
        ("qr-quishing-response", "QR Quishing 대응: 카메라를 열기 전 확인할 세 가지", "QR Quishing Response: Three Checks Before Scanning", "QR code", "destination URL"),
        ("invoice-fraud-approval-chain", "송장 사기 승인 체계: 입금 계좌 변경 요청 검증법", "Invoice Fraud Approval Chain: Verify Bank Account Change Requests", "payment request", "callback"),
        ("cloud-sharing-audit", "클라우드 공유 링크 감사: 외부 공개 파일을 줄이는 루틴", "Cloud Sharing Audit: Reduce Public Links and External Files", "public link", "owner"),
        ("family-password-manager", "가족 비밀번호 관리자 운영: 공유 계정과 복구코드 정리", "Family Password Manager: Shared Accounts and Recovery Codes", "shared vault", "recovery code"),
        ("mfa-recovery-drill", "MFA 복구 훈련: 휴대폰 분실 전 예비 인증수단 만들기", "MFA Recovery Drill: Prepare Before Losing a Phone", "backup factor", "lockout"),
        ("ransomware-restore-test", "랜섬웨어 백업 복구 테스트: 백업이 있다는 말보다 복구 시간", "Ransomware Restore Test: Recovery Time Matters More Than Backup Claims", "restore test", "RTO"),
        ("home-router-hardening", "가정용 라우터 보안 강화: 기본 비밀번호와 펌웨어부터", "Home Router Hardening: Default Passwords and Firmware First", "router admin", "firmware"),
        ("browser-extension-review", "브라우저 확장 프로그램 검토: 권한이 과한 도구를 줄이기", "Browser Extension Review: Remove Over-Permissioned Tools", "extension permission", "publisher"),
        ("public-wifi-real-risk", "공공 Wi-Fi 실제 위험: VPN보다 먼저 확인할 접속 습관", "Public Wi-Fi Real Risk: Connection Habits Before VPN Claims", "network name", "HTTPS"),
        ("smart-home-network-separation", "스마트홈 기기 분리: IoT가 계정 보안으로 번지지 않게 하기", "Smart Home Network Separation: Keep IoT Away from Accounts", "IoT device", "guest network"),
        ("domain-dmarc-baseline", "도메인 이메일 위조 방지: SPF, DKIM, DMARC 기본선", "Domain Email Spoofing Baseline: SPF, DKIM, and DMARC", "DMARC policy", "spoofing"),
        ("phishing-training-metrics", "피싱 훈련 지표: 클릭률보다 신고율과 반복 실패 보기", "Phishing Training Metrics: Report Rate and Repeat Failures", "report rate", "repeat click"),
        ("identity-theft-document-kit", "신원도용 문서 키트: 신고 전 모아야 할 증거", "Identity Theft Document Kit: Evidence to Gather Before Reports", "fraud account", "report number"),
        ("child-device-privacy-setup", "자녀 기기 개인정보 설정: 위치, 결제, 앱 권한부터", "Child Device Privacy Setup: Location, Payments, and App Permissions", "parent control", "location access"),
        ("ai-phishing-script-risk", "AI 피싱 문장 리스크: 자연스러운 한국어 사기를 판별하는 법", "AI Phishing Script Risk: Detect More Natural Scam Messages", "message intent", "verification route"),
        ("marketplace-escrow-scam", "중고거래 안전결제 사기: 링크형 escrow를 확인하는 순서", "Marketplace Escrow Scam: Verify Link-Based Payment Requests", "escrow link", "seller pressure"),
        ("software-update-calendar", "소프트웨어 업데이트 캘린더: 미루지 않는 월간 보안 루틴", "Software Update Calendar: A Monthly Security Routine", "patch window", "device list"),
        ("travel-device-lockdown", "여행 전 기기 보안: 공항, 호텔, 임대차량에서 줄일 위험", "Travel Device Lockdown: Reduce Airport, Hotel, and Rental-Car Risk", "travel mode", "device lock"),
        ("account-takeover-first-signs", "계정 탈취 초기 신호: 로그인 알림과 복구 이메일을 읽는 법", "Early Signs of Account Takeover: Login Alerts and Recovery Emails", "login alert", "recovery email"),
    ],
    "finance": [
        ("emergency-fund-inflation", "인플레이션 시기 비상금: 금액보다 지출 개월 수로 보기", "Emergency Fund During Inflation: Think in Months of Expenses", "monthly expense", "cash buffer"),
        ("debt-avalanche-interest-map", "Debt Avalanche 이자 지도: 고금리 부채부터 줄이는 표", "Debt Avalanche Interest Map: Rank High-Rate Debt First", "APR", "minimum payment"),
        ("credit-report-freeze-plan", "신용보고서 동결 계획: 사기 피해 전 잠금 장치 만들기", "Credit Report Freeze Plan: Lock Before Fraud Happens", "credit freeze", "fraud alert"),
        ("retirement-contribution-check", "퇴직연금 납입 순서: 세제혜택보다 현금흐름 먼저", "Retirement Contribution Check: Cash Flow Before Tax Benefits", "contribution", "cash flow"),
        ("etf-expense-ratio-compounding", "ETF 비용률 복리 효과: 작은 수수료가 장기수익을 줄이는 방식", "ETF Expense Ratio Compounding: How Small Fees Reduce Long-Term Returns", "expense ratio", "holding period"),
        ("portfolio-rebalancing-calendar", "포트폴리오 리밸런싱 달력: 시장 예측보다 기준 비중", "Portfolio Rebalancing Calendar: Target Weights Before Market Calls", "target weight", "rebalance band"),
        ("tax-withholding-paycheck", "원천징수 점검: 월급이 늘어도 세금 환급이 줄 수 있는 이유", "Tax Withholding Check: Why Bigger Paychecks Can Change Refunds", "withholding", "refund"),
        ("freelancer-quarterly-tax-buckets", "프리랜서 분기 세금 버킷: 매출이 들어올 때 나눠 두기", "Freelancer Quarterly Tax Buckets: Separate Money When Revenue Arrives", "tax bucket", "quarterly estimate"),
        ("auto-loan-apr-total-cost", "자동차 대출 APR 총비용: 월 납입액보다 전체 이자", "Auto Loan APR Total Cost: Total Interest Before Monthly Payment", "APR", "loan term"),
        ("mortgage-stress-rate", "주택담보대출 스트레스 금리: 낮은 금리 광고보다 버틸 금리", "Mortgage Stress Rate: What Payment Can Survive Higher Rates", "stress rate", "debt service"),
        ("rent-buy-mobility-framework", "전월세 vs 매수 판단: 가격보다 이동성, 현금흐름, 리스크", "Rent vs Buy Framework: Mobility, Cash Flow, and Risk", "mobility", "ownership cost"),
        ("insurance-deductible-cash", "보험 자기부담금 현금 버퍼: 보험이 있어도 필요한 돈", "Insurance Deductible Cash Buffer: Money Needed Even With Coverage", "deductible", "emergency cash"),
        ("travel-fx-card-fees", "여행 환전과 카드 수수료: 환율보다 총 결제비용 보기", "Travel FX and Card Fees: Total Payment Cost Before Exchange Rate", "FX fee", "card spread"),
        ("sinking-fund-dashboard", "Sinking Fund 대시보드: 비정기 지출을 월별로 나누기", "Sinking Fund Dashboard: Spread Irregular Expenses Monthly", "irregular expense", "monthly set-aside"),
        ("subscription-audit-roi", "구독 감사 ROI: 해지보다 사용 빈도와 대체재 확인", "Subscription Audit ROI: Usage Frequency Before Cancellation", "monthly fee", "usage log"),
        ("investment-scam-verification", "투자 사기 검증 루틴: 수익률 약속보다 등록과 송금 경로", "Investment Scam Verification Routine: Registration and Payment Path", "guaranteed return", "registration"),
        ("target-date-fund-fit", "Target Date Fund 적합성: 은퇴연도보다 수수료와 주식 비중", "Target-Date Fund Fit: Fees and Stock Mix Before Retirement Year", "glide path", "expense"),
        ("student-loan-repayment-plan", "학자금 대출 상환 계획: 최저납입, 이자, 유예 조건 정리", "Student Loan Repayment Plan: Minimums, Interest, and Deferment Terms", "interest rate", "repayment option"),
        ("salary-raise-budget-reset", "연봉 인상 후 예산 리셋: 생활비 팽창을 막는 순서", "Budget Reset After a Raise: Prevent Lifestyle Creep", "raise", "savings rate"),
        ("couple-money-meeting-agenda", "커플 머니 미팅 아젠다: 싸우지 않고 숫자를 보는 순서", "Couple Money Meeting Agenda: Review Numbers Without Fighting", "shared goal", "spending rule"),
    ],
    "health": [
        ("sleep-debt-weekend-recovery", "수면부채와 주말 보충잠: 회복보다 루틴 안정이 먼저", "Sleep Debt and Weekend Recovery: Stabilize Routine First", "sleep schedule", "daytime sleepiness"),
        ("blood-pressure-home-log", "가정 혈압 기록법: 숫자 하나보다 측정 조건", "Home Blood Pressure Log: Conditions Before One Number", "measurement time", "cuff fit"),
        ("heat-illness-warning-plan", "온열질환 경고 계획: 폭염 전 물, 그늘, 휴식 기준", "Heat Illness Warning Plan: Water, Shade, and Rest Before Heat Waves", "heat index", "cooling plan"),
        ("food-safety-leftovers", "남은 음식 안전 루틴: 냉장 시간과 재가열 기준", "Leftover Food Safety Routine: Refrigeration Time and Reheating", "storage time", "temperature"),
        ("vaccination-record-family", "가족 예방접종 기록 정리: 기억보다 문서로 확인하기", "Family Vaccination Record: Verify With Documents", "record", "booster"),
        ("respiratory-virus-home-plan", "호흡기 바이러스 가정 계획: 증상, 격리, 환기 체크", "Respiratory Virus Home Plan: Symptoms, Isolation, and Ventilation", "symptom onset", "ventilation"),
        ("medicine-label-double-check", "일반의약품 라벨 두 번 읽기: 성분 중복을 피하는 법", "OTC Medicine Label Double Check: Avoid Duplicate Ingredients", "active ingredient", "warning"),
        ("mental-health-red-flag-list", "정신건강 red flags: 혼자 버티지 말아야 할 신호", "Mental Health Red Flags: When Not to Handle It Alone", "safety risk", "support contact"),
        ("headache-red-flag-diary", "두통 red flag와 기록: 갑작스러운 변화는 따로 표시", "Headache Red Flags and Diary: Mark Sudden Changes", "onset", "neurologic sign"),
        ("back-pain-activity-log", "허리통증 활동 기록: 쉬는 것과 움직임의 균형", "Back Pain Activity Log: Balance Rest and Movement", "pain trigger", "function"),
        ("oral-health-night-routine", "밤 양치 루틴: 치실, 불소, 간식 시간을 같이 보기", "Night Oral Health Routine: Floss, Fluoride, and Snack Timing", "brushing", "sugar exposure"),
        ("hearing-protection-decibel", "청력 보호와 dB: 이어폰 볼륨보다 노출 시간", "Hearing Protection and Decibels: Exposure Time Before Volume", "noise level", "duration"),
        ("hydration-urine-color-check", "수분 섭취 점검: 물 몇 잔보다 소변색과 활동량", "Hydration Check: Urine Color and Activity Before Cup Counts", "urine color", "heat exposure"),
        ("sodium-label-soup-noodles", "나트륨 라벨 읽기: 국물, 소스, 1회 제공량 함정", "Sodium Label Reading: Soups, Sauces, and Serving Size", "serving size", "sodium"),
        ("added-sugar-drink-swap", "가당음료 줄이기: 금지보다 대체 루틴 만들기", "Added Sugar Drink Swap: Build Replacement Routines", "sugar grams", "replacement"),
        ("strength-training-start-safe", "근력운동 시작 안전 루틴: 무게보다 자세와 회복", "Starting Strength Training Safely: Form and Recovery Before Load", "form", "recovery"),
        ("walking-program-baseline", "걷기 운동 시작 기준: 하루 만보보다 현재 수준", "Walking Program Baseline: Current Level Before 10,000 Steps", "baseline steps", "progression"),
        ("family-health-history-update", "가족력 업데이트: 병명보다 나이, 관계, 진단 시점", "Family Health History Update: Age, Relationship, and Diagnosis Timing", "relative", "age at diagnosis"),
        ("doctor-visit-one-page-brief", "진료 전 한 장 요약: 증상, 약, 질문을 정리하는 법", "One-Page Doctor Visit Brief: Symptoms, Medicines, and Questions", "symptom timeline", "medication list"),
        ("sun-safety-uv-index", "자외선 지수 읽기: 계절보다 시간대와 노출 부위", "UV Index Sun Safety: Time of Day and Exposed Skin", "UV index", "shade"),
    ],
    "study": [
        ("retrieval-practice-prompts", "Retrieval Practice 질문 만들기: 다시 읽기보다 꺼내 쓰기", "Retrieval Practice Prompts: Retrieve Instead of Rereading", "question prompt", "recall score"),
        ("spaced-review-calendar", "Spaced Review 달력: 복습을 미루지 않는 날짜 설계", "Spaced Review Calendar: Dates That Prevent Review Drift", "review interval", "due item"),
        ("interleaving-math-science", "Interleaving 수학·과학 연습: 유형을 섞어 판단력 키우기", "Interleaving Math and Science: Mix Types to Build Judgment", "problem type", "method choice"),
        ("mistake-log-feedback-loop", "오답 로그 피드백 루프: 틀린 이유를 다음 문제로 바꾸기", "Mistake Log Feedback Loop: Turn Errors Into Next Problems", "error cause", "retest"),
        ("coding-roadmap-projects", "코딩 로드맵 프로젝트형 학습: 문법을 산출물로 연결하기", "Coding Roadmap With Projects: Connect Syntax to Output", "small project", "debug log"),
        ("reading-notes-question-first", "질문 먼저 읽기 노트: 밑줄보다 답을 찾는 구조", "Question-First Reading Notes: Find Answers Before Highlighting", "reading question", "source note"),
        ("exam-day-energy-plan", "시험 당일 에너지 계획: 새 공부보다 수면과 동선", "Exam Day Energy Plan: Sleep and Logistics Before New Study", "sleep", "arrival plan"),
        ("flashcard-bad-card-fix", "나쁜 Flashcard 고치기: 너무 큰 카드와 애매한 답 줄이기", "Fix Bad Flashcards: Reduce Huge Cards and Vague Answers", "card prompt", "answer rule"),
        ("ai-tutor-verification-routine", "AI Tutor 안전 사용법: 설명을 믿기 전 검산 루틴", "AI Tutor Verification Routine: Check Before Trusting Explanations", "source check", "worked example"),
        ("writing-revision-pass", "글쓰기 revision pass: 문장 고치기 전에 주장 구조 보기", "Writing Revision Pass: Structure Before Sentences", "claim", "evidence"),
        ("research-citation-note", "Research Citation Note: 출처, 주장, 내 생각을 분리하기", "Research Citation Notes: Separate Source, Claim, and Your Thought", "citation", "paraphrase"),
        ("textbook-output-method", "교과서 Output Method: 읽은 장을 문제와 요약으로 바꾸기", "Textbook Output Method: Turn Chapters Into Questions and Summaries", "chapter question", "summary"),
        ("study-group-roles", "스터디그룹 역할 설계: 모임 시간을 문제풀이로 바꾸기", "Study Group Roles: Turn Meeting Time Into Practice", "role", "practice round"),
        ("math-problem-solve-template", "수학 문제풀이 템플릿: 풀이보다 조건과 전략 먼저", "Math Problem-Solving Template: Conditions and Strategy First", "condition", "strategy"),
        ("language-shadowing-feedback", "Language Shadowing 피드백: 따라 말하기를 녹음 검토로 연결", "Language Shadowing Feedback: Connect Speaking to Recording Review", "recording", "pronunciation target"),
        ("lecture-review-24h-system", "강의 24시간 리뷰 시스템: 필기 정리보다 회상 질문", "24-Hour Lecture Review System: Retrieval Before Notes Cleanup", "lecture question", "review time"),
        ("deep-work-distraction-audit", "Deep Work 방해요인 감사: 집중 시간보다 차단 규칙", "Deep Work Distraction Audit: Blocking Rules Before Focus Hours", "distraction", "block rule"),
        ("metacognition-scorecard", "Metacognition Scorecard: 아는 느낌과 실제 점수 분리", "Metacognition Scorecard: Separate Feeling From Performance", "confidence", "actual score"),
        ("semester-calendar-buffer", "학기 캘린더 버퍼: 마감일보다 시작일과 예비일", "Semester Calendar Buffer: Start Dates and Backup Days", "deadline", "buffer day"),
        ("sleep-study-boundary", "수면과 공부 경계선: 밤샘보다 다음 날 회상률", "Sleep and Study Boundary: Next-Day Recall Before All-Nighters", "sleep window", "recall rate"),
    ],
    "economy": [
        ("yield-curve-household-signal", "수익률곡선과 가계 신호: 경기 뉴스가 대출금리로 오는 길", "Yield Curve as Household Signal: From Macro News to Loan Rates", "yield curve", "loan rate"),
        ("cpi-pce-basket-difference", "CPI와 PCE 차이: 같은 물가라도 바구니가 다르다", "CPI vs PCE: Same Inflation Story, Different Basket", "price basket", "weight"),
        ("real-wage-paycheck-check", "실질임금 확인법: 명목 월급보다 구매력", "Real Wage Paycheck Check: Purchasing Power Before Nominal Pay", "nominal wage", "inflation"),
        ("household-debt-dsr-watch", "가계부채 DSR 보기: 금리보다 상환액이 먼저 흔들린다", "Household Debt DSR Watch: Payments Move Before Headlines", "debt service", "interest rate"),
        ("exchange-rate-import-price", "환율과 수입물가: 달러 뉴스가 장바구니로 번지는 경로", "Exchange Rate and Import Prices: How Dollar Moves Reach Baskets", "KRW/USD", "import price"),
        ("oil-import-inflation-lag", "유가와 수입 인플레이션 시차: 오늘 가격이 다음 달 비용으로", "Oil Prices and Import Inflation Lag: Today's Price, Later Costs", "oil price", "lag"),
        ("current-account-household", "경상수지를 가계 관점에서 읽기: 수출, 수입, 환율", "Current Account for Households: Exports, Imports, and FX", "current account", "trade balance"),
        ("fiscal-deficit-interest-burden", "재정적자와 이자부담: 정부 지출 뉴스의 장기 비용", "Fiscal Deficit and Interest Burden: Long-Term Cost of Spending", "deficit", "interest payment"),
        ("central-bank-meeting-template", "중앙은행 회의 읽기 템플릿: 결정, 문구, 전망 분리", "Central Bank Meeting Template: Decision, Language, and Outlook", "policy rate", "guidance"),
        ("productivity-wage-link", "생산성과 임금: 장기 구매력을 결정하는 느린 변수", "Productivity and Wages: Slow Variables Behind Purchasing Power", "productivity", "real wage"),
        ("labor-market-underemployment", "실업률 너머 노동시장: 불완전고용과 임금 압력", "Beyond Unemployment: Underemployment and Wage Pressure", "underemployment", "wage growth"),
        ("semiconductor-cycle-households", "반도체 사이클과 가계: 수출 호조가 임금·환율로 오는 길", "Semiconductor Cycle and Households: Exports, Wages, and FX", "chip exports", "manufacturing wage"),
        ("tariff-household-price-map", "관세가 가계물가로 오는 지도: 수입품, 중간재, 환율", "Tariff to Household Price Map: Imports, Inputs, and FX", "tariff", "consumer price"),
        ("dollar-liquidity-credit-cost", "달러 유동성과 신용비용: 해외 뉴스가 대출조건을 바꾸는 법", "Dollar Liquidity and Credit Cost: How Global News Changes Loan Conditions", "dollar funding", "credit spread"),
        ("housing-affordability-payment", "주거비 부담률: 집값보다 월 상환액과 소득", "Housing Affordability: Monthly Payment and Income Before Price", "payment", "income"),
        ("savings-real-rate", "저축 실질금리: 예금 이자에서 물가를 뺀 뒤 보기", "Real Savings Rate: Deposit Interest After Inflation", "deposit rate", "inflation"),
        ("inflation-expectation-household", "기대 인플레이션과 가계 결정: 가격이 오를 것이라는 믿음", "Inflation Expectations and Household Decisions", "expectation", "spending"),
        ("small-business-break-even", "소상공인 손익분기점: 임대료, 인건비, 재료비를 한 표로", "Small Business Break-Even: Rent, Labor, and Input Costs", "break-even", "fixed cost"),
        ("supply-chain-shock-table", "공급망 충격 표 만들기: 가격, 납기, 재고를 같이 보기", "Supply Chain Shock Table: Price, Lead Time, and Inventory", "lead time", "inventory"),
        ("gdp-components-household", "GDP 구성요소를 가계 언어로 읽기: 소비, 투자, 정부, 순수출", "GDP Components in Household Language: Consumption, Investment, Government, Net Exports", "GDP", "component"),
    ],
    "labeling": [
        ("instance-segmentation-mask-review", "Instance Segmentation 마스크 검수: 경계보다 클래스와 연결 영역", "Instance Segmentation Mask Review: Class and Connected Regions", "mask class", "connected region"),
        ("yolo-class-taxonomy-audit", "YOLO 클래스 taxonomy 감사: 이름, ID, 예외를 같이 잠그기", "YOLO Class Taxonomy Audit: Lock Names, IDs, and Exceptions", "class ID", "exception"),
        ("browser-folder-permission-labeling", "브라우저 폴더 권한 라벨링: File System Access API 작업 전 확인", "Browser Folder Permission Labeling: Checks Before File System Access", "folder permission", "local save"),
        ("dataset-drift-sampling", "Dataset Drift 샘플링: 새 배치가 기존 기준과 달라졌는지 보기", "Dataset Drift Sampling: Check Whether New Batches Changed", "drift sample", "batch source"),
        ("mask-box-cost-calculator", "Mask vs Box 비용 계산: Segmentation이 필요한 이미지 고르기", "Mask vs Box Cost Calculator: Choose Images That Need Segmentation", "annotation time", "precision need"),
        ("labeler-disagreement-resolution", "라벨러 의견 불일치 해결: 다수결보다 기준 업데이트", "Resolving Labeler Disagreement: Update Rules Before Voting", "disagreement", "rule update"),
        ("segmentation-region-class-change", "Segmentation 영역 클래스 변경: 마스크 검수에서 놓치기 쉬운 오류", "Segmentation Region Class Change: Common Mask Review Errors", "region class", "mask overlay"),
        ("yolo-empty-label-policy", "YOLO 빈 라벨 정책: negative image를 학습 신호로 남기는 법", "YOLO Empty Label Policy: Keep Negative Images as Training Signals", "empty label", "negative image"),
        ("annotation-time-benchmark", "Annotation Time Benchmark: 장당 시간으로 비용과 품질을 같이 보기", "Annotation Time Benchmark: Time per Image With Quality", "time per image", "review rate"),
        ("training-error-label-fix", "모델 학습 오류에서 라벨 수정으로 돌아가는 루프", "From Training Error Back to Label Fixes", "false positive", "label fix"),
        ("multi-class-visibility-review", "다중 클래스 가시성 검수: 클래스별 숨김으로 누락 찾기", "Multi-Class Visibility Review: Use Class Filters to Find Missing Labels", "class filter", "missing label"),
        ("windows-electron-local-labeling", "Windows Electron 로컬 라벨링: 브라우저 제한을 줄이는 선택지", "Windows Electron Local Labeling: Reducing Browser Limitations", "Electron", "local folder"),
        ("file-naming-contract", "파일명 계약: 이미지, 라벨, 마스크가 같은 객체를 가리키게 하기", "File Naming Contract: Keep Images, Labels, and Masks Aligned", "filename", "pairing"),
        ("small-object-min-size-rule", "Small Object 최소 크기 규칙: 라벨링할 물체와 버릴 물체 구분", "Small Object Minimum Size Rule: Label or Ignore", "min size", "small object"),
        ("bbox-alignment-batch-edit", "Bounding Box 정렬과 batch edit: 반복 객체 라벨링 속도 높이기", "Bounding Box Alignment and Batch Edit for Repeated Objects", "alignment", "batch edit"),
        ("brush-eraser-mask-protocol", "Brush/Eraser 마스크 프로토콜: Segmentation 작업 일관성 만들기", "Brush and Eraser Mask Protocol for Consistent Segmentation", "brush size", "eraser"),
        ("yolo-label-lint-check", "YOLO Label Lint Check: 학습 전 txt 파일 오류 찾기", "YOLO Label Lint Check: Find TXT Errors Before Training", "label lint", "coordinate range"),
        ("review-sampling-dashboard", "Review Sampling Dashboard: 라벨 검수를 숫자로 운영하기", "Review Sampling Dashboard: Operate Annotation QA With Numbers", "sample rate", "defect type"),
        ("active-learning-batch-priority", "Active Learning Batch Priority: 먼저 라벨링할 이미지 고르는 법", "Active Learning Batch Priority: Pick Images to Label First", "uncertainty", "priority"),
        ("dataset-license-handoff", "Dataset License Handoff: 이미지 권리와 라벨 파일을 같이 넘기기", "Dataset License Handoff: Transfer Image Rights With Labels", "license", "handoff"),
    ],
}


def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9-]+", "-", value.lower()).strip("-")


def yaml_list(items: list[str]) -> str:
    return "\n".join(f"  - {item}" for item in items)


def svg(path: Path, title: str, subtitle: str, labels: list[str], lang: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    colors = ["#1f7a8c", "#bf4342", "#4f772d", "#8d6a9f"]
    label_nodes = []
    for idx, label in enumerate(labels[:4]):
        x = 88 + idx * 260
        color = colors[idx % len(colors)]
        label_nodes.append(
            f'<rect x="{x}" y="390" width="210" height="92" rx="8" fill="{color}" opacity="0.92"/>'
            f'<text x="{x + 105}" y="440" text-anchor="middle" font-size="24" fill="#fff" font-family="Arial">{html.escape(label[:22])}</text>'
        )
    doc = f"""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630">
  <rect width="1200" height="630" fill="#f7f8f3"/>
  <rect x="56" y="54" width="1088" height="522" rx="18" fill="#ffffff" stroke="#263238" stroke-width="3"/>
  <text x="92" y="142" font-size="42" font-weight="700" fill="#263238" font-family="Arial">{html.escape(title[:54])}</text>
  <text x="92" y="200" font-size="27" fill="#455a64" font-family="Arial">{html.escape(subtitle[:76])}</text>
  <path d="M92 292 H1088" stroke="#d5dad6" stroke-width="4"/>
  <circle cx="180" cy="292" r="18" fill="#1f7a8c"/>
  <circle cx="452" cy="292" r="18" fill="#bf4342"/>
  <circle cx="724" cy="292" r="18" fill="#4f772d"/>
  <circle cx="996" cy="292" r="18" fill="#8d6a9f"/>
  {''.join(label_nodes)}
  <text x="92" y="548" font-size="22" fill="#607d8b" font-family="Arial">{'Korean and English paired guide' if lang == 'en' else '한국어/영어 페어 전문 가이드'}</text>
</svg>
"""
    path.write_text(doc, encoding="utf-8")


def source_notes(source_key: str, lang: str) -> str:
    heading = "## 참고할 자료" if lang == "ko" else "## Source Notes"
    lines = [heading, ""]
    for name, url in SOURCES[source_key]:
        lines.append(f"- [{name}]({url})")
    return "\n".join(lines)


def related(field: dict, lang: str) -> str:
    heading = "## 함께 보면 좋은 글" if lang == "ko" else "## Related Reading"
    links = field["ko_related" if lang == "ko" else "en_related"]
    return "\n".join([heading, "", *[f"- [{title}]({url})" for title, url in links]])


def normalize_body(text: str) -> str:
    lines = [re.sub(r"^ {8,12}", "", line) for line in text.splitlines()]
    return "\n".join(lines).strip() + "\n"


def front_matter(field: dict, topic: tuple[str, str, str, str, str], day: date, lang: str) -> str:
    slug, ko_title, en_title, _, _ = topic
    title = ko_title if lang == "ko" else en_title
    category = field["ko_category" if lang == "ko" else "en_category"]
    image_dir = f"/images/expert-growth-{slug}"
    description = (
        f"{title} 주제의 핵심 검증 흐름과 실무 체크포인트를 요약한 이미지입니다."
        if lang == "ko"
        else f"Visual summary of the verification flow and practical checkpoints for {title}."
    )
    excerpt = (
        f"{title}를 검색 독자가 바로 적용할 수 있도록 기준, 기록, 검증 순서로 정리합니다."
        if lang == "ko"
        else f"{title} organized into standards, records, and verification steps readers can apply."
    )
    return f"""---
layout: single
title: >
  {title}
seo_title: >
  {title[:68]}
date: {day.isoformat()}T09:00:00+09:00
last_modified_at: {LAST_MODIFIED_AT}
lang: {lang}
translation_id: expert-growth-{slug}
header:
  teaser: {image_dir}/hero.svg
  overlay_image: {image_dir}/hero.svg
  overlay_filter: 0.34
  image_description: >
    {description[:170]}
excerpt: >
  {excerpt}
seo_description: >
  {excerpt}
categories:
  - {category}
tags:
{yaml_list(field["tags"])}
---
"""


def body(field_key: str, field: dict, topic: tuple[str, str, str, str, str], lang: str) -> str:
    slug, ko_title, en_title, signal_a, signal_b = topic
    title = ko_title if lang == "ko" else en_title
    hero = f"/images/expert-growth-{slug}/hero.svg"
    checklist = f"/images/expert-growth-{slug}/checklist.svg"
    if lang == "ko":
        return normalize_body(
            dedent(
            f"""\
            {field["ko_intro"]}

            이 글은 **{title}**를 조회수를 위한 자극적인 제목이 아니라, 독자가 실제로 저장하고 다시 볼 수 있는 전문 체크리스트로 정리합니다. 핵심은 `{signal_a}`와 `{signal_b}`를 같은 표에서 관리하고, 판단을 미루는 조건과 바로 행동할 조건을 분리하는 것입니다.

            {field["ko_disclaimer"]}

            ![{title} 핵심 흐름도]({hero})

            ## 검색 의도와 독자 문제

            이 주제를 검색하는 독자는 보통 정의만 찾는 것이 아닙니다. 이미 문제를 겪고 있거나, 팀 회의·가계 결정·프로젝트 검수·리스크 점검에 쓸 기준을 찾고 있습니다. 그래서 이 글은 세 가지 질문에 답합니다.

            - 지금 무엇을 먼저 확인해야 하는가?
            - 어떤 기록을 남겨야 나중에 설명할 수 있는가?
            - 공식 출처와 내부 판단을 어떻게 나눠야 하는가?

            ## 먼저 볼 기준

            - **핵심 신호**: `{signal_a}`를 단독 숫자로 보지 말고 날짜, 출처, 책임자와 함께 둡니다.
            - **보조 신호**: `{signal_b}`가 바뀌면 기존 결론을 다시 봐야 하는지 표시합니다.
            - **증거 수준**: 공식 문서, 기관 자료, 내부 로그, 개인 추정을 구분합니다.
            - **업데이트 조건**: 새 규정, 새 데이터, 사고 사례, 비용 변화가 나오면 글이나 지침을 갱신합니다.

            ![{title} 실무 체크리스트]({checklist})

            ## 실무 적용 순서

            1. 현재 상태를 한 문장으로 적습니다. 예를 들어 “우리는 `{signal_a}` 때문에 의사결정이 늦어지고 있다”처럼 문제를 좁힙니다.
            2. 공식 출처에서 확인할 항목과 내부에서만 확인할 항목을 나눕니다.
            3. 검토 표에는 날짜, 출처 링크, 판단 근거, 다음 행동을 반드시 넣습니다.
            4. 이해관계자가 많은 주제라면 결론보다 먼저 가정과 제외 범위를 공유합니다.
            5. 2주 뒤 다시 볼 항목을 남겨 글이 일회성 요약으로 끝나지 않게 합니다.

            ## 품질을 높이는 기록 양식

            | 항목 | 기록할 내용 | 왜 중요한가 |
            | --- | --- | --- |
            | 기준 신호 | `{signal_a}`의 현재 값 또는 상태 | 제목만 보고 판단하지 않게 합니다 |
            | 보조 신호 | `{signal_b}`의 변화 방향 | 결론이 흔들리는 조건을 보여 줍니다 |
            | 출처 | 공식 문서와 확인 날짜 | 오래된 정보와 추정을 구분합니다 |
            | 행동 | 담당자와 다음 확인일 | 읽고 끝나는 글을 실행으로 바꿉니다 |

            ## 자주 묻는 질문

            ### 이 주제는 한 번 확인하면 끝나나요?

            아닙니다. `{signal_a}`와 `{signal_b}`는 환경이 바뀌면 의미가 달라질 수 있습니다. 최소한 분기별로 출처와 내부 기록을 다시 확인하는 편이 안전합니다.

            ### 공식 출처만 보면 충분한가요?

            공식 출처는 기준점입니다. 다만 실제 의사결정에는 내부 비용, 일정, 데이터 품질, 계약 조건처럼 공개 자료에 없는 변수가 들어갑니다. 두 층을 섞지 않고 나눠 적는 것이 중요합니다.

            ### 조회수를 위해 더 자극적인 결론을 써도 되나요?

            단기 클릭에는 도움이 될 수 있지만 오래 남는 글은 검증 가능한 기준을 줍니다. 특히 이 분야는 과장된 표현보다 재확인 가능한 절차가 신뢰를 만듭니다.

            {source_notes(field_key, "ko")}

            {related(field, "ko")}
            """
            )
        )
    return normalize_body(
        dedent(
        f"""\
        {field["en_intro"]}

        This guide treats **{title}** as a practical checklist rather than a headline. The useful move is to track `{signal_a}` and `{signal_b}` together, then separate conditions that require more review from conditions that require action.

        {field["en_disclaimer"]}

        ![{title} core workflow diagram]({hero})

        ## Search Intent and Reader Problem

        Readers searching this topic usually need more than a definition. They need a standard they can use in a team meeting, household decision, project review, or risk check. This guide answers three questions.

        - What should be checked first?
        - What record will make the decision explainable later?
        - How should official sources be separated from internal judgment?

        ## Standards To Check First

        - **Primary signal**: Track `{signal_a}` with date, source, and owner instead of as an isolated number.
        - **Secondary signal**: Mark whether a change in `{signal_b}` should reopen the conclusion.
        - **Evidence level**: Separate official documents, institution-grade sources, internal logs, and assumptions.
        - **Update trigger**: Revisit the decision when rules, data, incidents, or costs change.

        ![{title} practical checklist]({checklist})

        ## Practical Workflow

        1. Write the current problem in one sentence, such as “we are delayed because `{signal_a}` is unclear.”
        2. Separate what must be checked in official sources from what only internal records can answer.
        3. In the review table, include date, source link, reasoning, next action, and owner.
        4. When many stakeholders are involved, share assumptions and exclusions before the conclusion.
        5. Leave a two-week follow-up item so the article becomes an operating reference rather than a one-time summary.

        ## Record Template

        | Item | What to Record | Why It Matters |
        | --- | --- | --- |
        | Primary signal | Current state of `{signal_a}` | Prevents headline-only decisions |
        | Secondary signal | Direction of `{signal_b}` | Shows when the conclusion can change |
        | Source | Official source and check date | Separates old information from assumptions |
        | Action | Owner and next review date | Turns reading into execution |

        ## FAQ

        ### Is this a one-time check?

        No. `{signal_a}` and `{signal_b}` can change meaning as rules, data, costs, or user behavior change. A quarterly review is a practical minimum for most teams.

        ### Are official sources enough?

        Official sources provide the baseline. Real decisions also depend on internal costs, schedules, data quality, contracts, and risk tolerance. Keep those layers separate.

        ### Should the conclusion be stronger for traffic?

        Short-term clicks may reward bold claims, but durable search traffic comes from verifiable standards, source notes, and concrete workflows.

        {source_notes(field_key, "en")}

        {related(field, "en")}
        """
        )
    )


def write_post(field_key: str, topic: tuple[str, str, str, str, str], day: date, lang: str) -> None:
    field = FIELDS[field_key]
    slug = topic[0]
    post_dir = ROOT / "_posts" / lang
    path = post_dir / f"{day.isoformat()}-{slug}.md"
    text = front_matter(field, topic, day, lang) + body(field_key, field, topic, lang)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    written = []
    index = 0
    for field_key, topics in TOPICS.items():
        if len(topics) != 20:
            raise ValueError(f"{field_key} has {len(topics)} topics, expected 20")
        field = FIELDS[field_key]
        for topic in topics:
            day = START_DATE - timedelta(days=index)
            title_ko = topic[1]
            title_en = topic[2]
            labels = [topic[3], topic[4], "source", "action"]
            image_dir = ROOT / "images" / f"expert-growth-{topic[0]}"
            svg(image_dir / "hero.svg", title_en, title_ko, labels, "en")
            svg(image_dir / "checklist.svg", title_ko, title_en, labels, "ko")
            write_post(field_key, topic, day, "ko")
            write_post(field_key, topic, day, "en")
            written.append((field["en_category"], topic[0], day.isoformat()))
            index += 1
    print(f"Generated {len(written)} topic pairs")
    for category, slug, day in written:
        print(f"{day} {category} {slug}")


if __name__ == "__main__":
    main()
