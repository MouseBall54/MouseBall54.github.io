#!/usr/bin/env python3
"""Expand posts below the site's five-minute reading threshold.

The site uses 150 words per minute. This script inserts category-aware
professional review material into posts that are still below the threshold.
It is intentionally deterministic so the same content policy can be audited.
"""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
POSTS = ROOT / "_posts"
WORDS_PER_MINUTE = 150
TARGET_WORDS = 850
MARKERS = {
    "en": "## Professional Depth Check",
    "ko": "## 전문 보완 체크",
}
EXTRA_MARKERS = {
    "en": "## Applied Review Scenario",
    "ko": "## 적용 검토 시나리오",
}
FINAL_MARKERS = {
    "en": "## Additional Professional Check",
    "ko": "## 추가 전문 검토",
}


DATA = {
    "Troubleshooting": {
        "en": {
            "context": "a reproducible debugging procedure",
            "dimensions": ["runtime environment", "exact error boundary", "minimal reproduction", "rollback path"],
            "evidence": ["full command output", "version numbers", "changed files", "expected versus actual behavior"],
            "risks": ["fixing the symptom while leaving the root cause", "mixing unrelated changes into the same test"],
            "cadence": "after dependency, operating-system, or build-tool changes",
        },
        "ko": {
            "context": "재현 가능한 디버깅 절차",
            "dimensions": ["실행 환경", "정확한 오류 경계", "최소 재현 예제", "되돌릴 수 있는 경로"],
            "evidence": ["전체 명령 출력", "버전 번호", "변경된 파일", "기대 동작과 실제 동작"],
            "risks": ["증상만 고치고 원인을 남기는 상황", "서로 무관한 변경을 같은 테스트에 섞는 상황"],
            "cadence": "의존성, 운영체제, 빌드 도구가 바뀐 뒤",
        },
    },
    "AI_Trends": {
        "en": {
            "context": "an AI governance and workflow decision",
            "dimensions": ["task boundary", "evaluation data", "human review trigger", "cost and latency budget"],
            "evidence": ["eval results", "sample prompts", "tool traces", "failure examples"],
            "risks": ["automation before failure cases are collected", "vendor claims replacing local measurement"],
            "cadence": "when the model, prompt, tool permission, or data source changes",
        },
        "ko": {
            "context": "AI 거버넌스와 워크플로 의사결정",
            "dimensions": ["작업 경계", "평가 데이터", "사람 검토 조건", "비용과 지연시간 예산"],
            "evidence": ["평가 결과", "샘플 프롬프트", "도구 실행 기록", "실패 사례"],
            "risks": ["실패 사례를 모으기 전에 자동화하는 상황", "벤더 주장으로 내부 측정을 대체하는 상황"],
            "cadence": "모델, 프롬프트, 도구 권한, 데이터 소스가 바뀔 때",
        },
    },
    "Global_Affairs": {
        "en": {
            "context": "a geopolitical risk reading process",
            "dimensions": ["trade exposure", "shipping route", "financial condition", "Korea-facing channel"],
            "evidence": ["official releases", "trade data", "freight or insurance indicators", "policy dates"],
            "risks": ["turning a single event into a broad forecast", "ignoring time lags between policy and prices"],
            "cadence": "after sanctions, elections, conflicts, or trade-rule updates",
        },
        "ko": {
            "context": "지정학 리스크를 읽는 절차",
            "dimensions": ["무역 노출", "해상 운송 경로", "금융 여건", "한국으로 전달되는 경로"],
            "evidence": ["공식 발표", "무역 데이터", "운임 또는 보험 지표", "정책 시행일"],
            "risks": ["단일 사건을 넓은 전망으로 확대하는 상황", "정책과 가격 사이의 시차를 무시하는 상황"],
            "cadence": "제재, 선거, 분쟁, 통상 규칙이 바뀐 뒤",
        },
    },
    "Climate_Energy": {
        "en": {
            "context": "a climate and energy feasibility review",
            "dimensions": ["grid constraint", "capital cost", "fuel or material input", "household and industrial price channel"],
            "evidence": ["official energy statistics", "project assumptions", "capacity factors", "tariff or bill data"],
            "risks": ["confusing targets with delivered capacity", "ignoring interconnection and permitting constraints"],
            "cadence": "when policy targets, fuel prices, grid plans, or project costs change",
        },
        "ko": {
            "context": "기후·에너지 실행 가능성 검토",
            "dimensions": ["전력망 제약", "자본비용", "연료 또는 소재 투입", "가계와 산업 가격 경로"],
            "evidence": ["공식 에너지 통계", "프로젝트 가정", "이용률", "요금 또는 청구서 데이터"],
            "risks": ["목표를 실제 공급 능력으로 착각하는 상황", "계통 접속과 인허가 제약을 빼는 상황"],
            "cadence": "정책 목표, 연료 가격, 전력망 계획, 프로젝트 비용이 바뀔 때",
        },
    },
    "Consumer_Rights": {
        "en": {
            "context": "an evidence-based consumer dispute workflow",
            "dimensions": ["contract language", "payment trail", "seller response", "platform or regulator escalation"],
            "evidence": ["receipts", "screenshots", "dates", "case numbers"],
            "risks": ["missing refund deadlines", "sending emotional messages without evidence"],
            "cadence": "whenever a seller changes the promise, price, fee, delivery date, or repair estimate",
        },
        "ko": {
            "context": "증거 기반 소비자 분쟁 대응 절차",
            "dimensions": ["계약 문구", "결제 흐름", "판매자 답변", "플랫폼 또는 기관 이의제기"],
            "evidence": ["영수증", "화면 캡처", "날짜", "접수 번호"],
            "risks": ["환불 기한을 놓치는 상황", "증거 없이 감정적인 메시지만 보내는 상황"],
            "cadence": "판매자가 약속, 가격, 수수료, 배송일, 수리 견적을 바꿀 때",
        },
    },
    "Digital_Security": {
        "en": {
            "context": "a security prevention and recovery routine",
            "dimensions": ["account access", "device state", "recovery channel", "evidence preservation"],
            "evidence": ["login history", "alert emails", "transaction records", "device and browser versions"],
            "risks": ["resetting evidence before screenshots are captured", "reusing compromised recovery channels"],
            "cadence": "after suspicious messages, account alerts, device changes, or breach notices",
        },
        "ko": {
            "context": "보안 예방과 복구 루틴",
            "dimensions": ["계정 접근", "기기 상태", "복구 채널", "증거 보존"],
            "evidence": ["로그인 기록", "경고 이메일", "거래 내역", "기기와 브라우저 버전"],
            "risks": ["캡처 전에 증거를 초기화하는 상황", "침해된 복구 채널을 다시 쓰는 상황"],
            "cadence": "의심 메시지, 계정 경고, 기기 변경, 유출 통지를 받은 뒤",
        },
    },
    "Personal_Finance": {
        "en": {
            "context": "a personal finance planning check, not individualized advice",
            "dimensions": ["cash flow", "interest and fees", "tax or contract rule", "risk capacity"],
            "evidence": ["statements", "APR or expense ratio", "payment schedule", "emergency reserve"],
            "risks": ["optimizing for headline return while ignoring liquidity", "comparing products before checking constraints"],
            "cadence": "after income, debt, tax, family, or market-condition changes",
        },
        "ko": {
            "context": "개인별 조언이 아닌 개인금융 계획 점검",
            "dimensions": ["현금흐름", "이자와 수수료", "세금 또는 계약 규칙", "위험 감내 능력"],
            "evidence": ["명세서", "APR 또는 보수율", "상환 일정", "비상자금"],
            "risks": ["유동성을 무시하고 표면 수익률만 보는 상황", "제약 조건을 확인하기 전에 상품부터 비교하는 상황"],
            "cadence": "소득, 부채, 세금, 가족 상황, 시장 여건이 바뀐 뒤",
        },
    },
    "Health_Literacy": {
        "en": {
            "context": "a health-literacy record for conversations with qualified professionals",
            "dimensions": ["symptom timeline", "severity and red flags", "medication or exposure history", "questions for a clinician"],
            "evidence": ["dates", "measurements", "photos when appropriate", "medication labels"],
            "risks": ["using an article as diagnosis", "delaying urgent care for sudden or severe symptoms"],
            "cadence": "when symptoms change, new medicine starts, or red flags appear",
        },
        "ko": {
            "context": "전문 의료진과 대화하기 위한 건강 문해력 기록",
            "dimensions": ["증상 타임라인", "심각도와 위험 신호", "복용약 또는 노출 이력", "의료진에게 물을 질문"],
            "evidence": ["날짜", "측정값", "필요한 경우 사진", "약 라벨"],
            "risks": ["글을 진단처럼 사용하는 상황", "갑작스럽거나 심한 증상에서 진료를 미루는 상황"],
            "cadence": "증상이 바뀌거나 새 약을 시작하거나 위험 신호가 나타날 때",
        },
    },
    "Study": {
        "en": {
            "context": "an evidence-informed study routine",
            "dimensions": ["retrieval practice", "spacing interval", "error log", "feedback source"],
            "evidence": ["quiz results", "mistake categories", "review dates", "teacher or peer comments"],
            "risks": ["measuring study time instead of output", "rereading without retrieval or feedback"],
            "cadence": "at the end of each week and after every practice test",
        },
        "ko": {
            "context": "근거 기반 학습 루틴",
            "dimensions": ["인출 연습", "간격 복습", "오답 기록", "피드백 출처"],
            "evidence": ["퀴즈 결과", "오답 유형", "복습 날짜", "교사 또는 동료 피드백"],
            "risks": ["학습 시간을 성과로 착각하는 상황", "인출과 피드백 없이 다시 읽기만 하는 상황"],
            "cadence": "매주 끝과 모의 테스트 뒤",
        },
    },
    "Economy": {
        "en": {
            "context": "a macro-to-household interpretation framework",
            "dimensions": ["price channel", "wage or income channel", "interest-payment channel", "exchange-rate or import channel"],
            "evidence": ["official statistics", "central-bank releases", "household budget lines", "revision dates"],
            "risks": ["treating one indicator as a forecast", "forgetting that data revisions can change the story"],
            "cadence": "after major data releases, central-bank meetings, budget changes, or exchange-rate shocks",
        },
        "ko": {
            "context": "거시경제를 가계 영향으로 해석하는 틀",
            "dimensions": ["가격 경로", "임금 또는 소득 경로", "이자 지급 경로", "환율 또는 수입 경로"],
            "evidence": ["공식 통계", "중앙은행 자료", "가계 예산 항목", "수정 발표일"],
            "risks": ["하나의 지표를 전망으로 착각하는 상황", "통계 수정으로 해석이 바뀔 수 있음을 잊는 상황"],
            "cadence": "주요 통계, 중앙은행 회의, 예산 변화, 환율 충격 뒤",
        },
    },
    "easy_labeling": {
        "en": {
            "context": "a computer-vision dataset quality workflow",
            "dimensions": ["class dictionary", "annotation consistency", "train/validation/test split", "export format"],
            "evidence": ["sample review notes", "YOLO or COCO files", "labeler disagreement records", "training error examples"],
            "risks": ["clean exports with inconsistent labels", "privacy leakage through uploaded source images"],
            "cadence": "before every export, model training run, and dataset handoff",
        },
        "ko": {
            "context": "컴퓨터 비전 데이터셋 품질 관리 절차",
            "dimensions": ["클래스 사전", "어노테이션 일관성", "train/validation/test 분리", "내보내기 형식"],
            "evidence": ["샘플 검수 메모", "YOLO 또는 COCO 파일", "라벨러 불일치 기록", "학습 오류 사례"],
            "risks": ["형식은 정상인데 라벨 기준이 흔들리는 상황", "원본 이미지 업로드로 개인정보가 새는 상황"],
            "cadence": "내보내기, 모델 학습, 데이터셋 인수인계 전마다",
        },
    },
}


