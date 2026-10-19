from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ReflectionResult:
    success: bool
    summary: str
