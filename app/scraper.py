from __future__ import annotations

from typing import Any

import requests
from bs4 import BeautifulSoup


def _get_page_title(soup: BeautifulSoup) -> str:
    if soup.title and soup.title.string:
        return soup.title.string.strip()
    return ""


def _get_meta_description(soup: BeautifulSoup) -> str:
    tag = soup.find("meta", attrs={"name": "description"})
    if tag and tag.get("content"):
        return tag["content"].strip()
    return ""


def _get_visible_text(soup: BeautifulSoup) -> str:
    text_soup = BeautifulSoup(str(soup), "html.parser")
    for tag in text_soup(["script", "style", "noscript"]):
        tag.decompose()
    return " ".join(text_soup.get_text(separator=" ").split())


def scrape_page(url: str) -> dict[str, Any]:
    response = requests.get(url, timeout=15)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    page_title = _get_page_title(soup)
    meta_description = _get_meta_description(soup)
    visible_text = _get_visible_text(soup)

    return {
        "url": url,
        "page_title": page_title,
        "meta_title": page_title,
        "meta_description": meta_description,
        "visible_text": visible_text,
    }
