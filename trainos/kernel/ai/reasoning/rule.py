from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Rule:
    name: str
    condition: str
    conclusion: str