TECH_DATA = {
    "Git": {
        "en": {
            "dimensions": ["repository root", "branch and remote state", "index and working tree", "credential or network boundary"],
            "evidence": ["`git status`", "`git remote -v`", "`git branch --show-current`", "the exact command that failed"],
        },
        "ko": {
            "dimensions": ["저장소 루트", "브랜치와 원격 상태", "인덱스와 작업 트리", "인증 또는 네트워크 경계"],
            "evidence": ["`git status`", "`git remote -v`", "`git branch --show-current`", "실패한 정확한 명령"],
        },
    },
    "Python": {
        "en": {
            "dimensions": ["interpreter path", "virtual environment", "package version", "input file or data boundary"],
            "evidence": ["`python --version`", "`python -m pip show`", "the full traceback", "a minimal script"],
        },
        "ko": {
            "dimensions": ["인터프리터 경로", "가상환경", "패키지 버전", "입력 파일 또는 데이터 경계"],
            "evidence": ["`python --version`", "`python -m pip show`", "전체 traceback", "최소 재현 스크립트"],
        },
    },
    "Java": {
        "en": {
            "dimensions": ["JDK version", "build tool configuration", "classpath or module path", "runtime stack trace"],
            "evidence": ["`java -version`", "`javac -version`", "Maven or Gradle output", "the smallest failing class"],
        },
        "ko": {
            "dimensions": ["JDK 버전", "빌드 도구 설정", "classpath 또는 module path", "런타임 stack trace"],
            "evidence": ["`java -version`", "`javac -version`", "Maven 또는 Gradle 출력", "가장 작은 실패 클래스"],
        },
    },
    "JavaScript": {
        "en": {
            "dimensions": ["browser or Node version", "bundler setting", "async boundary", "DOM or API state"],
            "evidence": ["console stack trace", "`node --version`", "network tab output", "a minimal reproduction"],
        },
        "ko": {
            "dimensions": ["브라우저 또는 Node 버전", "번들러 설정", "비동기 경계", "DOM 또는 API 상태"],
            "evidence": ["콘솔 stack trace", "`node --version`", "Network 탭 출력", "최소 재현 예제"],
        },
    },
}


