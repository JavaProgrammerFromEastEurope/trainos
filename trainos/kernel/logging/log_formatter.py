# kernel/logging/log_formatter.py

from __future__ import annotations
from trainos.kernel.logging.log_record import LogRecord


class LogFormatter:

    def format(
        self,
        record: LogRecord,
    ) -> str:

        return (
            f"[{record.timestamp:.3f}] "
            f"[{record.level.name}] "
            f"[{record.source}] "
            f"{record.message}"
        )

