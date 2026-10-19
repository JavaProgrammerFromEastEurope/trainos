from __future__ import annotations

from dataclasses import dataclass


@dataclass
class GoalResult:
    success: 	bool
    reason: 	str = ""