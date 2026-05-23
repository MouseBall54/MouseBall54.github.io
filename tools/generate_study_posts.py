#!/usr/bin/env python3
"""Generate paired Study posts and local PNG context images."""

from __future__ import annotations

import struct
import zlib
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parents[1]
POST_DATE = "2026-05-23"
LAST_MODIFIED_AT = "2026-05-23T23:58:00+09:00"
KO_CATEGORY = "ko_Study"
EN_CATEGORY = "en_Study"


SOURCES = {
    "ies_guide": {
        "ko": "IES What Works Clearinghouse Study Guide",
        "en": "IES What Works Clearinghouse Study Guide",
        "url": "https://ies.ed.gov/ncee/wwc/PracticeGuide/1",
    },
    "ies_pdf": {
        "ko": "IES Organizing Instruction and Study PDF",
        "en": "IES Organizing Instruction and Study PDF",
        "url": "https://ies.ed.gov/ncee/WWC/Docs/PracticeGuide/20072004.pdf",
    },
    "eef_metacognition": {
        "ko": "EEF Metacognition and Self-Regulation",
        "en": "EEF Metacognition and Self-Regulation",
        "url": "https://educationendowmentfoundation.org.uk/education-evidence/evidence-reviews/metacognition-and-self-regulation",
    },
    "cdc_sleep": {
        "ko": "CDC About Sleep",
        "en": "CDC About Sleep",
        "url": "https://www.cdc.gov/sleep/about/index.html",
    },
    "medline_sleep": {
        "ko": "NIH MedlinePlus Healthy Sleep",
        "en": "NIH MedlinePlus Healthy Sleep",
        "url": "https://medlineplus.gov/healthysleep.html",
    },
    "python_start": {
        "ko": "Python.org Getting Started",
        "en": "Python.org Getting Started",
        "url": "https://www.python.org/about/gettingstarted/",
    },
    "mdn_learn": {
        "ko": "MDN Learn Web Development",
        "en": "MDN Learn Web Development",
        "url": "https://developer.mozilla.org/en-US/docs/Learn",
    },
    "git_book": {
        "ko": "Pro Git Book",
        "en": "Pro Git Book",
        "url": "https://git-scm.com/book/en/v2",
    },
    "cornell_notes": {
        "ko": "Cornell Learning Strategies Center Note Taking",
        "en": "Cornell Learning Strategies Center Note Taking",
        "url": "https://lsc.cornell.edu/study-skills/cornell-note-taking-system/",
    },
    "purdue_paraphrase": {
        "ko": "Purdue OWL Paraphrasing",
        "en": "Purdue OWL Paraphrasing",
        "url": "https://owl.purdue.edu/owl/research_and_citation/using_research/quoting_paraphrasing_and_summarizing/paraphrasing.html",
    },
    "purdue_writing": {
        "ko": "Purdue OWL Academic Writing",
        "en": "Purdue OWL Academic Writing",
        "url": "https://owl.purdue.edu/owl/general_writing/academic_writing/index.html",
    },
    "ucsd_spaced": {
        "ko": "UC San Diego Spaced Practice",
        "en": "UC San Diego Spaced Practice",
        "url": "https://psychology.ucsd.edu/undergraduate-program/undergraduate-resources/academic-writing-resources/effective-studying/spaced-practice.html",
    },
    "indiana_spaced": {
        "ko": "Indiana University Spaced Practice",
        "en": "Indiana University Spaced Practice",
        "url": "https://citl.indiana.edu/teaching-resources/evidence-based/spaced-practice.html",
    },
    "harvard_arc": {
        "ko": "Harvard Academic Resource Center",
        "en": "Harvard Academic Resource Center",
        "url": "https://academicresourcecenter.harvard.edu/resources/",
    },
}


