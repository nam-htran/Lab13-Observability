import os

from dotenv import load_dotenv

load_dotenv()

if not os.getenv("LANGFUSE_HOST") and os.getenv("LANGFUSE_BASE_URL"):
    os.environ["LANGFUSE_HOST"] = os.environ["LANGFUSE_BASE_URL"]

__all__ = []
