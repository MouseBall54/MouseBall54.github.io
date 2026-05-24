#!/usr/bin/env python3
"""Revise repeated generated text in safety, finance, and consumer posts."""

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


DIGITAL = load_module("generate_digital_security_posts")
HEALTH = load_module("generate_health_literacy_posts")
FINANCE = load_module("generate_personal_finance_posts")
CONSUMER = load_module("generate_consumer_rights_posts")


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


def replace_paragraph_containing(body: str, needle: str, replacement: str) -> str:
    pattern = rf"(?m)^.*{re.escape(needle)}.*(?:\n(?!\n).*)*\n"
    updated, count = re.subn(pattern, replacement.rstrip() + "\n", body, count=1)
    if count != 1:
        raise RuntimeError(f"paragraph not found: {needle}")
    return updated


def replace_section(body: str, start_heading: str, end_heading: str, replacement: str) -> str:
    pattern = rf"({re.escape(start_heading)}\n\n)(.*?)({re.escape(end_heading)}\n)"
    updated, count = re.subn(pattern, rf"\1{replacement.rstrip()}\n\n\3", body, count=1, flags=re.DOTALL)
    if count != 1:
        raise RuntimeError(f"section not found: {start_heading}")
    return updated


def digital_signals(topic: dict[str, object], lang: str) -> str:
    if lang == "ko":
        templates = [
            "메시지나 앱 안에서 바로 해결하지 말고, 저장된 북마크나 공식 앱처럼 통제 가능한 경로에서 다시 확인합니다.",
            "화면 캡처, 발신 주소, 결제 요청, 로그인 기록을 먼저 보존합니다. 증거를 남긴 뒤 차단하거나 신고해야 복구가 쉽습니다.",
            "비밀번호 변경, MFA 재설정, 연결 기기 삭제처럼 복구 순서를 정합니다. 중요한 계정은 한 번에 하나씩 처리합니다.",
            "가족, 회사, 결제 권한이 연결되어 있으면 담당자에게 빠르게 공유합니다. 빠른 보고는 피해 확산을 줄이는 보안 절차입니다.",
        ]
        signals = topic["ko_signals"]
    else:
        templates = [
            "Do not fix the issue inside the message or app that triggered it. Recheck through a saved bookmark, official app, or another trusted route.",
            "Preserve screenshots, sender details, payment requests, and login history first. Evidence makes blocking, reporting, and recovery more reliable.",
            "Define the recovery order: password change, MFA reset, connected-device review, and payment alert checks. Handle important accounts one at a time.",
            "If family, work, customer data, or payment authority is involved, tell the responsible person quickly. Fast reporting limits the damage.",
        ]
        signals = topic["en_signals"]
    return "\n".join(f"- **{signal}**: {templates[index % len(templates)]}" for index, signal in enumerate(signals))


def digital_checklist(topic: dict[str, object], lang: str) -> str:
    if lang == "ko":
        actions = topic["ko_actions"]
        extras = ["로그인 기록과 연결 기기를 함께 확인합니다.", "보안 설정을 바꾼 날짜와 이유를 기록합니다."]
        return "\n".join([f"- {action}" for action in actions] + [f"- {item}" for item in extras])
    actions = [str(action).rstrip(".") for action in topic["en_actions"]]
    extras = ["Review login history and connected devices together.", "Record the date and reason when you change a security setting."]
    return "\n".join([f"- {action[0].upper() + action[1:]}." for action in actions] + [f"- {item}" for item in extras])