TOPICS = [
    {
        "slug": "active-recall-study-method",
        "ko_title": "Active Recall 공부법: 읽은 내용을 덮고 꺼내 쓰는 루틴",
        "en_title": "Active Recall Study Method: Close the Book and Retrieve",
        "ko_summary": "Active recall은 다시 읽기보다 기억에서 답을 꺼내는 과정으로, 시험과 실무 적용 모두에서 학습 상태를 더 분명히 보여 준다.",
        "en_summary": "Active recall replaces passive rereading with retrieval, making it clearer whether you can use knowledge in exams or real work.",
        "ko_focus": "핵심은 많이 보는 것이 아니라 힌트 없이 설명하고, 틀린 지점을 다시 공부하는 루프를 만드는 것입니다.",
        "en_focus": "The point is not looking at material more often; it is explaining without cues and restudying the failure point.",
        "ko_actions": ["교재를 덮고 핵심 질문 5개에 답합니다.", "틀린 답을 표시하고 원문으로 돌아갑니다.", "다음 복습 날짜를 바로 정합니다."],
        "en_actions": ["Close the material and answer five core questions.", "Mark wrong answers and return to the source.", "Schedule the next review immediately."],
        "signals": ["retrieval question", "wrong answer", "source check", "review date"],
        "ko_signals": ["회상 질문", "오답", "원문 확인", "복습 날짜"],
        "sources": ["ies_guide", "ies_pdf", "eef_metacognition"],
        "tags": ["ActiveRecall", "StudySkills", "Memory", "Learning"],
    },
    {
        "slug": "spaced-repetition-schedule",
        "ko_title": "Spaced Repetition 복습 일정: 몰아보기보다 간격을 설계하기",
        "en_title": "Spaced Repetition Schedule: Design Gaps Instead of Cramming",
        "ko_summary": "Spaced repetition은 같은 시간을 한 번에 쓰는 대신 며칠과 몇 주에 나누어 복습해 장기 기억을 목표로 한다.",
        "en_summary": "Spaced repetition spreads review across days and weeks so the same study time is aimed at longer-term retention.",
        "ko_focus": "복습 간격은 완벽한 공식보다 놓치지 않고 다시 꺼내 보는 달력으로 작동해야 합니다.",
        "en_focus": "A spacing plan should work as a calendar for retrieval, not as a perfect formula.",
        "ko_actions": ["처음 배운 날, 다음 날, 1주 뒤, 3주 뒤 복습을 잡습니다.", "쉬운 항목은 간격을 늘립니다.", "틀린 항목은 간격을 다시 좁힙니다."],
        "en_actions": ["Review on the study day, next day, one week later, and three weeks later.", "Increase gaps for easy items.", "Shorten gaps for missed items."],
        "signals": ["review interval", "recall score", "easy item", "missed item"],
        "ko_signals": ["복습 간격", "회상 점수", "쉬운 항목", "틀린 항목"],
        "sources": ["ies_guide", "ucsd_spaced", "indiana_spaced"],
        "tags": ["SpacedRepetition", "Review", "Memory", "Planning"],
    },
    {
        "slug": "pomodoro-deep-work",
        "ko_title": "Pomodoro와 Deep Work: 타이머보다 방해 차단이 먼저다",
        "en_title": "Pomodoro and Deep Work: Block Distractions Before Timing",
        "ko_summary": "집중 루틴은 25분 타이머 자체보다 시작 조건, 방해 차단, 쉬는 시간, 완료 기록을 함께 설계할 때 효과가 커진다.",
        "en_summary": "A focus routine works better when start conditions, distraction blocking, breaks, and completion logs are designed together.",
        "ko_focus": "타이머는 집중을 만들어 주지 않습니다. 무엇을 하지 않을지 정해야 집중 시간이 실제 작업으로 남습니다.",
        "en_focus": "A timer does not create focus by itself; the rule for what not to do protects the work block.",
        "ko_actions": ["한 블록에서 끝낼 결과물을 적습니다.", "휴대폰과 알림을 시작 전에 치웁니다.", "끝난 뒤 산출물과 방해 요인을 기록합니다."],
        "en_actions": ["Write the output for one block.", "Remove phone and notifications before starting.", "Log the output and distraction after the block."],
        "signals": ["focus output", "distraction trigger", "break rule", "completion log"],
        "ko_signals": ["집중 산출물", "방해 요인", "휴식 규칙", "완료 기록"],
        "sources": ["eef_metacognition", "harvard_arc", "cdc_sleep"],
        "tags": ["Focus", "Pomodoro", "DeepWork", "StudyRoutine"],
    },
    {
        "slug": "exam-mistake-note-system",
        "ko_title": "오답노트 시스템: 틀린 문제를 다시 틀리지 않는 기록법",
        "en_title": "Exam Mistake Note System: Turn Wrong Answers into Review Tasks",
        "ko_summary": "오답노트는 문제를 예쁘게 베끼는 노트가 아니라 오류 원인, 정답 조건, 다음 복습 질문을 남기는 시스템이다.",
        "en_summary": "A mistake note is not a copied solution; it records the error cause, correct condition, and next retrieval question.",
        "ko_focus": "오답의 가치는 정답 해설보다 왜 그 선택을 했는지 드러날 때 생깁니다.",
        "en_focus": "The value of a mistake note comes from identifying why the wrong choice looked plausible.",
        "ko_actions": ["오답 원인을 개념, 계산, 독해, 시간으로 분류합니다.", "정답 조건을 한 문장으로 씁니다.", "3일 뒤 풀 재시험 문제를 만듭니다."],
        "en_actions": ["Classify the error as concept, calculation, reading, or time.", "Write the correct condition in one sentence.", "Create a retest question for three days later."],
        "signals": ["error type", "correct condition", "retest question", "repeat mistake"],
        "ko_signals": ["오류 유형", "정답 조건", "재시험 질문", "반복 오답"],
        "sources": ["ies_guide", "eef_metacognition", "ies_pdf"],
        "tags": ["ExamPrep", "MistakeNotes", "Feedback", "Review"],
    },
    {
        "slug": "coding-study-roadmap",
        "ko_title": "코딩 공부 로드맵: 문법, 프로젝트, 디버깅을 한 루프로 묶기",
        "en_title": "Coding Study Roadmap: Connect Syntax, Projects, and Debugging",
        "ko_summary": "코딩 공부는 강의 시청 순서가 아니라 작은 문법 연습, 프로젝트, 디버깅 기록, 문서 읽기가 반복되는 루프다.",
        "en_summary": "Learning to code is a loop of syntax practice, small projects, debugging records, and documentation reading, not a playlist order.",
        "ko_focus": "문법을 모두 외운 뒤 프로젝트를 시작하려 하면 너무 늦습니다. 작게 만들고 막힐 때 문서를 읽어야 합니다.",
        "en_focus": "Waiting to master all syntax before projects delays learning; build small, then read docs when blocked.",
        "ko_actions": ["하루 문법 목표를 하나만 정합니다.", "그 문법을 쓰는 작은 프로그램을 만듭니다.", "에러 메시지와 해결 과정을 기록합니다."],
        "en_actions": ["Choose one syntax goal per day.", "Build a small program using it.", "Record the error message and fix path."],
        "signals": ["syntax target", "small project", "error log", "documentation link"],
        "ko_signals": ["문법 목표", "작은 프로젝트", "에러 로그", "문서 링크"],
        "sources": ["python_start", "mdn_learn", "git_book"],
        "tags": ["CodingStudy", "Programming", "Documentation", "Practice"],
    },
    {
        "slug": "english-vocabulary-system",
        "ko_title": "영어 단어 반복 시스템: 뜻 암기보다 문맥과 회상으로 남기기",
        "en_title": "English Vocabulary System: Learn Words Through Context and Recall",
        "ko_summary": "단어장은 뜻을 많이 적는 곳이 아니라 예문, 직접 만든 문장, 회상 날짜, 틀린 용례를 함께 남기는 학습 시스템이다.",
        "en_summary": "A vocabulary system should keep examples, self-made sentences, recall dates, and wrong usage, not only translated meanings.",
        "ko_focus": "단어를 안다는 것은 뜻을 보는 것이 아니라 문장에서 맞게 꺼내 쓰는 것입니다.",
        "en_focus": "Knowing a word means being able to retrieve and use it in context, not only recognizing a translation.",
        "ko_actions": ["새 단어마다 원문 예문을 남깁니다.", "직접 만든 문장을 하나 씁니다.", "다음 복습 때 뜻이 아니라 문장 완성을 테스트합니다."],
        "en_actions": ["Save an original example sentence for each word.", "Write one sentence of your own.", "Test sentence completion rather than only meaning."],
        "signals": ["context sentence", "self-made sentence", "recall date", "usage error"],
        "ko_signals": ["문맥 예문", "직접 문장", "회상 날짜", "용례 오류"],
        "sources": ["ies_guide", "eef_metacognition", "purdue_paraphrase"],
        "tags": ["Vocabulary", "EnglishStudy", "Recall", "LanguageLearning"],
    },
    {
        "slug": "notion-study-dashboard",
        "ko_title": "Notion 공부 대시보드: 예쁜 화면보다 복습과 오답 흐름",
        "en_title": "Notion Study Dashboard: Track Review and Mistakes Before Design",
        "ko_summary": "공부 대시보드는 꾸미는 화면이 아니라 오늘 할 회상, 밀린 복습, 오답, 주간 성과를 한눈에 보여 주는 운영판이어야 한다.",
        "en_summary": "A study dashboard should show today’s recall tasks, overdue reviews, mistakes, and weekly output before visual design.",
        "ko_focus": "대시보드가 할 일 목록만 늘리면 실패합니다. 복습과 오답이 자동으로 다시 보이게 해야 합니다.",
        "en_focus": "A dashboard fails if it only collects tasks; reviews and mistakes must resurface automatically.",
        "ko_actions": ["오늘 회상할 항목을 맨 위에 둡니다.", "오답 상태를 미해결, 재시험, 해결로 나눕니다.", "주간 리뷰에서 완료보다 기억 점수를 봅니다."],
        "en_actions": ["Put today’s recall items at the top.", "Classify mistakes as open, retest, or solved.", "Review recall score, not only task completion."],
        "signals": ["today review", "overdue item", "mistake status", "weekly score"],
        "ko_signals": ["오늘 복습", "밀린 항목", "오답 상태", "주간 점수"],
        "sources": ["eef_metacognition", "ies_guide", "harvard_arc"],
        "tags": ["Notion", "StudyDashboard", "Review", "Productivity"],
    },
    {
        "slug": "weekly-study-review",
        "ko_title": "주간 공부 회고: 공부 시간보다 회상률과 산출물 보기",
        "en_title": "Weekly Study Review: Track Recall and Output, Not Only Hours",
        "ko_summary": "주간 회고는 공부 시간을 자랑하는 기록이 아니라 무엇을 기억했고 어디서 반복 실패했는지 확인하는 점검 시간이다.",
        "en_summary": "A weekly review should check what you can retrieve and where failure repeats, not only how many hours you studied.",
        "ko_focus": "시간 기록은 출발점일 뿐입니다. 회상률, 문제 정답률, 작성한 코드나 글 같은 산출물이 더 강한 증거입니다.",
        "en_focus": "Hours are only a starting point; recall rate, problem accuracy, written code, or drafts are stronger evidence.",
        "ko_actions": ["이번 주 목표와 실제 산출물을 비교합니다.", "틀린 항목 5개를 다음 주 첫 복습으로 올립니다.", "공부 시간을 늘리기보다 막힌 원인을 하나 줄입니다."],
        "en_actions": ["Compare weekly goals with actual output.", "Move five missed items into next week’s first review.", "Remove one bottleneck before adding more hours."],
        "signals": ["weekly output", "recall rate", "missed item", "next bottleneck"],
        "ko_signals": ["주간 산출물", "회상률", "틀린 항목", "다음 병목"],
        "sources": ["eef_metacognition", "ies_guide", "harvard_arc"],
        "tags": ["WeeklyReview", "StudyPlanning", "Metacognition", "Progress"],
    },
    {
        "slug": "interleaving-practice",
        "ko_title": "Interleaving Practice: 비슷한 문제를 섞어 진짜 구분력을 키우기",
        "en_title": "Interleaving Practice: Mix Similar Problems to Build Discrimination",
        "ko_summary": "Interleaving은 같은 유형을 몰아서 푸는 대신 비슷한 유형을 섞어 어떤 방법을 써야 하는지 판단하는 연습이다.",
        "en_summary": "Interleaving mixes similar problem types so learners practice choosing the method, not only repeating it.",
        "ko_focus": "시험에서는 유형 이름이 붙어 나오지 않으므로 문제를 구분하는 힘이 필요합니다.",
        "en_focus": "Exams rarely label the problem type, so students need practice deciding which method applies.",
        "ko_actions": ["이미 배운 유형 3개를 섞습니다.", "풀이 전 어떤 유형인지 먼저 말합니다.", "틀린 이유가 계산인지 유형 판단인지 나눕니다."],
        "en_actions": ["Mix three already learned problem types.", "Name the type before solving.", "Separate calculation errors from method-selection errors."],
        "signals": ["mixed set", "method choice", "confusion pair", "error reason"],
        "ko_signals": ["혼합 세트", "방법 선택", "헷갈린 쌍", "오류 이유"],
        "sources": ["ies_guide", "ies_pdf", "eef_metacognition"],
        "tags": ["Interleaving", "Practice", "ExamPrep", "ProblemSolving"],
    },
    {
        "slug": "practice-test-review",
        "ko_title": "모의고사 리뷰법: 점수보다 틀린 근거를 먼저 분해하기",
        "en_title": "Practice Test Review: Break Down Evidence Before Chasing Scores",
        "ko_summary": "모의고사는 점수 확인보다 시간 배분, 오답 원인, 찍은 문제, 헷갈린 개념을 분리할 때 다음 점수를 올린다.",
        "en_summary": "Practice tests improve future scores when timing, error causes, guessed items, and confused concepts are separated.",
        "ko_focus": "점수만 보면 다음 행동이 흐려집니다. 각 문제를 다시 공부할 이유로 바꿔야 합니다.",
        "en_focus": "A score alone does not tell the next action; each item must become a study decision.",
        "ko_actions": ["틀린 문제와 찍은 문제를 따로 표시합니다.", "시간 부족 구간을 문제 번호로 기록합니다.", "다시 풀 날짜를 정합니다."],
        "en_actions": ["Mark wrong and guessed items separately.", "Record where time pressure started.", "Schedule the retest date."],
        "signals": ["score section", "guessed item", "time pressure", "retest date"],
        "ko_signals": ["영역 점수", "찍은 문제", "시간 압박", "재시험 날짜"],
        "sources": ["ies_guide", "eef_metacognition", "harvard_arc"],
        "tags": ["PracticeTests", "ExamReview", "Feedback", "StudyPlan"],
    },
    {
        "slug": "question-bank-system",
        "ko_title": "질문은행 만들기: 필기노트를 회상 문제로 바꾸는 법",
        "en_title": "Question Bank System: Convert Notes into Recall Prompts",
        "ko_summary": "질문은행은 노트를 보관하는 폴더가 아니라 다음 복습 때 스스로 답해야 할 질문을 쌓는 시스템이다.",
        "en_summary": "A question bank is not a note archive; it stores prompts you must answer in later review sessions.",
        "ko_focus": "좋은 질문은 답을 찾게 하는 것이 아니라 답을 기억에서 꺼내게 합니다.",
        "en_focus": "A good prompt makes you retrieve the answer, not search for it again.",
        "ko_actions": ["강의 제목을 질문으로 바꿉니다.", "답안 기준을 3개 이하로 둡니다.", "틀린 질문은 다음 주 첫 복습에 올립니다."],
        "en_actions": ["Turn lecture headings into questions.", "Keep answer criteria to three points or fewer.", "Move missed prompts to next week’s first review."],
        "signals": ["recall prompt", "answer key", "missed prompt", "review queue"],
        "ko_signals": ["회상 질문", "답안 기준", "틀린 질문", "복습 대기열"],
        "sources": ["ies_guide", "ies_pdf", "eef_metacognition"],
        "tags": ["QuestionBank", "Recall", "Notes", "Review"],
    },
    {
        "slug": "semester-study-calendar",
        "ko_title": "학기 공부 캘린더: 시험 직전이 아니라 제출일에서 거꾸로 계획하기",
        "en_title": "Semester Study Calendar: Plan Backward from Exams and Deadlines",
        "ko_summary": "학기 캘린더는 일정표가 아니라 시험, 과제, 복습, 휴식, 버퍼 시간을 거꾸로 배치하는 위험 관리 도구다.",
        "en_summary": "A semester calendar is a risk-management tool that schedules exams, assignments, review, rest, and buffers backward.",
        "ko_focus": "시험 전날의 의지는 계획이 아닙니다. 마감 2주 전부터 복습과 초안을 배치해야 합니다.",
        "en_focus": "Motivation the night before is not a plan; review and drafts need space weeks earlier.",
        "ko_actions": ["시험과 제출일을 먼저 표시합니다.", "각 마감에서 2주 전까지 거꾸로 단계를 둡니다.", "예상보다 오래 걸릴 과목에 버퍼를 둡니다."],
        "en_actions": ["Mark exams and deadlines first.", "Plan milestones backward from each deadline.", "Add buffers for subjects that usually run long."],
        "signals": ["deadline", "backward milestone", "review block", "buffer day"],
        "ko_signals": ["마감일", "역산 단계", "복습 블록", "버퍼일"],
        "sources": ["eef_metacognition", "harvard_arc", "ies_guide"],
        "tags": ["StudyPlanning", "Semester", "Calendar", "TimeManagement"],
    },
    {
        "slug": "cornell-note-taking-system",
        "ko_title": "Cornell Note Taking: 필기를 복습 질문으로 바꾸는 구조",
        "en_title": "Cornell Note Taking: Turn Notes into Review Questions",
        "ko_summary": "Cornell note 방식은 필기, 단서, 요약 영역을 나누어 강의 내용을 나중에 회상 질문으로 바꾸기 쉽게 만든다.",
        "en_summary": "The Cornell note system separates notes, cues, and summary so lecture material can become review questions later.",
        "ko_focus": "필기는 많이 받아 적는 것이 아니라 나중에 스스로 테스트할 단서를 남기는 일입니다.",
        "en_focus": "Note taking is not transcription; it should leave cues for later self-testing.",
        "ko_actions": ["오른쪽에는 강의 내용을 짧게 적습니다.", "왼쪽 단서 칸에는 질문을 씁니다.", "하단에는 한 문단 요약을 남깁니다."],
        "en_actions": ["Write concise class notes on the right.", "Add questions in the cue column.", "Write a short summary at the bottom."],
        "signals": ["note column", "cue question", "summary line", "review test"],
        "ko_signals": ["필기 칸", "단서 질문", "요약 줄", "복습 테스트"],
        "sources": ["cornell_notes", "ies_guide", "purdue_paraphrase"],
        "tags": ["CornellNotes", "NoteTaking", "Review", "StudySkills"],
    },
    {
        "slug": "textbook-reading-output",
        "ko_title": "교재 읽기 루틴: 밑줄보다 질문, 요약, 예제로 남기기",
        "en_title": "Textbook Reading Routine: Leave Questions, Summary, and Examples",
        "ko_summary": "교재 읽기는 밑줄 개수보다 읽기 전 질문, 읽은 뒤 요약, 직접 만든 예제가 남을 때 학습으로 이어진다.",
        "en_summary": "Textbook reading becomes study when it leaves pre-questions, post-reading summaries, and self-made examples.",
        "ko_focus": "읽었다는 느낌과 설명할 수 있다는 능력은 다릅니다.",
        "en_focus": "Feeling familiar with a page is different from being able to explain it.",
        "ko_actions": ["읽기 전 소제목을 질문으로 바꿉니다.", "한 절마다 책을 덮고 요약합니다.", "마지막에 직접 예시 하나를 만듭니다."],
        "en_actions": ["Turn headings into questions before reading.", "Close the book and summarize each section.", "Create one original example at the end."],
        "signals": ["pre-question", "section summary", "self example", "unclear term"],
        "ko_signals": ["읽기 전 질문", "절 요약", "직접 예시", "불명확한 용어"],
        "sources": ["ies_guide", "purdue_paraphrase", "eef_metacognition"],
        "tags": ["Reading", "Textbooks", "Summarizing", "StudyRoutine"],
    },
    {
        "slug": "lecture-review-24-hour",
        "ko_title": "강의 후 24시간 리뷰: 잊기 전에 회상 질문 만들기",
        "en_title": "24-Hour Lecture Review: Create Recall Questions Before Forgetting",
        "ko_summary": "강의 직후 24시간 안에 필기를 정리하고 질문으로 바꾸면 다음 복습에서 다시 읽기보다 회상을 시작할 수 있다.",
        "en_summary": "Reviewing lecture notes within 24 hours and turning them into questions makes the next session retrieval-based.",
        "ko_focus": "강의 후 리뷰의 목표는 예쁘게 정리하는 것이 아니라 다음 복습 문제를 만드는 것입니다.",
        "en_focus": "The purpose of post-lecture review is not prettier notes; it is creating the next retrieval task.",
        "ko_actions": ["강의 당일 핵심 5문장을 고릅니다.", "각 문장을 질문으로 바꿉니다.", "모르는 부분은 다음 수업 전 질문 목록에 넣습니다."],
        "en_actions": ["Pick five key sentences the same day.", "Turn each sentence into a question.", "Move unclear points into a question list before the next class."],
        "signals": ["same-day review", "key sentence", "recall question", "next class question"],
        "ko_signals": ["당일 리뷰", "핵심 문장", "회상 질문", "다음 수업 질문"],
        "sources": ["cornell_notes", "ies_guide", "ucsd_spaced"],
        "tags": ["LectureReview", "Notes", "Recall", "Review"],
    },
    {
        "slug": "math-problem-solving-routine",
        "ko_title": "수학 문제 풀이 루틴: 공식 암기보다 조건 해석 먼저",
        "en_title": "Math Problem-Solving Routine: Read Conditions Before Formulas",
        "ko_summary": "수학 공부는 공식을 더 외우는 것보다 문제 조건, 사용할 방법, 검산, 오답 원인을 일정한 순서로 남길 때 안정된다.",
        "en_summary": "Math study improves when conditions, method choice, checking, and error causes are recorded in a stable order.",
        "ko_focus": "공식은 도구이고 문제 조건은 사용 설명서입니다.",
        "en_focus": "A formula is a tool; the problem conditions tell when it applies.",
        "ko_actions": ["주어진 조건과 구할 값을 분리합니다.", "공식을 쓰기 전에 방법 후보를 말합니다.", "답을 낸 뒤 단위와 범위를 검산합니다."],
        "en_actions": ["Separate given conditions from the target value.", "Name candidate methods before using formulas.", "Check units and plausible range after solving."],
        "signals": ["given condition", "target value", "method choice", "check step"],
        "ko_signals": ["주어진 조건", "구할 값", "방법 선택", "검산 단계"],
        "sources": ["ies_guide", "ies_pdf", "eef_metacognition"],
        "tags": ["MathStudy", "ProblemSolving", "ExamPrep", "Feedback"],
    },
    {
        "slug": "writing-revision-study-loop",
        "ko_title": "글쓰기 공부 루프: 초안, 피드백, 재작성으로 실력 만들기",
        "en_title": "Writing Revision Study Loop: Draft, Feedback, Rewrite",
        "ko_summary": "글쓰기 실력은 좋은 문장 읽기만으로 늘지 않고 초안, 기준표, 피드백, 재작성 기록이 반복될 때 개선된다.",
        "en_summary": "Writing improves when drafting, criteria, feedback, and revision records repeat, not from reading good prose alone.",
        "ko_focus": "글쓰기 공부의 핵심 산출물은 완벽한 첫 문장이 아니라 고친 흔적입니다.",
        "en_focus": "The core evidence of writing study is not a perfect first sentence; it is the revision trail.",
        "ko_actions": ["짧은 초안을 제한 시간 안에 씁니다.", "한 번에 한 기준만 고칩니다.", "수정 전후 문장을 나란히 남깁니다."],
        "en_actions": ["Write a short draft under a time limit.", "Revise for one criterion at a time.", "Keep before-and-after sentences side by side."],
        "signals": ["draft", "revision criterion", "feedback note", "before-after sentence"],
        "ko_signals": ["초안", "수정 기준", "피드백 메모", "전후 문장"],
        "sources": ["purdue_writing", "purdue_paraphrase", "eef_metacognition"],
        "tags": ["Writing", "Revision", "Feedback", "AcademicWriting"],
    },
    {
        "slug": "coding-kata-deliberate-practice",
        "ko_title": "Coding Kata 루틴: 같은 문제를 다르게 풀어 패턴을 익히기",
        "en_title": "Coding Kata Routine: Solve the Same Problem in Better Ways",
        "ko_summary": "Coding kata는 문제 수를 늘리는 훈련이 아니라 같은 작은 문제를 조건, 시간, 가독성 기준을 바꿔 반복하는 연습이다.",
        "en_summary": "A coding kata is not about many problems; it repeats a small problem with different constraints, time limits, and readability goals.",
        "ko_focus": "코딩 연습은 정답 제출 후 끝나지 않습니다. 더 읽기 쉬운 풀이와 실패 로그가 남아야 합니다.",
        "en_focus": "Coding practice should continue after a correct answer with readability improvements and failure logs.",
        "ko_actions": ["작은 문제 하나를 고릅니다.", "첫 풀이는 제한 시간 안에 씁니다.", "두 번째 풀이는 이름, 함수 분리, 테스트를 개선합니다."],
        "en_actions": ["Choose one small problem.", "Write the first solution under a time limit.", "Improve naming, function boundaries, and tests in the second solution."],
        "signals": ["small problem", "time box", "refactor note", "test case"],
        "ko_signals": ["작은 문제", "제한 시간", "리팩터 메모", "테스트 케이스"],
        "sources": ["python_start", "mdn_learn", "git_book"],
        "tags": ["CodingPractice", "Kata", "Programming", "Feedback"],
    },
    {
        "slug": "project-based-learning-portfolio",
        "ko_title": "프로젝트 기반 공부 포트폴리오: 결과물과 회고를 함께 남기기",
        "en_title": "Project-Based Learning Portfolio: Keep Output and Reflection Together",
        "ko_summary": "프로젝트 공부는 완성작만 올리는 것이 아니라 문제 정의, 구현 결정, 막힌 지점, 다음 개선을 함께 남길 때 포트폴리오가 된다.",
        "en_summary": "Project-based study becomes a portfolio when the problem, implementation decisions, blockers, and next improvements are recorded.",
        "ko_focus": "작은 프로젝트라도 왜 만들었고 무엇을 배웠는지가 보이면 학습 증거가 됩니다.",
        "en_focus": "Even a small project becomes learning evidence when it shows why it was built and what changed.",
        "ko_actions": ["문제 정의를 3문장으로 씁니다.", "구현 중 선택한 결정을 기록합니다.", "README에 배운 점과 다음 개선을 남깁니다."],
        "en_actions": ["Write the problem in three sentences.", "Record implementation decisions.", "Add lessons learned and next improvements to the README."],
        "signals": ["project output", "decision log", "blocker", "reflection"],
        "ko_signals": ["프로젝트 결과물", "결정 로그", "막힌 지점", "회고"],
        "sources": ["git_book", "python_start", "mdn_learn"],
        "tags": ["ProjectBasedLearning", "Portfolio", "CodingStudy", "Reflection"],
    },
    {
        "slug": "language-shadowing-routine",
        "ko_title": "Language Shadowing 루틴: 따라 말하기를 녹음과 피드백으로 바꾸기",
        "en_title": "Language Shadowing Routine: Turn Repetition into Recorded Feedback",
        "ko_summary": "Shadowing은 그냥 따라 말하는 시간이 아니라 원본, 내 녹음, 차이 표시, 재녹음이 반복될 때 발음과 리듬을 점검할 수 있다.",
        "en_summary": "Shadowing becomes useful when the original, your recording, gap notes, and rerecording form a feedback loop.",
        "ko_focus": "반복 횟수보다 내 소리가 원본과 어디서 달라지는지 듣는 과정이 중요합니다.",
        "en_focus": "The key is hearing where your output differs from the model, not only repeating more times.",
        "ko_actions": ["짧은 원문 30초를 고릅니다.", "그대로 따라 읽고 녹음합니다.", "강세, 속도, 끊어 읽기 차이를 표시합니다."],
        "en_actions": ["Choose a 30-second source.", "Shadow and record yourself.", "Mark differences in stress, speed, and phrasing."],
        "signals": ["source clip", "recording", "gap note", "rerecording"],
        "ko_signals": ["원본 클립", "녹음", "차이 메모", "재녹음"],
        "sources": ["ies_guide", "eef_metacognition", "harvard_arc"],
        "tags": ["LanguageLearning", "Shadowing", "Speaking", "Feedback"],
    },
    {
        "slug": "flashcard-quality-rules",
        "ko_title": "Flashcard 품질 규칙: 카드 수보다 한 카드 한 질문",
        "en_title": "Flashcard Quality Rules: One Card, One Question",
        "ko_summary": "Flashcard는 많이 만드는 것보다 한 카드에 하나의 질문, 짧은 답, 문맥, 실패 기록을 유지할 때 복습 효율이 높다.",
        "en_summary": "Flashcards work better when each card keeps one question, a short answer, context, and failure history.",
        "ko_focus": "좋은 카드는 기억을 꺼내기 쉽게 만들고, 나쁜 카드는 다시 읽기 자료가 됩니다.",
        "en_focus": "A good card prompts retrieval; a bad card becomes another rereading note.",
        "ko_actions": ["한 카드에는 질문 하나만 둡니다.", "답은 세 줄 이하로 줄입니다.", "계속 틀리는 카드는 더 작은 카드로 나눕니다."],
        "en_actions": ["Keep one question per card.", "Keep answers under three lines.", "Split repeatedly missed cards into smaller ones."],
        "signals": ["single prompt", "short answer", "context", "miss history"],
        "ko_signals": ["단일 질문", "짧은 답", "문맥", "오답 기록"],
        "sources": ["ies_guide", "ucsd_spaced", "indiana_spaced"],
        "tags": ["Flashcards", "SpacedRepetition", "Recall", "Memory"],
    },
    {
        "slug": "exam-time-management",
        "ko_title": "시험 시간 관리: 어려운 문제보다 시간 손실 지점을 먼저 찾기",
        "en_title": "Exam Time Management: Find Where Time Leaks Before Hard Problems",
        "ko_summary": "시험 시간 관리는 빨리 푸는 요령이 아니라 문제별 제한 시간, 넘길 기준, 재검토 순서를 미리 정하는 전략이다.",
        "en_summary": "Exam timing is not a speed trick; it sets per-question limits, skip rules, and review order before the test.",
        "ko_focus": "시간 부족은 실력 문제가 아니라 운영 규칙이 없는 문제일 때가 많습니다.",
        "en_focus": "Running out of time is often an operating-rule problem, not only a knowledge problem.",
        "ko_actions": ["문제 유형별 목표 시간을 정합니다.", "막히면 넘길 시간을 미리 정합니다.", "마지막 10분 재검토 순서를 정합니다."],
        "en_actions": ["Set target time by problem type.", "Define when to skip before the test.", "Decide the final ten-minute review order."],
        "signals": ["target time", "skip rule", "review order", "time leak"],
        "ko_signals": ["목표 시간", "넘김 규칙", "재검토 순서", "시간 누수"],
        "sources": ["eef_metacognition", "ies_guide", "harvard_arc"],
        "tags": ["ExamStrategy", "TimeManagement", "TestTaking", "Planning"],
    },
    {
        "slug": "sleep-study-performance",
        "ko_title": "수면과 공부 성과: 밤샘보다 기억과 집중을 보호하기",
        "en_title": "Sleep and Study Performance: Protect Memory and Attention",
        "ko_summary": "수면은 학습과 기억, 집중에 영향을 주므로 시험 전 밤샘은 단기 공부 시간을 늘려도 다음 날 수행을 해칠 수 있다.",
        "en_summary": "Sleep affects learning, memory, and attention, so all-nighters can add study time while weakening next-day performance.",
        "ko_focus": "수면은 공부를 방해하는 시간이 아니라 배운 내용을 유지하기 위한 조건입니다.",
        "en_focus": "Sleep is not wasted study time; it is a condition for retaining and using what was learned.",
        "ko_actions": ["시험 전날 새 범위보다 복습 범위를 좁힙니다.", "잠들기 전 화면과 카페인 시간을 점검합니다.", "수면 문제가 지속되면 전문가 상담을 고려합니다."],
        "en_actions": ["Narrow review scope instead of adding new material the night before.", "Check screen and caffeine timing before bed.", "Consider professional help if sleep problems persist."],
        "signals": ["sleep duration", "bedtime routine", "caffeine timing", "next-day focus"],
        "ko_signals": ["수면 시간", "취침 루틴", "카페인 시간", "다음날 집중"],
        "sources": ["cdc_sleep", "medline_sleep", "ies_guide"],
        "tags": ["Sleep", "StudyHealth", "Memory", "Focus"],
    },
    {
        "slug": "distraction-audit-study",
        "ko_title": "공부 방해요인 감사: 의지보다 환경과 트리거를 고치기",
        "en_title": "Study Distraction Audit: Fix Environment and Triggers Before Willpower",
        "ko_summary": "방해요인 감사는 집중 실패를 의지 문제로 끝내지 않고 알림, 장소, 도구, 시작 조건을 바꾸는 절차다.",
        "en_summary": "A distraction audit turns focus failure into changes to notifications, place, tools, and start conditions.",
        "ko_focus": "집중이 깨지는 순간을 기록하면 반복되는 트리거가 보입니다.",
        "en_focus": "Recording the moment focus breaks reveals repeated triggers.",
        "ko_actions": ["공부가 끊긴 시각과 이유를 적습니다.", "가장 많은 방해요인 하나만 제거합니다.", "다음 블록 전에 환경을 먼저 세팅합니다."],
        "en_actions": ["Record when and why study broke.", "Remove the most frequent trigger first.", "Set up the environment before the next block."],
        "signals": ["break moment", "trigger", "environment change", "next block"],
        "ko_signals": ["끊긴 순간", "트리거", "환경 변경", "다음 블록"],
        "sources": ["eef_metacognition", "harvard_arc", "cdc_sleep"],
        "tags": ["Focus", "Distraction", "StudyRoutine", "Environment"],
    },
    {
        "slug": "study-group-rules",
        "ko_title": "스터디 그룹 규칙: 친목보다 문제 풀이와 피드백을 남기기",
        "en_title": "Study Group Rules: Leave Problem Solving and Feedback",
        "ko_summary": "스터디 그룹은 모이는 횟수보다 각자 풀어온 문제, 설명, 피드백, 다음 과제가 남을 때 학습 효과가 커진다.",
        "en_summary": "A study group works when it leaves solved problems, explanations, feedback, and next tasks, not only attendance.",
        "ko_focus": "같이 공부했다는 느낌보다 각자 설명하고 검증받는 구조가 중요합니다.",
        "en_focus": "The structure for explaining and checking matters more than the feeling of studying together.",
        "ko_actions": ["모임 전 각자 풀 문제를 정합니다.", "한 명씩 풀이를 설명합니다.", "피드백과 다음 과제를 회의록으로 남깁니다."],
        "en_actions": ["Assign problems before the meeting.", "Have each person explain a solution.", "Record feedback and next tasks."],
        "signals": ["prework", "explanation turn", "peer feedback", "next task"],
        "ko_signals": ["사전 과제", "설명 차례", "동료 피드백", "다음 과제"],
        "sources": ["eef_metacognition", "ies_guide", "harvard_arc"],
        "tags": ["StudyGroup", "Feedback", "Collaboration", "ExamPrep"],
    },
    {
        "slug": "metacognition-study-log",
        "ko_title": "Metacognition 공부 로그: 안다고 느낀 것과 실제 회상을 비교하기",
        "en_title": "Metacognition Study Log: Compare Confidence with Recall",
        "ko_summary": "메타인지 공부 로그는 자신감 점수와 실제 회상 점수를 비교해 착각한 단원과 과신한 문제를 찾는 기록이다.",
        "en_summary": "A metacognition log compares confidence with actual recall so overconfident topics and weak units become visible.",
        "ko_focus": "모른다는 사실을 빨리 아는 것이 공부 시간을 줄입니다.",
        "en_focus": "Knowing what you do not know early saves study time.",
        "ko_actions": ["공부 전 자신감 점수를 적습니다.", "책을 덮고 회상 테스트를 합니다.", "자신감과 실제 점수 차이가 큰 항목을 다음 복습으로 보냅니다."],
        "en_actions": ["Write a confidence score before study.", "Close the book and run a recall test.", "Move large confidence-recall gaps to the next review."],
        "signals": ["confidence score", "recall score", "gap", "next review"],
        "ko_signals": ["자신감 점수", "회상 점수", "차이", "다음 복습"],
        "sources": ["eef_metacognition", "ies_guide", "ies_pdf"],
        "tags": ["Metacognition", "StudyLog", "SelfRegulation", "Review"],
    },
    {
        "slug": "research-note-citation-system",
        "ko_title": "리서치 노트와 출처 관리: 복붙보다 요약과 인용 기준",
        "en_title": "Research Note and Citation System: Summarize Before Quoting",
        "ko_summary": "리서치 노트는 자료를 복사해 모으는 공간이 아니라 핵심 주장, 내 말 요약, 출처, 사용할 위치를 함께 남기는 시스템이다.",
        "en_summary": "A research note system records the claim, your paraphrase, source, and planned use instead of collecting copied text.",
        "ko_focus": "출처 관리는 마지막 참고문헌 작업이 아니라 읽을 때부터 시작됩니다.",
        "en_focus": "Citation management starts while reading, not at the final bibliography stage.",
        "ko_actions": ["원문 링크와 접근 날짜를 남깁니다.", "핵심 내용을 내 말로 바꿉니다.", "직접 인용한 문장은 따옴표로 구분합니다."],
        "en_actions": ["Save the source link and access date.", "Rewrite the claim in your own words.", "Mark direct quotations with quotation marks."],
        "signals": ["source link", "paraphrase", "quote mark", "use case"],
        "ko_signals": ["출처 링크", "요약 문장", "직접 인용 표시", "사용 위치"],
        "sources": ["purdue_paraphrase", "purdue_writing", "cornell_notes"],
        "tags": ["ResearchNotes", "Citation", "Writing", "AcademicSkills"],
    },
    {
        "slug": "reading-comprehension-prompts",
        "ko_title": "독해력 질문 프롬프트: 글을 읽고 주장, 근거, 반례를 찾기",
        "en_title": "Reading Comprehension Prompts: Find Claims, Evidence, and Counterexamples",
        "ko_summary": "독해력은 문장을 많이 읽는 것만으로 늘지 않고 주장, 근거, 전제, 반례를 질문으로 확인할 때 깊어진다.",
        "en_summary": "Reading comprehension deepens when claims, evidence, assumptions, and counterexamples are checked with prompts.",
        "ko_focus": "글을 이해했다면 핵심 주장과 그 주장을 받치는 근거를 분리해서 말할 수 있어야 합니다.",
        "en_focus": "Understanding a text means being able to separate the claim from the evidence supporting it.",
        "ko_actions": ["문단마다 주장 한 문장을 찾습니다.", "그 주장의 근거를 표시합니다.", "가능한 반례나 빠진 조건을 적습니다."],
        "en_actions": ["Find one claim per paragraph.", "Mark evidence for that claim.", "Write a possible counterexample or missing condition."],
        "signals": ["claim", "evidence", "assumption", "counterexample"],
        "ko_signals": ["주장", "근거", "전제", "반례"],
        "sources": ["purdue_writing", "purdue_paraphrase", "eef_metacognition"],
        "tags": ["Reading", "Comprehension", "CriticalThinking", "Writing"],
    },
    {
        "slug": "spaced-review-for-coding",
        "ko_title": "코딩 개념 Spaced Review: 문법을 프로젝트 안에서 다시 쓰기",
        "en_title": "Spaced Review for Coding Concepts: Reuse Syntax in Projects",
        "ko_summary": "코딩 개념 복습은 플래시카드만이 아니라 며칠 뒤 작은 기능을 다시 구현해 문법과 사용 맥락을 함께 확인하는 방식이 좋다.",
        "en_summary": "Coding review works well when a concept is reused in a small feature days later, combining syntax with context.",
        "ko_focus": "코드를 이해했다는 증거는 문법 설명보다 다시 작성하고 디버깅할 수 있는지입니다.",
        "en_focus": "The evidence of coding knowledge is whether you can rewrite and debug it, not only explain syntax.",
        "ko_actions": ["오늘 배운 문법을 작은 예제로 씁니다.", "3일 뒤 다른 미니 기능에 다시 씁니다.", "에러 로그를 복습 카드로 바꿉니다."],
        "en_actions": ["Use today’s syntax in a small example.", "Reuse it in a different mini feature three days later.", "Turn error logs into review cards."],
        "signals": ["syntax reuse", "mini feature", "debug log", "review card"],
        "ko_signals": ["문법 재사용", "미니 기능", "디버그 로그", "복습 카드"],
        "sources": ["python_start", "mdn_learn", "ucsd_spaced"],
        "tags": ["CodingStudy", "SpacedPractice", "Debugging", "Programming"],
    },
    {
        "slug": "habit-stack-study-routine",
        "ko_title": "공부 습관 쌓기: 큰 목표보다 시작 신호와 첫 10분",
        "en_title": "Habit Stack Study Routine: Start Signal and First Ten Minutes",
        "ko_summary": "공부 습관은 의욕이 아니라 같은 시간, 같은 시작 신호, 첫 10분 과제, 완료 기록을 반복할 때 유지되기 쉽다.",
        "en_summary": "A study habit is easier to keep when time, start signal, first ten-minute task, and completion log repeat.",
        "ko_focus": "습관의 목표는 긴 공부가 아니라 시작 마찰을 줄이는 것입니다.",
        "en_focus": "The goal of a habit system is reducing start friction, not forcing long sessions immediately.",
        "ko_actions": ["공부 시작 신호를 하나 정합니다.", "첫 10분 과제를 매우 작게 둡니다.", "끝난 뒤 완료 표시와 다음 시작점을 남깁니다."],
        "en_actions": ["Choose one start signal.", "Make the first ten-minute task very small.", "Log completion and the next starting point."],
        "signals": ["start cue", "first task", "completion mark", "next start"],
        "ko_signals": ["시작 신호", "첫 과제", "완료 표시", "다음 시작점"],
        "sources": ["eef_metacognition", "harvard_arc", "cdc_sleep"],
        "tags": ["StudyHabit", "Routine", "Motivation", "Planning"],
    },
    {
        "slug": "exam-day-checklist",
        "ko_title": "시험 당일 체크리스트: 새 공부보다 실수 방지에 집중하기",
        "en_title": "Exam Day Checklist: Prevent Mistakes Instead of Adding New Study",
        "ko_summary": "시험 당일에는 새로운 범위를 무리하게 넣기보다 준비물, 시간, 쉬운 문제, 검토 순서, 컨디션을 확인하는 것이 안전하다.",
        "en_summary": "On exam day, checking materials, timing, easy items, review order, and condition is safer than forcing new material.",
        "ko_focus": "시험 당일의 목표는 실력을 갑자기 늘리는 것이 아니라 이미 가진 실력을 잃지 않는 것입니다.",
        "en_focus": "The exam-day goal is not sudden improvement; it is protecting the ability already built.",
        "ko_actions": ["준비물과 입실 시간을 전날 확인합니다.", "아침에는 핵심 질문만 가볍게 회상합니다.", "시험 중 넘길 규칙과 검토 순서를 지킵니다."],
        "en_actions": ["Check materials and arrival time the day before.", "Use light recall of core questions in the morning.", "Follow skip rules and review order during the test."],
        "signals": ["materials", "arrival time", "light recall", "review order"],
        "ko_signals": ["준비물", "입실 시간", "가벼운 회상", "검토 순서"],
        "sources": ["eef_metacognition", "cdc_sleep", "medline_sleep"],
        "tags": ["ExamDay", "Checklist", "TestTaking", "Stress"],
    },
    {
        "slug": "learning-with-ai-safely",
        "ko_title": "AI로 공부할 때 주의점: 답을 받기보다 질문과 피드백에 쓰기",
        "en_title": "Learning with AI Safely: Use It for Questions and Feedback",
        "ko_summary": "AI 학습 도구는 정답을 바로 받는 용도보다 회상 질문 만들기, 설명 점검, 힌트 단계, 오답 분석에 쓸 때 학습 루프를 해치지 않는다.",
        "en_summary": "AI study tools are more useful for recall prompts, explanation checks, staged hints, and mistake analysis than for instant answers.",
        "ko_focus": "AI가 답을 대신하면 빠르지만, 기억에서 꺼내는 연습이 사라질 수 있습니다.",
        "en_focus": "AI answers can be fast, but they can remove the retrieval effort that learning needs.",
        "ko_actions": ["정답 요청 전에 내 답을 먼저 씁니다.", "AI에게 힌트를 단계별로 요구합니다.", "AI 답변은 원문 자료나 교재로 검증합니다."],
        "en_actions": ["Write your answer before asking for help.", "Ask for staged hints instead of the full answer.", "Verify AI output against the source or textbook."],
        "signals": ["own answer", "hint stage", "source check", "mistake analysis"],
        "ko_signals": ["내 답안", "힌트 단계", "원문 확인", "오답 분석"],
        "sources": ["ies_guide", "eef_metacognition", "purdue_paraphrase"],
        "tags": ["AIStudy", "Learning", "Feedback", "Verification"],
    },
]