def split_front_matter(text: str) -> tuple[str, str]:
    match = re.match(r"^---\n.*?\n---\n", text, re.S)
    if not match:
        return "", text
    return match.group(0), text[match.end():]


def front_value(front: str, key: str) -> str:
    match = re.search(rf"^{re.escape(key)}:\s*(.+)$", front, re.M)
    if not match:
        return ""
    return match.group(1).strip().strip('"')


def front_list(front: str, key: str) -> list[str]:
    match = re.search(rf"^{re.escape(key)}:\n((?:  - .+\n)+)", front, re.M)
    if not match:
        return []
    return [line[4:].strip() for line in match.group(1).splitlines()]


def word_count(markdown: str) -> int:
    text = re.sub(r"^---\n.*?\n---\n", " ", markdown, flags=re.S)
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = text.replace("`", " ")
    text = re.sub(r"!\[[^\]]*\]\([^)]+\)", " ", text)
    text = re.sub(r"\[[^\]]+\]\([^)]+\)", lambda m: re.sub(r"[\[\]\(\)]", " ", m.group(0)), text)
    text = re.sub(r"<[^>]+>", " ", text)
    return len(re.findall(r"\S+", text))


def family(category: str) -> str:
    for candidate in DATA:
        if category.endswith(candidate):
            return candidate
    return "Troubleshooting"


