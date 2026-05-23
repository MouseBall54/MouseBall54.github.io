# MouseBall54's Toolbox 주간 10만 조회 성장 마스터플랜

작성일: 2026-05-23  
목표: 주간 조회 수 100,000회 이상, 검색 유입 기반의 안정적 성장, Google AdSense 수익화 준비, 다분야 bilingual 콘텐츠 포트폴리오 운영

## 1. 목표와 기준

주간 100,000 조회는 하루 평균 약 14,300 조회다. 이 사이트는 단일 대형 글보다 검색 의도가 분명한 글을 폭넓게 누적하는 구조가 적합하다.
초기 강점은 개발 트러블슈팅이지만, 현재는 스터디, 경제 기초, AI 동향, 국제정세, 기후·에너지, 소비자 권리, 디지털 보안, 개인재무, 건강 문해력, 컴퓨터 비전 글까지 확장된 상태다.

현실적인 목표 모델은 다음과 같다.

| 단계 | 글 수 | 글당 주간 평균 조회 | 주간 조회 목표 |
| --- | ---: | ---: | ---: |
| 1차 | 200개 | 100회 | 20,000회 |
| 2차 | 350개 | 150회 | 52,500회 |
| 3차 | 500개 | 200회 | 100,000회 |

핵심 전제:

- 대량 생산보다, 검색 의도가 분명한 글을 꾸준히 누적한다.
- 한국어와 영어 글을 항상 함께 작성한다. 현재는 473개 주제 쌍, 즉 한국어 473개와 영어 473개를 기준으로 관리한다.
- AI로 초안을 만들 수는 있지만, 실행 결과, 버전 차이, 실패 사례, 검증 절차를 사람이 보강한다.
- 글마다 이해를 돕는 이미지를 새로 만들거나 직접 캡처하고, header와 본문 초반에 의미 있게 배치한다.
- 광고는 본문 탐색을 방해하지 않는 선에서 표준화한다.

## 2. 현재 저장소 기준 콘텐츠 현황

현재 `_posts/ko`와 `_posts/en`에는 각각 473개 글이 있다. 언어별 category 기준 주제 분포는 다음과 같다.

| 주제 | 영어 글 수 | 한국어 글 수 | 판단 |
| --- | ---: | ---: | --- |
| Troubleshooting | 150 | 150 | 강점. Python, JavaScript, Java, Git, Docker, CI 오류 검색 유입 기반 |
| AI Trends | 30 | 30 | 공식 문서와 거버넌스 기반 AI workflow, RAG, 보안, 비용, 평가 글 |
| Global Affairs | 30 | 30 | 세계정세와 한국-facing 수출, 에너지, 금융, 안보 채널 설명 |
| Climate & Energy | 38 | 38 | 전력망, AI 전력 수요, 재생에너지, 배터리, 기후 리스크 설명 |
| Consumer Rights | 30 | 30 | 환불, 구독취소, chargeback, 리콜, 항공·통신 분쟁 대응 |
| Digital Security | 30 | 30 | 피싱, MFA, 백업, 랜섬웨어, 개인정보, 가족·소상공인 보안 루틴 |
| Personal Finance | 30 | 30 | 예산, 부채, 신용, 세금, 투자위험, 수수료, 금융사기 교육 글 |
| Health Literacy | 30 | 30 | 수면, 활동, 영양, 예방, 증상기록, 약 안전, 응급 대비 교육 글 |
| Study | 32 | 32 | 회상, 간격복습, 오답, 집중, 코딩공부, 수면과 시험 루틴 |
| Economy | 36 | 36 | 금리, 물가, 환율, GDP, 고용, 가계부채, 생활비 설명 |
| Easy Labeling | 37 | 37 | YOLO, COCO 변환, bounding box QA, 데이터셋 분할, 로컬 라벨링 |

추가 기술 메모:

- `ads.txt`에는 AdSense publisher 항목이 있다.
- `_includes/head/custom.html`에는 AdSense script가 추가되어 있다.
- `_includes/ad-content.html`과 `_includes/ad-inarticle.html`로 포스트 본문 광고 위치를 제어한다.
- `_config.yml`의 `adsense.enabled`가 `false`이면 광고 markup은 준비되어도 live ad는 렌더링되지 않는다.
- 신규 대량 작성 중에는 시간이 오래 걸리는 `bundle exec jekyll build --trace`를 생략하고, `npm run validate:content-plan`을 우선 품질 게이트로 사용한다.

