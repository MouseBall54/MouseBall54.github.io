# 100 Post Multidomain Growth Queue

Created: 2026-05-23

This queue translates the expanded traffic goal into paired Korean and English topic sets.
It began as a 50-pair campaign, but production now intentionally exceeds that baseline as fields are expanded toward roughly 30 or more topic pairs each.
The list keeps the existing troubleshooting strength, then adds study, economy, AI trends, and practical AI workflow content.

## Operating Rules

- Publish Korean and English posts together with the same `translation_id`.
- Create or select at least two useful images for every topic pair.
- Prefer original diagrams, screenshots, annotated workflows, tables, or generated editorial images that explain the topic.
- Use generated images only when they help understanding; never use generic decorative stock-like images.
- Put the primary image in `header.teaser`, `header.overlay_image`, and once near the opening section when it clarifies the concept.
- Include 2-4 internal links per post when relevant existing posts exist.
- Include external sources for AI trends, economy, policy, or time-sensitive claims.
- During this bulk-writing phase, run `npm run validate:content-plan`; skip `bundle exec jekyll build --trace` unless explicitly requested.

## Topic Mix

| Domain | Topic pairs | Post files | Search intent |
| --- | ---: | ---: | --- |
| Troubleshooting | 20 | 40 | Immediate problem solving |
| AI trends and workflow | 30 | 60 | Current AI adoption and practical implementation |
| Study and productivity | 32 | 64 | Evidence-informed study systems and exam preparation |
| Economy and money basics | 36 | 72 | Official-source economic indicators and household cost explanations |
| Easy Labeling and computer vision | 5 | 10 | Product-led education and tool discovery |
| Total | 123 | 246 | Balanced growth portfolio |

## Troubleshooting: 20 Topic Pairs

| Status | Translation ID | Primary keyword | Korean title direction | English title direction | Image direction |
| --- | --- | --- | --- | --- | --- |
| review | python-pip-install-failed | pip install failed | Python `pip install` 실패 해결 | How to Fix pip install Failed in Python | terminal error + package flow |
| review | python-no-module-named-pip | No module named pip | `No module named pip` 해결 | How to Fix No module named pip | Python interpreter and pip module |
| review | python-venv-not-activating | python venv not activating | Python 가상환경이 활성화되지 않을 때 | Python venv Not Activating | virtual environment path map |
| review | python-command-not-found-windows | python command not found windows | Windows에서 `python` 명령어가 안 될 때 | Python Command Not Found on Windows | Windows PATH diagram |
| review | python-externally-managed-environment | externally-managed-environment | `externally-managed-environment` 해결 | Fix externally-managed-environment in Python | system Python vs venv |
| review | javascript-npm-err-eresolve | npm ERR ERESOLVE | `npm ERR! ERESOLVE` 해결 | How to Fix npm ERR ERESOLVE | dependency conflict graph |
| review | node-cannot-find-module | Cannot find module node | `Cannot find module` 해결 | Fix Cannot Find Module in Node.js | Node module resolution |
| review | typescript-cannot-find-name | TypeScript Cannot find name | TypeScript `Cannot find name` 해결 | Fix TypeScript Cannot Find Name | TypeScript scope diagram |
| review | typescript-property-does-not-exist | Property does not exist on type | `Property does not exist on type` 해결 | Fix Property Does Not Exist on Type | object type mismatch |
| review | typescript-tsconfig-paths-not-working | tsconfig paths not working | `tsconfig` paths가 동작하지 않을 때 | tsconfig Paths Not Working | tsconfig path alias map |
| review | github-actions-build-failed | GitHub Actions build failed | GitHub Actions build failed 해결 | How to Fix GitHub Actions Build Failed | CI pipeline failure |
| review | github-pages-jekyll-build-failed | GitHub Pages Jekyll build failed | GitHub Pages Jekyll build 실패 | Fix GitHub Pages Jekyll Build Failed | Jekyll build pipeline |
| review | git-fatal-authentication-failed | git fatal authentication failed | `fatal: authentication failed` 해결 | Fix Git fatal authentication failed | credential flow |
| review | git-gh006-protected-branch | GH006 protected branch | `GH006 protected branch hook declined` 해결 | Fix GH006 Protected Branch Hook Declined | protected branch gate |
| review | spring-boot-port-8080-already-in-use | Spring Boot port 8080 already in use | Spring Boot port 8080 already in use 해결 | Fix Spring Boot Port 8080 Already in Use | port conflict map |
| review | gradle-build-failed | Gradle build failed | Gradle build failed 해결 | How to Fix Gradle Build Failed | Gradle task pipeline |
| review | maven-dependency-not-found | Maven dependency not found | Maven dependency not found 해결 | Fix Maven Dependency Not Found | Maven repository lookup |
| review | java-unsupported-class-file-major-version | unsupported class file major version | Unsupported class file major version 해결 | Fix Unsupported Class File Major Version | JDK version ladder |
| review | docker-daemon-not-running | Docker daemon not running | Docker daemon not running 해결 | Fix Docker Daemon Not Running | Docker client/server |
| review | vscode-python-interpreter-not-showing | VS Code Python interpreter not showing | VS Code Python interpreter 선택 문제 | VS Code Python Interpreter Not Showing | VS Code interpreter picker |

