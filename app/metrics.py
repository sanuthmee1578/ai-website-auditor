from __future__ import annotations

from typing import Any
from urllib.parse import urlparse


def _count_words(visible_text: str) -> int:
    return len(visible_text.split())


def _count_links(links: list[dict[str, str]], page_url: str) -> tuple[int, int]:
    internal_count = 0
    external_count = 0
    page_domain = urlparse(page_url).netloc

    for link in links:
        href = link.get("href", "")
        parsed_href = urlparse(href)

        if not parsed_href.netloc or parsed_href.netloc == page_domain:
            internal_count += 1
        else:
            external_count += 1

    return internal_count, external_count


def _get_missing_alt_percentage(images: list[dict[str, str]]) -> float:
    if not images:
        return 0.0

    missing_alt_count = 0
    for image in images:
        alt = image.get("alt", "").strip()
        if not alt:
            missing_alt_count += 1

    return round((missing_alt_count / len(images)) * 100, 2)


def calculate_metrics(scraped_page: dict[str, Any]) -> dict[str, Any]:
    visible_text = scraped_page.get("visible_text", "")
    h1_texts = scraped_page.get("h1_texts", [])
    h2_texts = scraped_page.get("h2_texts", [])
    h3_texts = scraped_page.get("h3_texts", [])
    links = scraped_page.get("links", [])
    images = scraped_page.get("images", [])
    cta_candidates = scraped_page.get("cta_candidates", [])
    internal_link_count, external_link_count = _count_links(
        links, scraped_page.get("url", "")
    )
    missing_alt_percentage = _get_missing_alt_percentage(images)

    return {
        "word_count": _count_words(visible_text),
        "h1_count": len(h1_texts),
        "h2_count": len(h2_texts),
        "h3_count": len(h3_texts),
        "cta_count": len(cta_candidates),
        "internal_link_count": internal_link_count,
        "external_link_count": external_link_count,
        "image_count": len(images),
        "missing_alt_percentage": missing_alt_percentage,
        "meta_title": scraped_page.get("meta_title", ""),
        "meta_description": scraped_page.get("meta_description", ""),
    }