## 3. 시장 근거

이 계획은 다음 근거를 기준으로 한다.

- Google Search Central은 사람에게 도움이 되는 신뢰 가능한 콘텐츠와 좋은 페이지 경험을 우선하라고 안내한다. 출처: https://developers.google.com/search/docs/fundamentals/creating-helpful-content
- Google의 spam policies는 검색 순위 조작 목적의 대량 저가치 콘텐츠를 위험 신호로 본다. 출처: https://developers.google.com/search/docs/essentials/spam-policies
- Stack Overflow 2025 Developer Survey는 JavaScript, HTML/CSS, SQL, Python이 여전히 대규모 개발자 수요를 가진다고 보여준다. Python은 AI, data science, backend 수요와 함께 성장했다. 출처: https://survey.stackoverflow.co/2025/
- GitHub Octoverse 2025는 TypeScript가 GitHub에서 가장 많이 쓰이는 언어로 올라섰고, Python은 AI와 data science에서 계속 강하다고 설명한다. 출처: https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/
- AdSense는 사용자 경험, 광고와 콘텐츠의 구분, 과도한 광고 회피, genuine user interest를 강조한다. 출처: https://support.google.com/adsense/answer/1282097, https://support.google.com/adsense/answer/48182

## 4. 콘텐츠 전략

### 4.1 우선순위 원칙

1. 오류 메시지 그대로 검색하는 키워드를 우선한다.
2. 설치, 버전, 경로, 인증, CORS, permission, build failure처럼 즉시 해결 욕구가 강한 문제를 우선한다.
3. 한 글은 하나의 문제만 해결한다.
4. 한국어 글은 자연스러운 설명을 쓰되, 오류명과 명령어는 영어 원문을 유지한다.
5. 영어 글은 짧은 문장, 명확한 heading, 복사 가능한 명령어, verification section을 고정한다.

### 4.2 핵심 주제 축

| 축 | 목적 | 대표 키워드 |
| --- | --- | --- |
| Python 실무 오류 | 기존 강점 확장, AI/데이터 입문 유입 | pip install error, uv, venv, ModuleNotFoundError, PyTorch CUDA, FastAPI, Pydantic |
| JavaScript/TypeScript 오류 | GitHub/Stack Overflow 수요 반영 | TypeScript error, tsconfig, npm ERR, pnpm, Vite, React, Next.js |
| Git/GitHub 작업 오류 | 이미 글 수가 많고 검색 의도 명확 | GitHub Actions failed, deploy key, branch protection, GitHub Pages build, rebase conflict |
| Java/Spring Boot 오류 | Java 기본 예외에서 실무 프레임워크로 확장 | Spring Boot error, Gradle, Maven, JDK, Lombok, port 8080 |
| 개발 환경 문제 | 초보자와 실무자 모두 검색 | VS Code, WSL, Docker, Windows PATH, PowerShell, Homebrew |
| AI 개발 워크플로우 | 2025-2026 수요 확장 | OpenAI API, RAG, LangChain, Ollama, vector database, Pydantic AI |
| Easy Labeling | 대표 도구 브랜딩과 제품 유입 | YOLO labeling tool, image annotation, local labeling, custom-classes.yaml |
| 스터디와 생산성 | 반복 검색되는 학습법/템플릿 수요 | active recall, spaced repetition, Pomodoro, mistake note, study planner |
| 경제 기초 | evergreen 금융 문해력 유입 | interest rate, inflation, exchange rate, ETF, compound interest, budget |
| 국제정세 | 국내외 이슈와 생활·산업 영향 연결 | global growth, trade fragmentation, Korea exports, energy security |
| 기후·에너지 | 장기 정책·산업 변화 검색 유입 | AI electricity demand, grid bottlenecks, renewables, batteries, adaptation |
| 소비자 권리 | 실생활 문제 해결형 evergreen 유입 | refund, chargeback, subscription cancellation, recalls, complaint |
| 디지털 보안 | 일반 사용자와 소상공인 안전 루틴 | phishing, MFA, backup, ransomware, privacy |
| 개인재무 | 수익화 친화적 교육형 금융 문해력 | budget, debt payoff, credit score, emergency fund, scam |
| 건강 문해력 | 고검색량 evergreen 주제의 안전한 교육 글 | sleep, prevention, nutrition, medicine safety, mental health |

