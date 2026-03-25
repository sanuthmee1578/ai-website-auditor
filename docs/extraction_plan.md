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
