# Sample Prompt Log

This file shows the structure of the prompt logging output written by the tool.

## Run Info

- URL: https://example.com
- Model: gemini-2.0-flash

## Structured Input

```json
{
  "url": "https://example.com",
  "page_title": "Example Domain",
  "meta_title": "Example Domain",
  "meta_description": "",
  "h1_texts": ["Example Domain"],
  "h2_texts": [],
  "h3_texts": [],
  "cta_candidates": [
    {
      "text": "Learn more",
      "href": "https://iana.org/domains/example",
      "source_type": "link"
    }
  ],
  "content_snippet": "Example Domain Example Domain This domain is for use in documentation examples without needing permission. Avoid use in operations. Learn more",
  "metrics": {
    "word_count": 21,
    "h1_count": 1,
    "h2_count": 0,
    "h3_count": 0,
    "cta_count": 1,
    "internal_link_count": 0,
    "external_link_count": 1,
    "image_count": 0,
    "missing_alt_percentage": 0.0,
    "meta_title": "Example Domain",
    "meta_description": ""
  }
}
```

## System Prompt

```text
You are a senior website strategist reviewing a single webpage.
Use only the provided extracted data and metrics.
Avoid generic advice.
Ground all insights in the supplied content and metrics.
Return structured analysis only.
```

## Raw Model Output

```json
{
  "seo_structure": {
    "score": 0,
    "insight": "AI analysis unavailable: quota exceeded or model access failed.",
    "metric_ref": ""
  }
}
```