def health_signals(topic: dict[str, object], lang: str) -> str:
    if lang == "ko":
        templates = [
            "시작 시점, 지속시간, 빈도, 악화·완화 요인을 같은 형식으로 기록합니다. 갑작스러운 악화나 안전 문제가 있으면 전문 도움을 우선합니다.",
            "일상 기능에 미치는 영향을 함께 적습니다. 통증이나 불편감의 강도보다 학교, 일, 수면, 식사에 미친 변화가 판단에 도움이 됩니다.",
            "나이, 임신, 기저질환, 복용약, 최근 감염이나 외상 여부를 같이 확인합니다. 같은 신호도 조건에 따라 의미가 달라집니다.",
            "호흡곤란, 흉통, 의식 변화, 심한 출혈, 자해 위험처럼 긴급 신호가 있으면 기록보다 응급 도움 요청이 먼저입니다.",
        ]
        signals = topic["ko_signals"]
    else:
        templates = [
            "Record start date, duration, frequency, triggers, and relieving factors in the same format. Sudden worsening or safety concerns should move professional help first.",
            "Write the effect on daily function. Changes in school, work, sleep, eating, or mobility often matter more than a vague severity label.",
            "Check age, pregnancy, existing conditions, medicines, recent infection, and injury. The same sign can mean different things under different conditions.",
            "For breathing trouble, chest pain, confusion, severe bleeding, self-harm risk, or other emergency signs, seeking urgent help comes before record keeping.",
        ]
        signals = topic["signals"]
    return "\n".join(f"- **{signal}**: {templates[index % len(templates)]}" for index, signal in enumerate(signals))


def health_checklist(topic: dict[str, object], lang: str) -> str:
    if lang == "ko":
        actions = topic["ko_actions"]
        extras = ["증상이나 습관이 일상 기능에 미친 변화를 적습니다.", "공식 보건 자료와 의료 전문가를 통해 다시 확인합니다."]
        return "\n".join([f"- {action}" for action in actions] + [f"- {item}" for item in extras])
    actions = [str(action).rstrip(".") for action in topic["en_actions"]]
    extras = ["Write how symptoms or habits affect daily function.", "Recheck health information through official local guidance and qualified medical professionals."]
    return "\n".join([f"- {action[0].upper() + action[1:]}." for action in actions] + [f"- {item}" for item in extras])


def finance_checklist(topic: dict[str, object], lang: str) -> str:
    if lang == "ko":
        actions = topic["ko_actions"]
        extras = ["수수료, 세금, 계약 조건, 유동성 제한을 함께 확인합니다.", "개인 상황에 적용하기 전 현지 금융·세금 규칙을 다시 확인합니다."]
        return "\n".join([f"- {action}" for action in actions] + [f"- {item}" for item in extras])
    actions = [str(action).rstrip(".") for action in topic["en_actions"]]
    extras = ["Check fees, taxes, contract terms, and liquidity limits together.", "Verify local financial and tax rules before applying the idea to your situation."]
    return "\n".join([f"- {action[0].upper() + action[1:]}." for action in actions] + [f"- {item}" for item in extras])


def revise_digital(topic: dict[str, object], lang: str) -> None:
    path = find_post(lang, str(topic["slug"]))
    fm, body = split_front_matter(path.read_text(encoding="utf-8"))
    if lang == "ko":
        body = replace_first_paragraph(
            body,
            f"이 글은 **{topic['ko_title']}**를 제품 추천이 아니라 압박 상황에서 따라야 할 확인 절차로 정리합니다. 작은 보안 신호도 돈, 개인정보, 가족 안전, 업무 계정으로 이어질 수 있으므로 멈춤, 별도 확인, 기록 보존, 복구 순서를 미리 정해 둡니다.",
        )
        body = replace_section(body, "## 먼저 볼 위험 신호", "## 바로 적용할 순서", digital_signals(topic, lang))
        body = replace_section(body, "## 월간 점검 체크리스트", "## 참고할 공식 자료", digital_checklist(topic, lang))
    else:
        body = replace_first_paragraph(
            body,
            f"This guide treats **{topic['en_title']}** as a pressure-tested security routine, not a product recommendation. Small warning signs can affect money, privacy, family safety, and work accounts, so the routine starts with pause, separate verification, evidence preservation, and recovery order.",
        )
        body = replace_section(body, "## Warning Signals To Check First", "## Practical Setup Order", digital_signals(topic, lang))
        body = replace_section(body, "## Monthly Checkup", "## Source Notes", digital_checklist(topic, lang))
    path.write_text(fm + body, encoding="utf-8")


