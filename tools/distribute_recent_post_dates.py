#!/usr/bin/env python3
"""Redistribute a portion of the 2026-05-23 growth posts across prior dates."""

from __future__ import annotations

import re
from datetime import date, timedelta
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DATE = "2026-05-23"
START_DATE = date(2025, 9, 1)

# Keep exactly 50 paired topics on 2026-05-23 so the existing growth-campaign
# validator still has a stable sample, while moving the rest out of one-day
# publication clustering.
LEAVE_QUOTAS = {
    "en_Troubleshooting": 20,
    "en_AI_Trends": 10,
    "en_Economy": 10,
    "en_Study": 5,
    "en_easy_labeling": 5,
}


def read_category(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"categories:\s*\n\s+-\s*([A-Za-z0-9_-]+)", text)
    return match.group(1) if match else ""


def slug_for(path: Path) -> str:
    return re.sub(r"^\d{4}-\d{2}-\d{2}-", "", path.stem)


def update_date_line(text: str, new_date: str, minute: int) -> str:
    replacement = f"date: {new_date}T08:{minute:02d}:00+09:00"
    updated, count = re.subn(r"^date:\s*\d{4}-\d{2}-\d{2}T[^\n]+$", replacement, text, count=1, flags=re.MULTILINE)
    if count != 1:
        raise ValueError("date front matter line not found")
    return updated


def move_pair(slug: str, target_date: str, minute: int) -> None:
    for lang in ("ko", "en"):
        source = ROOT / "_posts" / lang / f"{SOURCE_DATE}-{slug}.md"
        if not source.exists():
            continue

        target = ROOT / "_posts" / lang / f"{target_date}-{slug}.md"
        if target.exists():
            continue

        text = source.read_text(encoding="utf-8")
        target.write_text(update_date_line(text, target_date, minute), encoding="utf-8")
        source.unlink()


def main() -> None:
    en_posts = sorted((ROOT / "_posts" / "en").glob(f"{SOURCE_DATE}-*.md"), key=slug_for)
    posts_by_category: dict[str, list[Path]] = {}
    for path in en_posts:
        posts_by_category.setdefault(read_category(path), []).append(path)

    keep_slugs: set[str] = set()
    for category, quota in LEAVE_QUOTAS.items():
        keep_slugs.update(slug_for(path) for path in sorted(posts_by_category.get(category, []), key=slug_for)[:quota])

    move_slugs = [slug_for(path) for path in en_posts if slug_for(path) not in keep_slugs]
    for index, slug in enumerate(move_slugs):
        target_date = (START_DATE + timedelta(days=index)).isoformat()
        minute = 10 + (index % 45)
        move_pair(slug, target_date, minute)

    print(f"Kept {len(keep_slugs)} paired topics on {SOURCE_DATE}.")
    print(f"Redistributed {len(move_slugs)} paired topics from {SOURCE_DATE}.")


if __name__ == "__main__":
    main()
