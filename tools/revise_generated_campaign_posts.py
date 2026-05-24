#!/usr/bin/env python3
"""Revise weak generated campaign post sections without changing metadata."""

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
EASY = load_module("generate_easy_labeling_posts")


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


def replace_section_until_image(body: str, heading: str, replacement: str) -> str:
    pattern = rf"({re.escape(heading)}\n\n)(.*?)(\n\n!\[)"
    updated, count = re.subn(pattern, rf"\1{replacement.rstrip()}\3", body, count=1, flags=re.DOTALL)
    if count != 1:
        raise RuntimeError(f"section not found: {heading}")
    return updated


def ai_signal_block(topic: dict[str, object], lang: str) -> str:
    if lang == "ko":
        signals = list(topic["ko_signals"])
        templates = [
            "이 기준은 에이전트가 실제로 접근할 수 있는 도구, 데이터, 실행 권한을 정합니다. 읽기, 초안 작성, 외부 실행을 분리해 적고 금지 작업을 예외 없이 표시합니다.",
            "이 기준은 사람이 반드시 확인해야 하는 지점을 정합니다. 비용 발생, 사용자 영향, 외부 전송, 파일 삭제처럼 되돌리기 어려운 행동은 승인 전에는 실행하지 않게 둡니다.",
            "이 기준은 사후 검토가 가능한 기록을 남깁니다. 입력 자료, 사용한 도구, 판단 근거, 실패 원인을 같은 위치에 남겨 다음 실험과 비교할 수 있어야 합니다.",
            "이 기준은 실패 후 복구 방법을 정합니다. 이전 버전, 담당자, 중단 조건, 사용자 알림 필요 여부를 미리 적어 자동화가 멈췄을 때 바로 되돌릴 수 있게 합니다.",
        ]
    else:
        signals = list(topic["signals"])
        templates = [
            "Define the tools, data, and execution rights the agent can actually use. Separate read, draft, and external execution permissions, and write down prohibited actions explicitly.",
            "Define where a human must approve the workflow. Costly actions, user-impacting output, external transfer, and file deletion should remain blocked until this gate passes.",
            "Keep enough evidence for later review. Store the input, tool call, decision reason, and failure class together so the next run can be compared against the same standard.",
            "Define the recovery path before the workflow runs. Name the previous version, owner, stop condition, and user-notice rule so a failed automation can be reversed quickly.",
        ]

    return "\n".join(f"- **{signal}**: {templates[index % len(templates)]}" for index, signal in enumerate(signals))


def easy_signal_block(topic: dict[str, object], lang: str) -> str:
    if lang == "ko":
        signals = list(topic["ko_signals"])
        templates = [
            "작업 전에 기준을 문서로 고정합니다. 라벨러가 같은 이미지를 봤을 때 같은 결정을 내릴 수 있도록 포함 기준, 제외 기준, 예외 예시를 함께 둡니다.",
            "파일럿 배치에서 바로 확인합니다. 전체 데이터를 열기 전에 20~50장 샘플로 좌표, 클래스, 저장 경로가 학습 폴더와 맞는지 봅니다.",
            "애매한 사례를 질문 로그나 edge case gallery에 남깁니다. 반복 질문이 생기면 개인 판단으로 넘기지 말고 지침서 버전을 올립니다.",
            "학습팀에 넘기기 전 검수 기록과 함께 묶습니다. 이미지, 라벨, 클래스 파일, 변환 스크립트, 검수 샘플이 같은 버전을 가리켜야 합니다.",
        ]
    else:
        signals = list(topic["signals"])
        templates = [
            "Freeze the rule before labeling starts. Include positive examples, exclusion rules, and edge cases so two labelers can make the same decision on the same image.",
            "Check it in a pilot batch first. Before opening the full dataset, use 20 to 50 samples to verify coordinates, classes, and save paths against the training folder.",
            "Capture ambiguous cases in a question log or edge-case gallery. When the same question repeats, update the instruction version instead of relying on individual judgment.",
            "Package it with the QA record before handoff. Images, labels, class files, conversion scripts, and reviewed samples should point to the same dataset version.",
        ]

    return "\n".join(f"- **{signal}**: {templates[index % len(templates)]}" for index, signal in enumerate(signals))


def revise_ai_post(topic: dict[str, object], lang: str) -> None:
    slug = str(topic["slug"])
    path = find_post(lang, slug)
    front_matter, body = split_front_matter(path.read_text(encoding="utf-8"))

    if lang == "ko":
        intro = (
            f"이 글은 **{topic['ko_title']}**를 유행어가 아니라 운영 설계 문제로 다룹니다. "
            "그래서 먼저 정해야 할 것은 모델 이름이 아니라 사용 범위, 검증 기준, 사람이 멈춰야 할 지점입니다."
        )
        body = replace_first_paragraph(body, intro)
        body = replace_section_until_image(body, "## 먼저 볼 신호", ai_signal_block(topic, lang))
    else:
        intro = (
            f"This guide treats **{topic['en_title']}** as an operating-design problem, not a trend label. "
            "The first decision is therefore not which model to use, but where scope, verification, and human stop points are defined."
        )
        body = replace_first_paragraph(body, intro)
        body = replace_section_until_image(body, "## Signals To Check First", ai_signal_block(topic, lang))

    path.write_text(front_matter + body, encoding="utf-8")


def revise_easy_post(topic: dict[str, object], lang: str) -> None:
    slug = str(topic["slug"])
    path = find_post(lang, slug)
    front_matter, body = split_front_matter(path.read_text(encoding="utf-8"))

    if lang == "ko":
        intro = (
            f"이 글은 **{topic['ko_title']}**를 라벨링 속도가 아니라 데이터셋 품질 기준으로 정리합니다. "
            "Easy Labeling은 작업을 빠르게 만들 수 있지만, 학습 가능한 데이터는 클래스 규칙과 검수 루틴이 함께 있을 때 만들어집니다."
        )
        body = replace_first_paragraph(body, intro)
        body = replace_section_until_image(body, "## 먼저 확인할 품질 신호", easy_signal_block(topic, lang))
    else:
        intro = (
            f"This guide frames **{topic['en_title']}** as a dataset-quality workflow rather than a labeling-speed trick. "
            "Easy Labeling can make the work faster, but trainable data still depends on class rules and review routines."
        )
        body = replace_first_paragraph(body, intro)
        body = replace_section_until_image(body, "## Quality Signals To Check First", easy_signal_block(topic, lang))

    path.write_text(front_matter + body, encoding="utf-8")


def main() -> None:
    changed = 0
    for topic in AI.TOPICS:
        for lang in ("ko", "en"):
            revise_ai_post(topic, lang)
            changed += 1

    for topic in EASY.TOPICS:
        for lang in ("ko", "en"):
            revise_easy_post(topic, lang)
            changed += 1

    print(f"Revised {changed} generated campaign posts.")


if __name__ == "__main__":
    main()