LEGACY_IMAGES = {
    "active-recall-study-method": ["active-recall-hero.png"],
    "spaced-repetition-schedule": ["spaced-repetition-hero.png"],
    "pomodoro-deep-work": ["pomodoro-deep-work-hero.png"],
    "exam-mistake-note-system": ["mistake-note-hero.png"],
    "coding-study-roadmap": ["coding-roadmap-hero.png"],
    "english-vocabulary-system": ["vocabulary-system-hero.png"],
    "notion-study-dashboard": ["notion-study-dashboard-hero.png"],
    "weekly-study-review": ["weekly-review-hero.png", "weekly-study-review-hero.png"],
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
    paper = (250, 250, 245)
    ink = (17, 24, 39)
    rows: list[bytes] = []
    title_weight = sum(ord(ch) for ch in title) % 180

    for y in range(height):
        vertical = y / (height - 1)
        left = blend(base, paper, 0.20 + vertical * 0.10)
        mid = blend(base, ink, 0.34 + vertical * 0.16)
        right = blend(ink, accent, 0.24 + variant * 0.04)
        card = blend(paper, accent, 0.07)
        mark = blend(accent, paper, 0.18)

        if y % 68 == 0:
            row = bytes(blend(left, paper, 0.18)) * width
        elif 288 <= y <= 552:
            row = bytes(left) * 78 + bytes(card) * 540 + bytes(mid) * 232 + bytes(right) * 350
        elif 132 + variant * 24 <= y <= 166 + variant * 24:
            row = bytes(left) * (470 + title_weight) + bytes(mark) * 460 + bytes(right) * (270 - title_weight)
        elif 342 <= y <= 522 and (y - 342) % 52 < 16:
            row = bytes(left) * 96 + bytes(mark) * 458 + bytes(mid) * 256 + bytes(right) * 390
        elif 176 <= y <= 590 and (y + title_weight) % 126 < 18:
            row = bytes(left) * 702 + bytes(mid) * 132 + bytes(mark) * 250 + bytes(right) * 116
        else:
            row = bytes(left) * 628 + bytes(mid) * 248 + bytes(right) * 324
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
    return bounded_text(title, 10 if lang == "ko" else 20, 70, "study guide")


def seo_description(topic: dict[str, object], lang: str) -> str:
    if lang == "ko":
        return bounded_text(str(topic["ko_summary"]), 60, 170, "근거 있는 루틴, 복습 기준, 오답 관리 방법을 함께 정리합니다.")
    return bounded_text(
        str(topic["en_summary"]),
        80,
        170,
        "It adds a practical routine, review signal, and feedback loop for one study session.",
    )


def source_notes(source_keys: list[str], lang: str) -> str:
    return "\n".join(f"- [{SOURCES[key][lang]}]({SOURCES[key]['url']})" for key in source_keys)


def related_links(index: int, lang: str) -> str:
    related = [TOPICS[(index + 1) % len(TOPICS)], TOPICS[(index + 10) % len(TOPICS)]]
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
        f"공부법은 기분 좋은 동기부여보다 **{first}** 같은 관찰 가능한 신호가 남아야 지속됩니다. "
        f"이 글은 **{topic['ko_title']}** 주제를 한 번의 공부 세션에서 바로 테스트할 수 있는 루틴으로 정리합니다."
    )


