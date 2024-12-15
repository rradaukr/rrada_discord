from __future__ import annotations

DOTENV_PATH: str = ".env"
from dotenv import load_dotenv; load_dotenv(DOTENV_PATH, "r", encoding="utf-8")
from os import environ

from dataclasses import dataclass
@dataclass
class Configuration:
    assert (TOKEN := environ.get("TOKEN")) is not None, "TOKEN is not set"
    assert (OWNER_ID := environ.get("OWNER_ID")) is not None, "OWNER_ID is not set"

__all__ = ["DOTENV_PATH", "Configuration"]
