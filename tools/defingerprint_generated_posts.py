#!/usr/bin/env python3
"""Remove high-frequency template fingerprints from generated posts."""

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


AI = load_module("generate_ai_trends_posts")
STUDY = load_module("generate_study_posts")
ECONOMY = load_module("generate_economy_posts")
DIGITAL = load_module("generate_digital_security_posts")
HEALTH = load_module("generate_health_literacy_posts")
AGENT_CLI = load_module("generate_ai_agent_cli_posts")


def find_post(lang: str, slug: str, translation_id: str | None = None) -> Path:
    matches = sorted((ROOT / "_posts" / lang).glob(f"????-??-??-{slug}.md"))
    if translation_id is not None:
        matches = [
            path
            for path in matches
            if re.search(rf"^translation_id:\s*{re.escape(translation_id)}\s*$", path.read_text(encoding="utf-8"), re.MULTILINE)
        ]
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


def replace_paragraph_containing(body: str, needle: str, replacement: str) -> str:
    pattern = rf"(?m)^.*{re.escape(needle)}.*(?:\n(?!\n).*)*\n"
    updated, count = re.subn(pattern, replacement.rstrip() + "\n", body, count=1)
    return updated if count == 1 else body


def replace_section(body: str, start_heading: str, end_heading: str, replacement: str) -> str:
    pattern = rf"({re.escape(start_heading)}\n\n)(.*?)({re.escape(end_heading)}\n)"
    updated, count = re.subn(pattern, rf"\1{replacement.rstrip()}\n\n\3", body, count=1, flags=re.DOTALL)
    if count != 1:
        raise RuntimeError(f"section not found: {start_heading}")
    return updated


def revise_ai(topic: dict[str, object], lang: str) -> None:
    slug = str(topic["slug"])
    path = find_post(lang, slug, f"ai-trends-{slug}")
    fm, body = split_front_matter(path.read_text(encoding="utf-8"))
    if lang == "ko":
        first, second = topic["ko_signals"][:2]
        text = f"{topic['ko_focus']} 실제 도입 전에는 **{first}**와 **{second}**를 먼저 문서화해야 결과 검토, 비용, 책임 소재가 뒤로 밀리지 않습니다."
    else:
        first, second = topic["signals"][:2]
        text = f"{topic['en_focus']} Before adoption, document **{first}** and **{second}** so review, cost control, and accountability are not pushed downstream."
    path.write_text(fm + replace_first_paragraph(body, text), encoding="utf-8")


def revise_study(topic: dict[str, object], lang: str) -> None:
    slug = str(topic["slug"])
    path = find_post(lang, slug, f"study-{slug}")
    fm, body = split_front_matter(path.read_text(encoding="utf-8"))
    if lang == "ko":
        first, second = topic["ko_signals"][:2]
        intro = f"{topic['ko_focus']} 오늘의 목표는 **{first}**와 **{second}**를 남겨 다음 복습에서 무엇을 반복하고 무엇을 줄일지 바로 결정하는 것입니다."
        summary = f"{topic['ko_focus']}\n\n작게 시작하려면 한 과목, 한 단원, 한 회상 질문만 고릅니다. 종료 기록에는 **{first}**와 **{second}**만 남겨도 다음 세션의 첫 행동이 분명해집니다."
        body = replace_first_paragraph(body, intro)
        body = replace_section(body, "## 핵심 요약", "## 먼저 확인할 신호", summary)
    else:
        first, second = topic["signals"][:2]
        intro = f"{topic['en_focus']} The goal is to leave **{first}** and **{second}** so the next review can start with a decision, not setup."
        summary = f"{topic['en_focus']}\n\nStart small: one subject, one unit, and one retrieval question. A closing record with **{first}** and **{second}** is enough to decide what to repeat or reduce next time."
        body = replace_first_paragraph(body, intro)
        body = replace_section(body, "## Quick Summary", "## Signals To Check First", summary)
    path.write_text(fm + body, encoding="utf-8")


