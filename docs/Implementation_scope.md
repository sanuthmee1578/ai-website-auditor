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