## 5. 키워드 마스터 리스트

아래 목록은 검색량 수치가 아니라 작성 우선순위다. 실제 순위는 Google Search Console, Google Trends, Ahrefs/Semrush 같은 외부 데이터가 확보되면 조정한다.

### 5.1 Python

| 우선순위 | 한국어 제목 방향 | English title direction | Primary keyword |
| --- | --- | --- | --- |
| P0 | Python `pip install` 실패 해결 | How to Fix pip install Failed in Python | pip install failed |
| P0 | `No module named pip` 해결 | How to Fix No module named pip | No module named pip |
| P0 | Python 가상환경이 활성화되지 않을 때 | Python venv Not Activating | python venv not activating |
| P0 | Windows에서 `python` 명령어가 안 될 때 | Python Command Not Found on Windows | python command not found windows |
| P0 | `externally-managed-environment` 해결 | Fix externally-managed-environment in Python | externally-managed-environment |
| P1 | `uv` 설치와 기존 pip 차이 | uv vs pip for Python Projects | uv python package manager |
| P1 | FastAPI `422 Unprocessable Entity` 해결 | Fix FastAPI 422 Unprocessable Entity | FastAPI 422 |
| P1 | Pydantic validation error 읽는 법 | How to Read Pydantic ValidationError | Pydantic ValidationError |
| P1 | PyTorch CUDA 설치 오류 해결 | Fix PyTorch CUDA Installation Errors | PyTorch CUDA install error |
| P2 | `UnicodeEncodeError`와 터미널 인코딩 | Fix UnicodeEncodeError in Python Terminal | UnicodeEncodeError |

### 5.2 JavaScript and TypeScript

| 우선순위 | 한국어 제목 방향 | English title direction | Primary keyword |
| --- | --- | --- | --- |
| P0 | `npm ERR! ERESOLVE` 해결 | How to Fix npm ERR ERESOLVE | npm ERR ERESOLVE |
| P0 | `Cannot find module` 해결 | Fix Cannot Find Module in Node.js | Cannot find module node |
| P0 | TypeScript `Cannot find name` 해결 | Fix TypeScript Cannot Find Name | TypeScript Cannot find name |
| P0 | `Property does not exist on type` 해결 | Fix Property Does Not Exist on Type | Property does not exist on type |
| P0 | `tsconfig` paths가 동작하지 않을 때 | tsconfig Paths Not Working | tsconfig paths not working |
| P1 | Vite dev server가 뜨지 않을 때 | Vite Dev Server Not Starting | Vite dev server not starting |
| P1 | React `useEffect` 무한 반복 해결 | Fix React useEffect Infinite Loop | React useEffect infinite loop |
| P1 | Next.js hydration error 해결 | Fix Next.js Hydration Error | Next.js hydration error |
| P1 | pnpm lockfile 오류 해결 | Fix pnpm Lockfile Errors | pnpm lockfile error |
| P2 | CORS preflight 오류 해결 | Fix CORS Preflight Error | CORS preflight error |

### 5.3 Git and GitHub

| 우선순위 | 한국어 제목 방향 | English title direction | Primary keyword |
| --- | --- | --- | --- |
| P0 | GitHub Actions build failed 해결 | How to Fix GitHub Actions Build Failed | GitHub Actions build failed |
| P0 | GitHub Pages Jekyll build 실패 | Fix GitHub Pages Jekyll Build Failed | GitHub Pages Jekyll build failed |
| P0 | `fatal: authentication failed` 해결 | Fix Git fatal authentication failed | git fatal authentication failed |
| P0 | `GH006 protected branch hook declined` 해결 | Fix GH006 Protected Branch Hook Declined | GH006 protected branch |
| P1 | rebase conflict 안전하게 해결 | How to Resolve Git Rebase Conflicts | git rebase conflict |
| P1 | `non-fast-forward` push rejected 해결 | Fix Git Non-Fast-Forward Push Rejected | git non-fast-forward |
| P1 | Git LFS quota exceeded 해결 | Fix Git LFS Quota Exceeded | Git LFS quota exceeded |
| P1 | GitHub token permission 오류 | Fix GitHub Token Permission Errors | GitHub token permission |
| P2 | `safe.directory` 오류 해결 | Fix Git safe.directory Error | git safe.directory |
| P2 | `.gitignore`가 적용되지 않을 때 | Gitignore Not Working | gitignore not working |

