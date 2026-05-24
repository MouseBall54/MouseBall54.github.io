#!/usr/bin/env python3
"""Revise generated Climate/Energy and Global Affairs posts."""

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


CLIMATE = load_module("generate_climate_energy_posts")
GLOBAL = load_module("generate_global_affairs_posts")


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
    if count != 1:
        return body
    return updated


def replace_section(body: str, start_heading: str, end_heading: str, replacement: str) -> str:
    pattern = rf"({re.escape(start_heading)}\n\n)(.*?)({re.escape(end_heading)}\n)"
    updated, count = re.subn(pattern, rf"\1{replacement.rstrip()}\n\n\3", body, count=1, flags=re.DOTALL)
    if count != 1:
        raise RuntimeError(f"section not found: {start_heading}")
    return updated


def climate_matter(topic: dict[str, object], lang: str) -> str:
    if lang == "ko":
        first, second, third = topic["ko_signals"][:3]
        return (
            f"{topic['ko_context']}\n\n"
            f"{topic['ko_angle']} 국내 비용 경로는 **{first}**, **{second}**, **{third}** 세 신호의 움직이는 순서를 볼 때 드러납니다. "
            "한 달 수치나 제목 하나로 판단하지 말고 수요, 공급, 가격, 정책 지연을 분리해 읽어야 합니다.\n\n"
            "찬반 구도만으로는 실행 리스크가 보이지 않습니다. 수요가 움직여도 공급 병목이 그대로면 비용은 늦게 나타나고, 가격이 안정돼 보여도 계통·허가·금융 조건이 뒤에서 제약이 될 수 있습니다."
        )
    first, second, third = topic["signals"][:3]
    return (
        f"{topic['en_context']}\n\n"
        f"{topic['en_angle']} The domestic cost path becomes clearer when **{first}**, **{second}**, and **{third}** are read as a sequence. "
        "Do not treat one monthly number or one headline as the whole story; separate demand, supply, price, and policy lag.\n\n"
        "A simple for-or-against debate hides implementation risk. Demand can move before supply bottlenecks clear, and stable prices can still hide grid, permitting, or financing constraints."
    )


def climate_structure(topic: dict[str, object], lang: str) -> str:
    if lang == "ko":
        s = topic["ko_signals"]
        return "\n".join(
            [
                f"- **수요**: **{s[0]}**의 증가 위치와 시간대를 확인합니다.",
                f"- **공급**: **{s[1]}**가 실제 공급 능력인지 병목인지 구분합니다.",
                f"- **가격**: **{s[2]}**가 전기요금, 수입비용, 산업 원가로 옮겨 가는 시차를 봅니다.",
                f"- **리스크**: **{s[3]}**가 정책, 기후, 공급망 중 어디에서 오는지 분리합니다.",
            ]
        )
    s = topic["signals"]
    return "\n".join(
        [
            f"- **Demand**: use **{s[0]}** to locate where and when exposure is changing.",
            f"- **Supply**: use **{s[1]}** to test whether the issue is real capacity or a bottleneck.",
            f"- **Price**: use **{s[2]}** to trace the lag into tariffs, import costs, or industrial margins.",
            f"- **Risk**: use **{s[3]}** to separate policy, climate, and supply-chain risk.",
        ]
    )


def climate_signals(topic: dict[str, object], lang: str) -> str:
    if lang == "ko":
        templates = [
            "방향과 지속 기간을 함께 봅니다. 하루짜리 가격 변화인지 여러 분기 동안 이어질 물량 변화인지 구분해야 합니다.",
            "국내 전달 경로를 적습니다. 전기요금, 수입 물가, 산업 원가, 지역 인프라 중 어디에 먼저 닿는지 표시합니다.",
            "실행 병목을 확인합니다. 계통 접속, 허가, 금융, 장비, 인력, 지역 수용성이 발표 목표를 지연시킬 수 있습니다.",
            "정책 가정을 분리합니다. 보조금, 규제, 세금, 국제 규칙이 바뀌면 같은 기술도 비용 구조가 달라집니다.",
        ]
        signals = topic["ko_signals"]
    else:
        templates = [
            "Read direction together with duration. A one-day price move and a multi-quarter volume shift require different decisions.",
            "Write the domestic transmission channel. Mark whether it reaches tariffs, import prices, industrial costs, or local infrastructure first.",
            "Check the implementation bottleneck. Grid connection, permits, finance, equipment, labour, and local acceptance can delay headline targets.",
            "Separate the policy assumption. Subsidies, regulation, taxes, and international rules can change the cost structure of the same technology.",
        ]
        signals = topic["signals"]
    return "\n".join(f"- **{signal}**: {templates[index % len(templates)]}" for index, signal in enumerate(signals))