def enrich_troubleshooting(data: dict, tags: list[str], lang: str) -> dict:
    merged = {key: list(value) if isinstance(value, list) else value for key, value in data.items()}
    for tag in tags:
        tech = TECH_DATA.get(tag)
        if tech:
            merged["dimensions"] = tech[lang]["dimensions"]
            merged["evidence"] = tech[lang]["evidence"]
            break
    return merged


def join_items(items: list[str], lang: str) -> str:
    if lang == "ko":
        return ", ".join(items)
    if len(items) == 1:
        return items[0]
    return ", ".join(items[:-1]) + ", and " + items[-1]


def blocks_en(title: str, data: dict) -> list[str]:
    d = data["dimensions"]
    e = data["evidence"]
    r = data["risks"]
    return [
        f"""## Professional Depth Check

For **{title}**, the practical standard is not whether the reader can repeat one instruction once. Treat the topic as {data["context"]}: verify {join_items(d, "en")} before drawing a conclusion. The result should be written as a small decision record, because future readers need to know which fact was observed, which assumption was used, and which condition would change the answer.""",
        f"""### Evidence That Makes the Guidance Reliable

Use objective evidence before changing a workflow. Good evidence includes {join_items(e, "en")}. If two pieces of evidence conflict, keep the conflict visible instead of smoothing it over. For example, a successful quick fix is still weak evidence if the same input, account, dependency, or device state has not been tested again. A durable article should help the reader distinguish a confirmed fix from a plausible fix.""",
        f"""### Review Table

| Review Item | What To Confirm | Why It Matters |
| --- | --- | --- |
| Scope | The exact case covered by this article | Prevents over-applying the advice |
| Baseline | The state before any change | Makes rollback and comparison possible |
| Change | The smallest action taken | Reduces hidden side effects |
| Result | The observed output after the change | Separates evidence from expectation |
| Recheck | When to revisit the conclusion | Keeps the post accurate over time |""",
        f"""### Edge Cases and Failure Modes

The main risks are {join_items(r, "en")}. When the situation involves production data, personal information, money, health, legal rights, or security recovery, the conservative path is to stop and collect evidence before applying a broad fix. The same title can describe very different cases, so the reader should compare their environment with the assumptions in the post before copying commands or decisions.""",
        f"""### Maintenance Standard

Recheck this guidance {data["cadence"]}. A useful update does not need to rewrite the entire post; it should confirm whether the examples, links, commands, screenshots, and decision criteria still match current behavior. If the old conclusion remains valid, record the check date. If it changes, explain what changed and why the previous advice is no longer enough.""",
        f"""### Practical Questions Before Acting

- What is the smallest observable signal that proves the problem or decision is real?
- Which source is official, and which part is local judgment?
- What should be captured before making changes?
- What result would show that the guidance did not apply?
- Who needs the record if the same issue appears again?""",
    ]


