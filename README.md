# AI-Powered Website Audit Tool

CLI-based single-page website audit tool built for the EIGHT25 AI-Native Software Engineer assessment.

## Overview

This tool accepts one public webpage URL, extracts deterministic on-page data, computes factual metrics, and then sends grounded structured input to Gemini for AI-generated analysis and recommendations.

The output is intentionally separated into four blocks:

- page info
- factual metrics
- AI analysis
- recommendations

This separation is one of the main design choices in the project: scraping and metric calculation stay deterministic, while the model is used only for interpretation.

## Important

Run everything from the project root directory.

```powershell
cd website-audit-tool
```

## Features

### Factual Metrics

- total word count
- H1, H2, and H3 counts
- CTA count
- internal vs external link counts
- image count
- percentage of images missing alt text
- meta title and meta description

### AI Insights

- SEO structure analysis
- messaging clarity analysis
- CTA usage analysis
- content depth analysis
- UX / structural concerns

### Recommendations

- prioritized recommendations
- structured AI output
- graceful fallback when AI quota or API access is unavailable

## Setup

Create and activate a virtual environment, then install dependencies:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Create a local `.env` file:

```env
GEMINI_API_KEY=your_real_key
MODEL_NAME=gemini-2.0-flash
```

`.env.example` is included only as a template. Do not commit a real key.

## Run

```powershell
python -m app.main "https://example.com"
```

## Example Output

```text
Website Audit: https://example.com

=== PAGE INFO ===
Page Title: Example Domain
Meta Title: Example Domain
Meta Description:

=== FACTUAL METRICS ===
Word Count: 21
H1 Count: 1
H2 Count: 0
H3 Count: 0
CTA Count: 1
Internal Links: 0
External Links: 1
Images: 0
Missing Alt %: 0.0

=== AI ANALYSIS ===
Model: gemini-2.0-flash
AI analysis unavailable: 429 You exceeded your current quota...

=== RECOMMENDATIONS ===
AI recommendations unavailable.
```

If Gemini quota is available, the AI section returns structured insights and recommendations. If quota is unavailable, the app still returns the factual audit and logs the AI failure cleanly instead of crashing.

## Repository Structure

- `app/`
  Core implementation
- `docs/`
  Architecture, AI design, scope, extraction plan, and trade-offs
- `prompt_logs/`
  Sample and generated prompt logs
- `tests/`
  Minimal deterministic verification

## Project Docs

- [Setup Instructions](docs/setup.md)
- [Project Scope](docs/Implementation_scope.md)
- [Extraction Plan](docs/extraction_plan.md)
- [Architecture](docs/architecture.md)
- [AI Design](docs/ai_design.md)
- [Trade-offs](docs/tradeoffs.md)

## Prompt Logs

Prompt logs are written to `prompt_logs/` and include:

- structured input
- factual metrics
- system prompt
- user prompt
- raw model output

See [sample_run.md](prompt_logs/sample_run.md) for the expected format.

## Testing

Run the minimal deterministic test suite with:

```powershell
python -m pytest -q
```

## What I Would Improve With More Time

- stricter schema validation for AI output
- cleaner fetch configuration instead of the current SSL fallback path
- richer prompt log examples from successful model runs
- stronger handling for provider quota and retry behavior
- more scraper and metrics tests for edge cases
