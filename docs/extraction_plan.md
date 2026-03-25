# Extraction Plan

This document defines the scraper layer for the first version of the project. It focuses on what `scraper.py` is responsible for, what it must return, and what it must not do.

## Scraper Responsibilities

The scraper is the first implementation layer in the pipeline.

It should accept one public URL, fetch the HTML for that page, parse the document, and return raw structured page data.

Its responsibilities are limited to:

- requesting the page content
- parsing the HTML
- extracting page metadata
- extracting visible text
- extracting headings
- extracting links
- extracting images
- extracting CTA candidates

The scraper should keep its output raw and descriptive. It should represent what is present on the page without trying to interpret quality or compute summary metrics.

The scraper should not:

- calculate counts or percentages
- classify links as internal or external in the final metrics sense
- generate insights or recommendations
- call the AI model

Its only job is to produce clean raw page data for the next layer.

## Extraction Rules

The scraper should use simple, explainable extraction rules that are easy to defend in an assessment setting.

### Page Metadata

The scraper should extract:

- the requested URL
- the page title from the `<title>` tag
- the meta title
- the meta description

If a field is missing, the scraper should return an empty value consistently rather than inventing one.

### Visible Text

The scraper should extract visible page text from the main HTML content while excluding obvious non-content elements such as:

- `<script>`
- `<style>`
- `<noscript>`

The result should be cleaned into readable plain text so it can later be used for word counting and AI input.

### Headings

The scraper should collect heading text separately for:

- `h1`
- `h2`
- `h3`

The headings should be returned as raw text lists rather than pre-counted values.

### Links

The scraper should collect links as raw extracted items, including:

- visible link text
- href value

Links should not yet be classified as internal or external in this stage.

### Images

The scraper should collect images as raw extracted items, including:

- image source
- alt text

Missing alt text should remain a raw missing value at this stage rather than being converted into a percentage here.

### CTA Candidates

The scraper should collect CTA candidates from:

- button text
- link text that appears action-oriented
- links whose href suggests a primary action, such as contact, demo, pricing, signup, or booking paths

CTA detection does not need to be perfect. It needs to be reasonable, explainable, and consistent.
