# kernel/logging/log_record.py

from __future__ import annotations
from dataclasses import dataclass
from trainos.kernel.logging.log_level import LogLevel


@dataclass(slots=True)
class LogRecord:
    timestamp: float
    level: LogLevel
    source: str
    message: str
