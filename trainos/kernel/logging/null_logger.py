# kernel/logging/null_logger.py

from __future__ import annotations


class NullLogger:

    def debug(
        self,
        *args,
        **kwargs,
    ) -> None:
        pass

    def info(
        self,
        *args,
        **kwargs,
    ) -> None:
        pass

    def warning(
        self,
        *args,
        **kwargs,
    ) -> None:
        pass

    def error(
        self,
        *args,
        **kwargs,
    ) -> None:
        pass

    def critical(
        self,
        *args,
        **kwargs,
    ) -> None:
        pass
