from __future__ import annotations

import json
import sys
from datetime import datetime
from pathlib import Path

from app.ai import analyze_page
from app.config import get_gemini_api_key, get_model_name
from app.metrics import calculate_metrics
from app.scraper import scrape_page


def write_prompt_log(
    url: str,
    model_name: str,
    scraped_page: dict,
    metrics: dict,
    ai_result: dict,
) -> Path:
    prompt_log_dir = Path("prompt_logs")
    prompt_log_dir.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_path = prompt_log_dir / f"run_{timestamp}.md"

    body = f"""# Prompt Log

## Run Info

- URL: {url}
- Model: {model_name}
- Timestamp: {timestamp}

## Structured Input

```json
{json.dumps(ai_result.get("ai_input", {}), indent=2)}
```

## Factual Metrics

```json
{json.dumps(metrics, indent=2)}
```

## System Prompt

```text
{ai_result.get("prompt_package", {}).get("system_prompt", "")}
```

## User Prompt

```text
{ai_result.get("prompt_package", {}).get("user_prompt", "")}
```

## Raw Model Output

```json
{ai_result.get("raw_output", "")}
```

## Scraped Page Snapshot

```json
{json.dumps(scraped_page, indent=2)}
```
"""
    log_path.write_text(body, encoding="utf-8")
    return log_path


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python -m app.main <url>")
        return 1

    api_key = get_gemini_api_key()
    model_name = get_model_name()

    if not api_key:
        print("Missing GEMINI_API_KEY in .env. Add it before running the AI analysis.")
        return 1

    url = sys.argv[1]
    scraped_page = scrape_page(url)
    metrics = calculate_metrics(scraped_page)
    ai_result = analyze_page(scraped_page, metrics, api_key=api_key, model_name=model_name)
    analysis = ai_result.get("analysis", {})
    recommendations = analysis.get("recommendations", [])
    ai_message = analysis.get("seo_structure", {}).get("insight", "")
    log_path = write_prompt_log(url, model_name, scraped_page, metrics, ai_result)

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
    print(f"Prompt Log: {log_path}")
    print()
    print("=== AI ANALYSIS ===")
    print(f"Model: {model_name}")
    if ai_message.startswith("AI analysis unavailable:"):
        print(ai_message)
        print()
        print("=== RECOMMENDATIONS ===")
        print("AI recommendations unavailable.")
        return 0

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