def en_intro(topic: dict[str, object]) -> str:
    first = topic["signals"][0]
    return (
        f"A study method becomes useful when it leaves an observable signal such as **{first}**. "
        f"This guide turns **{topic['en_title']}** into a routine that can be tested in one session."
    )


def ko_disclaimer(topic: dict[str, object]) -> str:
    return (
        f"이 글은 교육용 학습 가이드입니다. **{topic['ko_title']}**가 모든 학생, 시험, 과목에 같은 결과를 보장하지는 않습니다. "
        "수면, 건강, 불안, 집중 문제가 심하거나 지속된다면 학교 상담, 보호자, 의료 전문가처럼 자격 있는 도움을 함께 고려해야 합니다."
    )


def en_disclaimer(topic: dict[str, object]) -> str:
    return (
        f"This article is educational. **{topic['en_title']}** does not guarantee the same result for every learner, exam, or subject. "
        "If sleep, health, anxiety, or attention problems are severe or persistent, consider qualified support from school staff, guardians, or medical professionals."
    )


def ko_signal_items(topic: dict[str, object]) -> str:
    title = topic["ko_title"]
    return "\n".join(
        f"- **{signal}**: {title}를 적용할 때 이 항목을 실제 기록으로 남겨 다음 복습에서 확인합니다."
        for signal in topic["ko_signals"]
    )


