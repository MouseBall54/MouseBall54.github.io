#!/usr/bin/env python3
"""Move remaining clustered post dates to open days while preserving URLs."""

from __future__ import annotations

import re
from collections import Counter
from datetime import date, timedelta
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
KEEP_CLUSTER_DATE = "2026-05-23"
TARGET_START = date(2025, 1, 6)
TARGET_END = date(2026, 5, 22)
MAX_NON_CAMPAIGN_POSTS_PER_LANG_PER_DAY = 8


def slug_for(path: Path) -> str:
    return re.sub(r"^\d{4}-\d{2}-\d{2}-", "", path.stem)


def post_date_for(path: Path) -> str:
    return path.name[:10]


def update_date_line(text: str, new_date: str, minute: int) -> str:
    replacement = f"date: {new_date}T07:{minute:02d}:00+09:00"
    updated, count = re.subn(r"^date:\s*\d{4}-\d{2}-\d{2}T[^\n]+$", replacement, text, count=1, flags=re.MULTILINE)
    if count != 1:
        raise ValueError("date front matter line not found")
    return updated


def available_dates(used_dates: set[str], excluded_dates: set[str]) -> list[str]:
    current = TARGET_START
    values: list[str] = []
    while current <= TARGET_END:
        value = current.isoformat()
        if value not in used_dates and value not in excluded_dates:
            values.append(value)
        current += timedelta(days=1)
    return values


def move_pair(old_date: str, slug: str, new_date: str, minute: int) -> None:
    for lang in ("ko", "en"):
        source = ROOT / "_posts" / lang / f"{old_date}-{slug}.md"
        if not source.exists():
            continue

        target = ROOT / "_posts" / lang / f"{new_date}-{slug}.md"
        if target.exists():
            raise FileExistsError(target)

        text = source.read_text(encoding="utf-8")
        target.write_text(update_date_line(text, new_date, minute), encoding="utf-8")
        source.unlink()


def main() -> None:
    en_dir = ROOT / "_posts" / "en"
    en_posts = sorted(en_dir.glob("*.md"), key=lambda path: (post_date_for(path), slug_for(path)))
    counts = Counter(post_date_for(path) for path in en_posts)
    cluster_dates = {
        current_date
        for current_date, count in counts.items()
        if current_date != KEEP_CLUSTER_DATE and count > MAX_NON_CAMPAIGN_POSTS_PER_LANG_PER_DAY
    }

    used_dates = {post_date_for(path) for path in en_posts if post_date_for(path) not in cluster_dates}
    targets = available_dates(used_dates, cluster_dates)

    move_items = [(post_date_for(path), slug_for(path)) for path in en_posts if post_date_for(path) in cluster_dates]
    if len(targets) < len(move_items):
        raise RuntimeError(f"Need {len(move_items)} target dates, found {len(targets)}")

    for index, (old_date, slug) in enumerate(move_items):
        move_pair(old_date, slug, targets[index], 10 + (index % 45))

    print(f"Cluster dates moved: {', '.join(sorted(cluster_dates))}")
    print(f"Redistributed {len(move_items)} additional paired topics.")


if __name__ == "__main__":
    main()
