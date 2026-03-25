from __future__ import annotations

from typing import Any


SYSTEM_PROMPT = """You are a senior website strategist reviewing a single webpage.
Use only the provided extracted data and metrics.
Avoid generic advice.
Ground all insights in the supplied content and metrics.
Return structured analysis only."""


def build_ai_input(
    scraped_page: dict[str, Any],
    metrics: dict[str, Any],
    content_word_limit: int = 150,
) -> dict[str, Any]:
    content_words = scraped_page.get("visible_text", "").split()
    content_snippet = " ".join(content_words[:content_word_limit])

    return {
        "url": scraped_page.get("url", ""),
        "page_title": scraped_page.get("page_title", ""),
        "meta_title": scraped_page.get("meta_title", ""),
        "meta_description": scraped_page.get("meta_description", ""),
        "h1_texts": scraped_page.get("h1_texts", []),
        "h2_texts": scraped_page.get("h2_texts", []),
        "h3_texts": scraped_page.get("h3_texts", []),
        "cta_candidates": scraped_page.get("cta_candidates", []),
        "content_snippet": content_snippet,
        "metrics": metrics,
    }
