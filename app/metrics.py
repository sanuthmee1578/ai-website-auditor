from __future__ import annotations

from typing import Any


def _count_words(visible_text: str) -> int:
    return len(visible_text.split())


def calculate_metrics(scraped_page: dict[str, Any]) -> dict[str, Any]:
    visible_text = scraped_page.get("visible_text", "")
    h1_texts = scraped_page.get("h1_texts", [])
    h2_texts = scraped_page.get("h2_texts", [])
    h3_texts = scraped_page.get("h3_texts", [])
    images = scraped_page.get("images", [])
    cta_candidates = scraped_page.get("cta_candidates", [])

    return {
        "word_count": _count_words(visible_text),
        "h1_count": len(h1_texts),
        "h2_count": len(h2_texts),
        "h3_count": len(h3_texts),
        "cta_count": len(cta_candidates),
        "image_count": len(images),
        "meta_title": scraped_page.get("meta_title", ""),
        "meta_description": scraped_page.get("meta_description", ""),
    }
