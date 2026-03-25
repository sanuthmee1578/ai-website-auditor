from __future__ import annotations

import sys

from app.ai import analyze_page
from app.metrics import calculate_metrics
from app.scraper import scrape_page


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python -m app.main <url>")
        return 1

    url = sys.argv[1]
    scraped_page = scrape_page(url)
    metrics = calculate_metrics(scraped_page)
    ai_result = analyze_page(scraped_page, metrics)
    analysis = ai_result.get("analysis", {})
    recommendations = analysis.get("recommendations", [])

    print(f"Website Audit: {url}")
    print()
    print("=== PAGE INFO ===")
    print(f"Page Title: {scraped_page.get('page_title', '')}")
    print(f"Meta Title: {scraped_page.get('meta_title', '')}")
    print(f"Meta Description: {scraped_page.get('meta_description', '')}")
    print()
    print("=== FACTUAL METRICS ===")
    print(f"Word Count: {metrics.get('word_count', 0)}")
    print(f"H1 Count: {metrics.get('h1_count', 0)}")
    print(f"H2 Count: {metrics.get('h2_count', 0)}")
    print(f"H3 Count: {metrics.get('h3_count', 0)}")
    print(f"CTA Count: {metrics.get('cta_count', 0)}")
    print(f"Internal Links: {metrics.get('internal_link_count', 0)}")
    print(f"External Links: {metrics.get('external_link_count', 0)}")
    print(f"Images: {metrics.get('image_count', 0)}")
    print(f"Missing Alt %: {metrics.get('missing_alt_percentage', 0.0)}")
    print()
    print("=== AI ANALYSIS ===")
    print(f"SEO Structure: {analysis.get('seo_structure', {}).get('insight', '')}")
    print(
        f"Messaging Clarity: {analysis.get('messaging_clarity', {}).get('insight', '')}"
    )
    print(f"CTA Usage: {analysis.get('cta_usage', {}).get('insight', '')}")
    print(f"Content Depth: {analysis.get('content_depth', {}).get('insight', '')}")
    print(
        "UX / Structural Concerns: "
        f"{analysis.get('ux_structural_concerns', {}).get('insight', '')}"
    )
    print()
    print("=== RECOMMENDATIONS ===")
    for item in recommendations:
        print(
            f"{item.get('priority', '')}. {item.get('title', '')} - "
            f"{item.get('action', '')}"
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