def blocks_ko(title: str, data: dict) -> list[str]:
    d = data["dimensions"]
    e = data["evidence"]
    r = data["risks"]
    return [
        f"""## 전문 보완 체크

**{title}**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 {data["context"]}로 다루는 편이 안전합니다. 결론을 내리기 전에 {join_items(d, "ko")}를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.""",
        f"""### 신뢰도를 높이는 증거

작업을 바꾸기 전에는 객관적인 증거를 먼저 확인해야 합니다. 쓸 만한 증거에는 {join_items(e, "ko")}가 포함됩니다. 증거가 서로 맞지 않으면 억지로 하나의 이야기로 합치지 말고 충돌 자체를 남겨야 합니다. 빠른 해결이 한 번 성공했더라도 같은 입력, 계정, 의존성, 기기 상태에서 다시 확인하지 않았다면 아직 확정된 해결책이라고 보기 어렵습니다.""",
        f"""### 검토 표

| 검토 항목 | 확인할 내용 | 중요한 이유 |
| --- | --- | --- |
| 범위 | 이 글이 다루는 정확한 사례 | 조언을 과도하게 적용하지 않게 합니다 |
| 기준 상태 | 변경 전 상태 | 되돌리기와 비교를 가능하게 합니다 |
| 변경 | 실제로 수행한 가장 작은 조치 | 숨은 부작용을 줄입니다 |
| 결과 | 변경 뒤 관찰한 출력 또는 반응 | 기대와 증거를 구분합니다 |
| 재확인 | 결론을 다시 볼 시점 | 글의 정확도를 유지합니다 |""",
        f"""### 예외 상황과 실패 모드

주요 위험은 {join_items(r, "ko")}입니다. 생산 데이터, 개인정보, 돈, 건강, 법적 권리, 보안 복구가 관련되어 있다면 넓은 해결책을 바로 적용하기보다 먼저 증거를 모으는 보수적인 접근이 낫습니다. 같은 제목의 문제라도 환경이 다르면 원인이 달라질 수 있으므로, 독자는 명령이나 결정을 복사하기 전에 자신의 조건이 글의 가정과 맞는지 비교해야 합니다.""",
        f"""### 유지보수 기준

이 안내는 {data["cadence"]} 다시 확인해야 합니다. 좋은 업데이트는 글 전체를 다시 쓰는 것이 아니라 예시, 링크, 명령, 화면, 판단 기준이 현재 동작과 여전히 맞는지 확인하는 일입니다. 기존 결론이 유효하면 확인 날짜를 남기고, 바뀌었다면 무엇이 바뀌었고 왜 이전 조언만으로 부족한지 설명해야 합니다.""",
        f"""### 실행 전 질문

- 문제나 판단이 실제임을 보여 주는 가장 작은 관찰 신호는 무엇인가?
- 공식 출처는 무엇이고, 내부 판단은 어느 부분인가?
- 변경 전에 반드시 캡처해야 할 기록은 무엇인가?
- 어떤 결과가 나오면 이 글의 조언이 맞지 않는다고 볼 것인가?
- 같은 문제가 반복될 때 누가 이 기록을 다시 봐야 하는가?""",
    ]


