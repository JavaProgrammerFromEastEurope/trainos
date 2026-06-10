# kernel/logging/logger.py

from __future__ 	import annotations
from collections 	import deque
from trainos.kernel.logging.log_level import LogLevel
from trainos.kernel.logging.log_record import LogRecord


class Logger:

    def __init__(
        self,
        level: LogLevel = LogLevel.INFO,
        max_records: int = 10000,
    ) -> None:

        self._level = level
        self._records: deque[LogRecord] = deque(
            maxlen=max_records,
        )

    @property
    def level(self) -> LogLevel:
        return self._level

    def set_level(
        self,
        level: LogLevel,
    ) -> None:

        self._level = level

    def debug(
        self,
        source: str,
        message: str,
        timestamp: float,
    ) -> None:

        self.log(
            level=LogLevel.DEBUG,
            source=source,
            message=message,
            timestamp=timestamp,
        )

    def info(
        self,
        source: str,
        message: str,
        timestamp: float,
    ) -> None:

        self.log(
            level=LogLevel.INFO,
            source=source,
            message=message,
            timestamp=timestamp,
        )

    def warning(
        self,
        source: str,
        message: str,
        timestamp: float,
    ) -> None:

        self.log(
            level=LogLevel.WARNING,
            source=source,
            message=message,
            timestamp=timestamp,
        )

    def error(
        self,
        source: str,
        message: str,
        timestamp: float,
    ) -> None:

        self.log(
            level=LogLevel.ERROR,
            source=source,
            message=message,
            timestamp=timestamp,
        )

    def critical(
        self,
        source: str,
        message: str,
        timestamp: float,
    ) -> None:

        self.log(
            level=LogLevel.CRITICAL,
            source=source,
            message=message,
            timestamp=timestamp,
        )

    def log(
        self,
        level: LogLevel,
        source: str,
        message: str,
        timestamp: float,
    ) -> None:

        if level < self._level:
            return

        self._records.append(
            LogRecord(
                timestamp=timestamp,
                level=level,
                source=source,
                message=message,
            )
        )

    def records(self) -> list[LogRecord]:
        return list(self._records)

    def clear(self) -> None:
        self._records.clear()