### 5.4 Java and Spring Boot

| 우선순위 | 한국어 제목 방향 | English title direction | Primary keyword |
| --- | --- | --- | --- |
| P0 | Spring Boot port 8080 already in use 해결 | Fix Spring Boot Port 8080 Already in Use | Spring Boot port 8080 already in use |
| P0 | Gradle build failed 해결 | How to Fix Gradle Build Failed | Gradle build failed |
| P0 | Maven dependency not found 해결 | Fix Maven Dependency Not Found | Maven dependency not found |
| P0 | Unsupported class file major version 해결 | Fix Unsupported Class File Major Version | unsupported class file major version |
| P1 | Lombok이 IDE에서 동작하지 않을 때 | Lombok Not Working in IntelliJ | Lombok not working IntelliJ |
| P1 | Spring Boot bean could not be found 해결 | Fix Spring Boot Bean Could Not Be Found | Spring Boot bean could not be found |
| P1 | JPA lazy initialization exception 해결 | Fix LazyInitializationException in JPA | LazyInitializationException |
| P1 | `Cannot resolve symbol` 해결 | Fix Cannot Resolve Symbol in IntelliJ | IntelliJ cannot resolve symbol |
| P2 | Java heap space와 GC 로그 확인 | Fix Java Heap Space Error | Java heap space |
| P2 | `Connection refused` in Spring Boot | Fix Spring Boot Connection Refused | Spring Boot connection refused |

### 5.5 개발 환경, Docker, WSL

| 우선순위 | 한국어 제목 방향 | English title direction | Primary keyword |
| --- | --- | --- | --- |
| P0 | VS Code Python interpreter 선택 문제 | VS Code Python Interpreter Not Showing | VS Code Python interpreter not showing |
| P0 | Windows PATH 설정 오류 해결 | Fix Windows PATH Not Working | Windows PATH not working |
| P0 | Docker daemon not running 해결 | Fix Docker Daemon Not Running | Docker daemon not running |
| P0 | WSL `network unreachable` 해결 | Fix WSL Network Unreachable | WSL network unreachable |
| P1 | Docker port already allocated 해결 | Fix Docker Port Is Already Allocated | Docker port already allocated |
| P1 | Docker compose env file 적용 문제 | Docker Compose env File Not Working | docker compose env file |
| P1 | PowerShell execution policy 오류 | Fix PowerShell Execution Policy Error | PowerShell execution policy |
| P1 | Homebrew command not found 해결 | Fix Homebrew Command Not Found | brew command not found |
| P2 | VS Code terminal encoding 문제 | Fix VS Code Terminal Encoding | VS Code terminal encoding |
| P2 | SSH config permission 오류 | Fix SSH Config Permission Error | SSH config permission |

### 5.6 AI 개발 and Computer Vision

| 우선순위 | 한국어 제목 방향 | English title direction | Primary keyword |
| --- | --- | --- | --- |
| P0 | OpenAI API key 환경변수 설정 | How to Set OPENAI_API_KEY | OPENAI_API_KEY |
| P0 | OpenAI API rate limit 해결 | Fix OpenAI API Rate Limit Error | OpenAI API rate limit |
| P0 | Ollama 모델 다운로드 오류 해결 | Fix Ollama Model Download Error | Ollama model download error |
| P1 | LangChain import 오류 해결 | Fix LangChain Import Errors | LangChain import error |
| P1 | RAG 벡터 검색이 빈 결과를 줄 때 | RAG Vector Search Returns No Results | RAG vector search no results |
| P1 | YOLO label format 읽는 법 | How to Read YOLO Label Format | YOLO label format |
| P1 | COCO to YOLO 변환 실수 | COCO to YOLO Conversion Mistakes | COCO to YOLO |
| P2 | 이미지 라벨링 클래스 관리법 | How to Manage Classes for Image Labeling | image labeling classes |
| P2 | Roboflow vs local labeling workflow | Roboflow vs Local Labeling Workflow | local image labeling |
| P2 | Easy Labeling으로 YOLO 데이터셋 만들기 | Build a YOLO Dataset with Easy Labeling | Easy Labeling YOLO |

## 6. 콘텐츠 생산 로드맵