def en_signal_items(topic: dict[str, object]) -> str:
    title = topic["en_title"]
    return "\n".join(
        f"- **{signal}**: for {title}, leave this as a record that can be checked in the next review."
        for signal in topic["signals"]
    )


def ko_action_items(topic: dict[str, object]) -> str:
    return "\n".join(f"- {action}" for action in topic["ko_actions"])


def en_action_items(topic: dict[str, object]) -> str:
    return "\n".join(f"- {action}" for action in topic["en_actions"])


def ko_context(topic: dict[str, object]) -> str:
    first = topic["ko_signals"][0]
    second = topic["ko_signals"][1]
    return (
        f"이 루틴은 공부 시간을 늘리기 위한 장식이 아닙니다. **{first}**와 **{second}**가 남아야 다음 공부에서 무엇을 반복하고 "
        "무엇을 줄일지 판단할 수 있습니다. 한 번에 모든 과목에 적용하지 말고, 먼저 한 과목과 한 단원에서 작게 시작하는 편이 좋습니다."
    )


def en_context(topic: dict[str, object]) -> str:
    first = topic["signals"][0]
    second = topic["signals"][1]
    return (
        f"This routine is not decoration for a longer study session. It should leave **{first}** and **{second}** so the next session can decide what to repeat "
        "and what to reduce. Start with one subject and one unit before scaling it across a full schedule."
    )