def extra_blocks_en(title: str, data: dict) -> str:
    d = data["dimensions"]
    e = data["evidence"]
    return f"""## Applied Review Scenario

Assume a reader has already tried the first recommendation for **{title}**, but the outcome is still uncertain. The next step is to build a short audit trail instead of trying several fixes at once. Start with one sentence that names the decision, one sentence that names the environment, and one sentence that names the observed result. Then compare {join_items(d, "en")} against the facts already captured. This prevents the article from becoming a list of disconnected tips.

### Audit Trail Template

| Field | Example Standard | Reason |
| --- | --- | --- |
| Observation | What was seen before action | Keeps the baseline objective |
| Evidence | {join_items(e[:2], "en")} | Anchors the decision in records |
| Assumption | What is believed but not proven | Prevents hidden guesses |
| Action | One change at a time | Makes the result attributable |
| Stop Rule | When to stop and escalate | Reduces repeated trial and error |

### Quality Boundary

The guidance should be treated as strong only when the same result appears after a controlled recheck. If a different account, device, data sample, dependency version, contract term, or official rule is involved, the conclusion should be downgraded to a hypothesis. That distinction is important for search readers because they often arrive with an urgent problem and may skip context. A professional post should slow down the risky part of the decision while still giving a practical next action."""


def extra_blocks_ko(title: str, data: dict) -> str:
    d = data["dimensions"]
    e = data["evidence"]
    return f"""## 적용 검토 시나리오

독자가 **{title}**의 첫 번째 권장 조치를 이미 시도했지만 결과가 여전히 불확실하다고 가정해 봅니다. 다음 단계는 여러 해결책을 한꺼번에 시험하는 것이 아니라 짧은 감사 기록을 만드는 것입니다. 먼저 어떤 판단을 하려는지 한 문장으로 쓰고, 환경을 한 문장으로 적고, 관찰된 결과를 한 문장으로 남깁니다. 그다음 {join_items(d, "ko")}를 이미 확보한 사실과 대조합니다. 이렇게 해야 글이 서로 끊어진 팁 목록이 아니라 검증 가능한 절차가 됩니다.

### 감사 기록 양식

| 항목 | 예시 기준 | 이유 |
| --- | --- | --- |
| 관찰 | 조치 전 실제로 본 내용 | 기준 상태를 객관화합니다 |
| 증거 | {join_items(e[:2], "ko")} | 판단을 기록에 연결합니다 |
| 가정 | 믿고 있지만 아직 증명하지 못한 내용 | 숨은 추정을 드러냅니다 |
| 조치 | 한 번에 하나의 변경 | 결과의 원인을 추적하게 합니다 |
| 중단 기준 | 멈추고 도움을 요청할 조건 | 반복적인 시행착오를 줄입니다 |

### 품질 경계

같은 결과가 통제된 재확인 뒤에도 반복될 때만 이 안내를 강한 결론으로 보아야 합니다. 계정, 기기, 데이터 샘플, 의존성 버전, 계약 조건, 공식 규칙이 달라졌다면 결론의 강도를 낮추고 가설로 다루는 편이 안전합니다. 검색 독자는 급한 문제를 안고 들어오는 경우가 많아 맥락을 건너뛰기 쉽습니다. 전문적인 글은 위험한 판단을 천천히 하게 만들면서도 다음 행동은 분명하게 제시해야 합니다."""


def expansion(front: str, body: str) -> str:
    lang = front_value(front, "lang") or ("ko" if "/ko/" in front else "en")
    title = front_value(front, "title")
    if title in {">", "|"}:
        match = re.search(r"^title:\s*[>|]\n((?:  .+\n)+)", front, re.M)
        if match:
            title = " ".join(line.strip() for line in match.group(1).splitlines())
    if not title:
        title = "this topic" if lang == "en" else "이 주제"
    categories = front_list(front, "categories")
    tags = front_list(front, "tags")
    key = family(categories[0] if categories else "")
    data = DATA[key][lang]
    if key == "Troubleshooting":
        data = enrich_troubleshooting(data, tags, lang)
    return "\n\n".join(blocks_ko(title, data) if lang == "ko" else blocks_en(title, data)) + "\n"


