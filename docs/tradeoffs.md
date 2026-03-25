# Trade-offs

## Key Choices

### CLI Instead of Web UI

The project uses a CLI because the assessment values the core workflow more than interface polish. This keeps the submission focused and faster to build.

### Deterministic Metrics Before AI

Word count, heading counts, link counts, image count, and missing alt percentage are computed in Python before the AI layer runs. This keeps the model grounded and reduces generic output.

### Single-Page Scope

The tool analyzes one URL at a time. This matches the assessment scope and avoids unnecessary complexity like crawling, deduplication, or robots handling.

### Raw Extraction First, Interpretation Later

The scraper returns raw fields such as headings, links, images, and CTA candidates. Metrics and AI interpretation happen later. This makes the code easier to explain and test.

### Gemini with Graceful Fallback

The current AI integration uses Gemini because that is the available provider in the local environment. Since provider quota can fail, the tool now falls back gracefully and still produces the factual audit.

## Current Limitations

- no multi-page crawling
- no authenticated page support
- no browser-based rendering for JavaScript-heavy pages
- AI output is not yet strongly validated against a strict schema
- live AI output depends on Gemini quota availability