def ko_record_example(topic: dict[str, object]) -> str:
    first = topic["ko_signals"][0]
    second = topic["ko_signals"][1]
    third = topic["ko_signals"][2]
    return (
        f"기록은 길 필요가 없습니다. 세션 마지막에 **{first}**, **{second}**, **{third}** 세 칸만 채워도 충분합니다. "
        "예를 들어 맞힌 항목은 다음 간격을 늘리고, 헷갈린 항목은 이유를 한 단어로 표시하며, 완전히 틀린 항목은 다음 세션의 첫 문제로 올립니다. "
        "이렇게 하면 공부가 끝난 뒤에도 무엇을 해야 하는지 남아 있고, 다음 날 다시 책상에 앉았을 때 준비 시간이 줄어듭니다."
    )


def en_record_example(topic: dict[str, object]) -> str:
    first = topic["signals"][0]
    second = topic["signals"][1]
    third = topic["signals"][2]
    return (
        f"The record does not need to be long. Filling three fields, **{first}**, **{second}**, and **{third}**, is enough for one session. "
        "Move correct items to a longer interval, tag confused items with a short reason, and put missed items at the top of the next session. "
        "This keeps the next study block from starting with setup work."
    )


def ko_example(topic: dict[str, object]) -> str:
    first = topic["ko_signals"][0]
    action = topic["ko_actions"][0]
    return (
        f"예를 들어 오늘 40분만 쓸 수 있다면 먼저 '{action}' 단계를 수행합니다. 이후 **{first}** 결과를 남기고, 맞힌 항목과 "
        "헷갈린 항목을 분리합니다. 마지막 5분에는 다음 복습에서 바로 시작할 질문 하나를 적습니다. 이 작은 종료 기록이 있어야 "
        "다음 세션이 다시 준비 시간으로 낭비되지 않습니다."
    )