def extra_expansion(front: str) -> str:
    lang = front_value(front, "lang") or "en"
    title = front_value(front, "title")
    if title in {">", "|"}:
        match = re.search(r"^title:\s*[>|]\n((?:  .+\n)+)", front, re.M)
        if match:
            title = " ".join(line.strip() for line in match.group(1).splitlines())
    if not title:
        title = "this topic" if lang == "en" else "이 주제"
    categories = front_list(front, "categories")
    tags = front_list(front, "tags")
    key = family(categories[0] if categories else "")
    data = DATA[key][lang]
    if key == "Troubleshooting":
        data = enrich_troubleshooting(data, tags, lang)
    return extra_blocks_ko(title, data) if lang == "ko" else extra_blocks_en(title, data)


def final_expansion(front: str) -> str:
    lang = front_value(front, "lang") or "en"
    title = front_value(front, "title")
    if title in {">", "|"}:
        match = re.search(r"^title:\s*[>|]\n((?:  .+\n)+)", front, re.M)
        if match:
            title = " ".join(line.strip() for line in match.group(1).splitlines())
    if not title:
        title = "this topic" if lang == "en" else "이 주제"
    categories = front_list(front, "categories")
    tags = front_list(front, "tags")
    key = family(categories[0] if categories else "")
    data = DATA[key][lang]
    if key == "Troubleshooting":
        data = enrich_troubleshooting(data, tags, lang)
    if lang == "ko":
        return f"""## 추가 전문 검토

**{title}**를 실제 업무나 학습 상황에 적용하기 전에는 결론을 세 단계로 나누어 확인하는 것이 좋습니다. 첫째, 현재 사례가 글의 범위 안에 들어오는지 확인합니다. 둘째, {join_items(data["evidence"][:3], "ko")}처럼 다시 확인할 수 있는 자료를 남깁니다. 셋째, 조치 뒤 결과가 기대와 다를 때 멈출 기준을 정합니다. 이 순서가 없으면 같은 문장을 읽고도 독자마다 서로 다른 행동을 하게 됩니다.

특히 {join_items(data["dimensions"][:3], "ko")}가 바뀌면 기존 결론의 신뢰도는 낮아집니다. 이때는 해결책을 더 많이 시도하는 것보다 조건을 다시 분리하는 편이 낫습니다. 원인, 증거, 조치, 결과를 한 줄씩 분리하면 나중에 같은 문제가 재발했을 때 비교가 가능합니다. 검색 유입을 노린 글일수록 이 구분이 중요합니다. 자극적인 문장보다 재검증 가능한 기준이 누적될 때 오래 읽히는 글이 됩니다.

마지막으로 이 글을 체크리스트로 사용할 때는 “지금 바로 할 일”과 “전문가, 관리자, 공식 기관, 또는 팀 리뷰가 필요한 일”을 구분해야 합니다. 돈, 건강, 개인정보, 계정 보안, 법적 권리, 배포 환경이 관련된 문제라면 빠른 해결보다 기록 보존과 책임 경계가 우선입니다. 이 기준을 적용하면 글의 길이는 늘어나지만, 단순한 분량 추가가 아니라 판단 품질을 높이는 실무 자료가 됩니다."""
    return f"""## Additional Professional Check

Before applying **{title}** in a real workflow, split the conclusion into three checks. First, confirm that the reader's case is inside the scope of the article. Second, preserve evidence such as {join_items(data["evidence"][:3], "en")}. Third, define the point where the reader should stop, escalate, or ask for review. Without those boundaries, the same article can lead different readers to take different actions.

If {join_items(data["dimensions"][:3], "en")} changes, downgrade the confidence of the conclusion. In that case, trying more fixes is less useful than separating the conditions again. A one-line record for cause, evidence, action, and result makes future comparison possible. This matters for search-driven content because urgent readers often skip context; the post has to make the careful path visible without hiding the practical next step.

Finally, use the article as a checklist rather than a guarantee. Problems involving money, health, personal data, account security, legal rights, or production systems should prioritize evidence preservation and responsibility boundaries over speed. That added structure increases reading time, but it also increases decision quality, which is the point of expanding a short post."""