def climate_checklist(topic: dict[str, object], lang: str) -> str:
    if lang == "ko":
        actions = topic["ko_actions"]
        return "\n".join(
            [f"- {action}" for action in actions]
            + [
                "기준 연도, 지역 범위, 단위, 정책 가정을 먼저 확인합니다.",
                "한국의 수입 구조, 전력망 위치, 산업 노출, 가계 비용 중 어느 경로로 이어지는지 표시합니다.",
            ]
        )
    actions = [str(action).rstrip(".") for action in topic["en_actions"]]
    return "\n".join(
        [f"- {action[0].upper() + action[1:]}." for action in actions]
        + [
            "Check baseline year, geography, unit, and policy assumptions first.",
            "Translate the signal into Korea's import structure, grid geography, industrial exposure, or household cost channel.",
        ]
    )


def climate_numbers(topic: dict[str, object], lang: str) -> str:
    if lang == "ko":
        first, second, third = topic["ko_signals"][:3]
        return (
            "기후·에너지 자료는 기준 연도, 지역 범위, 단위가 바뀌면 결론도 달라집니다. 평균값만 보지 말고 피크, 지연, 예외 조건을 함께 확인해야 실제 리스크를 놓치지 않습니다.\n\n"
            f"먼저 **기준선, 기간, 단위, 지역 범위, 정책 가정**을 확인하세요. 그다음 **{first}**, **{second}**, **{third}**가 한국의 수입 구조, 전력망 위치, 산업 노출, 가계 비용 중 어디로 연결되는지 표시해야 합니다."
        )
    first, second, third = topic["signals"][:3]
    return (
        "Climate and energy numbers can change meaning when baseline year, region, or unit changes. Peaks, delays, and exceptions often matter more than averages.\n\n"
        f"Check the **baseline, period, unit, geographic coverage, and policy assumptions** first. Then translate **{first}**, **{second}**, and **{third}** into Korea's import structure, grid geography, industrial exposure, or household cost channels."
    )


def global_intro(topic: dict[str, object], lang: str) -> str:
    if lang == "ko":
        first = topic["ko_signals"][0]
        return (
            f"{topic['ko_summary']}\n\n"
            f"한국 독자에게 중요한 질문은 사건 자체보다 **{first}** 변화가 수출, 수입물가, 환율, 에너지 비용, 안보 비용 중 어디로 전달되는지입니다. "
            "공식 자료의 수치와 해설 기사의 해석을 분리해 읽어야 다음 뉴스의 의미가 선명해집니다."
        )
    first = topic["signals"][0]
    return (
        f"{topic['en_summary']}\n\n"
        f"For Korean readers, the practical question is where **{first}** flows first: exports, import prices, exchange rates, energy costs, or security budgets. "
        "Keep official data separate from commentary so the next update can be read with a clearer baseline."
    )


def global_matter(topic: dict[str, object], lang: str) -> str:
    if lang == "ko":
        first, second = topic["ko_signals"][:2]
        return (
            f"{topic['ko_angle']}\n\n"
            f"먼저 **{first}**의 방향을 보고, 이어서 **{second}**가 가격, 물량, 정책 대응, 금융 조건 중 어디로 번지는지 확인합니다. "
            "일시적 가격 충격, 분기 단위 공급 차질, 장기 제도 변화는 한국 기업과 가계에 전혀 다른 결정을 요구합니다."
        )
    first, second = topic["signals"][:2]
    return (
        f"{topic['en_angle']}\n\n"
        f"Start with **{first}**, then check whether **{second}** is moving through prices, physical supply, policy response, or financing conditions. "
        "A short market shock, a quarter-long supply disruption, and a permanent rule change require different decisions."
    )


def global_signals(topic: dict[str, object], lang: str) -> str:
    if lang == "ko":
        templates = [
            "숫자보다 방향, 발표 기준일, 정책 반응을 함께 봅니다. 기준일이 다르면 같은 사건도 다른 결론으로 보일 수 있습니다.",
            "국내 기사와 외부 원인을 연결합니다. 수출 주문, 수입 가격, 환율, 에너지 비용, 안보 예산 중 먼저 움직이는 항목을 표시합니다.",
            "재고와 계약 완충을 확인합니다. 시장 가격이 안정돼 보여도 운송, 보험, 규제 준수 비용은 늦게 반영될 수 있습니다.",
            "후속 보고서를 정합니다. 공식 통계, 국제기구 전망, 정부 발표 중 어느 자료가 다음 판단을 바꿀지 미리 정해 둡니다.",
        ]
        signals = topic["ko_signals"]
    else:
        templates = [
            "Read direction, reference date, and policy response together. A different cutoff date can make the same event look different.",
            "Connect domestic headlines to external causes. Mark whether exports, import prices, exchange rates, energy costs, or security budgets move first.",
            "Check inventory and contract cushions. Market prices can look stable while shipping, insurance, or compliance costs pass through later.",
            "Choose the next source to watch. Decide whether official statistics, institutional forecasts, or government releases would change the baseline.",
        ]
        signals = topic["signals"]
    return "\n".join(f"- **{signal}**: {templates[index % len(templates)]}" for index, signal in enumerate(signals))


