from pathlib import Path

from bs4 import BeautifulSoup

from app.metrics import calculate_metrics
from app.scraper import (
    _get_cta_candidates,
    _get_heading_texts,
    _get_images,
    _get_links,
    _get_meta_description,
    _get_page_title,
    _get_visible_text,
)


def test_calculate_metrics_from_fixture():
    fixture_path = Path("tests/fixtures/sample_page.html")
    html = fixture_path.read_text(encoding="utf-8")
    soup = BeautifulSoup(html, "html.parser")

    scraped = {
        "url": "https://example.com",
        "page_title": _get_page_title(soup),
        "meta_title": _get_page_title(soup),
        "meta_description": _get_meta_description(soup),
        "visible_text": _get_visible_text(soup),
        "h1_texts": _get_heading_texts(soup, "h1"),
        "h2_texts": _get_heading_texts(soup, "h2"),
        "h3_texts": _get_heading_texts(soup, "h3"),
        "links": _get_links(soup),
        "images": _get_images(soup),
        "cta_candidates": _get_cta_candidates(soup),
    }

    metrics = calculate_metrics(scraped)

    assert metrics["h1_count"] == 1
    assert metrics["h2_count"] == 1
    assert metrics["h3_count"] == 1
    assert metrics["cta_count"] == 2
    assert metrics["internal_link_count"] == 1
    assert metrics["external_link_count"] == 1
    assert metrics["image_count"] == 2
    assert metrics["missing_alt_percentage"] == 50.0