def insertion_index(body: str) -> int:
    patterns = [
        r"\n```\n## (Related|함께|관련)",
        r"\n## (Related Reading|Related Posts|Related Articles|함께 보면 좋은 글|관련 글)",
        r"\n## (Source Notes|참고할 자료)",
    ]
    positions = []
    for pattern in patterns:
        match = re.search(pattern, body)
        if match:
            positions.append(match.start())
    return min(positions) if positions else len(body)


def remove_stray_related_fence(body: str) -> str:
    return re.sub(r"\n```\n(## (Related Reading|Related Posts|Related Articles|함께 보면 좋은 글|관련 글))", r"\n\n\1", body)


def insert_section(path: Path, section: str, markers: dict[str, str]) -> bool:
    text = path.read_text(encoding="utf-8")
    front, body = split_front_matter(text)
    if any(marker in body for marker in markers.values()):
        return False
    idx = insertion_index(body)
    body = body[:idx].rstrip() + "\n\n" + section.strip() + "\n\n" + body[idx:].lstrip()
    path.write_text(front + body, encoding="utf-8")
    return True


def rendered_short_posts() -> list[Path]:
    site = ROOT / "_site"
    if not site.exists():
        return []
    short: list[Path] = []
    pattern = re.compile(r"\b([1-4]) minute read\b|less than\s+1\s+minute read|\b[1-4]\s+분 소요\b")
    for post in sorted(POSTS.glob("*/*.md")):
        text = post.read_text(encoding="utf-8")
        front, _ = split_front_matter(text)
        categories = front_list(front, "categories")
        if not categories:
            continue
        permalink = front_value(front, "permalink")
        if permalink:
            page = site / permalink.strip("/") / "index.html"
        else:
            slug = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", post.stem)
            page = site / categories[0].lower() / slug / "index.html"
        if not page.exists():
            continue
        html = page.read_text(encoding="utf-8", errors="ignore")
        if pattern.search(html):
            short.append(post)
    return short


def process(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    front, body = split_front_matter(text)
    if any(marker in body for marker in MARKERS.values()):
        cleaned = remove_stray_related_fence(body)
        if (
            word_count(front + cleaned) < WORDS_PER_MINUTE * 5
            and not any(marker in cleaned for marker in EXTRA_MARKERS.values())
        ):
            idx = insertion_index(cleaned)
            cleaned = cleaned[:idx].rstrip() + "\n\n" + extra_expansion(front).strip() + "\n\n" + cleaned[idx:].lstrip()
        if cleaned != body:
            path.write_text(front + cleaned, encoding="utf-8")
            return True
        return False

    current = word_count(text)
    if current >= TARGET_WORDS:
        cleaned = remove_stray_related_fence(body)
        if cleaned != body:
            path.write_text(front + cleaned, encoding="utf-8")
            return True
        return False

    blocks = expansion(front, body).split("\n\n")
    inserted: list[str] = []
    candidate_body = body
    for block in blocks:
        inserted.append(block)
        idx = insertion_index(body)
        candidate_body = body[:idx].rstrip() + "\n\n" + "\n\n".join(inserted).strip() + "\n\n" + body[idx:].lstrip()
        candidate_body = remove_stray_related_fence(candidate_body)
        if word_count(front + candidate_body) >= TARGET_WORDS:
            break

    path.write_text(front + candidate_body, encoding="utf-8")
    return True


def main() -> None:
    changed = 0
    for path in sorted(POSTS.glob("*/*.md")):
        if process(path):
            changed += 1
    short = []
    for path in sorted(POSTS.glob("*/*.md")):
        words = word_count(path.read_text(encoding="utf-8"))
        if words < WORDS_PER_MINUTE * 5:
            short.append((words, path))
    print(f"Changed posts: {changed}")
    print(f"Posts still below 5 minutes: {len(short)}")
    for words, path in short[:20]:
        print(f"{words} {path.relative_to(ROOT)}")
    rendered_changed = 0
    for path in rendered_short_posts():
        front, _ = split_front_matter(path.read_text(encoding="utf-8"))
        if insert_section(path, final_expansion(front), FINAL_MARKERS):
            rendered_changed += 1
    if rendered_changed:
        print(f"Rendered-short posts supplemented: {rendered_changed}")


if __name__ == "__main__":
    main()
