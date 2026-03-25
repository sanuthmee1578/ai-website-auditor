# Project Scope

This document defines the fixed implementation boundaries for the internship assessment repository. Its purpose is to keep the project focused, prevent unnecessary expansion, and make later engineering decisions consistent.

## Project Definition

The final product is a CLI-based single-page website audit tool.

The tool accepts one URL, extracts factual on-page information, computes deterministic metrics, and then uses those grounded inputs to generate structured AI insights and prioritized recommendations.

## Input

- A single public webpage URL

## Output

The final CLI output must keep deterministic data and AI-generated analysis clearly separate.
AI insights and recommendations will be returned in a structured format (JSON internally) before being formatted for CLI display.

### Block 1: Page Info

- URL
- page title
- meta title
- meta description

### Block 2: Factual Metrics

- total word count
- H1 count
- H2 count
- H3 count
- CTA count
- internal link count
- external link count
- image count
- missing alt percentage

### Block 3: AI Insights

- SEO structure
- messaging clarity
- CTA usage
- content depth
- UX or structural concerns

### Block 4: Recommendations

- 3 to 5 prioritized recommendations

## Fixed Scope Boundaries

The first version of this project will include:

- single-page analysis only
- CLI output only
- deterministic scraping and metric extraction
- structured AI analysis grounded in extracted data
- one prompt log sample
- minimal deterministic tests

The first version of this project will not include:

- multi-page crawling
- authenticated or logged-in pages
- a deployed web UI
- page-speed or Core Web Vitals analysis
- visual screenshot analysis
- advanced browser automation unless it becomes necessary later

## Core Design Rule

The project will follow a strict separation of concerns:

- `scraper.py` extracts raw page data
- `metrics.py` computes deterministic factual metrics
- `ai.py` analyzes the extracted data and metrics
- `main.py` orchestrates the flow and presents the result

This separation is fixed for the implementation because the assessment explicitly values clean boundaries between scraping and AI analysis.

## Scraper Output Contract

The scraper layer is responsible only for raw extraction from a single webpage. It should return structured page data that can later be used by the metrics layer and the AI layer.

The scraper output should include:

- `url`
- `page_title`
- `meta_title`
- `meta_description`
- `visible_text`
- `h1_texts`
- `h2_texts`
- `h3_texts`
- `links` with visible text and href
- `images` with src and alt
- `cta_candidates` detected from buttons and likely action links

This contract is intentionally raw. It should describe what exists on the page, not what those values mean.

The scraper layer should not compute:

- total word count
- heading counts
- internal or external link counts
- missing alt percentage
- recommendation logic
- AI insights

Those belong to later layers in the pipeline.

## Metrics Output Contract

The metrics layer is responsible for taking raw scraped page data and converting it into deterministic factual outputs.

The metrics output should include:

- `word_count`
- `h1_count`
- `h2_count`
- `h3_count`
- `cta_count`
- `internal_link_count`
- `external_link_count`
- `image_count`
- `missing_alt_percentage`
- `meta_title`
- `meta_description`

These values should be computed directly from the scraper output using clear, explainable rules.

The metrics layer should not:

- fetch or parse HTML
- generate recommendations
- write qualitative judgments
- produce AI analysis

Its job is to turn extracted page content into a reliable factual summary that can be shown directly to the user and passed into the AI layer as grounded input.

Additional derived metrics may be added later, but the fields above define the required baseline for the first implementation.

## AI Input Contract

The AI layer should not receive raw HTML. It should receive a focused, structured input built from the scraper output and the metrics output.

The AI input should include:

- `url`
- `page_title`
- `meta_title`
- `meta_description`
- `h1_texts`
- `h2_texts`
- `h3_texts`
- `cta_candidates`
- a short visible content snippet
- the full factual metrics block

This input is designed to give the model enough context to reason about the page while keeping the prompt focused, explainable, and easy to debug.

The AI layer should use this structured input to produce:

- SEO structure observations
- messaging clarity observations
- CTA usage observations
- content depth observations
- UX or structural concerns
- 3 to 5 prioritized recommendations

The AI layer should not be responsible for discovering page facts that were never extracted or computed earlier in the pipeline.

## Data Flow Summary

The implementation will follow this fixed handoff:

1. `scraper.py` returns raw page data.
2. `metrics.py` converts that raw data into deterministic factual metrics.
3. `ai.py` receives the raw page context plus the computed metrics and returns structured analysis and recommendations.
4. `main.py` coordinates the pipeline and presents the final output in clearly separated sections.

This flow is locked for the first version of the project so that each layer has a single responsibility and the final output remains easy to explain.

## Implementation Principle

The goal is not to build a large product.

The goal is to build a focused, explainable tool that demonstrates:

- clear separation between deterministic logic and AI reasoning
- grounded AI outputs
- structured outputs
- practical engineering judgment

Any implementation decision that makes the repo bigger without improving those goals should be rejected.

## Project Summary

The project can be described in one sentence as follows:

This tool takes one webpage URL, extracts factual on-page metrics, and uses those grounded metrics plus page content to generate structured AI insights and prioritized recommendations.

## Locked Decisions

- The product remains CLI-based.
- The scope remains single-page only.
- Factual metrics and AI insights must be clearly separated in the output.
- Deterministic metrics must be computed in code, not invented by the model.
- The AI layer will consume structured extracted data rather than raw HTML.
- The repo will stay lightweight and will not be expanded into a full application unless the assessment requires it.
