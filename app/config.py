from __future__ import annotations

import os

from dotenv import load_dotenv


load_dotenv()


def get_openai_api_key() -> str:
    return os.getenv("OPENAI_API_KEY", "").strip()


def get_model_name() -> str:
    return os.getenv("MODEL_NAME", "gpt-4.1-mini").strip() or "gpt-4.1-mini"
