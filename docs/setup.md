# Setup Instructions

This file explains how to set up and run the Website Audit Tool from a fresh local environment.

## Prerequisites

Make sure the following are available on your machine:

- Python 3.11 or newer
- PowerShell or a terminal with Python available on `PATH`
- A Gemini API key for the AI analysis step

## 1. Open the Project Root

Run all commands from the repository root:

```powershell
cd website-audit-tool
```

## 2. Create a Virtual Environment

```powershell
python -m venv venv
```

## 3. Activate the Virtual Environment

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run:

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\venv\Scripts\Activate.ps1
```

## 4. Install Dependencies

```powershell
python -m pip install -r requirements.txt
```

## 5. Configure Environment Variables

Create a local `.env` file in the project root.

Use this format:

```env
GEMINI_API_KEY=your_real_key_here
MODEL_NAME=gemini-2.0-flash
```

Notes:

- `.env.example` is only a template
- do not place a real API key in `.env.example`
- do not commit `.env`

## 6. Run the Tool

```powershell
python -m app.main "https://example.com"
```

## 7. Run Tests

```powershell
python -m pytest -q
```

## Expected Output

The CLI prints:

- page info
- factual metrics
- AI analysis
- recommendations

If the Gemini API is unavailable or quota is exhausted, the tool still prints the factual audit and shows a clear AI fallback message instead of crashing.

## Prompt Logs

Each run writes a prompt log to `prompt_logs/`.

The log includes:

- structured input
- factual metrics
- system prompt
- user prompt
- raw model output

## Troubleshooting

### Python Is Not Recognized

Install Python and make sure it is available on `PATH`, then restart the terminal.

### `.env` Is Not Being Picked Up

Make sure:

- the file is named `.env`
- it is saved in the project root
- the variable name is `GEMINI_API_KEY`

You can verify loading with:

```powershell
python -c "import app.config; print(bool(app.config.get_gemini_api_key()))"
```

### SSL Certificate Errors During Scraping

The scraper currently includes an SSL fallback for local environments where certificate verification fails. This was added to keep the assessment submission runnable on machines with local trust issues.

### Gemini Quota Errors

If you see a quota or rate-limit error from Gemini:

- confirm the API key is valid
- confirm the project has access to the chosen model
- confirm quota is available
- retry later if the provider suggests a retry delay

The application will continue to show factual metrics even if AI analysis is unavailable.
