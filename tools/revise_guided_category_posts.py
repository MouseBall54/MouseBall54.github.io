#!/usr/bin/env python3
"""Bulk readability revisions for generated category posts."""

from __future__ import annotations

import importlib.util
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str):
    path = ROOT / "tools" / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


STUDY = load_module("generate_study_posts")
ECONOMY = load_module("generate_economy_posts")


def find_post(lang: str, slug: str) -> Path:
    matches = sorted((ROOT / "_posts" / lang).glob(f"????-??-??-{slug}.md"))
    if len(matches) != 1:
        raise RuntimeError(f"Expected one {lang} post for {slug}, found {len(matches)}")
    return matches[0]


def split_front_matter(text: str) -> tuple[str, str]:
    match = re.match(r"(?s)\A(---\n.*?\n---\n)(.*)\Z", text)
    if not match:
        raise RuntimeError("front matter not found")
    return match.group(1), match.group(2)


def replace_first_paragraph(body: str, paragraph: str) -> str:
    return re.sub(r"\A.*?\n\n", paragraph.rstrip() + "\n\n", body, count=1, flags=re.DOTALL)


def replace_section(body: str, start_heading: str, end_heading: str, replacement: str) -> str:
    pattern = rf"({re.escape(start_heading)}\n\n)(.*?)({re.escape(end_heading)}\n)"
    updated, count = re.subn(pattern, rf"\1{replacement.rstrip()}\n\n\3", body, count=1, flags=re.DOTALL)
    if count != 1:
        raise RuntimeError(f"section not found: {start_heading}")
    return updated


def replace_section_until_image(body: str, heading: str, replacement: str) -> str:
    pattern = rf"({re.escape(heading)}\n\n)(.*?)(\n\n!\[)"
    updated, count = re.subn(pattern, rf"\1{replacement.rstrip()}\3", body, count=1, flags=re.DOTALL)
    if count != 1:
        raise RuntimeError(f"section not found: {heading}")
    return updated


def study_summary(topic: dict[str, object], lang: str) -> str:
    if lang == "ko":
        first, second = topic["ko_signals"][:2]
        return (
            f"{topic['ko_focus']}\n\n"
            f"이 루틴은 긴 공부 시간을 꾸미는 부가 작업이 아닙니다. 오늘 남겨야 할 기록은 **{first}**와 **{second}**처럼 다음 복습을 바꾸는 신호입니다. "
            "한 과목의 한 단원에서 먼저 시험하고, 다음 세션에서 실제로 도움이 된 기록만 남기면 부담이 작아집니다."
        )
    first, second = topic["signals"][:2]
    return (
        f"{topic['en_focus']}\n\n"
        f"This routine is not extra paperwork for a longer study session. The useful record is a signal such as **{first}** or **{second}** that changes the next review. "
        "Test it on one subject and one unit first, then keep only the fields that help the next session start faster."
    )


def study_signal_block(topic: dict[str, object], lang: str) -> str:
    if lang == "ko":
        templates = [
            "공부를 시작하기 전에 기준을 정합니다. 오늘 무엇을 맞히거나 설명할 수 있어야 하는지 한 문장으로 적어야 결과를 해석할 수 있습니다.",
            "책을 덮고 확인합니다. 읽은 느낌이 아니라 실제로 떠올린 답, 풀이, 설명을 남겨야 다음 복습 대상이 보입니다.",
            "틀린 이유를 짧게 분류합니다. 개념 누락, 조건 착각, 계산 실수, 시간 부족처럼 다시 고칠 수 있는 원인으로 적습니다.",
            "다음 복습 행동을 예약합니다. 같은 자료를 다시 읽을지, 문제를 바꿀지, 설명을 다시 만들지까지 정해야 기록이 실행으로 이어집니다.",
        ]
        signals = topic["ko_signals"]
    else:
        templates = [
            "Define the target before studying. A one-sentence standard for what you should recall, solve, or explain makes the result interpretable.",
            "Check it with the book closed. Record the answer, solution, or explanation you actually produced, not the feeling that the page looked familiar.",
            "Classify the miss briefly. Use fixable causes such as missing concept, condition error, calculation slip, or time pressure.",
            "Schedule the next review action. Decide whether to reread, solve a different problem, or rebuild the explanation so the record turns into work.",
        ]
        signals = topic["signals"]
    return "\n".join(f"- **{signal}**: {templates[index % len(templates)]}" for index, signal in enumerate(signals))


def study_record(topic: dict[str, object], lang: str) -> str:
    if lang == "ko":
        first, second, third = topic["ko_signals"][:3]
        return (
            f"기록은 길 필요가 없습니다. `{first}`, `{second}`, `{third}` 세 칸만 있어도 오늘의 판단을 다음 세션에서 다시 확인할 수 있습니다. "
            "맞힌 항목은 간격을 늘리고, 헷갈린 항목은 이유를 붙이고, 틀린 항목은 다음 세션의 첫 문제로 올립니다."
        )
    first, second, third = topic["signals"][:3]
    return (
        f"The record can stay short. Three fields, `{first}`, `{second}`, and `{third}`, are enough to make today's judgment visible in the next session. "
        "Move correct items to a longer interval, tag confused items with a reason, and put missed items at the top of the next session."
    )