### Phase 0: 기반 정리, 1주

- 대량 작성 중에는 `bundle exec jekyll build --trace`를 생략하고, 필요 시 별도 검증 작업으로 분리
- 최근 글 front matter 유효성 점검
- Search Console sitemap 제출 상태 확인
- GA4, Search Console, AdSense의 동일 URL 기준 추적표 작성
- AdSense script 위치와 수동 광고 include 설계

### Phase 1: 빠른 검색 유입 확보, 4주

목표:

- 1차 목표 큐 50쌍 작성은 완료했고, 현재는 주요 성장 카테고리 대부분이 30쌍 이상이다.
- 현재 완성 규모: Troubleshooting 150쌍, AI Trends 30쌍, Global Affairs 30쌍, Climate & Energy 38쌍, Consumer Rights 30쌍, Digital Security 30쌍, Personal Finance 30쌍, Health Literacy 30쌍, Study 32쌍, Economy 36쌍, Easy Labeling 37쌍.
- 신규 캠페인 글은 각 글마다 이미지 2개 이상, 내부 링크, 출처 또는 검수 기준, category hub 연결을 유지한다.

운영 기준:

- 하루 2쌍 이하로 발행한다.
- 작성한 글은 `npm run validate:content-plan`으로 front matter, paired translation, AdSense 기본 조건을 확인한다.
- 기존 글에서 같은 주제의 내부 링크 2개 이상을 추가한다.

### Phase 2: 클러스터 강화, 8주

목표:

- P1 글 80쌍 작성
- pillar page 8개 작성
- category별 상위 글에서 관련 글 링크 구조 정리

필수 pillar page:

- Python Errors and Environment Setup
- JavaScript and TypeScript Troubleshooting
- Git and GitHub Troubleshooting
- Java and Spring Boot Troubleshooting
- Docker and WSL Developer Setup
- AI Developer Workflow Notes
- Computer Vision Dataset Labeling
- Easy Labeling Guide Hub

### Phase 3: 수익화 최적화, 12주 이후

목표:

- Search Console에서 impressions가 높고 CTR이 낮은 글의 title/excerpt 개선
- AdSense에서 RPM이 높은 category를 기준으로 광고 밀도 실험
- 30일 단위로 글 업데이트, 내부 링크 추가, FAQ 보강
- Easy Labeling 관련 글에서 launch link와 실사용 화면 강화

## 7. 글 작성 표준

모든 글은 검색자가 첫 화면에서 답을 얻고, 이어서 자세한 맥락을 확인할 수 있어야 한다.
트러블슈팅 글은 다음 구조를 따른다.

1. 문제 요약: 오류 메시지와 재현 상황을 첫 3문장 안에 넣는다.
2. 원인: 버전, 경로, 권한, dependency, network, config 중 어디에 속하는지 설명한다.
3. 빠른 해결: 가장 안전한 해결책부터 제시한다.
4. 명령어 또는 코드: 복사 가능한 block으로 작성한다.
5. 검증 방법: 사용자가 문제가 해결됐는지 확인할 명령어를 제공한다.
6. 흔한 실수: 같은 오류를 다시 만들 수 있는 실수를 정리한다.
7. 관련 글: 같은 category 안에서 2-4개 링크한다.

스터디, 경제, AI 동향 글은 다음 구조를 따른다.

1. 핵심 요약: 검색자가 묻는 질문에 먼저 답한다.
2. 개념 설명: 용어를 짧게 정의하고 오해하기 쉬운 부분을 분리한다.
3. 실제 적용: 체크리스트, 예시, 템플릿, 숫자 계산, workflow 중 하나를 제공한다.
4. 이미지 설명: 생성 이미지나 도표가 무엇을 보여주는지 alt text와 본문으로 설명한다.
5. 검증 또는 주의점: AI/경제/정책처럼 바뀌는 내용은 확인일과 공식 출처를 남긴다.
6. 관련 글: 같은 category 안에서 2-4개 링크한다.

품질 기준:

- 제목에는 실제 검색어를 포함한다.
- excerpt는 120-160자 안팎으로 문제와 해결을 함께 말한다.
- 글 하나에 해결 대상은 하나만 둔다.
- 명령어는 Windows, macOS/Linux 차이가 있으면 분리한다.
- 버전 의존적인 내용은 작성일 또는 확인 버전을 적는다.
- 자동 생성 문장처럼 보이는 결론은 쓰지 않는다.
- 이미지에는 의미 있는 alt text를 넣고, 생성 이미지에 들어간 작은 글자는 신뢰하지 않는다.

