import os
from pathlib import Path
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent
ENV_PATH = PROJECT_ROOT / ".env"

load_dotenv(dotenv_path=ENV_PATH)


class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "").strip()
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini").strip()
    TEMPERATURE = 0.2
    MAX_ITERATIONS = 3
    PREVIEW_ROWS = 5