## AI Trends and Workflow: 30 Topic Pairs

Production source: `tools/generate_ai_trends_posts.py`.
The table below records the original seed set; the generator now expands this field to 30 paired Korean and English posts.

| Status | Translation ID | Primary keyword | Korean title direction | English title direction | Image direction |
| --- | --- | --- | --- | --- | --- |
| review | ai-agent-workflow-2026 | AI agent workflow | AI agent workflow 2026: 자동화보다 검증이 먼저 | AI Agent Workflow 2026: Build for Verification First | generated workflow diagram |
| review | openai-responses-api-guide | OpenAI Responses API | OpenAI Responses API 사용 흐름 | OpenAI Responses API Practical Guide | request-response flow |
| review | ai-tools-function-calling | AI tool calling | AI tool calling과 function calling 차이 | AI Tool Calling vs Function Calling | tool routing diagram |
| review | rag-evaluation-checklist | RAG evaluation checklist | RAG 답변 품질 평가 체크리스트 | RAG Evaluation Checklist | retrieval and answer scoring |
| review | local-llm-vs-cloud-llm | local LLM vs cloud LLM | Local LLM과 Cloud LLM 선택 기준 | Local LLM vs Cloud LLM | tradeoff matrix |
| review | ai-coding-agent-workflow | AI coding agent workflow | AI coding agent를 안전하게 쓰는 워크플로우 | AI Coding Agent Workflow | coding review loop |
| review | ai-search-optimization | AI search optimization | AI 검색 시대의 글 작성 기준 | How to Write for AI Search | content answer blocks |
| review | prompt-engineering-checklist | prompt engineering checklist | Prompt engineering 실무 체크리스트 | Prompt Engineering Checklist | prompt structure board |
| review | ai-automation-roi | AI automation ROI | AI 자동화 ROI 계산법 | How to Calculate AI Automation ROI | process cost chart |
| review | ai-meeting-notes-workflow | AI meeting notes workflow | AI 회의록 자동화 워크플로우 | AI Meeting Notes Workflow | meeting to action pipeline |

## Study and Productivity: 32 Topic Pairs

Production source: `tools/generate_study_posts.py`.

