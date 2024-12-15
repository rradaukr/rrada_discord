from __future__ import annotations

import os

def request_resource_text(string_content: str) -> str | None:
    if not os.path.exists(f"resources/{string_content}.txt"): return None
    try:
        with open(f"resources/{string_content}.txt", "r", encoding="utf-8") as f_IO: return f_IO.read(-1)
    except Exception as e:  return None

__all__ = ["request_resource_text"]
