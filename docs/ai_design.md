# AI Design

This document defines the AI layer for the first version of the project. It focuses on how the model should be used, what structured input it should receive, and what structured output it must return.

## AI Output Shape

The AI layer should return structured analysis rather than free-form prose.

The first version should produce a JSON-like structure with these top-level sections:

- `seo_structure`
- `messaging_clarity`
- `cta_usage`
- `content_depth`
- `ux_structural_concerns`
- `recommendations`

Each insight section should contain:

- `score`
- `insight`
- `metric_ref`

The `recommendations` section should contain 3 to 5 items. Each recommendation should include:

- `priority`
- `title`
- `reasoning`
- `action`
- `metric_ref`
- `expected_outcome`

This structure is intentionally explicit so the AI output can be validated, logged, and rendered cleanly in the CLI later.

## AI Input Payload

The AI layer should receive a focused structured payload built from the scraper output and the metrics output.

The first version should provide:

- `url`
- `page_title`
- `meta_title`
- `meta_description`
- `h1_texts`
- `h2_texts`
- `h3_texts`
- `cta_candidates`
- a short `content_snippet`
- the factual metrics block

The AI layer should not receive raw HTML.

This keeps the model grounded in extracted facts while keeping the prompt small enough to remain understandable and easy to debug.

## Prompt Rules

The prompt should instruct the model to behave within clear boundaries.

The first version should require the model to:

- use only the provided structured data
- avoid generic website advice
- ground each insight in actual extracted metrics or content
- keep the analysis concise and practical
- return structured output only
- produce 3 to 5 prioritized recommendations

The prompt should discourage the model from inventing facts that were never extracted by the scraper or computed by the metrics layer.

This is important because the assessment values grounded AI analysis, not broad or speculative commentary.

## Current Implementation Notes

The current implementation builds:

- a fixed system prompt
- a structured AI input payload
- a user prompt that embeds the structured input
- an explicit expected output shape

The model is instructed to analyze a single webpage using only the extracted content and factual metrics already computed in Python.

If the Gemini call fails because of quota or API issues, the application now returns a structured fallback message rather than crashing.
