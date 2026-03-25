from __future__ import annotations

from typing import Any

import requests
from bs4 import BeautifulSoup
from requests import Response
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning


CTA_TEXT_KEYWORDS = (
    "contact",
    "get started",
    "book",
    "schedule",
    "call",
    "buy",
    "sign up",
    "learn more",
    "request",
    "start",
)

CTA_HREF_KEYWORDS = (
    "/contact",
    "/demo",
    "/pricing",
    "/signup",
    "/book",
    "#contact",
)


disable_warnings(InsecureRequestWarning)


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


def _get_heading_texts(soup: BeautifulSoup, tag_name: str) -> list[str]:
    headings: list[str] = []
    for tag in soup.find_all(tag_name):
        text = tag.get_text(separator=" ", strip=True)
        if text:
            headings.append(text)
    return headings


def _get_links(soup: BeautifulSoup) -> list[dict[str, str]]:
    links: list[dict[str, str]] = []
    for tag in soup.find_all("a", href=True):
        href = tag["href"].strip()
        text = tag.get_text(separator=" ", strip=True)
        if href:
            links.append({"text": text, "href": href})
    return links


def _get_images(soup: BeautifulSoup) -> list[dict[str, str]]:
    images: list[dict[str, str]] = []
    for tag in soup.find_all("img"):
        src = tag.get("src", "").strip()
        alt = tag.get("alt", "").strip()
        images.append({"src": src, "alt": alt})
    return images


def _get_cta_candidates(soup: BeautifulSoup) -> list[dict[str, str]]:
    cta_candidates: list[dict[str, str]] = []

    for tag in soup.find_all("button"):
        text = tag.get_text(separator=" ", strip=True)
        if text:
            cta_candidates.append(
                {"text": text, "href": "", "source_type": "button"}
            )

    for tag in soup.find_all("a", href=True):
        href = tag["href"].strip()
        text = tag.get_text(separator=" ", strip=True)
        text_lower = text.lower()
        href_lower = href.lower()

        matches_text = any(keyword in text_lower for keyword in CTA_TEXT_KEYWORDS)
        matches_href = any(keyword in href_lower for keyword in CTA_HREF_KEYWORDS)

        if matches_text or matches_href:
            cta_candidates.append(
                {"text": text, "href": href, "source_type": "link"}
            )

    return cta_candidates


def _fetch_page(url: str) -> Response:
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        return response
    except requests.exceptions.SSLError:
        response = requests.get(url, timeout=15, verify=False)
        response.raise_for_status()
        return response


def scrape_page(url: str) -> dict[str, Any]:
    response = _fetch_page(url)

    soup = BeautifulSoup(response.text, "html.parser")
    page_title = _get_page_title(soup)
    meta_description = _get_meta_description(soup)
    visible_text = _get_visible_text(soup)
    h1_texts = _get_heading_texts(soup, "h1")
    h2_texts = _get_heading_texts(soup, "h2")
    h3_texts = _get_heading_texts(soup, "h3")
    links = _get_links(soup)
    images = _get_images(soup)
    cta_candidates = _get_cta_candidates(soup)

    return {
        "url": url,
        "page_title": page_title,
        "meta_title": page_title,
        "meta_description": meta_description,
        "visible_text": visible_text,
        "h1_texts": h1_texts,
        "h2_texts": h2_texts,
        "h3_texts": h3_texts,
        "links": links,
        "images": images,
        "cta_candidates": cta_candidates,
    }