def economy_summary(topic: dict[str, object], lang: str) -> str:
    if lang == "ko":
        first, second = topic["ko_signals"][:2]
        return (
            f"{topic['ko_focus']}\n\n"
            f"**{first}**와 **{second}**는 단독 숫자로 보면 쉽게 오해됩니다. 발표일, 기준 기간, 전월 대비와 전년 대비, 명목과 실질을 먼저 확인한 뒤 "
            "가계에는 물가, 임금, 이자 비용, 환율, 저축 여력 중 어디로 전달되는지 따로 적어야 합니다."
        )
    first, second = topic["signals"][:2]
    return (
        f"{topic['en_focus']}\n\n"
        f"Signals such as **{first}** and **{second}** are easy to misread as standalone numbers. Check the release date, reference period, month-over-month versus year-over-year basis, and nominal versus real terms first. "
        "For household use, write down whether the signal reaches prices, wages, interest payments, exchange rates, or savings capacity."
    )


def economy_signal_block(topic: dict[str, object], lang: str) -> str:
    if lang == "ko":
        templates = [
            "최신 수치와 발표일을 같이 적습니다. 숫자만 옮기면 이후 수정치, 기준 기간, 계절 조정 여부를 놓치기 쉽습니다.",
            "방향과 크기를 나눠 봅니다. 상승 또는 하락 자체보다 변화 폭이 가계 지출, 임금, 대출금리에 닿는지가 중요합니다.",
            "다른 지표와 함께 확인합니다. 물가, 고용, 금리, 환율 중 하나만 보면 평균 경제와 개인 현금흐름의 차이를 놓칩니다.",
            "한국 독자에게 닿는 경로를 적습니다. 원화 환율, 수입 에너지, 변동금리 대출, 수출 업종 고용처럼 실제 비용 채널로 바꿔 봅니다.",
        ]
        signals = topic["ko_signals"]
    else:
        templates = [
            "Record the latest value together with the release date. A number without revision status, reference period, or seasonal adjustment can mislead later comparisons.",
            "Separate direction from magnitude. The household question is not only whether it rose or fell, but whether the change reaches spending, wages, or debt rates.",
            "Read it with companion indicators. Inflation, jobs, rates, and exchange rates often explain why the average economy differs from one household's cash flow.",
            "Write the Korea-facing channel. Translate the signal into won exchange rates, imported energy, variable-rate loans, export jobs, or other concrete cost paths.",
        ]
        signals = topic["signals"]
    return "\n".join(f"- **{signal}**: {templates[index % len(templates)]}" for index, signal in enumerate(signals))


def revise_study(topic: dict[str, object], lang: str) -> None:
    path = find_post(lang, str(topic["slug"]))
    fm, body = split_front_matter(path.read_text(encoding="utf-8"))
    if lang == "ko":
        body = replace_first_paragraph(
            body,
            f"이 글은 **{topic['ko_title']}**를 의지 문제가 아니라 다음 복습을 바꾸는 실행 루틴으로 정리합니다. 기록, 회상, 피드백이 한 세트로 남아야 공부 시간이 실제 결과로 이어집니다.",
        )
        body = replace_section(body, "## 핵심 요약", "## 먼저 확인할 신호", study_summary(topic, lang))
        body = replace_section_until_image(body, "## 먼저 확인할 신호", study_signal_block(topic, lang))
        body = replace_section(body, "## 기록 예시", "## 체크리스트", study_record(topic, lang))
    else:
        body = replace_first_paragraph(
            body,
            f"This guide treats **{topic['en_title']}** as an execution routine, not a motivation trick. Recall, feedback, and a small record need to stay together for study time to change the next session.",
        )
        body = replace_section(body, "## Quick Summary", "## Signals To Check First", study_summary(topic, lang))
        body = replace_section_until_image(body, "## Signals To Check First", study_signal_block(topic, lang))
        body = replace_section(body, "## Record Example", "## Checklist", study_record(topic, lang))
    path.write_text(fm + body, encoding="utf-8")


def revise_economy(topic: dict[str, object], lang: str) -> None:
    path = find_post(lang, str(topic["slug"]))
    fm, body = split_front_matter(path.read_text(encoding="utf-8"))
    if lang == "ko":
        body = replace_first_paragraph(
            body,
            f"이 글은 **{topic['ko_title']}**를 예측 문제가 아니라 가계 의사결정에 필요한 신호 읽기 문제로 설명합니다. 숫자를 맞히기보다 발표 기준, 전달 경로, 한국 독자에게 닿는 비용 채널을 분리해 봅니다.",
        )
        body = replace_section(body, "## 핵심 요약", "## 먼저 확인할 신호", economy_summary(topic, lang))
        body = replace_section_until_image(body, "## 먼저 확인할 신호", economy_signal_block(topic, lang))
    else:
        body = replace_first_paragraph(
            body,
            f"This guide explains **{topic['en_title']}** as a signal-reading problem for household decisions, not a forecasting game. The goal is to separate release details, transmission channels, and Korea-facing cost paths.",
        )
        body = replace_section(body, "## Quick Summary", "## Signals To Check First", economy_summary(topic, lang))
        body = replace_section_until_image(body, "## Signals To Check First", economy_signal_block(topic, lang))
    path.write_text(fm + body, encoding="utf-8")


def main() -> None:
    changed = 0
    for topic in STUDY.TOPICS:
        for lang in ("ko", "en"):
            revise_study(topic, lang)
            changed += 1

    for topic in ECONOMY.TOPICS:
        for lang in ("ko", "en"):
            revise_economy(topic, lang)
            changed += 1

    print(f"Revised {changed} study/economy posts.")


if __name__ == "__main__":
    main()
