from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ReasoningResult:
    success: bool
    conclusion: str
