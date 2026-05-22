# 100 Post Multidomain Growth Queue

Created: 2026-05-23

This queue translates the expanded traffic goal into 50 paired topics, or about 100 posts when Korean and English versions are published together.
The list keeps the existing troubleshooting strength, then adds study, economy, AI trends, and practical AI workflow content.

## Operating Rules

- Publish Korean and English posts together with the same `translation_id`.
- Create or select one useful image for every topic pair.
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
| AI trends and workflow | 10 | 20 | Current AI adoption and practical implementation |
| Study and productivity | 8 | 16 | Repeatable study systems and exam preparation |
| Economy and money basics | 7 | 14 | Evergreen financial literacy and market explanations |
| Easy Labeling and computer vision | 5 | 10 | Product-led education and tool discovery |
| Total | 50 | 100 | Balanced growth portfolio |

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

## AI Trends and Workflow: 10 Topic Pairs

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

## Study and Productivity: 8 Topic Pairs

| Status | Translation ID | Primary keyword | Korean title direction | English title direction | Image direction |
| --- | --- | --- | --- | --- | --- |
| review | active-recall-study-method | active recall study method | Active recall 공부법 실전 적용 | Active Recall Study Method | memory retrieval diagram |
| review | spaced-repetition-schedule | spaced repetition schedule | Spaced repetition 복습 일정 만들기 | Spaced Repetition Schedule | review calendar |
| review | pomodoro-deep-work | Pomodoro deep work | Pomodoro와 Deep Work를 함께 쓰는 법 | Pomodoro vs Deep Work | focused desk timeline |
| review | exam-mistake-note-system | mistake note study | 오답노트 시스템 만드는 법 | How to Build a Mistake Note System | correction workflow |
| review | coding-study-roadmap | coding study roadmap | 코딩 공부 로드맵 세우는 법 | Coding Study Roadmap | roadmap board |
| review | english-vocabulary-system | vocabulary study system | 영어 단어장 반복 시스템 | Vocabulary Study System | flashcard workflow |
| review | notion-study-dashboard | Notion study dashboard | Notion 공부 대시보드 구성 | Notion Study Dashboard | dashboard mockup |
| review | weekly-study-review | weekly study review | 주간 공부 회고 템플릿 | Weekly Study Review Template | weekly review sheet |

## Economy and Money Basics: 7 Topic Pairs

| Status | Translation ID | Primary keyword | Korean title direction | English title direction | Image direction |
| --- | --- | --- | --- | --- | --- |
| review | interest-rate-inflation-basics | interest rates and inflation | 금리와 물가가 같이 움직이는 이유 | Interest Rates and Inflation Explained | macro loop |
| review | exchange-rate-basics | exchange rate basics | 환율이 오르면 생기는 일 | Exchange Rate Basics | currency flow |
| review | etf-vs-mutual-fund | ETF vs mutual fund | ETF와 펀드 차이 | ETF vs Mutual Fund | comparison table |
| review | compound-interest-example | compound interest example | 복리 계산을 실제 숫자로 이해하기 | Compound Interest Example | growth curve |
| review | household-budget-50-30-20 | 50 30 20 budget rule | 50/30/20 예산법 쓰는 법 | 50/30/20 Budget Rule | budget pie chart |
| review | emergency-fund-how-much | emergency fund how much | 비상금은 얼마가 적당할까 | How Much Emergency Fund Do You Need | safety reserve |
| review | recession-indicators-basics | recession indicators | 경기 침체 지표 쉽게 읽기 | Recession Indicators Explained | indicator dashboard |

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
