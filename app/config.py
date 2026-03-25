from __future__ import annotations

import os

from dotenv import load_dotenv


load_dotenv()


def get_gemini_api_key() -> str:
    return os.getenv("GEMINI_API_KEY", "").strip()


def get_model_name() -> str:
    return os.getenv("MODEL_NAME", "gemini-1.5-flash").strip() or "gemini-1.5-flash"