def revise_economy(topic: dict[str, object], lang: str) -> None:
    slug = str(topic["slug"])
    path = find_post(lang, slug, f"economy-{slug}")
    fm, body = split_front_matter(path.read_text(encoding="utf-8"))
    if lang == "ko":
        first, second = topic["ko_signals"][:2]
        text = f"{topic['ko_focus']} **{first}**와 **{second}**를 발표일, 기준 기간, 물가·임금·이자·환율 경로와 함께 읽어야 가계 의사결정에 쓸 수 있습니다."
    else:
        first, second = topic["signals"][:2]
        text = f"{topic['en_focus']} Read **{first}** and **{second}** with release date, reference period, and the path into prices, wages, interest payments, or exchange rates."
    path.write_text(fm + replace_first_paragraph(body, text), encoding="utf-8")


def revise_digital(topic: dict[str, object], lang: str) -> None:
    slug = str(topic["slug"])
    path = find_post(lang, slug, f"digital-security-{slug}")
    fm, body = split_front_matter(path.read_text(encoding="utf-8"))
    if lang == "ko":
        text = f"{topic['ko_risk']} 대응은 '{topic['ko_actions'][0]}'에서 시작해 증거 보존, 별도 확인, 복구 순서를 차례로 밟아야 합니다."
        body = replace_first_paragraph(body, text)
    else:
        text = f"{topic['en_risk']} Start with: {str(topic['en_actions'][0]).rstrip('.').lower()}. Then preserve evidence, verify through a separate route, and recover accounts in order."
        body = replace_first_paragraph(body, text)
        body = replace_paragraph_containing(
            body,
            "This guide is not a product recommendation.",
            f"Use this as a response routine for **{topic['en_signals'][0]}**: act through official routes, keep records, and involve the right owner when money, work, or family accounts are exposed.",
        )
    path.write_text(fm + body, encoding="utf-8")


def revise_health(topic: dict[str, object], lang: str) -> None:
    slug = str(topic["slug"])
    path = find_post(lang, slug, f"health-literacy-{slug}")
    fm, body = split_front_matter(path.read_text(encoding="utf-8"))
    if lang == "ko":
        signal = topic["ko_signals"][0]
        text = f"{topic['ko_focus']} **{signal}**처럼 관찰 가능한 변화를 시작 시점, 지속시간, 일상 기능 변화와 함께 적어야 도움을 요청할 기준이 분명해집니다."
    else:
        signal = topic["signals"][0]
        text = f"{topic['en_focus']} Track **{signal}** with start date, duration, daily-function impact, and safety concerns so the threshold for qualified help is clearer."
    path.write_text(fm + replace_first_paragraph(body, text), encoding="utf-8")


def revise_agent_cli(topic: dict[str, object], lang: str) -> None:
    slug = str(topic["slug"])
    translation_id = f"ai-agent-cli-{slug}"
    path = find_post(lang, slug, translation_id)
    fm, body = split_front_matter(path.read_text(encoding="utf-8"))
    if lang == "ko":
        text = f"2026년 5월 24일 기준 공식 문서와 CLI 동작을 기준으로, 이 글은 **{topic['ko_title']}**에서 먼저 확인할 설정과 실패 지점을 정리합니다. 핵심 판단은 {topic['ko_answer']}"
    else:
        text = f"Checked against official documentation on May 24, 2026, this post focuses on the setup and failure points behind **{topic['en_title']}**. The practical baseline is: {topic['en_answer']}"
    path.write_text(fm + replace_first_paragraph(body, text), encoding="utf-8")


def main() -> None:
    changed = 0
    for topic in AI.TOPICS:
        for lang in ("ko", "en"):
            revise_ai(topic, lang)
            changed += 1
    for topic in STUDY.TOPICS:
        for lang in ("ko", "en"):
            revise_study(topic, lang)
            changed += 1
    for topic in ECONOMY.TOPICS:
        for lang in ("ko", "en"):
            revise_economy(topic, lang)
            changed += 1
    for topic in DIGITAL.TOPICS:
        for lang in ("ko", "en"):
            revise_digital(topic, lang)
            changed += 1
    for topic in HEALTH.TOPICS:
        for lang in ("ko", "en"):
            revise_health(topic, lang)
            changed += 1
    for topic in AGENT_CLI.TOPICS:
        for lang in ("ko", "en"):
            revise_agent_cli(topic, lang)
            changed += 1
    print(f"Defingerprinted {changed} generated posts.")


if __name__ == "__main__":
    main()