def en_example(topic: dict[str, object]) -> str:
    first = topic["signals"][0]
    action = str(topic["en_actions"][0]).rstrip(".")
    return (
        f"If you only have 40 minutes today, start with '{action}'. Then record the **{first}** result and separate correct items from confused items. "
        "Use the final five minutes to write one question that starts the next review. That small closing record prevents the next session from becoming setup time again."
    )


def ko_checklist(topic: dict[str, object]) -> str:
    first = topic["ko_signals"][0]
    second = topic["ko_signals"][1]
    return "\n".join(
        [
            f"- 시작 전에 오늘 남길 **{first}** 결과를 정합니다.",
            f"- 끝나기 전에 **{second}**를 확인하고 다음 복습 항목을 표시합니다.",
            "- 공부 시간, 맞힌 항목, 틀린 항목을 같은 표에 남깁니다.",
            "- 루틴이 너무 복잡하면 한 단계만 줄이고 다음 주에 다시 비교합니다.",
        ]
    )


def en_checklist(topic: dict[str, object]) -> str:
    first = topic["signals"][0]
    second = topic["signals"][1]
    return "\n".join(
        [
            f"- Before starting, define the **{first}** output for today.",
            f"- Before ending, check **{second}** and mark the next review item.",
            "- Keep time spent, correct items, and missed items in one table.",
            "- If the routine is too complex, remove one step and compare again next week.",
        ]
    )