## 8. 내부 링크 전략

링크 구조:

- 오류 글 -> 상위 pillar page
- 오류 글 -> 같은 도구의 관련 오류 2개
- pillar page -> 관련 오류 글 목록
- Easy Labeling 글 -> `https://mouseball54.github.io/easy_labeling/`

예시:

- `npm ERR ERESOLVE` -> `Cannot find module`, `pnpm lockfile error`, JavaScript/TypeScript pillar
- `GitHub Pages Jekyll build failed` -> `GitHub Actions build failed`, front matter troubleshooting, Git/GitHub pillar
- `YOLO label format` -> Easy Labeling guide, COCO to YOLO, image labeling classes

## 9. AdSense 배치 계획

현재 상태:

- `ads.txt`는 존재한다.
- `_includes/head/custom.html`에 AdSense script가 있고, 현재 `auto_ads: true`로 Auto ads script가 로드된다.
- `_includes/ad-content.html`과 `_includes/ad-inarticle.html`이 있다.
- `_config.yml`에서 `adsense.enabled`, `in_article_slot`, `post_bottom_slot`, `min_words_for_ads`로 렌더링을 제어한다.
- 수동 본문/하단 광고는 AdSense slot ID가 들어오기 전까지 비활성이다.

권장 구현:

1. AdSense에서 manual ad unit을 만든 뒤 `in_article_slot`과 `post_bottom_slot`을 설정한다.
2. Auto ads는 현재 켜져 있으므로, 수동 광고 단위가 준비되면 slot ID를 추가해 본문 중간/하단 배치를 보강한다.
3. 글 길이에 따라 광고 수를 제한한다.
4. 검색, 태그, 카테고리, 짧은 static page에는 광고를 넣지 않거나 Auto ads excluded pages로 관리한다.
5. 이미지와 광고가 연속으로 붙어 콘텐츠 흐름을 끊지 않게 한다.

초기 배치:

| 위치 | 조건 | 목적 |
| --- | --- | --- |
| 본문 첫 번째 H2 이후 | 800단어 이상 글 | 초반 이탈 전 수익화 |
| 본문 중간 | 1,400단어 이상 글 | 긴 글 수익화 |
| 본문 끝, 관련 글 전 | 모든 충분한 길이의 글 | 검색 문제 해결 후 자연스러운 노출 |
| sidebar 또는 side rail | desktop only, UX 확인 후 | desktop 추가 수익 |

제한:

- 광고가 콘텐츠보다 많아 보이면 안 된다.
- 광고 위 label은 `Advertisements` 또는 `Sponsored links`만 사용한다.
- "광고를 클릭해 주세요" 같은 문구를 절대 쓰지 않는다.
- 다운로드 버튼, navigation, code copy button 근처에는 광고를 배치하지 않는다.
- 본인 광고 클릭과 자동/반복 노출 유도는 금지한다.

Auto ads 운영:

- 첫 2주는 Auto ads를 낮은 밀도로 켜고 Search Console/GA4 체류 지표를 본다.
- anchor ads는 mobile UX를 실제 기기에서 확인한 뒤 유지 여부를 결정한다.
- vignette ads는 개발 문서 탐색 흐름을 끊을 수 있으므로 기본 off로 시작한다.
- 수동 광고와 Auto ads를 함께 쓸 경우 중복 과밀 배치가 생기지 않는지 확인한다.

## 10. 측정 지표

주간 체크:

- Search Console clicks, impressions, CTR, average position
- GA4 page views, engaged sessions, country, device
- AdSense page RPM, impression RPM, viewability, invalid traffic warnings
- 상위 20개 글의 검색어
- impression은 높지만 CTR이 낮은 글
- position 8-20 사이에 있는 글

성장 기준:

| 기준 | 조치 |
| --- | --- |
| impression 높고 CTR 낮음 | title, excerpt, 첫 문단 개선 |
| position 8-20 | 예시, FAQ, 내부 링크 보강 |
| traffic 높고 RPM 낮음 | 광고 위치 A/B, 관련 글 연결 |
| bounce 높음 | quick fix 위치 상향, code block 개선 |
| 한국어만 유입 | 영어 제목과 slug 재점검 |