| Status | Translation ID | Primary keyword | Korean title direction | English title direction | Image direction |
| --- | --- | --- | --- | --- | --- |
| review | active-recall-study-method | ActiveRecall | Active Recall 공부법: 읽은 내용을 덮고 꺼내 쓰는 루틴 | Active Recall Study Method: Close the Book and Retrieve | study routine diagram |
| review | spaced-repetition-schedule | SpacedRepetition | Spaced Repetition 복습 일정: 몰아보기보다 간격을 설계하기 | Spaced Repetition Schedule: Design Gaps Instead of Cramming | study routine diagram |
| review | pomodoro-deep-work | Focus | Pomodoro와 Deep Work: 타이머보다 방해 차단이 먼저다 | Pomodoro and Deep Work: Block Distractions Before Timing | study routine diagram |
| review | exam-mistake-note-system | ExamPrep | 오답노트 시스템: 틀린 문제를 다시 틀리지 않는 기록법 | Exam Mistake Note System: Turn Wrong Answers into Review Tasks | study routine diagram |
| review | coding-study-roadmap | CodingStudy | 코딩 공부 로드맵: 문법, 프로젝트, 디버깅을 한 루프로 묶기 | Coding Study Roadmap: Connect Syntax, Projects, and Debugging | study routine diagram |
| review | english-vocabulary-system | Vocabulary | 영어 단어 반복 시스템: 뜻 암기보다 문맥과 회상으로 남기기 | English Vocabulary System: Learn Words Through Context and Recall | study routine diagram |
| review | notion-study-dashboard | Notion | Notion 공부 대시보드: 예쁜 화면보다 복습과 오답 흐름 | Notion Study Dashboard: Track Review and Mistakes Before Design | study routine diagram |
| review | weekly-study-review | WeeklyReview | 주간 공부 회고: 공부 시간보다 회상률과 산출물 보기 | Weekly Study Review: Track Recall and Output, Not Only Hours | study routine diagram |
| review | interleaving-practice | Interleaving | Interleaving Practice: 비슷한 문제를 섞어 진짜 구분력을 키우기 | Interleaving Practice: Mix Similar Problems to Build Discrimination | study routine diagram |
| review | practice-test-review | PracticeTests | 모의고사 리뷰법: 점수보다 틀린 근거를 먼저 분해하기 | Practice Test Review: Break Down Evidence Before Chasing Scores | study routine diagram |
| review | question-bank-system | QuestionBank | 질문은행 만들기: 필기노트를 회상 문제로 바꾸는 법 | Question Bank System: Convert Notes into Recall Prompts | study routine diagram |
| review | semester-study-calendar | StudyPlanning | 학기 공부 캘린더: 시험 직전이 아니라 제출일에서 거꾸로 계획하기 | Semester Study Calendar: Plan Backward from Exams and Deadlines | study routine diagram |
| review | cornell-note-taking-system | CornellNotes | Cornell Note Taking: 필기를 복습 질문으로 바꾸는 구조 | Cornell Note Taking: Turn Notes into Review Questions | study routine diagram |
| review | textbook-reading-output | Reading | 교재 읽기 루틴: 밑줄보다 질문, 요약, 예제로 남기기 | Textbook Reading Routine: Leave Questions, Summary, and Examples | study routine diagram |
| review | lecture-review-24-hour | LectureReview | 강의 후 24시간 리뷰: 잊기 전에 회상 질문 만들기 | 24-Hour Lecture Review: Create Recall Questions Before Forgetting | study routine diagram |
| review | math-problem-solving-routine | MathStudy | 수학 문제 풀이 루틴: 공식 암기보다 조건 해석 먼저 | Math Problem-Solving Routine: Read Conditions Before Formulas | study routine diagram |
| review | writing-revision-study-loop | Writing | 글쓰기 공부 루프: 초안, 피드백, 재작성으로 실력 만들기 | Writing Revision Study Loop: Draft, Feedback, Rewrite | study routine diagram |
| review | coding-kata-deliberate-practice | CodingPractice | Coding Kata 루틴: 같은 문제를 다르게 풀어 패턴을 익히기 | Coding Kata Routine: Solve the Same Problem in Better Ways | study routine diagram |
| review | project-based-learning-portfolio | ProjectBasedLearning | 프로젝트 기반 공부 포트폴리오: 결과물과 회고를 함께 남기기 | Project-Based Learning Portfolio: Keep Output and Reflection Together | study routine diagram |
| review | language-shadowing-routine | LanguageLearning | Language Shadowing 루틴: 따라 말하기를 녹음과 피드백으로 바꾸기 | Language Shadowing Routine: Turn Repetition into Recorded Feedback | study routine diagram |
| review | flashcard-quality-rules | Flashcards | Flashcard 품질 규칙: 카드 수보다 한 카드 한 질문 | Flashcard Quality Rules: One Card, One Question | study routine diagram |
| review | exam-time-management | ExamStrategy | 시험 시간 관리: 어려운 문제보다 시간 손실 지점을 먼저 찾기 | Exam Time Management: Find Where Time Leaks Before Hard Problems | study routine diagram |
| review | sleep-study-performance | Sleep | 수면과 공부 성과: 밤샘보다 기억과 집중을 보호하기 | Sleep and Study Performance: Protect Memory and Attention | study routine diagram |
| review | distraction-audit-study | Focus | 공부 방해요인 감사: 의지보다 환경과 트리거를 고치기 | Study Distraction Audit: Fix Environment and Triggers Before Willpower | study routine diagram |
| review | study-group-rules | StudyGroup | 스터디 그룹 규칙: 친목보다 문제 풀이와 피드백을 남기기 | Study Group Rules: Leave Problem Solving and Feedback | study routine diagram |
| review | metacognition-study-log | Metacognition | Metacognition 공부 로그: 안다고 느낀 것과 실제 회상을 비교하기 | Metacognition Study Log: Compare Confidence with Recall | study routine diagram |
| review | research-note-citation-system | ResearchNotes | 리서치 노트와 출처 관리: 복붙보다 요약과 인용 기준 | Research Note and Citation System: Summarize Before Quoting | study routine diagram |
| review | reading-comprehension-prompts | Reading | 독해력 질문 프롬프트: 글을 읽고 주장, 근거, 반례를 찾기 | Reading Comprehension Prompts: Find Claims, Evidence, and Counterexamples | study routine diagram |
| review | spaced-review-for-coding | CodingStudy | 코딩 개념 Spaced Review: 문법을 프로젝트 안에서 다시 쓰기 | Spaced Review for Coding Concepts: Reuse Syntax in Projects | study routine diagram |
| review | habit-stack-study-routine | StudyHabit | 공부 습관 쌓기: 큰 목표보다 시작 신호와 첫 10분 | Habit Stack Study Routine: Start Signal and First Ten Minutes | study routine diagram |
| review | exam-day-checklist | ExamDay | 시험 당일 체크리스트: 새 공부보다 실수 방지에 집중하기 | Exam Day Checklist: Prevent Mistakes Instead of Adding New Study | study routine diagram |
| review | learning-with-ai-safely | AIStudy | AI로 공부할 때 주의점: 답을 받기보다 질문과 피드백에 쓰기 | Learning with AI Safely: Use It for Questions and Feedback | study routine diagram |