def revise_health(topic: dict[str, object], lang: str) -> None:
    path = find_post(lang, str(topic["slug"]))
    fm, body = split_front_matter(path.read_text(encoding="utf-8"))
    if lang == "ko":
        body = replace_first_paragraph(
            body,
            f"이 글은 **{topic['ko_title']}**를 스스로 진단하는 방법이 아니라 관찰 가능한 신호를 정리하고 도움을 요청할 시점을 구분하는 건강 문해력 루틴으로 다룹니다.",
        )
        body = replace_section(body, "## 먼저 볼 신호", "## 생활 속 실행 순서", health_signals(topic, lang))
        body = replace_section(body, "## 월간 점검 체크리스트", "## 참고할 공식 자료", health_checklist(topic, lang))
    else:
        body = replace_first_paragraph(
            body,
            f"This guide treats **{topic['en_title']}** as a health-literacy routine, not self-diagnosis. The goal is to track observable signs, describe daily-function changes, and know when qualified help is safer than waiting.",
        )
        body = replace_paragraph_containing(
            body,
            "This article is educational and is not diagnosis or treatment advice",
            f"This article is educational and does not diagnose, treat, or set dosage for **{topic['en_title']}**. Sudden worsening, breathing trouble, chest pain, confusion, self-harm thoughts, severe bleeding, or any immediate safety concern should be handled through local emergency services or qualified medical professionals.",
        )
        body = replace_section(body, "## Signals To Check First", "## Practical Order", health_signals(topic, lang))
        body = replace_section(body, "## Monthly Checkup", "## Source Notes", health_checklist(topic, lang))
    path.write_text(fm + body, encoding="utf-8")


def revise_finance(topic: dict[str, object], lang: str) -> None:
    path = find_post(lang, str(topic["slug"]))
    fm, body = split_front_matter(path.read_text(encoding="utf-8"))
    if lang == "en":
        body = replace_paragraph_containing(
            body,
            "This article is educational and is not individualized financial advice",
            f"This article is educational and does not give individualized investment, tax, lending, or legal advice for **{topic['en_title']}**. Use it to organize questions, then verify local rules, fees, contracts, and personal risk capacity before acting.",
        )
        body = replace_section(body, "## Monthly Checkup", "## Source Notes", finance_checklist(topic, lang))
    else:
        body = replace_section(body, "## 월간 점검 체크리스트", "## 참고할 공식 자료", finance_checklist(topic, lang))
    path.write_text(fm + body, encoding="utf-8")


def revise_consumer(topic: dict[str, object], lang: str) -> None:
    path = find_post(lang, str(topic["slug"]))
    fm, body = split_front_matter(path.read_text(encoding="utf-8"))
    if lang == "en":
        body = replace_paragraph_containing(
            body,
            "This article is educational information, not legal advice",
            f"This article is educational and does not provide legal advice for **{topic['en_title']}**. It focuses on preserving evidence, checking dates and contract wording, and choosing the right seller, platform, payment-provider, carrier, or regulator channel.",
        )
    path.write_text(fm + body, encoding="utf-8")


def main() -> None:
    changed = 0
    for topic in DIGITAL.TOPICS:
        for lang in ("ko", "en"):
            revise_digital(topic, lang)
            changed += 1
    for topic in HEALTH.TOPICS:
        for lang in ("ko", "en"):
            revise_health(topic, lang)
            changed += 1
    for topic in FINANCE.TOPICS:
        for lang in ("ko", "en"):
            revise_finance(topic, lang)
            changed += 1
    for topic in CONSUMER.TOPICS:
        for lang in ("ko", "en"):
            revise_consumer(topic, lang)
            changed += 1
    print(f"Revised {changed} safety/finance/consumer posts.")


if __name__ == "__main__":
    main()
