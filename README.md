# AI-Native Website Audit Tool

CLI-based single-page website audit tool built for the EIGHT25MEDIA internship assessment.

## What It Does

The tool accepts one public webpage URL, extracts deterministic on-page data, computes factual metrics, and then sends grounded structured input to Gemini for AI-generated analysis and recommendations.

The output is intentionally separated into:

- page info
- factual metrics
- AI analysis
- recommendations

## Current Features

- page metadata extraction
- visible text extraction
- heading extraction
- raw link, image, and CTA extraction
- deterministic metrics for headings, links, images, and alt text
- Gemini prompt construction and analysis call
- graceful fallback when AI quota or API access fails
- prompt log generation
- one deterministic fixture-based test

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
```

If Gemini quota is unavailable, the tool still prints factual metrics and shows a clear AI fallback message instead of crashing.

## Project Docs

- [Project Scope](docs/Implementation_scope.md)
- [Extraction Plan](docs/extraction_plan.md)
- [Architecture](docs/architecture.md)
- [AI Design](docs/ai_design.md)
- [Trade-offs](docs/tradeoffs.md)

## Prompt Logs

Prompt logs are written to `prompt_logs/` for each run and include:

- structured input
- factual metrics
- system prompt
- user prompt
- raw model output

## What I Would Improve With More Time

- better schema validation for AI output
- cleaner fetch configuration instead of the local SSL fallback path
- stronger prompt logging examples from successful model runs
- better error handling around provider rate limits
- more tests for scraper and metrics edge cases