## 11. 실행 체크리스트

콘텐츠:

- [x] P0 40쌍 작성 후보를 이 문서에서 issue 또는 작업 목록으로 분리: `planning/p0-content-queue.md`
- [x] 약 100개 포스트 확장 큐 작성: `planning/100-post-multidomain-queue.md`
- [x] Study, Economy, AI Trends category page와 sidebar navigation 추가
- [x] 신규 글 작성 템플릿과 품질 체크리스트 작성: `planning/post-production-template.md`
- [x] 첫 번째 작성 스프린트용 P0 브리프 10개 작성: `planning/p0-content-briefs.md`
- [x] P0 브리프 기반 첫 포스트 쌍 작성: `python-pip-install-failed`
- [x] P0 브리프 기반 두 번째 포스트 쌍 작성: `python-no-module-named-pip`
- [x] P0 브리프 기반 세 번째 포스트 쌍 작성: `python-venv-not-activating`
- [x] P0 브리프 기반 네 번째 포스트 쌍 작성: `python-command-not-found-windows`
- [x] P0 브리프 기반 다섯 번째 포스트 쌍 작성: `python-externally-managed-environment`
- [x] P0 브리프 기반 여섯 번째 포스트 쌍 작성: `javascript-npm-err-eresolve`
- [x] P0 브리프 기반 일곱 번째 포스트 쌍 작성: `node-cannot-find-module`
- [x] P0 브리프 기반 여덟 번째 포스트 쌍 작성: `typescript-cannot-find-name`
- [x] P0 브리프 기반 아홉 번째 포스트 쌍 작성: `typescript-property-does-not-exist`
- [x] P0 브리프 기반 열 번째 포스트 쌍 작성: `typescript-tsconfig-paths-not-working`
- [x] Git/GitHub P0 포스트 쌍 작성: `github-actions-build-failed`
- [x] Git/GitHub P0 포스트 쌍 작성: `github-pages-jekyll-build-failed`
- [x] Troubleshooting 이미지 포함 포스트 쌍 작성: `git-fatal-authentication-failed`
- [x] Troubleshooting 이미지 포함 포스트 쌍 작성: `git-gh006-protected-branch`
- [x] Troubleshooting 이미지 포함 포스트 쌍 작성: `spring-boot-port-8080-already-in-use`
- [x] Troubleshooting 이미지 포함 포스트 쌍 작성: `docker-daemon-not-running`
- [x] Troubleshooting 이미지 포함 포스트 쌍 작성: `gradle-build-failed`
- [x] Troubleshooting 이미지 포함 포스트 쌍 작성: `maven-dependency-not-found`
- [x] Troubleshooting 이미지 포함 포스트 쌍 작성: `java-unsupported-class-file-major-version`
- [x] Troubleshooting 이미지 포함 포스트 쌍 작성: `vscode-python-interpreter-not-showing`
- [x] AI Trends 이미지 포함 포스트 쌍 작성: `ai-agent-workflow-2026`
- [x] AI Trends 이미지 포함 포스트 쌍 작성: `openai-responses-api-guide`
- [x] AI Trends 이미지 포함 포스트 쌍 작성: `ai-tools-function-calling`
- [x] AI Trends 이미지 포함 포스트 쌍 작성: `rag-evaluation-checklist`
- [x] AI Trends 이미지 포함 포스트 쌍 작성: `local-llm-vs-cloud-llm`
- [x] AI Trends 이미지 포함 포스트 쌍 작성: `prompt-engineering-checklist`
- [x] AI Trends 이미지 포함 포스트 쌍 작성: `ai-coding-agent-workflow`
- [x] AI Trends 이미지 포함 포스트 쌍 작성: `ai-search-optimization`
- [x] AI Trends 이미지 포함 포스트 쌍 작성: `ai-automation-roi`
- [x] AI Trends 이미지 포함 포스트 쌍 작성: `ai-meeting-notes-workflow`
- [x] Study 이미지 포함 포스트 쌍 작성: `active-recall-study-method`
- [x] Study 이미지 포함 포스트 쌍 작성: `spaced-repetition-schedule`
- [x] Study 이미지 포함 포스트 쌍 작성: `pomodoro-deep-work`
- [x] Study 이미지 포함 포스트 쌍 작성: `exam-mistake-note-system`
- [x] Study 이미지 포함 포스트 쌍 작성: `coding-study-roadmap`
- [x] Study 이미지 포함 포스트 쌍 작성: `english-vocabulary-system`
- [x] Study 이미지 포함 포스트 쌍 작성: `weekly-study-review`
- [x] Study 이미지 포함 포스트 쌍 작성: `notion-study-dashboard`
- [x] Economy 이미지 포함 포스트 쌍 작성: `compound-interest-example`
- [x] Economy 이미지 포함 포스트 쌍 작성: `etf-vs-mutual-fund`
- [x] Economy 이미지 포함 포스트 쌍 작성: `household-budget-50-30-20`
- [x] Economy 이미지 포함 포스트 쌍 작성: `emergency-fund-how-much`
- [x] Economy 이미지 포함 포스트 쌍 작성: `interest-rate-inflation-basics`
- [x] Economy 이미지 포함 포스트 쌍 작성: `exchange-rate-basics`
- [x] Economy 이미지 포함 포스트 쌍 작성: `recession-indicators-basics`
- [x] Easy Labeling 이미지 포함 포스트 쌍 작성: `yolo-label-format`
- [x] Easy Labeling 이미지 포함 포스트 쌍 작성: `coco-to-yolo-conversion`
- [x] Easy Labeling 이미지 포함 포스트 쌍 작성: `image-labeling-classes`
- [x] Easy Labeling 이미지 포함 포스트 쌍 작성: `local-image-labeling-workflow`
- [x] Easy Labeling 이미지 포함 포스트 쌍 작성: `easy-labeling-yolo-dataset`
- [x] Global Affairs 30쌍 작성 및 category hub 구성
- [x] Climate & Energy 38쌍 작성 및 category hub 구성
- [x] Consumer Rights 30쌍 작성 및 category hub 구성
- [x] Digital Security 30쌍 작성 및 category hub 구성
- [x] Personal Finance 30쌍 작성 및 category hub 구성
- [x] Health Literacy 30쌍 작성 및 category hub 구성
- [x] AI Trends 30쌍, Study 32쌍, Economy 36쌍, Easy Labeling 37쌍으로 확장
- [x] 각 글에 `lang`, `translation_id`, category, English tags 확인: `npm run validate:content-plan`
- [x] 신규 글마다 내부 링크 최소 2개 추가
- [x] Easy Labeling 글은 실제 화면과 launch link 포함