## Economy and Money Basics: 36 Topic Pairs

Production source: `tools/generate_economy_posts.py`.

| Status | Translation ID | Primary keyword | Korean title direction | English title direction | Image direction |
| --- | --- | --- | --- | --- | --- |
| review | interest-rate-inflation-basics | InterestRates | 금리와 물가 기초: 중앙은행 뉴스를 생활비 언어로 읽기 | Interest Rates and Inflation: Read Central Bank News in Household Terms | economy decision diagram |
| review | exchange-rate-basics | ExchangeRates | 환율 기초: 원화 약세가 여행, 수입물가, 수출에 주는 영향 | Exchange Rate Basics: Travel, Import Prices, and Exports | economy decision diagram |
| review | etf-vs-mutual-fund | ETF | ETF와 펀드 차이: 수수료, 거래 방식, 세금을 먼저 비교하기 | ETF vs Mutual Fund: Compare Fees, Trading, and Taxes First | economy decision diagram |
| review | compound-interest-example | CompoundInterest | 복리 계산 예시: 수익률보다 기간과 추가 납입이 중요한 이유 | Compound Interest Example: Time and Contributions Matter | economy decision diagram |
| review | household-budget-50-30-20 | Budgeting | 50/30/20 예산법: 규칙보다 고정비와 현금흐름 먼저 보기 | 50/30/20 Budget Rule: Start With Fixed Costs and Cash Flow | economy decision diagram |
| review | emergency-fund-how-much | EmergencyFund | 비상금은 얼마가 적당할까: 3개월보다 먼저 봐야 할 생활비 | How Much Emergency Fund Is Enough? Start With Essential Costs | economy decision diagram |
| review | recession-indicators-basics | Recession | 경기 침체 지표 읽기: GDP, 고용, 소비를 한 번에 보기 | Recession Indicators: Read GDP, Jobs, and Consumption Together | economy decision diagram |
| review | real-wage-purchasing-power | Wages | 실질임금과 구매력: 월급이 올랐는데 왜 빠듯한지 계산하기 | Real Wages and Purchasing Power: Why Raises Can Still Feel Tight | economy decision diagram |
| review | cpi-vs-personal-inflation | CPI | CPI와 개인 물가 차이: 공식 물가와 체감 물가가 다른 이유 | CPI vs Personal Inflation: Why Official Inflation Feels Different | economy decision diagram |
| review | gdp-components-guide | GDP | GDP 구성요소 읽기: 소비, 투자, 정부, 순수출을 나눠 보기 | GDP Components: Read Consumption, Investment, Government, and Net Exports | economy decision diagram |
| review | unemployment-rate-labor-market | LaborMarket | 실업률과 노동시장: 낮은 실업률만 보면 놓치는 신호 | Unemployment Rate and Labor Market Signals Beyond the Headline | economy decision diagram |
| review | central-bank-meeting-how-to-read | CentralBanks | 중앙은행 회의 읽는 법: 결정문, 전망, 기자회견을 분리하기 | How to Read a Central Bank Meeting: Statement, Projections, Press Conference | economy decision diagram |
| review | bond-yield-curve-basics | Bonds | 채권 금리와 수익률 곡선: 장단기 금리가 말하는 경기 기대 | Bond Yields and the Yield Curve: What Short and Long Rates Signal | economy decision diagram |
| review | household-debt-service-ratio | HouseholdDebt | 가계부채 부담 읽기: 대출 잔액보다 월 상환액이 먼저다 | Household Debt Burden: Monthly Payments Matter Before Balances | economy decision diagram |
| review | current-account-trade-balance | TradeBalance | 경상수지와 무역수지: 수출이 좋아도 환율이 흔들릴 수 있는 이유 | Current Account and Trade Balance: Why Exports Do Not Explain Everything | economy decision diagram |
| review | oil-price-import-inflation | OilPrices | 유가와 수입물가: 국제유가가 전기요금과 장바구니까지 오는 경로 | Oil Prices and Import Inflation: From Crude Markets to Household Bills | economy decision diagram |
| review | semiconductor-cycle-korea-economy | Semiconductors | 반도체 경기와 한국 경제: 수출 호황이 모두에게 같지 않은 이유 | Semiconductor Cycle and Korea: Why Export Booms Feel Uneven | economy decision diagram |
| review | fiscal-deficit-public-debt | FiscalPolicy | 재정적자와 국가채무: 좋은 지출과 지속가능성을 같이 보기 | Fiscal Deficits and Public Debt: Read Support and Sustainability Together | economy decision diagram |
| review | dollar-won-exchange-rate-checklist | KoreanWon | 원달러 환율 체크리스트: 뉴스 한 줄보다 금리차, 유가, 수지를 같이 보기 | Dollar-Won Exchange Rate Checklist: Rates, Oil, and External Balance | economy decision diagram |
| review | savings-rate-real-interest-rate | Saving | 저축금리와 실질금리: 예금 이자가 물가를 이기는지 확인하기 | Savings Rates and Real Interest: Check Whether Interest Beats Inflation | economy decision diagram |
| review | mortgage-rate-rent-affordability | Housing | 주택담보대출 금리와 임대료: 집값보다 월 부담액 먼저 계산하기 | Mortgage Rates and Rent Affordability: Calculate Monthly Burden First | economy decision diagram |
| review | credit-card-interest-minimum-payment | CreditCards | 신용카드 이자와 최소결제: 잔액이 오래 남는 구조 이해하기 | Credit Card Interest and Minimum Payments: Why Balances Last | economy decision diagram |
| review | supply-chain-shock-inflation | SupplyChains | 공급망 충격과 물가: 운임, 재고, 대체 공급처를 같이 보기 | Supply Chain Shocks and Inflation: Freight, Inventories, and Substitutes | economy decision diagram |
| review | productivity-wage-growth | Productivity | 생산성과 임금: 경제가 좋아져도 임금이 늦게 움직이는 이유 | Productivity and Wages: Why Pay Can Lag a Better Economy | economy decision diagram |
| review | inflation-expectations-guide | InflationExpectations | 기대 인플레이션 읽기: 사람들이 믿는 물가가 실제 물가에 미치는 영향 | Inflation Expectations: Why Beliefs About Prices Matter | economy decision diagram |
| review | global-growth-forecast-how-to-read | GlobalEconomy | 세계 성장률 전망 읽기: IMF·OECD·World Bank 숫자가 다른 이유 | How to Read Global Growth Forecasts from IMF, OECD, and World Bank | economy decision diagram |
| review | trade-tariff-household-prices | Tariffs | 관세와 생활물가: 무역정책이 소비자 가격으로 오는 경로 | Tariffs and Household Prices: How Trade Policy Reaches Consumers | economy decision diagram |
| review | emergency-budget-job-loss | EmergencyBudget | 실직 대비 비상 예산: 평상시 예산과 위기 예산을 나누기 | Emergency Budget for Job Loss: Separate Normal and Crisis Spending | economy decision diagram |
| review | deposit-insurance-bank-risk | DepositInsurance | 예금자보호와 은행 리스크: 금리보다 안전 한도를 먼저 확인하기 | Deposit Insurance and Bank Risk: Check Safety Limits Before Yield | economy decision diagram |
| review | consumer-sentiment-economic-signal | ConsumerSentiment | 소비심리 지표 읽기: 기분과 실제 소비를 구분하기 | Consumer Sentiment as an Economic Signal: Separate Mood from Spending | economy decision diagram |
| review | core-vs-headline-inflation | Inflation | 근원물가와 헤드라인 물가: 에너지·식품 변동을 따로 보는 이유 | Core vs Headline Inflation: Why Food and Energy Are Read Separately | economy decision diagram |
| review | nominal-vs-real-gdp | GDP | 명목 GDP와 실질 GDP: 성장과 물가 효과를 분리하기 | Nominal vs Real GDP: Separate Growth from Price Effects | economy decision diagram |
| review | household-balance-sheet-basics | HouseholdFinance | 가계 재무상태표: 소득보다 자산, 부채, 유동성을 함께 보기 | Household Balance Sheet Basics: Assets, Debt, and Liquidity | economy decision diagram |
| review | small-business-break-even-inflation | SmallBusiness | 소상공인 손익분기점과 물가: 매출보다 마진을 먼저 지키기 | Small Business Break-Even and Inflation: Protect Margin Before Revenue | economy decision diagram |
| review | global-dollar-liquidity-basics | Dollar | 달러 유동성 기초: 미국 금리가 세계 금융여건에 미치는 영향 | Global Dollar Liquidity: How U.S. Rates Shape Financial Conditions | economy decision diagram |
| review | economic-calendar-for-households | EconomicCalendar | 가계를 위한 경제 캘린더: CPI, 고용, 금리, 환율 발표일 정리 | Economic Calendar for Households: CPI, Jobs, Rates, and Exchange Rates | economy decision diagram |