def global_checklist(topic: dict[str, object], lang: str) -> str:
    if lang == "ko":
        s = topic["ko_signals"]
        return "\n".join(
            [
                f"- **{s[0]}** 변화가 가격 충격인지 물량 충격인지 구분합니다.",
                f"- **{s[1]}**가 하루짜리 뉴스인지 분기 단위 구조 변화인지 확인합니다.",
                f"- **{s[2]}**와 관련된 한국 연결 경로를 수출, 수입물가, 금융시장, 안보비용, 생활비 중 하나로 표시합니다.",
                "공식 자료와 해설 기사, 전망과 확정 통계를 분리합니다.",
                "발표일, 기준 기간, 가정을 확인한 뒤 다음 판단에 사용합니다.",
            ]
        )
    s = topic["signals"]
    return "\n".join(
        [
            f"- Decide whether **{s[0]}** is creating a price shock, a volume shock, or both.",
            f"- Check whether **{s[1]}** is a short news cycle or a structural change that can last for quarters.",
            f"- Mark the Korea-facing channel for **{s[2]}**: exports, import prices, financial markets, security costs, or household costs.",
            "- Separate official data from interpretation and commentary.",
            "- Check release date, reference period, and assumptions before using any forecast.",
        ]
    )


def revise_climate(topic: dict[str, object], lang: str) -> None:
    slug = str(topic["slug"])
    path = find_post(lang, slug, f"climate-energy-{slug}")
    fm, body = split_front_matter(path.read_text(encoding="utf-8"))
    if lang == "ko":
        body = replace_paragraph_containing(
            body,
            "교육용 브리핑입니다",
            f"이 글은 투자, 법률, 에너지 제품 구매 조언이 아닙니다. **{topic['ko_title']}**을 공식 자료와 한국 비용 경로 관점에서 읽기 위한 교육용 글입니다.",
        )
        body = replace_section(body, "## 왜 지금 봐야 하나", "## 핵심 구조", climate_matter(topic, lang))
        body = replace_section(body, "## 핵심 구조", "## 현재 읽어야 할 신호", climate_structure(topic, lang))
        body = replace_section(body, "## 현재 읽어야 할 신호", "## 국내 연결 경로", climate_signals(topic, lang))
        body = replace_section(body, "## 실무 체크리스트", "## 숫자를 볼 때 주의할 점", climate_checklist(topic, lang))
        body = replace_section(body, "## 숫자를 볼 때 주의할 점", "## 공식 자료로 다시 확인하기", climate_numbers(topic, lang))
    else:
        body = replace_paragraph_containing(
            body,
            "This article is an educational briefing",
            f"This article is educational and does not provide investment, legal, or energy-product advice for **{topic['en_title']}**. It uses official-source context to connect the issue with costs, infrastructure, policy, and Korea-facing channels.",
        )
        body = replace_section(body, "## Why This Matters Now", "## Core Structure", climate_matter(topic, lang))
        body = replace_section(body, "## Core Structure", "## Signals To Watch", climate_structure(topic, lang))
        body = replace_section(body, "## Signals To Watch", "## Korea-Facing Transmission", climate_signals(topic, lang))
        body = replace_section(body, "## Practical Checklist", "## How To Read The Numbers", climate_checklist(topic, lang))
        body = replace_section(body, "## How To Read The Numbers", "## Source Notes", climate_numbers(topic, lang))
    path.write_text(fm + body, encoding="utf-8")


def revise_global(topic: dict[str, object], lang: str) -> None:
    slug = str(topic["slug"])
    path = find_post(lang, slug, f"global-affairs-{slug}")
    fm, body = split_front_matter(path.read_text(encoding="utf-8"))
    if lang == "ko":
        body = replace_first_paragraph(body, global_intro(topic, lang))
        body = replace_section(body, "## 왜 지금 중요한가", "## 핵심 신호", global_matter(topic, lang))
        body = replace_section(body, "## 핵심 신호", "## 한국 독자 관점", global_signals(topic, lang))
        body = replace_section(body, "## 독자 체크리스트", "## 참고할 공식 자료", global_checklist(topic, lang))
    else:
        body = replace_first_paragraph(body, global_intro(topic, lang))
        body = replace_section(body, "## Why This Issue Matters", "## Current Signals To Watch", global_matter(topic, lang))
        body = replace_section(body, "## Current Signals To Watch", "## Korea-Facing Angle", global_signals(topic, lang))
        body = replace_section(body, "## Reader Checklist", "## Source Notes", global_checklist(topic, lang))
    path.write_text(fm + body, encoding="utf-8")


def main() -> None:
    changed = 0
    for topic in CLIMATE.TOPICS:
        for lang in ("ko", "en"):
            revise_climate(topic, lang)
            changed += 1
    for topic in GLOBAL.TOPICS:
        for lang in ("ko", "en"):
            revise_global(topic, lang)
            changed += 1
    print(f"Revised {changed} climate/global posts.")


if __name__ == "__main__":
    main()