기술:

- [x] 현재 build 오류 여부 확인: `bundle exec jekyll build --trace`
- [x] Jekyll doctor 확인: `bundle exec jekyll doctor`
- [x] 최근 글 front matter delimiter 점검 및 opening delimiter 누락 포스트 보정
- [x] sitemap과 robots.txt 확인: `jekyll-sitemap` 설정 및 `robots.txt` 파일 존재 확인
- [x] AdSense script include 추가: `_includes/head/custom.html`
- [x] in-article ad include 추가: `_includes/ad-content.html`, `_includes/ad-inarticle.html`
- [x] 광고가 짧은 글과 archive page에 과도하게 나오지 않게 제한: posts only, `min_words_for_ads`, `page.ads != false`
- [x] 콘텐츠/광고/계획 검증 스크립트 추가: `npm run validate:content-plan`

운영:

- [x] Search Console 성과표 작성: `planning/weekly-performance-review-template.md`
- [x] AdSense 활성화 체크리스트 작성: `planning/adsense-rollout-checklist.md`
- [ ] 2주 단위로 키워드 우선순위 재정렬
- [ ] 4주 단위로 title/excerpt 개선
- [ ] 8주 단위로 pillar page 보강

## 12. 다음 작업 순서

1. Search Console과 GA4 데이터가 쌓이면 category별 impressions, CTR, position, landing page를 주 단위로 기록한다.
2. position 8-20에 있는 글부터 title, excerpt, 첫 문단, FAQ, 내부 링크를 보강한다.
3. AdSense slot ID가 준비되면 `_config.yml`의 `in_article_slot`, `post_bottom_slot`에 반영한다.
4. 신규 또는 수정 글마다 `npm run validate:content-plan`을 실행하고, 주요 field 단위 변경은 `bundle exec jekyll build --trace`로 닫는다.
5. 실제 query 기준으로 다음 확장 분야와 pillar page 우선순위를 다시 정렬한다.