## Easy Labeling and Computer Vision: 5 Topic Pairs

| Status | Translation ID | Primary keyword | Korean title direction | English title direction | Image direction |
| --- | --- | --- | --- | --- | --- |
| review | yolo-label-format | YOLO label format | YOLO label format 읽는 법 | How to Read YOLO Label Format | labeled bounding box |
| review | coco-to-yolo-conversion | COCO to YOLO | COCO to YOLO 변환 실수 | COCO to YOLO Conversion Mistakes | format conversion |
| review | image-labeling-classes | image labeling classes | 이미지 라벨링 클래스 관리법 | How to Manage Classes for Image Labeling | class taxonomy |
| review | local-image-labeling-workflow | local image labeling | 로컬 이미지 라벨링 워크플로우 | Local Image Labeling Workflow | local folder flow |
| review | easy-labeling-yolo-dataset | Easy Labeling YOLO | Easy Labeling으로 YOLO 데이터셋 만들기 | Build a YOLO Dataset with Easy Labeling | Easy Labeling screen flow |

## Image Checklist

For each topic pair:

- Save generated or original images under `images/YYYY-MM-DD-slug/`.
- Use descriptive filenames such as `hero.png`, `workflow.png`, or `example-output.png`.
- Add meaningful alt text in both languages.
- Avoid small text inside generated images unless the image is manually verified.
- Prefer diagrams and annotated screenshots for troubleshooting posts.
- Prefer conceptual editorial illustrations for AI trends, study, and economy posts.

## AdSense Checklist

- Keep the global AdSense script in `_includes/head/custom.html`.
- Use the same publisher ID as `ads.txt`: `pub-2983974324971673`.
- Keep manual post ads controlled by `_includes/ad-content.html` and `_includes/ad-inarticle.html`.
- Do not enable live manual units until `adsense.in_article_slot` and `adsense.post_bottom_slot` are set.
- Keep the minimum word threshold enabled so short posts do not show disruptive ads.