def ko_faq(topic: dict[str, object]) -> str:
    first = topic["ko_signals"][0]
    second = topic["ko_signals"][1]
    return dedent(f"""\
    ### {topic["ko_title"]}를 모든 과목에 바로 적용해도 되나요?

    처음에는 한 과목, 한 단원, 한 주기로 제한하는 편이 안전합니다. **{first}** 기록이 남고 다음 복습에서 다시 쓸 수 있을 때 **{topic["ko_title"]}** 루틴을 다른 과목으로 넓히면 됩니다.

    ### 공부 시간이 짧아도 효과가 있나요?

    짧은 시간이라도 **{second}**를 확인하고 종료 기록을 남기면 다음 세션의 시작 비용이 줄어듭니다. **{topic["ko_title"]}**에서는 단순히 시간을 채우는 것보다 회상, 피드백, 재복습이 포함되어야 합니다.

    ### 결과가 바로 좋아지지 않으면 실패인가요?

    아닙니다. **{topic["ko_title"]}** 같은 학습 루틴은 즉시 점수 상승보다 반복 실패 지점을 드러내는 데 먼저 가치가 있습니다. 2~3주 동안 **{first}** 기준을 같은 방식으로 기록한 뒤 조정하는 것이 좋습니다.
    """)


def en_faq(topic: dict[str, object]) -> str:
    first = topic["signals"][0]
    second = topic["signals"][1]
    return dedent(f"""\
    ### Should I apply {topic["en_title"]} to every subject immediately?

    Start with one subject, one unit, and one review cycle. Expand **{topic["en_title"]}** only after the **{first}** record is useful in the next session.

    ### Can this work when study time is short?

    Yes, if the short session still checks **{second}** and leaves a closing record. In **{topic["en_title"]}**, time alone is not the point; retrieval, feedback, and rescheduling need to be included.

    ### Is {topic["en_title"]} failing if scores do not improve immediately?

    No. **{topic["en_title"]}** first becomes valuable by revealing repeated failure points. Keep the same **{first}** measure for two or three weeks before changing the system.
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
    date: {POST_DATE}T{6 + index // 3:02d}:{(index % 3) * 18:02d}:00+09:00
    last_modified_at: {LAST_MODIFIED_AT}
    lang: ko
    translation_id: study-{slug}
    header:
      teaser: {image_dir}/hero.png
      overlay_image: {image_dir}/hero.png
      overlay_filter: 0.36
      image_description: >
        {topic["ko_title"]}의 학습 루틴과 복습 신호를 요약한 이미지입니다.
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

    ![{topic["ko_title"]} 학습 루틴 흐름]({image_dir}/hero.png)

    ## 핵심 요약

    {topic["ko_focus"]}

    {ko_context(topic)}

    ## 먼저 확인할 신호

    {ko_signal_items(topic)}

    ![{topic["ko_title"]} 실행 체크리스트]({image_dir}/checklist.png)

    ## 실전 적용 순서

    {ko_action_items(topic)}

    ## 40분 세션 예시

    {ko_example(topic)}

    ## 기록 예시

    {ko_record_example(topic)}

    ## 체크리스트

    {ko_checklist(topic)}

    ## 자주 묻는 질문

    {ko_faq(topic)}

    ## 참고할 자료

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
    date: {POST_DATE}T{6 + index // 3:02d}:{(index % 3) * 18:02d}:00+09:00
    last_modified_at: {LAST_MODIFIED_AT}
    lang: en
    translation_id: study-{slug}
    header:
      teaser: {image_dir}/hero.png
      overlay_image: {image_dir}/hero.png
      overlay_filter: 0.36
      image_description: >
        Study guide image summarizing the learning routine and review signals for this topic.
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

    ![{topic["en_title"]} study routine flow]({image_dir}/hero.png)

    ## Quick Summary

    {topic["en_focus"]}

    {en_context(topic)}

    ## Signals To Check First

    {en_signal_items(topic)}

    ![{topic["en_title"]} action checklist]({image_dir}/checklist.png)

    ## Practical Routine

    {en_action_items(topic)}

    ## 40-Minute Session Example

    {en_example(topic)}

    ## Record Example

    {en_record_example(topic)}

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
        title: "Study"
        layout: archive
        permalink: /ko_study/
        lang: ko
        seo_description: >
          Active recall, spaced repetition, 오답노트, 집중 루틴, 코딩 공부, 영어 단어, 노트 정리, 시험 전략처럼 근거 있는 학습 시스템을 정리한 글 모음입니다.
        sidebar:
            nav: "sidebar-category"
        ---

        Study 카테고리는 공부 시간을 늘리는 방법보다 결과가 남는 학습 시스템을 다룹니다. 기억에서 꺼내 쓰기, 복습 간격, 오답 관리, 집중 시간 설계, 필기와 독해, 코딩 연습, 언어 학습처럼 시험과 실무 공부에 모두 적용할 수 있는 주제를 모았습니다.

        각 글은 IES, EEF, CDC, NIH MedlinePlus, Purdue OWL, Cornell Learning Strategies Center, Python.org, MDN, Pro Git 같은 교육·기관 자료를 참고합니다. 목표는 공부법을 많이 모으는 것이 아니라 한 번의 세션에서 회상, 피드백, 다음 복습이 남는 루틴을 만드는 것입니다.

        처음에는 active recall과 spaced repetition을 읽고, 이후 오답노트, 질문은행, 주간 리뷰, 수면과 집중 루틴으로 공부 루프를 넓히면 좋습니다.

        ## 먼저 읽기

        - [Active Recall 공부법](/ko_study/active-recall-study-method/)
        - [Spaced Repetition 복습 일정](/ko_study/spaced-repetition-schedule/)
        - [오답노트 시스템](/ko_study/exam-mistake-note-system/)
        - [질문은행 만들기](/ko_study/question-bank-system/)
        - [수면과 공부 성과](/ko_study/sleep-study-performance/)

        ## 최신 글

        {% assign posts = site.categories["ko_Study"] %}
        {% for post in posts %}
          {% include archive-single.html type=page.entries_layout %}
        {% endfor %}
        """)
    return dedent("""\
    ---
    title: "Study"
    layout: archive
    permalink: /en_study/
    lang: en
    seo_description: >
      Evidence-informed study system guides for active recall, spaced repetition, mistake notes, focus routines, coding practice, vocabulary, note taking, and exam strategy.
    sidebar:
        nav: "sidebar-category"
    ---

    The Study category focuses on learning systems that produce visible output. It covers retrieval, review intervals, mistake tracking, focus blocks, notes, reading, coding practice, language learning, exam strategy, and weekly review.

    The articles refer to education and institution-grade sources such as IES, EEF, CDC, NIH MedlinePlus, Purdue OWL, Cornell Learning Strategies Center, Python.org, MDN, and Pro Git. The goal is not to collect more study hacks. The goal is to build one-session routines that leave recall evidence, feedback, and a next review task.

    Start with active recall and spaced repetition, then add mistake notes, question banks, weekly review, sleep, and focus routines to close the learning loop.

    ## Start Here

    - [Active Recall Study Method](/en_study/active-recall-study-method/)
    - [Spaced Repetition Schedule](/en_study/spaced-repetition-schedule/)
    - [Exam Mistake Note System](/en_study/exam-mistake-note-system/)
    - [Question Bank System](/en_study/question-bank-system/)
    - [Sleep and Study Performance](/en_study/sleep-study-performance/)

    ## Latest Articles

    {% assign posts = site.categories["en_Study"] %}
    {% for post in posts %}
      {% include archive-single.html type=page.entries_layout %}
    {% endfor %}
    """)


def main() -> None:
    palettes = [
        ("#1e3a8a", "#f97316"),
        ("#0f766e", "#facc15"),
        ("#6d28d9", "#38bdf8"),
        ("#9f1239", "#22c55e"),
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
        write_png(image_dir / "hero.png", str(topic["en_title"]), [str(item) for item in topic["signals"]], palette, index % 3)
        write_png(image_dir / "checklist.png", str(topic["en_title"]), [str(item) for item in topic["en_actions"]], (palette[0], "#eab308"), (index + 1) % 3)
        (ROOT / "_posts" / "ko" / f"{POST_DATE}-{slug}.md").write_text(normalize_markdown(ko_post(topic, index)), encoding="utf-8")
        (ROOT / "_posts" / "en" / f"{POST_DATE}-{slug}.md").write_text(normalize_markdown(en_post(topic, index)), encoding="utf-8")
    (ROOT / "_pages" / "category-ko_Study.md").write_text(normalize_markdown(category_page("ko")), encoding="utf-8")
    (ROOT / "_pages" / "category-en_Study.md").write_text(normalize_markdown(category_page("en")), encoding="utf-8")
    print(f"Generated {len(TOPICS)} paired Study topics.")


if __name__ == "__main__":
    main()
