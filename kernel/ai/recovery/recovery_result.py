from __future__ import annotations

from dataclasses import dataclass


@dataclass
class RecoveryResult:
    recovered: 		bool
    rolled_back: 	bool
    retry_count: 	int