# Architecture

## Overview

The tool follows a simple linear pipeline:

1. `main.py` receives a single URL from the CLI
2. `scraper.py` fetches and parses the page
3. `metrics.py` computes deterministic factual metrics
4. `ai.py` builds a structured prompt and calls Gemini
5. `main.py` prints the final result and writes a prompt log

## Separation of Responsibilities

- `scraper.py`
  Extracts raw page data only
- `metrics.py`
  Computes factual metrics only
- `ai.py`
  Builds AI input, prompt payload, and model analysis
- `main.py`
  Orchestrates the flow and prints the final CLI output

This separation is the main architectural principle of the project. Deterministic extraction and metric computation are kept separate from AI-generated analysis.

## Current Data Flow

`URL -> scraped page data -> factual metrics -> AI input payload -> AI output -> CLI output + prompt log`

## Output Structure

The CLI prints four sections:

- page info
- factual metrics
- AI analysis
- recommendations

This keeps extracted facts separate from model-generated commentary.
