from __future__ import annotations

import json
from typing import Any


SYSTEM_PROMPT = """You are a senior website strategist reviewing a single webpage.
Use only the provided extracted data and metrics.
Avoid generic advice.
Ground all insights in the supplied content and metrics.
Return structured analysis only."""


OUTPUT_SHAPE = {
    "seo_structure": {
        "score": 0,
        "insight": "",
        "metric_ref": "",
    },
    "messaging_clarity": {
        "score": 0,
        "insight": "",
        "metric_ref": "",
    },
    "cta_usage": {
        "score": 0,
        "insight": "",
        "metric_ref": "",
    },
    "content_depth": {
        "score": 0,
        "insight": "",
        "metric_ref": "",
    },
    "ux_structural_concerns": {
        "score": 0,
        "insight": "",
        "metric_ref": "",
    },
    "recommendations": [
        {
            "priority": 1,
            "title": "",
            "reasoning": "",
            "action": "",
            "metric_ref": "",
            "expected_outcome": "",
        }
    ],
}


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


def build_prompt_package(
    scraped_page: dict[str, Any],
    metrics: dict[str, Any],
    content_word_limit: int = 150,
) -> dict[str, str]:
    ai_input = build_ai_input(
        scraped_page=scraped_page,
        metrics=metrics,
        content_word_limit=content_word_limit,
    )

    user_prompt = (
        "Review this single webpage using only the provided structured input.\n\n"
        f"INPUT:\n{json.dumps(ai_input, indent=2)}\n\n"
        "Return structured analysis that matches this shape:\n"
        f"{json.dumps(OUTPUT_SHAPE, indent=2)}"
    )

    return {
        "system_prompt": SYSTEM_PROMPT,
        "user_prompt": user_prompt,
    }


def analyze_page(
    scraped_page: dict[str, Any],
    metrics: dict[str, Any],
    content_word_limit: int = 150,
) -> dict[str, Any]:
    prompt_package = build_prompt_package(
        scraped_page=scraped_page,
        metrics=metrics,
        content_word_limit=content_word_limit,
    )

    return {
        "prompt_package": prompt_package,
        "analysis": OUTPUT_SHAPE,
    }
