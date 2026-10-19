# kernel/health/health_report.py

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True, slots=True)
class HealthReport:
    healthy: bool
    checked_services: int
    failed_services: int
    failed_service_names: Tuple[str, ...]
