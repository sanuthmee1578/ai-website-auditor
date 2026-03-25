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


def scrape_page(url: str) -> dict[str, Any]:
    response = requests.get(url, timeout=15)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    page_title = _get_page_title(soup)
    meta_description = _get_meta_description(soup)

    return {
        "url": url,
        "page_title": page_title,
        "meta_title": page_title,
        "meta_description": meta_description,
    }
