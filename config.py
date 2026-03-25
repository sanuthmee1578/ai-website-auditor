from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv


PROJECT_ROOT = Path(__file__).resolve().parent.parent
ENV_PATH = PROJECT_ROOT / ".env"

load_dotenv(dotenv_path=ENV_PATH)


def get_gemini_api_key() -> str:
    return os.getenv("GEMINI_API_KEY", "").strip()


def get_model_name() -> str:
    return (
        os.getenv("MODEL_NAME", "gemini-2.5-flash-lite").strip()
        or "gemini-2.5-flash-lite"
    )
